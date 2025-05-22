import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import unquote
from collections import defaultdict

# Output folder
OUTPUT_FOLDER = "scraped_roms"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ROM URLs to scrape
URLS = [
    #HANDHELDS
    #PSP
    'https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20Portable/',
    #Nintendo DS
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20DS%20(Decrypted)/",
    #Lynx
    "https://myrient.erista.me/files/No-Intro/Atari%20-%20Lynx%20%28LNX%29/",
    #Game gear
    "https://myrient.erista.me/files/No-Intro/Sega%20-%20Game%20Gear/",
    #NEOGEO POCKET
    "https://myrient.erista.me/files/No-Intro/SNK%20-%20NeoGeo%20Pocket%20Color/",
    #Game-boy
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy/",
    #GBA
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Advance/",     
    #GBC
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Color/",
    #CONSOLES
    #N64
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%2064%20(BigEndian)/",
    #NES
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20(Headered)/",     
    #SNES
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Super%20Nintendo%20Entertainment%20System/",
    #Mega Drive
    "https://myrient.erista.me/files/No-Intro/Sega%20-%20Mega%20Drive%20-%20Genesis/",
    #Atari 2600
    "https://myrient.erista.me/files/No-Intro/Atari%20-%202600/",
    #Atari 5200
    "https://myrient.erista.me/files/No-Intro/Atari%20-%205200/",
    #Atari 7800
    "https://myrient.erista.me/files/No-Intro/Atari%20-%207800/",
    #Arcadia 2001
    "https://myrient.erista.me/files/No-Intro/Emerson%20-%20Arcadia%202001/",
    #Sega 32X
    "https://myrient.erista.me/files/No-Intro/Sega%20-%2032X/",
    #Master System
    "https://myrient.erista.me/files/No-Intro/Sega%20-%20Master%20System%20-%20Mark%20III/",
    #TurboGrafx-16
    "https://myrient.erista.me/files/No-Intro/NEC%20-%20PC%20Engine%20-%20TurboGrafx-16/",
    #Sega CD
    'https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_segacd/CHD-MegaCD-PAL/',
    #Jaguar
    "https://myrient.erista.me/files/No-Intro/Atari%20-%20Jaguar%20%28ROM%29/",
    #Playstation
    "https://myrient.erista.me/files/Internet%20Archive/chadmaster/chd_psx/CHD-PSX-USA/",
    #Gamecube
    'https://myrient.erista.me/files/Redump/Nintendo%20-%20GameCube%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/',
    #Dreamcast
    'https://myrient.erista.me/files/Redump/Sega%20-%20Dreamcast/',
    #Gamecube
    'https://myrient.erista.me/files/Redump/Nintendo%20-%20GameCube%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/',
]

ROM_EXTENSIONS = ['.zip']
REGIONS = ['europe', 'usa']

def get_system_name(url):
    parts = [p for p in url.strip('/').split('/') if p]
    return unquote(parts[-1]).replace('%20', ' ').title()

def is_valid_rom(filename):
    decoded = unquote(filename).lower()
    return (
        any(decoded.endswith(ext) for ext in ROM_EXTENSIONS) and
        any(region in decoded for region in REGIONS)
    )

def get_base_rom_name(filename):
    decoded = unquote(os.path.splitext(filename)[0])
    name = re.sub(r"\s*\((.*?)\)", "", decoded)
    return name.strip()

rom_names_by_system = defaultdict(set)

for url in URLS:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        continue

    soup = BeautifulSoup(response.content, 'html.parser')
    system_name = get_system_name(url)
    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        if href and is_valid_rom(href):
            base_name = get_base_rom_name(href)
            rom_names_by_system[system_name].add(base_name)

# Save each system's ROM list to a separate .txt file
for system, roms in rom_names_by_system.items():
    filename = os.path.join(OUTPUT_FOLDER, f"{system}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        for rom_name in sorted(roms):
            f.write(rom_name + "\n")
    print(f"Saved {len(roms)} ROMs to {filename}")
