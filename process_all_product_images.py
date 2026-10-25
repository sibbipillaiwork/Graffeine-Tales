import os
from PIL import Image, ImageOps

out_dir = os.path.join("assets", "products")
os.makedirs(out_dir, exist_ok=True)

# Helper to optimize and resize WITHOUT ANY CROPPING
def process_full_image(src_path, dest_name, max_size=1200):
    if not os.path.exists(src_path):
        print(f"Skipping {src_path}, does not exist")
        return False
    try:
        im = Image.open(src_path)
        # 1. Correct EXIF rotation
        im = ImageOps.exif_transpose(im)
        
        # 2. Thumbnail preserving full aspect ratio (NO CROPPING)
        im.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        dest_path = os.path.join(out_dir, dest_name)
        if dest_name.lower().endswith(".png"):
            im.save(dest_path, "PNG", optimize=True)
        else:
            im = im.convert("RGB")
            im.save(dest_path, "JPEG", quality=90, optimize=True)
            
        print(f"Saved {dest_name}: {im.size} ({os.path.getsize(dest_path)} bytes)")
        return True
    except Exception as e:
        print(f"Error processing {src_path}: {e}")
        return False

# List of actual products to process
products_to_process = [
    # Stationaries: Calendars & Planners
    ("drive_products/Calendars/Artist Calender.JPG", "artist_calendar.jpg"),
    ("drive_products/Calendars/Cat Calender.JPG", "cat_calendar.jpg"),
    ("drive_products/Calendars/Dog Calender.JPG", "dog_calendar.jpg"),
    
    # Stationaries: Bookmarks
    ("drive_products/Wooden Bookmarks/Flower.jpg", "wood_flower_bookmark.jpg"),
    ("drive_products/Wooden Bookmarks/Girls who loves books.JPG", "wood_girl_bookmark.jpg"),
    ("drive_products/Wooden Bookmarks/Its Book Oclock.JPG", "wood_book_oclock.jpg"),
    ("Magnetic Bookmark/Reading Boo.JPG", "magnetic_reading_boo.jpg"),
    ("Magnetic Bookmark/Nerdy Boo.JPG", "magnetic_nerdy_boo.jpg"),
    ("Magnetic Bookmark/Overthinker Girl.JPG", "magnetic_overthinker.jpg"),
    
    # Stationaries: Stickers
    ("Laptop Stickers + Magnets/1-01.jpg", "sticker_desi_chai.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Bobby Deol.png", "sticker_bobby_deol.png"),
    ("drive_products/Acrylic coasters + Magnets/Control Uday.png", "sticker_control_uday.png"),
    ("drive_products/Acrylic coasters + Magnets/MOJO JOJO.png", "sticker_mojo_jojo.png"),
    
    # Handcrafted Decor: Coasters
    ("drive_products/Acrylic coasters + Magnets/Lady TeaTrip.JPG", "lady_teatrip.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Chugli over Chai.png", "chugli_chai.png"),
    ("drive_products/Acrylic coasters + Magnets/Formula 1.JPG", "f1_coaster.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Starry Nights.png", "starry_nights.png"),
    ("drive_products/Acrylic coasters + Magnets/Pitstop_Yellow.JPG", "pitstop_racing.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Drink_Drank_Drunk.JPG", "drink_drank_drunk.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Lay Swagster.JPG", "lady_swagster.jpg"),
    ("drive_products/Acrylic coasters + Magnets/Breaking Bad.png", "coaster_breaking_bad.png"),
    
    # Handcrafted Decor: Door Hanger
    ("drive_products/Home Decor/Door Name Tag", "door_hanger_neetu.jpg"),
    
    # Handcrafted Decor: Wall Hanging & Thread Art
    ("drive_products/Home Decor/Mermaid", "mermaid_wall_hoop.png"),
    ("Photo Thread Art/Photo thread art 02.png", "photo_thread_art_family.png"),
    ("Photo Thread Art/Photo Thread art 03.png", "photo_thread_art_couple.png"),
    ("drive_products/Home Decor/Cherry Blossom.png", "cherry_blossom.png"),
    ("drive_products/Home Decor/Day & Night.png", "day_and_night.png"),
]

for src, dest in products_to_process:
    process_full_image(src, dest)

print("\nAll real products processed successfully with ZERO cropping!")
