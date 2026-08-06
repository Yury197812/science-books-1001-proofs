import re, os
os.chdir("D:/4/CLEAN_ARCHIVE")

def gh(fp):
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()
    pat = chr(34).join(["href=", "(["]+)", ""])
    return re.findall(pat, c)

print("=== CHECK 1: index.html ===")
h = gh("index.html")
internal = [x for x in h if not x.startswith(("http","mailto","data:")) and x != "#"]
broken1 = []
for x in internal:
    fp = x.split("#")[0]
    norm = fp.replace("/", os.sep)
    if not os.path.isfile(norm):
        broken1.append(x)
print("index.html: %d links, %d broken" % (len(internal), len(broken1)))
for b in broken1:
    print("  BROKEN:", b)
