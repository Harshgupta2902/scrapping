
    const axios = require('axios');
    const cheerio = require('cheerio');
    const mysql = require('mysql');
    
    const url = 'https://ipowatch.in';
    
    async function fetchData() {
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
    
        // Create MySQL database connection
        const connection = mysql.createConnection({
          host: 'localhost',
          user: 'root',
          password: '',
          database: 'ipo',
        });
    
        // Connect to the database
        connection.connect();
    
        // Create 'recents' table
        createTable(connection, 'recents');
    
        // Insert data into 'recents' table
        insertDataIntoTable(connection, 'recents', table1Data);
        insertDataIntoTable(connection, 'recents', table2Data);
    
        // Close the database connection
        console.log('Data Inserted Successfully');

        // connection.end();
      } catch (error) {
        console.error('Error fetching data:', error);
      }finally{
        // connection.end();
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
        $(row).find('td').each((j, cell) => {
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
    
      connection.query(query, (error, results, fields) => {
        if (error) {
          console.error('Error creating table:', error);
        } else {
          console.log('Table created successfully');
        }
      });
    }
    
    async function checkExistingRecord(connection, tableName, companyName) {
      const query = `SELECT * FROM ${tableName} WHERE Company = ?`;
      const params = [companyName];
    
      return new Promise((resolve, reject) => {
        connection.query(query, params, (error, results, fields) => {
          if (error) {
            console.error('Error checking existing record:', error);
            reject(error);
          } else {
            resolve(results.length > 0);
          }
        });
      });
    }
    
    async function insertDataIntoTable(connection, tableName, data) {
      for (const row of data) {
        const company = row.Company;
    
        try {
          const existingRecord = await checkExistingRecord(connection, tableName, company);
    
          if (!existingRecord) {
            const columns = Object.keys(row).join(', ');
            const values = Object.values(row)
              .map((value) => (typeof value === 'string' ? `'${value}'` : value))
              .join(', ');
    
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
    
    async function executeQuery(connection, query) {
      return new Promise((resolve, reject) => {
        connection.query(query, (error, results, fields) => {
          if (error) {
            console.error('Error executing query:', error);
            reject(error);
          } else {
            resolve(results);
          }
        });
      });
    }
    
    
    // Call the fetchData function
    fetchData();
    