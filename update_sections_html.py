import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Announcement bar links
announcement_old = '<a href="#gifting-section">Custom &amp; Bulk Gifting Open</a>\n        <span>•</span>\n        <a href="#founder-section">Our Atelier Story</a>'
announcement_new = '<a href="#new-launch-section">✨ New Launch</a>\n        <span>•</span>\n        <a href="#bestsellers-section">🔥 Bestsellers</a>\n        <span>•</span>\n        <a href="#catalogue-section">Full Catalogue</a>\n        <span>•</span>\n        <a href="#gifting-section">Custom Gifting</a>'

if announcement_old in html:
    html = html.replace(announcement_old, announcement_new)
    print("Updated announcement bar links!")

# 2. Update Hero buttons
hero_btn_old = 'href="#bestsellers"'
hero_btn_new = 'href="#catalogue-section"'
html = html.replace(hero_btn_old, hero_btn_new)

# 3. Replace the existing catalog section with New Launch, Bestsellers, and Clean Category-only Catalogue
catalog_pattern = re.compile(
    r'<section class="section-padding bestsellers-section" id="bestsellers">.*?</section>',
    re.DOTALL
)

new_sections = '''<!-- =========================================================================
         5. NEW LAUNCH SECTION
         Fresh Studio Drops & 2026 Calendars
         ========================================================================= -->
    <section class="section-padding new-launch-section" id="new-launch-section">
      <div class="container">
        
        <header class="section-header">
          <span class="section-tag">Fresh From Atelier</span>
          <h2 class="section-title">New Launch</h2>
          <p class="section-desc">
            Discover our latest seasonal creations — from interactive 2026 desk companion calendars to mindful guided journals and celestial hoop art.
          </p>
        </header>

        <!-- New Launch Products Grid -->
        <div class="products-grid grid-3" id="new-launch-grid">
          <!-- Rendered dynamically by app.js -->
        </div>

      </div>
    </section>

    <!-- =========================================================================
         6. BESTSELLERS SECTION
         Most Loved Editions & Community Favorites
         ========================================================================= -->
    <section class="section-padding bestsellers-section" id="bestsellers-section">
      <div class="container">
        
        <header class="section-header">
          <span class="section-tag">Most Loved</span>
          <h2 class="section-title">Bestsellers</h2>
          <p class="section-desc">
            Artisanal editions and community favorites that have brought warmth, humor, and elegance to over 2,400+ homes and desks.
          </p>
        </header>

        <!-- Bestsellers Products Grid -->
        <div class="products-grid grid-4" id="bestsellers-grid">
          <!-- Rendered dynamically by app.js -->
        </div>

      </div>
    </section>

    <!-- =========================================================================
         7. THE COMPLETE ATELIER COLLECTION (CATALOGUE)
         Category-Only Filtered Grid (No Subcategories)
         ========================================================================= -->
    <section class="section-padding catalogue-section" id="catalogue-section">
      <div class="container">
        
        <header class="section-header">
          <span class="section-tag">Full Studio Archive</span>
          <h2 class="section-title">The Complete Atelier Collection</h2>
          <p class="section-desc">
            Explore all handcrafted editions across our 5 signature categories: Stationaries, Journals, Handcrafted Décor, Events &amp; Gifting, and Bulk Orders.
          </p>
        </header>

        <!-- Dynamic Category Filter Pills with Live Count (ONLY CATEGORIES) -->
        <div class="filter-pills" id="catalog-filter-pills">
          <!-- Rendered dynamically by app.js with live product counts -->
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

if catalog_pattern.search(html):
    html = catalog_pattern.sub(new_sections, html)
    print("Replaced with New Launch, Bestsellers, and Category-only Catalogue!")
else:
    print("Error: Could not match catalog pattern!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
