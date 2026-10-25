import re
import gdown
import os

with open(r"C:\Users\sibbi\.gemini\antigravity-ide\brain\81b4418a-3019-4c4d-8b51-67f71454ca5d\.system_generated\steps\198\content.md", "r", encoding="utf-8") as f:
    text = f.read()

# Search for Flower .JPG and Girls who loves books.JPG
for target in ["Flower .JPG", "Girls who loves books.JPG", "clock.JPG"]:
    pos = text.find(target)
    if pos != -1:
        snippet = text[max(0, pos-400):pos+400]
        # Look for drive file IDs
        ids = re.findall(r'([a-zA-Z0-9_-]{28,35})', snippet)
        print(f"Target: {target}, found IDs: {ids}")
        for fid in ids:
            if len(fid) in [33, 32]:
                url = f"https://drive.google.com/uc?id={fid}"
                out = f"drive_products/Wooden Bookmarks/{target.replace(' ', '_')}"
                os.makedirs("drive_products/Wooden Bookmarks", exist_ok=True)
                try:
                    res = gdown.download(url, out, quiet=True)
                    if res and os.path.exists(out) and os.path.getsize(out) > 10000:
                        print(f"Successfully downloaded {target} to {out}")
                        break
                except Exception as e:
                    pass
