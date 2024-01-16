const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://ipowatch.in/ipo-forms-download-ipo-application-asba-form/';

axios.get(url)
  .then(response => {
    if (response.status === 200) {
      const html = response.data;
      const $ = cheerio.load(html);
      const table = $('table');
      const tableData = [];
      table.find('tr').each((rowIndex, row) => {
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
      console.log(tableData);
    }
  })
  .catch(error => {
    console.error(`Error fetching data: ${error.message}`);
  });
