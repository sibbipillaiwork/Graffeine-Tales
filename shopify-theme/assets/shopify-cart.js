/**
 * GRAFFEINE TALES — SHOPIFY NATIVE AJAX CART ENGINE
 * Provides seamless bridge between Luxury Slide-Over Cart Drawer & Shopify's Live Cart API.
 */

window.ShopifyCart = {
  // Fetch live cart JSON from Shopify
  getCart: async function() {
    try {
      const res = await fetch((window.ShopifyTheme ? window.ShopifyTheme.cartUrl : '/cart') + '.js');
      const cart = await res.json();
      return cart;
    } catch (err) {
      console.warn('[ShopifyCart] Falling back to local cart data', err);
      return null;
    }
  },

  // Add item by variant ID to Shopify Cart
  addItem: async function(variantId, qty = 1, properties = {}) {
    try {
      const res = await fetch((window.ShopifyTheme ? window.ShopifyTheme.cartAddUrl : '/cart/add') + '.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          id: variantId,
          quantity: qty,
          properties: properties
        })
      });
      const item = await res.json();
      await this.refreshDrawer();
      if (typeof showToast === 'function') {
        showToast(`✦ Added to your Atelier Bag`);
      }
      const cartDrawer = document.querySelector('#cart-drawer-overlay');
      if (cartDrawer) cartDrawer.classList.add('open');
      return item;
    } catch (err) {
      console.error('[ShopifyCart] Failed to add item', err);
    }
  },

  // Update line item quantity
  changeItem: async function(lineKeyOrIndex, qty) {
    try {
      const res = await fetch((window.ShopifyTheme ? window.ShopifyTheme.cartChangeUrl : '/cart/change') + '.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          line: lineKeyOrIndex,
          quantity: qty
        })
      });
      const cart = await res.json();
      await this.refreshDrawer();
      return cart;
    } catch (err) {
      console.error('[ShopifyCart] Failed to change quantity', err);
    }
  },

  // Synchronize and render Shopify Cart in the drawer
  refreshDrawer: async function() {
    const cart = await this.getCart();
    if (!cart) return;

    const cartBadge = document.querySelector('#cart-badge-count');
    const bottomCartBadge = document.querySelector('#bottom-cart-count');
    const subtotalEl = document.querySelector('#cart-subtotal-val');
    const cartList = document.querySelector('#cart-items-list');
    const goalLabel = document.querySelector('#shipping-goal-label');
    const progressFill = document.querySelector('#shipping-progress-fill');

    const totalCount = cart.item_count;
    const totalAmount = cart.total_price / 100; // in store currency
    const threshold = (window.ShopifyTheme && window.ShopifyTheme.freeShippingThreshold) ? window.ShopifyTheme.freeShippingThreshold : 1499;

    if (cartBadge) {
      cartBadge.textContent = totalCount;
      cartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
    }
    if (bottomCartBadge) {
      bottomCartBadge.textContent = totalCount;
      bottomCartBadge.style.display = totalCount > 0 ? 'inline-flex' : 'none';
    }
    if (subtotalEl) {
      subtotalEl.textContent = `₹${Math.round(totalAmount).toLocaleString('en-IN')}`;
    }

    // Free shipping threshold progress bar
    if (goalLabel && progressFill) {
      if (totalAmount >= threshold) {
        goalLabel.innerHTML = '<span>✨ You unlocked <strong>FREE Studio Courier Shipping!</strong></span>';
        progressFill.style.width = '100%';
      } else {
        const remaining = Math.round(threshold - totalAmount);
        const pct = Math.min(100, Math.round((totalAmount / threshold) * 100));
        goalLabel.innerHTML = `<span>Add <strong>₹${remaining.toLocaleString('en-IN')}</strong> more for <strong>FREE Shipping</strong></span><span>${pct}%</span>`;
        progressFill.style.width = `${pct}%`;
      }
    }

    if (!cartList) return;

    if (cart.items.length === 0) {
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
    }

    cartList.innerHTML = cart.items.map((item, index) => `
      <div class="cart-item">
        <img src="${item.image || 'assets/products/lady_teatrip.jpg'}" alt="${item.product_title}" class="cart-item-img" />
        <div class="cart-item-info">
          <h4 class="item-name">${item.product_title}</h4>
          <p class="item-variant">${item.variant_title || 'Atelier Original'}</p>
          <div class="qty-control">
            <button class="qty-btn" onclick="ShopifyCart.changeItem(${index + 1}, ${item.quantity - 1})" aria-label="Decrease">−</button>
            <span class="qty-val">${item.quantity}</span>
            <button class="qty-btn" onclick="ShopifyCart.changeItem(${index + 1}, ${item.quantity + 1})" aria-label="Increase">+</button>
          </div>
        </div>
        <div class="cart-item-actions">
          <span class="item-price">₹${Math.round(item.final_line_price / 100).toLocaleString('en-IN')}</span>
          <button class="remove-btn" onclick="ShopifyCart.changeItem(${index + 1}, 0)" title="Remove item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>
            </svg>
          </button>
        </div>
      </div>
    `).join('');
  }
};

// Global helper for product cards
window.addShopifyItem = function(variantId, qty = 1) {
  if (window.ShopifyCart && window.ShopifyTheme) {
    window.ShopifyCart.addItem(variantId, qty);
  } else if (typeof addToCart === 'function') {
    addToCart(variantId, qty);
  }
};

// Auto-sync cart on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  if (window.ShopifyTheme) {
    window.ShopifyCart.refreshDrawer();
  }
});
