const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://ipowatch.in/share-buyback-offers/';

axios.get(url)
  .then(response => {
    if (response.status === 200) {
      const html = response.data;
      const $ = cheerio.load(html);

      // Assuming the table you want is the first one on the page
      const table = $('table').first();

      // Extracting table headers
      const headers = [];
      table.find('th').each((i, el) => {
        headers.push($(el).text().trim());
      });

      // Extracting table rows
      const rows = [];
      table.find('tbody tr').each((i, row) => {
        const rowData = [];
        $(row).find('td').each((j, cell) => {
          rowData.push($(cell).text().trim());
        });
        rows.push(rowData);
      });

      // Printing the headers and rows
      console.log(rows);
    } else {
      console.error('Failed to fetch the page. Status:', response.status);
    }
  })
  .catch(error => {
    console.error('Error fetching the page:', error.message);
  });
