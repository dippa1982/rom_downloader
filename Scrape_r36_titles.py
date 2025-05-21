from bs4 import BeautifulSoup
import requests

url = 'https://r36s.co.uk/blogs/news/r36s-game-list'
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Request failed: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
h2_elements = soup.find_all('h2')

with open('r36s_titles_with_list.txt', 'w', encoding='utf-8') as f:
    for h2 in h2_elements:
        header = h2.get_text(strip=True)
        f.write(f"{header}\n")

        # Look for the next sibling that contains <li> elements
        next_sibling = h2.find_next_sibling()
        while next_sibling and not next_sibling.find_all('li'):
            next_sibling = next_sibling.find_next_sibling()

        if next_sibling:
            li_items = next_sibling.find_all('li')
            for li in li_items:
                item_text = li.get_text(strip=True)
                if item_text:
                    f.write(f"{item_text}\n")
        
        f.write('\n')  # Separate sections with a blank line

print("Scraping complete. Output saved to r36s_titles_with_list.txt.")
