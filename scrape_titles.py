import os
import re
import requests
from bs4 import BeautifulSoup

def sanitize_filename(name):
    """Sanitize string to be a safe filename."""
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def remove_parentheses(text):
    """Remove anything in parentheses, including the parentheses."""
    return re.sub(r'\s*\([^)]*\)', '', text).strip()

def scrape_and_save(url, output_dir="output"):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for h2 in soup.find_all('h2'):
        title = h2.get_text(strip=True)
        filename = sanitize_filename(title) + ".txt"
        file_path = os.path.join(output_dir, filename)

        ol_items = []
        next_elem = h2.find_next_sibling()
        while next_elem and next_elem.name != 'h2':
            if next_elem.name == 'ol':
                ol_items = [remove_parentheses(li.get_text(strip=True)) for li in next_elem.find_all('li')]
                break
            elif next_elem.find('ol'):
                ol = next_elem.find('ol')
                ol_items = [remove_parentheses(li.get_text(strip=True)) for li in ol.find_all('li')]
                break
            next_elem = next_elem.find_next_sibling()

        if ol_items:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(ol_items))
            print(f"Saved: {file_path}")
        else:
            print(f"No <ol> found for section: {title}")

# Example usage
url = "https://r36s.co.uk/blogs/news/r36s-game-list"
scrape_and_save(url)
