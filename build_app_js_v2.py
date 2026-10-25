import json

with open('products_data.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

products_json_str = json.dumps(products, indent=2, ensure_ascii=False)

app_js_content = f"""/**
 * GRAFFEINE TALES — D2C SHOPIFY LUXURY COMMERCE SUITE
 * High-Fidelity Interactive Architecture
 * Enhanced with UI/UX Pro Max Design Intelligence
 */

const productsData = {products_json_str};

// State
let cart = JSON.parse(localStorage.getItem('gtb_cart') || 'null') || [
  {{
    id: 'prod-1',
    name: 'Lady TeaTrip Acrylic Coaster & Teak Stand',
    price: 699,
    image: 'assets/products/lady_teatrip.jpg',
    qty: 1
  }}
];

let wishlist = JSON.parse(localStorage.getItem('gtb_wishlist') || 'null') || ['prod-1', 'prod-2'];

let currentFilter = 'all';
let currentSort = 'featured';
let currentSearch = '';
let currentLayout = 'grid-4';

const FREE_SHIPPING_THRESHOLD = 1499;

// Init
document.addEventListener('DOMContentLoaded', () => {{
  initFeaturedSections();
  initCatalog();
  initHeader();
  initCart();
  initWishlist();
  initQuickView();
  initSearch();
  initGiftingTabs();
  initNewsletter();
  initFloatingCartPill();
  updateWishlistUI();
}});

// 1. Featured Sections: New Launch & Bestsellers
function initFeaturedSections() {{
  renderNewLaunchSection();
  renderBestsellersSection();
}}

function renderProductCardHTML(prod) {{
  const isWishlisted = wishlist.includes(prod.id);
  const discount = prod.mrp ? Math.round(((prod.mrp - prod.price) / prod.mrp) * 100) : 0;

  return `
    <article class="product-card" data-id="${{prod.id}}" data-category="${{prod.category}}">
      <div class="product-thumb-wrap">
        <img src="${{prod.image}}" alt="${{prod.name}}" class="product-thumb" loading="lazy" />
        
        <!-- Badge -->
        <span class="product-badge ${{prod.badgeType || 'gold'}}">${{prod.badge || 'Atelier'}}</span>
        
        <!-- Wishlist Toggle Button -->
        <button class="wishlist-toggle-btn ${{isWishlisted ? 'active' : ''}}" onclick="toggleWishlist('${{prod.id}}', event)" aria-label="Save to wishlist" title="Save to wishlist">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="${{isWishlisted ? 'currentColor' : 'none'}}" stroke="currentColor" stroke-width="2">
            <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
          </svg>
        </button>

        <!-- Quick Actions Bar -->
        <div class="quick-actions">
          <button class="quick-btn" onclick="openQuickView('${{prod.id}}'); event.stopPropagation();">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/>
              <circle cx="12" cy="12" r="3"/>
            </svg>
            Quick View
          </button>
        </div>
      </div>

      <div class="product-details">
        <div class="product-info-top">
          <span class="product-cat">${{prod.category}}</span>
          <h3 class="product-name" onclick="openQuickView('${{prod.id}}')">${{prod.name}}</h3>
          
          <div class="product-rating">
            <div class="stars">
              ${{renderStars(prod.rating)}}
            </div>
            <span class="rating-count">(${{prod.reviews}})</span>
          </div>

          <div class="product-pricing">
            <span class="price-current">₹${{prod.price.toLocaleString('en-IN')}}</span>
            ${{prod.mrp ? `<span class="price-original">₹${{prod.mrp.toLocaleString('en-IN')}}</span>` : ''}}
            ${{discount > 0 ? `<span class="discount-pill">${{discount}}% OFF</span>` : ''}}
          </div>
        </div>

        <button class="add-cart-btn" onclick="addToCart('${{prod.id}}')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
            <path d="M3 6h18"/>
            <path d="M16 10a4 4 0 0 1-8 0"/>
          </svg>
          Add to Bag
        </button>
      </div>
    </article>
  `;
}}

function renderNewLaunchSection() {{
  const grid = document.querySelector('#new-launch-grid');
  if (!grid) return;
  const newItems = productsData.filter(p => p.isNewLaunch);
  grid.innerHTML = newItems.map(renderProductCardHTML).join('');
}}

function renderBestsellersSection() {{
  const grid = document.querySelector('#bestsellers-grid');
  if (!grid) return;
  const bestsellers = productsData.filter(p => p.isBestseller);
  grid.innerHTML = bestsellers.map(renderProductCardHTML).join('');
}}

// 2. Catalog Engine (ONLY CATEGORIES, NO SUBCATEGORIES)
function initCatalog() {{
  renderCategoryPills();
  renderCatalog();

  // Search input in catalog toolbar
  const searchInput = document.querySelector('#catalog-search-input');
  const clearBtn = document.querySelector('#catalog-search-clear');
  if (searchInput) {{
    searchInput.addEventListener('input', (e) => {{
      currentSearch = e.target.value.trim().toLowerCase();
      if (clearBtn) clearBtn.style.display = currentSearch ? 'block' : 'none';
      renderCatalog();
    }});
  }}
  if (clearBtn && searchInput) {{
    clearBtn.addEventListener('click', () => {{
      searchInput.value = '';
      currentSearch = '';
      clearBtn.style.display = 'none';
      renderCatalog();
    }});
  }}

  // Sort dropdown
  const sortSelect = document.querySelector('#catalog-sort-select');
  if (sortSelect) {{
    sortSelect.addEventListener('change', (e) => {{
      currentSort = e.target.value;
      renderCatalog();
    }});
  }}

  // Layout switcher
  const layoutBtns = document.querySelectorAll('.layout-btn');
  layoutBtns.forEach(btn => {{
    btn.addEventListener('click', () => {{
      layoutBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentLayout = btn.dataset.layout;
      const grid = document.querySelector('#products-grid');
      if (grid) {{
        grid.className = `products-grid ${{currentLayout}}`;
      }}
    }});
  }});
}}

function renderCategoryPills() {{
  // Accurate counts using clean categoryGroup
  const counts = {{
    all: productsData.length,
    stationaries: productsData.filter(p => p.categoryGroup === 'stationaries').length,
    journals: productsData.filter(p => p.categoryGroup === 'journals').length,
    decor: productsData.filter(p => p.categoryGroup === 'decor').length,
    events: productsData.filter(p => p.categoryGroup === 'events').length,
    bulk: productsData.filter(p => p.categoryGroup === 'bulk').length,
  }};

  const pillsContainer = document.querySelector('#catalog-filter-pills');
  if (!pillsContainer) return;

  const categories = [
    {{ id: 'all', label: 'All Editions', count: counts.all }},
    {{ id: 'stationaries', label: '1. Stationaries', count: counts.stationaries }},
    {{ id: 'journals', label: '2. Journals', count: counts.journals }},
    {{ id: 'decor', label: '3. Handcrafted Décor', count: counts.decor }},
    {{ id: 'events', label: '4. Events & Gifting', count: counts.events }},
    {{ id: 'bulk', label: '5. Bulk Orders', count: counts.bulk }}
  ];

  pillsContainer.innerHTML = categories.map(cat => `
    <button class="pill-btn ${{currentFilter === cat.id ? 'active' : ''}}" data-cat="${{cat.id}}">
      <span>${{cat.label}}</span>
      <span class="pill-count">${{cat.count}}</span>
    </button>
  `).join('');

  pillsContainer.querySelectorAll('.pill-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      pillsContainer.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.dataset.cat;
      renderCatalog();
    }});
  }});
}}

function getFilteredProducts() {{
  return productsData.filter(p => {{
    // 1. Category Filter (Only Categories)
    if (currentFilter !== 'all') {{
      if (p.categoryGroup !== currentFilter) return false;
    }}

    // 2. Search Query
    if (currentSearch) {{
      const q = currentSearch;
      const searchable = (p.name + ' ' + p.category + ' ' + p.desc + ' ' + (p.specs || []).join(' ')).toLowerCase();
      if (!searchable.includes(q)) return false;
    }}

    return true;
  }}).sort((a, b) => {{
    if (currentSort === 'price-asc') return a.price - b.price;
    if (currentSort === 'price-desc') return b.price - a.price;
    if (currentSort === 'rating') return b.rating - a.rating || b.reviews - a.reviews;
    if (currentSort === 'bestseller') return b.reviews - a.reviews;
    return 0; // Default featured order
  }});
}}

function renderCatalog() {{
  const grid = document.querySelector('#products-grid');
  const countBadge = document.querySelector('#catalog-count-badge');
  if (!grid) return;

  const filtered = getFilteredProducts();

  if (countBadge) {{
    countBadge.textContent = `Showing ${{filtered.length}} of ${{productsData.length}} handcrafted atelier editions`;
  }}

  if (filtered.length === 0) {{
    grid.innerHTML = `
      <div class="catalog-empty-state">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="11" cy="11" r="8"/>
          <path d="m21 21-4.3-4.3"/>
        </svg>
        <h3>No matching editions found</h3>
        <p>Try clearing your search query or selecting another category.</p>
        <button class="btn btn-outline" onclick="resetFilters()">Reset All Filters</button>
      </div>
    `;
    return;
  }}

  grid.innerHTML = filtered.map(renderProductCardHTML).join('');
}}

function renderStars(rating) {{
  const fullStar = '<svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>';
  return Array(5).fill(fullStar).join('');
}}

function resetFilters() {{
  currentFilter = 'all';
  currentSearch = '';
  currentSort = 'featured';

  const searchInput = document.querySelector('#catalog-search-input');
  if (searchInput) searchInput.value = '';
  const clearBtn = document.querySelector('#catalog-search-clear');
  if (clearBtn) clearBtn.style.display = 'none';

  renderCategoryPills();
  renderCatalog();
}}

// 3. Wishlist Management
function initWishlist() {{
  const wishlistTrigger = document.querySelector('#wishlist-trigger');
  const wishlistDrawer = document.querySelector('#wishlist-drawer-overlay');
  const wishlistClose = document.querySelector('#wishlist-close-btn');

  if (wishlistTrigger && wishlistDrawer) {{
    wishlistTrigger.addEventListener('click', (e) => {{
      e.preventDefault();
      wishlistDrawer.classList.add('open');
      renderWishlistDrawer();
    }});
  }}

  if (wishlistClose && wishlistDrawer) {{
    wishlistClose.addEventListener('click', () => wishlistDrawer.classList.remove('open'));
    wishlistDrawer.addEventListener('click', (e) => {{
      if (e.target === wishlistDrawer) wishlistDrawer.classList.remove('open');
    }});
  }}
}}

function toggleWishlist(prodId, event) {{
  if (event) event.stopPropagation();
  const prod = productsData.find(p => p.id === prodId);
  if (!prod) return;

  const idx = wishlist.indexOf(prodId);
  if (idx > -1) {{
    wishlist.splice(idx, 1);
    showToast(`Removed "${{prod.name}}" from your wishlist`);
  }} else {{
    wishlist.push(prodId);
    showToast(`Saved "${{prod.name}}" to your wishlist ❤️`);
  }}

  localStorage.setItem('gtb_wishlist', JSON.stringify(wishlist));
  updateWishlistUI();
  renderNewLaunchSection();
  renderBestsellersSection();
  renderCatalog();
  renderWishlistDrawer();
}}

function updateWishlistUI() {{
  const badge = document.querySelector('#wishlist-badge-count');
  if (badge) {{
    badge.textContent = wishlist.length;
    badge.style.display = wishlist.length > 0 ? 'inline-flex' : 'none';
  }}
}}

function renderWishlistDrawer() {{
  const list = document.querySelector('#wishlist-items-list');
  const countLabel = document.querySelector('#wishlist-count-label');
  if (!list) return;

  if (countLabel) {{
    countLabel.textContent = `${{wishlist.length}} Saved Editions`;
  }}

  if (wishlist.length === 0) {{
    list.innerHTML = `
      <div class="empty-drawer-state">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
        </svg>
        <p class="empty-title">Your Wishlist is Empty</p>
        <p class="empty-sub">Tap the heart on any product to curate your personal collection.</p>
      </div>
    `;
    return;
  }}

  const items = wishlist.map(id => productsData.find(p => p.id === id)).filter(Boolean);

  list.innerHTML = items.map(item => `
    <div class="wishlist-item">
      <img src="${{item.image}}" alt="${{item.name}}" class="wishlist-item-img" />
      <div class="wishlist-item-details">
        <span class="item-cat">${{item.category}}</span>
        <h4 class="item-name">${{item.name}}</h4>
        <div class="item-price-wrap">
          <span class="item-price">₹${{item.price.toLocaleString('en-IN')}}</span>
          ${{item.mrp ? `<span class="item-mrp">₹${{item.mrp.toLocaleString('en-IN')}}</span>` : ''}}
        </div>
        <div class="wishlist-actions-row">
          <button class="btn-micro-bag" onclick="addToCart('${{item.id}}')">Add to Bag</button>
          <button class="btn-micro-remove" onclick="toggleWishlist('${{item.id}}', event)">Remove</button>
        </div>
      </div>
    </div>
  `).join('');
}}

// 4. Cart Operations
function initCart() {{
  const cartTrigger = document.querySelector('#cart-trigger');
  const cartDrawer = document.querySelector('#cart-drawer-overlay');
  const cartClose = document.querySelector('#cart-close-btn');

  if (cartTrigger && cartDrawer) {{
    cartTrigger.addEventListener('click', (e) => {{
      e.preventDefault();
      cartDrawer.classList.add('open');
      renderCart();
    }});
  }}

  if (cartClose && cartDrawer) {{
    cartClose.addEventListener('click', () => cartDrawer.classList.remove('open'));
    cartDrawer.addEventListener('click', (e) => {{
      if (e.target === cartDrawer) cartDrawer.classList.remove('open');
    }});
  }}

  renderCart();
}}

function addToCart(prodId, qty = 1) {{
  const item = productsData.find(p => p.id === prodId);
  if (!item) return;

  const existing = cart.find(i => i.id === prodId);
  if (existing) {{
    existing.qty += qty;
  }} else {{
    cart.push({{
      id: item.id,
      name: item.name,
      price: item.price,
      image: item.image,
      category: item.category,
      qty: qty
    }});
  }}

  localStorage.setItem('gtb_cart', JSON.stringify(cart));
  renderCart();
  updateFloatingCartPill();
  showToast(`Added "${{item.name}}" to your bag`);

  const cartDrawer = document.querySelector('#cart-drawer-overlay');
  if (cartDrawer) {{
    cartDrawer.classList.add('open');
  }}
}}

function updateCartQty(prodId, delta) {{
  const item = cart.find(i => i.id === prodId);
  if (!item) return;

  item.qty += delta;
  if (item.qty <= 0) {{
    cart = cart.filter(i => i.id !== prodId);
  }}

  localStorage.setItem('gtb_cart', JSON.stringify(cart));
  renderCart();
  updateFloatingCartPill();
}}

function renderCart() {{
  const cartList = document.querySelector('#cart-items-list');
  const cartBadge = document.querySelector('#cart-badge-count');
  const subtotalEl = document.querySelector('#cart-subtotal-val');
  const goalLabel = document.querySelector('#shipping-goal-label');
  const progressFill = document.querySelector('#shipping-progress-fill');

  const totalCount = cart.reduce((acc, curr) => acc + curr.qty, 0);
  const totalAmount = cart.reduce((acc, curr) => acc + (curr.price * curr.qty), 0);

  if (cartBadge) {{
    cartBadge.textContent = totalCount;
    cartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
  }}

  if (subtotalEl) {{
    subtotalEl.textContent = `₹${{totalAmount.toLocaleString('en-IN')}}`;
  }}

  // Update Free Shipping Progress (Threshold: ₹1,499)
  if (goalLabel && progressFill) {{
    if (totalAmount >= FREE_SHIPPING_THRESHOLD) {{
      goalLabel.innerHTML = '<span>✨ You unlocked <strong>FREE Studio Courier Shipping!</strong></span>';
      progressFill.style.width = '100%';
    }} else {{
      const remaining = FREE_SHIPPING_THRESHOLD - totalAmount;
      const pct = Math.min(100, Math.round((totalAmount / FREE_SHIPPING_THRESHOLD) * 100));
      goalLabel.innerHTML = `<span>Add <strong>₹${{remaining.toLocaleString('en-IN')}}</strong> more for <strong>FREE Shipping</strong></span><span>${{pct}}%</span>`;
      progressFill.style.width = `${{pct}}%`;
    }}
  }}

  if (!cartList) return;

  if (cart.length === 0) {{
    cartList.innerHTML = `
      <div class="empty-drawer-state">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
          <path d="M3 6h18"/>
          <path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
        <p class="empty-title">Your shopping bag is empty</p>
        <p class="empty-sub">Explore our actual acrylic coasters, calendars, and door hangers.</p>
        <button class="btn btn-primary" onclick="document.querySelector('#cart-drawer-overlay').classList.remove('open'); window.location.hash='catalogue-section';">Explore Catalogue</button>
      </div>
    `;
    return;
  }}

  cartList.innerHTML = cart.map(item => `
    <div class="cart-item">
      <img src="${{item.image}}" alt="${{item.name}}" class="cart-item-img" />
      <div class="cart-item-info">
        <h4 class="item-name">${{item.name}}</h4>
        <p class="item-variant">${{item.category || 'Atelier Original'}}</p>
        <div class="qty-control">
          <button class="qty-btn" onclick="updateCartQty('${{item.id}}', -1)" aria-label="Decrease">−</button>
          <span class="qty-val">${{item.qty}}</span>
          <button class="qty-btn" onclick="updateCartQty('${{item.id}}', 1)" aria-label="Increase">+</button>
        </div>
      </div>
      <div class="cart-item-actions">
        <span class="item-price">₹${{(item.price * item.qty).toLocaleString('en-IN')}}</span>
        <button class="remove-btn" onclick="updateCartQty('${{item.id}}', -999)" title="Remove item">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>
          </svg>
        </button>
      </div>
    </div>
  `).join('');
}}

// 5. Quick View Modal with Quantity Stepper
let quickViewQty = 1;
function initQuickView() {{
  const modal = document.querySelector('#quick-view-modal');
  const closeBtn = document.querySelector('#modal-close-btn');

  if (closeBtn && modal) {{
    closeBtn.addEventListener('click', () => modal.classList.remove('open'));
    modal.addEventListener('click', (e) => {{
      if (e.target === modal) modal.classList.remove('open');
    }});
  }}
}}

function openQuickView(prodId) {{
  const prod = productsData.find(p => p.id === prodId);
  if (!prod) return;

  quickViewQty = 1;
  const modal = document.querySelector('#quick-view-modal');
  const modalImg = document.querySelector('#modal-img');
  const modalTag = document.querySelector('#modal-tag');
  const modalTitle = document.querySelector('#modal-title');
  const modalPrice = document.querySelector('#modal-price');
  const modalDesc = document.querySelector('#modal-desc');
  const specsList = document.querySelector('#modal-specs-list');

  if (modalImg) modalImg.src = prod.image;
  if (modalTag) modalTag.textContent = prod.category;
  if (modalTitle) modalTitle.textContent = prod.name;
  if (modalPrice) {{
    modalPrice.innerHTML = `
      <span class="price-val">₹${{prod.price.toLocaleString('en-IN')}}</span>
      ${{prod.mrp ? `<span class="mrp-val">₹${{prod.mrp.toLocaleString('en-IN')}}</span>` : ''}}
      ${{prod.mrp ? `<span class="discount-tag">${{Math.round(((prod.mrp - prod.price) / prod.mrp) * 100)}}% OFF</span>` : ''}}
    `;
  }}
  if (modalDesc) modalDesc.textContent = prod.desc;

  if (specsList && prod.specs) {{
    specsList.innerHTML = prod.specs.map(s => `<li><span class="bullet-dot"></span>${{s}}</li>`).join('');
  }}

  // Quantity Stepper
  const qtyVal = document.querySelector('#modal-qty-val');
  if (qtyVal) qtyVal.textContent = quickViewQty;

  const modalAddBtn = document.querySelector('#modal-add-cart');
  if (modalAddBtn) {{
    modalAddBtn.onclick = () => {{
      addToCart(prod.id, quickViewQty);
      modal.classList.remove('open');
    }};
  }}

  modal.classList.add('open');
}}

function adjustQuickViewQty(delta) {{
  quickViewQty = Math.max(1, quickViewQty + delta);
  const qtyVal = document.querySelector('#modal-qty-val');
  if (qtyVal) qtyVal.textContent = quickViewQty;
}}

// 6. Global Search Modal (Cmd+K)
function initSearch() {{
  const searchTrigger = document.querySelector('#header-search-trigger');
  const searchModal = document.querySelector('#search-modal-overlay');
  const searchClose = document.querySelector('#search-modal-close');
  const searchInput = document.querySelector('#search-modal-input');
  const resultsContainer = document.querySelector('#search-modal-results');

  if (searchTrigger && searchModal) {{
    searchTrigger.addEventListener('click', (e) => {{
      e.preventDefault();
      searchModal.classList.add('open');
      if (searchInput) {{
        setTimeout(() => searchInput.focus(), 100);
      }}
    }});
  }}

  if (searchClose && searchModal) {{
    searchClose.addEventListener('click', () => searchModal.classList.remove('open'));
    searchModal.addEventListener('click', (e) => {{
      if (e.target === searchModal) searchModal.classList.remove('open');
    }});
  }}

  window.addEventListener('keydown', (e) => {{
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {{
      e.preventDefault();
      if (searchModal) {{
        searchModal.classList.toggle('open');
        if (searchModal.classList.contains('open') && searchInput) {{
          setTimeout(() => searchInput.focus(), 100);
        }}
      }}
    }}
    if (e.key === 'Escape' && searchModal && searchModal.classList.contains('open')) {{
      searchModal.classList.remove('open');
    }}
  }});

  if (searchInput && resultsContainer) {{
    searchInput.addEventListener('input', (e) => {{
      const query = e.target.value.trim().toLowerCase();
      if (!query) {{
        renderSearchTags(resultsContainer);
        return;
      }}

      const matches = productsData.filter(p => {{
        return (p.name + ' ' + p.category + ' ' + p.desc + ' ' + (p.specs || []).join(' ')).toLowerCase().includes(query);
      }}).slice(0, 6);

      if (matches.length === 0) {{
        resultsContainer.innerHTML = `
          <div class="search-empty">
            <p>No handcrafted editions matching "<strong>${{query}}</strong>"</p>
          </div>
        `;
        return;
      }}

      resultsContainer.innerHTML = `
        <div class="search-results-list">
          ${{matches.map(p => `
            <div class="search-result-item" onclick="openQuickView('${{p.id}}'); document.querySelector('#search-modal-overlay').classList.remove('open');">
              <img src="${{p.image}}" alt="${{p.name}}" class="search-result-thumb" />
              <div>
                <span class="search-result-cat">${{p.category}}</span>
                <h4 class="search-result-name">${{p.name}}</h4>
                <span class="search-result-price">₹${{p.price.toLocaleString('en-IN')}}</span>
              </div>
            </div>
          `).join('')}}
        </div>
      `;
    }});

    renderSearchTags(resultsContainer);
  }}
}}

function renderSearchTags(container) {{
  const tags = ['Desk Calendar', 'F1 Coaster', 'Chugli Over Chai', 'Magnetic Bookmark', 'Sunflower', 'Thread Art', 'Door Hanger', 'Linen Journal'];
  container.innerHTML = `
    <div class="search-popular-tags">
      <span class="search-tags-label">Popular Searches:</span>
      <div class="tags-row">
        ${{tags.map(t => `<button class="tag-chip" onclick="searchTag('${{t}}')">${{t}}</button>`).join('')}}
      </div>
    </div>
  `;
}}

function searchTag(tag) {{
  const searchInput = document.querySelector('#search-modal-input');
  if (searchInput) {{
    searchInput.value = tag;
    searchInput.dispatchEvent(new Event('input'));
  }}
}}

// 7. Floating Cart Pill
function initFloatingCartPill() {{
  let pill = document.querySelector('#floating-cart-pill');
  if (!pill) {{
    pill = document.createElement('div');
    pill.id = 'floating-cart-pill';
    pill.className = 'floating-cart-pill';
    pill.onclick = () => {{
      const drawer = document.querySelector('#cart-drawer-overlay');
      if (drawer) drawer.classList.add('open');
      renderCart();
    }};
    document.body.appendChild(pill);
  }}
  updateFloatingCartPill();
}}

function updateFloatingCartPill() {{
  const pill = document.querySelector('#floating-cart-pill');
  if (!pill) return;

  const totalCount = cart.reduce((acc, curr) => acc + curr.qty, 0);
  const totalAmount = cart.reduce((acc, curr) => acc + (curr.price * curr.qty), 0);

  if (totalCount > 0) {{
    pill.innerHTML = `
      <div class="floating-pill-content">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/>
          <path d="M3 6h18"/>
          <path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
        <span class="floating-count">${{totalCount}}</span>
        <span class="floating-divider">|</span>
        <span class="floating-price">₹${{totalAmount.toLocaleString('en-IN')}}</span>
      </div>
    `;
    pill.classList.add('visible');
  }} else {{
    pill.classList.remove('visible');
  }}
}}

// 8. Header Scroll and Mobile Nav
function initHeader() {{
  const header = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {{
    if (window.scrollY > 30) {{
      header.classList.add('scrolled');
    }} else {{
      header.classList.remove('scrolled');
    }}
  }});

  const toggleBtn = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  if (toggleBtn && navMenu) {{
    toggleBtn.addEventListener('click', () => {{
      navMenu.classList.toggle('mobile-open');
    }});
  }}
}}

// 9. Gifting Spotlight Tabs
function initGiftingTabs() {{
  const corporateTab = document.querySelector('#tab-corporate');
  const weddingTab = document.querySelector('#tab-wedding');
  const giftingImg = document.querySelector('#gifting-hero-img');
  const giftingTitle = document.querySelector('#gifting-title-text');
  const giftingDesc = document.querySelector('#gifting-desc-text');

  if (corporateTab && weddingTab) {{
    corporateTab.addEventListener('click', () => {{
      corporateTab.classList.add('active');
      weddingTab.classList.remove('active');
      giftingTitle.innerHTML = 'Corporate Keepsakes &amp; <em>Executive Swag</em>';
      giftingDesc.textContent = 'Thoughtfully branded onboarding kits, bespoke acrylic coasters, desk calendars with wooden easels, and curated festive hampers designed to leave an indelible impression on clients and teams.';
      if (giftingImg) giftingImg.src = 'assets/cat_bulk.jpg';
    }});

    weddingTab.addEventListener('click', () => {{
      weddingTab.classList.add('active');
      corporateTab.classList.remove('active');
      giftingTitle.innerHTML = 'Wedding Celebrations &amp; <em>Bespoke Favours</em>';
      giftingDesc.textContent = 'Custom illustrated acrylic coasters, wooden keepsake stands, personalized door plaques, and custom stationery suites crafted to celebrate your one-of-a-kind story.';
      if (giftingImg) giftingImg.src = 'assets/cat_events.jpg';
    }});
  }}
}}

// 10. Newsletter
function initNewsletter() {{
  const form = document.querySelector('#newsletter-form');
  if (form) {{
    form.addEventListener('submit', (e) => {{
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      if (input && input.value) {{
        showToast(`Welcome to the Society! 10% welcome coupon sent to ${{input.value}}`);
        input.value = '';
      }}
    }});
  }}
}}

// 11. Toast Notification
function showToast(message) {{
  let container = document.querySelector('.toast-container');
  if (!container) {{
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }}

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `
    <span class="toast-icon">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M20 6 9 17l-5-5"/>
      </svg>
    </span>
    <span>${{message}}</span>
  `;

  container.appendChild(toast);
  setTimeout(() => toast.classList.add('show'), 20);

  setTimeout(() => {{
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }}, 3500);
}}
"""

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js_content)

print("app.js updated with dedicated New Launch, Bestsellers, and clean Category-only Catalogue!")
