with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace toggleBtn listener in initHeader and add mobile drawer handling
old_init_header = """  const toggleBtn = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  if (toggleBtn && navMenu) {
    toggleBtn.addEventListener('click', () => {
      navMenu.classList.toggle('mobile-open');
    });
  }"""

new_init_header = """  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('#mobile-drawer-overlay');
  const drawerClose = document.querySelector('#mobile-drawer-close');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', () => {
      openMobileDrawer();
    });
  }

  if (drawerClose && drawer) {
    drawerClose.addEventListener('click', () => {
      closeMobileDrawer();
    });
  }

  if (drawer) {
    drawer.addEventListener('click', (e) => {
      if (e.target === drawer) {
        closeMobileDrawer();
      }
    });
  }"""

if old_init_header in js:
    js = js.replace(old_init_header, new_init_header)
    print("Updated initHeader in app.js!")

mobile_functions = """
// 12. Mobile Drawer Helpers
function openMobileDrawer() {
  const drawer = document.querySelector('#mobile-drawer-overlay');
  if (drawer) {
    drawer.classList.add('open');
    document.body.classList.add('no-scroll');
  }
}

function closeMobileDrawer() {
  const drawer = document.querySelector('#mobile-drawer-overlay');
  if (drawer) {
    drawer.classList.remove('open');
    document.body.classList.remove('no-scroll');
  }
}

function openSearchFromMobile() {
  closeMobileDrawer();
  const searchModal = document.querySelector('#search-modal-overlay');
  const searchInput = document.querySelector('#search-modal-input');
  if (searchModal) {
    searchModal.classList.add('open');
    if (searchInput) {
      setTimeout(() => searchInput.focus(), 150);
    }
  }
}

function filterFromMobile(cat) {
  closeMobileDrawer();
  currentFilter = cat;
  
  // Update category pill active state
  const pills = document.querySelectorAll('#catalog-filter-pills .pill-btn');
  pills.forEach(p => {
    if (p.dataset.cat === cat) {
      p.classList.add('active');
      p.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    } else {
      p.classList.remove('active');
    }
  });

  renderCatalog();
}
"""

js += mobile_functions

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with mobile drawer helpers!")
