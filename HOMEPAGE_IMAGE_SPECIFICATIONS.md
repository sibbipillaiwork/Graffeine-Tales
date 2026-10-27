# Graffeine Tales — Homepage Image Dimensions & Asset Specifications

This document outlines the exact image dimensions, aspect ratios, CSS display sizes, recommended upload resolutions, file formats, and file size budgets for all sections on the Graffeine Tales homepage (`index.html` and Shopify theme).

---

## Quick Reference Summary Table

| Section | Element / Selector | Aspect Ratio | Desktop Display Size | Recommended Upload Size (2x Retina) | Format | Max File Size |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **01. Header & Nav** | Brand Cup Icon (`.brand-cup-img`) | 1:1 | 36 × 36 px | **512 × 512 px** | PNG (Transparent) | < 30 KB |
| **01. Header & Nav** | Brand Logo Wordmark (`.brand-logo-img`) | ~4:1 | 200 × 48 px | **600 × 150 px** | SVG or PNG | < 45 KB |
| **01. Header & Nav** | Mega Menu Dropdown Feature (`.mega-feature-img`) | 3:2 | 220 × 120 px | **600 × 400 px** | WebP / JPG | < 60 KB |
| **02. Hero Carousel** | Panoramic Slides (`.hero-carousel-img`) | ~21:9 to 16:9 | 100vw × 480–640 px | **1920 × 800 px** *(or 2400 × 1000 px)* | WebP / JPG | < 250 KB |
| **03. Category Strip** | Category Pill Cards (`.category-pill-card img`) | 1:1.34 (3:4) | 155 × 208 px | **600 × 800 px** | WebP / JPG | < 80 KB |
| **04. New Launch** | Product Card Thumbnail (`.product-thumb`) | 4:5 (or 1:1) | 280 × 250 px | **1000 × 1250 px** *(or 1200 × 1200 px)* | WebP / JPG | < 120 KB |
| **05. Bestsellers** | Product Card Thumbnail (`.product-thumb`) | 4:5 (or 1:1) | 280 × 250 px | **1000 × 1250 px** *(or 1200 × 1200 px)* | WebP / JPG | < 120 KB |
| **06. Built with Heart** | Product Card Thumbnail (`.product-thumb`) | 4:5 (or 1:1) | 280 × 250 px | **1000 × 1250 px** *(or 1200 × 1200 px)* | WebP / JPG | < 120 KB |
| **07. Artisanal Catalog**| Product Card Thumbnail (`.product-thumb`) | 4:5 (or 1:1) | 280 × 250 px | **1000 × 1250 px** *(or 1200 × 1200 px)* | WebP / JPG | < 120 KB |
| **08. Stories in Motion** | 9:16 Video Reels (`.reel-media-wrap video`) | 9:16 | 290 × 515 px | **1080 × 1920 px (Full HD)** | MP4 (H.264) | < 8 MB |
| **08. Stories in Motion** | Video Poster / Cover (`.reel-cover-img`) | 9:16 | 290 × 515 px | **1080 × 1920 px** | WebP / JPG | < 150 KB |
| **08. Stories in Motion** | Reel Floating Product Pill (`.reel-prod-img`) | 1:1 | 42 × 42 px | **200 × 200 px** | WebP / JPG | < 25 KB |
| **08. Stories in Motion** | Creator Avatar (`.creator-avatar`) | 1:1 | 38 × 38 px | **150 × 150 px** | PNG / WebP | < 20 KB |
| **09. Founder Craft** | Editorial Studio Photo (`.founder-photo`) | 4:5 (or 3:4) | 480 × 480 px | **1200 × 1500 px** | WebP / JPG | < 200 KB |
| **10. Customer Reviews**| Reviewer Avatar (`.author-avatar`) | 1:1 | 44 × 44 px | **180 × 180 px** | WebP / JPG | < 25 KB |
| **11. Artisanal Footer** | Corner Vines (`.footer-corner-vine`) | ~3:2 | 240 × 160 px | **600 × 400 px** | PNG (Transparent) | < 60 KB |
| **11. Artisanal Footer** | Central Desk Scene (`.footer-desk-illustration-img`) | ~3.5:1 | 900 × 240 px | **1800 × 500 px** | PNG (Transparent) | < 180 KB |
| **11. Artisanal Footer** | Bottom Flourishes (`.footer-bottom-flourish`) | ~2:1 | 180 × 90 px | **400 × 200 px** | PNG (Transparent) | < 30 KB |
| **12. Quick View Modal** | Modal Product Gallery (`#modal-img`) | 1:1 | 450 × 450 px | **1200 × 1200 px** | WebP / JPG | < 150 KB |

---

## Detailed Section-by-Section Specifications

### 1. Global Header & Navigation (`<header class="site-header">`)

#### A. Brand Coffee Cup Logo (`.brand-cup-img`)
* **Aspect Ratio:** `1:1` (Perfect Square)
* **CSS Display Size:** Desktop `36 × 36 px` | Mobile `32 × 32 px`
* **Recommended Upload Dimensions:** `512 × 512 px` (Retina crispness)
* **File Format:** PNG with transparent background
* **Max File Size:** `30 KB`
* **Art Direction:** Cutout of the signature ceramic cup with dark chocolate/coffee rim and warm latte foam.

#### B. Brand Wordmark Logo (`.brand-logo-img`)
* **Aspect Ratio:** `~4:1` (Horizontal Landscape)
* **CSS Display Size:** Desktop `200 × 48 px` | Mobile `160 × 40 px`
* **Recommended Upload Dimensions:** `600 × 150 px`
* **File Format:** SVG (preferred) or 24-bit transparent PNG
* **Max File Size:** `40 KB`
* **Color:** Deep Charcoal Espresso (`#363638`) for clean contrast against the Warm Paper background (`#F8F5ED`).

#### C. Mega Menu Feature Card Image (`.mega-feature-img`)
* **Aspect Ratio:** `3:2` or `4:3`
* **CSS Display Size:** Container width `220 px` × fixed height `120 px` (`object-fit: contain`)
* **Recommended Upload Dimensions:** `600 × 400 px`
* **File Format:** WebP or JPG
* **Max File Size:** `60 KB`
* **Art Direction:** Centered product on clean ivory or transparent backdrop showcasing the featured drop of the category.

---

### 2. Hero Showcase Carousel (`#hero`, `.hero-carousel`)

* **Aspect Ratio:** `16:9` (Mobile) to `21:9` (Desktop Wide Ultrawide)
* **CSS Display Size:**
  * Width: Full viewport width `100vw`
  * Height: Clamped between `480px` (mobile minimum) and `640px` (desktop maximum)
  * CSS Rule: `height: clamp(480px, 45vw, 640px); object-fit: cover;`
* **Recommended Upload Dimensions:**
  * **Desktop:** `1920 × 800 px` (Standard HD) or `2400 × 1000 px` (4K/Retina displays)
  * **Mobile Alternate (Optional):** `1080 × 1080 px` or `1080 × 1200 px` if using responsive `<picture>` tags
* **File Format:** Progressive WebP or compressed JPG (82% quality)
* **Max File Size:** `250 KB` per slide
* **Art Direction:**
  * Warm, tactile lifestyle flatlays (open journals, warm espresso cup, brass ruler, pens, linen textures).
  * Keep focal points near the center so edges crop cleanly on diverse laptop and ultrawide screens.
  * Avoid placing hardcoded text inside the banner image.

---

### 3. Shop by Category Strip (`#category-section`, `.categories-strip-wrapper`)

* **Aspect Ratio:** `1 : 1.34` (approximately `3:4` vertical portrait pill)
* **CSS Display Size:**
  * Desktop: `155 px` width × `208 px` height
  * Mobile: `125 px` width × `168 px` height (horizontal scrolling track)
  * CSS Rule: `aspect-ratio: 1 / 1.34; object-fit: cover; border-radius: 14px;`
* **Recommended Upload Dimensions:** `600 × 800 px`
* **File Format:** WebP or JPG
* **Max File Size:** `80 KB` each
* **Art Direction:**
  * Close-up lifestyle imagery with rich editorial depth.
  * Dark gradient overlay (`rgba(0,0,0,0.35)`) is applied via CSS at the bottom to ensure category text remains legible.

---

### 4. Product Cards Across All Grid Sections
*(New Launch `#new-launch-section`, Bestsellers `#bestsellers-section`, Built with Heart `#built-with-heart-section`, Catalogue `#catalogue-section`)*

* **Container Aspect Ratio:** `4:5` (Vertical Portrait)
* **CSS Display Size:**
  * Grid Container: 4 columns on desktop, 2 columns on mobile.
  * Card Thumbnail Wrap: `240px–280px` width × `250px` height.
  * CSS Rule: `aspect-ratio: 4 / 5; object-fit: contain; background: #F8F6F0;`
* **Recommended Upload Dimensions:**
  * **Option A (4:5 Ratio - Recommended):** `1000 × 1250 px`
  * **Option B (1:1 Square - High Flexibility):** `1200 × 1200 px`
* **File Format:** WebP or JPG (white/warm ivory background) or transparent PNG
* **Max File Size:** `120 KB` per product
* **Art Direction:**
  * Keep product centered with `8–10%` internal whitespace padding so borders don't touch card edges.
  * Consistent soft warm shadow beneath product to create tactile elevation.
  * Product background matches Warm Paper (`#F8F5ED` or `#F8F6F0`).

---

### 5. Stories in Motion / Shoppable Video Reels (`#stories-in-motion`)

#### A. Vertical Video Files (`.reel-media-wrap video`)
* **Aspect Ratio:** `9:16` (Instagram Reel / TikTok vertical format)
* **CSS Display Size:** Width `290 px` × Height `515 px` (scroll-snap carousel)
* **Recommended Resolution:** `1080 × 1920 px` (Full HD)
* **Video Encoding:** MP4 container, H.264 video codec, AAC audio, 30 fps
* **Max Video File Size:** `< 8 MB` (ideally 3–5 MB for instant streaming on mobile 4G/5G)

#### B. Video Poster / Fallback Image (`.reel-cover-img`)
* **Aspect Ratio:** `9:16`
* **Recommended Upload Dimensions:** `1080 × 1920 px`
* **File Format:** WebP or JPG
* **Max File Size:** `150 KB`

#### C. Floating Product Pill Thumbnail (`.reel-prod-img`)
* **Aspect Ratio:** `1:1` (Square)
* **CSS Display Size:** `42 × 42 px` (Circle or rounded square)
* **Recommended Upload Dimensions:** `200 × 200 px`
* **File Format:** WebP / PNG
* **Max File Size:** `25 KB`

#### D. Creator Studio Avatar (`.creator-avatar`)
* **Aspect Ratio:** `1:1`
* **CSS Display Size:** `38 × 38 px` (Circle)
* **Recommended Upload Dimensions:** `150 × 150 px`
* **File Format:** PNG / WebP

---

### 6. Founder & Studio Craft Story (`#about-us`)

* **Aspect Ratio:** `4:5` or `3:4` (Vertical Editorial Portrait)
* **CSS Display Size:** Width `100%` of column (~`480 px`) × Height `480 px` (`object-fit: cover;`)
* **Recommended Upload Dimensions:** `1200 × 1500 px`
* **File Format:** WebP or JPG
* **Max File Size:** `200 KB`
* **Art Direction:**
  * Warm ambient studio lighting, hands holding bookbinding needle, cutting linen, or sketching with fountain pen.
  * Surrounded by a 6px clean white border and tactile drop shadow (`box-shadow: 0 10px 30px rgba(77, 53, 29, 0.08)`).

---

### 7. Client Proof & Customer Reviews (`#reviews-section`)

* **Aspect Ratio:** `1:1` (Circle Avatar)
* **CSS Display Size:** `44 × 44 px`
* **Recommended Upload Dimensions:** `180 × 180 px`
* **File Format:** WebP or JPG
* **Max File Size:** `25 KB`
* **Art Direction:** Friendly customer portraits, warm color tone, or initial monograms.

---

### 8. Artisanal Footer Illustrations (`.site-footer`)

#### A. Corner Foliage Vines (`.footer-corner-vine`)
* **Aspect Ratio:** `~3:2`
* **CSS Display Size:** `240 px` width × `160 px` height
* **Recommended Upload Dimensions:** `600 × 400 px`
* **File Format:** PNG with clean transparent alpha background
* **Max File Size:** `60 KB`

#### B. Handcrafted Desk Scene Illustration (`.footer-desk-illustration-img`)
* **Aspect Ratio:** `~3.5:1` (Ultra-wide horizontal panoramic illustration)
* **CSS Display Size:** Max width `900 px` × Height `240 px`
* **Recommended Upload Dimensions:** `1800 × 500 px`
* **File Format:** 24-bit PNG with transparent alpha background
* **Max File Size:** `180 KB`
* **Art Direction:** Warm hand-drawn ink & watercolor lineart of an artist desk with sleeping cat, coffee cup, journals, and botanical sprigs.

#### C. Bottom Border Flourishes (`.footer-bottom-flourish`)
* **Aspect Ratio:** `~2:1`
* **CSS Display Size:** `180 px` width × `90 px` height
* **Recommended Upload Dimensions:** `400 × 200 px`
* **File Format:** Transparent PNG
* **Max File Size:** `30 KB`

---

### 9. Interactive Modals

#### A. Quick View / Product Lightbox Modal (`#modal-img`)
* **Aspect Ratio:** `1:1` (Square)
* **CSS Display Size:** `450 × 450 px`
* **Recommended Upload Dimensions:** `1200 × 1200 px` (allows pinch-to-zoom without pixelation)
* **File Format:** WebP or JPG
* **Max File Size:** `180 KB`

#### B. Fullscreen Video Reel Viewer Modal (`#story-video`)
* **Aspect Ratio:** `9:16`
* **CSS Display Size:** Up to `420 × 746 px`
* **Recommended Video Resolution:** `1080 × 1920 px`
* **Format:** MP4 (H.264, 30fps)
* **Max File Size:** `< 8 MB`

---

## Performance & Optimization Guidelines

1. **Modern Format Priority:** Always deliver in **WebP** with fallback to JPG/PNG. WebP yields 30–35% smaller file sizes at identical visual fidelity.
2. **Color Profile:** Ensure all exported assets use the standard **sRGB** color space to maintain exact brand color fidelity across mobile OLED and desktop screens.
3. **Lazy Loading:** All images below the fold must include `loading="lazy"` to preserve sub-second First Contentful Paint (FCP).
4. **Compression Target:** Compress JPG/WebP at **80%–84% quality**. This achieves imperceptible loss with maximal file size reduction.
