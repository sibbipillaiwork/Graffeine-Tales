# Add mobile drawer to index.html and update app.js & styles.css for full mobile responsiveness

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

mobile_drawer_markup = '''  <!-- =========================================================================
       13. DEDICATED MOBILE NAVIGATION DRAWER
       ========================================================================= -->
  <div class="mobile-drawer-overlay" id="mobile-drawer-overlay">
    <div class="mobile-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation">
      
      <div class="mobile-drawer-header">
        <a href="index.html" class="brand-logo-wrap" onclick="closeMobileDrawer()">
          <img src="assets/logo_dark.png" alt="Graffeine Tales" class="brand-logo-img" />
        </a>
        <button class="mobile-drawer-close" id="mobile-drawer-close" aria-label="Close navigation menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 6 6 18"/><path d="m6 6 12 12"/>
          </svg>
        </button>
      </div>

      <div class="mobile-drawer-body">
        
        <!-- Mobile Quick Search -->
        <div class="mobile-search-wrap">
          <button class="mobile-search-trigger" onclick="openSearchFromMobile()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
            </svg>
            <span>Search 41 handcrafted editions...</span>
          </button>
        </div>

        <!-- Featured Section Jump Links -->
        <div class="mobile-featured-links">
          <a href="#new-launch-section" class="mobile-nav-link highlight" onclick="closeMobileDrawer()">
            <span class="link-label">✨ New Launch Drop</span>
            <span class="mobile-pill-tag new">Fresh</span>
          </a>
          <a href="#bestsellers-section" class="mobile-nav-link highlight" onclick="closeMobileDrawer()">
            <span class="link-label">🔥 Community Bestsellers</span>
            <span class="mobile-pill-tag hot">Viral</span>
          </a>
        </div>

        <div class="mobile-nav-divider"></div>

        <!-- Category Links -->
        <div class="mobile-category-group">
          <span class="mobile-group-title">Shop by Category</span>
          <a href="#catalogue-section" class="mobile-nav-link" onclick="filterFromMobile('all')">
            <span>All Studio Editions</span>
            <span class="mobile-count-badge">41</span>
          </a>
          <a href="#catalogue-section" class="mobile-nav-link" onclick="filterFromMobile('stationaries')">
            <span>1. Stationaries &amp; Calendars</span>
            <span class="mobile-count-badge">16</span>
          </a>
          <a href="#catalogue-section" class="mobile-nav-link" onclick="filterFromMobile('journals')">
            <span>2. Journals &amp; Planners</span>
            <span class="mobile-count-badge">2</span>
          </a>
          <a href="#catalogue-section" class="mobile-nav-link" onclick="filterFromMobile('decor')">
            <span>3. Handcrafted Décor &amp; Coasters</span>
            <span class="mobile-count-badge">18</span>
          </a>
          <a href="#catalogue-section" class="mobile-nav-link" onclick="filterFromMobile('events')">
            <span>4. Events &amp; Personalized Gifting</span>
            <span class="mobile-count-badge">3</span>
          </a>
          <a href="#catalogue-section" class="mobile-nav-link" onclick="filterFromMobile('bulk')">
            <span>5. Bulk Orders &amp; Corporate</span>
            <span class="mobile-count-badge">2</span>
          </a>
        </div>

        <div class="mobile-nav-divider"></div>

        <!-- Studio & Story Links -->
        <div class="mobile-secondary-links">
          <a href="#gifting-section" class="mobile-nav-link" onclick="closeMobileDrawer()">
            <span>Corporate &amp; Wedding Services</span>
          </a>
          <a href="#founder-section" class="mobile-nav-link" onclick="closeMobileDrawer()">
            <span>Brand Story &amp; The 4 Pillars</span>
          </a>
          <a href="#reviews-section" class="mobile-nav-link" onclick="closeMobileDrawer()">
            <span>Client Reviews (2,400+)</span>
          </a>
          <a href="#newsletter" class="mobile-nav-link" onclick="closeMobileDrawer()">
            <span>Join The Society (10% Code)</span>
          </a>
        </div>

      </div>

      <div class="mobile-drawer-footer">
        <div class="mobile-meta-row">
          <span>Currency:</span>
          <select class="currency-select" aria-label="Currency Selector">
            <option>INR (₹)</option>
            <option>USD ($)</option>
            <option>GBP (£)</option>
          </select>
        </div>
        <p class="mobile-copyright">© 2026 Graffeine Tales Studio. All Rights Reserved.</p>
      </div>

    </div>
  </div>
'''

if '<!-- Script -->' in html:
    html = html.replace('<!-- Script -->', mobile_drawer_markup + '\n  <!-- Script -->')
    print("Added mobile drawer to index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
