const axios = require('axios');
const cheerio = require('cheerio');
const mysql = require('mysql2/promise');

const insertDataIntoDatabase = async (url, tableName) => {
  try {
    const response = await axios.get(url);
    if (response.status === 200) {
      const html = response.data;
      const $ = cheerio.load(html);

      const tableData = $('#report_data table').map(function () {
        const headers = [];
        const rows = [];
        $(this).find('thead th').each(function () {
          headers.push($(this).text().trim());
        });
        $(this).find('tbody tr').each(function () {
          const row = {};
          $(this).find('td').each(function (index) {
            row[headers[index]] = $(this).text().trim();
          });
          rows.push(row);
        });
        return rows;
      }).get();
      console.log(tableData);
      const pool = mysql.createPool({
        host: 'localhost',
        user: 'root',
        password: '',
        database: 'ipo',
        waitForConnections: true,
        connectionLimit: 10,
        queueLimit: 0
      });
      const createDataTable = async () => {
        const connection = await pool.getConnection();
        try {
          await connection.query(`
            CREATE TABLE IF NOT EXISTS ${tableName} (
              id INT AUTO_INCREMENT PRIMARY KEY,
              company_name VARCHAR(255),
              close_date VARCHAR(255),
              size_rs_cr VARCHAR(255),
              qib_x VARCHAR(255),
              snii_x VARCHAR(255),
              bnii_x VARCHAR(255),
              nii_x VARCHAR(255),
              retail_x VARCHAR(255),
              employee_x VARCHAR(255),
              others_x VARCHAR(255),
              total_x VARCHAR(255),
              applications VARCHAR(255)
            );
          `);
      await connection.query(`TRUNCATE TABLE ${tableName};`);

        } finally {
          connection.release();
        }
      };
      const insertData = async () => {
        const connection = await pool.getConnection();
        try {
          for (const data of tableData) {
            const [results] = await connection.query(
              `INSERT INTO ${tableName} (company_name, close_date, size_rs_cr, qib_x, snii_x, bnii_x, nii_x, retail_x, employee_x, others_x, total_x, applications) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
              [
                data['Company Name'],
                data['Close Date'],
                data['Size (Rs Cr)'],
                data['QIB (x)'],
                data['sNII (x)'],
                data['bNII (x)'],
                data['NII (x)'],
                data['Retail (x)'],
                data['Employee (x)'],
                data['Others (x)'],
                data['Total (x)'],
                data['Applications']
              ]
            );
          }
        } finally {
          connection.release();
        }
      };

      try {
        await createDataTable();
        await insertData();
        console.log(`Data from ${url} inserted successfully.`);
      } catch (error) {
        console.error(`Error during database operations for ${url}:`, error.message);
      } finally {
        await pool.end();
      }
    }
  } catch (error) {
    console.error(`Error fetching data from ${url}: ${error.message}`);
  }
};
const firstUrl = 'https://www.chittorgarh.com/report/ipo-subscription-status-live-bidding-data-bse-nse/21/?year=2024';
const firstTableName = 'ipo_subscription_data';
insertDataIntoDatabase(firstUrl, firstTableName);


const secondUrl = 'https://www.chittorgarh.com/report/sme-ipo-subscription-status-live-bidding-bse-nse/22/';
const secondTableName = 'sme_subscription_data';
insertDataIntoDatabase(secondUrl, secondTableName);
