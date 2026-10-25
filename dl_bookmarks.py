import gdown
import os
from PIL import Image

fids = {
    "wooden_bookmark_flower.jpg": "1GOPxAQmcaniOsjUyuRWgJ428X6p-0N8W",
    "wooden_bookmark_girls.jpg": "1Uokxpb4WAM_8rmfbi2WR8g9r3vQadLst",
    "wooden_bookmark_clock.jpg": "1w0JT51yR7CqQIaX1XfnaBWh1w2PUTFyI"
}

out_dir = os.path.join("assets", "products")
os.makedirs(out_dir, exist_ok=True)
os.makedirs(os.path.join("drive_products", "Wooden Bookmarks"), exist_ok=True)

for fname, fid in fids.items():
    raw_path = os.path.join("drive_products", "Wooden Bookmarks", fname)
    print(f"Downloading {fname}...")
    try:
        gdown.download(id=fid, output=raw_path, quiet=False)
        if os.path.exists(raw_path) and os.path.getsize(raw_path) > 1000:
            im = Image.open(raw_path).convert("RGB")
            w, h = im.size
            min_dim = min(w, h)
            left = (w - min_dim) // 2
            top = (h - min_dim) // 2
            im_cropped = im.crop((left, top, left + min_dim, top + min_dim))
            im_resized = im_cropped.resize((900, 900), Image.Resampling.LANCZOS)
            final_path = os.path.join(out_dir, fname)
            im_resized.save(final_path, "JPEG", quality=88, optimize=True)
            print(f"Optimized to {final_path} ({os.path.getsize(final_path)} bytes)")
    except Exception as e:
        print(f"Error {fname}: {e}")
