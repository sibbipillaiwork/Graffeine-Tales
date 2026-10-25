import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header Nav Actions
old_nav_actions = '''      <!-- Nav Icons (Search, Wishlist, Cart Drawer) -->
      <div class="nav-actions">
        <!-- Search Trigger -->
        <button class="action-btn" id="search-trigger" aria-label="Search collection">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
          </svg>
        </button>

        <!-- Wishlist -->
        <a href="#bestsellers" class="action-btn" aria-label="Wishlist items">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
          </svg>
        </a>

        <!-- Cart Trigger (Opens Slide-over Drawer) -->
        <button class="action-btn" id="cart-trigger" aria-label="Open shopping bag">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
            <path d="M3 6h18"/>
            <path d="M16 10a4 4 0 0 1-8 0"/>
          </svg>
          <span class="action-badge" id="cart-badge-count">1</span>
        </button>'''

new_nav_actions = '''      <!-- Nav Icons (Search Modal, Wishlist Drawer, Cart Drawer) -->
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
        </button>'''

if old_nav_actions in html:
    html = html.replace(old_nav_actions, new_nav_actions)
    print("Replaced nav actions successfully!")
else:
    print("Warning: old nav actions block not matched exactly, checking regex...")

# 2. Replace the entire Bestsellers Section (from <section class="section-padding bestsellers-section" id="bestsellers"> down to </section>)
catalog_section_pattern = re.compile(
    r'<section class="section-padding bestsellers-section" id="bestsellers">.*?</section>',
    re.DOTALL
)

new_catalog_section = '''<section class="section-padding bestsellers-section" id="bestsellers">
      <div class="container">
        
        <header class="section-header">
          <span class="section-tag">Authentic Studio Catalogue</span>
          <h2 class="section-title">The Complete Atelier Collection</h2>
          <p class="section-desc">
            Explore all handcrafted editions across our 5 signature categories: Stationaries, Journals, Handcrafted Décor, Events &amp; Gifting, and Bulk Orders.
          </p>
        </header>

        <!-- Dynamic Category Filter Pills with Live Count -->
        <div class="filter-pills" id="catalog-filter-pills">
          <!-- Rendered dynamically by app.js with live product counts -->
        </div>

        <!-- Quick Subcategory Chips -->
        <div class="subcat-pills" id="catalog-subcat-pills">
          <!-- Rendered dynamically by app.js based on selected category -->
        </div>

        <!-- Catalog Toolbar: Live Search, Sort, View Toggle, Count -->
        <div class="catalog-toolbar">
          <div class="toolbar-left">
            <div class="catalog-search-bar">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
              </svg>
              <input type="text" id="catalog-search-input" placeholder="Search across all 41 products, coasters, calendars, thread art..." aria-label="Search catalogue" />
              <button id="catalog-search-clear" style="display: none;" aria-label="Clear search">×</button>
            </div>
            <span class="catalog-count-badge" id="catalog-count-badge">Showing 41 handcrafted atelier editions</span>
          </div>

          <div class="toolbar-right">
            <!-- Sort dropdown -->
            <div class="sort-wrap">
              <label for="catalog-sort-select" class="sort-label">Sort by:</label>
              <select id="catalog-sort-select" class="sort-select" aria-label="Sort products">
                <option value="featured">Featured Atelier Drops</option>
                <option value="price-asc">Price: Low to High</option>
                <option value="price-desc">Price: High to Low</option>
                <option value="rating">Top Rated &amp; Reviewed</option>
                <option value="bestseller">Most Popular</option>
              </select>
            </div>

            <!-- Layout switcher -->
            <div class="layout-switcher">
              <button class="layout-btn active" data-layout="grid-4" title="4 Columns Grid">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <rect x="2" y="2" width="4" height="20" rx="1"/>
                  <rect x="8" y="2" width="4" height="20" rx="1"/>
                  <rect x="14" y="2" width="4" height="20" rx="1"/>
                  <rect x="20" y="2" width="4" height="20" rx="1"/>
                </svg>
              </button>
              <button class="layout-btn" data-layout="grid-3" title="3 Columns Editorial">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <rect x="2" y="2" width="5.5" height="20" rx="1"/>
                  <rect x="9.25" y="2" width="5.5" height="20" rx="1"/>
                  <rect x="16.5" y="2" width="5.5" height="20" rx="1"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Dynamic Product Cards Grid -->
        <div class="products-grid grid-4" id="products-grid">
          <!-- Dynamically populated by app.js with full 41 products -->
        </div>

      </div>
    </section>'''

if catalog_section_pattern.search(html):
    html = catalog_section_pattern.sub(new_catalog_section, html)
    print("Replaced catalog section successfully!")
else:
    print("Error: Could not match catalog section pattern.")

# 3. Add Search Modal and Wishlist Drawer before the Quick View Modal
modals_addition = '''  <!-- =========================================================================
       11.5 INSTANT SEARCH MODAL (CMD+K / SEARCH BUTTON)
       ========================================================================= -->
  <div class="search-modal-overlay" id="search-modal-overlay">
    <div class="search-modal-dialog" role="dialog" aria-modal="true" aria-label="Search studio catalogue">
      <div class="search-input-wrap">
        <svg class="search-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
        </svg>
        <input type="text" id="search-modal-input" placeholder="Type to search desk calendars, acrylic coasters, bookmarks..." autocomplete="off" />
        <button class="search-modal-close" id="search-modal-close" aria-label="Close search">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
        </button>
      </div>
      <div class="search-modal-results" id="search-modal-results">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </div>

  <!-- =========================================================================
       11.6 WISHLIST SLIDE-OVER DRAWER
       ========================================================================= -->
  <div class="wishlist-drawer-overlay" id="wishlist-drawer-overlay">
    <div class="wishlist-drawer" role="dialog" aria-modal="true" aria-labelledby="wishlist-title">
      <div class="wishlist-header">
        <div>
          <h3 class="wishlist-title" id="wishlist-title">Saved Treasures</h3>
          <span class="wishlist-count-label" id="wishlist-count-label">2 Saved Editions</span>
        </div>
        <button class="close-btn" id="wishlist-close-btn" aria-label="Close wishlist">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
        </button>
      </div>
      <div class="wishlist-items-list" id="wishlist-items-list">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </div>
'''

if '<!-- =========================================================================\n       12. QUICK VIEW MODAL' in html:
    html = html.replace(
        '<!-- =========================================================================\n       12. QUICK VIEW MODAL',
        modals_addition + '\n  <!-- =========================================================================\n       12. QUICK VIEW MODAL'
    )
    print("Added Search Modal and Wishlist Drawer!")
else:
    print("Warning: Quick View Modal anchor not found.")

# 4. Enhance Quick View Modal with Quantity Stepper
old_quick_view_inner = '''        <div class="modal-specs">
          <ul id="modal-specs-list">
            <!-- Dynamic specs -->
          </ul>
        </div>

        <button class="btn btn-primary" id="modal-add-cart" style="width: 100%;">
          Add to Atelier Bag
        </button>'''

new_quick_view_inner = '''        <div class="modal-specs">
          <span class="specs-title">Edition Specifications:</span>
          <ul id="modal-specs-list">
            <!-- Dynamic specs -->
          </ul>
        </div>

        <!-- Quantity Stepper & Add to Bag Row -->
        <div class="modal-actions-row">
          <div class="modal-qty-stepper">
            <button class="qty-btn" onclick="adjustQuickViewQty(-1)" aria-label="Decrease quantity">−</button>
            <span class="qty-val" id="modal-qty-val">1</span>
            <button class="qty-btn" onclick="adjustQuickViewQty(1)" aria-label="Increase quantity">+</button>
          </div>
          <button class="btn btn-primary modal-cart-cta" id="modal-add-cart">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            Add to Atelier Bag
          </button>
        </div>'''

if old_quick_view_inner in html:
    html = html.replace(old_quick_view_inner, new_quick_view_inner)
    print("Enhanced Quick View Modal with quantity stepper!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
