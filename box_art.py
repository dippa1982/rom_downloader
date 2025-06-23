import hashlib
import requests
import os
from settings import SCREENSCRAPER_SYSTEM_IDS

def normalize_system_name(system_name):
    return system_name.lower().replace('-', ' ').replace('_', ' ').strip()

def download_box_art(rom_name, system_name, art_folder):
    key = normalize_system_name(system_name)
    system_id = SCREENSCRAPER_SYSTEM_IDS.get(key)
    if not system_id:
        print(f"[Error] System ID not found for system: '{system_name}' (normalized: '{key}')")
        return

    try:
        clean_name = rom_name.replace('_', ' ').replace('-', ' ').replace('.', ' ').strip()

        params = {
            "devid": "1",
            "devpassword": "hO1IspiRkXx",
            "output": "json",
            "romnom": clean_name,
            "systemeid": system_id,
            "ssid": "BPAlpha",
            "sspassword": "MLeo26wqk2y"
        }

        response = requests.get("https://www.screenscraper.fr/api2/jeuInfos.php", params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        jeu = data.get("jeu")
        if not jeu:
            print(f"No data found for {rom_name}")
            return

        media = jeu.get("medias", {}).get("media")
        if not media:
            print(f"No media found for {rom_name}")
            return

        front_image_url = None
        if isinstance(media, list):
            for item in media:
                if item.get("type") == "box-2D":
                    front_image_url = item.get("url")
                    break
        elif media.get("type") == "box-2D":
            front_image_url = media.get("url")

        if not front_image_url:
            print(f"No box art found for {rom_name}")
            return

        os.makedirs(art_folder, exist_ok=True)
        file_path = os.path.join(art_folder, f"{rom_name}.jpg")

        img_data = requests.get(front_image_url, timeout=10).content
        with open(file_path, 'wb') as f:
            f.write(img_data)

        print(f"[OK] Downloaded box art for {rom_name}")

    except Exception as e:
        print(f"[Exception] Failed to download box art for {rom_name}: {e}")
