"""Mechanical checks on one instrument HTML (blank or simulated).

Usage: python3 check_instrument.py <path-to-instrument.html> [--json]

Prints a report of verifiable facts; a human judgment step reads this report, never replaces it.
Checks: page structure, header on every page, footer numbering, section lettering, Section A title,
final signature block, version consistency, acronyms outside the 24-instrument set, CtQ coding,
British spellings, duplicated table headers, empty cells (blank form only).
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

INSTR = set("CCDM RACI DTRM TRE SCR POT MRL SRR SLCT SCML CSST SART IMP IMC SIRR IQL ICDL PSEAR SIFSL PFVR FUCR PIR CAPA PIDLR".split())
KNOWN = set("""PI CIP ICH GCP ISO MDR EU EN CRO CRF EDC ISF AE AEs SAE SAEs ADE ADEs SADE SADEs DD DDs UDI DI PI QA QC QMS CtQ CTQ
DR SOP SOPs IFU ID IDs IRB EC REC ROM PRO PROs PROM CT MRI CEC DSMB RBM RBQM IMDRF MDCG FDA CFR USA UK OR OK NA PDF HTML
ICF CV GDPR RACI ECG BMI ASA SSP IC PD PDs AP ASES PROMs ROM MRI UDI OR MOD RL FOR NOT USE II III TR AS AW CD NA""".split())
BRITISH = r"\b(?:\w*isation|centre|centres|behaviour|programme|labelled|licence|enrolment|colour|(?:organis|recognis|standardis|authoris|prioritis|minimis|summaris|finalis|utilis|harmonis|randomis|categoris|characteris|optimis|realis|specialis(?!t))\w*|analys(?:e|ed|ing))\b"


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.pages, self.cur = [], [], None
        self.skip = 0
        self.tables, self.cur_table, self.cur_row, self.cell = [], None, None, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if tag in ("script", "style") or a.get("id") in ("ccdm-editor",) or a.get("data-editor-ui"):
            self.skip += 1
        self.stack.append((tag, cls, a))
        if tag == "main" and "page" in cls.split():
            self.cur = {"landscape": "landscape" in cls, "text": [], "header": "", "footer": "", "sections": []}
            self.pages.append(self.cur)
        if tag == "table" and self.cur is not None:
            self.cur_table = {"page": len(self.pages), "head": [], "rows": []}
        if tag == "tr" and self.cur_table is not None:
            self.cur_row = []
        if tag in ("td", "th") and self.cur_row is not None:
            self.cell = {"tag": tag, "text": "", "has_check": False}
        if "check" in cls.split() and self.cell is not None:
            self.cell["has_check"] = True

    def handle_endtag(self, tag):
        while self.stack:
            t, cls, a = self.stack.pop()
            if t in ("script", "style") or a.get("id") == "ccdm-editor" or a.get("data-editor-ui"):
                self.skip = max(0, self.skip - 1)
            if t == tag:
                break
        if tag in ("td", "th") and self.cell is not None and self.cur_row is not None:
            self.cur_row.append(self.cell); self.cell = None
        if tag == "tr" and self.cur_row is not None and self.cur_table is not None:
            if self.cur_row and all(c["tag"] == "th" for c in self.cur_row) and not self.cur_table["head"]:
                self.cur_table["head"] = [c["text"].strip() for c in self.cur_row]
            else:
                self.cur_table["rows"].append(self.cur_row)
            self.cur_row = None
        if tag == "table" and self.cur_table is not None:
            self.tables.append(self.cur_table); self.cur_table = None

    def handle_data(self, data):
        if self.skip or self.cur is None:
            return
        self.cur["text"].append(data)
        classes = " ".join(c for _, c, _ in self.stack)
        if "topbar" in classes and "version" not in classes:
            self.cur["header"] += data
        if "footer" in classes:
            self.cur["footer"] += data + " "
        if re.search(r"(?:^|\s)(?:section-letter|letter)(?:\s|$)", classes) and data.strip():
            self.cur["sections"].append([data.strip(), ""])
        if "section-title" in classes and self.cur["sections"]:
            self.cur["sections"][-1][1] += data
        if self.cell is not None:
            self.cell["text"] += data


def main(path, as_json=False):
    html = Path(path).read_text(encoding="utf-8")
    c = Collector(); c.feed(html)
    full = " ".join(" ".join(p["text"]) for p in c.pages)
    full = re.sub(r"\s+", " ", full)
    rep = {"file": Path(path).name, "pages": len(c.pages), "findings": [], "facts": {}}
    F = rep["findings"].append

    # pages / header / footer
    n = len(c.pages)
    rep["facts"]["orientation"] = ["landscape" if p["landscape"] else "portrait" for p in c.pages]
    titles = [re.sub(r"\s+", " ", p["header"]).strip() for p in c.pages]
    rep["facts"]["headers"] = titles
    if any(not t for t in titles):
        F("HEADER: page(s) without the instrument header: " + str([i + 1 for i, t in enumerate(titles) if not t]))
    base = [t.split(" Site")[0] for t in titles]
    for i, p in enumerate(c.pages):
        m = re.search(r"Page\s+(\d+)\s+of\s+(\d+)", p["footer"])
        if not m:
            F(f"FOOTER: page {i+1} has no 'Page x of y'")
        elif (int(m.group(1)), int(m.group(2))) != (i + 1, n):
            F(f"FOOTER: page {i+1} says {m.group(0)} (expected Page {i+1} of {n})")

    # sections
    secs = [(L, re.sub(r"\s+", " ", T).strip()) for p in c.pages for L, T in p["sections"]]
    rep["facts"]["sections"] = secs
    letters = [L for L, _ in secs]
    if letters:
        expect = [chr(ord("A") + i) for i in range(len(letters))]
        if letters != expect:
            F(f"SECTIONS: lettering {letters} is not consecutive (expected {expect})")
        if not re.match(r"purpose(?:,| and) use", secs[0][1], re.I):
            F(f"SECTIONS: Section A is '{secs[0][1]}', must start with 'Purpose and use'")
    sig_page = next((i + 1 for i, p in enumerate(c.pages) if re.search(r"signature", " ".join(p["text"]), re.I)), None)
    rep["facts"]["signature_block_page"] = sig_page
    if sig_page is None:
        F("SIGNATURE: no signature block found")
    elif sig_page != n:
        after = c.pages[sig_page:]
        cont = all(re.search(r"continuation", p["header"] + " ".join(p["text"]), re.I) for p in after)
        linked = all(re.search(r"record ID", " ".join(p["text"]), re.I) and re.search(r"sheet", " ".join(p["text"]), re.I) for p in after)
        if not cont:
            F(f"SIGNATURE: signature block on page {sig_page} but pages {sig_page+1}-{n} are not marked as continuation sheets")
        elif not linked:
            F("SIGNATURE: continuation sheet(s) after the signature lack a header linking them to the record (record ID and sheet number)")
    sigs = re.findall(r"<div class=\"signature\"><b>([^<]+)</b>", html)
    rep["facts"]["signature_roles"] = sigs

    # versions
    acr = re.match(r"([A-Z]{2,6})", Path(path).name)
    acr = acr.group(1) if acr else ""
    fv = re.findall(r"v(\d+\.\d+)", Path(path).name)
    selfv = sorted(set(re.findall(rf"{acr}\s*(?:[·|-]\s*)?v(\d+\.\d+)", full)) | set(re.findall(r"(?:SIMULATED|BLANK|DRAFT)?\s*·\s*v(\d+\.\d+)", full)))
    rep["facts"]["version"] = {"file_name": fv, "in_document": selfv}
    if len(set(fv) | set(selfv)) > 1:
        F(f"VERSION: file name says {fv}, document says {selfv}")

    # acronyms
    tokens = set(re.findall(r"\b[A-Z][A-Za-z]*[A-Z]{1,}[A-Za-z0-9]*\b", full))
    instr_refs = sorted(t for t in tokens if t in INSTR)
    unknown = sorted(t for t in tokens if t not in INSTR and t not in KNOWN and not re.search(r"\d", t) and len(t) <= 6)
    rep["facts"]["instrument_refs"] = instr_refs
    rep["facts"]["other_acronyms_to_check"] = unknown
    if unknown:
        F("ACRONYMS outside the 24-instrument set and the common list (verify each is defined or replace): " + ", ".join(unknown))
    if re.search(r"\bCTQ\b", full):
        F("TERM: 'CTQ' used; the thesis writes 'CtQ' and codes domains CtQ1-CtQ12")
    if re.search(r"CtQ|CTQ", full) and not re.search(r"CtQ\s?(?:[1-9]|1[0-2])\b", full):
        F("CtQ: domains named in free text, never by thesis code CtQ1-CtQ12")

    brit = sorted(set(m.group(0) for m in re.finditer(BRITISH, full, re.I)))
    if brit:
        F("SPELLING (British, thesis uses American; ignore proper names): " + ", ".join(brit))

    # tables
    rep["facts"]["tables"] = [{"page": t["page"], "header": t["head"], "rows": len(t["rows"])} for t in c.tables]
    heads = [(i, set(h.lower() for h in t["head"] if h)) for i, t in enumerate(c.tables) if t["head"]]
    for a in range(len(heads)):
        for b in range(a + 1, len(heads)):
            i, A = heads[a]; j, B = heads[b]
            if A and B and len(A & B) / min(len(A), len(B)) >= 0.6:
                F(f"DUPLICATION: tables {i+1} and {j+1} share most column headers: {sorted(A & B)}")
    empty = sum(1 for t in c.tables for r in t["rows"] for cell in r if not cell["text"].strip() and not cell["has_check"])
    rep["facts"]["empty_cells"] = empty

    # simulated example domain check (thesis = shoulder device investigations)
    if re.search(r"<body[^>]*simulated", html, re.I) or any("SIMULATED" in t.upper() for t in titles) or re.search(r"class=\"version\">\s*SIMULATED", html):
        shoulder = bool(re.search(r"shoulder|arthroplast|humer|glenoid|rotator", full, re.I))
        rep["facts"]["simulated_example_is_shoulder"] = shoulder
        if not shoulder:
            F("EXAMPLE: simulated content is not a shoulder device investigation (thesis Section 4.8 says templates were developed for shoulder)")

    if as_json:
        print(json.dumps(rep, indent=2, ensure_ascii=False)); return
    print(f"# Mechanical check: {rep['file']}\n")
    print(f"Pages: {n} ({', '.join(rep['facts']['orientation'])})")
    print("Sections:", "; ".join(f"{L} {T}" for L, T in secs))
    print("Signature roles:", rep["facts"]["signature_roles"], "on page", sig_page)
    print("Instrument references:", ", ".join(instr_refs) or "none")
    print("Tables:", len(c.tables), "| empty cells:", empty)
    print("\n## Findings")
    for f in rep["findings"] or ["none"]:
        print("-", f)


if __name__ == "__main__":
    main(sys.argv[1], "--json" in sys.argv)
