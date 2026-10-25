import gdown
import os

subfolders = {
    "Magnetic Bookmark": "1uSChrjqo8bhiUU8252Mbc1GN4bLqSX0R",
    "Wooden Bookmarks": "1qo7s-9Uyy9CYz82veBDX6T_bFiJDeMrW",
    "Photo Thread Art": "1fl13LSvBo4wcPtkGTbMhRrVGarBe3xyE",
    "Laptop Stickers + Magnets": "17usQHPY3hjw4bS9rCrVrRlvEpayLSjSC",
    "Personalized Handkerchief": "1-xksVUyRbKhXrGJ2b4kBLe8YM5GBqGTZ"
}

for name, fid in subfolders.items():
    out_dir = os.path.join("drive_products", name)
    os.makedirs(out_dir, exist_ok=True)
    url = f"https://drive.google.com/drive/folders/{fid}"
    print(f"Downloading {name}...")
    try:
        gdown.download_folder(url, output=out_dir, quiet=True, use_cookies=False)
        print(f"Finished {name}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")
