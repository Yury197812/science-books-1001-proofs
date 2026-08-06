import os,re
from collections import Counter
base="D:/4/CLEAN_ARCHIVE"
print("=== TASK 3: Duplicate THEOREM anchors check ===")
dupes=0
C=chr(34)
for root,dirs,files in os.walk(base):
    for fname in sorted(files):
        if fname.startswith("chapter_") and fname.endswith(".html"):
            fpath=os.path.join(root,fname)
            with open(fpath,encoding="utf-8") as f:
                content=f.read()
            thm_ids=[]
            for line in content.split(chr(10)):
                temp=line
                while C in temp:
                    i1=temp.index(C)+1
                    i2=temp.index(C,i1)
                    val=temp[i1:i2]
                    if val.startswith("thm_"):
                        thm_ids.append(val)
                    temp=temp[i2+1:]
            counter=Counter(thm_ids)
            for id_val,count in counter.items():
                if count>1:
                    rel=os.path.relpath(fpath,base)
                    print(" ",rel+": "+id_val+" x"+str(count))
                    dupes+=1
if dupes==0:
    print("NO DUPLICATE thm_N ANCHORS found in any chapter file.")
else:
    print("Total duplicate thm_N anchor issues:",dupes)
