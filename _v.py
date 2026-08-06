import re,json,os
from collections import defaultdict,Counter
base="D:/4/CLEAN_ARCHIVE"
hrefs=json.load(open(base+"/_hrefs.json"))
print("Unique:",len(set(hrefs)))
broken=[]
ok_count=0
for h in set(hrefs):
  parts=h.split("#")
  fpath=os.path.join(base,parts[0])
  thm=parts[1]
  exists=os.path.exists(fpath)
  found=False
  if exists:
    c=open(fpath,encoding="utf-8").read()
    dq=id_dq="id="+chr(34)+thm+chr(34)
    sq=id_sq="id="+chr(39)+thm+chr(39)
    found=(dq in c) or (sq in c)
  if not found:
    broken.append(h)
  else:
    ok_count+=1
print("Task1 Found:",ok_count)
print("Task1 Broken:",len(broken))
for b in broken:
  print(" ",b)
