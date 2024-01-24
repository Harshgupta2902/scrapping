const axios = require('axios');
const cheerio = require('cheerio');
const mysql = require('mysql2/promise');

async function scrapeIPOData() {
  try {
    const response = await axios.get('https://ipowatch.in/upcoming-sme-ipo-calendar-list/');
    const html = response.data;

    const $ = cheerio.load(html);

    const tableData = [];
    $('table tbody tr').each((index, element) => {
      const rowData = {};
      $(element).find('td').each((i, td) => {
        const anchor = $(td).find('a');
        if (anchor.length > 0) {
          const anchorText = anchor.text().trim();
          const anchorLink = anchor.attr('href').trim();
          rowData['link'] = anchorLink;
          rowData[`Column_${i + 1}`] = anchorText;
        } else {
          rowData[`Column_${i + 1}`] = $(td).text().trim();
        }
      });
      tableData.push(rowData);
    });
    console.log(tableData.slice(1));
    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: '',
      database: 'ipo',
    });

      const createTableQuery = `
        CREATE TABLE IF NOT EXISTS sme (
          id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(255),
          Dates VARCHAR(255),
          Price VARCHAR(255),
          Platform VARCHAR(255),
          link VARCHAR(255)
        );
      `;
      await connection.execute(createTableQuery);
      await connection.query('TRUNCATE TABLE sme;');
      console.log('Table sme created.');

    const insertDataQuery = `
      INSERT INTO sme (name, Dates, Price, Platform, link)
      VALUES (?, ?, ?, ?, ?);
    `;
    for (const rowData of tableData.slice(1)) {
      const { Column_1, Column_2, Column_3, Column_4, link } = rowData;
      await connection.execute(insertDataQuery, [Column_1, Column_2, Column_3, Column_4, link]);
    }

    console.log('Data inserted into the table successfully.');
    await connection.end();

  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the function to initiate the scraping
scrapeIPOData();
