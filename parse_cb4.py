import re
import json

path = r"C:\Users\sibbi\.gemini\antigravity-ide\brain\81b4418a-3019-4c4d-8b51-67f71454ca5d\.system_generated\steps\132\content.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

cb4 = re.findall(r'AF_initDataCallback\((.*?)\);</script>', text, re.DOTALL)[3]

# Print strings in cb4 that are not null, numbers, or short symbols
strings = re.findall(r'"([^"]{4,})"', cb4)
print("Strings in cb4:")
for s in strings:
    if not s.startswith("driveweb") and not s in ["Name", "A to Z", "Date modified", "New to old", "Z to A"]:
        print(" ->", s)
