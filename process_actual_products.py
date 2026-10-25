import os
import shutil
from PIL import Image

out_dir = os.path.join("assets", "products")
os.makedirs(out_dir, exist_ok=True)

# Helper to crop square and resize to 900x900 for fast high-res web display
def optimize_image(src_path, dest_name, size=(900, 900)):
    if not os.path.exists(src_path):
        print(f"Skipping {src_path}, does not exist")
        return False
    try:
        im = Image.open(src_path)
        im = im.convert("RGB")
        # Center crop to square or target aspect ratio
        w, h = im.size
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim
        im_cropped = im.crop((left, top, right, bottom))
        im_resized = im_cropped.resize(size, Image.Resampling.LANCZOS)
        dest_path = os.path.join(out_dir, dest_name)
        im_resized.save(dest_path, "JPEG", quality=88, optimize=True)
        print(f"Saved {dest_path} ({os.path.getsize(dest_path)} bytes)")
        return True
    except Exception as e:
        print(f"Error processing {src_path}: {e}")
        return False

# Actual items from the Google Drive
items = [
    ("drive_products/Acrylic coasters + Magnets/Lady TeaTrip.JPG", "lady_teatrip.jpg"),
    ("drive_products/Calendars/Artist Calender.JPG", "artist_calendar.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Formula 1.JPG", "f1_coaster.jpg"),
    ("drive_products/Calendars/Cat Calender.JPG", "cat_calendar.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Starry Nights.png", "starry_nights.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Chugli over Chai.png", "chugli_chai.jpg"),
    ("drive_products/Home Decor/Cherry Blossom.png", "cherry_blossom.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Pitstop_Yellow.JPG", "pitstop_racing.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Drink_Drank_Drunk.JPG", "drink_drank_drunk.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Lay Swagster.JPG", "lady_swagster.jpg")
]

for src, dest in items:
    optimize_image(src, dest)

print("Actual product optimization complete!")
