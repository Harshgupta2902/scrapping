from bs4 import BeautifulSoup
import json

html_code = """
<table width="100%" border="0" cellpadding="0" cellspacing="0" class="tablebg">
                                <tr>
        <th>List of NEFT enabled bank Branches (Bank-wise Indian Financial System Code) updated as on December 15, 2023</th>
    </tr>
    <tr>
        <td>
            <table width="70%" border="0" align="center" cellpadding="0" cellspacing="1" class="tablebg">
                <tr>
                    <td width="3%" align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td width="97%">
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_02.xlsx" class="links">Abhyudaya Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_76.xlsx" class="links">Ahmedabad Mercantile Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_240.xlsx" class="links">Ahmednagar Merchants Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_194.xlsx" class="links">Airtel Payments Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_161.xlsx" class="links">Akola Janata Commercial Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_105.xlsx" class="links">Almora Urban Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_227.xlsx" class="links">Ambarnath Jaihind Cooperative Bank Limited, Ambarnath</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_141.xlsx" class="links">Andhra Pragathi Grameena Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_229.xlsx" class="links">Andhra Pradesh Grameena Vikas Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_106.xlsx" class="links">Apna Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_269.xlsx" class="links">Arvind Sahakari Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_107.xlsx" class="links">Australia and New Zealand Banking Group Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_204.xlsx" class="links">AU Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_05.xlsx" class="links">Axis Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_178.xlsx" class="links">Bandhan Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_06.xlsx" class="links">Bank of America</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_07.xlsx" class="links">Bank of Bahrein and Kuwait</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_08.xlsx" class="links">Bank of Baroda</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_09.xlsx" class="links">Bank of Ceylon</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_293.xlsx" class="links">Bank of China Limited India Branch</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_10.xlsx" class="links">Bank of India</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_11.xlsx" class="links">Bank of Maharashtra</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_13.xlsx" class="links">Barclays Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_14.xlsx" class="links">Bassein Catholic Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_228.xlsx" class="links">Bhagini Nivedita Sahakari Bank Limited, Pune</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_77.xlsx" class="links">Bharat Cooperative Bank Mumbai Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_271.xlsx" class="links">Bombay Mercantile Cooperative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_15.xlsx" class="links">BNP Paribas Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_16.xlsx" class="links">Canara Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_192.xlsx" class="links">Capital Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_18.xlsx" class="links">Central Bank of India</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_283.xlsx" class="links">Chhattisgarh Rajya Gramin Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_20.xlsx" class="links">CITI Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_21.xlsx" class="links">Citizen Credit Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_22.xlsx" class="links">City Union Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_266.xlsx" class="links">Coastal Local Area Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_24.xlsx" class="links">Credit Agricole Corporate and Investment Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_109.xlsx" class="links">Credit Suisse AG</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_251.xlsx" class="links">CSB Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_253.xlsx" class="links">CTBC Bank Co Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_279.xlsx" class="links">Darussalam Cooperative Urban Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_25.xlsx" class="links">DBS Bank India Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_28.xlsx" class="links">DCB Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_189.xlsx" class="links">Deogiri Nagari Sahakari Bank Limited, Aurangabad</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_172.xlsx" class="links">Deposit Insurance and Credit Guarantee Corporation</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_27.xlsx" class="links">Deustche Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_29.xlsx" class="links">Dhanalakshmi Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_213.xlsx" class="links">DMK Jaoli Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_174.xlsx" class="links">Doha Bank QSC</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_31.xlsx" class="links">Dombivli Nagari Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_218.xlsx" class="links">Durgapur Steel Peoples Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_210.xlsx" class="links">Emirates NBD Bank P J S C</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_200.xlsx" class="links">Esaf Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_193.xlsx" class="links">Equitas Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_175.xlsx" class="links">Export Import Bank of India</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_79.xlsx" class="links">Federal Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_209.xlsx" class="links">Fincare Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_207.xlsx" class="links">FINO Payments Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_32.xlsx" class="links">Firstrand Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_211.xlsx" class="links">First Abu Dhabi Bank PJSC</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_56.xlsx" class="links">G P Parsik Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_231.xlsx" class="links">GS Mahanagar Cooperative Bank Limited, Mumbai</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_294.xlsx" class="links">Guardian Souharda Sahakari Bank Niyamita</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_33.xlsx" class="links">HDFC Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_237.xlsx" class="links">Haryana State Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_188.xlsx" class="links">Himachal Pradesh State Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_34.xlsx" class="links">HSBC Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_280.xlsx" class="links">Hutatma Sahakari Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_35.xlsx" class="links">ICICI Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_36.xlsx" class="links">IDBI Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_180.xlsx" class="links">IDFC First Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td class="links">
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_37.xlsx" class="links">Indian Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td class="links">
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_224.xlsx" class="links">India Post Payment Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td class="links">
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_39.xlsx" class="links">Indusind Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td class="links">
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_38.xlsx" class="links">Indian Overseas Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td class="links">
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_154.xlsx" class="links">Industrial and Commercial Bank of China Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_181.xlsx" class="links">Industrial Bank of Korea</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_232.xlsx" class="links">Irinjalakuda Town Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_111.xlsx" class="links">Jalgaon Janata Sahkari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_81.xlsx" class="links">Jammu and Kashmir Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_176.xlsx" class="links">Janakalyan Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_225.xlsx" class="links">Jana Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_157.xlsx" class="links">Janaseva Sahakari Bank (Borivli) Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_42.xlsx" class="links">Janaseva Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_112.xlsx" class="links">Janata Sahakari Bank Limited (Pune)</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_272.xlsx" class="links">Janatha Seva Cooperative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_219.xlsx" class="links">Jio Payments Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_145.xlsx" class="links">JP Morgan Chase Bank NA</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_113.xlsx" class="links">Kallappanna Awade Ichalkaranji Janata Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_84.xlsx" class="links">Kalyan Janata Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_82.xlsx" class="links">Kalupur Commercial Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_44.xlsx" class="links">Karnataka Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_260.xlsx" class="links">Karnataka Gramin Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_121.xlsx" class="links">Karnataka Vikas Grameena Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_45.xlsx" class="links">Karur Vysya Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_184.xlsx" class="links">KEB Hana Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_170.xlsx" class="links">Kerala Gramin Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_261.xlsx" class="links">Kookmin Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_46.xlsx" class="links">Kotak Mahindra Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_191.xlsx" class="links">Maharashtra Gramin Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_48.xlsx" class="links">Maharashtra State Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_239.xlsx" class="links">Mahesh Sahakari Bank Limited Pune</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_49.xlsx" class="links">MashreqBank PSC</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_50.xlsx" class="links">Mizuho Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_264.xlsx" class="links">Model Co-operative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_226.xlsx" class="links">MUFG Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_223.xlsx" class="links">National Bank for Agriculture and Rural Development</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_123.xlsx" class="links">Nagpur Nagarik Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_245.xlsx" class="links">Nav Jeevan Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_51.xlsx" class="links">New India Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_52.xlsx" class="links">NKGSB Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_214.xlsx" class="links">North East Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_234.xlsx" class="links">NSDL Payments Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_53.xlsx" class="links">Nutan Nagarik Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_284.xlsx" class="links">Pavana Sahakari Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_205.xlsx" class="links">Paytm Payments Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_116.xlsx" class="links">Prime Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_190.xlsx" class="links">PT Bank Maybank Indonesia TBK</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_58.xlsx" class="links">Punjab and Sind Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_59.xlsx" class="links">Punjab National Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_212.xlsx" class="links">Qatar National Bank SAQ</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_117.xlsx" class="links">Rabobank International</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_220.xlsx" class="links">Rajarambapu Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_262.xlsx" class="links">Rajarshi Shahu Sahakari Bank Limited, Pune</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_250.xlsx" class="links">Rajasthan Marudhara Gramin Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_159.xlsx" class="links">Rajgurunagar Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_60.xlsx" class="links">Rajkot Nagrik Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_274.xlsx" class="links">Rajnandgaon District Central Co-operative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_88.xlsx" class="links">RBL Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_61.xlsx" class="links">Reserve Bank of India</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_186.xlsx" class="links">Samarth Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_246.xlsx" class="links">Sant Sopankaka Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_295.xlsx" class="links">Saptagiri Grameena Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_252.xlsx" class="links">Saraspur Nagrik Cooperative Bank Limited, Saraspur</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_90.xlsx" class="links">Saraswat Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_258.xlsx" class="links">Satara Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_287.xlsx" class="links">Saurashtra Gramin Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_137.xlsx" class="links">SBER Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_235.xlsx" class="links">SBM Bank India Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_166.xlsx" class="links">Shikshak Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_62.xlsx" class="links">Shinhan Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_289.xlsx" class="links">Shivalik Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_136.xlsx" class="links">Shri Chhatrapati Rajashri Shahu Urban Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_236.xlsx" class="links">Shri Veershaiv Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_286.xlsx" class="links">Shree Kadi Nagarik Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_282.xlsx" class="links">Smriti Nagrik Sahakari Bank Maryadit</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_233.xlsx" class="links">Sir M Visvesvaraya Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_63.xlsx" class="links">Societe Generale</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_153.xlsx" class="links">Solapur Janata Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_64.xlsx" class="links">South Indian Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif" border="0">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_273.xlsx" target="_blank" class="links">Sree Charan Souhardha Cooperative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_65.xlsx" class="links">Standard Chartered Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_68.xlsx" class="links">State Bank of India</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_265.xlsx" target="_blank" class="links">Suco Souharda Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_142.xlsx" class="links">Sumitomo Mitsui Banking Corporation</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_179.xlsx" class="links">Surat National Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_201.xlsx" class="links">Suryoday Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_129.xlsx" class="links">Sutex Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_74.xlsx" class="links">Tamilnad Mercantile Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_196.xlsx" class="links">Telangana State Coop Apex Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_203.xlsx" class="links">Textile Traders Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_244.xlsx" class="links">The Ajara Urban Cooperative Bank Limited, Ajara</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_119.xlsx" class="links">The A.P. Mahesh Cooperative Urban Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_147.xlsx" class="links">The Akola District Central Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_281.xlsx" class="links">The Akola Urban Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_277.xlsx" class="links">The Ahmednagar District Central Co-Operative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_101.xlsx" class="links">The Andhra Pradesh State Coop Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_75.xlsx" class="links">The Bank of Nova Scotia</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/content/docs/IFCB2009_275.xlsx" target="_blank" class="links">The Banaskantha Mercantile Cooperative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_199.xlsx" class="links">The Baramati Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_292.xlsx" class="links">The Burdwan Central Co-operative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_78.xlsx" class="links">The Cosmos Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_158.xlsx" class="links">The Delhi State Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_146.xlsx" class="links">The Gadchiroli District Central Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_80.xlsx" class="links">The Greater Bombay Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_120.xlsx" class="links">The Gujarat State Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_167.xlsx" class="links">The HASTI Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_149.xlsx" class="links">The Jalgaon Peopels Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_288.xlsx" class="links">The Kalyan Janata Sahakari Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_124.xlsx" class="links">The Kangra Central Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_164.xlsx" class="links">The Kangra Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_102.xlsx" class="links">The Karad Urban Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_83.xlsx" class="links">The Karanataka State Cooperative Apex Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_248.xlsx" class="links">The Kerala State Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_270.xlsx" class="links">The Kolhapur Urban Co-op Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_148.xlsx" class="links">The Kurmanchal Nagar Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/content/docs/IFCB2009_276.xlsx" target="_blank" class="links">The Malad Sahakari Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_285.xlsx" class="links">The Meghalaya Co-operative Apex Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_86.xlsx" class="links">The Mehsana Urban Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_114.xlsx" class="links">The Mumbai District Central Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_255.xlsx" class="links">The Muslim Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_122.xlsx" class="links">The Municipal Cooperative Bank Limited, Mumbai</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_87.xlsx" class="links">The Nainital Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_104.xlsx" class="links">The Nasik Merchants Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_197.xlsx" class="links">The Navnirman Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_268.xlsx" class="links">The Nawanagar Cooperative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_249.xlsx" class="links">The Nilambur Cooperative Urban Bank Limited, Nilambur</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_256.xlsx" class="links">The Odisha State Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_185.xlsx" class="links">The Pandharpur Urban Cooperative Bank Limited, Pandharpur</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_259.xlsx" class="links">The Pusad Urban Cooperative Bank Limited, Pusad</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_267.xlsx" class="links">The Punjab State Cooperative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_125.xlsx" class="links">The Rajasthan State Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_278.xlsx" class="links">The Satara District Central Cooperative Bank Ltd</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_91.xlsx" class="links">The Shamrao Vithal Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_206.xlsx" class="links">The Sindhudurg District Central Coop Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_126.xlsx" class="links">The Surat District Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_92.xlsx" class="links">The Surath Peoples Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_93.xlsx" class="links">The Tamil Nadu State Apex Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_118.xlsx" class="links">The Thane Bharat Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_144.xlsx" class="links">The Thane District Central Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_263.xlsx" class="links">The Udaipur Urban Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_243.xlsx" class="links">The Urban Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_135.xlsx" class="links">The Varachha Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_247.xlsx" class="links">The Vijay Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_127.xlsx" class="links">The Vishweshwar Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_95.xlsx" class="links">The West Bengal State Cooperative Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_165.xlsx" class="links">The Zoroastrian Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_177.xlsx" class="links">TJSB Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_138.xlsx" class="links">Tumkur Grain Merchants Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_96.xlsx" class="links">UCO Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_198.xlsx" class="links">Ujjivan Small Finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_97.xlsx" class="links">Union Bank of India</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_155.xlsx" class="links">United Overseas Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_290.xlsx" class="links">Unity Small finance Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_291.xlsx" class="links">Urban Co operative Bank Limited Bareilly</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_202.xlsx" class="links">Utkarsh Small Finance Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_257.xlsx" class="links">Uttar Pradesh Cooperative Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_230.xlsx" class="links">Vasai Janata Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_139.xlsx" class="links">Vasai Vikas Sahakari Bank Limited</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_128.xlsx" class="links">Woori Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_100.xlsx" class="links">Yes Bank</a>
                    </td>
                </tr>
                <tr>
                    <td align="center" valign="top">
                        <img src="https://www.rbi.org.in/images/bullet3.gif">
                    </td>
                    <td>
                        <a href="https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_156.xlsx" class="links">Zila Sahakri Bank Limited Ghaziabad</a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
"""

soup = BeautifulSoup(html_code, 'html.parser')

anchor_links = []

for link in soup.find_all('a', class_='links'):
    anchor_links.append({
        'text': link.get_text(strip=True),
        'href': link['href']
    })

json_result = json.dumps(anchor_links, indent=2)

# Save the JSON to a file
with open('anchor_links.json', 'w') as file:
    file.write(json_result)

print('Anchor links saved to anchor_links.json')

