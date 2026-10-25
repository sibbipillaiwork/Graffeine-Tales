import re
import json

path = r"C:\Users\sibbi\.gemini\antigravity-ide\brain\81b4418a-3019-4c4d-8b51-67f71454ca5d\.system_generated\steps\132\content.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Find AF_initDataCallback calls
callbacks = re.findall(r'AF_initDataCallback\((.*?)\);</script>', text, re.DOTALL)
print(f"Total callbacks found: {len(callbacks)}")

for i, cb in enumerate(callbacks):
    print(f"\n--- CALLBACK {i+1} (length {len(cb)}) ---")
    # let's look for key
    key_match = re.search(r"key:\s*'([^']+)'", cb)
    key = key_match.group(1) if key_match else "unknown"
    print(f"Key: {key}")
    
    # search for file IDs and names in cb
    # Let's search for substrings like 'image/' or '.jpg' or '.png' or file items
    items = re.findall(r'\[\"([a-zA-Z0-9_-]{25,45})\",\[\"([^\"]+)\"', cb)
    if items:
        print(f"Items found: {len(items)}")
        for it in items[:10]:
            print(" ", it)
    else:
        # print first 500 chars of data
        data_match = re.search(r"data:\s*(.*)", cb, re.DOTALL)
        if data_match:
            d = data_match.group(1)[:500]
            print(f"Data snippet: {d}")
