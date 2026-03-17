import requests
from bs4 import BeautifulSoup

def get_ufc_data(url):
    # This "User-Agent" makes you look like a real person on Chrome
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # If the UFC blocks us, this will raise an error we can catch
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        fights = []
        
        # New selectors for the 2026 site layout
        listings = soup.select('.c-listing-fight') 
        
        for fight in listings:
            # We use .select_one to safely find names and records
            red_name = fight.select_one('.c-listing-fight__corner--red .c-listing-athlete__name')
            blue_name = fight.select_one('.c-listing-fight__corner--blue .c-listing-athlete__name')
            red_rec = fight.select_one('.c-listing-fight__corner--red .c-listing-athlete__record')
            blue_rec = fight.select_one('.c-listing-fight__corner--blue .c-listing-athlete__record')
            weight = fight.select_one('.c-listing-fight__weight-class')

            if red_name and blue_name:
                fights.append({
                    "red_name": red_name.get_text(strip=True),
                    "blue_name": blue_name.get_text(strip=True),
                    "red_record": red_rec.get_text(strip=True) if red_rec else "0-0-0",
                    "blue_record": blue_rec.get_text(strip=True) if blue_rec else "0-0-0",
                    "weight": weight.get_text(strip=True) if weight else "TBD"
                })
        
        return fights

    except Exception as e:
        print(f"Scrape failed: {e}")
        return []