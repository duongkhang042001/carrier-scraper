import requests
from bs4 import BeautifulSoup
import json

def scrape_carrier_list(url):
    carriers = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        carrier_table = soup.find('table', {'class': 'table', 'class': 'table-responsive', 'class': 'table-striped'})
        if carrier_table:
            rows = carrier_table.find_all('tr')
            for row in rows[1:]:
                cols = row.find_all('td')
                code = cols[0].text.strip()
                operator = cols[1].text.strip()
                country = cols[2].text.strip()
                detail_link = cols[1].find('a')['href']
                carrier_data = {
                    "Code": code,
                    "Operator": operator,
                    "Country": country,
                    "DetailLink": f"https://www.imei.info{detail_link}"
                }
                carriers.append(carrier_data)
    return carriers

def scrape_carrier_details(url):
    details = {}
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        details_table = soup.find('table', {'class': 'table', 'class': 'table-responsive', 'class': 'free_check_result', 'class': 'text-center', 'class': 'carrier_details_table'})
        if details_table:
            rows = details_table.find_all('tr')
            for row in rows:
                th = row.find('th').text.strip()
                td = row.find('td').text.strip()
                details[th] = td
    return details

def main():
    all_carriers = []
    for page_num in range(1, 48):  # 47 pages
        url = f"https://www.imei.info/carriers/?page={page_num}"
        print(f"Scraping carrier list page {page_num}...")
        carriers = scrape_carrier_list(url)
        all_carriers.extend(carriers)
    
    detailed_carriers = []
    for carrier in all_carriers:
        print(f"Scraping details for {carrier['Operator']}...")
        details = scrape_carrier_details(carrier['DetailLink'])
        carrier.update(details)
        detailed_carriers.append(carrier)
    
    with open("detailed_carriers_data.json", "w") as f:
        json.dump(detailed_carriers, f, indent=4)
    print("All data scraped and saved to detailed_carriers_data.json.")

if __name__ == "__main__":
    main()
