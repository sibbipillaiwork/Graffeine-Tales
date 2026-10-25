import json

# Load base 37 products from products_data.json
with open('products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Ensure proper unicode characters in categories
for p in products:
    p['category'] = p['category'].replace('', '•').replace('?', '•')
    if 'filterCat' not in p or not p['filterCat']:
        p['filterCat'] = p['category'].lower()

# Add high-fidelity editions for the remaining subcategories: Journals & Bulk Orders
# so that all 5 requested categories have complete representation
journals_and_bulk = [
    {
        "id": "prod-38",
        "name": "The Atelier Hardcover Linen Journal (Plain)",
        "category": "Journals • Plain Journals",
        "filterCat": "journals plain stationery",
        "price": 899,
        "mrp": 1199,
        "badge": "Heirloom Edition",
        "badgeType": "gold",
        "image": "assets/cat_journals.jpg",
        "rating": 5.0,
        "reviews": 142,
        "desc": "Hand-bound archival linen hardcover journal featuring 120 GSM bleedproof warm ivory bamboo paper. Flat-lay stitch binding, gold foiled ribbon bookmark, and back accordion pocket.",
        "specs": ["Pages: 192 bleedproof unruled archival pages", "Binding: 180° Lay-flat thread binding", "Cover: Natural tactile woven book-cloth linen", "Paper: 120 GSM fountain-pen friendly warm bamboo paper"]
    },
    {
        "id": "prod-39",
        "name": "Slow Mornings & Reflections Guided Journal (Prompted)",
        "category": "Journals • Prompted Journals",
        "filterCat": "journals prompted stationery",
        "price": 999,
        "mrp": 1299,
        "badge": "Mindful Living",
        "badgeType": "sage",
        "image": "assets/cat_journals.jpg",
        "rating": 4.9,
        "reviews": 118,
        "desc": "A 90-day daily introspective companion curated with mindful creative prompts, coffee musings, gratitude trackers, and weekly art reflection spaces.",
        "specs": ["90 Days of structured creative prompts and reflection", "Dimensions: A5 (148 x 210 mm) compact hardcover", "Foil-stamped spine with dual satin ribbon markers", "Includes bespoke illustrated mindfulness sticker sheet"]
    },
    {
        "id": "prod-40",
        "name": "Corporate Welcome & Appreciation Desk Hamper",
        "category": "Bulk Orders • Corporate",
        "filterCat": "bulk corporate gifting",
        "price": 2899,
        "mrp": 3800,
        "badge": "Bulk Tier (10+ Units)",
        "badgeType": "gold",
        "image": "assets/cat_bulk.jpg",
        "rating": 5.0,
        "reviews": 68,
        "desc": "Custom corporate onboarding gift box comprising custom logo acrylic coasters with teakwood easels, 2026 desk calendar, bespoke linen journal, and brass pen.",
        "specs": ["Minimum Order Quantity: 10 sets (Tiered pricing available)", "Full company logo laser engraving & custom foil packaging", "Includes custom handwritten welcome cards on seeded paper", "Delivery: Pan-India studio courier with individual dispatch"]
    },
    {
        "id": "prod-41",
        "name": "Custom Celebration Favours & Milestone Box",
        "category": "Bulk Orders • Events & Birthday",
        "filterCat": "bulk events gifting birthday",
        "price": 1950,
        "mrp": 2500,
        "badge": "Custom Favours",
        "badgeType": "sage",
        "image": "assets/cat_events.jpg",
        "rating": 4.9,
        "reviews": 52,
        "desc": "Curated celebration favors for milestone birthdays, intimate weddings, and festive gatherings. Includes personalized acrylic coasters, floral door tags, and bespoke packaging.",
        "specs": ["Custom guest name personalization on each keepsake", "Eco-luxe rigid magnetic gift box with satin bow", "Custom color palette matched to your event theme", "Bulk discount tiers from 15 to 500+ units"]
    }
]

existing_ids = {p['id'] for p in products}
for jb in journals_and_bulk:
    if jb['id'] not in existing_ids:
        products.append(jb)

print(f"Total catalog products: {len(products)}")

with open('products_data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("Saved updated products_data.json successfully!")
