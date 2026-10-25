"""Read the mark of every instrument in thesis Figures 4.4 (CtQ x instrument) and 4.5 (DR x instrument).

Usage: python3 read_matrix_marks.py [ACRONYM]
Prints the marks for one instrument (or all) so a review can verify coverage against the figure itself.
Marks, Figure 4.4: FILLED = primary/emphasis, OPEN = support/limit/scope, - = none.
Marks, Figure 4.5: DIRECT, INHERITED (open square), EXTENSION (dashed), SUPPORT (small grey), - = none.
"""
import sys
import numpy as np
from PIL import Image

IMG = "/Users/felipegregorio/Desktop/auditor_tese_corrigido/Imagens/"
INSTR = "CCDM RACI DTRM TRE SCR POT MRL SRR SLCT SCML CSST SART IMP IMC SIRR IQL ICDL PSEAR SIFSL PFVR FUCR PIR CAPA PIDLR".split()
X0, DX = 702, 78.1

def load(name):
    return np.array(Image.open(IMG + name).convert("RGB")).astype(int)

def row_centers(im, n):
    band = im[230:1045, 100:180]
    dark = (band.sum(axis=2) < 380).any(axis=1)
    ys = np.where(dark)[0] + 230
    groups, start, prev = [], ys[0], ys[0]
    for y in ys[1:]:
        if y - prev > 8:
            groups.append((start, prev)); start = y
        prev = y
    groups.append((start, prev))
    groups = [g for g in groups if g[1] - g[0] > 8][:n]
    return [int((a + b) / 2) for a, b in groups]

def colored(px):
    return (px.max() - px.min()) > 45 or px.sum() < 560

def ring_fraction(im, cx, cy, r):
    hits = tot = 0
    for t in np.linspace(0, 2 * np.pi, 48, endpoint=False):
        x, y = int(cx + r * np.cos(t)), int(cy + r * np.sin(t))
        tot += 1
        hits += colored(im[y, x])
    return hits / tot

def square_fraction(im, cx, cy, h):
    pts = [(cx + dx, cy - h) for dx in range(-h, h + 1, 2)] + [(cx + dx, cy + h) for dx in range(-h, h + 1, 2)] \
        + [(cx - h, cy + dy) for dy in range(-h, h + 1, 2)] + [(cx + h, cy + dy) for dy in range(-h, h + 1, 2)]
    return sum(colored(im[y, x]) for x, y in pts) / len(pts)

def ctq_marks():
    im = load("Fig. CtQ domains by instrument@2x.png")
    rows = row_centers(im, 12)
    out = {}
    for j, a in enumerate(INSTR):
        cx = int(round(X0 + DX * j)); col = []
        for cy in rows:
            if colored(im[cy, cx]): col.append("FILLED")
            elif ring_fraction(im, cx, cy, 13) > 0.5: col.append("OPEN")
            else: col.append("-")
        out[a] = col
    return out

def dr_marks():
    im = load("Fig. Design requirements by instrument (matrix)@2x.png")
    rows = row_centers(im, 12)
    out = {}
    for j, a in enumerate(INSTR):
        cx = int(round(X0 + DX * j)); col = []
        for k, cy in enumerate(rows):
            if k >= 10:
                col.append("ALL (banner)"); continue
            if colored(im[cy, cx]):
                col.append("DIRECT" if colored(im[cy - 9, cx - 9]) else "SUPPORT")
            else:
                f = square_fraction(im, cx, cy, 14)
                col.append("INHERITED" if f > 0.75 else "EXTENSION" if f > 0.2 else "-")
        out[a] = col
    return out

if __name__ == "__main__":
    want = [sys.argv[1].upper()] if len(sys.argv) > 1 else INSTR
    c, d = ctq_marks(), dr_marks()
    for a in want:
        print(a)
        print("  Fig 4.4 CtQ:", ", ".join(f"CtQ{i+1}={m}" for i, m in enumerate(c[a]) if m != "-") or "none")
        print("  Fig 4.5 DR :", ", ".join(f"DR{i+1}={m}" for i, m in enumerate(d[a]) if m not in ("-", "ALL (banner)")) or "none", "| DR11, DR12 = all instruments")
