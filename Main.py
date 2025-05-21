import os
import requests
import urllib.parse
from bs4 import BeautifulSoup
from tqdm import tqdm
import settings

# CONFIGURATION
BASE_DOWNLOAD_DIR = "D:/roms"
URLS = [
    "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation/",
]
VALID_EXTENSIONS = [".zip", ".7z", ".iso", ".bin", ".img", ".nkit.iso", ".nkit.gcz", ".rvz", ".cue"]

def get_system_name(url):
    """Extract a folder-friendly system name from the URL."""
    return urllib.parse.unquote(url.rstrip("/").split("/")[-1])

def load_title_filters():
    """Load allowed base filenames from txt files per system."""
    filters = {}
    for system, file_path in settings.SYSTEM_TITLE_FILTERS.items():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                titles = set(line.strip().lower() for line in f if line.strip())
                filters[system] = titles
        except Exception as e:
            print(f"Warning: Could not load filter for {system}: {e}")
            filters[system] = set()
    return filters

def get_all_existing_filenames(base_dir):
    """Collect all filenames from the entire ROM download directory."""
    existing = set()
    for root, _, files in os.walk(base_dir):
        for file in files:
            existing.add(file)
    return existing

def scrape_rom_links(title_filters):
    rom_links = {}

    for url in URLS:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            system = get_system_name(url)
            rom_links[system] = []

            for link in soup.find_all('a'):
                href = link.get("href")
                if href and any(href.lower().endswith(ext) for ext in VALID_EXTENSIONS):
                    full_url = urllib.parse.urljoin(url, href)
                    filename = urllib.parse.unquote(href)
                    base_name = os.path.splitext(filename)[0].lower()

                    # Title filter check
                    if system in title_filters:
                        if not any(base_name.startswith(title) for title in title_filters[system]):
                            continue

                    rom_links[system].append(full_url)

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

    return rom_links

def download_roms(rom_links):
    existing_files = get_all_existing_filenames(BASE_DOWNLOAD_DIR)

    for system, urls in rom_links.items():
        system_dir = os.path.join(BASE_DOWNLOAD_DIR, system)
        os.makedirs(system_dir, exist_ok=True)

        for url in urls:
            filename = urllib.parse.unquote(url.split("/")[-1])
            dest_path = os.path.join(system_dir, filename)

            if filename in existing_files:
                print(f"Already exists in library: {filename}")
                continue

            try:
                print(f"Downloading: {filename}")
                with requests.get(url, stream=True, timeout=120) as r:
                    r.raise_for_status()
                    with open(dest_path, "wb") as f, tqdm(
                        total=int(r.headers.get("content-length", 0)),
                        unit="B", unit_scale=True, desc=filename
                    ) as bar:
                        for chunk in r.iter_content(chunk_size=1024):
                            f.write(chunk)
                            bar.update(len(chunk))
                print(f"Saved: {dest_path}")
                existing_files.add(filename)  # Add to dedup set after successful save
            except Exception as e:
                print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    title_filters = load_title_filters()
    rom_links = scrape_rom_links(title_filters)
    download_roms(rom_links)
