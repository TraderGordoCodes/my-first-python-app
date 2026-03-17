import requests
from bs4 import BeautifulSoup

def get_ufc_data():
    # Targeted ID for the London Card (Mar 21)
    url = "http://ufcstats.com/event-details/69108cb8b32efe04"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # FIND THE TABLE - The most important safety check
        table = soup.find('table', class_='b-fight-details__table')
        if not table:
            return []

        fights = []
        # Target the rows specifically
        rows = table.find_all('tr', class_='b-fight-details__table-row')
        
        for row in rows[1:]: # Skip the header row
            cols = row.find_all('td')
            if len(cols) < 7: continue
            
            # Pull names from the <p> tags Greco's library targets
            names = cols[1].find_all('p')
            weight = cols[6].get_text(strip=True)
            
            fights.append({
                "red_name": names[0].get_text(strip=True),
                "blue_name": names[1].get_text(strip=True),
                "weight": weight,
                "red_record": "LIVE",
                "blue_record": "LIVE"
            })
        return fights
    except Exception as e:
        print(f"Scraper Error: {e}")
        return []