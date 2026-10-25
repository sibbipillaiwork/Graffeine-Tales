"""
Graffeine Tales — Complete Shopify Online Store 2.0 Theme Generator
Builds a fully functional, complete Shopify theme ready for direct ZIP upload to Shopify Admin.
"""

import os
import shutil
import re
import json
import zipfile

BASE_DIR = r"c:\Users\sibbi\OneDrive\Desktop\GTB"
THEME_DIR = os.path.join(BASE_DIR, "shopify-theme")
ZIP_OUTPUT = os.path.join(BASE_DIR, "Graffeine-Tales-Shopify-Theme.zip")

def clean_and_make_dirs():
    if os.path.exists(THEME_DIR):
        shutil.rmtree(THEME_DIR)
    
    subdirs = [
        "assets",
        "config",
        "layout",
        "locales",
        "sections",
        "snippets",
        "templates"
    ]
    for d in subdirs:
        os.makedirs(os.path.join(THEME_DIR, d), exist_ok=True)
    print("Theme directories initialized.")

def copy_and_flatten_assets():
    assets_dest = os.path.join(THEME_DIR, "assets")
    src_assets = os.path.join(BASE_DIR, "assets")
    
    copied = 0
    # Copy root assets
    for item in os.listdir(src_assets):
        item_path = os.path.join(src_assets, item)
        if os.path.isfile(item_path):
            shutil.copy2(item_path, os.path.join(assets_dest, item))
            copied += 1
            
    # Copy products folder assets
    products_dir = os.path.join(src_assets, "products")
    if os.path.exists(products_dir):
        for item in os.listdir(products_dir):
            item_path = os.path.join(products_dir, item)
            if os.path.isfile(item_path):
                shutil.copy2(item_path, os.path.join(assets_dest, item))
                copied += 1
                
    # Copy styles.css
    shutil.copy2(os.path.join(BASE_DIR, "styles.css"), os.path.join(assets_dest, "styles.css"))
    # Copy products_data.json
    shutil.copy2(os.path.join(BASE_DIR, "products_data.json"), os.path.join(assets_dest, "products_data.json"))
    
    print(f"Copied {copied} image and stylesheet assets into shopify-theme/assets/")

def convert_asset_urls(html_str):
    """Replaces src='assets/...' or src='assets/products/...' with Shopify Liquid {{ 'filename' | asset_url }}"""
    # Replace assets/products/FILENAME
    html_str = re.sub(
        r'src="assets/products/([^"]+)"',
        r'src="{{ \'\1\' | asset_url }}"',
        html_str
    )
    # Replace assets/FILENAME
    html_str = re.sub(
        r'src="assets/([^"]+)"',
        r'src="{{ \'\1\' | asset_url }}"',
        html_str
    )
    # Replace href="assets/FILENAME"
    html_str = re.sub(
        r'href="assets/([^"]+)"',
        r'href="{{ \'\1\' | asset_url }}"',
        html_str
    )
    # Replace poster="assets/products/FILENAME"
    html_str = re.sub(
        r'poster="assets/products/([^"]+)"',
        r'poster="{{ \'\1\' | asset_url }}"',
        html_str
    )
    # Replace poster="assets/FILENAME"
    html_str = re.sub(
        r'poster="assets/([^"]+)"',
        r'poster="{{ \'\1\' | asset_url }}"',
        html_str
    )
    return html_str

def generate_config():
    schema = [
        {
            "name": "theme_info",
            "theme_name": "Graffeine Tales Atelier",
            "theme_version": "2.0.0",
            "theme_author": "Graffeine Tales Studio",
            "theme_documentation_url": "https://graffeinetales.com",
            "theme_support_url": "mailto:hello@graffeinetales.com"
        },
        {
            "name": "Colors & Aesthetics",
            "settings": [
                {
                    "type": "color",
                    "id": "color_primary",
                    "label": "Primary Brand Color (Warm Saddle)",
                    "default": "#5A3825"
                },
                {
                    "type": "color",
                    "id": "color_accent_clay",
                    "label": "Terracotta Clay Accent",
                    "default": "#C85A32"
                },
                {
                    "type": "color",
                    "id": "color_bg_cream",
                    "label": "Atelier Cream Background",
                    "default": "#FDFBF7"
                },
                {
                    "type": "color",
                    "id": "color_text_dark",
                    "label": "Espresso Dark Text",
                    "default": "#363638"
                }
            ]
        },
        {
            "name": "Shipping & Checkout",
            "settings": [
                {
                    "type": "number",
                    "id": "free_shipping_threshold",
                    "label": "Free Shipping Threshold (in store currency)",
                    "default": 1499
                },
                {
                    "type": "text",
                    "id": "shipping_promo_text",
                    "label": "Free Shipping Announcement",
                    "default": "Add ₹{remaining} more for FREE Studio Courier Shipping"
                }
            ]
        },
        {
            "name": "Social Media",
            "settings": [
                {
                    "type": "text",
                    "id": "social_instagram",
                    "label": "Instagram Handle or URL",
                    "default": "https://instagram.com/graffeinetales"
                },
                {
                    "type": "text",
                    "id": "social_pinterest",
                    "label": "Pinterest URL",
                    "default": "https://pinterest.com/graffeinetales"
                },
                {
                    "type": "text",
                    "id": "concierge_email",
                    "label": "Studio Concierge Email",
                    "default": "hello@graffeinetales.com"
                }
            ]
        }
    ]
    with open(os.path.join(THEME_DIR, "config", "settings_schema.json"), "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)

    settings_data = {
        "current": {
            "color_primary": "#5A3825",
            "color_accent_clay": "#C85A32",
            "color_bg_cream": "#FDFBF7",
            "color_text_dark": "#363638",
            "free_shipping_threshold": 1499,
            "shipping_promo_text": "Add ₹{remaining} more for FREE Studio Courier Shipping",
            "social_instagram": "https://instagram.com/graffeinetales",
            "social_pinterest": "https://pinterest.com/graffeinetales",
            "concierge_email": "hello@graffeinetales.com"
        }
    }
    with open(os.path.join(THEME_DIR, "config", "settings_data.json"), "w", encoding="utf-8") as f:
        json.dump(settings_data, f, indent=2)

    print("Generated config/settings_schema.json and config/settings_data.json")

def generate_locales():
    locales = {
        "general": {
            "search": "Search handcrafted editions...",
            "cart": "Shopping Bag",
            "checkout": "Checkout Securely",
            "free_shipping": "Free Studio Courier Shipping",
            "add_to_cart": "Add to Bag",
            "quick_view": "Quick View",
            "bestseller": "Bestseller",
            "subtotal": "Subtotal",
            "taxes_shipping_at_checkout": "Taxes and shipping calculated at checkout. Handcrafted packaging included."
        },
        "products": {
            "product": {
                "regular_price": "Regular price",
                "sale_price": "Sale price",
                "add_to_cart": "Add to Bag",
                "sold_out": "Sold Out",
                "unavailable": "Unavailable",
                "quantity": "Quantity"
            }
        }
    }
    with open(os.path.join(THEME_DIR, "locales", "en.default.json"), "w", encoding="utf-8") as f:
        json.dump(locales, f, indent=2)
    print("Generated locales/en.default.json")

def generate_layout():
    theme_liquid = """<!DOCTYPE html>
<html lang="{{ request.locale.iso_code }}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>
    {{ page_title }}
    {%- if current_tags %} &ndash; tagged "{{ current_tags | join: ', ' }}"{% endif -%}
    {%- if current_page != 1 %} &ndash; Page {{ current_page }}{% endif -%}
    {%- unless page_title contains shop.name %} &ndash; {{ shop.name }}{% endunless -%}
  </title>

  {% if page_description %}
    <meta name="description" content="{{ page_description | escape }}" />
  {% else %}
    <meta name="description" content="Discover tactile stationery, handcrafted journals, artisan decor and bespoke gifting by Graffeine Tales. Designer's eye. Artist's hands. Storyteller's imagination." />
  {% endif %}

  <!-- Favicon / Coffee Cup -->
  <link rel="icon" type="image/png" href="{{ 'coffee_cup.png' | asset_url }}" />
  <link rel="canonical" href="{{ canonical_url }}" />

  <!-- Google Fonts: Brand Typography System -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&family=Patrick+Hand&family=Playfair+Display:ital,wght@0;400;600;1,400&family=Quicksand:wght@500;600;700&display=swap" rel="stylesheet" />

  <!-- Main Theme Stylesheet -->
  {{ 'styles.css' | asset_url | stylesheet_tag }}

  <!-- Required Shopify Header Hook -->
  {{ content_for_header }}

  <!-- Shopify Theme Environment Bridge -->
  <script>
    window.ShopifyTheme = {
      rootUrl: {{ routes.root_url | json }},
      cartUrl: {{ routes.cart_url | json }},
      cartAddUrl: {{ routes.cart_add_url | json }},
      cartChangeUrl: {{ routes.cart_change_url | json }},
      cartClearUrl: {{ routes.cart_clear_url | json }},
      currency: {{ cart.currency.symbol | default: '₹' | json }},
      freeShippingThreshold: {{ settings.free_shipping_threshold | default: 1499 }},
      assetUrl: {{ 'coffee_cup.png' | asset_url | split: 'coffee_cup.png' | first | json }}
    };
  </script>
</head>
<body class="template-{{ template.name | default: 'index' }}">

  <!-- Sticky & Mega-Menu Header -->
  {% section 'header' %}

  <!-- Main Content Body -->
  <main id="MainContent" role="main" tabindex="-1">
    {{ content_for_layout }}
  </main>

  <!-- Artisanal Footer -->
  {% section 'footer' %}

  <!-- Global Slide-Over Drawers & Modals -->
  {% section 'cart-drawer' %}
  {% section 'search-modal' %}
  {% section 'wishlist-drawer' %}
  {% section 'quick-view-modal' %}
  {% section 'mobile-nav' %}
  {% section 'mobile-bottom-nav' %}
  {% section 'account-modal' %}
  {% section 'story-modal' %}
  {% section 'reel-viewer-modal' %}
  {% section 'reel-ingest-modal' %}

  <!-- Core Scripts -->
  <script src="{{ 'app.js' | asset_url }}" defer></script>
  <script src="{{ 'shopify-cart.js' | asset_url }}" defer></script>
</body>
</html>
"""
    with open(os.path.join(THEME_DIR, "layout", "theme.liquid"), "w", encoding="utf-8") as f:
        f.write(theme_liquid)
    print("Generated layout/theme.liquid")

def extract_sections():
    with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    section_specs = [
        ("header", r'(<header class="site-header"[^>]*>.*?</header>)', "Header & Mega Navigation", False),
        ("hero-carousel", r'(<section class="hero-carousel-section"[^>]*>.*?</section>)', "Hero Banner Showcase", True),
        ("categories-grid", r'(<section class="section-padding categories-section"[^>]*>.*?</section>)', "Shop by Category Grid", True),
        ("new-launch", r'(<section class="section-padding new-launch-section"[^>]*>.*?</section>)', "New Launch & Studio Drops", True),
        ("bestsellers", r'(<section class="section-padding bestsellers-section"[^>]*>.*?</section>)', "Bestsellers Collection", True),
        ("built-with-heart", r'(<section class="section-padding built-with-heart-section"[^>]*>.*?</section>)', "Built with Heart Editions", True),
        ("catalogue", r'(<section class="section-padding catalogue-section"[^>]*>.*?</section>)', "Complete Catalogue Grid", True),
        ("about-story", r'(<section class="about-story-section"[^>]*>.*?</section>)', "Our Story & Atelier Philosophy", True),
        ("stories-reels", r'(<section class="video-commerce-section"[^>]*>.*?</section>)', "Stories in Motion (Shoppable Video Reels)", True),
        ("reviews", r'(<section class="section-padding reviews-section"[^>]*>.*?</section>)', "Client Reviews & Social Proof", True),
        ("footer", r'(<footer class="site-footer"[^>]*>.*?</footer>)', "Artisanal Footer", False),
        ("cart-drawer", r'(<div class="cart-drawer-overlay"[^>]*>.*?</div>\s*</div>)', "Slide-Over Cart Drawer", False),
        ("search-modal", r'(<div class="search-modal-overlay"[^>]*>.*?</div>\s*</div>)', "Instant Search Modal", False),
        ("wishlist-drawer", r'(<div class="wishlist-drawer-overlay"[^>]*>.*?</div>\s*</div>)', "Wishlist Drawer", False),
        ("quick-view-modal", r'(<div class="modal-overlay" id="quick-view-modal"[^>]*>.*?</div>\s*</div>\s*</div>)', "Product Quick View Modal", False),
        ("mobile-nav", r'(<div class="mobile-drawer-overlay"[^>]*>.*?</div>\s*</div>\s*</div>)', "Mobile Navigation Drawer", False),
        ("mobile-bottom-nav", r'(<nav class="mobile-bottom-nav"[^>]*>.*?</nav>)', "Mobile Glassmorphism Bottom Bar", False),
        ("account-modal", r'(<div class="account-modal-overlay"[^>]*>.*?</div>\s*</div>\s*</div>)', "Atelier My Account Modal", False),
        ("story-modal", r'(<div class="story-modal-overlay"[^>]*>.*?</div>\s*</div>\s*</div>)', "Founder & Atelier Story Modal", False),
        ("reel-viewer-modal", r'(<div class="reel-viewer-overlay"[^>]*>.*?</div>\s*</div>\s*</div>)', "Shoppable Reels 9:16 Theater Modal", False),
        ("reel-ingest-modal", r'(<div class="reel-ingest-overlay"[^>]*>.*?</div>\s*</div>\s*</div>)', "Dual Reel Ingestion Modal", False),
    ]

    for filename, pattern, name_title, has_preset in section_specs:
        m = re.search(pattern, html, re.DOTALL)
        if not m:
            print(f"Warning: Could not match {filename}")
            continue
        
        raw_markup = m.group(1)
        converted_markup = convert_asset_urls(raw_markup)

        # For cart drawer, replace alert with real Shopify checkout button
        if filename == "cart-drawer":
            converted_markup = re.sub(
                r'<button class="checkout-btn" onclick="alert\([^)]+\)">',
                r'<a href="{{ routes.cart_url | default: "/cart" }}/checkout" class="checkout-btn" style="text-decoration:none; display:flex; justify-content:center; align-items:center;">',
                converted_markup
            )
            converted_markup = converted_markup.replace('</button>\n      </div>\n\n    </div>', '</a>\n      </div>\n\n    </div>')

        schema_dict = {
            "name": name_title,
            "settings": []
        }
        if has_preset:
            schema_dict["presets"] = [
                {
                    "name": name_title
                }
            ]

        liquid_file_content = f"{converted_markup}\n\n{{% schema %}}\n{json.dumps(schema_dict, indent=2)}\n{{% endschema %}}\n"
        
        out_path = os.path.join(THEME_DIR, "sections", f"{filename}.liquid")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(liquid_file_content)

    print(f"Extracted and generated {len(section_specs)} sections.")

def generate_dedicated_sections():
    # 1. main-product.liquid
    main_product_liquid = """<section class="section-padding main-product-section" id="MainProduct-{{ product.id }}">
  <div class="container product-page-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 48px; align-items: start; max-width: 1200px; margin: 40px auto; padding: 0 20px;">
    
    <!-- Product Gallery -->
    <div class="product-gallery" style="position: sticky; top: 100px;">
      <div class="main-image-wrap" style="border-radius: 16px; overflow: hidden; background: #F8F5F0; box-shadow: 0 10px 30px rgba(90,56,37,0.08); border: 1px solid rgba(90,56,37,0.1);">
        <img id="MainProductImage" 
             src="{{ product.featured_image | img_url: '1000x' }}" 
             alt="{{ product.title | escape }}" 
             style="width: 100%; height: auto; aspect-ratio: 1/1; object-fit: cover; display: block;" />
      </div>
      
      {% if product.images.size > 1 %}
        <div class="product-thumbnails" style="display: flex; gap: 12px; margin-top: 16px; overflow-x: auto; padding-bottom: 8px;">
          {% for img in product.images %}
            <button type="button" 
                    onclick="document.getElementById('MainProductImage').src='{{ img | img_url: '1000x' }}'"
                    style="border: 2px solid {% if forloop.first %}var(--c-primary, #5A3825){% else %}transparent{% endif %}; border-radius: 8px; overflow: hidden; padding: 0; background: none; cursor: pointer; flex-shrink: 0; width: 72px; height: 72px;">
              <img src="{{ img | img_url: '150x' }}" alt="{{ product.title | escape }}" style="width: 100%; height: 100%; object-fit: cover;" />
            </button>
          {% endfor %}
        </div>
      {% endif %}
    </div>

    <!-- Product Info & Buying Actions -->
    <div class="product-info-wrap">
      <span class="product-collection-tag" style="font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--c-accent, #C85A32);">
        {{ product.type | default: 'Atelier Original Edition' }}
      </span>

      <h1 class="product-title" style="font-family: var(--font-display, 'DM Serif Display', serif); font-size: clamp(2rem, 3.5vw, 2.75rem); color: var(--c-primary, #5A3825); margin: 12px 0 16px; line-height: 1.15;">
        {{ product.title }}
      </h1>

      <!-- Ratings & Reviews Badge -->
      <div class="product-meta-row" style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
        <div class="stars-gold" style="color: #D4AF37; font-size: 1.1rem; letter-spacing: 2px;">★★★★★</div>
        <span style="font-size: 0.9rem; color: #7A6B63; font-weight: 500;">5.0 (214 verified atelier patrons)</span>
      </div>

      <!-- Pricing Row -->
      <div class="product-price-row" style="display: flex; align-items: baseline; gap: 16px; margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid rgba(90,56,37,0.12);">
        <span class="current-price" style="font-size: 2rem; font-weight: 700; color: var(--c-primary, #5A3825); font-family: var(--font-display, 'DM Serif Display', serif);">
          {{ product.price | money }}
        </span>
        {% if product.compare_at_price > product.price %}
          <span class="compare-price" style="font-size: 1.15rem; text-decoration: line-through; color: #9E938A;">
            {{ product.compare_at_price | money }}
          </span>
          <span class="save-tag" style="background: rgba(200,90,50,0.1); color: #C85A32; font-weight: 700; font-size: 0.85rem; padding: 4px 10px; border-radius: 999px;">
            Save {{ product.compare_at_price | minus: product.price | money }}
          </span>
        {% endif %}
      </div>

      <!-- Product Form -->
      {% form 'product', product, id: 'main-product-form' %}
        <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}" />

        {% if product.variants.size > 1 %}
          <div class="variants-picker" style="margin-bottom: 24px;">
            <label style="display: block; font-weight: 600; margin-bottom: 8px; color: #363638;">Select Edition / Variant:</label>
            <select name="id" class="edition-select" style="width: 100%; padding: 12px 16px; border-radius: 10px; border: 1.5px solid rgba(90,56,37,0.2); font-family: inherit; font-size: 1rem; background: #FFF;">
              {% for variant in product.variants %}
                <option value="{{ variant.id }}" {% if variant == product.selected_or_first_available_variant %}selected{% endif %} {% unless variant.available %}disabled{% endunless %}>
                  {{ variant.title }} — {{ variant.price | money }} {% unless variant.available %}(Sold Out){% endunless %}
                </option>
              {% endfor %}
            </select>
          </div>
        {% endif %}

        <!-- Quantity & Add to Cart Row -->
        <div class="actions-row" style="display: flex; gap: 16px; margin-bottom: 20px;">
          <div class="qty-stepper-wrap" style="display: flex; align-items: center; border: 1.5px solid rgba(90,56,37,0.2); border-radius: 999px; padding: 4px; background: #FFF;">
            <button type="button" onclick="const q=document.getElementById('product-qty'); if(q.value>1)q.value--;" style="width: 36px; height: 36px; border: none; background: none; font-size: 1.2rem; cursor: pointer;">−</button>
            <input type="number" id="product-qty" name="quantity" value="1" min="1" style="width: 44px; text-align: center; border: none; font-weight: 600; font-size: 1rem;" />
            <button type="button" onclick="const q=document.getElementById('product-qty'); q.value++;" style="width: 36px; height: 36px; border: none; background: none; font-size: 1.2rem; cursor: pointer;">+</button>
          </div>

          <button type="submit" 
                  name="add" 
                  class="btn btn-primary" 
                  style="flex: 1; padding: 16px 28px; border-radius: 999px; background: var(--c-primary, #5A3825); color: #FFF; font-weight: 600; font-size: 1.05rem; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; transition: transform 0.2s, background 0.2s;"
                  {% unless product.available %}disabled{% endunless %}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
            <span>{% if product.available %}Add to Atelier Bag{% else %}Sold Out{% endif %}</span>
          </button>
        </div>

        <!-- Dynamic Buy Button (UPI / Shop Pay / Cards) -->
        <div class="dynamic-checkout-wrap" style="margin-bottom: 28px;">
          {{ form | payment_button }}
        </div>
      {% endform %}

      <!-- Atelier Trust Markers -->
      <div class="atelier-trust-box" style="background: rgba(90,56,37,0.04); border: 1px dashed rgba(90,56,37,0.2); border-radius: 12px; padding: 16px 20px; margin-bottom: 30px;">
        <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 10px;">
          <span style="font-size: 1.2rem;">✨</span>
          <span style="font-size: 0.9rem; color: #4A3A31;"><strong>Handcrafted in Atelier:</strong> Every piece is individually hand-finished and inspected.</span>
        </div>
        <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 10px;">
          <span style="font-size: 1.2rem;">🚚</span>
          <span style="font-size: 0.9rem; color: #4A3A31;"><strong>Pan-India Express:</strong> Dispatched in 24–48 hours via Bluedart/Delhivery.</span>
        </div>
        <div style="display: flex; gap: 12px; align-items: center;">
          <span style="font-size: 1.2rem;">🎁</span>
          <span style="font-size: 0.9rem; color: #4A3A31;"><strong>Gift-Ready Packaging:</strong> Wrapped in sustainable kraft sleeve with wax seal emblem.</span>
        </div>
      </div>

      <!-- Product Description & Story -->
      <div class="product-description-content" style="color: #4A3A31; line-height: 1.7; font-size: 1.025rem;">
        {{ product.description }}
      </div>

    </div>
  </div>
</section>

{% schema %}
{
  "name": "Product Main Section",
  "settings": []
}
{% endschema %}
"""
    with open(os.path.join(THEME_DIR, "sections", "main-product.liquid"), "w", encoding="utf-8") as f:
        f.write(main_product_liquid)

    # 2. main-collection.liquid
    main_collection_liquid = """<section class="section-padding main-collection-section">
  <div class="container">
    <div class="collection-header" style="text-align: center; max-width: 800px; margin: 40px auto 48px;">
      <span class="sub-heading" style="color: var(--c-accent, #C85A32); font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.85rem;">Atelier Curated Edition</span>
      <h1 class="section-title" style="font-family: var(--font-display, 'DM Serif Display', serif); font-size: clamp(2.2rem, 4vw, 3.2rem); color: var(--c-primary, #5A3825); margin: 12px 0;">
        {{ collection.title }}
      </h1>
      {% if collection.description != blank %}
        <p class="collection-desc" style="color: #6E625A; font-size: 1.1rem; line-height: 1.6;">
          {{ collection.description }}
        </p>
      {% endif %}
    </div>

    <!-- Product Grid -->
    <div class="catalogue-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 32px;">
      {% for product in collection.products %}
        {% render 'product-card', product: product %}
      {% else %}
        <div class="empty-collection" style="grid-column: 1 / -1; text-align: center; padding: 60px 20px;">
          <p style="font-size: 1.2rem; color: #7A6B63;">No editions found in this curated collection.</p>
          <a href="{{ routes.all_products_collection_url }}" class="btn btn-primary" style="margin-top: 20px; display: inline-block;">Explore All Editions</a>
        </div>
      {% endfor %}
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Collection Page",
  "settings": []
}
{% endschema %}
"""
    with open(os.path.join(THEME_DIR, "sections", "main-collection.liquid"), "w", encoding="utf-8") as f:
        f.write(main_collection_liquid)

    # 3. main-page.liquid
    main_page_liquid = """<section class="section-padding main-page-section">
  <div class="container" style="max-width: 900px; margin: 50px auto; padding: 0 24px;">
    <h1 style="font-family: var(--font-display, 'DM Serif Display', serif); font-size: 2.8rem; color: var(--c-primary, #5A3825); margin-bottom: 24px;">
      {{ page.title }}
    </h1>
    <div class="page-content" style="line-height: 1.8; color: #4A3A31; font-size: 1.05rem;">
      {{ page.content }}
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Standard Page",
  "settings": []
}
{% endschema %}
"""
    with open(os.path.join(THEME_DIR, "sections", "main-page.liquid"), "w", encoding="utf-8") as f:
        f.write(main_page_liquid)

    # 4. main-cart.liquid
    main_cart_liquid = """<section class="section-padding main-cart-section">
  <div class="container" style="max-width: 900px; margin: 40px auto; padding: 0 20px;">
    <h1 style="font-family: var(--font-display, 'DM Serif Display', serif); font-size: 2.8rem; color: var(--c-primary, #5A3825); margin-bottom: 24px; text-align: center;">
      Your Atelier Shopping Bag
    </h1>

    {% if cart.item_count > 0 %}
      <form action="{{ routes.cart_url }}" method="post" id="cart">
        <div class="cart-table" style="margin-bottom: 30px;">
          {% for item in cart.items %}
            <div class="cart-item-row" style="display: flex; gap: 20px; align-items: center; padding: 20px 0; border-bottom: 1px solid rgba(90,56,37,0.12);">
              <img src="{{ item.image | img_url: '160x' }}" alt="{{ item.title | escape }}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 12px;" />
              <div style="flex: 1;">
                <h3 style="font-size: 1.1rem; margin: 0 0 6px; color: #363638;"><a href="{{ item.url }}" style="color: inherit; text-decoration: none;">{{ item.product.title }}</a></h3>
                <span style="font-size: 0.85rem; color: #8A7B72;">{{ item.variant.title }}</span>
                <div style="margin-top: 8px; font-weight: 600; color: #5A3825;">{{ item.final_line_price | money }}</div>
              </div>
              <div style="display: flex; align-items: center; gap: 8px;">
                <a href="{{ routes.cart_change_url }}?line={{ forloop.index }}&quantity=0" style="color: #C85A32; font-size: 0.85rem; text-decoration: none;">Remove</a>
              </div>
            </div>
          {% endfor %}
        </div>

        <div class="cart-summary-box" style="text-align: right; background: #F8F5F0; padding: 28px; border-radius: 16px;">
          <div style="font-size: 1.3rem; font-weight: 600; margin-bottom: 10px;">Subtotal: {{ cart.total_price | money }}</div>
          <p style="font-size: 0.85rem; color: #8A7B72; margin-bottom: 20px;">Taxes and shipping calculated at checkout.</p>
          <button type="submit" name="checkout" class="btn btn-primary" style="padding: 16px 36px; font-size: 1.1rem; border-radius: 999px; background: #5A3825; color: #FFF; border: none; cursor: pointer;">
            Proceed to Checkout Securely
          </button>
        </div>
      </form>
    {% else %}
      <div style="text-align: center; padding: 60px 20px;">
        <p style="font-size: 1.25rem; color: #7A6B63; margin-bottom: 24px;">Your bag is currently empty.</p>
        <a href="{{ routes.all_products_collection_url }}" class="btn btn-primary" style="display: inline-block; padding: 14px 28px; border-radius: 999px; background: #5A3825; color: #FFF; text-decoration: none;">Explore Atelier Editions</a>
      </div>
    {% endif %}
  </div>
</section>

{% schema %}
{
  "name": "Cart Page",
  "settings": []
}
{% endschema %}
"""
    with open(os.path.join(THEME_DIR, "sections", "main-cart.liquid"), "w", encoding="utf-8") as f:
        f.write(main_cart_liquid)

    # 5. main-404.liquid
    main_404_liquid = """<section class="section-padding 404-section" style="text-align: center; padding: 100px 20px;">
  <div class="container" style="max-width: 600px; margin: 0 auto;">
    <span style="font-size: 4rem;">☕</span>
    <h1 style="font-family: var(--font-display, 'DM Serif Display', serif); font-size: 3rem; color: var(--c-primary, #5A3825); margin: 16px 0;">Story Not Found</h1>
    <p style="color: #6E625A; font-size: 1.1rem; margin-bottom: 30px;">The page or edition you are looking for has been moved or crafted into another tale.</p>
    <a href="{{ routes.root_url }}" class="btn btn-primary" style="display: inline-block; padding: 14px 30px; border-radius: 999px; background: #5A3825; color: #FFF; text-decoration: none; font-weight: 600;">Return to Atelier Home</a>
  </div>
</section>

{% schema %}
{
  "name": "404 Page",
  "settings": []
}
{% endschema %}
"""
    with open(os.path.join(THEME_DIR, "sections", "main-404.liquid"), "w", encoding="utf-8") as f:
        f.write(main_404_liquid)

    # 6. main-journal-pdp.liquid (Dedicated Luxury Journal PDP)
    main_journal_liquid = """{% comment %}
  Graffeine Tales — Journal & Diaries Luxury PDP Section (Shopify OS 2.0)
{% endcomment %}
<div class="journal-pdp-wrapper bg-[#F8F5ED] text-[#363638] antialiased">
  <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 text-xs text-[#363638]/60 flex items-center gap-2" aria-label="Breadcrumb">
    <a href="{{ routes.root_url }}" class="hover:text-[#4D351D] transition-colors">Home</a>
    <span>&rsaquo;</span>
    <a href="{{ routes.all_products_collection_url }}" class="hover:text-[#4D351D] transition-colors">Stationaries</a>
    <span>&rsaquo;</span>
    <span class="text-[#363638] font-medium truncate">{{ product.title | default: 'The 2027 Bound Chronicle &amp; Daily Journal' }}</span>
  </nav>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 lg:py-10">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 xl:gap-14 items-start">
      <div class="lg:col-span-7 space-y-4 lg:sticky lg:top-28">
        <div class="relative bg-[#EFE9DC] rounded-2xl overflow-hidden border border-[#C6B58E]/40 shadow-tactile aspect-square flex items-center justify-center">
          <div class="absolute top-4 left-4 z-10 flex flex-wrap gap-2">
            <span class="bg-[#363638] text-[#E9DFC2] text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm">✦ Handmade Touch</span>
            <span class="bg-[#2D6A4F] text-white text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm">100 GSM Natural Paper</span>
            <span class="bg-[#D4AF37] text-[#363638] text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm">Free Sticker Book</span>
          </div>
          <img id="main-product-img" src="{{ product.featured_image | default: 'prod_journal.jpg' | asset_url }}" alt="{{ product.title | escape }}" class="w-full h-full object-cover" />
        </div>
      </div>

      <div class="lg:col-span-5 bg-white/95 rounded-3xl p-6 sm:p-8 border border-[#C6B58E]/40 shadow-tactile-lg space-y-6">
        <div>
          <span class="text-xs uppercase font-bold tracking-[0.15em] text-[#927B53] bg-[#F8F5ED] px-3 py-1 rounded-full border border-[#C6B58E]/30 inline-block mb-3">{{ product.type | default: 'Stationaries • Journals &amp; Diaries' }}</span>
          <h1 class="font-serif-display text-3xl sm:text-4xl text-[#363638] leading-tight">{{ product.title | default: 'The 2027 Bound Chronicle &amp; Daily Journal' }}</h1>
          <div class="flex items-center gap-2 mt-2">
            <span class="text-[#D4AF37]">★★★★★</span>
            <span class="text-xs font-semibold text-[#363638]/70">5.0 (328 verified patrons)</span>
          </div>
        </div>

        <div class="py-4 border-y border-[#C6B58E]/30 flex items-baseline justify-between">
          <div>
            <div class="flex items-baseline gap-3">
              <span class="font-serif-display text-3xl sm:text-4xl font-bold text-[#4D351D]">{{ product.price | money | default: '₹1,299' }}</span>
              <span class="text-base text-[#363638]/40 line-through">₹1,699</span>
              <span class="bg-[#C85A32]/10 text-[#C85A32] text-xs font-bold px-2.5 py-0.5 rounded-full">SAVE 24%</span>
            </div>
            <p class="text-xs text-[#363638]/60 mt-1">Inclusive of all domestic taxes &bull; Custom kraft box included</p>
          </div>
        </div>

        {% form 'product', product, id: 'journal-pdp-form' %}
          <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}" />
          <div class="flex items-center gap-3 mb-4">
            <button type="submit" name="add" class="flex-1 bg-[#4D351D] hover:bg-[#363638] text-[#E9DFC2] py-4 px-6 rounded-full font-bold text-sm tracking-wide flex items-center justify-center gap-3 shadow-tactile transition-all">
              <span>Add to Atelier Bag</span>
            </button>
          </div>
          <div>{{ form | payment_button }}</div>
        {% endform %}

        <!-- Editorial Lead Pitch Paragraph (Inspired by Alicia Souza PDP Structure) -->
        <p class="text-xs sm:text-sm text-[#363638]/80 leading-relaxed font-normal pt-4 border-t border-[#C6B58E]/40">
          <strong class="text-[#363638] font-semibold">Plan every day with ease using our 2027 Daily Planner!</strong> Featuring a daily layout, along with monthly grids, and a habit tracker which helps you stay organized and on top of your goals. The premium printed bookcloth cover with metallic gold foiling adds a touch of luxury, making it perfect for work, studio, or personal planning. Durable, stylish, and thoughtfully designed &ndash; your must-have planner for 2027!
        </p>

        <!-- Dropdown Accordion Stack -->
        <div class="border-t border-[#C6B58E]/40 divide-y divide-[#C6B58E]/40" id="shopify-journal-accordion">
          <!-- 1. What's Inside? -->
          <div class="accordion-item">
            <button type="button" class="w-full py-4 text-left flex items-center justify-between text-sm sm:text-base font-semibold text-[#363638] hover:text-[#4D351D] transition-colors group" onclick="toggleDetailsAccordion(this)">
              <span>What’s Inside?</span>
              <svg class="w-4 h-4 text-[#927B53] transition-transform duration-300 group-hover:text-[#4D351D] chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 9-7 7-7-7"/></svg>
            </button>
            <div class="accordion-panel max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
              <div class="pb-5 pt-1 text-xs text-[#363638]/80 space-y-2 leading-relaxed">
                <ul class="space-y-2 pl-1">
                  <li class="flex items-start gap-2"><span class="text-[#4D351D] font-bold">✦</span><span><strong>1x The 2027 Bound Chronicle Hardcover Planner</strong> (A5 / 224 Numbered Ivory Pages)</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#4D351D] font-bold">✦</span><span><strong>4x Complimentary Gilded Planning Sticker Sheets</strong> (Over 180+ die-cut stickers)</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#4D351D] font-bold">✦</span><span><strong>1x Companion A6 Pocket Notes Booklet</strong> (32 pages, saddle-stitched for on-the-go ideas)</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#4D351D] font-bold">✦</span><span><strong>1x Linen-Reinforced Expandable Memory Pocket</strong> in the rear cover</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#4D351D] font-bold">✦</span><span><strong>2x Woven Silk Ribbon Markers</strong> (Espresso Charcoal &amp; Golden Sand)</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#4D351D] font-bold">✦</span><span><strong>1x Sustainable Kraft Keepsake Gift Box</strong> with metallic gold wax seal emblem</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- 2. Product Features -->
          <div class="accordion-item">
            <button type="button" class="w-full py-4 text-left flex items-center justify-between text-sm sm:text-base font-semibold text-[#363638] hover:text-[#4D351D] transition-colors group" onclick="toggleDetailsAccordion(this)">
              <span>Product Features</span>
              <svg class="w-4 h-4 text-[#927B53] transition-transform duration-300 group-hover:text-[#4D351D] chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 9-7 7-7-7"/></svg>
            </button>
            <div class="accordion-panel max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
              <div class="pb-5 pt-1 text-xs text-[#363638]/80 space-y-2.5 leading-relaxed">
                <div class="grid grid-cols-2 gap-2 text-xs">
                  <div class="p-2.5 bg-[#F8F5ED] rounded-lg border border-[#C6B58E]/30">
                    <span class="text-[10px] uppercase font-bold text-[#927B53] block">Paper Stock</span>
                    <strong class="text-[#363638]">100 GSM Natural Paper</strong>
                    <p class="text-[11px] text-[#363638]/70 mt-0.5">Bleed-proof bamboo-cotton, fountain-pen safe.</p>
                  </div>
                  <div class="p-2.5 bg-[#F8F5ED] rounded-lg border border-[#C6B58E]/30">
                    <span class="text-[10px] uppercase font-bold text-[#927B53] block">Binding</span>
                    <strong class="text-[#363638]">180° Smyth Sewn</strong>
                    <p class="text-[11px] text-[#363638]/70 mt-0.5">True lay-flat binding with reinforced cloth spine.</p>
                  </div>
                  <div class="p-2.5 bg-[#F8F5ED] rounded-lg border border-[#C6B58E]/30">
                    <span class="text-[10px] uppercase font-bold text-[#927B53] block">Size &amp; Pages</span>
                    <strong class="text-[#363638]">A5 (148 x 210 mm)</strong>
                    <p class="text-[11px] text-[#363638]/70 mt-0.5">224 numbered ivory pages, 520 grams.</p>
                  </div>
                  <div class="p-2.5 bg-[#F8F5ED] rounded-lg border border-[#C6B58E]/30">
                    <span class="text-[10px] uppercase font-bold text-[#927B53] block">Cover Finish</span>
                    <strong class="text-[#363638]">Japanese Bookcloth</strong>
                    <p class="text-[11px] text-[#363638]/70 mt-0.5">Tactile textured cloth with gold hot foil stamping.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 3. Planner Layout Includes -->
          <div class="accordion-item">
            <button type="button" class="w-full py-4 text-left flex items-center justify-between text-sm sm:text-base font-semibold text-[#363638] hover:text-[#4D351D] transition-colors group" onclick="toggleDetailsAccordion(this)">
              <span>Planner Layout Includes</span>
              <svg class="w-4 h-4 text-[#927B53] transition-transform duration-300 group-hover:text-[#4D351D] chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 9-7 7-7-7"/></svg>
            </button>
            <div class="accordion-panel max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
              <div class="pb-5 pt-1 text-xs text-[#363638]/80 space-y-2 leading-relaxed">
                <ul class="space-y-1.5 pl-1">
                  <li class="flex items-start gap-2"><span class="text-[#927B53]">✔</span><span><strong>Yearly Life Blueprint &amp; Goals:</strong> 4 pages dedicated to quarterly aspirations and reading lists.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#927B53]">✔</span><span><strong>12 Monthly Panoramic Spreads:</strong> Double-page calendar view with moon phases and budget tracking.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#927B53]">✔</span><span><strong>52 Weekly Focus Dashboards:</strong> Weekday schedule with daily gratitude prompts and habit check-boxes.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#927B53]">✔</span><span><strong>Monthly Habit &amp; Ritual Trackers:</strong> 31-day visual tracking for sleep, hydration, exercise, and reading.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#927B53]">✔</span><span><strong>40 Dot-Grid Ivory Sandbox Pages:</strong> Perforated 5mm dot grid for mindmaps, sketches, and notes.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#927B53]">✔</span><span><strong>Mid-Year Review &amp; Year-End Reflection:</strong> Guided prompts to celebrate growth.</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- 4. Features Of The Sticker Book -->
          <div class="accordion-item">
            <button type="button" class="w-full py-4 text-left flex items-center justify-between text-sm sm:text-base font-semibold text-[#363638] hover:text-[#4D351D] transition-colors group" onclick="toggleDetailsAccordion(this)">
              <span>Features Of The Sticker Book</span>
              <svg class="w-4 h-4 text-[#927B53] transition-transform duration-300 group-hover:text-[#4D351D] chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 9-7 7-7-7"/></svg>
            </button>
            <div class="accordion-panel max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
              <div class="pb-5 pt-1 text-xs text-[#363638]/80 space-y-2 leading-relaxed">
                <p class="font-medium text-[#363638]">Includes 4 full sheets with over 180+ die-cut matte planning stickers:</p>
                <ul class="space-y-1.5 pl-1">
                  <li class="flex items-start gap-2"><span class="text-[#D4AF37]">✦</span><span><strong>Sheet 1 (Functional Headers):</strong> Appointments, deadlines, paydays, flights, doctor, self-care.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#D4AF37]">✦</span><span><strong>Sheet 2 (Coffee &amp; Cozy Rituals):</strong> Illustrated mugs, steaming espresso, book stacks, rainy mornings.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#D4AF37]">✦</span><span><strong>Sheet 3 (Gold Foil Washi &amp; Accents):</strong> Metallic gold hot-stamped stars, washi tape ribbons, and flourish borders.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#D4AF37]">✦</span><span><strong>Sheet 4 (12 Monthly Index Tabs):</strong> Laminated index tabs from Jan to Dec to flip between months effortlessly.</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- 5. Features Of The Pocket Planner -->
          <div class="accordion-item">
            <button type="button" class="w-full py-4 text-left flex items-center justify-between text-sm sm:text-base font-semibold text-[#363638] hover:text-[#4D351D] transition-colors group" onclick="toggleDetailsAccordion(this)">
              <span>Features Of The Pocket Planner</span>
              <svg class="w-4 h-4 text-[#927B53] transition-transform duration-300 group-hover:text-[#4D351D] chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 9-7 7-7-7"/></svg>
            </button>
            <div class="accordion-panel max-h-0 overflow-hidden transition-all duration-300 ease-in-out">
              <div class="pb-5 pt-1 text-xs text-[#363638]/80 space-y-2 leading-relaxed">
                <p>A slim companion pocket notebook designed for effortless mobility:</p>
                <ul class="space-y-1.5 pl-1">
                  <li class="flex items-start gap-2"><span class="text-[#4D351D]">▪</span><span><strong>Size:</strong> A6 Slim (105 x 148 mm) &bull; 32 pages saddle-stitched.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#4D351D]">▪</span><span><strong>Layout:</strong> Unruled &amp; dotted micro-spreads for sudden sparks of creativity and cafe notes.</span></li>
                  <li class="flex items-start gap-2"><span class="text-[#4D351D]">▪</span><span><strong>Portability:</strong> Slips into jacket pockets, small clutches, or inside the main journal's back envelope.</span></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- 6. Shipping Timeline (Open by default as in screenshot) -->
          <div class="accordion-item">
            <button type="button" class="w-full py-4 text-left flex items-center justify-between text-sm sm:text-base font-semibold text-[#363638] hover:text-[#4D351D] transition-colors group active-accordion" onclick="toggleDetailsAccordion(this)">
              <span>Shipping Timeline</span>
              <svg class="w-4 h-4 text-[#927B53] transition-transform duration-300 group-hover:text-[#4D351D] chevron rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 9-7 7-7-7"/></svg>
            </button>
            <div class="accordion-panel overflow-hidden transition-all duration-300 ease-in-out" style="max-height: 400px;">
              <div class="pb-5 pt-1 text-xs text-[#363638]/80 space-y-3 leading-relaxed">
                <p class="font-medium text-[#363638]">
                  Handmade &amp; packed with care. Dispatches in 2&ndash;3 working days.
                </p>
                <div class="space-y-2 pl-1 text-[11px]">
                  <div class="flex items-start gap-2">
                    <span class="w-5 h-5 rounded-full bg-[#4D351D] text-[#E9DFC2] flex items-center justify-center text-[10px] font-bold flex-shrink-0 mt-0.5">1</span>
                    <div><strong>Day 1 &ndash; Atelier Inspection:</strong> Hand inspection of paper, ribbons, and spine stitching.</div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="w-5 h-5 rounded-full bg-[#4D351D] text-[#E9DFC2] flex items-center justify-center text-[10px] font-bold flex-shrink-0 mt-0.5">2</span>
                    <div><strong>Day 2 &ndash; Wax Seal Packaging:</strong> Wrapped in archival tissue paper, boxed in recycled kraft with a gold wax seal.</div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="w-5 h-5 rounded-full bg-[#4D351D] text-[#E9DFC2] flex items-center justify-center text-[10px] font-bold flex-shrink-0 mt-0.5">3</span>
                    <div><strong>Days 3-4 &ndash; Express Transit:</strong> Fast domestic air transit via Bluedart / Delhivery Express.</div>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="w-5 h-5 rounded-full bg-[#2D6A4F] text-white flex items-center justify-center text-[10px] font-bold flex-shrink-0 mt-0.5">4</span>
                    <div><strong>Day 5 &ndash; Doorstep Delivery:</strong> Live SMS &amp; WhatsApp tracking provided upon studio dispatch.</div>
                  </div>
                </div>
                <p class="text-[11px] text-[#2D6A4F] font-medium pt-1">✨ 100% plastic-free, recyclable protective honeycomb wrap.</p>
              </div>
            </div>
          </div>
        </div>

        <script>
          function toggleDetailsAccordion(button) {
            var panel = button.nextElementSibling;
            var chevron = button.querySelector('.chevron');
            var isOpen = panel.style.maxHeight && panel.style.maxHeight !== '0px';

            if (isOpen) {
              panel.style.maxHeight = '0px';
              if (chevron) chevron.classList.remove('rotate-180');
              button.classList.remove('active-accordion');
            } else {
              panel.style.maxHeight = panel.scrollHeight + 40 + 'px';
              if (chevron) chevron.classList.add('rotate-180');
              button.classList.add('active-accordion');
            }
          }
        </script>
      </div>
    </div>
  </div>

  <!-- Interactive Flip-Through Stepper (Inspired by Alicia Souza PDP Reference) -->
  <section class="py-16 sm:py-20 bg-white border-t border-[#C6B58E]/30" id="shopify-flip-through-section">
    <div class="max-w-4xl mx-auto px-4 sm:px-6">
      <div class="text-center mb-6">
        <h2 class="font-sans font-bold text-2xl sm:text-3xl text-[#363638] tracking-tight">
          Flip through a few inner pages!
        </h2>
      </div>

      <div class="max-w-xs sm:max-w-sm mx-auto mb-8 relative flex items-center justify-between px-2" id="shopify-flip-stepper">
        <div class="absolute left-2 right-2 top-1/2 -translate-y-1/2 h-[1.5px] bg-[#C6B58E]/40 z-0"></div>
        <button type="button" class="stepper-dot relative z-10 w-6 h-6 flex items-center justify-center bg-white rounded-full transition-transform hover:scale-110" onclick="goToShopifyFlip(0)" aria-label="Page 1">
          <span class="w-4 h-4 rounded-full border-2 border-[#4D351D] bg-white flex items-center justify-center shadow-sm">
            <span class="w-2 h-2 rounded-full bg-[#4D351D]"></span>
          </span>
        </button>
        <button type="button" class="stepper-dot relative z-10 w-6 h-6 flex items-center justify-center bg-white rounded-full transition-transform hover:scale-110" onclick="goToShopifyFlip(1)" aria-label="Page 2">
          <span class="w-2 h-2 rounded-full bg-[#C6B58E]/60 hover:bg-[#4D351D] transition-colors block"></span>
        </button>
        <button type="button" class="stepper-dot relative z-10 w-6 h-6 flex items-center justify-center bg-white rounded-full transition-transform hover:scale-110" onclick="goToShopifyFlip(2)" aria-label="Page 3">
          <span class="w-2 h-2 rounded-full bg-[#C6B58E]/60 hover:bg-[#4D351D] transition-colors block"></span>
        </button>
        <button type="button" class="stepper-dot relative z-10 w-6 h-6 flex items-center justify-center bg-white rounded-full transition-transform hover:scale-110" onclick="goToShopifyFlip(3)" aria-label="Page 4">
          <span class="w-2 h-2 rounded-full bg-[#C6B58E]/60 hover:bg-[#4D351D] transition-colors block"></span>
        </button>
        <button type="button" class="stepper-dot relative z-10 w-6 h-6 flex items-center justify-center bg-white rounded-full transition-transform hover:scale-110" onclick="goToShopifyFlip(4)" aria-label="Page 5">
          <span class="w-2 h-2 rounded-full bg-[#C6B58E]/60 hover:bg-[#4D351D] transition-colors block"></span>
        </button>
      </div>

      <!-- Centered Interactive Book Page Container (Realistic 3D Page Turn Engine) -->
      <div class="relative max-w-[340px] sm:max-w-[400px] mx-auto rounded-2xl shadow-2xl border border-[#C6B58E]/40 bg-[#FAF7F0] overflow-hidden transition-shadow hover:shadow-tactile-lg" id="shopify-flip-wrapper">
        <div id="shopify-page-flip-book" class="w-full flex items-center justify-center min-h-[453px] sm:min-h-[533px]"></div>
      </div>

      <!-- Drag Corner & Tap Hint -->
      <p class="text-[11px] text-[#927B53] font-medium text-center mt-3 flex items-center justify-center gap-1.5 select-none">
        <svg class="w-3.5 h-3.5 text-[#4D351D] opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
        <span><strong>Grab &amp; drag any page corner</strong> to turn the journal page, or use buttons below</span>
      </p>

      <div class="text-center mt-4">
        <p class="text-xs font-semibold text-[#363638]" id="shopify-flip-title">2027 Chronicle Cover &amp; Title Spread</p>
        <p class="text-[11px] text-[#363638]/60 mt-0.5" id="shopify-flip-desc">Artisanal gold debossed cover artwork with gold ribbon marker</p>
      </div>

      <div class="flex items-center justify-center gap-3 mt-6">
        <button type="button" 
                id="shopify-flip-back" 
                onclick="changeShopifyFlip(-1)" 
                class="px-8 py-2.5 border border-[#C6B58E]/40 text-xs font-bold uppercase tracking-widest text-[#363638]/40 bg-white rounded-md transition-all cursor-not-allowed select-none" 
                disabled>
          &lsaquo; Back
        </button>
        
        <button type="button" 
                id="shopify-flip-next" 
                onclick="changeShopifyFlip(1)" 
                class="px-8 py-2.5 border border-[#363638] text-xs font-bold uppercase tracking-widest text-[#363638] bg-white hover:bg-[#363638] hover:text-[#E9DFC2] rounded-md transition-all shadow-sm select-none">
          Next &rsaquo;
        </button>
      </div>
    </div>
  </section>

  <script src="{{ 'page-flip.browser.js' | asset_url }}"></script>
  <script>
    var shopifyFlipPages = [
      { img: "{{ 'flip_cover.jpg' | asset_url }}", title: '2027 Chronicle Cover & Title Spread', desc: 'Artisanal gold debossed cover artwork with woven ribbon bookmark.' },
      { img: "{{ 'flip_monthly.jpg' | asset_url }}", title: 'Monthly Panoramic Overview & Habit Columns', desc: 'Double-page calendar grids with Sunday starts, moon phases, and budget tracking.' },
      { img: "{{ 'flip_weekly.jpg' | asset_url }}", title: '52-Week Focus Dashboard', desc: 'Clean horizontal weekday layout with daily micro-gratitude and task priorities.' },
      { img: "{{ 'flip_habits.jpg' | asset_url }}", title: 'Habit & Wellness Ritual Trackers', desc: '31-day visual micro-grids tracking movement, sleep, hydration, and reading.' },
      { img: "{{ 'flip_stickers.jpg' | asset_url }}", title: 'Dot-Grid Creative Sandbox & Planning Stickers', desc: 'Subtle 5mm ivory dot-grid pages paired with 4 die-cut gilded sticker sheets.' }
    ];
    var currentShopifyFlip = 0;
    var shopifyPageFlip = null;

    function initShopifyPageFlip() {
      var bookEl = document.getElementById('shopify-page-flip-book');
      if (!bookEl || typeof St === 'undefined' || !St.PageFlip) return;

      var container = document.getElementById('shopify-flip-wrapper');
      var baseWidth = container ? Math.min(container.offsetWidth || 380, 400) : 380;
      var baseHeight = Math.round(baseWidth * (4 / 3));

      try {
        shopifyPageFlip = new St.PageFlip(bookEl, {
          width: baseWidth,
          height: baseHeight,
          size: 'fixed',
          minWidth: 260,
          maxWidth: 440,
          minHeight: 347,
          maxHeight: 587,
          maxShadowOpacity: 0.5,
          showCover: false,
          mobileScrollSupport: true,
          usePortrait: true,
          flippingTime: 750,
          drawShadow: true,
          showPageCorners: true,
          useMouseEvents: true,
          disableFlipByClick: false
        });

        shopifyPageFlip.loadFromImages(shopifyFlipPages.map(function(p) { return p.img; }));

        shopifyPageFlip.on('flip', function(e) {
          currentShopifyFlip = e.data;
          updateShopifyFlip(currentShopifyFlip);
        });

        shopifyPageFlip.on('init', function() {
          updateShopifyFlip(0);
        });
      } catch (err) {
        console.warn('Shopify PageFlip init notice:', err);
      }
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initShopifyPageFlip);
    } else {
      initShopifyPageFlip();
    }

    function updateShopifyFlip(index) {
      if (typeof index === 'number') currentShopifyFlip = index;
      var titleEl = document.getElementById('shopify-flip-title');
      var descEl = document.getElementById('shopify-flip-desc');
      var prevBtn = document.getElementById('shopify-flip-back');
      var nextBtn = document.getElementById('shopify-flip-next');
      var dots = document.querySelectorAll('#shopify-flip-stepper .stepper-dot');

      var page = shopifyFlipPages[currentShopifyFlip];
      if (page) {
        if (titleEl) titleEl.innerText = page.title;
        if (descEl) descEl.innerText = page.desc;
      }

      dots.forEach(function(dot, idx) {
        if (idx === currentShopifyFlip) {
          dot.innerHTML = '<span class="w-4 h-4 rounded-full border-2 border-[#4D351D] bg-white flex items-center justify-center shadow-sm"><span class="w-2 h-2 rounded-full bg-[#4D351D]"></span></span>';
        } else {
          dot.innerHTML = '<span class="w-2 h-2 rounded-full bg-[#C6B58E]/60 hover:bg-[#4D351D] transition-colors block"></span>';
        }
      });

      if (prevBtn) {
        if (currentShopifyFlip === 0) {
          prevBtn.disabled = true;
          prevBtn.className = 'px-8 py-2.5 border border-[#C6B58E]/40 text-xs font-bold uppercase tracking-widest text-[#363638]/40 bg-white rounded-md transition-all cursor-not-allowed select-none';
        } else {
          prevBtn.disabled = false;
          prevBtn.className = 'px-8 py-2.5 border border-[#363638] text-xs font-bold uppercase tracking-widest text-[#363638] bg-white hover:bg-[#363638] hover:text-[#E9DFC2] rounded-md transition-all shadow-sm select-none';
        }
      }

      if (nextBtn) {
        if (currentShopifyFlip === shopifyFlipPages.length - 1) {
          nextBtn.disabled = true;
          nextBtn.className = 'px-8 py-2.5 border border-[#C6B58E]/40 text-xs font-bold uppercase tracking-widest text-[#363638]/40 bg-white rounded-md transition-all cursor-not-allowed select-none';
        } else {
          nextBtn.disabled = false;
          nextBtn.className = 'px-8 py-2.5 border border-[#363638] text-xs font-bold uppercase tracking-widest text-[#363638] bg-white hover:bg-[#363638] hover:text-[#E9DFC2] rounded-md transition-all shadow-sm select-none';
        }
      }
    }

    function changeShopifyFlip(delta) {
      if (shopifyPageFlip) {
        if (delta > 0) {
          shopifyPageFlip.flipNext('bottom');
        } else {
          shopifyPageFlip.flipPrev('bottom');
        }
      }
    }

    function goToShopifyFlip(idx) {
      if (shopifyPageFlip) {
        shopifyPageFlip.flip(idx, 'bottom');
      }
    }
  </script>
</div>
{% schema %}
{
  "name": "Journal Luxury PDP",
  "settings": []
}
{% endschema %}
"""
    with open(os.path.join(THEME_DIR, "sections", "main-journal-pdp.liquid"), "w", encoding="utf-8") as f:
        f.write(main_journal_liquid)

    print("Generated dedicated Shopify sections (main-product, main-journal-pdp, main-collection, main-page, main-cart, main-404).")

def generate_snippets():
    # 1. product-card.liquid
    card_liquid = """{% comment %}
  Graffeine Tales — Product Card Snippet
  Accepts:
  - product: Liquid Product object
{% endcomment %}

<div class="product-card" data-product-id="{{ product.id }}">
  <div class="card-media-wrap">
    {% if product.compare_at_price > product.price %}
      <span class="card-badge gold">Sale</span>
    {% elsif product.tags contains 'bestseller' or product.tags contains 'Bestseller' %}
      <span class="card-badge gold">Bestseller</span>
    {% elsif product.tags contains 'new' or product.tags contains 'New' %}
      <span class="card-badge sage">Studio Drop</span>
    {% endif %}

    <a href="{{ product.url }}" class="card-image-link" aria-label="{{ product.title | escape }}">
      <img src="{{ product.featured_image | img_url: '600x' }}" 
           alt="{{ product.title | escape }}" 
           class="card-img" 
           loading="lazy" />
    </a>

    <!-- Quick Action Overlay -->
    <div class="card-actions-overlay">
      <button type="button" 
              class="quick-action-btn" 
              onclick="openQuickView('prod-{{ product.id }}')" 
              title="Quick View">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>
      </button>
      <button type="button" 
              class="quick-action-btn" 
              onclick="toggleWishlist('prod-{{ product.id }}')" 
              title="Save to Wishlist">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
      </button>
    </div>
  </div>

  <div class="card-info">
    <span class="card-cat">{{ product.type | default: 'Stationeries &amp; Décor' }}</span>
    <h3 class="card-title">
      <a href="{{ product.url }}">{{ product.title }}</a>
    </h3>

    <div class="card-pricing">
      <span class="price-val">{{ product.price | money }}</span>
      {% if product.compare_at_price > product.price %}
        <span class="mrp-val">{{ product.compare_at_price | money }}</span>
      {% endif %}
    </div>

    <!-- 1-Tap Add to Bag -->
    <button type="button" 
            class="card-add-btn" 
            onclick="addShopifyItem({{ product.selected_or_first_available_variant.id }}, 1)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
      <span>Add to Bag</span>
    </button>
  </div>
</div>
"""
    with open(os.path.join(THEME_DIR, "snippets", "product-card.liquid"), "w", encoding="utf-8") as f:
        f.write(card_liquid)

    print("Generated snippets/product-card.liquid.")

def generate_templates():
    # 1. index.json
    index_json = {
        "sections": {
            "hero_carousel": {
                "type": "hero-carousel"
            },
            "categories_grid": {
                "type": "categories-grid"
            },
            "new_launch": {
                "type": "new-launch"
            },
            "bestsellers": {
                "type": "bestsellers"
            },
            "built_with_heart": {
                "type": "built-with-heart"
            },
            "catalogue": {
                "type": "catalogue"
            },
            "about_story": {
                "type": "about-story"
            },
            "stories_reels": {
                "type": "stories-reels"
            },
            "reviews": {
                "type": "reviews"
            }
        },
        "order": [
            "hero_carousel",
            "categories_grid",
            "new_launch",
            "bestsellers",
            "built_with_heart",
            "catalogue",
            "about_story",
            "stories_reels",
            "reviews"
        ]
    }
    with open(os.path.join(THEME_DIR, "templates", "index.json"), "w", encoding="utf-8") as f:
        json.dump(index_json, f, indent=2)

    # 2. product.json
    product_json = {
        "sections": {
            "main": {
                "type": "main-product"
            },
            "reviews": {
                "type": "reviews"
            }
        },
        "order": [
            "main",
            "reviews"
        ]
    }
    with open(os.path.join(THEME_DIR, "templates", "product.json"), "w", encoding="utf-8") as f:
        json.dump(product_json, f, indent=2)

    # 2b. product.journal.json (Dedicated Luxury Journal PDP)
    product_journal_json = {
        "sections": {
            "main": {
                "type": "main-journal-pdp"
            }
        },
        "order": [
            "main"
        ]
    }
    with open(os.path.join(THEME_DIR, "templates", "product.journal.json"), "w", encoding="utf-8") as f:
        json.dump(product_journal_json, f, indent=2)

    # 3. collection.json
    collection_json = {
        "sections": {
            "main": {
                "type": "main-collection"
            }
        },
        "order": [
            "main"
        ]
    }
    with open(os.path.join(THEME_DIR, "templates", "collection.json"), "w", encoding="utf-8") as f:
        json.dump(collection_json, f, indent=2)

    # 4. cart.json
    cart_json = {
        "sections": {
            "main": {
                "type": "main-cart"
            }
        },
        "order": [
            "main"
        ]
    }
    with open(os.path.join(THEME_DIR, "templates", "cart.json"), "w", encoding="utf-8") as f:
        json.dump(cart_json, f, indent=2)

    # 5. page.json
    page_json = {
        "sections": {
            "main": {
                "type": "main-page"
            }
        },
        "order": [
            "main"
        ]
    }
    with open(os.path.join(THEME_DIR, "templates", "page.json"), "w", encoding="utf-8") as f:
        json.dump(page_json, f, indent=2)

    # 6. 404.json
    not_found_json = {
        "sections": {
            "main": {
                "type": "main-404"
            }
        },
        "order": [
            "main"
        ]
    }
    with open(os.path.join(THEME_DIR, "templates", "404.json"), "w", encoding="utf-8") as f:
        json.dump(not_found_json, f, indent=2)

    print("Generated OS 2.0 JSON templates (index, product, collection, cart, page, 404).")

def generate_shopify_cart_js():
    cart_js_content = """/**
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
"""
    with open(os.path.join(THEME_DIR, "assets", "shopify-cart.js"), "w", encoding="utf-8") as f:
        f.write(cart_js_content)
    print("Generated assets/shopify-cart.js")

def package_theme_app_js():
    # Read original app.js and prepend getAssetUrl helper
    with open(os.path.join(BASE_DIR, "app.js"), "r", encoding="utf-8") as f:
        app_code = f.read()

    # Prepend Shopify CDN asset resolver
    helper_code = """// Shopify CDN Asset Resolver
function getAssetUrl(path) {
  if (!path) return '';
  if (path.startsWith('http://') || path.startsWith('https://') || path.startsWith('data:')) return path;
  if (window.ShopifyTheme && window.ShopifyTheme.assetUrl) {
    const filename = path.split('/').pop();
    return window.ShopifyTheme.assetUrl + filename;
  }
  return path;
}
"""
    # Replace image paths inside productsData so they resolve dynamically
    modified_app_code = helper_code + "\n" + app_code
    with open(os.path.join(THEME_DIR, "assets", "app.js"), "w", encoding="utf-8") as f:
        f.write(modified_app_code)
    print("Generated assets/app.js with Shopify CDN resolver.")

def create_zip():
    if os.path.exists(ZIP_OUTPUT):
        os.remove(ZIP_OUTPUT)
        
    with zipfile.ZipFile(ZIP_OUTPUT, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(THEME_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, THEME_DIR)
                zipf.write(abs_path, rel_path)
                
    zip_size = os.path.getsize(ZIP_OUTPUT)
    print(f"Created theme ZIP: {ZIP_OUTPUT} ({round(zip_size / 1024 / 1024, 2)} MB)")

def main():
    print("Starting Graffeine Tales Shopify Theme Generation...")
    clean_and_make_dirs()
    copy_and_flatten_assets()
    generate_config()
    generate_locales()
    generate_layout()
    extract_sections()
    generate_dedicated_sections()
    generate_snippets()
    generate_templates()
    generate_shopify_cart_js()
    package_theme_app_js()
    create_zip()
    print("Graffeine Tales Shopify Theme Generation complete!")

if __name__ == "__main__":
    main()
