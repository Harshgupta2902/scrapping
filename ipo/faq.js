const mysql = require('mysql');

// Create a MySQL connection
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'ipo'
});
// Connect to the database
connection.connect();

const jsonData = {
  "GMP": [
    {
      "question": "What is Grey Market Premium?",
      "answer": "Grey Market Premium (IPO GMP) refers to the premium or additional price at which IPO shares are traded unofficially before their official listing on a stock exchange. It represents the market’s perception of the potential value and demand for the shares."
    },
    {
      "question": "How is Grey Market Premium calculated?",
      "answer": "The calculation is based on the company’s performance, its demand in the grey market, and the probability of subscription. It works before the IPO listing and during the days from the IPO start date to the allotment date. The Grey Market Premium indicates how the IPO might react on a listing day with an estimated price."
    },
    {
      "question": "Is Grey Market Premium reliable?",
      "answer": "There is no reliability guaranteed. While IPO GMP works in most cases, exceptions exist. It depends on factors such as demand, HNI and QIB subscription levels, and overall market conditions."
    },
    {
      "question": "What is Kostak Rate?",
      "answer": "The Kostak rate is the amount that one investor pays to the seller of an IPO application before the IPO listing. It applies whether the investor gets the IPO allotment or not, and buyers and sellers use Kostak rates to fix their profits in the grey market."
    },
    {
      "question": "How is Subject to Sauda related to IPO applications?",
      "answer": "Subject to Sauda is the amount decided when investors get the firm allotment on their IPO Application. It means one can get the said amount if one gets the allotment; otherwise, sauda will be canceled. Profits are not fixed and depend on allotment and subsequent performance."
    },
    {
      "question": "How do you calculate Grey Market Premium?",
      "answer": "The IPO GMP, or Grey Market Premium, is calculated based on the company’s performance, its demand in the grey market, and the probability of subscription. It's an estimation of how the IPO might perform on the listing day, but the actual listing may vary from the grey market price."
    },
    {
      "question": "Are Grey Market Stocks safe?",
      "answer": "It depends on the broker or the trading person. Trading in the grey market is not considered safe, and it involves risks due to potential fluctuations. It is suggested to refer to the IPO GMP for listing gain purposes and exercise caution."
    },
    {
      "question": "How can one buy or sell IPO applications in the Grey Market?",
      "answer": "There are no official entities associated with the grey market. Some brokers facilitate buying and selling of IPO applications on Kostak Rates or Subject to Sauda Rates based on the IPO GMP. One should find local brokers who act as intermediaries between buyers and sellers."
    },
    {
      "question": "What is the significance of IPO GMP?",
      "answer": "The IPO Grey Market Premium serves as an indicator of market sentiment and the perceived value of the IPO shares. It allows potential investors to gauge the level of demand and the premium they may have to pay if they wish to purchase shares during the IPO. However, it’s essential to note that the GMP doesn’t guarantee future performance and is subject to change."
    }
  ],

  "SME": [
    {
      "question": "What is SME IPO?",
      "answer": "SME IPO refers to the initial public offering (IPO) undertaken by a small and medium-sized enterprise (SME) to raise funds from the public. The SME gets listed on either the BSE SME or NSE Emerge Platforms."
    },
    {
      "question": "Is SME IPO a good investment?",
      "answer": "As per the fundamentals of the company, SME IPO might be a good investment. However, records show that only a few SME IPOs are trading above the IPO price. Potential investors are advised to check detailed information on IPOWatch before applying for SME IPOs."
    },
    {
      "question": "What is the difference between main-board IPO and SME IPO?",
      "answer": "SME IPO stands for small and medium enterprises. The IPO size is much smaller compared to the main-board IPO. While main-board IPOs list on NSE and BSE platforms, SME IPOs list on either BSE SME or NSE Emerge platform."
    },
    {
      "question": "Can SMEs go for an IPO?",
      "answer": "Yes, SMEs can go for an IPO, but they need to pass eligibility criteria, including having a track record of at least 3 years, positive cash accruals from operations for at least 3 years, and a positive net worth."
    },
    {
      "question": "What are the criteria for SME listing?",
      "answer": "As per the rules, a company should have a track record of at least 3 years, positive cash accruals from operations for at least 3 years, and a positive net worth to be eligible for SME listing."
    },
    {
      "question": "Can we apply for SME IPO?",
      "answer": "Yes, investors can apply for SME IPOs based on the categories finalized. SME IPOs offer shares to Non-Institutional Investors (NII) and Retail investors, sometimes also to Qualified Institutional Buyers (QIB). Investors can apply via ASBA or UPI-based applications, submitting forms to their banks or brokers."
    },
    {
      "question": "How do I sell an SME IPO on the listing day?",
      "answer": "To sell an SME IPO on the listing day, online traders can log in to their trading app or broker website, access their demat or trading account, and sell the allotted SME IPO. For offline trading, investors can call their broker to initiate the sale from their demat account. It’s simple!"
    }
  ],

  "Status": [
    {
      "question": "What does IPO Subscription Status mean?",
      "answer": "IPO Subscription Status indicates the level of investor interest and participation in an Initial Public Offering (IPO). It is measured by the number of times the IPO offering is subscribed by investors."
    },
    {
      "question": "How does IPO Subscription Status impact allotment?",
      "answer": "Higher subscription status often leads to a lower basis of allotment, triggering a lottery system. For instance, if an IPO is subscribed 5 times, the allotment ratio becomes 5:1, meaning one out of five applicants will be allotted shares."
    },
    {
      "question": "How is IPO Subscription Status calculated?",
      "answer": "IPO Subscription Status is calculated based on the number of shares offered by the company and the total number of shares applied for by investors. For example, if a company offers 1,00,000 shares and receives subscriptions for 5,00,000 shares, the IPO is said to be subscribed 5 times."
    },
    {
      "question": "Who are Qualified Institutional Buyers (QIB) in an IPO?",
      "answer": "Qualified Institutional Buyers (QIB) in an IPO include Financial Institutions, Banks, Foreign Institutional Investors (FIIs), and Mutual Funds."
    },
    {
      "question": "Who are Non-Institutional Investors (NII) in an IPO?",
      "answer": "Non-Institutional Investors (NII) in an IPO include Individual Investors, Non-Resident Indians (NRIs), Companies, Trusts, etc."
    },
    {
      "question": "Who are Retail Investors (RII) in an IPO?",
      "answer": "Retail Investors (RII) in an IPO include Retail Individual Investors or NRIs."
    },
    {
      "question": "What is the meaning of EMP in an IPO?",
      "answer": "EMP stands for Employee Bidders in an IPO. They are individuals participating in the IPO who are employees of the issuing company."
    },
    {
      "question": "What is the meaning of SHQ in an IPO?",
      "answer": "SHQ stands for Share Holders Quota in an IPO. It is a quota reserved for existing shareholders of the company."
    },
    {
      "question": "What is the meaning of PHQ in an IPO?",
      "answer": "PHQ stands for Policy Holders Quota in an IPO. It is a quota reserved for policyholders, often applicable in insurance company IPOs."
    }
  ],

  "Buyback": [
    {
      "question": "What is a share buyback?",
      "answer": "A share buyback is a corporate action where a company repurchases its own listed shares, reducing the number of shares available in the stock market. Companies undertake buybacks to decrease the supply of shares in the market and potentially increase the value of remaining shares for shareholders."
    },
    {
      "question": "Why do companies go for share buyback?",
      "answer": "Companies may go for share buybacks to enhance the value of remaining shares by reducing the supply in the market. If a company believes its shares are undervalued, a buyback can provide good returns to current investors. Additionally, it allows the company to control its stake in the open market and boost the proportion of earnings."
    },
    {
      "question": "How does a share buyback work?",
      "answer": "In a share buyback, the company offers to repurchase its own shares. The buyback reduces the number of shares in the market, and if the company stays bullish on its operations, it can help boost the proportion of earnings. The company files a letter of offer with SEBI, specifying the ratio of shares, the number of shares, buyback amount, buyback type, record date, and open and close dates. The buyback process occurs in the open market according to the schedule."
    },
    {
      "question": "Why do companies offer a premium in buyback?",
      "answer": "Companies may offer a premium in buybacks to incentivize investors to participate. For example, if a company offers a buyback at Rs.1000 against the current market price of Rs.600, investors receive a Rs.400 premium per share in addition to the holding price. This can attract more investors to participate in the buyback offer."
    },
    {
      "question": "What is a buyback record date?",
      "answer": "The buyback record date is the date specified in the buyback offer on which shareholders must own the company's stock in their demat account to be eligible to participate in the buyback. Only those with the stock in their demat account on the record date can take part in the buyback offer."
    }
  ]
}

// Iterate through JSON data and insert into the database
for (const key in jsonData) {
  const entries = jsonData[key];

  for (const entry of entries) {
    const ipoid = null; // You may replace this with the actual ipoid value if available
    const question = entry.question || '';
    const answer = entry.answer || '';
    const typeValue = key;

    // Insert into the database
    const query = `INSERT INTO faq (ipoid, question, answer, type) VALUES (?, ?, ?, ?)`;
    connection.query(query, [ipoid, question, answer, typeValue], (error, results, fields) => {
      if (error) throw error;
      console.log(`Inserted into database: ${key}`);
    });
  }
}

// Close the connection after all queries are executed
connection.end();