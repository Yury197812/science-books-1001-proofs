import re, os
os.chdir("D:/4/CLEAN_ARCHIVE")

def extract_hrefs(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return re.findall(r'href=["](["]+)["]', content)


catalog_hrefs = extract_hrefs("catalog.html")
print("catalog links:", len(catalog_hrefs))
