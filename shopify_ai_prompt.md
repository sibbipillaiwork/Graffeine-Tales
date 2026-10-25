# MASTER AI DEVELOPMENT PROMPT: GRAFFEINE TALES SHOPIFY STORE

Copy and paste the entire prompt below into any AI assistant (ChatGPT, Claude 3.7, Gemini 1.5/2.0, Cursor, Devin, etc.) to develop, reconstruct, or maintain the Graffeine Tales Shopify store from scratch:

```markdown
You are an expert Shopify Online Store 2.0 theme architect and award-winning e-commerce frontend engineer specializing in luxury D2C, artisanal craft, and video commerce storefronts.

Your task is to build/reconstruct the complete, production-grade Shopify Online Store 2.0 theme for "Graffeine Tales" (Brand Tagline: "Where Stories Become Art" — Artisanal Stationery, Handcrafted Journals & Bespoke Gifting).

---

### 1. BRAND ESSENCE & DESIGN SYSTEM
- **Aesthetic Mood:** Editorial luxury, tactile warmth, artisanal craft storytelling, indie studio warmth. Avoid generic, sterile corporate e-commerce styling.
- **Color System (CSS Variables):**
  - `--c-primary`: `#5A3825` (Warm Saddle Leather — main brand color)
  - `--c-accent-clay`: `#C85A32` (Terracotta Clay — CTA highlights, urgency, sale tags)
  - `--c-espresso`: `#363638` (Charcoal Espresso — deep text, story section background)
  - `--c-bg-cream`: `#FDFBF7` (Atelier Cream — primary website canvas)
  - `--c-bg-sand`: `#F8F5F0` (Bone Sand — cards, modal surfaces)
  - `--c-gold`: `#D4AF37` (Wax Seal Gold — 5.0 star reviews, bestseller badges)
  - `--c-sage`: `#2D6A4F` (Botanical Sage — studio drops, eco-friendly badges)
- **Typography:**
  - Display Headings: `'DM Serif Display', Georgia, serif`
  - Body & UI: `'Inter', -apple-system, sans-serif`
  - Handwritten Accents: `'Patrick Hand', cursive`
  - Badges & Subheadings: `'Quicksand', sans-serif`

---

### 2. ARCHITECTURAL REQUIREMENTS (SHOPIFY OS 2.0)
Structure the project strictly according to Shopify Online Store 2.0 specifications:
- `layout/theme.liquid`: Main HTML5 wrapper with `{{ content_for_header }}`, Google Fonts, global CSS/JS, and `{{ content_for_layout }}`.
- `templates/`: OS 2.0 JSON templates (`index.json`, `product.json`, `collection.json`, `cart.json`, `page.json`, `404.json`).
- `sections/`: Modular Liquid sections with customizable `{% schema %}` settings:
  1. `header.liquid`: Sticky header with coffee cup logo with animated CSS steam wisps, full mega-menu dropdowns, Cmd+K search trigger, wishlist badge, and cart trigger.
  2. `hero-carousel.liquid`: Full-width editorial carousel with touch swiping, slide pagination, and dual CTAs.
  3. `categories-grid.liquid`: Asymmetric editorial grid showcasing 5 core categories:
     - Stationaries & Calendars
     - Journals & Planners
     - Handcrafted Décor & Teak Coasters
     - Events & Personalized Door Tags
     - Bulk Orders & Corporate Gifting
  4. `new-launch.liquid` & `bestsellers.liquid`: Dynamic product sliders/grids with gold/sage pill badges.
  5. `built-with-heart.liquid`: Showcase for personalized craft (Photo Thread Art, customized embroidery).
  6. `catalogue.liquid`: Complete store catalogue with category-only filter tabs (All, Stationaries, Journals, Décor, Events, Bulk) and responsive product cards.
  7. `about-story.liquid`: Jawa Yezdi inspired progressive text-highlight scroll section (Charcoal Espresso `#363638` background, glowing text as user scrolls down).
  8. `stories-reels.liquid`: 9:16 vertical video commerce carousel with sound toggles, shoppable product hotspot pills, and fullscreen 9:16 theater modal.
  9. `reviews.liquid`: Social proof grid with 2,400+ reviews, star ratings, and verified buyer badges.
  10. `footer.liquid`: Reference-grade artisanal footer with botanical vine accents, newsletter subscription form, customer service links, and animated coffee cup emblem.
  11. `cart-drawer.liquid`: Luxury slide-over cart drawer with dynamic Free Shipping progress bar (threshold: ₹1,499), quantity adjustment steppers, and direct checkout redirect to `/checkout`.
  12. `search-modal.liquid`: Instant search modal with live filtering.
  13. `wishlist-drawer.liquid`: Saved items slide-over drawer.
  14. `quick-view-modal.liquid`: Product quick preview with image, specs list, quantity selector, and AJAX Add to Bag.
  15. `mobile-nav.liquid` & `mobile-bottom-nav.liquid`: Dedicated mobile drawer navigation and fixed glassmorphism bottom dock (Home, Categories, Wishlist, Cart, Account).
  16. `main-product.liquid`: Dedicated PDP with sticky image gallery, variant picker, quantity stepper, "Add to Atelier Bag", and dynamic checkout button (UPI / Shop Pay / Cards).
  17. `main-collection.liquid`, `main-cart.liquid`, `main-page.liquid`, `main-404.liquid`.
- `snippets/product-card.liquid`: Reusable card with hover action overlays, badges, pricing in `{{ product.price | money }}`, and AJAX cart addition.
- `assets/`: Vanilla CSS (`styles.css`), core frontend logic (`app.js`), and Shopify AJAX Cart API bridge (`shopify-cart.js`).

---

### 3. CART & VIDEO COMMERCE LOGIC
1. **Shopify AJAX Cart Engine (`shopify-cart.js`):**
   - Must hook directly to Shopify Cart API (`/cart.js`, `/cart/add.js`, `/cart/change.js`).
   - Adding a product automatically recalculates the free shipping milestone bar (₹1,499) and opens the slide-over drawer optimistically.
   - "Checkout Securely" button redirects directly to Shopify's real, PCI-compliant checkout page (`/checkout`).
2. **Video Commerce & Creator Engine:**
   - 9:16 reels carousel autoplays muted in viewport using IntersectionObserver.
   - Tapping any reel opens a fullscreen 9:16 theater dialog with scrubber bar, like counter, and tagged product card.
   - Dual Ingestion Modal allows the studio team to ingest new reels via direct MP4 file upload OR Instagram Reel link embed, tag a catalog product, and publish live to the feed.

---

### 4. MOBILE & UX STANDARDS
- Complete mobile-first responsive layout (375px, 768px, 1024px, 1440px).
- Bottom glassmorphism bar on mobile screens.
- Zero emojis as icons; use clean, accessible SVG stroke icons.
- WCAG AA compliant color contrast (minimum 4.5:1).
- Smooth CSS cubic-bezier transitions on hover states (150–300ms).
- Graceful fallback: If opened without active Shopify backend, gracefully fall back to local JSON data so the store never appears broken.

Deliver clean, production-ready, modular Liquid, CSS, and JavaScript code.
```
