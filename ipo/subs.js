const axios = require('axios');
const cheerio = require('cheerio');
const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ipo',

});

const url = 'https://ipowatch.in/ipo-subscription-status-numbers/';

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to database: ', err.message);
    return;
  }
  console.log('Connected to the database');

  // Create the table if it doesn't exist
  const createTableQuery = `
    CREATE TABLE IF NOT EXISTS subs (
      id INT AUTO_INCREMENT PRIMARY KEY,
      status VARCHAR(255),
      name VARCHAR(255),
      QIB VARCHAR(255),
      NII VARCHAR(255),
      RII VARCHAR(255),
      Total VARCHAR(255)
    )`;
  
  connection.query(createTableQuery, (err, results) => {
    if (err) {
      console.error(`Error creating table: ${err.message}`);
      return;
    }
    console.log('Table created or already exists');

    axios.get(url)
      .then(response => {
        const html = response.data;
        const $ = cheerio.load(html);

        const rows = $('table tr');

        rows.each((index, element) => {
          const rowData = [];
          const columns = $(element).find('td');

          columns.each((index, element) => {
            let text = $(element).text().trim();

            if (index === 0) {
              const lines = text.split('\n');
              const strongText = $(element).find('strong').text().trim();
              rowData.push(strongText);
              if (lines.length > 1) {
                rowData.push(lines[0].trim(), lines[1].trim());
              } else {
                rowData.push(text.replace(strongText, '').trim());
              }
            } else {
              rowData.push(text);
            }
          });

          // Assuming rowData follows the format ['Closed', 'Company Name', 'QIB', 'NII', 'RII', 'Total']
          const [status, name, qib, nii, rii, total] = rowData;

          // Insert data into the database
          const insertQuery = `INSERT INTO subs (status, name, QIB, NII, RII, Total) VALUES (?, ?, ?, ?, ?, ?)`;
          connection.query(insertQuery, [status, name, qib, nii, rii, total], (err, results) => {
            if (err) {
              console.error(`Error inserting data into the database: ${err.message}`);
            } else {
              console.log(`Data inserted successfully for ${name}`);
            }
          });
        });
      })
      .catch(error => { 
        console.error(`Error fetching data from ${url}: ${error.message}`);
      })
      .finally(() => {
        // Close the database connection after processing
        connection.end();
      });
  });
});
