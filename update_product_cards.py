# Update app.js and styles.css for optimized product cards, brown Add to Cart button, and mobile carousel

# 1. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace button in renderProductCardHTML
old_btn_pattern = """        <button class="add-cart-btn" onclick="addToCart('${prod.id}')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
            <path d="M3 6h18"/>
            <path d="M16 10a4 4 0 0 1-8 0"/>
          </svg>
          Add to Bag
        </button>"""

new_btn_pattern = """        <button class="add-cart-btn" onclick="addToCart('${prod.id}')">
          Add to Cart
        </button>"""

if old_btn_pattern in js:
    js = js.replace(old_btn_pattern, new_btn_pattern)
    print("Replaced Add to Bag with Add to Cart (no icon) in renderProductCardHTML!")
else:
    print("Warning: old_btn_pattern not matched directly, checking regex...")

# Also update modal CTA if needed
js = js.replace('Add to Atelier Bag', 'Add to Cart')
js = js.replace('Add to Bag', 'Add to Cart')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")

# 2. Append Optimized Card and Carousel Styles to styles.css
card_and_carousel_css = """
/* ==========================================================================
   26. OPTIMIZED PRODUCT CARDS & MOBILE CAROUSEL ARCHITECTURE
   ========================================================================== */

/* Universal Add to Cart Button (Brown BG, Lighter Font, No Icon) */
.add-cart-btn {
  width: 100% !important;
  background-color: #4A3525 !important; /* Rich warm artisanal brown */
  color: #FAF7F2 !important;            /* Lighter warm cream font */
  border: none !important;
  padding: 12px 18px !important;
  border-radius: 8px !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.03em !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0 !important;
  cursor: pointer !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 2px 8px rgba(74, 53, 37, 0.2) !important;
  text-transform: none !important;
}

.add-cart-btn:hover {
  background-color: #38271C !important;
  color: #FFFFFF !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 4px 14px rgba(74, 53, 37, 0.35) !important;
}

.add-cart-btn:active {
  transform: scale(0.98) !important;
}

/* Hide any remaining icons inside add-cart-btn */
.add-cart-btn svg {
  display: none !important;
}

/* Desktop Optimized Product Cards (Increased Width & Fixed Height) */
@media (min-width: 769px) {
  .products-grid,
  .products-grid.grid-4 {
    display: grid !important;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)) !important;
    gap: 28px !important;
  }

  .products-grid.grid-3 {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 32px !important;
  }

  .product-card {
    height: 490px !important;
    max-height: 490px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    background: #FFFFFF !important;
    border-radius: 14px !important;
    border: 1px solid rgba(43, 37, 35, 0.08) !important;
    box-shadow: 0 4px 20px rgba(43, 37, 35, 0.04) !important;
    overflow: hidden !important;
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
  }

  .product-card:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 12px 32px rgba(43, 37, 35, 0.09) !important;
    border-color: rgba(200, 157, 102, 0.35) !important;
  }

  .product-thumb-wrap {
    height: 250px !important;
    min-height: 250px !important;
    max-height: 250px !important;
    flex-shrink: 0 !important;
    background-color: #F8F6F0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 14px !important;
    position: relative !important;
    overflow: hidden !important;
  }

  .product-thumb {
    max-width: 90% !important;
    max-height: 90% !important;
    object-fit: contain !important;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
  }

  .product-card:hover .product-thumb {
    transform: scale(1.04) !important;
  }

  .product-details {
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    padding: 16px 18px 18px !important;
  }

  .product-info-top {
    display: flex !important;
    flex-direction: column !important;
  }

  .product-cat {
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    color: var(--c-tan) !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    margin-bottom: 4px !important;
  }

  .product-name {
    font-size: 0.98rem !important;
    font-family: var(--font-display) !important;
    color: var(--c-espresso) !important;
    line-height: 1.35 !important;
    height: 2.7em !important;
    max-height: 2.7em !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    margin-bottom: 8px !important;
    cursor: pointer !important;
  }

  .product-rating {
    display: flex !important;
    align-items: center !important;
    gap: 6px !important;
    margin-bottom: 8px !important;
  }

  .stars svg {
    width: 12px !important;
    height: 12px !important;
    fill: var(--c-tan) !important;
  }

  .product-pricing {
    display: flex !important;
    align-items: baseline !important;
    gap: 8px !important;
    margin-bottom: 12px !important;
  }

  .price-current {
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    color: var(--c-espresso) !important;
  }

  .price-original {
    font-size: 0.85rem !important;
    color: var(--c-text-light) !important;
    text-decoration: line-through !important;
  }

  .discount-pill {
    font-size: 0.7rem !important;
    font-weight: 700 !important;
    color: #1F7A4D !important;
    background: #E8F5EE !important;
    padding: 2px 6px !important;
    border-radius: 4px !important;
  }
}

/* ==========================================================================
   MOBILE HORIZONTAL SWIPEABLE CAROUSEL (NOT STACKED, INCREASED WIDTH, FIXED HEIGHT)
   ========================================================================== */
@media (max-width: 768px) {
  /* All product sections become horizontal carousels on mobile */
  .products-grid,
  .products-grid.grid-4,
  .products-grid.grid-3,
  #new-launch-grid,
  #bestsellers-grid,
  #products-grid {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scroll-snap-type: x mandatory !important;
    gap: 16px !important;
    padding: 10px 16px 24px !important;
    margin-left: -16px !important;
    margin-right: -16px !important;
    scrollbar-width: none !important; /* Hide scrollbar Firefox */
  }

  .products-grid::-webkit-scrollbar,
  #new-launch-grid::-webkit-scrollbar,
  #bestsellers-grid::-webkit-scrollbar,
  #products-grid::-webkit-scrollbar {
    display: none !important; /* Hide scrollbar WebKit */
  }

  /* Optimized Wider Cards with Fixed Height */
  .product-card {
    /* Increased width for readability */
    width: 275px !important;
    min-width: 275px !important;
    max-width: 275px !important;
    /* Fixed height so cards never flow or mismatch */
    height: 480px !important;
    min-height: 480px !important;
    max-height: 480px !important;
    flex-shrink: 0 !important;
    scroll-snap-align: start !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    background: #FFFFFF !important;
    border-radius: 16px !important;
    border: 1px solid rgba(43, 37, 35, 0.08) !important;
    box-shadow: 0 4px 18px rgba(43, 37, 35, 0.05) !important;
    overflow: hidden !important;
  }

  /* Product Image Thumbnail Wrap */
  .product-thumb-wrap {
    height: 240px !important;
    min-height: 240px !important;
    max-height: 240px !important;
    flex-shrink: 0 !important;
    aspect-ratio: unset !important;
    background: #F8F6F0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 14px !important;
    position: relative !important;
    overflow: hidden !important;
  }

  .product-thumb {
    max-width: 90% !important;
    max-height: 90% !important;
    object-fit: contain !important;
  }

  /* Product Details with Fixed Proportions */
  .product-details {
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    padding: 14px 14px 16px !important;
  }

  .product-info-top {
    display: flex !important;
    flex-direction: column !important;
  }

  .product-cat {
    font-size: 0.68rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    color: var(--c-tan) !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    margin-bottom: 4px !important;
  }

  .product-name {
    font-size: 0.92rem !important;
    font-family: var(--font-display) !important;
    color: var(--c-espresso) !important;
    line-height: 1.35 !important;
    height: 2.7em !important;
    max-height: 2.7em !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    margin-bottom: 6px !important;
  }

  .product-rating {
    display: flex !important;
    align-items: center !important;
    gap: 4px !important;
    margin-bottom: 6px !important;
  }

  .stars svg {
    width: 11px !important;
    height: 11px !important;
    fill: var(--c-tan) !important;
  }

  .rating-count {
    font-size: 0.72rem !important;
    color: var(--c-text-muted) !important;
  }

  .product-pricing {
    display: flex !important;
    align-items: baseline !important;
    gap: 6px !important;
    margin-bottom: 10px !important;
  }

  .price-current {
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    color: var(--c-espresso) !important;
  }

  .price-original {
    font-size: 0.8rem !important;
    color: var(--c-text-light) !important;
    text-decoration: line-through !important;
  }

  .discount-pill {
    font-size: 0.65rem !important;
    font-weight: 700 !important;
    color: #1F7A4D !important;
    background: #E8F5EE !important;
    padding: 1px 5px !important;
    border-radius: 4px !important;
  }

  /* Mobile Brown Add to Cart Button (Clean, No Icon) */
  .add-cart-btn {
    width: 100% !important;
    height: 44px !important;
    background-color: #4A3525 !important; /* Brown */
    color: #FAF7F2 !important;            /* Lighter warm cream font */
    border: none !important;
    border-radius: 8px !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important;
    box-shadow: 0 2px 8px rgba(74, 53, 37, 0.25) !important;
  }

  .add-cart-btn:active {
    background-color: #38271C !important;
    transform: scale(0.98) !important;
  }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(card_and_carousel_css)

print("Appended optimized card, brown Add to Cart, and mobile carousel styles to styles.css!")
