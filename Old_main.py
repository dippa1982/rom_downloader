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

def get_existing_basenames(system_dir):
    if not os.path.exists(system_dir):
        return set()
    return {os.path.splitext(f)[0].lower() for f in os.listdir(system_dir)}

def strip_region_and_rev_tags(name):
    return re.sub(r'\s*(\((europe|usa|rev \d+|rev [0-9]+|demo)\)|\[bios\])', '', name, flags=re.IGNORECASE).strip()

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
                if not href or not any(href.lower().endswith(ext) for ext in VALID_EXTENSIONS):
                    continue

                full_url = urllib.parse.urljoin(url, href)
                filename = urllib.parse.unquote(href)
                base_name = os.path.splitext(filename)[0].lower()

                if system in title_filters:
                    if not any(base_name.startswith(title) for title in title_filters[system]):
                        continue

                rom_links[system].append(full_url)

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
    return rom_links

def extract_zip(zip_path, extract_to_dir):
    try:
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_dir)
        print(f"Extracted to: {extract_to_dir}")
    except Exception as e:
        print(f"Error extracting {zip_path}: {e}")

def download_roms(rom_links):
    allowed_regions = ['(europe)', '(usa)']
    skip_revs = ['(rev 1)', '(rev 2)', '(rev 3)', '(rev 4)', '(rev 5)', '(demo)', '[bios]']

    for system, urls in rom_links.items():
        system_dir = os.path.join(BASE_DOWNLOAD_DIR, system)
        os.makedirs(system_dir, exist_ok=True)

        existing_basenames = get_existing_basenames(system_dir)
        europe_basenames = {
            strip_region_and_rev_tags(name)
            for name in existing_basenames
            if "(europe)" in name
        }

        for url in urls:
            filename = urllib.parse.unquote(url.split("/")[-1])
            lower_filename = filename.lower()
            base_name = os.path.splitext(lower_filename)[0]
            stripped_base = strip_region_and_rev_tags(base_name)

            # Skip if (Europe) version already exists for this stripped title
            if stripped_base in europe_basenames and "(europe)" not in base_name:
                print(f"Skipping: {filename} — (Europe) version already exists")
                continue

            # Skip if already exists
            if base_name in existing_basenames:
                print(f"Skipping duplicate: {filename}")
                continue

            # Skip if not in allowed region
            if not any(region in lower_filename for region in allowed_regions):
                print(f"Skipping (region filter): {filename}")
                continue

            # Skip if rev/demo/bios
            if any(rev in lower_filename for rev in skip_revs):
                print(f"Skipping (rev filter): {filename}")
                continue

            dest_path = os.path.join(system_dir, filename)
            if os.path.exists(dest_path):
                print(f"Already exists (file): {filename}")
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

                # Update basenames to prevent re-download
                existing_basenames.add(base_name)
                if "(europe)" in base_name:
                    europe_basenames.add(stripped_base)

                # Extract ZIP if system is listed
                if system in SYSTEMS_TO_EXTRACT_ZIPS and dest_path.lower().endswith(".zip"):
                    extract_dir = os.path.join(system_dir, os.path.splitext(filename)[0])
                    os.makedirs(extract_dir, exist_ok=True)
                    extract_zip(dest_path, extract_dir)

            except Exception as e:
                print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    title_filters = load_title_filters()
    rom_links = scrape_rom_links(title_filters)
    download_roms(rom_links)
