const axios = require('axios');
const cheerio = require('cheerio');
const mysql = require('mysql2/promise');

async function scrapeIPOData() {
  try {
    const response = await axios.get('https://ipowatch.in/upcoming-sme-ipo-calendar-list/');
    const html = response.data;

    const $ = cheerio.load(html);

    const tableData = [];

    // Iterate over each row in the table
    $('table tbody tr').each((index, element) => {
      const rowData = {};

      // Iterate over each column in the row
      $(element).find('td').each((i, td) => {
        // Check if the current column contains an anchor
        const anchor = $(td).find('a');
        if (anchor.length > 0) {
          // If an anchor is found, extract both the text content and the href attribute
          const anchorText = anchor.text().trim();
          const anchorLink = anchor.attr('href').trim();

          // Add text content to the column key and link to the corresponding link key
          rowData['link'] = anchorLink;

          rowData[`Column_${i + 1}`] = anchorText;

          // Assign the href to the 'link' variable
        } else {
          // If no anchor is found, just add the text content of the column
          rowData[`Column_${i + 1}`] = $(td).text().trim();
        }
      });

      // Add the rowData object to the tableData array
      tableData.push(rowData);
    });

    // Output the extracted table data
    console.log(tableData.slice(1));

    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: '',
      database: 'ipo',
    });

    // Check if the table exists
      // Table does not exist, create it
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
      console.log('Table sme created.');

    // Define the SQL query to insert data into the table
    const insertDataQuery = `
      INSERT INTO sme (name, Dates, Price, Platform, link)
      VALUES (?, ?, ?, ?, ?);
    `;

    // Loop through the scraped data and insert into the table
    for (const rowData of tableData.slice(1)) {
      const { Column_1, Column_2, Column_3, Column_4, link } = rowData;
      await connection.execute(insertDataQuery, [Column_1, Column_2, Column_3, Column_4, link]);
    }

    console.log('Data inserted into the table successfully.');

    // Close the database connection
    await connection.end();

  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the function to initiate the scraping
scrapeIPOData();
