import os

URLS = [
    #Sega SG1000
    "https://myrient.erista.me/files/No-Intro/Sega%20-%20SG-1000/",
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
    #Saturn
    "https://myrient.erista.me/files/Redump/Sega%20-%20Saturn/",
    #Playstation
    "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation/",
    #Dreamcast
    "https://myrient.erista.me/files/Redump/Sega%20-%20Dreamcast/",
    #Gamecube
    'https://myrient.erista.me/files/Redump/Nintendo%20-%20GameCube%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/',
    #Sega CD
    'https://myrient.erista.me/files/Redump/Sega%20-%20Mega%20CD%20%26%20Sega%20CD/',
    #Sega Niomi
    "https://myrient.erista.me/files/Redump/Arcade%20-%20Sega%20-%20Naomi/",
    #Jaguar CD
    "https://myrient.erista.me/files/Redump/Atari%20-%20Jaguar%20CD%20Interactive%20Multimedia%20System/",
    #Jaguar
    "https://myrient.erista.me/files/Internet%20Archive/chadmaster/jagcd-chd-zstd/jagcd-chd-zstd/",
    #TurboGrafx-CD
    "https://myrient.erista.me/files/Redump/NEC%20-%20PC%20Engine%20CD%20&%20TurboGrafx%20CD/",
    #3DO
    "https://myrient.erista.me/files/Redump/Panasonic%20-%203DO%20Interactive%20Multiplayer/",
    #CD-I
    "https://myrient.erista.me/files/Redump/Philips%20-%20CD-i/",
    #NeoGeo CD
    "https://myrient.erista.me/files/Redump/SNK%20-%20Neo%20Geo%20CD/",
    #Retroarch files
    "https://myrient.erista.me/files/Internet%20Archive/chadmaster/RetroarchSystemFiles/Retroarch-System/",
]

SCREENSCRAPER_SYSTEM_IDS = {
    "pc engine cd": 114,
    "turbografx cd": 114,
    "nes": 3,
    "snes": 4,
    "mastersystem": 2,
    "sega genesis": 6,
    "game boy": 7,
    "gba": 10,
    "nintendo 64": 14,
    "gamecube": 11,
    "playstation": 7,
    "ps2": 8,
    "psp": 13,
    "dreamcast": 23,
    "wii": 9,
    "arcade": 75,
    "atari lynx": 12,
    "sega saturn": 10,
    "sega cd": 12,
    "neogeo pocket color": 15,
    "neogeo pocket": 16,
    "turbo grafx 16": 5,
    "turbo grafx cd": 18,
    "atari 2600": 19,
    "atari 5200": 20,
    "atari 7800": 21,
    "sega 32x": 22,
    "sega master system": 24,
    "emerson arcadia 2001": 25,
    "neogeo cd": 26,
    "jaguar cd": 30,
    "3do": 28,
    "atari jaguar cd": 171,
    "sega SG-1000": 29,
}

BASE_DOWNLOAD_DIR = "D:/roms"

VALID_EXTENSIONS = ['.zip', '.7z', '.chd', '.iso', '.nkit.iso', '.nkit.gcz', '.gdi', '.rvz']

ALLOWED_REGIONS = ["(europe)", "(usa)",'(world)']

DISALLOWED_TAGS = ["proto","(rev 1)", "(rev 2)", "(rev 3)", "(demo)", "[bios]",'(unl)','(aftermarket)','(beta)']

SYSTEMS_TO_EXTRACT_ZIPS = [
    'PSP',
    'Gamecube',
    'Sega Saturn',
    'Sony - PlayStation',
    'Dreamcast',
    'Sega Mega CD',
]

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
PAN3DO_TITLES = "filters/3DO.txt"

SYSTEM_TITLE_PATHS = {
    "3DO": PAN3DO_TITLES,
    "Gamecube": GAMECUBE_TITLES,
    "Sega Mega CD": SEGA_CD_TITLES,
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

SYSTEM_NAME_MAP = {
    "jagcd-chd-zstd": "Atari Jaguar",
    "Panasonic - 3DO Interactive Multiplayer": "3DO",
    "Atari - Jaguar CD Interactive Multimedia System": "Atari Jaguar CD",
    "Nintendo - GameCube - NKit RVZ [zstd-19-128k]": "Gamecube",
    "Nintendo - Nintendo 64 (BigEndian)": "N64",
    "Nintendo - Nintendo Entertainment System (Headered)": "NES",
    "Nintendo - Super Nintendo Entertainment System": "SNES",
    "Sega - Game Gear": "Game Gear",
    "Sega - Saturn": "Sega Saturn",
    "Sega - Mega Drive - Genesis": "Sega Mega Drive",
    "Sega - Mega CD & Sega CD": "Sega Mega CD",
    "Nintendo - Game Boy": "Game Boy",
    "Nintendo - Game Boy Advance": "Game Boy Advance",
    "Nintendo - Game Boy Color": "Game Boy Color",
    "Atari 2600": "Atari 2600",
    "Atari 5200": "Atari 5200",
    "Atari 7800": "Atari 7800",
    "Emerson - Arcadia 2001": "Arcadia 2001",
    "Sega - Dreamcast": "Dreamcast",
    "Sega - 32X": "Sega 32X",
    "Sega - Master System - Mark III": "Sega Master System",
    "NEC - PC Engine - TurboGrafx-16": "TurboGrafx-16",
    "Nintendo - Nintendo DS (Decrypted)": "Nintendo DS",
    "Sony - PlayStation Portable": "PSP",
    "CHD-PSX-USA": "Sony - PlayStation",
}