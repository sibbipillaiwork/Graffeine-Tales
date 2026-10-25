import re
import json

path = r"C:\Users\sibbi\.gemini\antigravity-ide\brain\81b4418a-3019-4c4d-8b51-67f71454ca5d\.system_generated\steps\132\content.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Look for filename patterns
filenames = set(re.findall(r'[\w\-\s\.]+\.(?:jpg|jpeg|png|webp|heic)', text, re.IGNORECASE))
print("Filenames:", filenames)

# Look for data chunks or Drive IDs
# In Google drive folder HTML, files are often in JSON arrays like [["id","name",...]]
# Let's search for "1mq6JLbC58Ygb4iMr8frI-FdPb3_1i2U9" in the text
matches = [m.start() for m in re.finditer(r'1mq6JLbC58Ygb4iMr8frI-FdPb3_1i2U9', text)]
print("Folder ID matches at indices:", matches)

# Check text around matches
for idx in matches[:3]:
    start = max(0, idx - 200)
    end = min(len(text), idx + 1000)
    print("--- SNIPPET ---")
    print(text[start:end])
