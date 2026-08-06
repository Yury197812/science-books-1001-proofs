# 1001 Proofs — Clean Archive

A deduplicated, validated archive of 864 unique theorems across 430 chapters and 9 science areas.

## Overview

| Metric | Value |
|--------|-------|
| Total theorems | 864 |
| Chapters | 430 |
| Science areas | 9 |
| Mathematical theorems | 596 |
| Empirical laws | 268 |
| HTML validation | 430/430 PASS |
| Archive size | ~0.9 MB |

This archive was generated from 433,267 original records, deduplicated to 864 unique theorem packages through a 14-stage pipeline including cross-chapter deduplication, formula repair, empirical law reclassification, and HTML validation.

## Science Areas

| Area | Chapters | Theorems | Laws |
|------|----------|----------|------|
| Mathematics | 98 | 436 | 0 |
| Physics | 90 | 1 | 116 |
| Chemistry | 46 | 0 | 48 |
| Biology | 48 | 0 | 50 |
| Astronomy | 25 | 0 | 26 |
| Computer Science | 48 | 75 | 0 |
| Statistics | 25 | 44 | 0 |
| Earth Sciences | 25 | 0 | 41 |
| Engineering | 25 | 0 | 27 |

## Structure

```
CLEAN_ARCHIVE/
  index.html          - Main page with all 430 chapters
  catalog.html        - Theorem catalog with search and filters
  MANIFEST.json       - Machine-readable metadata
  theorem_index.json  - All 864 theorems as structured JSON
  001_Algebra/
    chapter_0001.html - Chapter with theorem cards
  002_Groups/
    chapter_0002.html
  ...
  430_Computing/
    chapter_0430.html
```

## Chapter File Format

Each chapter HTML file contains:

```html
<div class="theorem">
  <h3>Theorem Name</h3>
  <p><strong>Statement:</strong> Exact mathematical statement</p>
  <p><strong>Hypotheses:</strong> Required conditions</p>
  <p><strong>Conclusion:</strong> What follows from hypotheses</p>
  <p><strong>Definitions:</strong> Key terms used</p>
  <div class="proof">
    <p><strong>Proof sketch:</strong></p>
    <p class="step">Step 1: ...</p>
    <p class="step">Step 2: ...</p>
    <p class="step">Step 3: ...</p>
  </div>
  <p class="metadata">ID: ... | Status: UNREVIEWED | Source: ... | Entry Type: THEOREM</p>
</div>
```

## Entry Types

- **THEOREM** (596) — Mathematically proven statements with proof sketches
- **EMPIRICAL_LAW** (268) — Experimentally determined relationships (Newton's laws, gas laws, etc.)

## Difficulty Levels

- **Elementary** (265) — Basic definitions and simple proofs (31%)
- **Intermediate** (577) — Standard proofs with moderate complexity (67%)
- **Advanced** (22) — Research-level results (Galois, cohomology, Navier-Stokes) (3%)

## Proof Banks

15 unique theorems have full proof sketches applied across multiple chapters:

| Theorem | Chapters | Proof |
|---------|----------|-------|
| Lagrange's theorem | 12 | Coset partition |
| MVT | 15 | Rolle's theorem |
| Master Theorem | 48 | Recursion tree (3 cases) |
| LLN | 5 | Kolmogorov + truncation |
| Brouwer fixed point | 3 | Retraction obstruction |
| Riesz representation | 7 | Kernel + projection |
| Euclid's infinity of primes | 6 | N = product + 1 |
| Gödel incompleteness | 4 | Arithmetization + diagonalization |
| Pigeonhole principle | 10 | Counting argument |
| MLE asymptotic normality | 24 | Score + CLT |
| Seismic wave velocities | 24 | V_p > V_s from moduli |
| Noether's theorem | 1 | Symmetry → conservation |
| RSA correctness | 1 | Fermat + CRT |

## How to Use

### Browse locally
```bash
# Extract the archive
unzip CLEAN_ARCHIVE_430.zip -d CLEAN_ARCHIVE

# Open in browser
start CLEAN_ARCHIVE/index.html     # Main page
start CLEAN_ARCHIVE/catalog.html   # Searchable theorem index
```

### Search theorems
- `index.html` has a search box that filters across all 430 chapters
- `catalog.html` has advanced filters: by area, entry type, difficulty, and full-text search

### Access specific theorems
```
001_Algebra/chapter_0001.html     # Chapter on Algebra
099_Classical_Mechanics/chapter_0099.html  # Classical Mechanics
308_Algorithms/chapter_0308.html  # Algorithms (48 theorems)
```

### Parse programmatically
```python
import json
theorems = json.load(open('theorem_index.json'))
math_theorems = [t for t in theorems if t['area'] == 'Mathematics']
advanced = [t for t in theorems if t['difficulty'] == 'Advanced']
```

## Metadata

### MANIFEST.json
```json
{
  "unique": 864,
  "chapters": 430,
  "areas": 9,
  "status": "UNREVIEWED",
  "license": "CC-BY-4.0",
  "validation": "430/430 PASS"
}
```

### theorem_index.json
Each of 864 theorems includes:
- `id` — unique hash
- `chapter` — parent chapter directory
- `area` — science area
- `h3` — theorem title
- `stmt` — statement text
- `hyps` — hypotheses
- `conc` — conclusion
- `steps_count` — proof steps
- `entry_type` — THEOREM or EMPIRICAL_LAW
- `difficulty` — Elementary/Intermediate/Advanced
- `source` — bibliographic reference
- `status` — UNREVIEWED

## Validation

Every chapter passes:
- Balanced `<div>` / `</div>` tags
- Balanced `<p>` / `</p>` tags
- No unescaped `<` in math content
- No template variables
- No placeholder text
- Canonical URL present
- MathJax included

## History

| Version | Changes |
|---------|---------|
| V1 | 433,267 raw records across 430 chapters |
| V3 | CRT formula fixed, misplaced removed, postulates reclassified |
| V5 | 588 bare `<` escaped in math |
| V7 | Cross-chapter dedup: 2,390 → 864 unique theorems |
| V8 | Stub detection: 403 empty cards identified |
| V9 | Template fills applied |
| V10 | Master Theorem corrected (3 cases), false source labels removed |
| V11 | 232 empirical laws reclassified |
| V12 | 15 proof banks written, 113 template proofs replaced |
| V13 | HTML catalog, theorem index, README |

## License

CC-BY-4.0

## Links

- [GitHub Pages](https://yury197812.github.io/science-books-1001-proofs/)
- [arXiv: 2608.07961](https://arxiv.org/abs/2608.07961)
- [OSF: hn236](https://osf.io/hn236/)
- [Zenodo: 10.5281/zenodo.21288911](https://doi.org/10.5281/zenodo.21288911)
- [GitHub Repo](https://github.com/Yury197812/science-books-1001-proofs)
