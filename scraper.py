import requests
from bs4 import BeautifulSoup

def get_ufc_data(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    fights = []
    # UFC uses 'c-listing-athlete__name' and 'c-listing-athlete__record' classes
    # This logic finds each fight card block on the event page
    listings = soup.find_all('div', class_='c-listing-fight')
    
    for fight in listings:
        red_corner = fight.find('div', class_='c-listing-fight__corner--red')
        blue_corner = fight.find('div', class_='c-listing-fight__corner--blue')
        
        if red_corner and blue_corner:
            fights.append({
                "red_name": red_corner.find('div', class_='c-listing-athlete__name').text.strip(),
                "red_record": red_corner.find('div', class_='c-listing-athlete__record').text.strip(),
                "blue_name": blue_corner.find('div', class_='c-listing-athlete__name').text.strip(),
                "blue_record": blue_corner.find('div', class_='c-listing-athlete__record').text.strip(),
                "weight": fight.find('div', class_='c-listing-fight__weight-class').text.strip()
            })
    return fights