import re, json, os
from collections import defaultdict, Counter

base = 'D:/4/CLEAN_ARCHIVE'

with open(os.path.join(base, 'catalog.html'), 'rb') as fh:
    data = fh.read()

C = chr(94)
pat = r'href=' + chr(34) + '([' + C + ' + C + ' + chr(34)
hrefs = [m.decode('utf-8') for m in re.findall(pat.encode(), data)]
print('=== TASK 1: catalog.html anchor verification ===')
print('Total href references:', len(hrefs))
print('Unique:', len(set(hrefs)))
 
by_chapter = defaultdict(set) 
for h in set(hrefs): 
    m = re.match(r'(.+/chapter_(\d+)\.html)#(thm_\d+)', h) 
    if m: 
        by_chapter[m.group(1)].add((h, m.group(3)))
 
broken = [] 
for ch_path in sorted(by_chapter.keys()): 
    for full_href, thm in by_chapter[ch_path]: 
        fpath = os.path.join(base, full_href) 
        if not os.path.exists(fpath): 
            broken.append((full_href, 'FILE NOT FOUND')) 
            continue 
        with open(fpath, encoding='utf-8') as f: 
            content = f.read() 
        thm_b = thm.encode('utf-8') 
        search_pat = rb"id=['\"]" + thm_b + rb"['\"]" 
        if re.search(search_pat, content.encode('utf-8')): 
            found_count +=  
        else: 
            broken.append((full_href, 'ANCHOR NOT FOUND'))
 
print('Found OK:', found_count) 
print('Broken:', len(broken)) 
for item in broken: 
    print('  BROKEN:', item[0], '-', item[1]) 
if not broken: 
    print('ALL catalog.html references are VALID.')
 
with open(os.path.join(base, 'search_index.json'), encoding='utf-8') as f: 
    sindex = json.load(f) 
 
print() 
print('=== TASK 2: search_index.json anc verification ===') 
print('Total entries:', len(sindex)) 
 
si_bad = [] 
for i, entry in enumerate(sindex): 
    anc = entry.get('anc', '') 
    m = re.search(r'(.+/chapter_(\d+)\.html)#(thm_\d+)', anc) 
    if not m: 
        m2 = re.match(r'(chapter_(\d+)\.html)#(thm_\d+)', anc) 
        if m2: 
            full = m2.group(1) 
            thm_id = m2.group(3) 
            fpath = os.path.join(base, full) 
            if not os.path.exists(fpath): 
                si_bad.append((i, anc, 'FILE NOT FOUND')) 
                continue 
        else: 
            si_bad.append((i, anc, 'BAD FORMAT')) 
            continue 
    else: 
        full = m.group(1) 
        thm_id = m.group(3) 
        fpath = os.path.join(base, full) 
        if not os.path.exists(fpath): 
            si_bad.append((i, anc, 'FILE NOT FOUND')) 
            continue
