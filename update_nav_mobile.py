import re

# 1. Update index.html Header & Add Bottom Nav
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Header Nav Container to position mobile-toggle on the left
old_header_inner = '''    <div class="container nav-container">
      
      <!-- Brand Logo -->
      <a href="index.html" class="brand-logo-wrap" aria-label="Graffeine Tales Home">
        <img src="assets/logo_dark.png" alt="Graffeine Tales - Where Stories Become Art" class="brand-logo-img" />
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="site-nav" aria-label="Main menu">'''

new_header_inner = '''    <div class="container nav-container">
      
      <!-- Mobile Menu Toggle (Left Aligned on Mobile) -->
      <button class="action-btn mobile-toggle" id="mobile-hamburger-btn" aria-label="Toggle navigation menu">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>
        </svg>
      </button>

      <!-- Brand Logo (Center on Mobile, Left on Desktop) -->
      <a href="index.html" class="brand-logo-wrap" aria-label="Graffeine Tales Home">
        <img src="assets/logo_dark.png" alt="Graffeine Tales - Where Stories Become Art" class="brand-logo-img" />
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="site-nav" aria-label="Main menu">'''

if old_header_inner in html:
    html = html.replace(old_header_inner, new_header_inner)
    print("Updated header left/center layout in index.html!")
else:
    print("Warning: old_header_inner not found directly")

# Update top nav actions: mark Wishlist as desktop-only and remove duplicate mobile-toggle
old_nav_actions = '''      <!-- Nav Icons (Search Modal, Wishlist Drawer, Cart Drawer) -->
      <div class="nav-actions">
        <!-- Search Trigger (Opens Instant Search Modal) -->
        <button class="action-btn" id="header-search-trigger" aria-label="Search collection" title="Search catalogue (Ctrl+K)">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
          </svg>
          <span class="kbd-hint">⌘K</span>
        </button>

        <!-- Wishlist Trigger (Opens Saved Items Drawer) -->
        <button class="action-btn" id="wishlist-trigger" aria-label="Wishlist items" title="Saved Wishlist">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
          </svg>
          <span class="action-badge" id="wishlist-badge-count">2</span>
        </button>

        <!-- Cart Trigger (Opens Slide-over Drawer) -->
        <button class="action-btn" id="cart-trigger" aria-label="Open shopping bag" title="Atelier Shopping Bag">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
            <path d="M3 6h18"/>
            <path d="M16 10a4 4 0 0 1-8 0"/>
          </svg>
          <span class="action-badge" id="cart-badge-count">1</span>
        </button>

        <!-- Mobile Menu Toggle -->
        <button class="action-btn mobile-toggle" aria-label="Toggle navigation menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>
          </svg>
        </button>
      </div>'''

new_nav_actions = '''      <!-- Nav Icons (Desktop: Search, Wishlist, Cart; Mobile: Search & Cart Right Aligned) -->
      <div class="nav-actions">
        <!-- Search Trigger (Opens Instant Search Modal) -->
        <button class="action-btn" id="header-search-trigger" aria-label="Search collection" title="Search catalogue (Ctrl+K)">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
          </svg>
          <span class="kbd-hint">⌘K</span>
        </button>

        <!-- Wishlist Trigger (Desktop Only - Mobile has it in Bottom Nav) -->
        <button class="action-btn desktop-only-action" id="wishlist-trigger" aria-label="Wishlist items" title="Saved Wishlist">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
          </svg>
          <span class="action-badge" id="wishlist-badge-count">2</span>
        </button>

        <!-- Cart Trigger (Opens Slide-over Drawer) -->
        <button class="action-btn" id="cart-trigger" aria-label="Open shopping bag" title="Atelier Shopping Bag">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
            <path d="M3 6h18"/>
            <path d="M16 10a4 4 0 0 1-8 0"/>
          </svg>
          <span class="action-badge" id="cart-badge-count">1</span>
        </button>
      </div>'''

if old_nav_actions in html:
    html = html.replace(old_nav_actions, new_nav_actions)
    print("Updated top nav actions in index.html!")

# Add Mobile Bottom Navigation Bar right before </body>
bottom_nav_markup = '''  <!-- =========================================================================
       14. MOBILE BOTTOM GLASSMORPHISM NAVIGATION BAR
       Home, Categories, Wishlist, Cart
       ========================================================================= -->
  <nav class="mobile-bottom-nav" aria-label="Mobile Navigation Bar">
    
    <!-- 1. Home -->
    <a href="#hero" class="bottom-nav-item active" id="bnav-home">
      <div class="bottom-nav-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
          <polyline points="9 22 9 12 15 12 15 22"/>
        </svg>
      </div>
      <span class="bottom-nav-label">Home</span>
    </a>

    <!-- 2. Categories -->
    <a href="#category-section" class="bottom-nav-item" id="bnav-categories">
      <div class="bottom-nav-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect width="7" height="7" x="3" y="3" rx="1"/>
          <rect width="7" height="7" x="14" y="3" rx="1"/>
          <rect width="7" height="7" x="14" y="14" rx="1"/>
          <rect width="7" height="7" x="3" y="14" rx="1"/>
        </svg>
      </div>
      <span class="bottom-nav-label">Categories</span>
    </a>

    <!-- 3. Wishlist (Opens Wishlist Drawer) -->
    <button class="bottom-nav-item" id="bnav-wishlist" aria-label="Open Saved Wishlist">
      <div class="bottom-nav-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
        </svg>
        <span class="bottom-badge" id="bottom-wishlist-count">2</span>
      </div>
      <span class="bottom-nav-label">Wishlist</span>
    </button>

    <!-- 4. Cart (Opens Cart Drawer) -->
    <button class="bottom-nav-item" id="bnav-cart" aria-label="Open Atelier Bag">
      <div class="bottom-nav-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
          <path d="M3 6h18"/>
          <path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
        <span class="bottom-badge" id="bottom-cart-count">1</span>
      </div>
      <span class="bottom-nav-label">Cart</span>
    </button>

  </nav>
'''

if '</main>' in html and 'mobile-bottom-nav' not in html:
    html = html.replace('</body>', bottom_nav_markup + '\n</body>')
    print("Added mobile-bottom-nav to index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
