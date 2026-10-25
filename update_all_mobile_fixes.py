import re

# ==========================================
# 1. UPDATE APP.JS
# ==========================================
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update renderCategoryPills to remove counts and serial numbers
old_render_pills = '''function renderCategoryPills() {
  // Accurate counts using clean categoryGroup
  const counts = {
    all: productsData.length,
    stationaries: productsData.filter(p => p.categoryGroup === 'stationaries').length,
    journals: productsData.filter(p => p.categoryGroup === 'journals').length,
    decor: productsData.filter(p => p.categoryGroup === 'decor').length,
    events: productsData.filter(p => p.categoryGroup === 'events').length,
    bulk: productsData.filter(p => p.categoryGroup === 'bulk').length,
  };

  const pillsContainer = document.querySelector('#catalog-filter-pills');
  if (!pillsContainer) return;

  const categories = [
    { id: 'all', label: 'All Editions', count: counts.all },
    { id: 'stationaries', label: '1. Stationaries', count: counts.stationaries },
    { id: 'journals', label: '2. Journals', count: counts.journals },
    { id: 'decor', label: '3. Handcrafted Décor', count: counts.decor },
    { id: 'events', label: '4. Events & Gifting', count: counts.events },
    { id: 'bulk', label: '5. Bulk Orders', count: counts.bulk }
  ];

  pillsContainer.innerHTML = categories.map(cat => `
    <button class="pill-btn ${currentFilter === cat.id ? 'active' : ''}" data-cat="${cat.id}">
      <span>${cat.label}</span>
      <span class="pill-count">${cat.count}</span>
    </button>
  `).join('');

  pillsContainer.querySelectorAll('.pill-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      pillsContainer.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.dataset.cat;
      renderCatalog();
    });
  });
}'''

new_render_pills = '''function renderCategoryPills() {
  const pillsContainer = document.querySelector('#catalog-filter-pills');
  if (!pillsContainer) return;

  // Clean category names without serial numbers and counts
  const categories = [
    { id: 'all', label: 'All Editions' },
    { id: 'stationaries', label: 'Stationaries & Calendars' },
    { id: 'journals', label: 'Journals & Planners' },
    { id: 'decor', label: 'Handcrafted Décor' },
    { id: 'events', label: 'Events & Gifting' },
    { id: 'bulk', label: 'Bulk Orders' }
  ];

  pillsContainer.innerHTML = categories.map(cat => `
    <button class="pill-btn ${currentFilter === cat.id ? 'active' : ''}" data-cat="${cat.id}">
      <span>${cat.label}</span>
    </button>
  `).join('');

  pillsContainer.querySelectorAll('.pill-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      pillsContainer.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.dataset.cat;
      renderCatalog();
    });
  });
}'''

if old_render_pills in js:
    js = js.replace(old_render_pills, new_render_pills)
    print("Updated renderCategoryPills in app.js successfully!")
else:
    print("Could not find exact old_render_pills in app.js, using regex...")
    pills_pattern = r'function renderCategoryPills\(\)\s*\{[\s\S]*?renderCatalog\(\);\s*\}\);\s*\}\);?\s*\}'
    if re.search(pills_pattern, js):
        js = re.sub(pills_pattern, new_render_pills, js)
        print("Replaced renderCategoryPills via regex!")
    else:
        print("Regex match failed for renderCategoryPills!")

# Add My Account controller logic to app.js
account_logic = '''
// 14. Atelier My Account Modal Controller
function openAccountModal() {
  const modal = document.querySelector('#account-modal-overlay');
  if (modal) {
    modal.classList.add('open');
    document.body.classList.add('no-scroll');
  }
}

function closeAccountModal() {
  const modal = document.querySelector('#account-modal-overlay');
  if (modal) {
    modal.classList.remove('open');
    document.body.classList.remove('no-scroll');
  }
}

function initAccountModal() {
  const modal = document.querySelector('#account-modal-overlay');
  const closeBtn = document.querySelector('#account-modal-close');
  const bnavAccount = document.querySelector('#bnav-account');
  const drawerAccountBtn = document.querySelector('#mobile-drawer-account-btn');

  if (closeBtn) {
    closeBtn.addEventListener('click', closeAccountModal);
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeAccountModal();
      }
    });
  }

  if (bnavAccount) {
    bnavAccount.addEventListener('click', (e) => {
      e.preventDefault();
      openAccountModal();
    });
  }

  if (drawerAccountBtn) {
    drawerAccountBtn.addEventListener('click', (e) => {
      e.preventDefault();
      closeMobileDrawer();
      openAccountModal();
    });
  }

  // Keyboard Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAccountModal();
    }
  });
}

// Expose globally
window.openAccountModal = openAccountModal;
window.closeAccountModal = closeAccountModal;
'''

if 'initAccountModal()' not in js:
    # Append account logic and call initAccountModal
    js += account_logic
    # Also add call inside DOMContentLoaded or init
    if 'initMobileBottomNav();' in js:
        js = js.replace('initMobileBottomNav();', 'initMobileBottomNav();\n  initAccountModal();')
        print("Added initAccountModal call to app.js!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Saved app.js successfully!")

# ==========================================
# 2. UPDATE STYLES.CSS
# ==========================================
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the unscoped .brand-logo-wrap at line 3865 that caused the floating logo in drawer
old_logo_rule = '''.brand-logo-wrap {
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
  }'''

new_logo_rule = '''.site-header .brand-logo-wrap {
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
  }'''

if old_logo_rule in css:
    css = css.replace(old_logo_rule, new_logo_rule)
    print("Scoped header brand-logo-wrap in styles.css!")
else:
    print("Could not find exact old_logo_rule, trying regex...")
    logo_pattern = r'\.brand-logo-wrap\s*\{\s*position:\s*absolute\s*!important;\s*left:\s*50%\s*!important;\s*top:\s*50%\s*!important;\s*transform:\s*translate\(-50%,\s*-50%\)\s*!important;'
    if re.search(logo_pattern, css):
        css = re.sub(logo_pattern, '.site-header .brand-logo-wrap {\n    position: absolute !important;\n    left: 50% !important;\n    top: 50% !important;\n    transform: translate(-50%, -50%) !important;', css)
        print("Scoped header brand-logo-wrap via regex!")

# Append new styles for mobile drawer menu title, account button, modal, and bottom nav 5 tabs
additional_css = """
/* ==========================================================================
   28. MOBILE DRAWER POLISH & MY ACCOUNT MODAL
   ========================================================================== */
.mobile-drawer-title {
  font-family: var(--f-serif);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--c-espresso);
  letter-spacing: 0.02em;
}

.mobile-drawer-account-btn {
  width: 100%;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 13px 16px !important;
  background: rgba(200, 157, 102, 0.12) !important;
  border: 1px solid rgba(200, 157, 102, 0.3) !important;
  border-radius: 12px !important;
  color: var(--c-espresso) !important;
  font-family: inherit !important;
  font-weight: 600 !important;
  font-size: 0.92rem !important;
  cursor: pointer !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  margin-bottom: 12px !important;
  box-sizing: border-box !important;
}

.mobile-drawer-account-btn .account-btn-left {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  color: var(--c-espresso) !important;
}

.mobile-drawer-account-btn .account-btn-left svg {
  color: var(--c-tan) !important;
  flex-shrink: 0;
}

.mobile-drawer-account-btn .account-chevron {
  color: var(--c-text-muted) !important;
  transition: transform 0.2s ease !important;
}

.mobile-drawer-account-btn:hover,
.mobile-drawer-account-btn:active {
  background: rgba(200, 157, 102, 0.22) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 14px rgba(200, 157, 102, 0.16) !important;
}

.mobile-drawer-account-btn:hover .account-chevron {
  transform: translateX(2px) !important;
  color: var(--c-tan) !important;
}

/* Atelier My Account Modal */
.account-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(43, 37, 35, 0.65);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  z-index: 1200;
  opacity: 0;
  visibility: hidden;
  transition: all 0.32s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  box-sizing: border-box;
}

.account-modal-overlay.open {
  opacity: 1;
  visibility: visible;
}

.account-modal {
  background: #FFFFFF;
  width: 100%;
  max-width: 440px;
  border-radius: 20px;
  box-shadow: 0 24px 60px rgba(43, 37, 35, 0.28);
  overflow: hidden;
  transform: scale(0.93) translateY(12px);
  transition: all 0.32s cubic-bezier(0.16, 1, 0.3, 1);
  border: 1px solid rgba(200, 157, 102, 0.25);
  display: flex;
  flex-direction: column;
}

.account-modal-overlay.open .account-modal {
  transform: scale(1) translateY(0);
}

.account-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 22px;
  background: linear-gradient(135deg, rgba(248, 245, 237, 0.95), rgba(244, 238, 227, 0.95));
  border-bottom: 1px solid rgba(200, 157, 102, 0.2);
}

.account-header-profile {
  display: flex;
  align-items: center;
  gap: 12px;
}

.account-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--c-espresso);
  color: #FAF7F2;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(43, 37, 35, 0.15);
  flex-shrink: 0;
}

.account-profile-info {
  display: flex;
  flex-direction: column;
}

.account-user-name {
  font-family: var(--f-serif);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--c-espresso);
  margin: 0;
  line-height: 1.2;
}

.account-user-tier {
  font-size: 0.72rem;
  color: var(--c-tan);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 3px;
}

.account-modal-close {
  background: none;
  border: none;
  color: var(--c-espresso);
  cursor: pointer;
  padding: 8px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.account-modal-close:hover {
  background: rgba(43, 37, 35, 0.08);
}

.account-modal-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  max-height: 75vh;
  overflow-y: auto;
}

.account-nav-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.account-card-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border-radius: 14px;
  background: #FAF8F5;
  border: 1px solid rgba(43, 37, 35, 0.07);
  text-align: left;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  font-family: inherit;
  width: 100%;
  box-sizing: border-box;
}

.account-card-item:hover,
.account-card-item:active {
  background: #FFFFFF;
  border-color: var(--c-tan);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(43, 37, 35, 0.06);
}

.account-card-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(200, 157, 102, 0.15);
  color: var(--c-tan);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.account-card-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.account-card-text strong {
  font-size: 0.92rem;
  color: var(--c-espresso);
  font-weight: 600;
}

.account-card-text span {
  font-size: 0.76rem;
  color: var(--c-text-muted);
}

.account-perks-box {
  background: linear-gradient(135deg, rgba(74, 53, 37, 0.04), rgba(200, 157, 102, 0.08));
  border: 1px dashed rgba(200, 157, 102, 0.45);
  border-radius: 14px;
  padding: 14px 16px;
}

.perks-badge {
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--c-tan);
  letter-spacing: 0.06em;
  margin-bottom: 4px;
}

.account-perks-box h4 {
  margin: 0 0 4px;
  font-size: 0.9rem;
  color: var(--c-espresso);
  font-family: var(--f-serif);
}

.account-perks-box p {
  margin: 0;
  font-size: 0.78rem;
  color: var(--c-text-muted);
  line-height: 1.4;
}

/* Ensure 5-tab mobile bottom nav items are well proportioned */
@media (max-width: 900px) {
  .mobile-bottom-nav .bottom-nav-item {
    padding: 6px 0 !important;
    gap: 2px !important;
  }

  .mobile-bottom-nav .bottom-nav-label {
    font-size: 0.64rem !important;
  }
}
"""

css += additional_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Saved styles.css successfully!")
