# Update index.html and styles.css with animated logo containing the coffee cup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header Logo in index.html
old_header_logo = '''      <!-- Brand Logo (Center on Mobile, Left on Desktop) -->
      <a href="index.html" class="brand-logo-wrap" aria-label="Graffeine Tales Home">
        <img src="assets/logo_dark.png" alt="Graffeine Tales - Where Stories Become Art" class="brand-logo-img" />
      </a>'''

new_header_logo = '''      <!-- Brand Logo with Animated Coffee Cup (Center on Mobile, Left on Desktop) -->
      <a href="index.html" class="brand-logo-wrap" aria-label="Graffeine Tales Home">
        <div class="brand-cup-container">
          <div class="cup-steam-particles" aria-hidden="true">
            <span class="steam-wisp w1"></span>
            <span class="steam-wisp w2"></span>
          </div>
          <img src="assets/coffee_cup.png" alt="Graffeine Coffee Cup Icon" class="brand-cup-img" />
        </div>
        <img src="assets/logo_dark.png" alt="Graffeine Tales - Where Stories Become Art" class="brand-logo-img" />
      </a>'''

if old_header_logo in html:
    html = html.replace(old_header_logo, new_header_logo)
    print("Replaced header logo in index.html!")

# 2. Update Mobile Drawer Logo in index.html
old_drawer_logo = '''      <div class="mobile-drawer-header">
        <a href="index.html" class="brand-logo-wrap" onclick="closeMobileDrawer()">
          <img src="assets/logo_dark.png" alt="Graffeine Tales" class="brand-logo-img" />
        </a>'''

new_drawer_logo = '''      <div class="mobile-drawer-header">
        <a href="index.html" class="brand-logo-wrap" onclick="closeMobileDrawer()">
          <div class="brand-cup-container">
            <div class="cup-steam-particles" aria-hidden="true">
              <span class="steam-wisp w1"></span>
              <span class="steam-wisp w2"></span>
            </div>
            <img src="assets/coffee_cup.png" alt="Graffeine Coffee Cup Icon" class="brand-cup-img" />
          </div>
          <img src="assets/logo_dark.png" alt="Graffeine Tales" class="brand-logo-img" />
        </a>'''

if old_drawer_logo in html:
    html = html.replace(old_drawer_logo, new_drawer_logo)
    print("Replaced mobile drawer logo in index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")

# 3. Append Animated Logo Styles to styles.css
animated_logo_css = """
/* ==========================================================================
   27. ANIMATED BRAND LOGO WITH STEAMING COFFEE CUP
   ========================================================================== */
.brand-logo-wrap {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.brand-cup-container {
  position: relative;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  flex-shrink: 0;
}

.brand-cup-img {
  height: 38px;
  width: auto;
  object-fit: contain;
  transform-origin: bottom center;
  animation: ambientCupFloat 4s ease-in-out infinite;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
  filter: drop-shadow(0 2px 6px rgba(74, 53, 37, 0.16));
}

.brand-logo-wrap:hover .brand-cup-img {
  animation: none;
  transform: translateY(-2px) rotate(-6deg) scale(1.12);
  filter: drop-shadow(0 4px 10px rgba(200, 157, 102, 0.45));
}

.brand-logo-img {
  height: 42px;
  width: auto;
  object-fit: contain;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
}

.brand-logo-wrap:hover .brand-logo-img {
  transform: scale(1.02);
  filter: drop-shadow(0 2px 8px rgba(200, 157, 102, 0.25));
}

/* Ambient Floating Cup Animation */
@keyframes ambientCupFloat {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  35% {
    transform: translateY(-2.5px) rotate(-3.5deg);
  }
  70% {
    transform: translateY(0.5px) rotate(3deg);
  }
}

/* Rising Coffee Steam Wisps */
.cup-steam-particles {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  width: 22px;
  height: 16px;
  pointer-events: none;
  overflow: visible;
}

.steam-wisp {
  position: absolute;
  bottom: 0;
  width: 3px;
  height: 10px;
  background: linear-gradient(180deg, rgba(200, 157, 102, 0.7), rgba(200, 157, 102, 0));
  border-radius: 3px;
  filter: blur(1px);
  opacity: 0;
}

.steam-wisp.w1 {
  left: 5px;
  animation: steamRise 2.8s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

.steam-wisp.w2 {
  right: 5px;
  animation: steamRise 2.8s cubic-bezier(0.4, 0, 0.2, 1) 1.4s infinite;
}

@keyframes steamRise {
  0% {
    opacity: 0;
    transform: translateY(0) scaleX(1) scaleY(0.6);
  }
  30% {
    opacity: 0.8;
    transform: translateY(-5px) scaleX(1.4) scaleY(1);
  }
  70% {
    opacity: 0.35;
    transform: translateY(-11px) scaleX(2) scaleY(1.3) rotate(6deg);
  }
  100% {
    opacity: 0;
    transform: translateY(-16px) scaleX(2.5) scaleY(1.5) rotate(-8deg);
  }
}

/* Mobile Scaling for Animated Logo (<= 900px) */
@media (max-width: 900px) {
  .brand-logo-wrap {
    gap: 7px !important;
  }

  .brand-cup-img {
    height: 28px !important;
  }

  .cup-steam-particles {
    top: -9px !important;
    height: 12px !important;
  }

  .steam-wisp {
    height: 8px !important;
  }

  .brand-logo-img {
    height: 30px !important;
    max-height: 30px !important;
  }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(animated_logo_css)

print("Appended animated coffee cup logo styles to styles.css!")
