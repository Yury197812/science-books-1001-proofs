import json,os
base="D:/4/CLEAN_ARCHIVE"
with open(os.path.join(base,"search_index.json"),encoding="utf-8") as f:
    sindex=json.load(f)
print("=== TASK 2: search_index.json anc verification ===")
print("Total entries:",len(sindex))
si_ok=0
si_bad=[]
for i,entry in enumerate(sindex):
    ch=entry.get("ch","")
    fl=entry.get("file","")
    anc=entry.get("anc","")
    if not ch or not fl or not anc:
        si_bad.append((i,"MISSING FIELDS","ch=%s file=%s anc=%s"%(ch,fl,anc)))
        continue
    full=os.path.join(base,ch,fl)
    if not os.path.exists(full):
        si_bad.append((i,full,"FILE NOT FOUND"))
        continue
    with open(full,encoding="utf-8") as f:
        content=f.read()
    dq="id="+chr(34)+anc+chr(34)
    sq="id="+chr(39)+anc+chr(39)
    if (dq in content) or (sq in content):
        si_ok+=1
    else:
        si_bad.append((i,full+"#"+anc,"ANCHOR NOT FOUND"))
print("Matched OK:",si_ok)
print("Mismatches:",len(si_bad))
for item in si_bad:
    print(" ",item)
if not si_bad:
    print("ALL search_index entries match valid anchors.")
