const axios = require('axios');
const cheerio = require('cheerio');
const mysql = require('mysql');

const url = 'https://ipowatch.in/ipo-forms-download-ipo-application-asba-form/';

// MySQL database connection configuration
const dbConfig = {
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ipo',
};

// Create a connection to the database
const connection = mysql.createConnection(dbConfig);

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to database:', err.message);
    return;
  }
  console.log('Connected to database');

  // Create 'forms' table
  const createTableQuery = `
    CREATE TABLE IF NOT EXISTS forms (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255),
      name_link VARCHAR(255),
      date VARCHAR(255),
      date_link VARCHAR(255),
      bse VARCHAR(255),
      bse_link VARCHAR(255),
      nse VARCHAR(255),
      nse_link VARCHAR(255)
    )
  `;
  
  connection.query(createTableQuery, (err) => {
    if (err) {
      console.error('Error creating table:', err.message);
    } else {
      console.log('Table created or already exists');
      // Proceed to fetch and insert data here
      fetchDataAndInsertData();
    }
  });
});

function fetchDataAndInsertData() {
  axios.get(url)
    .then(response => {
      if (response.status === 200) {
        const html = response.data;
        const $ = cheerio.load(html);
        const table = $('table');
        const tableData = [];

        table.find('tr').each((rowIndex, row) => {
          if (rowIndex === 0) {
            return;
          }
          const rowData = [];
          $(row).find('td').each((colIndex, column) => {
            const cellText = $(column).text().trim();
            rowData.push(cellText);
            const anchorLink = $(column).find('a').attr('href');
            const finalCellText = anchorLink ? anchorLink : null;
            rowData.push(finalCellText);
          });
          tableData.push(rowData);
        });

        // Insert data into the 'forms' table
        tableData.forEach(rowData => {
          const sql = 'INSERT INTO forms (name, name_link, date, date_link, bse, bse_link, nse, nse_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?)';
          connection.query(sql, rowData, (err, result) => {
            if (err) {
              console.error('Error inserting into database:', err.message);
            } else {
              console.log('Row inserted into database:');
            }
          });
        });

        // Close the database connection
        connection.end();
      }
    })
    .catch(error => {
      console.error(`Error fetching data: ${error.message}`);
      // Close the database connection in case of an error
      connection.end();
    });
}
