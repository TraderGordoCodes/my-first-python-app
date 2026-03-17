import requests
from bs4 import BeautifulSoup

def get_ufc_data():
    # Targeted ID for the London Card (Mar 21, 2026)
    url = "http://ufcstats.com/event-details/69108cb8b32efe04"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'http://ufcstats.com/statistics/events/upcoming'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Check if we actually got a 200 OK response
        if response.status_code != 200:
            print(f"UFC Stats blocked us (Status {response.status_code})")
            return get_backup_data()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # SAFETY GATE: Check if the table exists before calling .find_all()
        table = soup.find('table', class_='b-fight-details__table')
        if not table:
            print("Table not found on page. Using backup.")
            return get_backup_data()

        fights = []
        rows = table.find_all('tr', class_='b-fight-details__table-row')
        
        for row in rows[1:]: # Skip the header
            cols = row.find_all('td')
            if len(cols) < 7: continue
            
            names = cols[1].find_all('p')
            if len(names) >= 2:
                fights.append({
                    "red_name": names[0].get_text(strip=True),
                    "blue_name": names[1].get_text(strip=True),
                    "weight": cols[6].get_text(strip=True),
                    "red_record": "LIVE",
                    "blue_record": "LIVE"
                })
        
        return fights if fights else get_backup_data()

    except Exception as e:
        print(f"Scraper Error: {e}")
        return get_backup_data()

def get_backup_data():
    """Returns the verified London card if the scraper is blocked."""
    return [
        {"red_name": "Movsar Evloev", "blue_name": "Lerone Murphy", "weight": "Featherweight"},
        {"red_name": "Luke Riley", "blue_name": "Aswell Jr.", "weight": "Featherweight"},
        {"red_name": "Michael Page", "blue_name": "Patterson", "weight": "Welterweight"},
        {"red_name": "Iwo Baraniewski", "blue_name": "Austen Lane", "weight": "Light Heavyweight"},
        {"red_name": "Roman Dolidze", "blue_name": "Chris Duncan", "weight": "Middleweight"},
        {"red_name": "Kurtis Campbell", "blue_name": "Danny Silva", "weight": "Featherweight"},
        {"red_name": "Mason Jones", "blue_name": "Axel Sola", "weight": "Lightweight"},
        {"red_name": "Nathaniel Wood", "blue_name": "Losene Keita", "weight": "Featherweight"}
    ]