from googletrans import Translator
import psycopg2
import base64
import urllib.request
from requests_html import HTML,HTMLSession
from bs4 import BeautifulSoup

conn = psycopg2.connect(
   database="VTYS", user='postgres', password='ONURonur44', host='127.0.0.1', port= '5432'
)
class translate:
    sentence=""
    def cevir(self,sentence,dest):
        translator=Translator()
        self.sentence=sentence
        trans=translator.translate(sentence,dest=dest).text
        return trans
LANGUAGES = {'AX': 'Åland',
             'SX': 'Saint Martin',
             'CW': 'Cook Islands',
             'AD': 'Andorra',
             'AE': 'United Arab Emirates', 'AF': 'Afghanistan', 'AG': 'Antigua and Barbuda', 'AI': 'Anguilla', 'AL': 'Albania', 'AM': 'Armenia', 'AN': 'Netherlands Antilles', 'AO': 'Angola', 'AQ': 'Antarctica', 'AR': 'Argentina', 'AS': 'American Samoa', 'AT': 'Austria', 'AU': 'Australia', 'AW': 'Aruba', 'AZ': 'Azerbaijan', 'BA': 'Bosnia and Herzegovina', 'BB': 'Barbados', 'BD': 'Bangladesh', 'BE': 'Belgium', 'BF': 'Burkina Faso', 'BG': 'Bulgaria', 'BH': 'Bahrain', 'BI': 'Burundi', 'BJ': 'Benin', 'BM': 'Bermuda', 'BN': 'Brunei', 'BO': 'Bolivia', 'BR': 'Brazil', 'BS': 'Bahamas', 'BT': 'Bhutan', 'BV': 'Bouvet Island', 'BW': 'Botswana', 'BY': 'Belarus', 'BZ': 'Belize', 'CA': 'Canada', 'CC': 'Cocos [Keeling] Islands', 'CD': 'Congo [DRC]', 'CF': 'Central African Republic', 'CG': 'Congo [Republic]', 'CH': 'Switzerland', 'CI': "Côte d'Ivoire", 'CK': 'Cook Islands', 'CL': 'Chile', 'CM': 'Cameroon', 'CN': 'China', 'CO': 'Colombia', 'CR': 'Costa Rica', 'CU': 'Cuba', 'CV': 'Cape Verde', 'CX': 'Christmas Island', 'CY': 'Cyprus', 'CZ': 'Czech Republic', 'DE': 'Germany', 'DJ': 'Djibouti', 'DK': 'Denmark', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'DZ': 'Algeria', 'EC': 'Ecuador', 'EE': 'Estonia', 'EG': 'Egypt', 'EH': 'Western Sahara', 'ER': 'Eritrea', 'ES': 'Spain', 'ET': 'Ethiopia', 'FI': 'Finland', 'FJ': 'Fiji', 'FK': 'Falkland Islands [Islas Malvinas]', 'FM': 'Micronesia', 'FO': 'Faroe Islands', 'FR': 'France', 'GA': 'Gabon', 'GB': 'United Kingdom', 'GD': 'Grenada', 'GE': 'Georgia', 'GF': 'French Guiana', 'GG': 'Guernsey', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GL': 'Greenland', 'GM': 'Gambia', 'GN': 'Guinea', 'GP': 'Guadeloupe', 'GQ': 'Equatorial Guinea', 'GR': 'Greece', 'GS': 'South Georgia and the South Sandwich Islands', 'GT': 'Guatemala', 'GU': 'Guam', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'GZ': 'Gaza Strip', 'HK': 'Hong Kong', 'HM': 'Heard Island and McDonald Islands', 'HN': 'Honduras', 'HR': 'Croatia', 'HT': 'Haiti', 'HU': 'Hungary', 'ID': 'Indonesia', 'IE': 'Ireland', 'IL': 'Israel', 'IM': 'Isle of Man', 'IN': 'India', 'IO': 'British Indian Ocean Territory', 'IQ': 'Iraq', 'IR': 'Iran', 'IS': 'Iceland', 'IT': 'Italy', 'JE': 'Jersey', 'JM': 'Jamaica', 'JO': 'Jordan', 'JP': 'Japan', 'KE': 'Kenya', 'KG': 'Kyrgyzstan', 'KH': 'Cambodia', 'KI': 'Kiribati', 'KM': 'Comoros', 'KN': 'Saint Kitts and Nevis', 'KP': 'North Korea', 'KR': 'South Korea', 'KW': 'Kuwait', 'KY': 'Cayman Islands', 'KZ': 'Kazakhstan', 'LA': 'Laos', 'LB': 'Lebanon', 'LC': 'Saint Lucia', 'LI': 'Liechtenstein', 'LK': 'Sri Lanka', 'LR': 'Liberia', 'LS': 'Lesotho', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'LV': 'Latvia', 'LY': 'Libya', 'MA': 'Morocco', 'MC': 'Monaco', 'MD': 'Moldova', 'ME': 'Montenegro', 'MG': 'Madagascar', 'MH': 'Marshall Islands', 'MK': 'Macedonia [FYROM]', 'ML': 'Mali', 'MM': 'Myanmar [Burma]', 'MN': 'Mongolia', 'MO': 'Macau', 'MP': 'Northern Mariana Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MS': 'Montserrat', 'MT': 'Malta', 'MU': 'Mauritius', 'MV': 'Maldives', 'MW': 'Malawi', 'MX': 'Mexico', 'MY': 'Malaysia', 'MZ': 'Mozambique', 'NA': 'Namibia', 'NC': 'New Caledonia', 'NE': 'Niger', 'NF': 'Norfolk Island', 'NG': 'Nigeria', 'NI': 'Nicaragua', 'NL': 'Netherlands', 'NO': 'Norway', 'NP': 'Nepal', 'NR': 'Nauru', 'NU': 'Niue', 'NZ': 'New Zealand', 'OM': 'Oman', 'PA': 'Panama', 'PE': 'Peru', 'PF': 'French Polynesia', 'PG': 'Papua New Guinea', 'PH': 'Philippines', 'PK': 'Pakistan', 'PL': 'Poland', 'PM': 'Saint Pierre and Miquelon', 'PN': 'Pitcairn Islands', 'PR': 'Puerto Rico', 'PS': 'Palestinian Territories', 'PT': 'Portugal', 'PW': 'Palau', 'PY': 'Paraguay', 'QA': 'Qatar', 'RE': 'Réunion', 'RO': 'Romania', 'RS': 'Serbia', 'RU': 'Russia', 'RW': 'Rwanda', 'SA': 'Saudi Arabia', 'SB': 'Solomon Islands', 'SC': 'Seychelles', 'SD': 'Sudan', 'SE': 'Sweden', 'SG': 'Singapore', 'SH': 'Saint Helena', 'SI': 'Slovenia', 'SJ': 'Svalbard and Jan Mayen', 'SK': 'Slovakia', 'SL': 'Sierra Leone', 'SM': 'San Marino', 'SN': 'Senegal', 'SO': 'Somalia', 'SR': 'Suriname', 'ST': 'São Tomé and Príncipe', 'SV': 'El Salvador', 'SY': 'Syria', 'SZ': 'Swaziland', 'TC': 'Turks and Caicos Islands', 'TD': 'Chad', 'TF': 'French Southern Territories', 'TG': 'Togo', 'TH': 'Thailand', 'TJ': 'Tajikistan', 'TK': 'Tokelau', 'TL': 'Timor-Leste', 'TM': 'Turkmenistan', 'TN': 'Tunisia', 'TO': 'Tonga', 'TR': 'Turkey', 'TT': 'Trinidad and Tobago', 'TV': 'Tuvalu', 'TW': 'Taiwan', 'TZ': 'Tanzania', 'UA': 'Ukraine', 'UG': 'Uganda', 'UM': 'U.S. Minor Outlying Islands', 'US': 'United States', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VA': 'Vatican City', 'VC': 'Saint Vincent and the Grenadines', 'VE': 'Venezuela', 'VG': 'British Virgin Islands', 'VI': 'U.S. Virgin Islands', 'VN': 'Vietnam', 'VU': 'Vanuatu', 'WF': 'Wallis and Futuna', 'WS': 'Samoa', 'XK': 'Kosovo', 'YE': 'Yemen', 'YT': 'Mayotte', 'ZA': 'South Africa', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}

urls=list()
c=True
for i in LANGUAGES.keys():
    country_code = i
    country = LANGUAGES[i]
    translator = Translator()
    session = HTMLSession()
    search_param = translator.translate("{} tüm şehirler ".format(country), "en")
    print(search_param.text)
    r = session.get('https://www.google.com/search?q={}&hl={}'.format(search_param.text, country_code))
    soup = BeautifulSoup(r.text, "html.parser")
    cursor = conn.cursor()
    a=0
    for i in soup.find_all('div', attrs={'class': 'yuRUbf'}):
        link=i.a['href']
        script = '''INSERT INTO urls_sehir(url,ulke_kod,ulke) 
                        VALUES (%s,%s,%s)'''
        parametre=(str(link).strip(), country_code,country)
        cursor.execute(script,parametre)
        print("url :{} ülke kodu: {} ulke: {}".format(link, country_code, country))
        conn.commit()


