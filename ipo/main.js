const axios = require('axios');
const cheerio = require('cheerio');
const mysql = require('mysql');

const url = 'https://ipowatch.in';

// Create MySQL database connection pool
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ipo',
  connectionLimit: 10,
});

async function fetchData() {
  let connection;

  try {
    // Fetch HTML content from the website
    const { data } = await axios.get(url);

    // Load HTML content into Cheerio
    const $ = cheerio.load(data);

    // Extract data from table with id tablepress-1
    const table1Data = extractTableData($, $('#tablepress-1'), 'Upcoming');

    // Extract data from table with id tablepress-2
    const table2Data = extractTableData($, $('#tablepress-2'), 'SME');

    // Print the extracted data
    console.log('Table 1 Data:', table1Data);
    console.log('Table 2 Data:', table2Data);

    // Get a connection from the pool
    connection = await getConnectionFromPool();

    // Create 'recents' table
    await createTable(connection, 'recents');

    // Insert data into 'recents' table
    await insertDataIntoTable(connection, 'recents', table1Data);
    await insertDataIntoTable(connection, 'recents', table2Data);

    console.log('Data Inserted Successfully');
  } catch (error) {
    console.error('Error fetching data:', error);
  } finally {
    // Release the connection back to the pool
    if (connection) {
      connection.release();
    }

    // End the server gracefully
    process.exit();
  }
}

function extractTableData($, table, type) {
  const headers = [];
  const rows = [];

  // Extract headers
  table.find('thead tr th').each((i, el) => {
    headers.push($(el).text().trim());
  });

  // Extract rows
  table.find('tbody tr').each((i, row) => {
    const rowData = { Type: type };
    $(row)
      .find('td')
      .each((j, cell) => {
        rowData[headers[j]] = $(cell).text().trim();
      });
    rows.push(rowData);
  });

  return rows;
}

function createTable(connection, tableName) {
  const query = `
    CREATE TABLE IF NOT EXISTS ${tableName} (
      id INT AUTO_INCREMENT PRIMARY KEY,
      Type ENUM('Upcoming', 'SME'),
      Company VARCHAR(255),
      Open VARCHAR(255),
      Close VARCHAR(255)
    )
  `;

  return executeQuery(connection, query);
}

async function checkExistingRecord(connection, tableName, companyName) {
  const query = `SELECT * FROM ${tableName} WHERE Company = ?`;
  const params = [companyName];

  try {
    const results = await executeQuery(connection, query, params);
    return results.length > 0;
  } catch (error) {
    console.error('Error checking existing record:', error);
    throw error;
  }
}

async function insertDataIntoTable(connection, tableName, data) {
  for (const row of data) {
    const company = row.Company;

    try {
      const existingRecord = await checkExistingRecord(connection, tableName, company);

      if (!existingRecord) {
        const columns = Object.keys(row).join(', ');
        const values = Object.values(row).map((value) => (typeof value === 'string' ? `'${value}'` : value)).join(', ');

        const query = `INSERT INTO ${tableName} (${columns}) VALUES (${values})`;

        await executeQuery(connection, query);
        console.log(`Data for ${company} inserted successfully`);
      } else {
        console.log(`Record for ${company} already exists. Skipping insertion.`);
      }
    } catch (error) {
      console.error('Error inserting data:', error);
    }
  }
}

async function executeQuery(connection, query, params) {
  return new Promise((resolve, reject) => {
    connection.query(query, params, (error, results, fields) => {
      if (error) {
        console.error('Error executing query:', error);
        reject(error);
      } else {
        resolve(results);
      }
    });
  });
}

async function getConnectionFromPool() {
  return new Promise((resolve, reject) => {
    pool.getConnection((err, connection) => {
      if (err) {
        console.error('Error getting connection from pool:', err);
        reject(err);
      } else {
        resolve(connection);
      }
    });
  });
}

// Call the fetchData function
fetchData();
