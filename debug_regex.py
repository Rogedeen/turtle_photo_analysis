import re

with open("reports/morphological-rulebook.md", "r", encoding="utf-8") as f:
    content = f.read()

print("--- Content Length:", len(content))
name_pattern = r'\*\*\d+\.\s*Tür:\*\*\s*\*([^*]+)\*\s*/\s*([^\n\r]+)'
name_match = re.search(name_pattern, content)
if name_match:
    print("First Species Match:", name_match.group(1))

feature_pattern = r'-\s*\*\*([^*]+)\*\*:(.*?)[\-\→]\s*Vision AI sorusu:\s*"([^"]+)"'
item_matches = re.findall(feature_pattern, content)
print("Feature Matches Count:", len(item_matches))
if item_matches:
    print("First Feature Match:", item_matches[0])
