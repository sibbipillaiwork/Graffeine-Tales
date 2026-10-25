# Update app.js and styles.css for the new mobile navigation system

# 1. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update updateWishlistUI to update bottom badge as well
old_wishlist_ui = """function updateWishlistUI() {
  const badge = document.querySelector('#wishlist-badge-count');
  if (badge) {
    badge.textContent = wishlist.length;
    badge.style.display = wishlist.length > 0 ? 'inline-flex' : 'none';
  }
}"""

new_wishlist_ui = """function updateWishlistUI() {
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
}"""

if old_wishlist_ui in js:
    js = js.replace(old_wishlist_ui, new_wishlist_ui)
    print("Updated updateWishlistUI in app.js!")

# Update renderCart to update bottom cart badge as well
old_cart_badge = """  if (cartBadge) {
    cartBadge.textContent = totalCount;
    cartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
  }"""

new_cart_badge = """  if (cartBadge) {
    cartBadge.textContent = totalCount;
    cartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
  }
  const bottomCartBadge = document.querySelector('#bottom-cart-count');
  if (bottomCartBadge) {
    bottomCartBadge.textContent = totalCount;
    bottomCartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
  }"""

if old_cart_badge in js:
    js = js.replace(old_cart_badge, new_cart_badge)
    print("Updated renderCart badges in app.js!")

# Add initMobileBottomNav call inside DOMContentLoaded
if 'initMobileBottomNav();' not in js:
    js = js.replace("initFloatingCartPill();", "initFloatingCartPill();\n  initMobileBottomNav();")
    print("Added initMobileBottomNav() to DOMContentLoaded!")

# Add initMobileBottomNav function definition
bottom_nav_js = """
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
"""

if 'initMobileBottomNav()' in js and 'function initMobileBottomNav()' not in js:
    js += bottom_nav_js
    print("Appended initMobileBottomNav function to app.js!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")

# 2. Append Glassmorphism styles to styles.css
glassmorphism_nav_css = """
/* ==========================================================================
   24. MOBILE GLASSMORPHISM NAVIGATION (TOP BAR & BOTTOM NAV BAR)
   ========================================================================== */

/* Top Header Glassmorphism */
.site-header {
  background-color: rgba(248, 245, 237, 0.82) !important;
  backdrop-filter: blur(18px) saturate(160%) !important;
  -webkit-backdrop-filter: blur(18px) saturate(160%) !important;
  border-bottom: 1px solid rgba(200, 157, 102, 0.22) !important;
  box-shadow: 0 4px 20px rgba(43, 37, 35, 0.04) !important;
}

/* Mobile Top Nav Layout: Hamburger Left, Logo Center, Search & Cart Right */
@media (max-width: 900px) {
  .nav-container {
    display: grid !important;
    grid-template-columns: 44px 1fr auto !important;
    align-items: center !important;
    height: 64px !important;
    padding: 0 16px !important;
    gap: 8px !important;
  }

  /* Hamburger to the left */
  .mobile-toggle {
    display: flex !important;
    grid-column: 1 !important;
    justify-self: start !important;
    background: rgba(255, 255, 255, 0.65) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(200, 157, 102, 0.25) !important;
    border-radius: 10px !important;
    width: 40px !important;
    height: 40px !important;
    align-items: center !important;
    justify-content: center !important;
    color: var(--c-espresso) !important;
    box-shadow: 0 2px 8px rgba(43, 37, 35, 0.04) !important;
  }

  /* Logo perfectly center aligned */
  .brand-logo-wrap {
    grid-column: 2 !important;
    justify-self: center !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin: 0 auto !important;
  }

  .brand-logo-img {
    height: 36px !important;
    max-width: 160px !important;
    object-fit: contain !important;
  }

  /* Search & Cart right aligned */
  .nav-actions {
    grid-column: 3 !important;
    display: flex !important;
    justify-self: end !important;
    align-items: center !important;
    gap: 8px !important;
  }

  .nav-actions .action-btn {
    background: rgba(255, 255, 255, 0.65) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(200, 157, 102, 0.25) !important;
    border-radius: 10px !important;
    width: 40px !important;
    height: 40px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 2px 8px rgba(43, 37, 35, 0.04) !important;
  }

  /* Hide Wishlist in top nav on mobile (it's in the bottom nav) */
  .desktop-only-action {
    display: none !important;
  }
}

/* Mobile Bottom Navigation Bar (Glassmorphism) */
.mobile-bottom-nav {
  display: none;
}

@media (max-width: 900px) {
  .mobile-bottom-nav {
    display: flex !important;
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    height: calc(64px + env(safe-area-inset-bottom, 0px)) !important;
    padding-bottom: env(safe-area-inset-bottom, 0px) !important;
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(24px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
    border-top: 1px solid rgba(200, 157, 102, 0.25) !important;
    box-shadow: 0 -8px 32px rgba(43, 37, 35, 0.08) !important;
    z-index: 1000 !important;
    justify-content: space-around !important;
    align-items: center !important;
  }

  /* Push body up so content isn't covered by bottom nav */
  body {
    padding-bottom: calc(74px + env(safe-area-inset-bottom, 0px)) !important;
  }

  /* Hide floating cart pill on mobile since bottom nav already has Cart */
  .floating-cart-pill {
    display: none !important;
  }

  .bottom-nav-item {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 3px !important;
    flex: 1 !important;
    height: 100% !important;
    background: none !important;
    border: none !important;
    color: var(--c-text-muted) !important;
    text-decoration: none !important;
    cursor: pointer !important;
    position: relative !important;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
    padding: 8px 0 !important;
    -webkit-tap-highlight-color: transparent !important;
  }

  .bottom-nav-item:active {
    transform: scale(0.92) !important;
  }

  .bottom-nav-item.active {
    color: var(--c-tan) !important;
  }

  .bottom-nav-item.active .bottom-nav-label {
    color: var(--c-espresso) !important;
    font-weight: 700 !important;
  }

  .bottom-nav-icon {
    position: relative !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 28px !important;
    height: 28px !important;
  }

  .bottom-nav-label {
    font-size: 0.68rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em !important;
    transition: color 0.2s !important;
  }

  .bottom-badge {
    position: absolute !important;
    top: -3px !important;
    right: -7px !important;
    background: var(--c-tan) !important;
    color: var(--c-white) !important;
    font-size: 0.62rem !important;
    font-weight: 700 !important;
    width: 17px !important;
    height: 17px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: 2px solid #FFFFFF !important;
    box-shadow: 0 2px 6px rgba(200, 157, 102, 0.4) !important;
  }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(glassmorphism_nav_css)

print("Appended mobile glassmorphism navigation styles to styles.css!")
