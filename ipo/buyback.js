const axios = require('axios');
const cheerio = require('cheerio');
const mysql = require('mysql2/promise'); // Make sure to install mysql2

const url = 'https://ipowatch.in/share-buyback-offers/';

// Database configuration
const dbConfig = {
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ipo',
};

// Function to create table and insert data into the database
async function createTableAndInsertData(rows) {
  const connection = await mysql.createConnection(dbConfig);

  try {
    // Create the table if it doesn't exist
    await connection.execute(`
      CREATE TABLE IF NOT EXISTS buyback (
        id INT AUTO_INCREMENT PRIMARY KEY,
        company_name VARCHAR(255),
        record_date VARCHAR(255),
        open VARCHAR(255),
        close VARCHAR(255),
        price VARCHAR(255)
      );
    `);

    for (const row of rows) {
      const [company, recordDate, open, close, price] = row;

      // Insert data into the database
      await connection.execute(
        'INSERT INTO buyback (company_name, record_date, open, close, price) VALUES (?, ?, ?, ?, ?)',
        [company, recordDate, open, close, price]
      );
    }

    console.log('Table created, and data inserted into the database successfully');
  } catch (error) {
    console.error('Error creating table or inserting data into the database:', error.message);
  } finally {
    await connection.end();
  }
}

axios.get(url)
  .then(response => {
    if (response.status === 200) {
      const html = response.data;
      const $ = cheerio.load(html);

      // Assuming the table you want is the first one on the page
      const table = $('table').first();

      // Extracting table rows
      const rows = [];
      table.find('tbody tr').each((i, row) => {
        const rowData = [];
        $(row).find('td').each((j, cell) => {
          rowData.push($(cell).text().trim());
        });
        rows.push(rowData);
      });

      // Create table and insert data into the database
      createTableAndInsertData(rows);
    } else {
      console.error('Failed to fetch the page. Status:', response.status);
    }
  })
  .catch(error => {
    console.error('Error fetching the page:', error.message);
  });


