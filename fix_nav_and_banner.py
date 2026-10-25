# Clean up styles.css navigation and header styling to ensure pixel-perfect layout

with open('styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Remove old announcement bar styling if present
old_announcement_css = """/* ==========================================================================
   1. ANNOUNCEMENT BAR
   ========================================================================== */
.announcement-bar {
  background-color: var(--c-espresso);
  color: var(--c-cream);
  font-size: 0.825rem;
  padding: 10px 0;
  border-bottom: 1px solid rgba(233, 223, 194, 0.15);
  position: relative;
  z-index: 101;
}

.announcement-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ticker-item {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  letter-spacing: 0.04em;
}

.ticker-badge {
  background-color: var(--c-tan);
  color: var(--c-warm-paper);
  padding: 2px 8px;
  border-radius: var(--r-full);
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.announcement-meta {
  display: flex;
  align-items: center;
  gap: 20px;
}

.announcement-meta a, .announcement-meta span {
  color: rgba(233, 223, 194, 0.85);
  font-size: 0.775rem;
  letter-spacing: 0.02em;
}

.announcement-meta a:hover {
  color: var(--c-warm-paper);
}

.currency-select {
  background: transparent;
  color: var(--c-cream);
  border: 1px solid rgba(233, 223, 194, 0.25);
  border-radius: var(--r-sm);
  padding: 2px 6px;
  font-size: 0.75rem;
  cursor: pointer;
  outline: none;
}

.currency-select option {
  background-color: var(--c-espresso);
  color: var(--c-cream);
}"""

if old_announcement_css in css:
    css = css.replace(old_announcement_css, "/* Announcement Bar removed */\n.announcement-bar { display: none !important; }")
    print("Cleaned up old announcement bar styles in styles.css!")

# Append our master header and navigation glassmorphism specification
master_nav_css = """
/* ==========================================================================
   25. MASTER NAVIGATION ARCHITECTURE (DESKTOP & MOBILE GLASSMORPHISM)
   ========================================================================== */

/* Universal Glassmorphic Header */
.site-header {
  position: sticky !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  background-color: rgba(248, 245, 237, 0.85) !important;
  backdrop-filter: blur(20px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
  border-bottom: 1px solid rgba(200, 157, 102, 0.18) !important;
  box-shadow: 0 4px 20px rgba(43, 37, 35, 0.03) !important;
  z-index: 1000 !important;
}

/* Announcement bar permanently hidden */
.announcement-bar {
  display: none !important;
}

/* Desktop Header (>= 901px) */
@media (min-width: 901px) {
  .site-header {
    height: 80px;
  }

  .nav-container {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    height: 80px !important;
    padding: 0 32px !important;
    position: relative !important;
  }

  /* Hamburger hidden on desktop */
  .mobile-toggle {
    display: none !important;
  }

  .brand-logo-wrap {
    display: flex;
    align-items: center;
  }

  .brand-logo-img {
    height: 44px;
    width: auto;
  }

  .site-nav {
    display: flex;
    align-items: center;
  }

  .nav-menu {
    display: flex !important;
    align-items: center;
    gap: 32px;
    list-style: none;
  }

  .nav-actions {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
  }

  .nav-actions .action-btn {
    width: 42px !important;
    height: 42px !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.6) !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(43, 37, 35, 0.08) !important;
    color: var(--c-espresso) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03) !important;
  }

  .nav-actions .action-btn:hover {
    background: var(--c-white) !important;
    border-color: var(--c-tan) !important;
    transform: translateY(-1px) !important;
    color: var(--c-tan) !important;
  }

  .mobile-bottom-nav {
    display: none !important;
  }
}

/* Mobile Header & Bottom Navigation (<= 900px) */
@media (max-width: 900px) {
  .site-header {
    height: 60px !important;
  }

  .nav-container {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    height: 60px !important;
    padding: 0 16px !important;
    position: relative !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  /* 1. Left Aligned Hamburger */
  .mobile-toggle {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 40px !important;
    height: 40px !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.65) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(43, 37, 35, 0.08) !important;
    color: var(--c-espresso) !important;
    box-shadow: 0 2px 8px rgba(43, 37, 35, 0.04) !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
    z-index: 2 !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  .mobile-toggle svg {
    width: 20px !important;
    height: 20px !important;
  }

  .mobile-toggle:active {
    transform: scale(0.92) !important;
    background: var(--c-white) !important;
  }

  /* 2. Perfectly Center Aligned Logo */
  .brand-logo-wrap {
    position: absolute !important;
    left: 50% !important;
    top: 50% !important;
    transform: translate(-50%, -50%) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    z-index: 1 !important;
    margin: 0 !important;
    padding: 0 !important;
    pointer-events: auto !important;
  }

  .brand-logo-img {
    height: 32px !important;
    max-height: 32px !important;
    width: auto !important;
    object-fit: contain !important;
    margin: 0 !important;
  }

  /* Hide Desktop Nav on mobile */
  .site-nav,
  .nav-menu {
    display: none !important;
  }

  /* 3. Right Aligned Actions: Search & Cart ONLY */
  .nav-actions {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-end !important;
    gap: 8px !important;
    z-index: 2 !important;
    margin-left: auto !important;
    flex-shrink: 0 !important;
    padding: 0 !important;
    height: 40px !important;
  }

  /* Clean round glass icon buttons */
  .nav-actions .action-btn {
    width: 40px !important;
    height: 40px !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.65) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(43, 37, 35, 0.08) !important;
    color: var(--c-espresso) !important;
    box-shadow: 0 2px 8px rgba(43, 37, 35, 0.04) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important;
    margin: 0 !important;
    cursor: pointer !important;
    position: relative !important;
  }

  .nav-actions .action-btn svg {
    width: 19px !important;
    height: 19px !important;
  }

  .nav-actions .action-btn:active {
    transform: scale(0.92) !important;
    background: var(--c-white) !important;
  }

  /* Hide Wishlist button in top bar on mobile (lives in bottom nav) */
  .desktop-only-action,
  #wishlist-trigger {
    display: none !important;
  }

  /* Hide desktop keyboard shortcut hint */
  .kbd-hint {
    display: none !important;
  }

  /* Cart Badge on Mobile Top Bar */
  #cart-badge-count {
    position: absolute !important;
    top: -2px !important;
    right: -2px !important;
    background: var(--c-tan) !important;
    color: var(--c-white) !important;
    font-size: 0.6rem !important;
    font-weight: 700 !important;
    width: 17px !important;
    height: 17px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: 2px solid #FAF7F2 !important;
    box-shadow: 0 2px 6px rgba(200, 157, 102, 0.4) !important;
  }

  /* 4. Mobile Bottom Navigation Bar (Glassmorphism) */
  .mobile-bottom-nav {
    display: flex !important;
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    height: calc(60px + env(safe-area-inset-bottom, 0px)) !important;
    padding-bottom: env(safe-area-inset-bottom, 0px) !important;
    background: rgba(255, 255, 255, 0.88) !important;
    backdrop-filter: blur(24px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
    border-top: 1px solid rgba(200, 157, 102, 0.2) !important;
    box-shadow: 0 -4px 20px rgba(43, 37, 35, 0.06) !important;
    z-index: 1000 !important;
    justify-content: space-around !important;
    align-items: center !important;
  }

  body {
    padding-bottom: calc(70px + env(safe-area-inset-bottom, 0px)) !important;
  }

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
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
    padding: 6px 0 !important;
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
    width: 24px !important;
    height: 24px !important;
  }

  .bottom-nav-icon svg {
    width: 20px !important;
    height: 20px !important;
  }

  .bottom-nav-label {
    font-size: 0.65rem !important;
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
    font-size: 0.58rem !important;
    font-weight: 700 !important;
    width: 16px !important;
    height: 16px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: 2px solid #FFFFFF !important;
    box-shadow: 0 2px 6px rgba(200, 157, 102, 0.4) !important;
  }
}
"""

css += master_nav_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied master navigation architecture to styles.css!")
