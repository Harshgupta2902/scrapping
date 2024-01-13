import requests
import os

# Specify the path where you want to save the downloaded files
download_directory = '/home/user/Downloads/xls'

# Create the directory if it doesn't exist
os.makedirs(download_directory, exist_ok=True)

# List of banks with their respective URLs
banks = 	[
  {
    "text": "Abhyudaya Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_02.xlsx"
  },
  {
    "text": "Ahmedabad Mercantile Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_76.xlsx"
  },
  {
    "text": "Ahmednagar Merchants Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_240.xlsx"
  },
  {
    "text": "Airtel Payments Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_194.xlsx"
  },
  {
    "text": "Akola Janata Commercial Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_161.xlsx"
  },
  {
    "text": "Almora Urban Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_105.xlsx"
  },
  {
    "text": "Ambarnath Jaihind Cooperative Bank Limited, Ambarnath",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_227.xlsx"
  },
  {
    "text": "Andhra Pragathi Grameena Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_141.xlsx"
  },
  {
    "text": "Andhra Pradesh Grameena Vikas Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_229.xlsx"
  },
  {
    "text": "Apna Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_106.xlsx"
  },
  {
    "text": "Arvind Sahakari Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_269.xlsx"
  },
  {
    "text": "Australia and New Zealand Banking Group Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_107.xlsx"
  },
  {
    "text": "AU Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_204.xlsx"
  },
  {
    "text": "Axis Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_05.xlsx"
  },
  {
    "text": "Bandhan Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_178.xlsx"
  },
  {
    "text": "Bank of America",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_06.xlsx"
  },
  {
    "text": "Bank of Bahrein and Kuwait",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_07.xlsx"
  },
  {
    "text": "Bank of Baroda",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_08.xlsx"
  },
  {
    "text": "Bank of Ceylon",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_09.xlsx"
  },
  {
    "text": "Bank of China Limited India Branch",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_293.xlsx"
  },
  {
    "text": "Bank of India",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_10.xlsx"
  },
  {
    "text": "Bank of Maharashtra",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_11.xlsx"
  },
  {
    "text": "Barclays Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_13.xlsx"
  },
  {
    "text": "Bassein Catholic Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_14.xlsx"
  },
  {
    "text": "Bhagini Nivedita Sahakari Bank Limited, Pune",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_228.xlsx"
  },
  {
    "text": "Bharat Cooperative Bank Mumbai Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_77.xlsx"
  },
  {
    "text": "Bombay Mercantile Cooperative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_271.xlsx"
  },
  {
    "text": "BNP Paribas Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_15.xlsx"
  },
  {
    "text": "Canara Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_16.xlsx"
  },
  {
    "text": "Capital Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_192.xlsx"
  },
  {
    "text": "Central Bank of India",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_18.xlsx"
  },
  {
    "text": "Chhattisgarh Rajya Gramin Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_283.xlsx"
  },
  {
    "text": "CITI Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_20.xlsx"
  },
  {
    "text": "Citizen Credit Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_21.xlsx"
  },
  {
    "text": "City Union Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_22.xlsx"
  },
  {
    "text": "Coastal Local Area Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_266.xlsx"
  },
  {
    "text": "Credit Agricole Corporate and Investment Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_24.xlsx"
  },
  {
    "text": "Credit Suisse AG",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_109.xlsx"
  },
  {
    "text": "CSB Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_251.xlsx"
  },
  {
    "text": "CTBC Bank Co Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_253.xlsx"
  },
  {
    "text": "Darussalam Cooperative Urban Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_279.xlsx"
  },
  {
    "text": "DBS Bank India Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_25.xlsx"
  },
  {
    "text": "DCB Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_28.xlsx"
  },
  {
    "text": "Deogiri Nagari Sahakari Bank Limited, Aurangabad",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_189.xlsx"
  },
  {
    "text": "Deposit Insurance and Credit Guarantee Corporation",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_172.xlsx"
  },
  {
    "text": "Deustche Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_27.xlsx"
  },
  {
    "text": "Dhanalakshmi Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_29.xlsx"
  },
  {
    "text": "DMK Jaoli Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_213.xlsx"
  },
  {
    "text": "Doha Bank QSC",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_174.xlsx"
  },
  {
    "text": "Dombivli Nagari Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_31.xlsx"
  },
  {
    "text": "Durgapur Steel Peoples Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_218.xlsx"
  },
  {
    "text": "Emirates NBD Bank P J S C",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_210.xlsx"
  },
  {
    "text": "Esaf Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_200.xlsx"
  },
  {
    "text": "Equitas Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_193.xlsx"
  },
  {
    "text": "Export Import Bank of India",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_175.xlsx"
  },
  {
    "text": "Federal Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_79.xlsx"
  },
  {
    "text": "Fincare Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_209.xlsx"
  },
  {
    "text": "FINO Payments Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_207.xlsx"
  },
  {
    "text": "Firstrand Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_32.xlsx"
  },
  {
    "text": "First Abu Dhabi Bank PJSC",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_211.xlsx"
  },
  {
    "text": "G P Parsik Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_56.xlsx"
  },
  {
    "text": "GS Mahanagar Cooperative Bank Limited, Mumbai",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_231.xlsx"
  },
  {
    "text": "Guardian Souharda Sahakari Bank Niyamita",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_294.xlsx"
  },
  {
    "text": "HDFC Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_33.xlsx"
  },
  {
    "text": "Haryana State Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_237.xlsx"
  },
  {
    "text": "Himachal Pradesh State Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_188.xlsx"
  },
  {
    "text": "HSBC Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_34.xlsx"
  },
  {
    "text": "Hutatma Sahakari Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_280.xlsx"
  },
  {
    "text": "ICICI Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_35.xlsx"
  },
  {
    "text": "IDBI Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_36.xlsx"
  },
  {
    "text": "IDFC First Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_180.xlsx"
  },
  {
    "text": "Indian Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_37.xlsx"
  },
  {
    "text": "India Post Payment Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_224.xlsx"
  },
  {
    "text": "Indusind Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_39.xlsx"
  },
  {
    "text": "Indian Overseas Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_38.xlsx"
  },
  {
    "text": "Industrial and Commercial Bank of China Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_154.xlsx"
  },
  {
    "text": "Industrial Bank of Korea",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_181.xlsx"
  },
  {
    "text": "Irinjalakuda Town Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_232.xlsx"
  },
  {
    "text": "Jalgaon Janata Sahkari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_111.xlsx"
  },
  {
    "text": "Jammu and Kashmir Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_81.xlsx"
  },
  {
    "text": "Janakalyan Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_176.xlsx"
  },
  {
    "text": "Jana Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_225.xlsx"
  },
  {
    "text": "Janaseva Sahakari Bank (Borivli) Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_157.xlsx"
  },
  {
    "text": "Janaseva Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_42.xlsx"
  },
  {
    "text": "Janata Sahakari Bank Limited (Pune)",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_112.xlsx"
  },
  {
    "text": "Janatha Seva Cooperative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_272.xlsx"
  },
  {
    "text": "Jio Payments Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_219.xlsx"
  },
  {
    "text": "JP Morgan Chase Bank NA",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_145.xlsx"
  },
  {
    "text": "Kallappanna Awade Ichalkaranji Janata Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_113.xlsx"
  },
  {
    "text": "Kalyan Janata Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_84.xlsx"
  },
  {
    "text": "Kalupur Commercial Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_82.xlsx"
  },
  {
    "text": "Karnataka Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_44.xlsx"
  },
  {
    "text": "Karnataka Gramin Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_260.xlsx"
  },
  {
    "text": "Karnataka Vikas Grameena Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_121.xlsx"
  },
  {
    "text": "Karur Vysya Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_45.xlsx"
  },
  {
    "text": "KEB Hana Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_184.xlsx"
  },
  {
    "text": "Kerala Gramin Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_170.xlsx"
  },
  {
    "text": "Kookmin Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_261.xlsx"
  },
  {
    "text": "Kotak Mahindra Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_46.xlsx"
  },
  {
    "text": "Maharashtra Gramin Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_191.xlsx"
  },
  {
    "text": "Maharashtra State Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_48.xlsx"
  },
  {
    "text": "Mahesh Sahakari Bank Limited Pune",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_239.xlsx"
  },
  {
    "text": "MashreqBank PSC",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_49.xlsx"
  },
  {
    "text": "Mizuho Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_50.xlsx"
  },
  {
    "text": "Model Co-operative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_264.xlsx"
  },
  {
    "text": "MUFG Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_226.xlsx"
  },
  {
    "text": "National Bank for Agriculture and Rural Development",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_223.xlsx"
  },
  {
    "text": "Nagpur Nagarik Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_123.xlsx"
  },
  {
    "text": "Nav Jeevan Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_245.xlsx"
  },
  {
    "text": "New India Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_51.xlsx"
  },
  {
    "text": "NKGSB Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_52.xlsx"
  },
  {
    "text": "North East Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_214.xlsx"
  },
  {
    "text": "NSDL Payments Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_234.xlsx"
  },
  {
    "text": "Nutan Nagarik Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_53.xlsx"
  },
  {
    "text": "Pavana Sahakari Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_284.xlsx"
  },
  {
    "text": "Paytm Payments Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_205.xlsx"
  },
  {
    "text": "Prime Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_116.xlsx"
  },
  {
    "text": "PT Bank Maybank Indonesia TBK",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_190.xlsx"
  },
  {
    "text": "Punjab and Sind Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_58.xlsx"
  },
  {
    "text": "Punjab National Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_59.xlsx"
  },
  {
    "text": "Qatar National Bank SAQ",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_212.xlsx"
  },
  {
    "text": "Rabobank International",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_117.xlsx"
  },
  {
    "text": "Rajarambapu Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_220.xlsx"
  },
  {
    "text": "Rajarshi Shahu Sahakari Bank Limited, Pune",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_262.xlsx"
  },
  {
    "text": "Rajasthan Marudhara Gramin Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_250.xlsx"
  },
  {
    "text": "Rajgurunagar Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_159.xlsx"
  },
  {
    "text": "Rajkot Nagrik Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_60.xlsx"
  },
  {
    "text": "Rajnandgaon District Central Co-operative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_274.xlsx"
  },
  {
    "text": "RBL Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_88.xlsx"
  },
  {
    "text": "Reserve Bank of India",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_61.xlsx"
  },
  {
    "text": "Samarth Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_186.xlsx"
  },
  {
    "text": "Sant Sopankaka Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_246.xlsx"
  },
  {
    "text": "Saptagiri Grameena Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_295.xlsx"
  },
  {
    "text": "Saraspur Nagrik Cooperative Bank Limited, Saraspur",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_252.xlsx"
  },
  {
    "text": "Saraswat Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_90.xlsx"
  },
  {
    "text": "Satara Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_258.xlsx"
  },
  {
    "text": "Saurashtra Gramin Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_287.xlsx"
  },
  {
    "text": "SBER Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_137.xlsx"
  },
  {
    "text": "SBM Bank India Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_235.xlsx"
  },
  {
    "text": "Shikshak Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_166.xlsx"
  },
  {
    "text": "Shinhan Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_62.xlsx"
  },
  {
    "text": "Shivalik Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_289.xlsx"
  },
  {
    "text": "Shri Chhatrapati Rajashri Shahu Urban Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_136.xlsx"
  },
  {
    "text": "Shri Veershaiv Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_236.xlsx"
  },
  {
    "text": "Shree Kadi Nagarik Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_286.xlsx"
  },
  {
    "text": "Smriti Nagrik Sahakari Bank Maryadit",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_282.xlsx"
  },
  {
    "text": "Sir M Visvesvaraya Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_233.xlsx"
  },
  {
    "text": "Societe Generale",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_63.xlsx"
  },
  {
    "text": "Solapur Janata Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_153.xlsx"
  },
  {
    "text": "South Indian Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_64.xlsx"
  },
  {
    "text": "Sree Charan Souhardha Cooperative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_273.xlsx"
  },
  {
    "text": "Standard Chartered Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_65.xlsx"
  },
  {
    "text": "State Bank of India",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_68.xlsx"
  },
  {
    "text": "Suco Souharda Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_265.xlsx"
  },
  {
    "text": "Sumitomo Mitsui Banking Corporation",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_142.xlsx"
  },
  {
    "text": "Surat National Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_179.xlsx"
  },
  {
    "text": "Suryoday Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_201.xlsx"
  },
  {
    "text": "Sutex Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_129.xlsx"
  },
  {
    "text": "Tamilnad Mercantile Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_74.xlsx"
  },
  {
    "text": "Telangana State Coop Apex Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_196.xlsx"
  },
  {
    "text": "Textile Traders Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_203.xlsx"
  },
  {
    "text": "The Ajara Urban Cooperative Bank Limited, Ajara",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_244.xlsx"
  },
  {
    "text": "The A.P. Mahesh Cooperative Urban Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_119.xlsx"
  },
  {
    "text": "The Akola District Central Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_147.xlsx"
  },
  {
    "text": "The Akola Urban Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_281.xlsx"
  },
  {
    "text": "The Ahmednagar District Central Co-Operative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_277.xlsx"
  },
  {
    "text": "The Andhra Pradesh State Coop Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_101.xlsx"
  },
  {
    "text": "The Bank of Nova Scotia",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_75.xlsx"
  },
  {
    "text": "The Banaskantha Mercantile Cooperative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/content/docs/IFCB2009_275.xlsx"
  },
  {
    "text": "The Baramati Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_199.xlsx"
  },
  {
    "text": "The Burdwan Central Co-operative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_292.xlsx"
  },
  {
    "text": "The Cosmos Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_78.xlsx"
  },
  {
    "text": "The Delhi State Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_158.xlsx"
  },
  {
    "text": "The Gadchiroli District Central Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_146.xlsx"
  },
  {
    "text": "The Greater Bombay Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_80.xlsx"
  },
  {
    "text": "The Gujarat State Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_120.xlsx"
  },
  {
    "text": "The HASTI Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_167.xlsx"
  },
  {
    "text": "The Jalgaon Peopels Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_149.xlsx"
  },
  {
    "text": "The Kalyan Janata Sahakari Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_288.xlsx"
  },
  {
    "text": "The Kangra Central Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_124.xlsx"
  },
  {
    "text": "The Kangra Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_164.xlsx"
  },
  {
    "text": "The Karad Urban Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_102.xlsx"
  },
  {
    "text": "The Karanataka State Cooperative Apex Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_83.xlsx"
  },
  {
    "text": "The Kerala State Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_248.xlsx"
  },
  {
    "text": "The Kolhapur Urban Co-op Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_270.xlsx"
  },
  {
    "text": "The Kurmanchal Nagar Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_148.xlsx"
  },
  {
    "text": "The Malad Sahakari Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/content/docs/IFCB2009_276.xlsx"
  },
  {
    "text": "The Meghalaya Co-operative Apex Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_285.xlsx"
  },
  {
    "text": "The Mehsana Urban Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_86.xlsx"
  },
  {
    "text": "The Mumbai District Central Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_114.xlsx"
  },
  {
    "text": "The Muslim Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_255.xlsx"
  },
  {
    "text": "The Municipal Cooperative Bank Limited, Mumbai",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_122.xlsx"
  },
  {
    "text": "The Nainital Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_87.xlsx"
  },
  {
    "text": "The Nasik Merchants Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_104.xlsx"
  },
  {
    "text": "The Navnirman Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_197.xlsx"
  },
  {
    "text": "The Nawanagar Cooperative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_268.xlsx"
  },
  {
    "text": "The Nilambur Cooperative Urban Bank Limited, Nilambur",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_249.xlsx"
  },
  {
    "text": "The Odisha State Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_256.xlsx"
  },
  {
    "text": "The Pandharpur Urban Cooperative Bank Limited, Pandharpur",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_185.xlsx"
  },
  {
    "text": "The Pusad Urban Cooperative Bank Limited, Pusad",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_259.xlsx"
  },
  {
    "text": "The Punjab State Cooperative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_267.xlsx"
  },
  {
    "text": "The Rajasthan State Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_125.xlsx"
  },
  {
    "text": "The Satara District Central Cooperative Bank Ltd",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_278.xlsx"
  },
  {
    "text": "The Shamrao Vithal Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_91.xlsx"
  },
  {
    "text": "The Sindhudurg District Central Coop Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_206.xlsx"
  },
  {
    "text": "The Surat District Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_126.xlsx"
  },
  {
    "text": "The Surath Peoples Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_92.xlsx"
  },
  {
    "text": "The Tamil Nadu State Apex Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_93.xlsx"
  },
  {
    "text": "The Thane Bharat Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_118.xlsx"
  },
  {
    "text": "The Thane District Central Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_144.xlsx"
  },
  {
    "text": "The Udaipur Urban Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_263.xlsx"
  },
  {
    "text": "The Urban Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_243.xlsx"
  },
  {
    "text": "The Varachha Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_135.xlsx"
  },
  {
    "text": "The Vijay Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_247.xlsx"
  },
  {
    "text": "The Vishweshwar Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_127.xlsx"
  },
  {
    "text": "The West Bengal State Cooperative Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_95.xlsx"
  },
  {
    "text": "The Zoroastrian Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_165.xlsx"
  },
  {
    "text": "TJSB Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_177.xlsx"
  },
  {
    "text": "Tumkur Grain Merchants Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_138.xlsx"
  },
  {
    "text": "UCO Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_96.xlsx"
  },
  {
    "text": "Ujjivan Small Finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_198.xlsx"
  },
  {
    "text": "Union Bank of India",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_97.xlsx"
  },
  {
    "text": "United Overseas Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_155.xlsx"
  },
  {
    "text": "Unity Small finance Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_290.xlsx"
  },
  {
    "text": "Urban Co operative Bank Limited Bareilly",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_291.xlsx"
  },
  {
    "text": "Utkarsh Small Finance Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_202.xlsx"
  },
  {
    "text": "Uttar Pradesh Cooperative Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_257.xlsx"
  },
  {
    "text": "Vasai Janata Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_230.xlsx"
  },
  {
    "text": "Vasai Vikas Sahakari Bank Limited",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_139.xlsx"
  },
  {
    "text": "Woori Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_128.xlsx"
  },
  {
    "text": "Yes Bank",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_100.xlsx"
  },
  {
    "text": "Zila Sahakri Bank Limited Ghaziabad",
    "href": "https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_156.xlsx"
  }
]

# Download files
for bank in banks:
    url = bank["href"]
    filename = os.path.join(download_directory, f"{bank['text']}.xlsx")
    
    response = requests.get(url)
    
    with open(filename, "wb") as file:
        file.write(response.content)
    
    print(f"{bank['text']} file downloaded to {filename}")

