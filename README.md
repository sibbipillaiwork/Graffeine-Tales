# ☕ Graffeine Tales — Where Stories Become Art
> **Artisanal Stationery, Handcrafted Journals, Teak Décor & Bespoke Gifting**  
> *Production-Ready Front-End & Shopify Online Store 2.0 Theme Suite*

[![Shopify OS 2.0](https://img.shields.io/badge/Shopify-Online%20Store%202.0-7AB55C?logo=shopify&logoColor=white)](#shopify-installation)
[![UI/UX Pro Max](https://img.shields.io/badge/Design-Editorial%20Luxury-5A3825)](#design-system)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success)](#)

---

## ✦ Overview
Graffeine Tales is an editorial, luxury D2C e-commerce experience designed for an artisanal studio. Built with tactile warmth, rich storytelling, interactive video commerce ("Stories in Motion"), and native Shopify Online Store 2.0 compatibility.

### Key Features
- **Brand Identity & Atmosphere:** Warm Saddle (`#5A3825`), Terracotta Clay (`#C85A32`), Charcoal Espresso (`#363638`), and Atelier Cream (`#FDFBF7`) palette with `DM Serif Display` and `Inter` typography.
- **Steam Animated Emblem:** Coffee cup logo with continuous CSS keyframe steam wisps.
- **Interactive Mega-Menu & Mobile Bottom Dock:** Desktop hover mega-navigation and a glassmorphism bottom mobile bar.
- **Stories in Motion (Video Commerce):** 9:16 shoppable video reels feed, fullscreen theater modal with interactive scrubber & product drawer, and dual creator ingest engine (direct upload + Instagram reel embed).
- **Jawa Yezdi Inspired Story Section:** Scroll-triggered progressive text illumination highlighting the atelier’s craft philosophy.
- **Live Slide-Over Cart Drawer:** Free studio shipping milestone progress meter (₹1,499 threshold), quantity adjustment steppers, and direct checkout redirect.
- **Shopify Online Store 2.0 Ready:** Full native theme structure with modular `.liquid` sections, JSON templates, and AJAX Cart API bridge (`/cart.js`, `/cart/add.js`, `/checkout`).

---

## ✦ Repository Architecture

```
GTB/
├── shopify-theme/                   # Complete Shopify Online Store 2.0 Theme
│   ├── assets/                      # styles.css, app.js, shopify-cart.js, 80+ studio images
│   ├── config/                      # settings_schema.json, settings_data.json
│   ├── layout/                      # theme.liquid
│   ├── locales/                     # en.default.json
│   ├── sections/                    # 26 modular Liquid sections (Header, Hero, Reels, Cart, PDP, etc.)
│   ├── snippets/                    # product-card.liquid
│   └── templates/                   # index.json, product.json, collection.json, cart.json, etc.
│
├── Graffeine-Tales-Shopify-Theme.zip # Ready-to-upload theme zip for Shopify Admin
├── index.html                       # Standalone high-fidelity web storefront
├── styles.css                       # Complete design system & responsive styling
├── app.js                           # Storefront interactive engine & state management
├── products_data.json               # Full catalogue data
├── design.md                        # UI/UX Design System Specification & Hi-Fi Flows
└── shopify_ai_prompt.md             # Master AI Development Prompt
```

---

## ✦ Shopify Theme Installation

1. Navigate to your **Shopify Admin** (`https://admin.shopify.com/store/YOUR-STORE`).
2. Head to **Online Store** → **Themes**.
3. Under **Theme Library**, click **Add theme** → **Upload zip file**.
4. Select `Graffeine-Tales-Shopify-Theme.zip`.
5. Once uploaded, click **Actions** → **Publish** or **Preview**.

*Or deploy via Shopify CLI:*
```bash
cd shopify-theme
shopify theme push
```

---

## ✦ Local Web Preview
To preview the standalone web storefront without a server:
Simply open `index.html` in any modern browser, or launch a lightweight dev server:
```bash
python -m http.server 8000
```
Then visit `http://localhost:8000`.

---

## ✦ Documentation
- Detailed Design System & Hi-Fi Flows: [`design.md`](design.md)
- Master AI Prompt for LLM Theme Generation: [`shopify_ai_prompt.md`](shopify_ai_prompt.md)

---
*© 2026 Graffeine Tales Studio. All Rights Reserved. Where Stories Become Art.*
