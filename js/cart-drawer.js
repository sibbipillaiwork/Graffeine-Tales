/**
 * Graffeine Tales Atelier — High-Converting Production Side Cart Drawer Engine
 * Features:
 * - 0ms Optimistic UI updates with instant state calculation
 * - Multi-tier Server/Client Milestone Unlock Engine (₹499 Free Shipping, ₹749 Free Stickers, ₹999 VIP Club)
 * - Celebratory Multi-Color Confetti Physics
 * - Anti-Exploitation One-Tick Upsell Bump (Locked to Limit 1)
 * - Auto-Rotating Impulse Cross-Sell Carousel ("Best Paired With")
 * - Smart Auto-Shuffling Coupon Engine & Slide-up Offers Modal
 * - Indian GST Breakdown & Juspay Hypercheckout Simulation Handshake
 * - Full synchronization with localStorage ('gtb_cart') and page badges
 */

// ==========================================================================
// 1. CONFETTI CELEBRATION PHYSICS ENGINE
// ==========================================================================
class CartConfetti {
  constructor(canvasId = 'gtbConfettiCanvas') {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas ? this.canvas.getContext('2d') : null;
    this.particles = [];
    this.animationFrame = null;
    this.gtbPalette = [
      '#D4AF37', // Gold Wax
      '#4D351D', // Deep Coffee
      '#2D6A4F', // Sage Craft
      '#C85A32', // Terracotta
      '#C6B58E', // Sand
      '#E9DFC2', // Logo Cream
      '#FFFFFF'  // Pure White
    ];
    if (this.canvas) {
      this.resize();
      window.addEventListener('resize', () => this.resize());
    }
  }

  resize() {
    if (!this.canvas) return;
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  burst(tier = 1) {
    if (!this.canvas || !this.ctx) return;
    this.resize();

    const count = tier === 3 ? 120 : tier === 2 ? 85 : 60;
    const originX = window.innerWidth > 500 ? (window.innerWidth - 230) : (window.innerWidth / 2);
    const originY = Math.min(window.innerHeight * 0.25, 200);

    for (let i = 0; i < count; i++) {
      const angle = (Math.PI / 2) + ((Math.random() - 0.5) * Math.PI * 1.5);
      const speed = 6 + Math.random() * 9;
      const size = 5 + Math.random() * 6;
      const color = this.gtbPalette[Math.floor(Math.random() * this.gtbPalette.length)];

      this.particles.push({
        x: originX + (Math.random() - 0.5) * 50,
        y: originY,
        vx: Math.cos(angle) * speed,
        vy: -Math.abs(Math.sin(angle) * speed) - 2.5,
        size,
        color,
        rotation: Math.random() * 360,
        rotationSpeed: (Math.random() - 0.5) * 12,
        wobble: Math.random() * 10,
        wobbleSpeed: 0.1 + Math.random() * 0.1,
        gravity: 0.22 + Math.random() * 0.08,
        drag: 0.965,
        opacity: 1,
        fadeSpeed: 0.008 + Math.random() * 0.006,
        shape: Math.random() > 0.4 ? 'rect' : 'circle'
      });
    }

    if (!this.animationFrame) {
      this.animate();
    }
  }

  animate() {
    if (!this.ctx) return;
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    for (let i = this.particles.length - 1; i >= 0; i--) {
      const p = this.particles[i];
      p.x += p.vx;
      p.y += p.vy;
      p.vy += p.gravity;
      p.vx *= p.drag;
      p.rotation += p.rotationSpeed;
      p.wobble += p.wobbleSpeed;
      p.opacity -= p.fadeSpeed;

      if (p.opacity <= 0 || p.y > this.canvas.height + 30) {
        this.particles.splice(i, 1);
        continue;
      }

      this.ctx.save();
      this.ctx.globalAlpha = Math.max(0, p.opacity);
      this.ctx.translate(p.x + Math.sin(p.wobble) * 2, p.y);
      this.ctx.rotate((p.rotation * Math.PI) / 180);
      this.ctx.fillStyle = p.color;

      if (p.shape === 'rect') {
        this.ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
      } else {
        this.ctx.beginPath();
        this.ctx.arc(0, 0, p.size / 2.2, 0, Math.PI * 2);
        this.ctx.fill();
      }
      this.ctx.restore();
    }

    if (this.particles.length > 0) {
      this.animationFrame = requestAnimationFrame(() => this.animate());
    } else {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      this.animationFrame = null;
    }
  }
}

// ==========================================================================
// 2. GRAFFEINE TALES CART DRAWER CONTROLLER
// ==========================================================================
class GtbCartScreen {
  constructor() {
    this.userId = 'gtb_usr_' + Math.floor(10000 + Math.random() * 90000);
    this.sessionId = 'gtb_sess_' + Math.floor(10000 + Math.random() * 90000);

    // Master Catalog of Graffeine Tales Products for Rapid 0ms Optimistic Updates
    this.catalog = {
      'prod-1': {
        title: 'Lady TeaTrip Acrylic Coaster & Teak Stand',
        pack_size: 'Single Piece with Stand',
        mrp: 899,
        price: 699,
        image_url: 'assets/products/lady_teatrip.jpg'
      },
      'prod-2': {
        title: 'Progress Not Perfection — 2026 Desk Calendar',
        pack_size: '12 Months Art Pack',
        mrp: 999,
        price: 850,
        image_url: 'assets/products/artist_calendar.jpg'
      },
      'prod-4': {
        title: 'Handcrafted Wooden Sunflower Bookmark',
        pack_size: '1 Wooden Bookmark',
        mrp: 449,
        price: 349,
        image_url: 'assets/products/wood_flower_bookmark.jpg'
      },
      'prod-5': {
        title: 'Reading Boo Die-Cut Magnetic Bookmark',
        pack_size: 'Magnetic Bookmark',
        mrp: 299,
        price: 249,
        image_url: 'assets/products/magnetic_reading_boo.jpg'
      },
      'prod-30': {
        title: 'The Creative Chaos Sticker Pack',
        pack_size: '10-Pack Curated',
        mrp: 499,
        price: 349,
        image_url: 'assets/products/sticker_desi_vibes.jpg'
      },
      'prod-31': {
        title: 'Tuxedo Cat & Tea Time Decal Pack',
        pack_size: '8-Pack Die-Cut',
        mrp: 399,
        price: 299,
        image_url: 'assets/products/sticker_cat_lover.jpg'
      },
      'prod-32': {
        title: 'Desi Bollywood Cult Classics Sticker Pack',
        pack_size: '10-Pack Die-Cut',
        mrp: 449,
        price: 349,
        image_url: 'assets/products/sticker_chai_lover.jpg'
      },
      'prod-33': {
        title: 'Mojo Jojo & 90s Nostalgia Decal Pack',
        pack_size: '6-Pack Holographic',
        mrp: 399,
        price: 299,
        image_url: 'assets/products/sticker_bookworm.jpg'
      },
      'prod-15': {
        title: 'Midnight Espresso Hardbound Journal',
        pack_size: '192 Ruled Pages (100 GSM)',
        mrp: 999,
        price: 799,
        image_url: 'assets/products/lady_teatrip.jpg'
      },
      // Promotional One-Tick Upsell Bump (Permanently locked to Quantity: 1)
      'SKU_UPSELL_BOOKMARK': {
        title: 'Holographic Gold Foil Bookmark',
        pack_size: 'Atelier Collector Edition',
        mrp: 249,
        price: 99,
        excludeFromCoupons: true,
        image_url: 'assets/products/wood_flower_bookmark.jpg'
      },
      // Free Milestone Gift Items
      'SKU_GIFT_STICKER_PACK': {
        title: 'Artisanal Die-Cut Sticker Pack & Art Print',
        pack_size: 'Complimentary Tier 2 Reward',
        mrp: 349,
        price: 0,
        is_gift: true,
        image_url: 'assets/flip_stickers.jpg'
      },
      'SKU_VIP_MEMBERSHIP': {
        title: '1-Year Atelier VIP Club Membership (+5% Off)',
        pack_size: 'Digital VIP Status',
        mrp: 999,
        price: 0,
        is_gift: true,
        image_url: 'assets/cart/silver_membership.svg'
      }
    };

    // Load initial cart from localStorage
    this.cartItems = this.loadCartFromStorage();
    this.appliedCouponCode = null;
    this.serverCartState = null;

    // Checkout ticker timer (19:29 min left)
    this.checkoutSecondsLeft = 1169;
    this.tickerInterval = null;
    this.crossSellInterval = null;

    // Confetti Engine
    this.confetti = new CartConfetti('gtbConfettiCanvas');
    this.lastAchievedTier = 0;

    // Available Coupons Data
    this.availableCoupons = [
      { code: 'SAVE50', minSubtotal: 499, discount: 50, desc: '₹50 OFF on orders above ₹499' },
      { code: 'SAVE100', minSubtotal: 749, discount: 100, desc: '₹100 OFF on orders above ₹749' },
      { code: 'SAVE150', minSubtotal: 999, discount: 150, desc: '₹150 OFF on orders above ₹999' },
      { code: 'FREESHIP', minSubtotal: 0, discount: 99, desc: 'Free Shipping on any order' }
    ];

    this.init();
  }

  loadCartFromStorage() {
    try {
      const stored = localStorage.getItem('gtb_cart');
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed) && parsed.length > 0) {
          // Normalize items format { sku_id, quantity, finish }
          return parsed.map(item => ({
            sku_id: item.id || item.sku_id || 'prod-30',
            quantity: item.qty || item.quantity || 1,
            finish: item.finish || item.variant || null
          }));
        }
      }
    } catch (e) {}

    // Default seeded cart item if completely empty on first visit
    return [
      { sku_id: 'prod-30', quantity: 1, finish: 'Matte Weatherproof' }
    ];
  }

  saveCartToStorage() {
    try {
      // Map to GTB standard cart format
      const formatted = this.cartItems
        .filter(item => !this.catalog[item.sku_id]?.is_gift)
        .map(item => {
          const cat = this.catalog[item.sku_id] || {};
          return {
            id: item.sku_id,
            sku_id: item.sku_id,
            name: cat.title || item.sku_id,
            price: cat.price || 349,
            qty: item.quantity,
            finish: item.finish,
            image: cat.image_url || 'assets/products/sticker_desi_vibes.jpg'
          };
        });
      localStorage.setItem('gtb_cart', JSON.stringify(formatted));

      // Update page badges
      this.updatePageBadges();
    } catch (e) {}
  }

  updatePageBadges() {
    const totalCount = this.cartItems
      .filter(item => !this.catalog[item.sku_id]?.is_gift)
      .reduce((sum, item) => sum + item.quantity, 0);

    const badges = document.querySelectorAll('#cart-badge-count, #bottom-cart-count, .cart-count-badge');
    badges.forEach(b => {
      b.textContent = totalCount;
      b.style.display = totalCount > 0 ? 'inline-flex' : 'none';
    });

    const headerBadge = document.getElementById('drawerHeaderCount');
    if (headerBadge) {
      headerBadge.textContent = `${totalCount} item${totalCount !== 1 ? 's' : ''}`;
    }
  }

  init() {
    this.bindEvents();
    this.initCrossSellAutoRotate();
    this.recalculateCart();
    this.startCheckoutTimer();
  }

  bindEvents() {
    // Drawer close buttons
    const btnClose = document.getElementById('btnDrawerClose');
    if (btnClose) {
      btnClose.addEventListener('click', () => window.closeCartDrawer());
    }

    const overlay = document.getElementById('cart-drawer-overlay');
    if (overlay) {
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) window.closeCartDrawer();
      });
    }

    // Checkout CTA button
    const btnProceed = document.getElementById('btnProceedBuy');
    if (btnProceed) {
      btnProceed.addEventListener('click', () => {
        if (!this.cartItems || this.cartItems.length === 0) {
          alert('Your cart is empty. Please add items to proceed!');
          return;
        }
        if (window.juspayModal) {
          window.juspayModal.open(this.serverCartState);
        }
      });
    }

    // Global keyboard Escape listener
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.closeOffersModal();
        window.closeCartDrawer();
      }
    });
  }

  startCheckoutTimer() {
    if (this.tickerInterval) clearInterval(this.tickerInterval);
    this.tickerInterval = setInterval(() => {
      if (this.checkoutSecondsLeft > 0) {
        this.checkoutSecondsLeft -= 1;
        const mins = String(Math.floor(this.checkoutSecondsLeft / 60)).padStart(2, '0');
        const secs = String(this.checkoutSecondsLeft % 60).padStart(2, '0');
        const timerEl = document.getElementById('bannerTimer');
        if (timerEl) {
          timerEl.textContent = `${mins}:${secs} min left to checkout`;
        }
      }
    }, 1000);
  }

  initCrossSellAutoRotate() {
    const carousel = document.getElementById('crossSellCarousel');
    if (!carousel) return;

    let isInteracting = false;
    let resumeTimer = null;

    const pauseRotation = () => {
      isInteracting = true;
      if (resumeTimer) clearTimeout(resumeTimer);
    };

    const resumeRotation = (delay = 1200) => {
      if (resumeTimer) clearTimeout(resumeTimer);
      resumeTimer = setTimeout(() => {
        isInteracting = false;
      }, delay);
    };

    carousel.addEventListener('mouseenter', pauseRotation);
    carousel.addEventListener('mouseleave', () => resumeRotation(800));
    carousel.addEventListener('touchstart', pauseRotation, { passive: true });
    carousel.addEventListener('touchend', () => resumeRotation(3500), { passive: true });

    if (this.crossSellInterval) clearInterval(this.crossSellInterval);
    this.crossSellInterval = setInterval(() => {
      if (isInteracting || !carousel) return;
      const firstCard = carousel.querySelector('.rec-card');
      const step = firstCard ? (firstCard.offsetWidth + 10) : 150;
      const maxScroll = carousel.scrollWidth - carousel.clientWidth;

      if (carousel.scrollLeft >= maxScroll - 15) {
        carousel.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        carousel.scrollBy({ left: step, behavior: 'smooth' });
      }
    }, 3000);
  }

  scrollCrossSell(direction = 1) {
    const carousel = document.getElementById('crossSellCarousel');
    if (!carousel) return;
    const firstCard = carousel.querySelector('.rec-card');
    const step = firstCard ? (firstCard.offsetWidth + 10) : 150;
    carousel.scrollBy({ left: direction * step, behavior: 'smooth' });
  }

  /**
   * 0ms Instant Optimistic Cart Recalculation
   */
  recalculateCart() {
    let itemsSubtotal = 0;
    let itemsMrpTotal = 0;
    let couponEligibleSubtotal = 0;

    const lineItems = [];

    // Calculate regular items
    this.cartItems.forEach(item => {
      const cat = this.catalog[item.sku_id];
      if (!cat) return;

      const unitPrice = cat.price;
      const mrp = cat.mrp || unitPrice;
      const lineTotal = unitPrice * item.quantity;
      const lineMrp = mrp * item.quantity;

      itemsSubtotal += lineTotal;
      itemsMrpTotal += lineMrp;

      if (!cat.excludeFromCoupons) {
        couponEligibleSubtotal += lineTotal;
      }

      lineItems.push({
        sku_id: item.sku_id,
        title: cat.title,
        pack_size: cat.pack_size,
        quantity: item.quantity,
        unit_price: unitPrice,
        mrp: mrp,
        line_total: lineTotal,
        image_url: cat.image_url,
        finish: item.finish
      });
    });

    // Milestone thresholds
    const isTier1Unlocked = itemsSubtotal >= 499;
    const isTier2Unlocked = itemsSubtotal >= 749;
    const isTier3Unlocked = itemsSubtotal >= 999;

    // Inject gifts if unlocked
    if (isTier2Unlocked && itemsSubtotal > 0) {
      const giftCat = this.catalog['SKU_GIFT_STICKER_PACK'];
      lineItems.push({
        sku_id: 'SKU_GIFT_STICKER_PACK',
        title: giftCat.title,
        pack_size: giftCat.pack_size,
        quantity: 1,
        unit_price: 0,
        mrp: giftCat.mrp,
        line_total: 0,
        image_url: giftCat.image_url,
        is_gift: true
      });
    }

    if (isTier3Unlocked && itemsSubtotal > 0) {
      const vipCat = this.catalog['SKU_VIP_MEMBERSHIP'];
      lineItems.push({
        sku_id: 'SKU_VIP_MEMBERSHIP',
        title: vipCat.title,
        pack_size: vipCat.pack_size,
        quantity: 1,
        unit_price: 0,
        mrp: vipCat.mrp,
        line_total: 0,
        image_url: vipCat.image_url,
        is_gift: true
      });
    }

    // Check confetti celebration for newly unlocked tiers
    let currentTier = 0;
    if (isTier3Unlocked) currentTier = 3;
    else if (isTier2Unlocked) currentTier = 2;
    else if (isTier1Unlocked) currentTier = 1;

    if (currentTier > this.lastAchievedTier && this.lastAchievedTier > 0) {
      this.confetti.burst(currentTier);
    }
    this.lastAchievedTier = currentTier;

    // Shipping fee calculation (Free if >= 499 or FREESHIP coupon applied)
    let shippingFee = 99;
    if (isTier1Unlocked || itemsSubtotal === 0 || this.appliedCouponCode === 'FREESHIP') {
      shippingFee = 0;
    }

    // Coupon discount calculation
    let couponDiscount = 0;
    if (this.appliedCouponCode) {
      const cp = this.availableCoupons.find(c => c.code === this.appliedCouponCode);
      if (cp && itemsSubtotal >= cp.minSubtotal) {
        if (cp.code === 'FREESHIP') {
          couponDiscount = shippingFee;
          shippingFee = 0;
        } else {
          couponDiscount = Math.min(cp.discount, couponEligibleSubtotal);
        }
      } else {
        this.appliedCouponCode = null; // Auto-remove invalid coupon if subtotal dropped
      }
    }

    // VIP Discount: 5% recurring discount on Tier 3
    let vipDiscount = 0;
    if (isTier3Unlocked) {
      vipDiscount = Math.round(couponEligibleSubtotal * 0.05);
    }

    const finalPayable = Math.max(0, itemsSubtotal + shippingFee - couponDiscount - vipDiscount);
    const productDiscount = Math.max(0, itemsMrpTotal - itemsSubtotal);

    this.serverCartState = {
      line_items: lineItems,
      authoritative_totals: {
        items_mrp_total: itemsMrpTotal,
        items_subtotal: itemsSubtotal,
        product_discount: productDiscount,
        coupon_discount: couponDiscount,
        vip_discount: vipDiscount,
        shipping_fee: shippingFee,
        final_payable_amount: finalPayable
      },
      milestones: {
        subtotal: itemsSubtotal,
        isTier1: isTier1Unlocked,
        isTier2: isTier2Unlocked,
        isTier3: isTier3Unlocked
      },
      applied_coupon: this.appliedCouponCode ? {
        code: this.appliedCouponCode,
        discount: couponDiscount
      } : null
    };

    // Save to localStorage & update DOM
    this.saveCartToStorage();
    this.render();
  }

  render() {
    if (!this.serverCartState) return;

    const {
      line_items = [],
      authoritative_totals = {},
      milestones = {},
      applied_coupon = null
    } = this.serverCartState;

    const subtotal = authoritative_totals.items_subtotal || 0;

    // 1. Render Line Items
    this.renderLineItems(line_items);

    // 2. Update One-Tick Upsell Bump Checkbox
    this.updateUpsellCheckboxState();

    // 3. Render Milestones Progress Bar
    this.renderMilestones(milestones, subtotal);

    // 4. Render Quick Coupons
    this.renderQuickCoupons(subtotal);

    // 5. Render Price Summary & Sticky Bar
    this.renderPriceSummary(authoritative_totals, milestones, applied_coupon);
  }

  renderLineItems(items) {
    const container = document.getElementById('cartItemsContainer');
    if (!container) return;

    if (items.length === 0) {
      container.innerHTML = `
        <div style="text-align:center; padding:36px 16px; background:#FFFFFF; border-radius:16px; border:1px dashed var(--gtb-sand);">
          <div style="font-size:2.2rem; margin-bottom:8px;">☕</div>
          <p style="font-family:var(--font-serif); font-size:1.15rem; font-weight:700; color:var(--gtb-coffee); margin-bottom:4px;">Your Atelier Bag is Empty</p>
          <p style="font-size:0.78rem; color:var(--gtb-tan); margin-bottom:14px;">Select handcrafted journals, stickers, or bookmarks to start your journey.</p>
          <button type="button" onclick="window.closeCartDrawer(); window.location.hash='catalogue-section';" style="background:var(--gtb-coffee); color:var(--gtb-cream); border:none; border-radius:99px; padding:8px 20px; font-size:0.78rem; font-weight:700; cursor:pointer;">
            Explore Catalogue &rarr;
          </button>
        </div>
      `;
      return;
    }

    container.innerHTML = items.map(item => {
      const isGift = item.is_gift;
      const isVip = item.sku_id === 'SKU_VIP_MEMBERSHIP';
      const isUpsell = item.sku_id === 'SKU_UPSELL_BOOKMARK';

      return `
        <div class="cart-item-card ${isGift ? (isVip ? 'is-vip-card' : 'is-gift-card') : ''}" data-sku="${item.sku_id}">
          <div class="item-thumb-tile">
            <img src="${item.image_url}" alt="${item.title}" loading="lazy" />
          </div>

          <div class="item-info-col">
            <div class="item-title-row">
              ${isVip ? '<span class="reward-pill vip-pill">✦ VIP CLUB STATUS</span>' : ''}
              ${isGift && !isVip ? '<span class="reward-pill gift-pill">✦ COMPLIMENTARY GIFT</span>' : ''}
              <h3 class="item-name" title="${item.title}">${item.title}</h3>
            </div>

            <div class="item-price-row">
              ${!isGift ? `
                <span class="item-price-current">₹${item.line_total}</span>
                ${item.mrp > item.unit_price ? `
                  <span class="item-price-mrp">₹${item.mrp * item.quantity}</span>
                  <span class="item-discount-tag">${Math.round(((item.mrp - item.unit_price) / item.mrp) * 100)}% OFF</span>
                ` : ''}
              ` : `
                <span class="reward-price-free">FREE</span>
                <span class="item-price-mrp">₹${item.mrp}</span>
                <span class="reward-savings-tag">100% OFF</span>
              `}
            </div>

            <div class="item-controls-row">
              ${!isGift ? `
                <div class="item-variant-select" title="${item.finish || item.pack_size || 'Artisanal'}">
                  <span>${item.finish || item.pack_size || 'Handcrafted'}</span>
                </div>

                ${isUpsell ? `
                  <div class="item-stepper is-locked" title="Special offer: Limited to 1 per order">
                    <button type="button" class="stepper-btn" onclick="cartApp.removeItem('${item.sku_id}')" title="Remove item" aria-label="Remove item">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                    </button>
                    <span class="stepper-qty">1</span>
                    <span class="stepper-lock-tag">Limit 1</span>
                  </div>
                ` : `
                  <div class="item-stepper" aria-label="Quantity Stepper">
                    <button type="button" class="stepper-btn" onclick="cartApp.updateQuantity('${item.sku_id}', ${item.quantity - 1})" title="${item.quantity === 1 ? 'Remove item' : 'Decrease quantity'}">
                      ${item.quantity === 1 ? `
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                      ` : `
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                      `}
                    </button>
                    <span class="stepper-qty">${item.quantity}</span>
                    <button type="button" class="stepper-btn" onclick="cartApp.updateQuantity('${item.sku_id}', ${item.quantity + 1})" title="Increase quantity">
                      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                    </button>
                  </div>
                `}
              ` : `
                <div style="display:flex; align-items:center; gap:5px; font-size:0.72rem; font-weight:700; color:var(--gtb-sage);">
                  <span>✓</span>
                  <span>${isVip ? '5% VIP Member Discount Applied' : 'Auto-Added to Order'}</span>
                </div>
              `}
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  updateUpsellCheckboxState() {
    const checkbox = document.getElementById('upsellAddonCheckbox');
    const bumpCard = document.getElementById('gtbAddonBump');
    const titleEl = document.getElementById('addonHighlightTitle');
    const badgeEl = document.getElementById('addonSavingsBadge');
    if (!checkbox || !bumpCard) return;

    const hasUpsell = this.cartItems.some(item => item.sku_id === 'SKU_UPSELL_BOOKMARK');
    checkbox.checked = hasUpsell;

    if (hasUpsell) {
      bumpCard.classList.add('checked');
      if (titleEl) titleEl.textContent = '✓ Gold Foil Bookmark added for ₹99';
      if (badgeEl) badgeEl.textContent = 'You saved ₹150!';
    } else {
      bumpCard.classList.remove('checked');
      if (titleEl) titleEl.textContent = 'Add Holographic Gold Foil Bookmark worth ₹249 for just ₹99';
      if (badgeEl) badgeEl.textContent = 'Special Atelier Offer • Limit 1';
    }
  }

  toggleUpsellItem(e) {
    const isChecked = e.target.checked;
    if (isChecked) {
      if (!this.cartItems.some(i => i.sku_id === 'SKU_UPSELL_BOOKMARK')) {
        this.cartItems.push({ sku_id: 'SKU_UPSELL_BOOKMARK', quantity: 1 });
      }
    } else {
      this.cartItems = this.cartItems.filter(i => i.sku_id !== 'SKU_UPSELL_BOOKMARK');
    }
    this.recalculateCart();
  }

  renderMilestones(milestones, subtotal = 0) {
    const fillBar = document.getElementById('milestoneFillBar');
    const caret = document.getElementById('milestoneCaret');
    const headline = document.getElementById('bannerHeadline');
    const giftIcon = document.getElementById('bannerGiftIcon');

    const node499 = document.getElementById('node499');
    const node749 = document.getElementById('node749');
    const node999 = document.getElementById('node999');

    // Segmented percentage coordinates
    let progressPct = 0;
    if (subtotal < 499) {
      progressPct = Math.min(25, Math.round((subtotal / 499) * 25));
    } else if (subtotal < 749) {
      const inRange = subtotal - 499;
      progressPct = 25 + Math.min(33, Math.round((inRange / (749 - 499)) * 33));
    } else if (subtotal < 999) {
      const inRange = subtotal - 749;
      progressPct = 58 + Math.min(32, Math.round((inRange / (999 - 749)) * 32));
    } else {
      progressPct = 100;
    }

    if (fillBar) fillBar.style.width = `${progressPct}%`;

    // Node 1: ₹499 (Free Shipping)
    if (node499) {
      const dot = node499.querySelector('.m-dot-circle');
      if (milestones.isTier1) {
        node499.classList.add('unlocked');
        if (dot) dot.innerHTML = '✓';
      } else {
        node499.classList.remove('unlocked');
        if (dot) dot.innerHTML = '🚚';
      }
    }

    // Node 2: ₹749 (Free Sticker Pack)
    if (node749) {
      const dot = node749.querySelector('.m-dot-circle');
      if (milestones.isTier2) {
        node749.classList.add('unlocked');
        if (dot) dot.innerHTML = '✓';
      } else {
        node749.classList.remove('unlocked');
        if (dot) dot.innerHTML = '🎁';
      }
    }

    // Node 3: ₹999 (Silver VIP Club)
    if (node999) {
      const dot = node999.querySelector('.m-dot-circle');
      if (milestones.isTier3) {
        node999.classList.add('unlocked');
        if (dot) dot.innerHTML = '✓';
      } else {
        node999.classList.remove('unlocked');
        if (dot) dot.innerHTML = '👑';
      }
    }

    // Dynamic Caret & Headline Banner Text
    if (subtotal < 499) {
      const diff = 499 - subtotal;
      if (caret) caret.style.left = '25%';
      if (giftIcon) giftIcon.textContent = '🚚';
      if (headline) headline.textContent = `Add ₹${diff} more for FREE Express Shipping!`;
    } else if (subtotal < 749) {
      const diff = 749 - subtotal;
      if (caret) caret.style.left = '58%';
      if (giftIcon) giftIcon.textContent = '🎁';
      if (headline) headline.textContent = `Add ₹${diff} more for a Free Die-Cut Sticker Pack!`;
    } else if (subtotal < 999) {
      const diff = 999 - subtotal;
      if (caret) caret.style.left = '90%';
      if (giftIcon) giftIcon.textContent = '👑';
      if (headline) headline.textContent = `Add ₹${diff} more to unlock 1-Year Studio VIP Club!`;
    } else {
      if (caret) caret.style.left = '90%';
      if (giftIcon) giftIcon.textContent = '🎉';
      if (headline) headline.textContent = 'All Rewards Unlocked! Free Shipping + Stickers + 5% VIP Club!';
    }
  }

  renderQuickCoupons(subtotal = 0) {
    const container = document.getElementById('quickCouponsScroll');
    if (!container) return;

    // Auto-shuffle: Sort coupons so highest applicable discount is in front
    const sorted = [...this.availableCoupons].sort((a, b) => {
      const aApplicable = subtotal >= a.minSubtotal;
      const bApplicable = subtotal >= b.minSubtotal;
      if (aApplicable && !bApplicable) return -1;
      if (!aApplicable && bApplicable) return 1;
      return b.discount - a.discount;
    });

    container.innerHTML = sorted.map(cp => {
      const isApplied = this.appliedCouponCode === cp.code;
      const isEligible = subtotal >= cp.minSubtotal;

      return `
        <div class="coupon-card ${isApplied ? 'applied' : ''}" onclick="cartApp.applyQuickCoupon('${cp.code}')" style="${isApplied ? 'background:var(--gtb-sage-light); border-color:var(--gtb-sage);' : ''}">
          <div class="coupon-card-left">
            <span style="font-size:0.85rem;">🏷️</span>
            <div>
              <div class="coupon-code-pill">${cp.code}</div>
              <div class="coupon-discount-text">₹${cp.discount} OFF</div>
            </div>
          </div>
          <button type="button" class="btn-coupon-card-apply" style="${isApplied ? 'background:var(--gtb-sage); color:#fff;' : (!isEligible ? 'opacity:0.5;' : '')}">
            ${isApplied ? 'Applied ✓' : 'Apply'}
          </button>
        </div>
      `;
    }).join('');
  }

  renderPriceSummary(totals, milestones, appliedCoupon) {
    const elMrp = document.getElementById('summaryItemMrp');
    const elSavingsRow = document.getElementById('summarySavingsRow');
    const elSavingsVal = document.getElementById('summarySavingsVal');
    const elCouponRow = document.getElementById('summaryCouponRow');
    const elCouponVal = document.getElementById('summaryCouponVal');
    const elVipRow = document.getElementById('summaryVipRow');
    const elVipVal = document.getElementById('summaryVipVal');
    const elShippingFee = document.getElementById('summaryShippingFee');
    const elGrandTotal = document.getElementById('summaryGrandTotal');
    const elBottomTotal = document.getElementById('bottomGrandTotal');

    if (elMrp) elMrp.textContent = `₹${totals.items_mrp_total || 0}`;

    if (elSavingsRow && elSavingsVal) {
      if (totals.product_discount > 0) {
        elSavingsRow.style.display = 'flex';
        elSavingsVal.textContent = `-₹${totals.product_discount}`;
      } else {
        elSavingsRow.style.display = 'none';
      }
    }

    if (elCouponRow && elCouponVal) {
      if (totals.coupon_discount > 0) {
        elCouponRow.style.display = 'flex';
        elCouponVal.textContent = `-₹${totals.coupon_discount}`;
      } else {
        elCouponRow.style.display = 'none';
      }
    }

    if (elVipRow && elVipVal) {
      if (totals.vip_discount > 0) {
        elVipRow.style.display = 'flex';
        elVipVal.textContent = `-₹${totals.vip_discount}`;
      } else {
        elVipRow.style.display = 'none';
      }
    }

    if (elShippingFee) {
      if (totals.shipping_fee === 0) {
        elShippingFee.innerHTML = '<span style="color:var(--gtb-sage); font-weight:800;">FREE</span>';
      } else {
        elShippingFee.textContent = `₹${totals.shipping_fee}`;
      }
    }

    if (elGrandTotal) elGrandTotal.textContent = `₹${totals.final_payable_amount || 0}`;
    if (elBottomTotal) elBottomTotal.textContent = `₹${totals.final_payable_amount || 0}`;
  }

  updateQuantity(skuId, newQty) {
    if (newQty <= 0) {
      this.removeItem(skuId);
      return;
    }
    const item = this.cartItems.find(i => i.sku_id === skuId);
    if (item) {
      item.quantity = newQty;
    }
    this.recalculateCart();
  }

  removeItem(skuId) {
    this.cartItems = this.cartItems.filter(i => i.sku_id !== skuId);
    this.recalculateCart();
  }

  addItem(skuId, qty = 1, finish = null) {
    const existing = this.cartItems.find(i => i.sku_id === skuId);
    if (existing) {
      existing.quantity += qty;
      if (finish) existing.finish = finish;
    } else {
      this.cartItems.push({
        sku_id: skuId,
        quantity: qty,
        finish: finish
      });
    }
    this.recalculateCart();
    window.openCartDrawer();
  }

  rapidAddOn(skuId, btn) {
    if (btn) {
      btn.textContent = 'Adding...';
      btn.style.opacity = '0.7';
    }

    this.addItem(skuId, 1);

    if (btn) {
      setTimeout(() => {
        btn.textContent = 'Added ✓';
        btn.style.background = 'var(--gtb-sage)';
        btn.style.color = '#FFFFFF';
        btn.style.opacity = '1';
        setTimeout(() => {
          btn.textContent = '+ Add';
          btn.style.background = '';
          btn.style.color = '';
        }, 1500);
      }, 250);
    }
  }

  applyManualCoupon() {
    const input = document.getElementById('couponInput');
    if (!input) return;
    const code = input.value.trim().toUpperCase();
    if (!code) return;

    this.applyQuickCoupon(code);
    input.value = '';
  }

  applyQuickCoupon(code) {
    const cp = this.availableCoupons.find(c => c.code === code);
    const subtotal = this.serverCartState?.authoritative_totals?.items_subtotal || 0;

    if (!cp) {
      alert(`Invalid promo code "${code}". Try SAVE50, SAVE100, or FREESHIP.`);
      return;
    }

    if (subtotal < cp.minSubtotal) {
      alert(`Code ${code} requires a minimum order of ₹${cp.minSubtotal}. Add ₹${cp.minSubtotal - subtotal} more!`);
      return;
    }

    if (this.appliedCouponCode === code) {
      this.appliedCouponCode = null; // Toggle remove
    } else {
      this.appliedCouponCode = code;
    }

    this.recalculateCart();
    this.closeOffersModal();
  }

  toggleAllOffersModal() {
    const modal = document.getElementById('allOffersModal');
    if (!modal) return;
    modal.classList.add('active');
    this.renderOffersModal();
  }

  closeOffersModal() {
    const modal = document.getElementById('allOffersModal');
    if (modal) modal.classList.remove('active');
  }

  renderOffersModal() {
    const couponsList = document.getElementById('offersCouponsList');
    const subtotal = this.serverCartState?.authoritative_totals?.items_subtotal || 0;

    if (couponsList) {
      couponsList.innerHTML = this.availableCoupons.map(cp => {
        const isApplied = this.appliedCouponCode === cp.code;
        const isEligible = subtotal >= cp.minSubtotal;

        return `
          <div style="background:#FFFFFF; border:1px solid rgba(198, 181, 142, 0.4); border-radius:12px; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; gap:12px;">
            <div>
              <div style="font-weight:800; font-size:0.85rem; color:var(--gtb-coffee);">${cp.code}</div>
              <div style="font-size:0.74rem; color:var(--gtb-tan); margin-top:2px;">${cp.desc}</div>
            </div>
            <button type="button" onclick="cartApp.applyQuickCoupon('${cp.code}')" style="background:${isApplied ? 'var(--gtb-sage)' : 'var(--gtb-coffee)'}; color:var(--gtb-cream); border:none; border-radius:8px; padding:6px 14px; font-size:0.74rem; font-weight:700; cursor:pointer;">
              ${isApplied ? 'Applied ✓' : (isEligible ? 'Apply' : 'Unlock')}
            </button>
          </div>
        `;
      }).join('');
    }
  }

  showPrepaidRewardsInfo() {
    alert('✦ Prepaid Order Privilege:\n\nPay with UPI, Credit/Debit Cards, or NetBanking to receive an instant ₹100 gift voucher redeemable on your next order, plus priority handcrafted packaging!');
  }

  scrollToSummary() {
    const sec = document.getElementById('priceSummarySection');
    if (sec) sec.scrollIntoView({ behavior: 'smooth' });
  }
}

// ==========================================================================
// 3. GLOBAL DRAWER CONTROLLERS & INTEGRATION
// ==========================================================================
window.openCartDrawer = function() {
  const overlay = document.getElementById('cart-drawer-overlay');
  if (overlay) {
    overlay.classList.add('open');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
  if (window.cartApp) {
    window.cartApp.recalculateCart();
  }
};

window.closeCartDrawer = function() {
  const overlay = document.getElementById('cart-drawer-overlay');
  if (overlay) {
    overlay.classList.remove('open');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }
};

window.toggleCartDrawer = function() {
  const overlay = document.getElementById('cart-drawer-overlay');
  if (overlay && overlay.classList.contains('open')) {
    window.closeCartDrawer();
  } else {
    window.openCartDrawer();
  }
};

// Global Add to Cart helper override so existing shop buttons seamlessly trigger the drawer
window.addToCart = function(productId, qty = 1, finish = null) {
  if (window.cartApp) {
    window.cartApp.addItem(productId, qty, finish);
  } else {
    // Fallback to storage
    const cart = JSON.parse(localStorage.getItem('gtb_cart') || '[]');
    const existing = cart.find(i => i.id === productId);
    if (existing) {
      existing.qty += qty;
    } else {
      cart.push({ id: productId, qty: qty, finish: finish });
    }
    localStorage.setItem('gtb_cart', JSON.stringify(cart));
    window.openCartDrawer();
  }
};

// Initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  window.cartApp = new GtbCartScreen();

  // Attach to existing cart icons and buttons
  document.querySelectorAll('#cart-trigger, #bnav-cart, #floating-cart-pill, .cart-btn, [data-open-cart]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.openCartDrawer();
    });
  });
});
