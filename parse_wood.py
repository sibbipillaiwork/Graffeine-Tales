import re

with open(r"C:\Users\sibbi\.gemini\antigravity-ide\brain\81b4418a-3019-4c4d-8b51-67f71454ca5d\.system_generated\steps\198\content.md", "r", encoding="utf-8") as f:
    text = f.read()

# search for filenames ending in .jpg, .png, etc.
files = set(re.findall(r'[\w\-\s\.]+\.(?:jpg|jpeg|png)', text, re.IGNORECASE))
print("Found files:", files)
