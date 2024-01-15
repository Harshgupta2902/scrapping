const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://ipowatch.in/ipo-grey-market-premium-latest-ipo-gmp/';

axios.get(url)
  .then(response => {
    if (response.status === 200) {
      const $ = cheerio.load(response.data);
      const targetDiv = $('[data-id="107e3c99"]');

      // Define the stop condition
      const stopCondition = [ 'IPO Name', 'Price', 'IPO GMP', 'Listed' ];

      // Assuming the table is the first table within the target div
      const table = targetDiv.find('table');

      // Extracting data from the table
      const tableData = [];
      const additionalList = [];
      let stopScraping = false;

      table.find('tr').each((index, row) => {
        const rowData = [];
        $(row).find('td').each((index, column) => {
          rowData.push($(column).text().trim());
        });

        // Check if the stop condition is met
        if (JSON.stringify(rowData) === JSON.stringify(stopCondition)) {
          stopScraping = true;
          return;
        }

        // If the stop condition is not met and it's not the header row, add data to the appropriate list
        if (!stopScraping && index !== 0) {
          tableData.push(rowData);
        } else if (stopScraping && index !== 0) {
          additionalList.push(rowData);
        }
      });

      // Print the main table data
      console.log('Main Table Data:', tableData);

      // Print the additional data after the stop condition (without the header)
      console.log('Additional Data:', additionalList.slice(1));
    }
  })
  .catch(error => {
    console.error('Error fetching the page:', error);
  });
