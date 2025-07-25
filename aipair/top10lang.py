# List top 10 programming languages from tiobe.com 

import requests
from bs4 import BeautifulSoup   
def get_top_languages():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to load page")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'top20'})
    
    languages = []
    for row in table.find_all('tr')[1:11]:  # Skip header and get top 10
        cols = row.find_all('td')
        language = cols[4].text.strip()  # Language name is in the 4th column
        languages.append(language)
    
    return languages


if __name__ == "__main__":
    try:
        top_languages = get_top_languages()
        print("Top 10 Programming Languages:")
        for i, lang in enumerate(top_languages, start=1):
            print(f"{i}. {lang}")
    except Exception as e:
        print(f"Error: {e}")

        