const axios = require('axios');
const cheerio = require('cheerio');
const { json } = require('express');
const mysql = require('mysql2/promise'); // Import mysql2 library

const dbConfig = {
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ipo',
};

async function fetchUrlsFromDatabase() {
  try {
    const connection = await mysql.createConnection(dbConfig);
    const [rows] = await connection.query('SELECT link, id FROM ipos');
    await connection.end();

    return rows.map(row => ({
      id: row.id,
      link: row.link,
    }));
  } catch (error) {
    console.error(`Error fetching URLs from the database: ${error.message}`);
    return [];
  }
}


async function details(IPO_URL) {
  try {
    const response = await axios.get(IPO_URL);
    const html = response.data;
    const $ = cheerio.load(html);

    const targetText = $('[data-id="e2b564b"]').text().trim();
    const detailsText = targetText.split(':')[1].trim(); 
    // await insertDetailsIntoDatabase(detailsText);
    return detailsText;
  } catch (error) {
    return { error: `Failed to retrieve the webpage: ${error.message}` };
  }
}

async function PriceBandtable(IPO_URL, id) {
  try {
    const response = await axios.get(IPO_URL);
    const html = response.data;
    const $ = cheerio.load(html);

    const tables = $('table');
    const jsonData = [];

    tables.each((index, table) => {
      const tableName = `Table ${index + 1}`;

      const tableObject = {
        name: tableName,
        data: [],
      };

      $(table).find('tr').each((rowIndex, row) => {
        const rowData = {};
        $(row).find('td, th').each((colIndex, col) => {
          rowData[`col${colIndex + 1}`] = $(col).text().trim();
        });
        tableObject.data.push(rowData);
      });

      jsonData.push(tableObject);
    });
    await insertPriceBandData({data: jsonData[0].data}, id);
    await insertMarketLotData(jsonData[1].data, id);
    await insertTimeline(jsonData[2].data, id);
    await insertRevenueData(jsonData[3].data, id);
    await insertValuation(jsonData[4].data, id);
    // console.log(jsonData[3].data);
    return jsonData;
  } catch (error) {
    return { error: `Error fetching the page: ${error.message}` };
  }
}
async function fetchAllUlAfterHeadings(IPO_URL) {
  try {
    const response = await axios.get(IPO_URL);
    const html = response.data;
    const $ = cheerio.load(html);
    const headingElements = $('h2, h3');
    const results = [];

    headingElements.each((index, headingElement) => {
      const headingText = $(headingElement).text().trim();
      const ulElement = $(headingElement).next('ul');

      if (ulElement.length) {
        const ulObject = {
          heading: headingText,
          items: [],
        };

        ulElement.find('li').each((itemIndex, li) => {
          ulObject.items.push($(li).text().trim());
        });

        results.push(ulObject);
      }
    });

    return results;
  } catch (error) {
    return { error: `Error fetching the page: ${error.message}` };
  }
}

async function getIPOFAQ(IPO_URL) {
  try {
    const response = await axios.get(IPO_URL);
    const html = response.data;
    const $ = cheerio.load(html);

    const faqContainer = $('[itemtype="https://schema.org/FAQPage"]');
    const faqList = [];

    faqContainer.find('[itemtype="https://schema.org/Question"]').each((index, element) => {
      const question = $(element).find('[itemprop="name"]').text().trim();
      const answer = $(element).find('[itemprop="text"]').text().trim();

      faqList.push({ question, answer });
    });
    return faqList;
  } catch (error) {
    return { error: `Error fetching data: ${error.message}` };
  }
}

async function insertDetailsData(data, id) {
  try {
    const connection = await mysql.createConnection(dbConfig);

    // Insert details data
    const [insertDetailsResult] = await connection.query(`
      INSERT INTO details (ipoid, details, object_of_issue, review, firm_review, peer_group, company_promoters, lead_manager)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    `, [
      id,
      data.details,
      JSON.stringify(data.object_of_issue),
      JSON.stringify(data.review),
      JSON.stringify(data.firm_review),
      JSON.stringify(data.peer_group),
      JSON.stringify(data.company_promoters),
      JSON.stringify(data.lead_manager)
    ]);

    console.log(`Inserted details with id ${insertDetailsResult.insertId} into the details table.`);

    // Insert FAQ data
    if (data.getIPOFAQ && data.getIPOFAQ.length > 0) {
      for (const faqItem of data.getIPOFAQ) {
        const [insertFAQResult] = await connection.query(`
          INSERT INTO faq (ipoid, question, answer)
          VALUES (?, ?, ?);
        `, [id, faqItem.question, faqItem.answer]);

        console.log(`Inserted FAQ with id ${insertFAQResult.insertId} into the faq table.`);
      }
    }

    await connection.end();
  } catch (error) {
    console.error(`Error inserting data into the database: ${error.message}`);
  }
}

async function insertPriceBandData(data, id) {
  try {
    const connection = await mysql.createConnection(dbConfig);

    // Insert price_band data
    const [insertPriceBandResult] = await connection.query(`
      INSERT INTO price_band (ipoid, ipo_open, ipo_close, ipo_size, offer_for_sale, face_value, ipo_price_band, ipo_listing_on, retail_quota, qib_quota, nii_quota, drhp_link, rhp_link, anchor_investors_list)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    `, [
      id,
      data.data[0].col2, // IPO Open
      data.data[1].col2, // IPO Close
      data.data[2].col2, // IPO Size
      data.data[3].col2, // Offer for Sale
      data.data[4].col2, // Face Value
      data.data[5].col2, // IPO Price Band
      data.data[6].col2, // IPO Listing on
      data.data[7].col2, // Retail Quota
      data.data[8].col2, // QIB Quota
      data.data[9].col2, // NII Quota
      data.data[10].col2, // DRHP Draft Prospectus
      data.data[11].col2, // RHP Draft Prospectus
      data.data[12].col2 // Anchor Investors List
    ]);

    console.log(`Inserted price_band data with id ${insertPriceBandResult.insertId} into the price_band table.`);

    await connection.end();
  } catch (error) {
    console.error(`Error inserting price_band data into the database: ${error.message}`);
  }
}

async function insertMarketLotData(data) {
  try {
    const connection = await mysql.createConnection(dbConfig);
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      const [insertResult] = await connection.query(`
        INSERT INTO market_lot (ipoid, application, lot_size, shares, amount)
        VALUES (?, ?, ?, ?, ?);
      `, [id, row.col1, row.col2, row.col3, row.col4]);

      console.log(`Inserted market_lot data with id ${insertResult.insertId}`);
    }

    await connection.end();
  } catch (error) {
    console.error(`Error inserting market_lot data into the database: ${error.message}`);
  }
}

async function insertTimeline(data) {
  try {
    const connection = await mysql.createConnection(dbConfig);

    const [insertTimelineResult] = await connection.query(`
      INSERT INTO timeline (ipoid, anchor_investors_allotment, ipo_open_date, ipo_close_date, basis_of_allotment, refunds, credit_to_demat_account, ipo_listing_date)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    `, [
      id,
      data[0].col2, // Anchor Investors Allotment
      data[1].col2, // IPO Open Date
      data[2].col2, // IPO Close Date
      data[3].col2, // Basis of Allotment
      data[4].col2, // Refunds
      data[5].col2, // Credit to Demat Account
      data[6].col2  // IPO Listing Date
    ]);

    console.log(`Inserted timeline data with id ${insertTimelineResult.insertId} into the timeline table.`);
    await connection.end();
  } catch (error) {
    console.error(`Error inserting timeline data into the database: ${error.message}`);
  }
}

async function insertRevenueData(data) {
  try {
    const connection = await mysql.createConnection(dbConfig);

    // Assuming the data array has the required structure
    for (let i = 2; i < data.length; i++) {
      const row = data[i];
      const [insertResult] = await connection.query(`
        INSERT INTO financial_data (ipoid, year, revenue, expense, pat)
        VALUES (?, ?, ?, ?, ?);
      `, [id, row.col1, row.col2, row.col3, row.col4]);

      console.log(`Inserted revenue data with id ${insertResult.insertId}`);
    }

    await connection.end();
  } catch (error) {
    console.error(`Error inserting revenue data into the database: ${error.message}`);
  }
}

async function insertValuation(data) {
  try {
    const connection = await mysql.createConnection(dbConfig);

    const [insertValuationResult] = await connection.query(`
      INSERT INTO valuation (ipoid, eps, pe_ratio, ronw, nav)
      VALUES (?, ?, ?, ?, ?);
    `, [
      id,
      data[0].col2 || null, // Earning Per Share (EPS)
      data[1].col2 || null, // Price/Earning P/E Ratio
      data[2].col2 || null, // Return on Net Worth (RoNW)
      data[3].col2 || null, // Net Asset Value (NAV)
    ]);

    console.log(`Inserted insertValuation data with id ${insertValuationResult.insertId} into the valuation table.`);
    await connection.end();
  } catch (error) {
    console.error(`Error inserting insertValuation data into the database: ${error.message}`);
  }
}



async function main() {
  try {
    const results = await fetchUrlsFromDatabase();

    for (const ipo of results) {
      
      IPO_URL = ipo.link == null ? null :  `https://ipowatch.in${ipo.link}`;
      id = ipo.id;

      try {
        const detailsResult = await details(IPO_URL);
        const priceBandResult = await PriceBandtable(IPO_URL, id);
        const ulAfterHeadingsResult = await fetchAllUlAfterHeadings(IPO_URL);
        const faqResult = await getIPOFAQ(IPO_URL);

        const organizedData = {
          details: detailsResult,
          object_of_issue: ulAfterHeadingsResult[0].items,
          review: ulAfterHeadingsResult[1].items,
          firm_review: ulAfterHeadingsResult[2].items,
          peer_group: ulAfterHeadingsResult[3].items,
          company_promoters: ulAfterHeadingsResult[4].items,
          lead_manager: ulAfterHeadingsResult[5].items,
          getIPOFAQ: faqResult,
        };

        await insertDetailsData(organizedData, id);
        console.log("Data inserted successfully.");
      } 
      catch (error) {
        if (error.message.includes("Cannot read properties of undefined (reading 'items')")) {
          console.error(`Error: Page not found for ${IPO_URL}`);
        } else {
          console.error(`An error occurred: ${error.message}`);
        }
      }
    }
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

main();
