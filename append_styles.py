styles_addon = """
/* ==========================================================================
   15. UI/UX PRO MAX — LIQUID GLASS & INTERACTIVE CATALOGUE SUITE
   ========================================================================== */

/* Keyboard hint in header */
.kbd-hint {
  font-size: 0.65rem;
  background: rgba(43, 37, 35, 0.08);
  border: 1px solid rgba(43, 37, 35, 0.12);
  border-radius: 4px;
  padding: 2px 5px;
  margin-left: 6px;
  font-family: inherit;
  font-weight: 600;
  color: var(--c-espresso);
  display: inline-block;
  vertical-align: middle;
}

/* Category Filter Pills & Counts */
.filter-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-bottom: 16px;
}

.pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: var(--r-full);
  border: 1px solid rgba(43, 37, 35, 0.12);
  background: var(--c-white);
  color: var(--c-espresso);
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.25s var(--ease-smooth);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
}

.pill-btn:hover {
  border-color: var(--c-tan);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(200, 157, 102, 0.12);
}

.pill-btn.active {
  background: var(--c-espresso);
  color: var(--c-cream);
  border-color: var(--c-espresso);
  box-shadow: 0 6px 16px rgba(43, 37, 35, 0.2);
}

.pill-count {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: 10px;
  background: rgba(43, 37, 35, 0.08);
  color: inherit;
  transition: background 0.2s;
}

.pill-btn.active .pill-count {
  background: rgba(255, 255, 255, 0.2);
  color: var(--c-cream);
}

/* Subcategory Chips */
.subcat-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-bottom: 28px;
}

.subcat-chip {
  padding: 6px 14px;
  border-radius: var(--r-full);
  border: 1px dashed rgba(43, 37, 35, 0.18);
  background: rgba(248, 246, 240, 0.8);
  color: var(--c-text-muted);
  font-size: 0.8rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s var(--ease-smooth);
}

.subcat-chip:hover {
  border-color: var(--c-tan);
  color: var(--c-espresso);
  background: var(--c-white);
}

.subcat-chip.active {
  background: var(--c-tan);
  color: var(--c-white);
  border-color: var(--c-tan);
  border-style: solid;
  box-shadow: 0 2px 8px rgba(200, 157, 102, 0.25);
}

/* Catalogue Toolbar */
.catalog-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  padding: 16px 20px;
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(43, 37, 35, 0.08);
  border-radius: var(--r-md);
  margin-bottom: 32px;
  box-shadow: 0 4px 16px rgba(43, 37, 35, 0.03);
}

.toolbar-left {
  display: flex;
  align-items: center;
  gap: 16px;
  flex: 1;
  min-width: 280px;
}

.catalog-search-bar {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 440px;
}

.catalog-search-bar svg {
  position: absolute;
  left: 14px;
  color: var(--c-text-light);
  pointer-events: none;
}

.catalog-search-bar input {
  width: 100%;
  padding: 10px 38px 10px 42px;
  background: var(--c-white);
  border: 1px solid rgba(43, 37, 35, 0.14);
  border-radius: var(--r-full);
  font-size: 0.875rem;
  color: var(--c-espresso);
  transition: all 0.2s;
}

.catalog-search-bar input:focus {
  outline: none;
  border-color: var(--c-tan);
  box-shadow: 0 0 0 3px rgba(200, 157, 102, 0.15);
}

#catalog-search-clear {
  position: absolute;
  right: 12px;
  background: none;
  border: none;
  color: var(--c-text-light);
  font-size: 1.2rem;
  cursor: pointer;
  line-height: 1;
}

.catalog-count-badge {
  font-size: 0.8rem;
  color: var(--c-text-muted);
  white-space: nowrap;
}

.toolbar-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.sort-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.sort-label {
  font-size: 0.8rem;
  color: var(--c-text-muted);
  white-space: nowrap;
}

.sort-select {
  padding: 8px 14px;
  background: var(--c-white);
  border: 1px solid rgba(43, 37, 35, 0.14);
  border-radius: var(--r-sm);
  font-size: 0.85rem;
  color: var(--c-espresso);
  cursor: pointer;
  font-weight: 500;
}

.sort-select:focus {
  outline: none;
  border-color: var(--c-tan);
}

.layout-switcher {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(43, 37, 35, 0.05);
  padding: 4px;
  border-radius: var(--r-sm);
}

.layout-btn {
  background: none;
  border: none;
  padding: 6px 8px;
  border-radius: 4px;
  color: var(--c-text-muted);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.layout-btn.active {
  background: var(--c-white);
  color: var(--c-espresso);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
}

/* Products Grid Variations */
.products-grid.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.products-grid.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

/* Wishlist Toggle Button on Cards */
.wishlist-toggle-btn {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(43, 37, 35, 0.08);
  color: var(--c-text-muted);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 3;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.wishlist-toggle-btn:hover {
  transform: scale(1.12);
  color: #D94652;
  box-shadow: 0 4px 12px rgba(217, 70, 82, 0.2);
}

.wishlist-toggle-btn.active {
  color: #D94652;
  background: #FFF0F2;
  border-color: rgba(217, 70, 82, 0.3);
  animation: heartPulse 0.4s ease-out;
}

@keyframes heartPulse {
  0% { transform: scale(0.85); }
  50% { transform: scale(1.25); }
  100% { transform: scale(1); }
}

/* Discount Pill */
.discount-pill {
  font-size: 0.7rem;
  font-weight: 700;
  color: #1F7A4D;
  background: #E8F5EE;
  padding: 2px 6px;
  border-radius: 4px;
  margin-left: 8px;
}

.product-info-top {
  display: flex;
  flex-direction: column;
}

.product-name {
  cursor: pointer;
  transition: color 0.2s;
}

.product-name:hover {
  color: var(--c-tan);
}

/* Empty State */
.catalog-empty-state {
  grid-column: 1 / -1;
  text-align: center;
  padding: 64px 20px;
  background: var(--c-white);
  border-radius: var(--r-md);
  border: 1px dashed rgba(43, 37, 35, 0.15);
}

.catalog-empty-state svg {
  color: var(--c-tan);
  margin-bottom: 16px;
}

.catalog-empty-state h3 {
  font-family: var(--font-display);
  font-size: 1.35rem;
  color: var(--c-espresso);
  margin-bottom: 8px;
}

.catalog-empty-state p {
  color: var(--c-text-muted);
  font-size: 0.9rem;
  margin-bottom: 20px;
}

/* ==========================================================================
   16. INSTANT SEARCH MODAL (CMD+K)
   ========================================================================== */
.search-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(43, 37, 35, 0.6);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 100px;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s var(--ease-smooth);
}

.search-modal-overlay.open {
  opacity: 1;
  visibility: visible;
}

.search-modal-dialog {
  background: var(--c-white);
  width: 90%;
  max-width: 640px;
  border-radius: var(--r-lg);
  overflow: hidden;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(43, 37, 35, 0.1);
  transform: translateY(-20px) scale(0.98);
  transition: transform 0.3s var(--ease-smooth);
}

.search-modal-overlay.open .search-modal-dialog {
  transform: translateY(0) scale(1);
}

.search-input-wrap {
  position: relative;
  display: flex;
  align-items: center;
  padding: 18px 24px;
  border-bottom: 1px solid rgba(43, 37, 35, 0.08);
}

.search-input-wrap .search-icon {
  color: var(--c-tan);
  margin-right: 14px;
  flex-shrink: 0;
}

.search-input-wrap input {
  flex: 1;
  border: none;
  background: none;
  font-size: 1.1rem;
  font-family: inherit;
  color: var(--c-espresso);
}

.search-input-wrap input:focus {
  outline: none;
}

.search-modal-close {
  background: none;
  border: none;
  color: var(--c-text-muted);
  cursor: pointer;
  padding: 4px;
}

.search-modal-results {
  max-height: 420px;
  overflow-y: auto;
  padding: 20px 24px;
}

.search-popular-tags {
  padding: 10px 0;
}

.search-tags-label {
  display: block;
  font-size: 0.78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--c-text-light);
  margin-bottom: 12px;
}

.tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag-chip {
  padding: 6px 14px;
  background: rgba(43, 37, 35, 0.04);
  border: 1px solid rgba(43, 37, 35, 0.08);
  border-radius: var(--r-full);
  font-size: 0.8rem;
  color: var(--c-espresso);
  cursor: pointer;
  transition: all 0.2s;
}

.tag-chip:hover {
  background: var(--c-tan);
  color: var(--c-white);
  border-color: var(--c-tan);
}

.search-results-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.search-result-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 10px 14px;
  border-radius: var(--r-md);
  cursor: pointer;
  transition: background 0.2s;
}

.search-result-item:hover {
  background: rgba(200, 157, 102, 0.08);
}

.search-result-thumb {
  width: 54px;
  height: 54px;
  object-fit: contain;
  background: #F8F6F0;
  border-radius: var(--r-sm);
  padding: 4px;
}

.search-result-cat {
  font-size: 0.72rem;
  color: var(--c-tan);
  font-weight: 600;
  display: block;
  text-transform: uppercase;
}

.search-result-name {
  font-size: 0.95rem;
  font-family: var(--font-display);
  color: var(--c-espresso);
  margin: 2px 0;
}

.search-result-price {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--c-espresso);
}

/* ==========================================================================
   17. WISHLIST SLIDE-OVER DRAWER
   ========================================================================== */
.wishlist-drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(43, 37, 35, 0.6);
  backdrop-filter: blur(6px);
  z-index: 1000;
  opacity: 0;
  visibility: hidden;
  transition: all 0.35s var(--ease-smooth);
}

.wishlist-drawer-overlay.open {
  opacity: 1;
  visibility: visible;
}

.wishlist-drawer {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  max-width: 440px;
  background: var(--c-white);
  box-shadow: -10px 0 40px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.35s var(--ease-smooth);
}

.wishlist-drawer-overlay.open .wishlist-drawer {
  transform: translateX(0);
}

.wishlist-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px;
  border-bottom: 1px solid rgba(43, 37, 35, 0.08);
}

.wishlist-title {
  font-family: var(--font-display);
  font-size: 1.35rem;
  color: var(--c-espresso);
  margin: 0;
}

.wishlist-count-label {
  font-size: 0.8rem;
  color: var(--c-text-muted);
}

.wishlist-items-list {
  flex: 1;
  overflow-y: auto;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.wishlist-item {
  display: flex;
  gap: 16px;
  padding: 12px;
  border-radius: var(--r-md);
  border: 1px solid rgba(43, 37, 35, 0.08);
  background: rgba(248, 246, 240, 0.4);
}

.wishlist-item-img {
  width: 72px;
  height: 90px;
  object-fit: contain;
  background: #F8F6F0;
  border-radius: var(--r-sm);
  padding: 6px;
}

.wishlist-item-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.wishlist-item-details .item-cat {
  font-size: 0.7rem;
  color: var(--c-tan);
  font-weight: 600;
  text-transform: uppercase;
}

.wishlist-item-details .item-name {
  font-size: 0.9rem;
  font-family: var(--font-display);
  color: var(--c-espresso);
  margin: 2px 0 6px;
  line-height: 1.3;
}

.wishlist-item-details .item-price {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--c-espresso);
}

.wishlist-item-details .item-mrp {
  font-size: 0.8rem;
  color: var(--c-text-light);
  text-decoration: line-through;
  margin-left: 6px;
}

.wishlist-actions-row {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

.btn-micro-bag {
  padding: 6px 12px;
  background: var(--c-espresso);
  color: var(--c-white);
  border: none;
  border-radius: var(--r-sm);
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-micro-bag:hover {
  background: var(--c-tan);
}

.btn-micro-remove {
  padding: 6px 10px;
  background: none;
  border: 1px solid rgba(43, 37, 35, 0.15);
  color: var(--c-text-muted);
  border-radius: var(--r-sm);
  font-size: 0.75rem;
  cursor: pointer;
}

.btn-micro-remove:hover {
  color: #D94652;
  border-color: #D94652;
}

/* ==========================================================================
   18. QUICK VIEW MODAL ENHANCEMENTS
   ========================================================================== */
.modal-actions-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-top: 24px;
}

.modal-qty-stepper {
  display: flex;
  align-items: center;
  background: rgba(43, 37, 35, 0.05);
  border-radius: var(--r-sm);
  padding: 4px;
}

.modal-qty-stepper .qty-btn {
  width: 36px;
  height: 36px;
  background: var(--c-white);
  border: none;
  border-radius: var(--r-sm);
  font-size: 1.1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.modal-qty-stepper .qty-btn:hover {
  background: var(--c-tan);
  color: var(--c-white);
}

.modal-qty-stepper .qty-val {
  padding: 0 16px;
  font-weight: 600;
  font-size: 1rem;
}

.modal-cart-cta {
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.bullet-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--c-tan);
  margin-right: 8px;
  vertical-align: middle;
}

/* ==========================================================================
   19. FLOATING CART PILL (LIQUID GLASS)
   ========================================================================== */
.floating-cart-pill {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 990;
  background: rgba(43, 37, 35, 0.92);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(200, 157, 102, 0.3);
  color: var(--c-cream);
  padding: 12px 20px;
  border-radius: var(--r-full);
  box-shadow: 0 8px 32px rgba(43, 37, 35, 0.35);
  cursor: pointer;
  opacity: 0;
  transform: translateY(20px) scale(0.9);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
}

.floating-cart-pill.visible {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.floating-cart-pill:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 12px 36px rgba(200, 157, 102, 0.4);
  background: var(--c-espresso);
}

.floating-pill-content {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  font-weight: 600;
}

.floating-count {
  background: var(--c-tan);
  color: var(--c-white);
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
}

.floating-divider {
  opacity: 0.4;
}

.floating-price {
  letter-spacing: 0.02em;
}

/* ==========================================================================
   20. RESPONSIVE EXTENSIONS
   ========================================================================== */
@media (max-width: 1200px) {
  .products-grid.grid-4 {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 860px) {
  .products-grid.grid-4,
  .products-grid.grid-3 {
    grid-template-columns: repeat(2, 1fr);
  }
  .catalog-toolbar {
    flex-direction: column;
    align-items: stretch;
  }
  .toolbar-left, .toolbar-right {
    width: 100%;
    justify-content: space-between;
  }
  .catalog-search-bar {
    max-width: none;
  }
}

@media (max-width: 540px) {
  .products-grid.grid-4,
  .products-grid.grid-3 {
    grid-template-columns: 1fr;
  }
  .filter-pills {
    justify-content: flex-start;
    overflow-x: auto;
    padding-bottom: 8px;
    flex-wrap: nowrap;
  }
  .subcat-pills {
    justify-content: flex-start;
    overflow-x: auto;
    padding-bottom: 8px;
    flex-wrap: nowrap;
  }
  .floating-cart-pill {
    bottom: 20px;
    right: 20px;
    padding: 10px 16px;
  }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(styles_addon)

print("Appended UI/UX Pro Max styles to styles.css successfully!")
