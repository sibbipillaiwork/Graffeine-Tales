/**
 * GRAFFEINE TALES — D2C SHOPIFY LUXURY COMMERCE SUITE
 * High-Fidelity Interactive Architecture
 * Enhanced with UI/UX Pro Max Design Intelligence
 */

const productsData = [
  {
    "id": "prod-1",
    "name": "Lady TeaTrip Acrylic Coaster & Teak Stand",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 699,
    "mrp": 899,
    "badge": "Bestseller",
    "badgeType": "gold",
    "image": "assets/products/lady_teatrip.jpg",
    "rating": 5.0,
    "reviews": 214,
    "desc": "Vibrant desi pop art illustration printed on premium scratch-resistant acrylic with a solid teakwood display easel. Designed to bring humor, character, and warmth to your tea and coffee tables.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Material: High-gloss 4mm shatterproof optical acrylic",
      "Includes solid grooved teakwood easel stand",
      "Waterproof, heat-resistant up to 100°C and wipe-clean"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": true
  },
  {
    "id": "prod-2",
    "name": "Progress Not Perfection — 2026 Desk Calender",
    "category": "Stationaries • Desk Calendars & Planners",
    "filterCat": "calendar stationaries",
    "price": 850,
    "mrp": 1100,
    "badge": "Studio Drop",
    "badgeType": "sage",
    "image": "assets/products/artist_calendar.jpg",
    "rating": 4.9,
    "reviews": 148,
    "desc": "Interactive artist tool desk calendar featuring 12 die-cut stationery cards in a rich indigo holder with an artisanal wooden easel. Daily inspiration for painters, writers, and dreamers.",
    "specs": [
      "Includes 12 monthly illustrated die-cut cards",
      "Cardstock: Premium 350 GSM textured matte archival paper",
      "Handcrafted grooved teakwood easel stand included",
      "Packaging: Sustainable kraft gift sleeve with gold foil seal"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": true,
    "isBestseller": false
  },
  {
    "id": "prod-3",
    "name": "Personalized Floral Wooden Hoop Door Name Tag",
    "category": "Handcrafted Décor • Door Hanger",
    "filterCat": "decor door gifting",
    "price": 1250,
    "mrp": 1599,
    "badge": "Artisanal",
    "badgeType": "gold",
    "image": "assets/products/door_hanger_neetu.jpg",
    "rating": 5.0,
    "reviews": 184,
    "desc": "Handcrafted embroidery hoop door name plaque featuring botanical floral wreath and custom couple or family initials. Hung with natural jute rope on solid wood entryways.",
    "specs": [
      "Diameter: 8-inch solid beechwood embroidery hoop",
      "Fabric: Pure unbleached organic linen",
      "Hand-embroidered anchor thread botanicals",
      "Custom name personalization available upon order"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": true
  },
  {
    "id": "prod-4",
    "name": "Handcrafted Wooden Sunflower Bookmark with Tassel",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 349,
    "mrp": 450,
    "badge": "Hand-Carved",
    "badgeType": "sage",
    "image": "assets/products/wood_flower_bookmark.jpg",
    "rating": 4.9,
    "reviews": 162,
    "desc": "Laser-engraved and hand-painted botanical sunflower wooden bookmark crafted from natural birchwood, finished with an elegant royal blue silk tassel for avid readers.",
    "specs": [
      "Material: Sustainable 2mm natural birch wood",
      "Hand-painted sunflower botanical artwork",
      "Royal blue silk tassel included",
      "Protective natural matte sealant"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": true
  },
  {
    "id": "prod-5",
    "name": "Reading Boo Die-Cut Magnetic Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 249,
    "mrp": 350,
    "badge": "Studio Favorite",
    "badgeType": "gold",
    "image": "assets/products/magnetic_reading_boo.jpg",
    "rating": 5.0,
    "reviews": 240,
    "desc": "Cute whimsical die-cut magnetic bookmark featuring little ghost 'Boo' engrossed in a book atop a stack of vintage novels. Dual-sided magnetic grip that never damages book pages.",
    "specs": [
      "Dual neodymium magnets for secure grip",
      "Laminated water-resistant finish",
      "Non-creasing and paper safe",
      "Compact 60 x 40 mm clip size"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": true
  },
  {
    "id": "prod-6",
    "name": "Chugli Over Chai — Duo Coaster & Magnet Set",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 599,
    "mrp": 750,
    "badge": "Viral Pick",
    "badgeType": "gold",
    "image": "assets/products/chugli_chai.png",
    "rating": 5.0,
    "reviews": 310,
    "desc": "Our viral 'Aao Bhai Chugli Karein' & 'Aao Behen Chugli Karein' duo. Functions as heavy-duty acrylic drink coasters or high-grade fridge magnets for spicy gossip and steaming adrak chai.",
    "specs": [
      "Quantity: Set of 2 dual-use Coasters + Fridge Magnets",
      "Material: 4mm Shatterproof Acrylic",
      "Neodymium flush-mount magnet back",
      "Wipe-clean glossy UV print"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": true
  },
  {
    "id": "prod-7",
    "name": "Mermaid Hand-Embroidered Hoop Wall Hanging",
    "category": "Handcrafted Décor • Wall Hanging",
    "filterCat": "decor wall",
    "price": 1850,
    "mrp": 2200,
    "badge": "Heirloom",
    "badgeType": "gold",
    "image": "assets/products/mermaid_wall_hoop.png",
    "rating": 5.0,
    "reviews": 96,
    "desc": "Exquisite hand-stitched hoop artwork portraying a serene mermaid with flowing embroidered waves and origami boat accent. Mounted on textured natural fabric inside a smooth wooden hoop.",
    "specs": [
      "Diameter: 9-inch circular beechwood hoop",
      "Over 14 hours of artisan hand-embroidery",
      "Ready-to-hang brass hardware",
      "Unique numbered studio release"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-8",
    "name": "Bespoke Photo Thread Art Keepsake Frame",
    "category": "Events & Gifting • Personalized Gifting",
    "filterCat": "gifting decor",
    "price": 2499,
    "mrp": 3200,
    "badge": "Custom Heirloom",
    "badgeType": "gold",
    "image": "assets/products/photo_thread_art_family.png",
    "rating": 5.0,
    "reviews": 74,
    "desc": "Transform your cherished family portraits or wedding memories into heirloom art. Fine archival photographic print enhanced with intricate hand-embroidered concentric thread patterns in a luxury wood frame.",
    "specs": [
      "Dimensions: 8 x 10 inch solid wood table/wall frame",
      "Custom hand-stitched thread art over customer photo",
      "Museum-grade acid-free mount board",
      "Includes luxury protective gift packaging"
    ],
    "categoryGroup": "events",
    "isNewLaunch": false,
    "isBestseller": true
  },
  {
    "id": "prod-9",
    "name": "Monaco F1 Hex Checkered Acrylic Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 649,
    "mrp": 799,
    "badge": "Racing Series",
    "badgeType": "sage",
    "image": "assets/products/f1_coaster.jpg",
    "rating": 4.9,
    "reviews": 92,
    "desc": "Sleek monochrome hexagonal grid and Formula 1 inspired artwork on precision-cut circular acrylic with rubber dampeners. The perfect desk companion for Grand Prix race weekends.",
    "specs": [
      "Diameter: 100 mm circular cut",
      "Material: Laser-cut frosted & gloss acrylic",
      "Base: Non-slip acoustic rubber dampeners",
      "Scratch-resistant UV printing"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": true,
    "isBestseller": false
  },
  {
    "id": "prod-10",
    "name": "Curious Whiskers 2026 Desk Calender",
    "category": "Stationaries • Desk Calendars & Planners",
    "filterCat": "calendar stationaries",
    "price": 850,
    "mrp": 1100,
    "badge": "Studio Drop",
    "badgeType": "sage",
    "image": "assets/products/cat_calendar.jpg",
    "rating": 4.9,
    "reviews": 84,
    "desc": "Feline-inspired whimsical desk companion with custom die-cut monthly cards and wooden display easel for cat lovers and slow morning enthusiasts.",
    "specs": [
      "12 Die-cut monthly illustrated cards",
      "350 GSM premium archival paper",
      "Handcrafted teakwood easel stand",
      "Plastic-free gift packaging"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": true,
    "isBestseller": false
  },
  {
    "id": "prod-11",
    "name": "Loyal Companions 2026 Dog Desk Calender",
    "category": "Stationaries • Desk Calendars & Planners",
    "filterCat": "calendar stationaries",
    "price": 850,
    "mrp": 1100,
    "badge": "Pet Series",
    "badgeType": "sage",
    "image": "assets/products/dog_calendar.jpg",
    "rating": 4.9,
    "reviews": 78,
    "desc": "Heartwarming monthly illustrations of dog breeds and joyful canine moments on die-cut cardstock with a handcrafted solid wooden display stand.",
    "specs": [
      "12 Die-cut monthly illustrated cards",
      "350 GSM matte textured art paper",
      "Solid grooved wooden easel stand included",
      "Gift-ready presentation box"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": true,
    "isBestseller": false
  },
  {
    "id": "prod-12",
    "name": "Starry Nights Fine Art Acrylic Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 499,
    "mrp": 650,
    "badge": "Art Edition",
    "badgeType": "gold",
    "image": "assets/products/starry_nights.png",
    "rating": 4.8,
    "reviews": 112,
    "desc": "Swirling nocturnal celestial art on lustrous glossy acrylic. Brings painterly elegance to bedside tables, studio desks, and quiet reading nooks.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Material: 4mm High-clarity optical acrylic",
      "Anti-slip cork base backing",
      "Heat resistant up to 100°C"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-13",
    "name": "Pitstop Yellow Speed Racing Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 649,
    "mrp": 799,
    "badge": "Limited",
    "badgeType": "gold",
    "image": "assets/products/pitstop_yellow.jpg",
    "rating": 4.9,
    "reviews": 67,
    "desc": "High-octane yellow and matte charcoal automotive pitstop graphic coaster with precision debossed rims and rubber backing.",
    "specs": [
      "Diameter: 100 mm round",
      "Automotive grade durable print",
      "Acoustic silicone dampeners",
      "Collectible racer series"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-14",
    "name": "Pitstop Red Monza Racing Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 649,
    "mrp": 799,
    "badge": "Scuderia Red",
    "badgeType": "gold",
    "image": "assets/products/pitstop_red.jpg",
    "rating": 4.9,
    "reviews": 73,
    "desc": "Fiery Italian racing red circular coaster celebrating speed, apex corners, and motorsport culture with rubberized non-slip feet.",
    "specs": [
      "Diameter: 100 mm circular",
      "Material: High-impact acrylic",
      "Non-slip anti-vibration base",
      "Heat and water resistant"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-15",
    "name": "Drink Drank Drunk Pop Art Coaster & Stand",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 699,
    "mrp": 899,
    "badge": "Party Pick",
    "badgeType": "sage",
    "image": "assets/products/drink_drank_drunk.jpg",
    "rating": 4.9,
    "reviews": 128,
    "desc": "Witty typographic drink coaster with vibrant retro pop accents and a natural wooden display stand. Perfect for weekend cocktail bars and house parties.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Material: High gloss shatterproof acrylic",
      "Teakwood easel stand included",
      "Waterproof and alcohol resistant"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-16",
    "name": "Lady Swagster Desi Chic Coaster & Stand",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 699,
    "mrp": 899,
    "badge": "Desi Chic",
    "badgeType": "gold",
    "image": "assets/products/lady_swagster.jpg",
    "rating": 5.0,
    "reviews": 142,
    "desc": "Celebration of bold modern Indian aesthetics — featuring vibrant shades, aviator sunglasses, and ornate bridal jewelry in a modern pop art portrait.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Material: Optical grade 4mm acrylic",
      "Includes solid teak display easel",
      "High-definition fade-proof print"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-17",
    "name": "Heisenberg 'Say My Name' Acrylic Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 499,
    "mrp": 650,
    "badge": "Cult Classic",
    "badgeType": "sage",
    "image": "assets/products/coaster_breaking_bad.png",
    "rating": 4.8,
    "reviews": 95,
    "desc": "Iconic chemical periodic table graphic and portrait tribute for pop culture aficionados and serious desk setups.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Material: 4mm scratch-resistant acrylic",
      "Cork backing for scratch-free tables",
      "UV cured long-lasting colors"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-18",
    "name": "Animal Kingdom Wildlife Art Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 499,
    "mrp": 650,
    "badge": "Artisan",
    "badgeType": "sage",
    "image": "assets/products/coaster_animal_kingdom.png",
    "rating": 4.9,
    "reviews": 64,
    "desc": "Intricate wildlife mandala illustration capturing the spirit of the jungle on high-gloss transparent acrylic.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "High-clarity optical resin",
      "Cork backed protective base",
      "Washable surface"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-19",
    "name": "Lord Bobby Cult Pop Acrylic Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 499,
    "mrp": 650,
    "badge": "Cult Meme",
    "badgeType": "gold",
    "image": "assets/products/coaster_bobby_deol.png",
    "rating": 5.0,
    "reviews": 182,
    "desc": "The internet's beloved Lord Bobby avatar transformed into a tongue-in-cheek desk coaster and fridge magnet conversation starter.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Dual-use: Coaster + Fridge magnet",
      "Glossy scratchproof finish",
      "Made in India with love"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-20",
    "name": "Control Uday Desi Meme Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 499,
    "mrp": 650,
    "badge": "Desi Humour",
    "badgeType": "gold",
    "image": "assets/products/coaster_control_uday.png",
    "rating": 5.0,
    "reviews": 210,
    "desc": "Legendary 'Control Uday Control' Bollywood comedy dialogue rendered with expressive character caricature for high-stress work desks.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Heavyweight 4mm acrylic",
      "Silicone feet backing",
      "Instant mood booster"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-21",
    "name": "Mojo Jojo Cartoon Pop Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 499,
    "mrp": 650,
    "badge": "Nostalgia",
    "badgeType": "sage",
    "image": "assets/products/coaster_mojo_jojo.png",
    "rating": 4.9,
    "reviews": 88,
    "desc": "Pure 90s Saturday morning cartoon nostalgia featuring the master villain Mojo Jojo in vibrant neon inks.",
    "specs": [
      "Dimensions: 95 x 95 mm",
      "Shatterproof acrylic",
      "Vivid UV digital print",
      "Heat resistant"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-22",
    "name": "Sacred Mandala Fine Art Coaster",
    "category": "Handcrafted Décor • Coaster",
    "filterCat": "coaster decor",
    "price": 499,
    "mrp": 650,
    "badge": "Art Edition",
    "badgeType": "sage",
    "image": "assets/products/coaster_mandala.png",
    "rating": 4.9,
    "reviews": 76,
    "desc": "Intricate symmetrical spiritual mandala artwork rendered in deep espresso and gold hues on crystal-clear acrylic.",
    "specs": [
      "Dimensions: 95 x 95 mm square",
      "Geometric precision printing",
      "Anti-skid cork backing",
      "Protective coat"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-23",
    "name": "Girls Who Love Books Carved Wooden Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 349,
    "mrp": 450,
    "badge": "Hand-Carved",
    "badgeType": "gold",
    "image": "assets/products/wood_girl_bookmark.jpg",
    "rating": 5.0,
    "reviews": 115,
    "desc": "Delicately laser-cut natural birch wood bookmark celebrating women who find worlds between book covers. Comes with a soft woven tassel.",
    "specs": [
      "Sustainable 2mm birch wood",
      "Smooth splinter-free finish",
      "Woven silk tassel attached",
      "Size: 140 x 40 mm"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-24",
    "name": "It's Book O'Clock Laser-Engraved Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 349,
    "mrp": 450,
    "badge": "Artisan",
    "badgeType": "sage",
    "image": "assets/products/wood_book_oclock.jpg",
    "rating": 4.9,
    "reviews": 98,
    "desc": "Whimsical book clock typography engraved on honey-toned natural wood. A thoughtful gift for late-night readers.",
    "specs": [
      "Dimensions: 140 x 38 mm",
      "Natural grain birch ply",
      "Emerald green silk tassel",
      "Non-damaging edges"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-25",
    "name": "Nerdy Boo Glasses Magnetic Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 249,
    "mrp": 350,
    "badge": "Bestseller",
    "badgeType": "gold",
    "image": "assets/products/magnetic_nerdy_boo.jpg",
    "rating": 5.0,
    "reviews": 164,
    "desc": "The adorable Boo ghost wearing oversized vintage spectacles. Clips securely around pages with gentle dual neodymium magnets.",
    "specs": [
      "Dual magnetic clamp",
      "Laminated waterproof finish",
      "Tear-resistant flexible core",
      "Size: 55 x 35 mm"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-26",
    "name": "Overthinker Girl Pastel Magnetic Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 249,
    "mrp": 350,
    "badge": "Relatable",
    "badgeType": "sage",
    "image": "assets/products/magnetic_overthinker.jpg",
    "rating": 4.9,
    "reviews": 152,
    "desc": "Relatable pastel illustration for midnight overthinkers, daydreamers, and romance novel lovers.",
    "specs": [
      "Ultra-strong page grip",
      "Soft-touch matte laminate",
      "Zero paper creasing",
      "Die-cut silhouette"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-27",
    "name": "Reading Panda Cozy Magnetic Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 249,
    "mrp": 350,
    "badge": "Cute Pick",
    "badgeType": "sage",
    "image": "assets/products/magnetic_reading_panda.jpg",
    "rating": 4.9,
    "reviews": 121,
    "desc": "Sleepy giant panda munching bamboo while reading your favourite book. Perfectly sized for paperbacks and hardcovers alike.",
    "specs": [
      "Neodymium flush magnets",
      "Water-resistant film",
      "Lightweight 12 grams",
      "Rounded safe corners"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-28",
    "name": "Reading Sloth Slow Living Magnetic Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 249,
    "mrp": 350,
    "badge": "Slow Living",
    "badgeType": "sage",
    "image": "assets/products/magnetic_reading_sloth.jpg",
    "rating": 4.8,
    "reviews": 94,
    "desc": "Gentle reminder to slow down, brew a warm cup of coffee, and savor every page. Features a smiling sloth wrapped in a cozy blanket.",
    "specs": [
      "Magnetic page-clip design",
      "Durable water-repellent coat",
      "Safe on delicate bible/novel pages",
      "Size: 60 x 38 mm"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-29",
    "name": "Nerdy Skeleton Bookworm Magnetic Bookmark",
    "category": "Stationaries • Bookmarks",
    "filterCat": "bookmark stationaries",
    "price": 249,
    "mrp": 350,
    "badge": "Dark Academia",
    "badgeType": "gold",
    "image": "assets/products/magnetic_nerdy_skeleton.jpg",
    "rating": 5.0,
    "reviews": 140,
    "desc": "'Reading until I'm dead' dark academia tribute bookmark featuring a dapper skeleton with round wire glasses reading a tome.",
    "specs": [
      "High-strength magnetic hold",
      "Matte velvet finish",
      "Dark academia aesthetic",
      "Pocket friendly"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-30",
    "name": "Adrak Chai Lover Vinyl Laptop Sticker",
    "category": "Stationaries • Stickers",
    "filterCat": "sticker stationaries",
    "price": 149,
    "mrp": 199,
    "badge": "Waterproof",
    "badgeType": "sage",
    "image": "assets/products/sticker_chai_lover.jpg",
    "rating": 4.9,
    "reviews": 180,
    "desc": "Heavy-duty waterproof vinyl sticker celebrating true cutting chai and adrak tea devotion. Leaves no sticky residue when removed.",
    "specs": [
      "Material: Premium waterproof vinyl laminate",
      "UV resistant inks prevent fading",
      "Clean peel removal",
      "Size: 70 x 70 mm"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-31",
    "name": "Desi Vibes Pop Culture Sticker Pack",
    "category": "Stationaries • Stickers",
    "filterCat": "sticker stationaries",
    "price": 199,
    "mrp": 299,
    "badge": "Pack of 5",
    "badgeType": "gold",
    "image": "assets/products/sticker_desi_vibes.jpg",
    "rating": 4.9,
    "reviews": 165,
    "desc": "Set of 5 die-cut vinyl stickers showcasing desi humor, street signs, and quirky cultural catchphrases for laptops, bottles, and helmets.",
    "specs": [
      "Pack includes 5 distinct die-cut designs",
      "Waterproof and dishwasher safe",
      "Scratch-resistant laminate",
      "Residue-free adhesive"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": true
  },
  {
    "id": "prod-32",
    "name": "Bookworm Vintage Club Vinyl Sticker",
    "category": "Stationaries • Stickers",
    "filterCat": "sticker stationaries",
    "price": 149,
    "mrp": 199,
    "badge": "Bibliophile",
    "badgeType": "sage",
    "image": "assets/products/sticker_bookworm.jpg",
    "rating": 4.8,
    "reviews": 110,
    "desc": "Vintage seal design for members of the late-night reading society. Looks striking on Kindle covers and laptop lids.",
    "specs": [
      "Diameter: 65 mm round cut",
      "Matte protective film",
      "Weatherproof outdoor durability",
      "Bubble-free application"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-33",
    "name": "Curious Cat Vinyl Laptop Decal",
    "category": "Stationaries • Stickers",
    "filterCat": "sticker stationaries",
    "price": 149,
    "mrp": 199,
    "badge": "Pet Love",
    "badgeType": "sage",
    "image": "assets/products/sticker_cat_lover.jpg",
    "rating": 4.9,
    "reviews": 92,
    "desc": "Playful calico cat peeking over your keyboard. Precision die-cut with glossy protective laminate.",
    "specs": [
      "Die-cut shape: 75 x 50 mm",
      "High gloss waterproof vinyl",
      "UV protected ink",
      "Safe on anodized aluminum"
    ],
    "categoryGroup": "stationaries",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-34",
    "name": "Couple Anniversary Bespoke Photo Thread Art",
    "category": "Events & Gifting • Personalized Gifting",
    "filterCat": "gifting decor",
    "price": 2499,
    "mrp": 3200,
    "badge": "Made to Order",
    "badgeType": "gold",
    "image": "assets/products/photo_thread_art_couple.png",
    "rating": 5.0,
    "reviews": 56,
    "desc": "Celebrate weddings and anniversaries with custom hand-stitched thread embroidery over couple portraits, framed in rich dark walnut.",
    "specs": [
      "Solid walnut 8 x 10 inch tabletop frame",
      "Hand-stitched thread contour embroidery",
      "Archival acid-free photo print",
      "Includes engraved brass message plate option"
    ],
    "categoryGroup": "events",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-35",
    "name": "Family Portrait Hand-Stitched Thread Art",
    "category": "Events & Gifting • Personalized Gifting",
    "filterCat": "gifting decor",
    "price": 2799,
    "mrp": 3600,
    "badge": "Heirloom",
    "badgeType": "gold",
    "image": "assets/products/photo_thread_art_portrait.png",
    "rating": 5.0,
    "reviews": 42,
    "desc": "A timeless family keepsake: your photograph rendered with dimensional embroidery threads creating depth, texture, and lasting sentiment.",
    "specs": [
      "Frame: Premium handcrafted wood with glass front",
      "Over 18 hours of detailed needlework",
      "Mount: Cream museum rag board",
      "Ships in velvet-lined protective gift box"
    ],
    "categoryGroup": "events",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-36",
    "name": "Cherry Blossom Botanical Wooden Wall Decor",
    "category": "Handcrafted Décor • Wall Hanging",
    "filterCat": "decor wall",
    "price": 1450,
    "mrp": 1800,
    "badge": "Artisan",
    "badgeType": "sage",
    "image": "assets/products/cherry_blossom.png",
    "rating": 5.0,
    "reviews": 58,
    "desc": "Delicate sakura blossoms rendered in soft pastel hues, framed in natural wood for zen corners and thoughtful spaces.",
    "specs": [
      "Dimensions: 180 x 180 mm",
      "Material: Premium archival art on wood",
      "Brass hanging loop included",
      "Signed studio seal on reverse"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": false,
    "isBestseller": false
  },
  {
    "id": "prod-37",
    "name": "Day & Night Celestial Botanical Hoop Art",
    "category": "Handcrafted Décor • Wall Hanging",
    "filterCat": "decor wall",
    "price": 1650,
    "mrp": 2000,
    "badge": "Artisan",
    "badgeType": "gold",
    "image": "assets/products/day_and_night.png",
    "rating": 4.9,
    "reviews": 63,
    "desc": "Sun and moon duality captured in intricate botanical thread embroidery inside an 8-inch circular wooden embroidery hoop.",
    "specs": [
      "Diameter: 8-inch solid beechwood hoop",
      "High-contrast day and night embroidery",
      "Ready to hang with brass mount",
      "Handcrafted in limited batches"
    ],
    "categoryGroup": "decor",
    "isNewLaunch": true,
    "isBestseller": false
  },
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
    "specs": [
      "Pages: 192 bleedproof unruled archival pages",
      "Binding: 180° Lay-flat thread binding",
      "Cover: Natural tactile woven book-cloth linen",
      "Paper: 120 GSM fountain-pen friendly warm bamboo paper"
    ],
    "categoryGroup": "journals",
    "isNewLaunch": false,
    "isBestseller": true
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
    "specs": [
      "90 Days of structured creative prompts and reflection",
      "Dimensions: A5 (148 x 210 mm) compact hardcover",
      "Foil-stamped spine with dual satin ribbon markers",
      "Includes bespoke illustrated mindfulness sticker sheet"
    ],
    "categoryGroup": "journals",
    "isNewLaunch": true,
    "isBestseller": false
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
    "specs": [
      "Minimum Order Quantity: 10 sets (Tiered pricing available)",
      "Full company logo laser engraving & custom foil packaging",
      "Includes custom handwritten welcome cards on seeded paper",
      "Delivery: Pan-India studio courier with individual dispatch"
    ],
    "categoryGroup": "bulk",
    "isNewLaunch": false,
    "isBestseller": false
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
    "specs": [
      "Custom guest name personalization on each keepsake",
      "Eco-luxe rigid magnetic gift box with satin bow",
      "Custom color palette matched to your event theme",
      "Bulk discount tiers from 15 to 500+ units"
    ],
    "categoryGroup": "bulk",
    "isNewLaunch": false,
    "isBestseller": false
  }
];

// State
let cart = JSON.parse(localStorage.getItem('gtb_cart') || 'null') || [
  {
    id: 'prod-1',
    name: 'Lady TeaTrip Acrylic Coaster & Teak Stand',
    price: 699,
    image: 'assets/products/lady_teatrip.jpg',
    qty: 1
  }
];

let wishlist = JSON.parse(localStorage.getItem('gtb_wishlist') || 'null') || ['prod-1', 'prod-2'];

let currentFilter = 'all';
let currentSort = 'featured';
let currentSearch = '';
let currentLayout = 'grid-4';

const FREE_SHIPPING_THRESHOLD = 1499;

// Init
document.addEventListener('DOMContentLoaded', () => {
  initFeaturedSections();
  initCatalog();
  initHeader();
  initCart();
  initWishlist();
  initQuickView();
  initSearch();
  initGiftingTabs();
  initNewsletter();
  initFloatingCartPill();
  initMobileBottomNav();
  initAccountModal();
  updateWishlistUI();
  initCategoryStrip();
  initHeroCarousel();
  initStoryScrollHighlight();
  initVideoCommerce();
});

// 1. Featured Sections: New Launch, Bestsellers & Built with heart💖
function initFeaturedSections() {
  renderNewLaunchSection();
  renderBestsellersSection();
  renderBuiltWithHeartSection();
}

function getProductUrl(prodOrId) {
  const prod = typeof prodOrId === 'object' ? prodOrId : (productsData.find(p => p.id === prodOrId) || { id: prodOrId });
  if (!prod) return 'journal-pdp.html';
  const id = prod.id || '';
  const name = (prod.name || '').toLowerCase();
  const cat = (prod.category || '').toLowerCase();

  // All journals and diaries redirect to the new luxury journal PDP UI
  if (id === 'prod-chronicle' || id === 'prod-38' || id === 'prod-39' || 
      cat.includes('journal') || cat.includes('diary') || 
      name.includes('journal') || name.includes('diary') || name.includes('chronicle')) {
    return `journal-pdp.html?id=${id}`;
  }
  return `product.html?id=${id}`;
}

function renderProductCardHTML(prod) {
  const isWishlisted = wishlist.includes(prod.id);
  const discount = prod.mrp ? Math.round(((prod.mrp - prod.price) / prod.mrp) * 100) : 0;
  const prodUrl = getProductUrl(prod);

  return `
    <article class="product-card cursor-pointer" data-id="${prod.id}" data-category="${prod.category}" onclick="if (!event.target.closest('button') && !event.target.closest('a')) window.location.href = '${prodUrl}';">
      <div class="product-thumb-wrap">
        <a href="${prodUrl}" class="product-thumb-link block w-full h-full" aria-label="${prod.name}">
          <img src="${prod.image}" alt="${prod.name}" class="product-thumb" loading="lazy" />
        </a>
        
        <!-- Badge -->
        <span class="product-badge ${prod.badgeType || 'gold'}">${prod.badge || 'Atelier'}</span>
        
        <!-- Wishlist Toggle Button -->
        <button class="wishlist-toggle-btn ${isWishlisted ? 'active' : ''}" onclick="toggleWishlist('${prod.id}', event)" aria-label="Save to wishlist" title="Save to wishlist">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="${isWishlisted ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
            <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
          </svg>
        </button>

        <!-- Direct Action Bar -->
        <div class="quick-actions">
          <a href="${prodUrl}" class="quick-btn" onclick="event.stopPropagation();">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/>
              <circle cx="12" cy="12" r="3"/>
            </svg>
            View Details
          </a>
        </div>
      </div>

      <div class="product-details">
        <div class="product-info-top">
          <a href="${prodUrl}" class="product-name-link" style="text-decoration: none; color: inherit;">
            <h3 class="product-name">${prod.name}</h3>
          </a>
          
          <div class="product-rating">
            <div class="stars">
              ${renderStars(prod.rating)}
            </div>
            <span class="rating-count">(${prod.reviews})</span>
          </div>

          <div class="product-pricing">
            <span class="price-current">₹${prod.price.toLocaleString('en-IN')}</span>
            ${prod.mrp ? `<span class="price-original">₹${prod.mrp.toLocaleString('en-IN')}</span>` : ''}
            ${discount > 0 ? `<span class="discount-pill">${discount}% OFF</span>` : ''}
          </div>
        </div>

        <button class="add-cart-btn" onclick="addToCart('${prod.id}')">
          Add to Cart
        </button>
      </div>
    </article>
  `;
}

function renderNewLaunchSection() {
  const grid = document.querySelector('#new-launch-grid');
  if (!grid) return;
  const newItems = productsData.filter(p => p.isNewLaunch);
  grid.innerHTML = newItems.map(renderProductCardHTML).join('');
}

function renderBestsellersSection() {
  const grid = document.querySelector('#bestsellers-grid');
  if (!grid) return;
  const bestsellers = productsData.filter(p => p.isBestseller);
  grid.innerHTML = bestsellers.map(renderProductCardHTML).join('');
}

function renderBuiltWithHeartSection() {
  const grid = document.querySelector('#built-with-heart-grid');
  if (!grid) return;

  // Products exclusively customized and handmade
  const builtWithHeartIds = [
    'prod-3',  // Personalized Floral Wooden Hoop Door Name Tag
    'prod-8',  // Bespoke Photo Thread Art Keepsake Frame
    'prod-34', // Couple Anniversary Bespoke Photo Thread Art
    'prod-35', // Family Portrait Hand-Stitched Thread Art
    'prod-7',  // Mermaid Hand-Embroidered Hoop Wall Hanging
    'prod-4',  // Handcrafted Wooden Sunflower Bookmark with Tassel
    'prod-36', // Cherry Blossom Botanical Wooden Wall Decor
    'prod-37'  // Day & Night Celestial Botanical Hoop Art
  ];

  const handmadeCustomProducts = productsData.filter(p => builtWithHeartIds.includes(p.id) || p.isBuiltWithHeart);
  grid.innerHTML = handmadeCustomProducts.map(renderProductCardHTML).join('');
}

// 2. Catalog Engine (ONLY CATEGORIES, NO SUBCATEGORIES)
function initCatalog() {
  renderCategoryPills();
  renderCatalog();

  // Search input in catalog toolbar
  const searchInput = document.querySelector('#catalog-search-input');
  const clearBtn = document.querySelector('#catalog-search-clear');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentSearch = e.target.value.trim().toLowerCase();
      if (clearBtn) clearBtn.style.display = currentSearch ? 'block' : 'none';
      renderCatalog();
    });
  }
  if (clearBtn && searchInput) {
    clearBtn.addEventListener('click', () => {
      searchInput.value = '';
      currentSearch = '';
      clearBtn.style.display = 'none';
      renderCatalog();
    });
  }

  // Sort dropdown
  const sortSelect = document.querySelector('#catalog-sort-select');
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      currentSort = e.target.value;
      renderCatalog();
    });
  }

  // Layout switcher
  const layoutBtns = document.querySelectorAll('.layout-btn');
  layoutBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      layoutBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentLayout = btn.dataset.layout;
      const grid = document.querySelector('#products-grid');
      if (grid) {
        grid.className = `products-grid ${currentLayout}`;
      }
    });
  });
}

function renderCategoryPills() {
  const pillsContainer = document.querySelector('#catalog-filter-pills');
  if (!pillsContainer) return;

  // Clean category names without serial numbers and counts
  const categories = [
    { id: 'all', label: 'All Editions' },
    { id: 'stationaries', label: 'Stationaries & Calendars' },
    { id: 'journals', label: 'Journals & Planners' },
    { id: 'decor', label: 'Handcrafted Décor' },
    { id: 'events', label: 'Events & Gifting' },
    { id: 'bulk', label: 'Bulk Orders' }
  ];

  pillsContainer.innerHTML = categories.map(cat => `
    <button class="pill-btn ${currentFilter === cat.id ? 'active' : ''}" data-cat="${cat.id}">
      <span>${cat.label}</span>
    </button>
  `).join('');

  pillsContainer.querySelectorAll('.pill-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      pillsContainer.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.dataset.cat;
      renderCatalog();
    });
  });
}

function getFilteredProducts() {
  return productsData.filter(p => {
    // 1. Category Filter (Only Categories)
    if (currentFilter !== 'all') {
      if (p.categoryGroup !== currentFilter) return false;
    }

    // 2. Search Query
    if (currentSearch) {
      const q = currentSearch;
      const searchable = (p.name + ' ' + p.category + ' ' + p.desc + ' ' + (p.specs || []).join(' ')).toLowerCase();
      if (!searchable.includes(q)) return false;
    }

    return true;
  }).sort((a, b) => {
    if (currentSort === 'price-asc') return a.price - b.price;
    if (currentSort === 'price-desc') return b.price - a.price;
    if (currentSort === 'rating') return b.rating - a.rating || b.reviews - a.reviews;
    if (currentSort === 'bestseller') return b.reviews - a.reviews;
    return 0; // Default featured order
  });
}

function renderCatalog() {
  const grid = document.querySelector('#products-grid');
  const countBadge = document.querySelector('#catalog-count-badge');
  if (!grid) return;

  const filtered = getFilteredProducts();

  if (countBadge) {
    countBadge.textContent = `Showing ${filtered.length} of ${productsData.length} handcrafted atelier editions`;
  }

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="catalog-empty-state">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="11" cy="11" r="8"/>
          <path d="m21 21-4.3-4.3"/>
        </svg>
        <h3>No matching editions found</h3>
        <p>Try clearing your search query or selecting another category.</p>
        <button class="btn btn-outline" onclick="resetFilters()">Reset All Filters</button>
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(renderProductCardHTML).join('');
}

function renderStars(rating) {
  const fullStar = '<svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>';
  return Array(5).fill(fullStar).join('');
}

function resetFilters() {
  currentFilter = 'all';
  currentSearch = '';
  currentSort = 'featured';

  const searchInput = document.querySelector('#catalog-search-input');
  if (searchInput) searchInput.value = '';
  const clearBtn = document.querySelector('#catalog-search-clear');
  if (clearBtn) clearBtn.style.display = 'none';

  renderCategoryPills();
  renderCatalog();
}

// 3. Wishlist Management
function initWishlist() {
  const wishlistTrigger = document.querySelector('#wishlist-trigger');
  const wishlistDrawer = document.querySelector('#wishlist-drawer-overlay');
  const wishlistClose = document.querySelector('#wishlist-close-btn');

  if (wishlistTrigger && wishlistDrawer) {
    wishlistTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      wishlistDrawer.classList.add('open');
      renderWishlistDrawer();
    });
  }

  if (wishlistClose && wishlistDrawer) {
    wishlistClose.addEventListener('click', () => wishlistDrawer.classList.remove('open'));
    wishlistDrawer.addEventListener('click', (e) => {
      if (e.target === wishlistDrawer) wishlistDrawer.classList.remove('open');
    });
  }
}

function toggleWishlist(prodId, event) {
  if (event) event.stopPropagation();
  const prod = productsData.find(p => p.id === prodId);
  if (!prod) return;

  const idx = wishlist.indexOf(prodId);
  if (idx > -1) {
    wishlist.splice(idx, 1);
    showToast(`Removed "${prod.name}" from your wishlist`);
  } else {
    wishlist.push(prodId);
    showToast(`Saved "${prod.name}" to your wishlist ❤️`);
  }

  localStorage.setItem('gtb_wishlist', JSON.stringify(wishlist));
  updateWishlistUI();
  renderNewLaunchSection();
  renderBestsellersSection();
  renderCatalog();
  renderWishlistDrawer();
}

function updateWishlistUI() {
  const badge = document.querySelector('#wishlist-badge-count');
  const bottomBadge = document.querySelector('#bottom-wishlist-count');
  if (badge) {
    badge.textContent = wishlist.length;
    badge.style.display = wishlist.length > 0 ? 'inline-flex' : 'none';
  }
  if (bottomBadge) {
    bottomBadge.textContent = wishlist.length;
    bottomBadge.style.display = wishlist.length > 0 ? 'inline-flex' : 'none';
  }
}

function renderWishlistDrawer() {
  const list = document.querySelector('#wishlist-items-list');
  const countLabel = document.querySelector('#wishlist-count-label');
  if (!list) return;

  if (countLabel) {
    countLabel.textContent = `${wishlist.length} Saved Editions`;
  }

  if (wishlist.length === 0) {
    list.innerHTML = `
      <div class="empty-drawer-state">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
        </svg>
        <p class="empty-title">Your Wishlist is Empty</p>
        <p class="empty-sub">Tap the heart on any product to curate your personal collection.</p>
      </div>
    `;
    return;
  }

  const items = wishlist.map(id => productsData.find(p => p.id === id)).filter(Boolean);

  list.innerHTML = items.map(item => `
    <div class="wishlist-item">
      <img src="${item.image}" alt="${item.name}" class="wishlist-item-img" />
      <div class="wishlist-item-details">
        <span class="item-cat">${item.category}</span>
        <h4 class="item-name">${item.name}</h4>
        <div class="item-price-wrap">
          <span class="item-price">₹${item.price.toLocaleString('en-IN')}</span>
          ${item.mrp ? `<span class="item-mrp">₹${item.mrp.toLocaleString('en-IN')}</span>` : ''}
        </div>
        <div class="wishlist-actions-row">
          <button class="btn-micro-bag" onclick="addToCart('${item.id}')">Add to Cart</button>
          <button class="btn-micro-remove" onclick="toggleWishlist('${item.id}', event)">Remove</button>
        </div>
      </div>
    </div>
  `).join('');
}

// 4. Cart Operations
function initCart() {
  const cartTrigger = document.querySelector('#cart-trigger');
  const cartDrawer = document.querySelector('#cart-drawer-overlay');
  const cartClose = document.querySelector('#cart-close-btn');

  if (cartTrigger && cartDrawer) {
    cartTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      cartDrawer.classList.add('open');
      renderCart();
    });
  }

  if (cartClose && cartDrawer) {
    cartClose.addEventListener('click', () => cartDrawer.classList.remove('open'));
    cartDrawer.addEventListener('click', (e) => {
      if (e.target === cartDrawer) cartDrawer.classList.remove('open');
    });
  }

  renderCart();
}

function addToCart(prodId, qty = 1) {
  const item = productsData.find(p => p.id === prodId);
  if (!item) return;

  const existing = cart.find(i => i.id === prodId);
  if (existing) {
    existing.qty += qty;
  } else {
    cart.push({
      id: item.id,
      name: item.name,
      price: item.price,
      image: item.image,
      category: item.category,
      qty: qty
    });
  }

  localStorage.setItem('gtb_cart', JSON.stringify(cart));
  renderCart();
  updateFloatingCartPill();
  showToast(`Added "${item.name}" to your bag`);

  const cartDrawer = document.querySelector('#cart-drawer-overlay');
  if (cartDrawer) {
    cartDrawer.classList.add('open');
  }
}

function updateCartQty(prodId, delta) {
  const item = cart.find(i => i.id === prodId);
  if (!item) return;

  item.qty += delta;
  if (item.qty <= 0) {
    cart = cart.filter(i => i.id !== prodId);
  }

  localStorage.setItem('gtb_cart', JSON.stringify(cart));
  renderCart();
  updateFloatingCartPill();
}

function renderCart() {
  const cartList = document.querySelector('#cart-items-list');
  const cartBadge = document.querySelector('#cart-badge-count');
  const subtotalEl = document.querySelector('#cart-subtotal-val');
  const goalLabel = document.querySelector('#shipping-goal-label');
  const progressFill = document.querySelector('#shipping-progress-fill');

  const totalCount = cart.reduce((acc, curr) => acc + curr.qty, 0);
  const totalAmount = cart.reduce((acc, curr) => acc + (curr.price * curr.qty), 0);

  if (cartBadge) {
    cartBadge.textContent = totalCount;
    cartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
  }
  const bottomCartBadge = document.querySelector('#bottom-cart-count');
  if (bottomCartBadge) {
    bottomCartBadge.textContent = totalCount;
    bottomCartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
  }

  if (subtotalEl) {
    subtotalEl.textContent = `₹${totalAmount.toLocaleString('en-IN')}`;
  }

  // Update Free Shipping Progress (Threshold: ₹1,499)
  if (goalLabel && progressFill) {
    if (totalAmount >= FREE_SHIPPING_THRESHOLD) {
      goalLabel.innerHTML = '<span>✨ You unlocked <strong>FREE Studio Courier Shipping!</strong></span>';
      progressFill.style.width = '100%';
    } else {
      const remaining = FREE_SHIPPING_THRESHOLD - totalAmount;
      const pct = Math.min(100, Math.round((totalAmount / FREE_SHIPPING_THRESHOLD) * 100));
      goalLabel.innerHTML = `<span>Add <strong>₹${remaining.toLocaleString('en-IN')}</strong> more for <strong>FREE Shipping</strong></span><span>${pct}%</span>`;
      progressFill.style.width = `${pct}%`;
    }
  }

  if (!cartList) return;

  if (cart.length === 0) {
    cartList.innerHTML = `
      <div class="empty-drawer-state">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
          <path d="M3 6h18"/>
          <path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
        <p class="empty-title">Your shopping bag is empty</p>
        <p class="empty-sub">Explore our actual acrylic coasters, calendars, and door hangers.</p>
        <button class="btn btn-primary" onclick="document.querySelector('#cart-drawer-overlay').classList.remove('open'); window.location.hash='catalogue-section';">Explore Catalogue</button>
      </div>
    `;
    return;
  }

  cartList.innerHTML = cart.map(item => `
    <div class="cart-item">
      <img src="${item.image}" alt="${item.name}" class="cart-item-img" />
      <div class="cart-item-info">
        <h4 class="item-name">${item.name}</h4>
        <p class="item-variant">${item.category || 'Atelier Original'}</p>
        <div class="qty-control">
          <button class="qty-btn" onclick="updateCartQty('${item.id}', -1)" aria-label="Decrease">−</button>
          <span class="qty-val">${item.qty}</span>
          <button class="qty-btn" onclick="updateCartQty('${item.id}', 1)" aria-label="Increase">+</button>
        </div>
      </div>
      <div class="cart-item-actions">
        <span class="item-price">₹${(item.price * item.qty).toLocaleString('en-IN')}</span>
        <button class="remove-btn" onclick="updateCartQty('${item.id}', -999)" title="Remove item">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>
          </svg>
        </button>
      </div>
    </div>
  `).join('');
}

// 5. Quick View Modal with Quantity Stepper
let quickViewQty = 1;
function initQuickView() {
  const modal = document.querySelector('#quick-view-modal');
  const closeBtn = document.querySelector('#modal-close-btn');

  if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => modal.classList.remove('open'));
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.classList.remove('open');
    });
  }
}

function openQuickView(prodId) {
  const targetUrl = getProductUrl(prodId);
  window.location.href = targetUrl;
  return;
  const prod = productsData.find(p => p.id === prodId);
  if (!prod) return;

  quickViewQty = 1;
  const modal = document.querySelector('#quick-view-modal');
  const modalImg = document.querySelector('#modal-img');
  const modalTag = document.querySelector('#modal-tag');
  const modalTitle = document.querySelector('#modal-title');
  const modalPrice = document.querySelector('#modal-price');
  const modalDesc = document.querySelector('#modal-desc');
  const specsList = document.querySelector('#modal-specs-list');

  if (modalImg) modalImg.src = prod.image;
  if (modalTag) modalTag.textContent = prod.category;
  if (modalTitle) modalTitle.textContent = prod.name;
  if (modalPrice) {
    modalPrice.innerHTML = `
      <span class="price-val">₹${prod.price.toLocaleString('en-IN')}</span>
      ${prod.mrp ? `<span class="mrp-val">₹${prod.mrp.toLocaleString('en-IN')}</span>` : ''}
      ${prod.mrp ? `<span class="discount-tag">${Math.round(((prod.mrp - prod.price) / prod.mrp) * 100)}% OFF</span>` : ''}
    `;
  }
  if (modalDesc) modalDesc.textContent = prod.desc;

  if (specsList && prod.specs) {
    specsList.innerHTML = prod.specs.map(s => `<li><span class="bullet-dot"></span>${s}</li>`).join('');
  }

  // Quantity Stepper
  const qtyVal = document.querySelector('#modal-qty-val');
  if (qtyVal) qtyVal.textContent = quickViewQty;

  const modalAddBtn = document.querySelector('#modal-add-cart');
  if (modalAddBtn) {
    modalAddBtn.onclick = () => {
      addToCart(prod.id, quickViewQty);
      modal.classList.remove('open');
    };
  }

  modal.classList.add('open');
}

function adjustQuickViewQty(delta) {
  quickViewQty = Math.max(1, quickViewQty + delta);
  const qtyVal = document.querySelector('#modal-qty-val');
  if (qtyVal) qtyVal.textContent = quickViewQty;
}

// 6. Global Search Modal (Cmd+K)
function initSearch() {
  const searchTrigger = document.querySelector('#header-search-trigger');
  const searchModal = document.querySelector('#search-modal-overlay');
  const searchClose = document.querySelector('#search-modal-close');
  const searchInput = document.querySelector('#search-modal-input');
  const resultsContainer = document.querySelector('#search-modal-results');

  if (searchTrigger && searchModal) {
    searchTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      searchModal.classList.add('open');
      if (searchInput) {
        setTimeout(() => searchInput.focus(), 100);
      }
    });
  }

  if (searchClose && searchModal) {
    searchClose.addEventListener('click', () => searchModal.classList.remove('open'));
    searchModal.addEventListener('click', (e) => {
      if (e.target === searchModal) searchModal.classList.remove('open');
    });
  }

  window.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (searchModal) {
        searchModal.classList.toggle('open');
        if (searchModal.classList.contains('open') && searchInput) {
          setTimeout(() => searchInput.focus(), 100);
        }
      }
    }
    if (e.key === 'Escape' && searchModal && searchModal.classList.contains('open')) {
      searchModal.classList.remove('open');
    }
  });

  if (searchInput && resultsContainer) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.trim().toLowerCase();
      if (!query) {
        renderSearchTags(resultsContainer);
        return;
      }

      const matches = productsData.filter(p => {
        return (p.name + ' ' + p.category + ' ' + p.desc + ' ' + (p.specs || []).join(' ')).toLowerCase().includes(query);
      }).slice(0, 6);

      if (matches.length === 0) {
        resultsContainer.innerHTML = `
          <div class="search-empty">
            <p>No handcrafted editions matching "<strong>${query}</strong>"</p>
          </div>
        `;
        return;
      }

      resultsContainer.innerHTML = `
        <div class="search-results-list">
          ${matches.map(p => `
            <div class="search-result-item" onclick="openQuickView('${p.id}'); document.querySelector('#search-modal-overlay').classList.remove('open');">
              <img src="${p.image}" alt="${p.name}" class="search-result-thumb" />
              <div>
                <span class="search-result-cat">${p.category}</span>
                <h4 class="search-result-name">${p.name}</h4>
                <span class="search-result-price">₹${p.price.toLocaleString('en-IN')}</span>
              </div>
            </div>
          `).join('')}
        </div>
      `;
    });

    renderSearchTags(resultsContainer);
  }
}

function renderSearchTags(container) {
  const tags = ['Desk Calendar', 'F1 Coaster', 'Chugli Over Chai', 'Magnetic Bookmark', 'Sunflower', 'Thread Art', 'Door Hanger', 'Linen Journal'];
  container.innerHTML = `
    <div class="search-popular-tags">
      <span class="search-tags-label">Popular Searches:</span>
      <div class="tags-row">
        ${tags.map(t => `<button class="tag-chip" onclick="searchTag('${t}')">${t}</button>`).join('')}
      </div>
    </div>
  `;
}

function searchTag(tag) {
  const searchInput = document.querySelector('#search-modal-input');
  if (searchInput) {
    searchInput.value = tag;
    searchInput.dispatchEvent(new Event('input'));
  }
}

// 7. Floating Cart Pill
function initFloatingCartPill() {
  let pill = document.querySelector('#floating-cart-pill');
  if (!pill) {
    pill = document.createElement('div');
    pill.id = 'floating-cart-pill';
    pill.className = 'floating-cart-pill';
    pill.onclick = () => {
      const drawer = document.querySelector('#cart-drawer-overlay');
      if (drawer) drawer.classList.add('open');
      renderCart();
    };
    document.body.appendChild(pill);
  }
  updateFloatingCartPill();
}

function updateFloatingCartPill() {
  const pill = document.querySelector('#floating-cart-pill');
  if (!pill) return;

  const totalCount = cart.reduce((acc, curr) => acc + curr.qty, 0);
  const totalAmount = cart.reduce((acc, curr) => acc + (curr.price * curr.qty), 0);

  if (totalCount > 0) {
    pill.innerHTML = `
      <div class="floating-pill-content">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
          <path d="M3 6h18"/>
          <path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
        <span class="floating-count">${totalCount}</span>
        <span class="floating-divider">|</span>
        <span class="floating-price">₹${totalAmount.toLocaleString('en-IN')}</span>
      </div>
    `;
    pill.classList.add('visible');
  } else {
    pill.classList.remove('visible');
  }
}

// 8. Header Scroll and Mobile Nav
function initHeader() {
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  const toggleBtns = document.querySelectorAll('#mobile-toggle-btn, .mobile-toggle');
  const drawer = document.querySelector('#mobile-drawer-overlay');
  const drawerClose = document.querySelector('#mobile-drawer-close');

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openMobileDrawer();
    });
  });

  if (drawerClose && drawer) {
    drawerClose.addEventListener('click', () => {
      closeMobileDrawer();
    });
  }

  if (drawer) {
    drawer.addEventListener('click', (e) => {
      if (e.target === drawer) {
        closeMobileDrawer();
      }
    });
  }
}

// 9. Gifting Spotlight Tabs
function initGiftingTabs() {
  const corporateTab = document.querySelector('#tab-corporate');
  const weddingTab = document.querySelector('#tab-wedding');
  const giftingImg = document.querySelector('#gifting-hero-img');
  const giftingTitle = document.querySelector('#gifting-title-text');
  const giftingDesc = document.querySelector('#gifting-desc-text');

  if (corporateTab && weddingTab) {
    corporateTab.addEventListener('click', () => {
      corporateTab.classList.add('active');
      weddingTab.classList.remove('active');
      if (giftingTitle) giftingTitle.innerHTML = 'Corporate Keepsakes &amp; <em>Executive Swag</em>';
      if (giftingDesc) giftingDesc.textContent = 'Thoughtfully branded onboarding kits, bespoke acrylic coasters, desk calendars with wooden easels, and curated festive hampers designed to leave an indelible impression on clients and teams.';
      if (giftingImg) giftingImg.src = 'assets/cat_bulk.jpg';
    });

    weddingTab.addEventListener('click', () => {
      weddingTab.classList.add('active');
      corporateTab.classList.remove('active');
      if (giftingTitle) giftingTitle.innerHTML = 'Wedding Celebrations &amp; <em>Bespoke Favours</em>';
      if (giftingDesc) giftingDesc.textContent = 'Custom illustrated acrylic coasters, wooden keepsake stands, personalized door plaques, and custom stationery suites crafted to celebrate your one-of-a-kind story.';
      if (giftingImg) giftingImg.src = 'assets/cat_events.jpg';
    });
  }
}

// 10. Newsletter
function initNewsletter() {
  const form = document.querySelector('#newsletter-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      if (input && input.value) {
        showToast(`Welcome to the Society! 10% welcome coupon sent to ${input.value}`);
        input.value = '';
      }
    });
  }
}

// 11. Toast Notification
function showToast(message) {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `
    <span class="toast-icon">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M20 6 9 17l-5-5"/>
      </svg>
    </span>
    <span>${message}</span>
  `;

  container.appendChild(toast);
  setTimeout(() => toast.classList.add('show'), 20);

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, 3500);
}

// 12. Mobile Drawer Helpers
function openMobileDrawer() {
  const drawer = document.querySelector('#mobile-drawer-overlay');
  if (drawer) {
    drawer.classList.add('open');
    document.body.classList.add('no-scroll');
  }
}

function closeMobileDrawer() {
  const drawer = document.querySelector('#mobile-drawer-overlay');
  if (drawer) {
    drawer.classList.remove('open');
    document.body.classList.remove('no-scroll');
  }
}

function openSearchFromMobile() {
  closeMobileDrawer();
  const searchModal = document.querySelector('#search-modal-overlay');
  const searchInput = document.querySelector('#search-modal-input');
  if (searchModal) {
    searchModal.classList.add('open');
    if (searchInput) {
      setTimeout(() => searchInput.focus(), 150);
    }
  }
}

function filterFromMobile(cat) {
  closeMobileDrawer();
  currentFilter = cat;
  
  // Update category pill active state
  const pills = document.querySelectorAll('#catalog-filter-pills .pill-btn');
  pills.forEach(p => {
    if (p.dataset.cat === cat) {
      p.classList.add('active');
      p.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    } else {
      p.classList.remove('active');
    }
  });

  renderCatalog();
}

// 13. Mobile Bottom Navigation Controller
function initMobileBottomNav() {
  const bnavWishlist = document.querySelector('#bnav-wishlist');
  const bnavCart = document.querySelector('#bnav-cart');
  const wishlistDrawer = document.querySelector('#wishlist-drawer-overlay');
  const cartDrawer = document.querySelector('#cart-drawer-overlay');

  if (bnavWishlist && wishlistDrawer) {
    bnavWishlist.addEventListener('click', (e) => {
      e.preventDefault();
      wishlistDrawer.classList.add('open');
      renderWishlistDrawer();
    });
  }

  const bnavCategories = document.querySelector('#bnav-categories');
  if (bnavCategories) {
    bnavCategories.addEventListener('click', (e) => {
      e.preventDefault();
      openMobileDrawer();
    });
  }

  if (bnavCart && cartDrawer) {
    bnavCart.addEventListener('click', (e) => {
      e.preventDefault();
      cartDrawer.classList.add('open');
      renderCart();
    });
  }

  // Active tab switching
  const bottomNavItems = document.querySelectorAll('.bottom-nav-item');
  bottomNavItems.forEach(btn => {
    btn.addEventListener('click', () => {
      bottomNavItems.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  // Highlight Home when scrolling to top
  window.addEventListener('scroll', () => {
    const bHome = document.querySelector('#bnav-home');
    const bCat = document.querySelector('#bnav-categories');
    if (!bHome || !bCat) return;

    if (window.scrollY < 400) {
      bHome.classList.add('active');
      bCat.classList.remove('active');
    }
  });
}

// 14. Atelier My Account Modal Controller
function openAccountModal() {
  const modal = document.querySelector('#account-modal-overlay');
  if (modal) {
    modal.classList.add('open');
    document.body.classList.add('no-scroll');
  }
}

function closeAccountModal() {
  const modal = document.querySelector('#account-modal-overlay');
  if (modal) {
    modal.classList.remove('open');
    document.body.classList.remove('no-scroll');
  }
}

function initAccountModal() {
  const modal = document.querySelector('#account-modal-overlay');
  const closeBtn = document.querySelector('#account-modal-close');
  const bnavAccount = document.querySelector('#bnav-account');
  const drawerAccountBtn = document.querySelector('#mobile-drawer-account-btn');

  if (closeBtn) {
    closeBtn.addEventListener('click', closeAccountModal);
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeAccountModal();
      }
    });
  }

  if (bnavAccount) {
    bnavAccount.addEventListener('click', (e) => {
      e.preventDefault();
      openAccountModal();
    });
  }

  if (drawerAccountBtn) {
    drawerAccountBtn.addEventListener('click', (e) => {
      e.preventDefault();
      closeMobileDrawer();
      openAccountModal();
    });
  }

  // Keyboard Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAccountModal();
    }
  });
}

// Expose globally
window.openAccountModal = openAccountModal;
window.closeAccountModal = closeAccountModal;

// 15. Shop By Categories Strip Controller
function initCategoryStrip() {
  const cards = document.querySelectorAll('.category-pill-card');
  cards.forEach(card => {
    card.addEventListener('click', (e) => {
      const cat = card.dataset.category;
      if (!cat) return;

      if (cat === 'Stationaries') {
        e.preventDefault();
        filterFromMobile('stationaries');
        const catalogEl = document.querySelector('#catalogue-section');
        if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
      } else if (cat === 'Journals') {
        e.preventDefault();
        filterFromMobile('journals');
        const catalogEl = document.querySelector('#catalogue-section');
        if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
      } else if (cat === 'Coasters') {
        e.preventDefault();
        filterFromMobile('decor');
        const catalogEl = document.querySelector('#catalogue-section');
        if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
      } else if (cat === 'Bookmarks') {
        e.preventDefault();
        filterFromMobile('stationaries');
        const catalogEl = document.querySelector('#catalogue-section');
        if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
      } else if (cat === 'Decor') {
        e.preventDefault();
        filterFromMobile('decor');
        const catalogEl = document.querySelector('#catalogue-section');
        if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
      } else if (cat === 'Gifting') {
        e.preventDefault();
        filterFromMobile('events');
        const catalogEl = document.querySelector('#catalogue-section');
        if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
      } else if (cat === 'Bulk') {
        e.preventDefault();
        filterFromMobile('bulk');
        const catalogEl = document.querySelector('#catalogue-section');
        if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
      } else if (cat === 'Bestsellers') {
        e.preventDefault();
        filterFromMobile('all');
        const bestEl = document.querySelector('#bestsellers') || document.querySelector('#catalogue-section');
        if (bestEl) bestEl.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  const viewAllBtn = document.querySelector('.category-view-all-btn');
  if (viewAllBtn) {
    viewAllBtn.addEventListener('click', (e) => {
      e.preventDefault();
      filterFromMobile('all');
      const catalogEl = document.querySelector('#catalogue-section');
      if (catalogEl) catalogEl.scrollIntoView({ behavior: 'smooth' });
    });
  }
}

// ==========================================================================
// HERO CAROUSEL: Edge-to-Edge Pure Banner Carousel with Bubbles & Arrows
// ==========================================================================
function initHeroCarousel() {
  const carousel = document.getElementById('hero-carousel');
  const track = document.getElementById('hero-carousel-track');
  const slides = document.querySelectorAll('.hero-carousel-slide');
  const dots = document.querySelectorAll('#hero-carousel-dots .carousel-dot');
  const prevBtn = document.getElementById('hero-prev-btn');
  const nextBtn = document.getElementById('hero-next-btn');

  if (!carousel || !track || slides.length === 0) return;

  let currentIndex = 0;
  const totalSlides = slides.length;
  let autoPlayInterval = null;

  function updateCarousel(newIndex) {
    if (newIndex < 0) {
      currentIndex = totalSlides - 1;
    } else if (newIndex >= totalSlides) {
      currentIndex = 0;
    } else {
      currentIndex = newIndex;
    }

    // Smooth transform slide
    track.style.transform = `translateX(-${currentIndex * 100}%)`;

    // Update active slide state
    slides.forEach((slide, idx) => {
      slide.classList.toggle('active', idx === currentIndex);
    });

    // Update indicator bubble states
    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentIndex);
      dot.setAttribute('aria-selected', idx === currentIndex ? 'true' : 'false');
    });
  }

  // Prev & Next arrow listeners
  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      resetAutoPlay();
      updateCarousel(currentIndex - 1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      resetAutoPlay();
      updateCarousel(currentIndex + 1);
    });
  }

  // Bubble / Dot indicators listeners
  dots.forEach((dot, idx) => {
    dot.addEventListener('click', (e) => {
      e.preventDefault();
      resetAutoPlay();
      updateCarousel(idx);
    });
  });

  // Autoplay functionality (5 seconds interval)
  function startAutoPlay() {
    stopAutoPlay();
    autoPlayInterval = setInterval(() => {
      updateCarousel(currentIndex + 1);
    }, 5000);
  }

  function stopAutoPlay() {
    if (autoPlayInterval) {
      clearInterval(autoPlayInterval);
      autoPlayInterval = null;
    }
  }

  function resetAutoPlay() {
    stopAutoPlay();
    startAutoPlay();
  }

  // Pause on hover
  carousel.addEventListener('mouseenter', stopAutoPlay);
  carousel.addEventListener('mouseleave', startAutoPlay);

  // Touch Swipe Support (Mobile & Tablet)
  let touchStartX = 0;
  let touchEndX = 0;

  carousel.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    stopAutoPlay();
  }, { passive: true });

  carousel.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 45) {
      if (diff > 0) {
        // Swiped Left -> Next Slide
        updateCarousel(currentIndex + 1);
      } else {
        // Swiped Right -> Previous Slide
        updateCarousel(currentIndex - 1);
      }
    }
    startAutoPlay();
  }, { passive: true });

  // Initial setup
  updateCarousel(0);
  startAutoPlay();
}

// ==========================================================================
// ABOUT US / OUR STORY: Scroll-Triggered Progressive Text Highlight (Word-by-Word)
// ==========================================================================
let storyScrollListenerAttached = false;

function initStoryScrollHighlight() {
  const section = document.querySelector('.about-story-section');
  if (!section) return;

  const narrativeWrap = document.getElementById('story-narrative-wrap');
  const splitContainers = section.querySelectorAll('.story-split-text');
  
  splitContainers.forEach(container => {
    if (container.dataset.splitDone === 'true') return;
    const rawText = container.textContent.trim();
    if (!rawText) return;
    const words = rawText.split(/\s+/);
    container.innerHTML = words
      .map(word => `<span class="story-word">${word}</span>`)
      .join(' ');
    container.dataset.splitDone = 'true';
  });

  // Only select story-words inside visible containers
  const words = Array.from(section.querySelectorAll('.story-narrative-wrap > .story-split-text .story-word, .story-truncated-content[style*="flex"] .story-word, .story-truncated-content[style*="block"] .story-word'));
  const allWords = words.length ? words : Array.from(section.querySelectorAll('.story-word'));
  if (!allWords.length || !narrativeWrap) return;

  let ticking = false;

  function updateHighlights() {
    const vh = window.innerHeight;
    const wrapRect = narrativeWrap.getBoundingClientRect();
    
    // Calculate the scroll progress of the narrative container through the viewport
    const startPoint = vh * 0.75;
    const endPoint = vh * 0.25;
    const totalDist = wrapRect.height + (startPoint - endPoint);
    const scrolled = startPoint - wrapRect.top;
    const progress = Math.max(0, Math.min(1, scrolled / totalDist));
    
    // Strict sequential word-by-word activation count based on scroll progression
    const activeCount = Math.min(allWords.length, Math.floor(progress * (allWords.length + 1)));

    for (let i = 0; i < allWords.length; i++) {
      const word = allWords[i];
      if (i < activeCount) {
        word.classList.add('is-highlighted');
        if (i === activeCount - 1) {
          word.classList.add('is-active-word');
        } else {
          word.classList.remove('is-active-word');
        }
      } else {
        word.classList.remove('is-highlighted');
        word.classList.remove('is-active-word');
      }
    }
  }

  if (!storyScrollListenerAttached) {
    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          updateHighlights();
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    storyScrollListenerAttached = true;
  }

  // Check on update
  updateHighlights();
}

// Toggle truncated story text after 1000 characters
function toggleStoryTruncation() {
  const truncatedWrap = document.getElementById('story-truncated-content');
  const btn = document.getElementById('story-read-more-btn');
  const btnText = btn ? btn.querySelector('span') : null;
  
  if (!truncatedWrap) return;

  const isHidden = truncatedWrap.style.display === 'none';
  
  if (isHidden) {
    truncatedWrap.style.display = 'flex';
    if (btnText) btnText.textContent = 'Read Less';
    if (btn) btn.classList.add('is-expanded');
    initStoryScrollHighlight();
  } else {
    truncatedWrap.style.display = 'none';
    if (btnText) btnText.textContent = 'Read More';
    if (btn) btn.classList.remove('is-expanded');
    initStoryScrollHighlight();
  }
}

window.toggleStoryTruncation = toggleStoryTruncation;

function openStoryModal() {
  const modal = document.getElementById('story-modal-overlay');
  if (modal) {
    modal.style.display = 'flex';
    document.body.classList.add('no-scroll');
  }
}

function closeStoryModal() {
  const modal = document.getElementById('story-modal-overlay');
  if (modal) {
    modal.style.display = 'none';
    document.body.classList.remove('no-scroll');
  }
}

// Close story modal on backdrop click or Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeStoryModal();
  }
});

document.addEventListener('click', (e) => {
  const modal = document.getElementById('story-modal-overlay');
  if (modal && e.target === modal) {
    closeStoryModal();
  }
});

// ==========================================================================
// 16. VIDEO COMMERCE & SHOPPABLE REELS ("Stories in Motion")
// ==========================================================================

let reelsData = [
  {
    id: 'reel-1',
    title: 'Carving Teakwood Easels',
    caption: 'Behind the scenes in the atelier: precision-grooving solid teakwood easels to cradle our high-gloss optical acrylic coasters. ☕✨',
    duration: '0:24',
    views: '18.4K',
    likes: 1420,
    isLiked: false,
    poster: 'assets/products/lady_teatrip.jpg',
    videoSrc: '',
    productId: 'prod-1'
  },
  {
    id: 'reel-2',
    title: 'Midnight Thread Art Portrait',
    caption: 'Over 8,000 geometric thread intersections to bring a couple’s anniversary portrait to life. Hand-stitched with archival silk.',
    duration: '0:38',
    views: '34.2K',
    likes: 2890,
    isLiked: false,
    poster: 'assets/products/photo_thread_art_portrait.png',
    videoSrc: '',
    productId: 'prod-8'
  },
  {
    id: 'reel-3',
    title: 'Crafting Sunflower Bookmarks',
    caption: 'Laser-carved from sustainable birchwood and hand-finished with silky amber tassels. For readers who cherish tactile page-markers. 📖🌿',
    duration: '0:19',
    views: '12.8K',
    likes: 980,
    isLiked: false,
    poster: 'assets/products/wood_flower_bookmark.jpg',
    videoSrc: '',
    productId: 'prod-4'
  },
  {
    id: 'reel-4',
    title: 'Unboxing 2026 Artist Calendar',
    caption: '12 months of hand-drawn studio art on 350 GSM archival textured matte paper with a bespoke wooden display easel.',
    duration: '0:29',
    views: '26.1K',
    likes: 2150,
    isLiked: false,
    poster: 'assets/products/artist_calendar.jpg',
    videoSrc: '',
    productId: 'prod-2'
  },
  {
    id: 'reel-5',
    title: 'Botanical Wall Hoop Process',
    caption: 'From raw embroidery hoop to finished cherry blossom wall decor. Each delicate petal is hand-dyed and secured in our studio.',
    duration: '0:32',
    views: '15.9K',
    likes: 1670,
    isLiked: false,
    poster: 'assets/products/cherry_blossom.png',
    videoSrc: '',
    productId: 'prod-36'
  }
];

let activeViewerIndex = 0;
let isViewerMuted = true;
let reelObserver = null;
let uploadedVideoBlobUrl = null;
let simulatedVideoInterval = null;
let simulatedProgress = 0;

function initVideoCommerce() {
  const track = document.getElementById('reels-track');
  if (!track) return;

  renderReels();
  initReelsAutoplayObserver();
  initReelsCarouselScroll();
}

function renderReels() {
  const track = document.getElementById('reels-track');
  const dotsWrap = document.getElementById('reels-dots-wrap');
  if (!track) return;

  track.innerHTML = reelsData.map((reel, index) => {
    const prod = productsData.find(p => p.id === reel.productId) || productsData[0];
    const discount = prod.mrp ? Math.round(((prod.mrp - prod.price) / prod.mrp) * 100) : 0;

    return `
      <article class="reel-card" data-reel-id="${reel.id}" onclick="openReelViewerModal('${reel.id}')" aria-label="Watch shoppable reel: ${reel.title}">
        <!-- Video Media Background -->
        <div class="reel-media-wrap">
          ${reel.videoSrc ? `
            <video class="reel-video-element" loop muted playsinline poster="${reel.poster}" src="${reel.videoSrc}"></video>
          ` : `
            <div class="reel-poster-backdrop" style="background-image: url('${reel.poster}');"></div>
          `}
          <div class="reel-vignette"></div>
        </div>

        <!-- Top Bar Overlays -->
        <div class="reel-card-topbar">
          <span class="reel-views-pill">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            ${reel.views} • ${reel.duration}
          </span>
          <button class="reel-card-sound-btn" onclick="toggleCardSound(event, '${reel.id}')" aria-label="Toggle audio on card" title="Toggle audio">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
              <line x1="23" y1="9" x2="17" y2="15"></line>
              <line x1="17" y1="9" x2="23" y2="15"></line>
            </svg>
          </button>
        </div>

        <!-- Center Play/Pause Indicator -->
        <div class="reel-play-indicator" aria-hidden="true">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"></polygon></svg>
        </div>

        <!-- Bottom Story Info & Tagged Shoppable Hotspot -->
        <div class="reel-card-bottom">
          <div class="reel-card-meta">
            <h3 class="reel-card-title">${reel.title}</h3>
            <p class="reel-card-desc">${reel.caption}</p>
          </div>

          <!-- Shoppable Hotspot Product Pill -->
          <div class="reel-product-pill" onclick="handlePillClick(event, '${prod.id}')" role="button" aria-label="Shop featured product: ${prod.name}">
            <img src="${prod.image}" alt="${prod.name}" class="reel-pill-thumb" loading="lazy" />
            <div class="reel-pill-info">
              <span class="reel-pill-title">${prod.name}</span>
              <div class="reel-pill-price-row">
                <span class="reel-pill-price">₹${prod.price.toLocaleString('en-IN')}</span>
                ${prod.mrp ? `<span class="reel-pill-mrp">₹${prod.mrp.toLocaleString('en-IN')}</span>` : ''}
              </div>
            </div>
            <button class="reel-pill-buy-btn" onclick="handlePillQuickBuy(event, '${prod.id}')" title="Quick Add to Bag" aria-label="Add ${prod.name} to bag">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
                <path d="M3 6h18"/>
                <path d="M16 10a4 4 0 0 1-8 0"/>
              </svg>
            </button>
          </div>
        </div>
      </article>
    `;
  }).join('');

  // Generate mobile pagination dots
  if (dotsWrap) {
    dotsWrap.innerHTML = reelsData.map((_, idx) => `
      <span class="reel-dot ${idx === 0 ? 'active' : ''}" onclick="scrollReelTo(${idx})" aria-label="Go to reel ${idx + 1}"></span>
    `).join('');
  }
}

// Handle Pill Click: Open product quick view without opening the reel theater
function handlePillClick(e, prodId) {
  e.stopPropagation();
  openQuickView(prodId);
}

// Handle Pill Quick Buy: Add directly to cart with notification
function handlePillQuickBuy(e, prodId) {
  e.stopPropagation();
  addToCart(prodId, 1);
}

// Viewport Autoplay Observer (Muted auto-play on viewport entry)
function initReelsAutoplayObserver() {
  if (!('IntersectionObserver' in window)) return;

  if (reelObserver) reelObserver.disconnect();

  reelObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const card = entry.target;
      const video = card.querySelector('video');
      if (!video) return;

      if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
        video.play().then(() => {
          card.classList.remove('is-paused');
        }).catch(() => {
          // Autoplay blocked by browser policy; stays muted with poster fallback
        });
      } else {
        video.pause();
        card.classList.add('is-paused');
      }
    });
  }, {
    threshold: [0, 0.5, 1.0]
  });

  const cards = document.querySelectorAll('.reel-card');
  cards.forEach(card => reelObserver.observe(card));
}

// Horizontal Carousel Scroll Controls
function scrollReelsTrack(direction) {
  const wrapper = document.getElementById('reels-carousel-wrapper');
  if (!wrapper) return;
  const scrollAmount = 312 * direction;
  wrapper.scrollBy({ left: scrollAmount, behavior: 'smooth' });
}

function scrollReelTo(index) {
  const wrapper = document.getElementById('reels-carousel-wrapper');
  const cards = document.querySelectorAll('.reel-card');
  if (wrapper && cards[index]) {
    wrapper.scrollTo({
      left: cards[index].offsetLeft - wrapper.offsetLeft - 16,
      behavior: 'smooth'
    });
  }
}

function initReelsCarouselScroll() {
  const wrapper = document.getElementById('reels-carousel-wrapper');
  if (!wrapper) return;

  wrapper.addEventListener('scroll', () => {
    updateReelDots();
  }, { passive: true });
}

function updateReelDots() {
  const wrapper = document.getElementById('reels-carousel-wrapper');
  const dots = document.querySelectorAll('.reel-dot');
  const cards = document.querySelectorAll('.reel-card');
  if (!wrapper || !dots.length || !cards.length) return;

  const scrollLeft = wrapper.scrollLeft;
  let activeIdx = 0;
  let minDiff = Infinity;

  cards.forEach((card, idx) => {
    const cardLeft = card.offsetLeft - wrapper.offsetLeft;
    const diff = Math.abs(scrollLeft - cardLeft);
    if (diff < minDiff) {
      minDiff = diff;
      activeIdx = idx;
    }
  });

  dots.forEach((dot, idx) => {
    dot.classList.toggle('active', idx === activeIdx);
  });
}

function toggleCardSound(e, reelId) {
  e.stopPropagation();
  const card = document.querySelector(`.reel-card[data-reel-id="${reelId}"]`);
  if (!card) return;
  const video = card.querySelector('video');
  if (video) {
    video.muted = !video.muted;
    const btn = card.querySelector('.reel-card-sound-btn');
    if (btn) {
      btn.innerHTML = video.muted ? `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
          <line x1="23" y1="9" x2="17" y2="15"></line>
          <line x1="17" y1="9" x2="23" y2="15"></line>
        </svg>
      ` : `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
          <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
        </svg>
      `;
    }
  } else {
    showToast('Sound enabled for Studio Reels');
  }
}

// ==========================================================================
// EXPANDED FULLSCREEN REEL THEATER MODAL
// ==========================================================================

function openReelViewerModal(reelId) {
  const index = reelsData.findIndex(r => r.id === reelId);
  if (index === -1) return;

  activeViewerIndex = index;
  const modal = document.getElementById('reel-viewer-modal');
  if (!modal) return;

  modal.style.display = 'flex';
  document.body.classList.add('no-scroll');

  // Pause all background carousel videos
  document.querySelectorAll('.reel-video-element').forEach(v => v.pause());

  loadViewerReel(activeViewerIndex);
}

function loadViewerReel(index) {
  const reel = reelsData[index];
  if (!reel) return;

  const titleEl = document.getElementById('viewer-reel-title');
  const captionEl = document.getElementById('viewer-reel-caption');
  const videoEl = document.getElementById('reel-viewer-video');
  const iframeEl = document.getElementById('reel-viewer-iframe');
  const fallbackEl = document.getElementById('reel-viewer-poster-fallback');
  const scrubberFill = document.getElementById('viewer-scrubber-fill');
  const likeBtn = document.getElementById('viewer-like-btn');
  const likeCountEl = document.getElementById('viewer-like-count');
  const tapZone = document.querySelector('.reel-stage-tap-zone');

  if (titleEl) titleEl.textContent = reel.title;
  if (captionEl) captionEl.textContent = reel.caption;

  // Like status
  if (likeBtn && likeCountEl) {
    likeBtn.classList.toggle('is-liked', !!reel.isLiked);
    likeCountEl.textContent = (reel.likes || 1200).toLocaleString('en-IN');
  }

  // Handle Video / Instagram / Poster Fallback
  if (reel.isInstagram && reel.instagramEmbed) {
    if (videoEl) videoEl.style.display = 'none';
    if (fallbackEl) fallbackEl.style.display = 'none';
    if (iframeEl) {
      iframeEl.style.display = 'block';
      iframeEl.src = reel.instagramEmbed;
    }
  } else if (reel.videoSrc) {
    if (iframeEl) iframeEl.style.display = 'none';
    if (fallbackEl) fallbackEl.style.display = 'none';
    if (videoEl) {
      videoEl.style.display = 'block';
      videoEl.src = reel.videoSrc;
      videoEl.poster = reel.poster;
      videoEl.muted = isViewerMuted;
      videoEl.currentTime = 0;
      videoEl.play().catch(() => {});
      
      videoEl.ontimeupdate = () => {
        if (videoEl.duration && scrubberFill) {
          const pct = (videoEl.currentTime / videoEl.duration) * 100;
          scrubberFill.style.width = `${pct}%`;
        }
      };
    }
  } else {
    // Elegant Simulated Atelier Motion Loop
    if (iframeEl) iframeEl.style.display = 'none';
    if (videoEl) videoEl.style.display = 'none';
    if (fallbackEl) {
      fallbackEl.style.display = 'block';
      fallbackEl.style.backgroundImage = `url('${reel.poster}')`;
    }
    startSimulatedProgress(scrubberFill);
  }

  // Update Tagged Product Card in Viewer
  const prod = productsData.find(p => p.id === reel.productId) || productsData[0];
  const prodImg = document.getElementById('viewer-prod-img');
  const prodName = document.getElementById('viewer-prod-name');
  const prodPrice = document.getElementById('viewer-prod-price');
  const prodMrp = document.getElementById('viewer-prod-mrp');
  const prodBadge = document.getElementById('viewer-prod-badge');

  if (prodImg) prodImg.src = prod.image;
  if (prodName) prodName.textContent = prod.name;
  if (prodPrice) prodPrice.textContent = `₹${prod.price.toLocaleString('en-IN')}`;
  if (prodMrp) prodMrp.textContent = prod.mrp ? `₹${prod.mrp.toLocaleString('en-IN')}` : '';
  if (prodBadge) prodBadge.textContent = prod.badge || 'Atelier Edition';

  if (tapZone) tapZone.classList.remove('is-paused');
}

function startSimulatedProgress(fillEl) {
  clearInterval(simulatedVideoInterval);
  simulatedProgress = 0;
  simulatedVideoInterval = setInterval(() => {
    simulatedProgress += 1;
    if (simulatedProgress > 100) simulatedProgress = 0;
    if (fillEl) fillEl.style.width = `${simulatedProgress}%`;
  }, 180);
}

function closeReelViewerModal() {
  const modal = document.getElementById('reel-viewer-modal');
  const videoEl = document.getElementById('reel-viewer-video');
  const iframeEl = document.getElementById('reel-viewer-iframe');
  
  if (videoEl) {
    videoEl.pause();
    videoEl.src = '';
  }
  if (iframeEl) {
    iframeEl.src = '';
  }
  clearInterval(simulatedVideoInterval);

  if (modal) {
    modal.style.display = 'none';
    document.body.classList.remove('no-scroll');
  }

  // Re-observe and play visible track reels
  initReelsAutoplayObserver();
}

function navigateViewerReel(delta) {
  let newIndex = activeViewerIndex + delta;
  if (newIndex < 0) newIndex = reelsData.length - 1;
  if (newIndex >= reelsData.length) newIndex = 0;
  activeViewerIndex = newIndex;
  loadViewerReel(activeViewerIndex);
}

function toggleViewerPlayPause() {
  const videoEl = document.getElementById('reel-viewer-video');
  const tapZone = document.querySelector('.reel-stage-tap-zone');
  
  if (videoEl && videoEl.src) {
    if (videoEl.paused) {
      videoEl.play();
      if (tapZone) tapZone.classList.remove('is-paused');
    } else {
      videoEl.pause();
      if (tapZone) tapZone.classList.add('is-paused');
    }
  } else {
    // Simulated pause
    if (tapZone) {
      tapZone.classList.toggle('is-paused');
    }
  }
}

function toggleViewerSound() {
  const videoEl = document.getElementById('reel-viewer-video');
  const soundBtn = document.getElementById('viewer-sound-btn');
  isViewerMuted = !isViewerMuted;

  if (videoEl) {
    videoEl.muted = isViewerMuted;
  }

  if (soundBtn) {
    const unmutedIcon = soundBtn.querySelector('.icon-unmuted');
    const mutedIcon = soundBtn.querySelector('.icon-muted');
    if (unmutedIcon && mutedIcon) {
      unmutedIcon.style.display = isViewerMuted ? 'none' : 'block';
      mutedIcon.style.display = isViewerMuted ? 'block' : 'none';
    }
  }
}

function toggleReelLike() {
  const reel = reelsData[activeViewerIndex];
  if (!reel) return;

  reel.isLiked = !reel.isLiked;
  reel.likes = reel.isLiked ? reel.likes + 1 : reel.likes - 1;

  const likeBtn = document.getElementById('viewer-like-btn');
  const likeCountEl = document.getElementById('viewer-like-count');

  if (likeBtn) likeBtn.classList.toggle('is-liked', reel.isLiked);
  if (likeCountEl) likeCountEl.textContent = reel.likes.toLocaleString('en-IN');

  if (reel.isLiked) {
    showToast('✦ Saved to your favorite stories');
  }
}

function scrubViewerVideo(e) {
  const scrubber = document.getElementById('viewer-scrubber-bar');
  const videoEl = document.getElementById('reel-viewer-video');
  if (!scrubber || !videoEl || !videoEl.duration) return;

  const rect = scrubber.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const pct = Math.max(0, Math.min(1, clickX / rect.width));
  videoEl.currentTime = pct * videoEl.duration;
}

function buyViewerProduct() {
  const reel = reelsData[activeViewerIndex];
  if (!reel) return;
  const prodId = reel.productId;
  addToCart(prodId, 1);
  closeReelViewerModal();
}

function viewViewerProductDetails() {
  const reel = reelsData[activeViewerIndex];
  if (!reel) return;
  const prodId = reel.productId;
  closeReelViewerModal();
  openQuickView(prodId);
}

function shareCurrentReel() {
  const reel = reelsData[activeViewerIndex];
  if (!reel) return;
  const shareData = {
    title: `${reel.title} — Graffeine Tales Stories in Motion`,
    text: reel.caption,
    url: window.location.href.split('#')[0] + '#stories-in-motion'
  };

  if (navigator.share) {
    navigator.share(shareData).catch(() => {});
  } else {
    navigator.clipboard.writeText(shareData.url).then(() => {
      showToast('✦ Reel link copied to clipboard');
    }).catch(() => {
      showToast('✦ Link ready: ' + shareData.url);
    });
  }
}

// ==========================================================================
// DUAL INGESTION ARCHITECTURE (Manual Upload + Instagram Reel)
// ==========================================================================

function openReelIngestModal() {
  const modal = document.getElementById('reel-ingest-modal');
  const prodSelect = document.getElementById('ingest-product-select');
  if (!modal) return;

  // Populate products dropdown from catalogue
  if (prodSelect) {
    prodSelect.innerHTML = productsData.map(p => `
      <option value="${p.id}">${p.name} — ₹${p.price.toLocaleString('en-IN')}</option>
    `).join('');
  }

  modal.style.display = 'flex';
  document.body.classList.add('no-scroll');
}

function closeReelIngestModal() {
  const modal = document.getElementById('reel-ingest-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.classList.remove('no-scroll');
  }
}

function switchIngestTab(tab) {
  const tabUpload = document.getElementById('tab-btn-upload');
  const tabIg = document.getElementById('tab-btn-instagram');
  const panelUpload = document.getElementById('panel-upload');
  const panelIg = document.getElementById('panel-instagram');

  if (tab === 'upload') {
    tabUpload.classList.add('active');
    tabUpload.setAttribute('aria-selected', 'true');
    tabIg.classList.remove('active');
    tabIg.setAttribute('aria-selected', 'false');
    panelUpload.classList.add('active');
    panelUpload.style.display = 'block';
    panelIg.classList.remove('active');
    panelIg.style.display = 'none';
  } else {
    tabIg.classList.add('active');
    tabIg.setAttribute('aria-selected', 'true');
    tabUpload.classList.remove('active');
    tabUpload.setAttribute('aria-selected', 'false');
    panelIg.classList.add('active');
    panelIg.style.display = 'block';
    panelUpload.classList.remove('active');
    panelUpload.style.display = 'none';
  }
}

function handleManualVideoSelect(event) {
  const file = event.target.files[0];
  if (!file) return;

  uploadedVideoBlobUrl = URL.createObjectURL(file);
  const promptBox = document.getElementById('dropzone-prompt');
  const selectedInfo = document.getElementById('dropzone-selected-info');
  const nameEl = document.getElementById('selected-file-name');
  const sizeEl = document.getElementById('selected-file-size');
  const miniPreview = document.getElementById('ingest-mini-preview');

  if (promptBox) promptBox.style.display = 'none';
  if (selectedInfo) selectedInfo.style.display = 'flex';
  if (nameEl) nameEl.textContent = file.name;
  if (sizeEl) sizeEl.textContent = `${(file.size / (1024 * 1024)).toFixed(1)} MB`;
  if (miniPreview) {
    miniPreview.src = uploadedVideoBlobUrl;
    miniPreview.play().catch(() => {});
  }

  // Pre-fill title if empty
  const titleInput = document.getElementById('ingest-reel-title');
  if (titleInput && !titleInput.value) {
    titleInput.value = file.name.replace(/\.[^/.]+$/, '').replace(/[-_]/g, ' ');
  }
}

function removeSelectedVideoFile(event) {
  event.stopPropagation();
  uploadedVideoBlobUrl = null;
  const fileInput = document.getElementById('ingest-video-file');
  if (fileInput) fileInput.value = '';

  const promptBox = document.getElementById('dropzone-prompt');
  const selectedInfo = document.getElementById('dropzone-selected-info');
  const miniPreview = document.getElementById('ingest-mini-preview');

  if (promptBox) promptBox.style.display = 'block';
  if (selectedInfo) selectedInfo.style.display = 'none';
  if (miniPreview) {
    miniPreview.pause();
    miniPreview.src = '';
  }
}

function handlePosterSelectChange(event) {
  // Handled on submit
}

function fetchInstagramReelPreview() {
  const urlInput = document.getElementById('ingest-instagram-url');
  const url = (urlInput ? urlInput.value.trim() : '');
  const previewBox = document.getElementById('instagram-preview-box');
  const idLabel = document.getElementById('ig-reel-id-label');
  const iframe = document.getElementById('ig-preview-iframe');

  if (!url) {
    showToast('Please paste a valid Instagram Reel URL');
    return;
  }

  // Match Instagram Reel ID: e.g. /reel/C31234abc/ or /p/C31234abc/
  const match = url.match(/\/(?:reel|p)\/([A-Za-z0-9_-]+)/);
  const reelId = match ? match[1] : 'C' + Math.random().toString(36).substring(2, 9);

  if (previewBox) previewBox.style.display = 'block';
  if (idLabel) idLabel.textContent = `Reel ID: ${reelId}`;
  if (iframe) {
    iframe.src = `https://www.instagram.com/reel/${reelId}/embed`;
  }

  showToast('✦ Instagram Reel verified & ready to stream');
}

function handleReelIngestSubmit(event) {
  event.preventDefault();

  const isIgTab = document.getElementById('tab-btn-instagram').classList.contains('active');
  const title = document.getElementById('ingest-reel-title').value.trim();
  const caption = document.getElementById('ingest-reel-caption').value.trim();
  const productId = document.getElementById('ingest-product-select').value;
  const poster = document.getElementById('ingest-poster-select').value;

  if (!title) {
    showToast('Please enter a reel title');
    return;
  }

  let videoSrc = '';
  let isInstagram = false;
  let instagramEmbed = '';

  if (isIgTab) {
    const igUrl = document.getElementById('ingest-instagram-url').value.trim();
    if (!igUrl) {
      showToast('Please enter an Instagram Reel link');
      return;
    }
    const match = igUrl.match(/\/(?:reel|p)\/([A-Za-z0-9_-]+)/);
    const reelId = match ? match[1] : 'C_Studio';
    isInstagram = true;
    instagramEmbed = `https://www.instagram.com/reel/${reelId}/embed`;
  } else {
    if (uploadedVideoBlobUrl) {
      videoSrc = uploadedVideoBlobUrl;
    }
  }

  const newReel = {
    id: 'reel-custom-' + Date.now(),
    title: title,
    caption: caption || 'Crafted with human patience and tactile warmth in our studio atelier.',
    duration: '0:30',
    views: '1.2K',
    likes: 48,
    isLiked: false,
    poster: poster || 'assets/products/lady_teatrip.jpg',
    videoSrc: videoSrc,
    isInstagram: isInstagram,
    instagramEmbed: instagramEmbed,
    productId: productId
  };

  // Prepend new reel into live feed
  reelsData.unshift(newReel);
  renderReels();
  initReelsAutoplayObserver();

  // Reset form and close
  closeReelIngestModal();
  document.getElementById('reel-ingest-form').reset();
  removeSelectedVideoFile({ stopPropagation: () => {} });

  showToast(`✦ "${title}" published live to Stories in Motion!`);

  // Scroll smoothly to the new reel
  const section = document.getElementById('stories-in-motion');
  if (section) section.scrollIntoView({ behavior: 'smooth' });
}

// Global modal escape listener for reels
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeReelViewerModal();
    closeReelIngestModal();
  } else if (e.key === 'ArrowLeft') {
    const viewer = document.getElementById('reel-viewer-modal');
    if (viewer && viewer.style.display !== 'none') {
      navigateViewerReel(-1);
    }
  } else if (e.key === 'ArrowRight') {
    const viewer = document.getElementById('reel-viewer-modal');
    if (viewer && viewer.style.display !== 'none') {
      navigateViewerReel(1);
    }
  }
});

// Expose Video Commerce methods to global window
window.initVideoCommerce = initVideoCommerce;
window.renderReels = renderReels;
window.scrollReelsTrack = scrollReelsTrack;
window.scrollReelTo = scrollReelTo;
window.toggleCardSound = toggleCardSound;
window.handlePillClick = handlePillClick;
window.handlePillQuickBuy = handlePillQuickBuy;
window.openReelViewerModal = openReelViewerModal;
window.closeReelViewerModal = closeReelViewerModal;
window.navigateViewerReel = navigateViewerReel;
window.toggleViewerPlayPause = toggleViewerPlayPause;
window.toggleViewerSound = toggleViewerSound;
window.toggleReelLike = toggleReelLike;
window.scrubViewerVideo = scrubViewerVideo;
window.buyViewerProduct = buyViewerProduct;
window.viewViewerProductDetails = viewViewerProductDetails;
window.shareCurrentReel = shareCurrentReel;
window.openReelIngestModal = openReelIngestModal;
window.closeReelIngestModal = closeReelIngestModal;
window.switchIngestTab = switchIngestTab;
window.handleManualVideoSelect = handleManualVideoSelect;
window.removeSelectedVideoFile = removeSelectedVideoFile;
window.handlePosterSelectChange = handlePosterSelectChange;
window.fetchInstagramReelPreview = fetchInstagramReelPreview;
window.handleReelIngestSubmit = handleReelIngestSubmit;

// 12. Footer Newsletter Handler
function handleFooterNewsletterSubmit(event) {
  if (event) event.preventDefault();
  const input = document.getElementById('footer-newsletter-email');
  const consent = document.getElementById('footer-subscribe-consent');
  const email = input ? input.value.trim() : '';

  if (!email) {
    if (typeof showToast === 'function') {
      showToast('Please enter your email address.');
    }
    return;
  }

  if (consent && !consent.checked) {
    if (typeof showToast === 'function') {
      showToast('Please check the box to confirm your subscription.');
    }
    return;
  }

  if (typeof showToast === 'function') {
    showToast(`✦ Welcome to our circle! Inspiration is on its way to ${email}.`);
  }

  if (input) input.value = '';
}

window.handleFooterNewsletterSubmit = handleFooterNewsletterSubmit;



