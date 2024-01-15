const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://ipowatch.in/ipo-subscription-status-numbers/';

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

        // Handle case where IPO Open information is split across two lines
        if (index === 0) {
          const lines = text.split('\n');
          if (lines.length > 1) {
            rowData.push(lines[0].trim(), lines[1].trim()); // Extracting both lines
          } else {
            rowData.push(text);
          }
        } else {
          rowData.push(text);
        }
      });

      console.log(rowData);
    });
  })
  .catch(error => { 
    console.error(`Error fetching data from ${url}: ${error.message}`);
  });
