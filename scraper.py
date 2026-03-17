from scrape_ufc_stats_library import get_soup, get_event_urls
import requests

def get_ufc_data():
    # Direct link to London Event Stats
    url = "http://ufcstats.com/event-details/7f8379c614b03734"
    
    try:
        soup = get_soup(url)
        fights = []
        
        # This targets the specific table rows Greco's library looks for
        rows = soup.find_all('tr', class_='b-fight-details__table-row')
        
        for row in rows[1:]:  # Skip header
            cols = row.find_all('td')
            # Paragraph tags contain the fighter names
            names = cols[1].find_all('p')
            
            fights.append({
                "red_name": names[0].get_text(strip=True),
                "blue_name": names[1].get_text(strip=True),
                "weight": cols[6].get_text(strip=True),
                "red_record": "Live Stats", 
                "blue_record": "Live Stats"
            })
        return fights
    except Exception as e:
        print(f"Library Error: {e}")
        return []