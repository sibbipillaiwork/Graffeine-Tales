import json
import re

with open('products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

def clean_str(s):
    if not isinstance(s, str):
        return s
    # Remove null bytes and non-printable control characters
    s = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', s)
    s = s.replace('\ufffd', '')
    return s.strip()

for p in products:
    p['id'] = clean_str(p['id'])
    p['name'] = clean_str(p['name'])
    p['badge'] = clean_str(p.get('badge', ''))
    p['badgeType'] = clean_str(p.get('badgeType', 'gold'))
    p['desc'] = clean_str(p.get('desc', ''))
    if 'specs' in p:
        p['specs'] = [clean_str(x) for x in p['specs']]

    # Determine exact category group
    name_l = p['name'].lower()
    pid = p['id']

    if pid in ['prod-2', 'prod-10', 'prod-11']: # Calendars
        p['category'] = 'Stationaries • Desk Calendars & Planners'
        p['categoryGroup'] = 'stationaries'
    elif pid in ['prod-4', 'prod-5', 'prod-23', 'prod-24', 'prod-25', 'prod-26', 'prod-27', 'prod-28', 'prod-29']: # Bookmarks
        p['category'] = 'Stationaries • Bookmarks'
        p['categoryGroup'] = 'stationaries'
    elif pid in ['prod-30', 'prod-31', 'prod-32', 'prod-33']: # Stickers
        p['category'] = 'Stationaries • Stickers'
        p['categoryGroup'] = 'stationaries'
    elif pid in ['prod-38']: # Plain journal
        p['category'] = 'Journals • Plain Journals'
        p['categoryGroup'] = 'journals'
    elif pid in ['prod-39']: # Prompted journal
        p['category'] = 'Journals • Prompted Journals'
        p['categoryGroup'] = 'journals'
    elif pid in ['prod-1', 'prod-6', 'prod-9', 'prod-12', 'prod-13', 'prod-14', 'prod-15', 'prod-16', 'prod-17', 'prod-18', 'prod-19', 'prod-20', 'prod-21', 'prod-22']: # Coasters
        p['category'] = 'Handcrafted Décor • Coaster'
        p['categoryGroup'] = 'decor'
    elif pid in ['prod-7', 'prod-36', 'prod-37']: # Wall Hanging
        p['category'] = 'Handcrafted Décor • Wall Hanging'
        p['categoryGroup'] = 'decor'
    elif pid in ['prod-3']: # Door Hanger
        p['category'] = 'Handcrafted Décor • Door Hanger'
        p['categoryGroup'] = 'decor'
    elif pid in ['prod-8', 'prod-34', 'prod-35']: # Photo thread art
        p['category'] = 'Events & Gifting • Personalized Gifting'
        p['categoryGroup'] = 'events'
    elif pid in ['prod-40']: # Corporate hamper
        p['category'] = 'Bulk Orders • Corporate'
        p['categoryGroup'] = 'bulk'
    elif pid in ['prod-41']: # Celebration favours
        p['category'] = 'Bulk Orders • Events & Birthday'
        p['categoryGroup'] = 'bulk'
    else:
        # Fallback detection
        if 'stationar' in p.get('category', '').lower() or 'calendar' in name_l or 'bookmark' in name_l:
            p['categoryGroup'] = 'stationaries'
        elif 'journal' in p.get('category', '').lower():
            p['categoryGroup'] = 'journals'
        elif 'decor' in p.get('category', '').lower() or 'coaster' in name_l:
            p['categoryGroup'] = 'decor'
        elif 'event' in p.get('category', '').lower() or 'thread' in name_l:
            p['categoryGroup'] = 'events'
        elif 'bulk' in p.get('category', '').lower():
            p['categoryGroup'] = 'bulk'
        else:
            p['categoryGroup'] = 'decor'

# Tag specific items for New Launch and Bestsellers
new_launch_ids = {'prod-2', 'prod-10', 'prod-11', 'prod-39', 'prod-37', 'prod-9'}
bestseller_ids = {'prod-1', 'prod-6', 'prod-5', 'prod-4', 'prod-3', 'prod-8', 'prod-38', 'prod-31'}

for p in products:
    p['isNewLaunch'] = p['id'] in new_launch_ids
    p['isBestseller'] = p['id'] in bestseller_ids
    if p['isNewLaunch'] and not p['badge']:
        p['badge'] = 'New Launch'
        p['badgeType'] = 'sage'
    elif p['isBestseller'] and not p['badge']:
        p['badge'] = 'Bestseller'
        p['badgeType'] = 'gold'

# Verify counts per categoryGroup
groups = {}
for p in products:
    g = p['categoryGroup']
    groups[g] = groups.get(g, 0) + 1

print("Sanitized products:", len(products))
print("Category counts:", groups)

with open('products_data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("Saved clean products_data.json!")
