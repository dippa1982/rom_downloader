import os
import re
import requests
import urllib.parse
from bs4 import BeautifulSoup
from tqdm import tqdm
from zipfile import ZipFile
from settings import *

def load_title_filters():
    filters = {}
    for system, file_path in SYSTEM_TITLE_PATHS.items():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                titles = set(line.strip().lower() for line in f if line.strip())
                filters[system] = titles
        except Exception as e:
            print(f"Warning: Could not load filter for {system}: {e}")
            filters[system] = set()
    return filters

def get_system_name(url):
    raw_name = urllib.parse.unquote(url.rstrip("/").split("/")[-1])
    return SYSTEM_NAME_MAP.get(raw_name, raw_name)

def normalize_base_name(name):
    name = re.sub(r'\(.*?\)', '', name)  # Remove (...) tags
    name = re.sub(r'\[.*?\]', '', name)  # Remove [...] tags
    return name.strip().lower()

def extract_zip(zip_path, extract_to):
    print(f"Extracting {zip_path} to {extract_to}")
    try:
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Extracted: {zip_path} to {extract_to}")
    except Exception as e:
        print(f"Failed to extract {zip_path}: {e}")

def scrape_rom_links(title_filters):
    rom_links = {}
    for url in URLS:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            system = get_system_name(url)
            print(f"Scraping {system}")
            rom_links[system] = []

            for link in soup.find_all('a'):
                href = link.get("href")
                if not href or not any(href.lower().endswith(ext) for ext in VALID_EXTENSIONS):
                    continue

                full_url = urllib.parse.urljoin(url, href)
                filename = urllib.parse.unquote(href)
                base_name = os.path.splitext(filename)[0].lower()

                if system in title_filters and title_filters[system]:
                    if not any(base_name.startswith(title) for title in title_filters[system]):
                        continue

                rom_links[system].append(full_url)

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
    return rom_links

def download_roms(rom_links):
    for system, urls in rom_links.items():
        system_dir = os.path.join(BASE_DOWNLOAD_DIR, system)
        os.makedirs(system_dir, exist_ok=True)

        existing_normalized = {
            normalize_base_name(os.path.splitext(f)[0])
            for f in os.listdir(system_dir)
        }

        for url in urls:
            filename = urllib.parse.unquote(url.split("/")[-1])
            lower_filename = filename.lower()
            base_name = os.path.splitext(filename)[0]
            normalized_base = normalize_base_name(base_name)

            # Skip rev/demo/bios for all systems except Atari Lynx
            if system.lower() != "atari lynx" and any(tag in lower_filename for tag in DISALLOWED_TAGS):
                print(f"Skipping (rev/demo/bios): {filename}")
                continue

            # Skip region filtering for arcade only
            if system.lower() != "arcade":
                if not any(region in lower_filename for region in ALLOWED_REGIONS):
                    print(f"Skipping (region filter): {filename}")
                    continue

            # Skip if normalized name already exists in system folder
            if normalized_base in existing_normalized:
                print(f"Skipping duplicate (normalized match): {filename}")
                continue

            dest_path = os.path.join(system_dir, filename)
            base_name_no_ext = os.path.splitext(filename)[0]
            expected_folder = os.path.join(system_dir, base_name_no_ext)

            # Skip if extracted folder already exists
            if os.path.isdir(expected_folder):
                print(f"Skipping (folder exists): {expected_folder}")
                continue

            if os.path.exists(dest_path):
                print(f"Already exists (file): {filename}")
                continue

            try:
                print(f"Downloading: {system}: {filename}")
                temp_path = dest_path + ".part"
                with requests.get(url, stream=True, timeout=120) as r:
                    r.raise_for_status()
                    with open(temp_path, "wb") as f, tqdm(
                        total=int(r.headers.get("content-length", 0)),
                        unit="B", unit_scale=True, desc=filename
                    ) as bar:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                                bar.update(len(chunk))
                os.rename(temp_path, dest_path)
                print(f"Saved: {dest_path}")

                # Extract if ZIP and system requires it
                if system in SYSTEMS_TO_EXTRACT_ZIPS and dest_path.lower().endswith(".zip"):
                    extract_dir = os.path.join(system_dir, base_name_no_ext)
                    os.makedirs(extract_dir, exist_ok=True)
                    extract_zip(dest_path, extract_dir)
                    os.remove(dest_path)
                    print(f"Deleted zip: {dest_path}")

                existing_normalized.add(normalized_base)

            except Exception as e:
                print(f"Error downloading {filename}: {e}")
                if os.path.exists(temp_path):
                    os.remove(temp_path)

if __name__ == "__main__":
    title_filters = load_title_filters()
    rom_links = scrape_rom_links(title_filters)
    download_roms(rom_links)
