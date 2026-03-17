import requests
from bs4 import BeautifulSoup

def get_ufc_data():
    # This is the exact ID for the London 2026 card on UFCStats
    url = "http://ufcstats.com/event-details/69108cb8b32efe04"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # We need to find the table first. If this is None, we return empty to avoid the crash.
        table = soup.find('table', class_='b-fight-details__table')
        if not table:
            print("Table not found - page layout may have changed.")
            return []

        fights = []
        rows = table.find_all('tr', class_='b-fight-details__table-row')
        
        for row in rows:
            # Greco's logic uses 'b-fight-details__table-text' for fighter names
            names = row.find_all('p', class_='b-fight-details__table-text')
            
            if len(names) >= 2:
                fights.append({
                    "red_name": names[0].get_text(strip=True),
                    "blue_name": names[1].get_text(strip=True),
                    "weight": row.find_all('td')[6].get_text(strip=True),
                    "red_record": "Live",
                    "blue_record": "Live"
                })
        
        # The first row is usually empty/header, so we return from index 1 onwards
        return fights[1:] if len(fights) > 1 else fights

    except Exception as e:
        print(f"Scrape failed: {e}")
        return []