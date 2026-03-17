import requests
from bs4 import BeautifulSoup

def get_ufc_data(url="http://ufcstats.com/statistics/events/upcoming"):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first upcoming event link
        event_link = soup.find('td', class_='b-statistics__table-col').find('a')['href']
        
        # Now scrape that specific event page
        event_response = requests.get(event_link, headers=headers)
        event_soup = BeautifulSoup(event_response.text, 'html.parser')
        
        fights = []
        rows = event_soup.find_all('tr', class_='b-fight-details__table-row')[1:] # Skip header
        
        for row in rows:
            cols = row.find_all('td')
            # Greco's logic for parsing names from the table
            fighters = cols[1].find_all('a')
            weight = cols[6].get_text(strip=True)
            
            if len(fighters) >= 2:
                fights.append({
                    "red_name": fighters[0].get_text(strip=True),
                    "blue_name": fighters[1].get_text(strip=True),
                    "red_record": "See Stats", # Records on ufcstats require a 3rd click
                    "blue_record": "See Stats",
                    "weight": weight
                })
        return fights
    except Exception as e:
        print(f"Greco-style scrape failed: {e}")
        return []