mobile_css = """
/* ==========================================================================
   22. MOBILE NAVIGATION DRAWER & FULL MOBILE RESPONSIVENESS SYSTEM
   ========================================================================== */

/* Body scroll lock when drawers/modals are active */
body.no-scroll {
  overflow: hidden !important;
  touch-action: none;
}

/* Mobile Drawer Overlay */
.mobile-drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(43, 37, 35, 0.65);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 1100;
  opacity: 0;
  visibility: hidden;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.mobile-drawer-overlay.open {
  opacity: 1;
  visibility: visible;
}

/* Mobile Drawer Container */
.mobile-drawer {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 85%;
  max-width: 380px;
  background: var(--c-white);
  box-shadow: 10px 0 40px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  transform: translateX(-100%);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  overflow-y: auto;
}

.mobile-drawer-overlay.open .mobile-drawer {
  transform: translateX(0);
}

.mobile-drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 20px;
  border-bottom: 1px solid rgba(43, 37, 35, 0.08);
  background: rgba(248, 245, 237, 0.5);
}

.mobile-drawer-header .brand-logo-img {
  height: 38px;
}

.mobile-drawer-close {
  background: none;
  border: none;
  color: var(--c-espresso);
  cursor: pointer;
  padding: 6px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.mobile-drawer-close:hover {
  background: rgba(43, 37, 35, 0.08);
}

.mobile-drawer-body {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  overflow-y: auto;
}

/* Mobile Quick Search Button */
.mobile-search-wrap {
  margin-bottom: 4px;
}

.mobile-search-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: rgba(43, 37, 35, 0.04);
  border: 1px solid rgba(43, 37, 35, 0.1);
  border-radius: var(--r-full);
  color: var(--c-text-muted);
  font-size: 0.85rem;
  font-family: inherit;
  cursor: pointer;
  text-align: left;
}

.mobile-search-trigger svg {
  color: var(--c-tan);
  flex-shrink: 0;
}

/* Featured Links (New Launch / Bestsellers) */
.mobile-featured-links {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.mobile-nav-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 14px;
  border-radius: var(--r-sm);
  color: var(--c-espresso);
  font-size: 0.925rem;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.2s;
}

.mobile-nav-link:hover,
.mobile-nav-link:active {
  background: rgba(200, 157, 102, 0.1);
  color: var(--c-tan);
}

.mobile-nav-link.highlight {
  background: rgba(248, 245, 237, 0.7);
  font-weight: 600;
}

.mobile-pill-tag {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: var(--r-full);
  letter-spacing: 0.05em;
}

.mobile-pill-tag.new {
  background: #E8F5EE;
  color: #1F7A4D;
}

.mobile-pill-tag.hot {
  background: #FFF0F2;
  color: #D94652;
}

.mobile-nav-divider {
  height: 1px;
  background: rgba(43, 37, 35, 0.08);
  margin: 4px 0;
}

.mobile-group-title {
  display: block;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--c-text-light);
  padding: 0 14px 6px;
}

.mobile-count-badge {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: 10px;
  background: rgba(43, 37, 35, 0.08);
  color: var(--c-espresso);
}

.mobile-drawer-footer {
  padding: 18px 20px;
  border-top: 1px solid rgba(43, 37, 35, 0.08);
  background: rgba(248, 245, 237, 0.5);
}

.mobile-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
  font-size: 0.8rem;
  color: var(--c-text-muted);
}

.mobile-copyright {
  font-size: 0.7rem;
  color: var(--c-text-light);
  margin: 0;
}

/* ==========================================================================
   23. COMPREHENSIVE MOBILE BREAKPOINTS (UI/UX PRO MAX)
   ========================================================================== */

/* Tablets & Small Desktops (<= 1024px) */
@media (max-width: 1024px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .hero-visual {
    order: -1;
  }
  .hero-main-img {
    height: 380px;
  }
  .products-grid.grid-4 {
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }
  .gifting-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .founder-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
}

/* Mobile & Phablets (<= 768px) */
@media (max-width: 768px) {
  /* Prevent horizontal layout shifts */
  html, body {
    overflow-x: hidden;
    width: 100%;
  }

  .container {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }

  .section-padding {
    padding: 48px 0 !important;
  }

  .section-header {
    margin-bottom: 28px !important;
  }

  .section-title {
    font-size: 1.85rem !important;
    line-height: 1.25 !important;
  }

  .section-desc {
    font-size: 0.9rem !important;
  }

  /* Announcement Bar */
  .announcement-bar {
    padding: 7px 0;
    font-size: 0.75rem;
  }

  .announcement-inner {
    justify-content: center;
    text-align: center;
  }

  .announcement-meta {
    display: none;
  }

  /* Header */
  .site-header {
    height: 64px;
  }

  .nav-container {
    height: 64px;
  }

  .brand-logo-img {
    height: 36px !important;
  }

  .kbd-hint {
    display: none !important;
  }

  .nav-actions {
    gap: 4px;
  }

  .action-btn {
    width: 38px;
    height: 38px;
  }

  /* Mobile menu toggle */
  .nav-menu {
    display: none !important;
  }

  .mobile-toggle {
    display: flex !important;
  }

  /* Hero Section */
  .hero-section {
    padding: 24px 0 40px !important;
  }

  .hero-badge {
    margin-bottom: 16px;
    padding: 6px 12px;
  }

  .hero-title {
    font-size: 2.15rem !important;
    line-height: 1.18 !important;
    margin-bottom: 16px !important;
  }

  .hero-desc {
    font-size: 0.95rem !important;
    line-height: 1.5 !important;
    margin-bottom: 24px !important;
  }

  .hero-actions {
    flex-direction: column !important;
    gap: 12px !important;
    width: 100% !important;
    margin-bottom: 28px !important;
  }

  .hero-actions .btn {
    width: 100% !important;
    justify-content: center !important;
    height: 48px !important;
    font-size: 0.95rem !important;
  }

  .hero-trust-strip {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 10px !important;
  }

  .hero-image-card {
    height: 280px !important;
    border-radius: 16px !important;
  }

  .hero-floating-pill {
    bottom: 12px !important;
    left: 12px !important;
    right: 12px !important;
    max-width: calc(100% - 24px) !important;
    padding: 10px 14px !important;
  }

  /* Shop by Category Grid */
  .categories-grid {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
  }

  .cat-1, .cat-2, .cat-3, .cat-4, .cat-5 {
    grid-column: span 12 !important;
    min-height: 260px !important;
  }

  .cat-content {
    padding: 20px !important;
  }

  .cat-title {
    font-size: 1.35rem !important;
  }

  /* Filter Pills Swipeable Carousel */
  .filter-pills {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scroll-snap-type: x mandatory !important;
    scrollbar-width: none !important;
    padding: 4px 16px 12px !important;
    margin: 0 -16px 28px !important;
    gap: 8px !important;
    justify-content: flex-start !important;
  }

  .filter-pills::-webkit-scrollbar {
    display: none;
  }

  .pill-btn {
    flex-shrink: 0 !important;
    scroll-snap-align: start !important;
    padding: 8px 16px !important;
    font-size: 0.8rem !important;
  }

  /* Modern 2-Column Mobile Product Grid */
  .products-grid,
  .products-grid.grid-4,
  .products-grid.grid-3 {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
  }

  .product-card {
    border-radius: 12px !important;
    display: flex;
    flex-direction: column;
  }

  .product-thumb-wrap {
    aspect-ratio: 1 / 1.15 !important;
    padding: 8px !important;
    border-radius: 12px 12px 0 0 !important;
  }

  .product-badge {
    top: 8px !important;
    left: 8px !important;
    font-size: 0.62rem !important;
    padding: 2px 6px !important;
  }

  .wishlist-toggle-btn {
    top: 8px !important;
    right: 8px !important;
    width: 30px !important;
    height: 30px !important;
  }

  .wishlist-toggle-btn svg {
    width: 15px !important;
    height: 15px !important;
  }

  .quick-actions {
    display: none !important; /* Touch-optimized: click card to quick view */
  }

  .product-details {
    padding: 10px !important;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .product-cat {
    font-size: 0.62rem !important;
    line-height: 1.2 !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    margin-bottom: 2px !important;
  }

  .product-name {
    font-size: 0.82rem !important;
    line-height: 1.25 !important;
    min-height: 2.5em !important;
    display: -webkit-box !important;
    -webkit-line-clamp: 2 !important;
    -webkit-box-orient: vertical !important;
    overflow: hidden !important;
    margin-bottom: 4px !important;
  }

  .product-rating {
    margin-bottom: 4px !important;
  }

  .stars svg {
    width: 10px !important;
    height: 10px !important;
  }

  .rating-count {
    font-size: 0.7rem !important;
  }

  .product-pricing {
    margin-bottom: 8px !important;
    flex-wrap: wrap;
    gap: 4px;
  }

  .price-current {
    font-size: 0.95rem !important;
  }

  .price-original {
    font-size: 0.75rem !important;
  }

  .discount-pill {
    font-size: 0.62rem !important;
    padding: 1px 4px !important;
    margin-left: 0 !important;
  }

  .add-cart-btn {
    padding: 8px 10px !important;
    font-size: 0.78rem !important;
    border-radius: 8px !important;
    width: 100% !important;
    justify-content: center !important;
    gap: 6px !important;
  }

  .add-cart-btn svg {
    width: 14px !important;
    height: 14px !important;
  }

  /* Gifting Spotlight */
  .gifting-tabs {
    flex-direction: column !important;
    width: 100% !important;
  }

  .g-tab-btn {
    width: 100% !important;
    text-align: center !important;
  }

  .gifting-card {
    height: 280px !important;
  }

  /* Founder Pillars 2x2 on Mobile */
  .founder-pillars {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
  }

  .pillar-card {
    padding: 16px 12px !important;
  }

  .pillar-card h4 {
    font-size: 0.9rem !important;
  }

  .pillar-card p {
    font-size: 0.78rem !important;
  }

  /* Reviews Grid */
  .reviews-grid {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
  }

  /* Newsletter Card */
  .newsletter-card {
    padding: 32px 18px !important;
  }

  .newsletter-title {
    font-size: 1.6rem !important;
  }

  .newsletter-form {
    flex-direction: column !important;
    width: 100% !important;
    gap: 10px !important;
  }

  .newsletter-input,
  .newsletter-btn {
    width: 100% !important;
    height: 48px !important;
  }

  /* Footer */
  .footer-top {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }

  .footer-bottom {
    flex-direction: column !important;
    gap: 16px !important;
    text-align: center !important;
  }

  .payment-methods {
    justify-content: center !important;
    flex-wrap: wrap !important;
  }

  /* Drawers: 100% width on Mobile */
  .cart-drawer,
  .wishlist-drawer {
    width: 100% !important;
    max-width: 100% !important;
  }

  /* Search Modal on Mobile */
  .search-modal-overlay {
    padding-top: 16px !important;
    align-items: flex-start !important;
  }

  .search-modal-dialog {
    width: 95% !important;
    max-height: 85vh !important;
    border-radius: 16px !important;
  }

  .search-input-wrap input {
    font-size: 16px !important; /* Prevents iOS auto-zoom */
  }

  /* Quick View Modal on Mobile */
  .modal-overlay {
    padding: 16px !important;
    align-items: center !important;
  }

  .modal-content {
    grid-template-columns: 1fr !important;
    width: 100% !important;
    max-width: 480px !important;
    max-height: 90vh !important;
    overflow-y: auto !important;
    padding: 18px !important;
    gap: 16px !important;
  }

  .modal-image-col {
    max-height: 260px !important;
  }

  .modal-image-col img {
    max-height: 240px !important;
    object-fit: contain !important;
  }

  .modal-title {
    font-size: 1.25rem !important;
  }

  /* Floating Cart Pill on Mobile */
  .floating-cart-pill {
    bottom: 18px !important;
    right: 16px !important;
    padding: 10px 16px !important;
    font-size: 0.85rem !important;
  }
}

/* Extra Small Phones (<= 360px, e.g. iPhone SE / Mini) */
@media (max-width: 360px) {
  .products-grid,
  .products-grid.grid-4,
  .products-grid.grid-3 {
    grid-template-columns: 1fr !important;
  }

  .founder-pillars {
    grid-template-columns: 1fr !important;
  }

  .hero-title {
    font-size: 1.85rem !important;
  }

  .brand-logo-img {
    height: 32px !important;
  }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(mobile_css)

print("Appended comprehensive mobile responsive stylesheet to styles.css!")
