import re,os
os.chdir("D:/4/CLEAN_ARCHIVE")
def gh(fp):
  with open(fp,"r",encoding="utf-8") as f: c=f.read()
  return re.findall(r"href=\x22([\x22]+)\x22",c)
print("=== CHECK 1: index.html ===")
h=gh("index.html")
i=[x for x in h if not x.startswith(("http","mailto","data:")) and x!="#"]
b=[x for x in i if not os.path.isfile(x.split("#")[0].replace("/",os.sep))]
print("%d links, %d broken" % (len(i),len(b)))
for x in b: print(" BROKEN:",x)
