new_sections_css = """
/* ==========================================================================
   21. NEW LAUNCH & BESTSELLERS SECTIONS AESTHETICS
   ========================================================================== */
.new-launch-section {
  background: #FDFBF7;
  border-top: 1px solid rgba(43, 37, 35, 0.06);
  border-bottom: 1px solid rgba(43, 37, 35, 0.06);
  position: relative;
}

.new-launch-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 20%;
  right: 20%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(200, 157, 102, 0.4), transparent);
}

.bestsellers-section {
  background: #FFFFFF;
  border-bottom: 1px solid rgba(43, 37, 35, 0.06);
}

.catalogue-section {
  background: #FAF7F2;
  position: relative;
}

/* Ensure subcategories are completely removed */
.subcat-pills {
  display: none !important;
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(new_sections_css)

print("Appended section styles successfully!")
