import os

def read_titles(file_path):
    print(f"Reading title filter file: {file_path}")
    if not os.path.exists(file_path):
        print(f"Missing title filter file: {file_path}")
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        titles = [line.strip().replace("'", "").replace(",", "") for line in file if line.strip()]
    return titles

# settings.py

URLS = [
    #Lynx
    "https://myrient.erista.me/files/No-Intro/Atari%20-%20Lynx%20%28LNX%29/",
    #Game gear
    "https://myrient.erista.me/files/No-Intro/Sega%20-%20Game%20Gear/",
    #NEOGEO POCKET COLOR
    "https://myrient.erista.me/files/No-Intro/SNK%20-%20NeoGeo%20Pocket%20Color/",
    #Game-boy
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy/",
    #GBA
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Advance/",     
    #GBC
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Game%20Boy%20Color/",
    #Nintendo DS
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20DS%20(Decrypted)/",
    #PSP
    'https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20Portable/',
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
    #Jaguar CD
    "https://myrient.erista.me/files/Internet%20Archive/chadmaster/jagcd-chd-zstd/jagcd-chd-zstd/",
    #Jaguar
    "https://myrient.erista.me/files/No-Intro/Atari%20-%20Jaguar%20%28ROM%29/",
    #Saturn
    "https://myrient.erista.me/files/Redump/Sega%20-%20Saturn/",
    #Playstation
    "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation/",
    #Dreamcast
    "https://myrient.erista.me/files/Redump/Sega%20-%20Dreamcast/",
    #MAME/FBA
    'https://myrient.erista.me/files/Internet%20Archive/chadmaster/fbnarcade-fullnonmerged/arcade/'
]

BASE_DOWNLOAD_DIR = "D:/roms"

SYSTEMS_TO_EXTRACT_ZIPS = [
    'PSP',
    'Gamecube',
    'Sony - PlayStation',
    'Dreamcast',
    'Sega Mega CD',
]

TEMP_DOWNLOAD_DIR = "C:/temp_roms"
BASE_DOWNLOAD_DIR = "D:/roms"

PSP_TITLES = "filters/PSP.txt"
GAMECUBE_TITLES = "filters/Nintendo - Gamecube.txt"
GAMEGEAR_TITLES = "filters/GAMEGEAR.txt"
SATURN_TITLES = "filters/SATURN.txt"
NINTENDO_DS_TITLES = "filters/Nintendo DS.txt"
NEOGEO_POCKET_COLOR_TITLES = "filters/NEOGEOCOLOR.txt"
NEOGEO_POCKET_TITLES = "filters/NEOGEOPOCKET.txt"
DREAMCAST_TITLES = "filters/DREAMCAST.txt"
N64_TITLES = "filters/N64.txt"
PSONE_TITLES = "filters/PSONE.txt"
GAMECUBE_TITLES = "filters/GAMECUBE.txt"
GBA_TITLES = "filters/GBA.txt"
GBC_TITLES = "filters/GBC.txt"
LYNX_TITLES = "filters/LYNX.txt"
NES_TITLES = "filters/NES.txt"
SUPER_NINTENDO_TITLES = "filters/SNES.txt"
SEGA_MEGA_DRIVE_TITLES = "filters/MEGADRIVE.txt"
SEGA_MASTER_SYSTEM_TITLES = "filters/MASTERSYSTEM.txt"
SEGA_CD_TITLES = "filters/SEGACD.txt"

SYSTEM_TITLE_PATHS = {
    "Gamecube": GAMECUBE_TITLES,
    "Sega CD": SEGA_CD_TITLES,
    "Game Gear": GAMEGEAR_TITLES,
    "Sega Saturn": SATURN_TITLES,
    "N64": N64_TITLES,
    "Dreamcast": DREAMCAST_TITLES,
    "Sony - PlayStation": PSONE_TITLES,
    "Nintendo - Game Boy Color": GBC_TITLES,
    "Nintendo - Game Boy Advance": GBA_TITLES,
    "NES": NES_TITLES,
    "SNES": SUPER_NINTENDO_TITLES,
    "Sega - Mega Drive - Genesis": SEGA_MEGA_DRIVE_TITLES,
    "Sega Master System": SEGA_MASTER_SYSTEM_TITLES,
    "Nintendo DS": NINTENDO_DS_TITLES,
    "PSP": PSP_TITLES,
}

SYSTEM_TITLE_FILTERS = {
    "Gamecube": read_titles(GAMECUBE_TITLES),
    "Sega CD": read_titles(SEGA_CD_TITLES),
    "Game Gear": read_titles(GAMEGEAR_TITLES),
    "Sega Saturn": read_titles(SATURN_TITLES),
    "N64": read_titles(N64_TITLES),
    "Dreamcast": read_titles(DREAMCAST_TITLES),
    "Sony - PlayStation": read_titles(PSONE_TITLES),
    "Nintendo - Game Boy Color": read_titles(GBC_TITLES),
    "Nintendo - Game Boy Advance": read_titles(GBA_TITLES),
    "NES": read_titles(NES_TITLES),
    "SNES": read_titles(SUPER_NINTENDO_TITLES),
    "Sega - Mega Drive - Genesis": read_titles(SEGA_MEGA_DRIVE_TITLES),
    "Sega Master System": read_titles(SEGA_MASTER_SYSTEM_TITLES),
    "Nintendo DS": read_titles(NINTENDO_DS_TITLES),
    "PSP": read_titles(PSP_TITLES),
}

SYSTEM_NAME_MAP = {
    "Nintendo - GameCube - NKit RVZ [zstd-19-128k]": "Gamecube",
    "CHD-MegaCD-PAL": "Sega CD",
    "Atari - Jaguar (ROM)": "Atari Jaguar",
    "Nintendo - Nintendo 64 (BigEndian)": "N64",
    "Nintendo - Nintendo Entertainment System (Headered)": "NES",
    "Nintendo - Super Nintendo Entertainment System": "SNES",
    "Sega - Game Gear": "Game Gear",
    "Sega - Saturn": "Sega Saturn",
    "Sega - Mega Drive": "Sega Mega Drive",
    "Sega - Mega CD & Sega CD": "Sega Mega CD",
    "Game Boy": "Game Boy",
    "GBA": "Game Boy Advance",
    "GBC": "Game Boy Color",
    "Atari 2600": "Atari 2600",
    "Atari 5200": "Atari 5200",
    "Atari 7800": "Atari 7800",
    "Atari - Lynx (LNX)": "Atari Lynx",
    "Atari ST": "Atari ST",
    "Arcadia 2001": "Arcadia 2001",
    "Sega - Dreamcast": "Dreamcast",
    "SNK - NeoGeo Pocket": "NeoGeo Pocket",
    "Sega - 32X": "Sega 32X",
    "Sega - Master System - Mark III": "Sega Master System",
    "NEC - PC Engine - TurboGrafx-16": "TurboGrafx-16",
    "jagcd-chd-zstd": "Jaguar CD",
    "Nintendo - Nintendo DS (Decrypted)": "Nintendo DS",
    "Sony - PlayStation Portable": "PSP",
    "CHD-PSX-USA": "Sony - PlayStation",
}

# Allowed file extensions
VALID_EXTENSIONS = [".zip", ".7z", ".iso", ".bin", ".img", ".nkit.iso", ".nkit.gcz", ".rvz", ".cue"]

# List of ROM categories
TEMP_URLS = [
   #HANDHELDS
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
    #Nintendo DS
    "https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20DS%20(Decrypted)/",
    #PSP
    'https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%20Portable/',
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
    #Jaguar CD
    "https://myrient.erista.me/files/Internet%20Archive/chadmaster/jagcd-chd-zstd/jagcd-chd-zstd/",
    #Jaguar
    "https://myrient.erista.me/files/No-Intro/Atari%20-%20Jaguar%20%28ROM%29/",
    #Saturn
    "https://myrient.erista.me/files/Redump/Sega%20-%20Saturn/",
    #Playstation
    "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation/",
    #Dreamcast
    "https://myrient.erista.me/files/Redump/Sega%20-%20Dreamcast/",
]

