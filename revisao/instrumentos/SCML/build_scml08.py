# SCML v0.8 from the concluded v0.7 (blank or filled): adds the Clavien-Dindo grade (copied from the SART) to the surveillance profile.
import re, sys
from lxml import html as LH, etree
SRC, OUT = sys.argv[1], sys.argv[2]
GR = sys.argv[3].split(',') if len(sys.argv) > 3 else None
s = open(SRC).read().replace('v0.7', 'v0.8')
doc = LH.document_fromstring(s)
GRADES = ['I', 'II', 'IIIa', 'IIIb', 'IVa', 'IVb', 'V', 'N/A', 'Pending']
def opts(sel=None):
    d = etree.Element('div'); d.set('class', 'category-options grade-options')
    for g in GRADES:
        o = etree.SubElement(d, 'div'); o.set('class', 'option')
        c = etree.SubElement(o, 'span'); c.set('class', 'check marked' if g == sel else 'check')
        if g == sel:
            pm = etree.SubElement(c, 'span'); pm.set('class', 'pen-mark'); pm.set('aria-label', 'selected'); pm.text = 'X'
        t = etree.SubElement(o, 'span'); t.text = g
    return d
tb = doc.xpath('//table[contains(@class,"profile-log")]')[0]
cols = tb.find('colgroup').findall('col')
for c, w in zip(cols, [5, 10, 23, 9, 14, 8, 15]): c.set('style', f'width:{w}%')
nc = etree.Element('col'); nc.set('style', 'width:16%'); cols[3].addnext(nc)
th = tb.xpath('./thead/tr/th')[3]; nth = etree.Element('th'); nth.text = 'Grade (Clavien-Dindo)'; br = etree.SubElement(nth, 'br'); br.tail = '(from SART)'; th.addnext(nth)
for i, r in enumerate(tb.xpath('./tbody/tr')):
    td = r.findall('td')[3]; ntd = etree.Element('td'); ntd.set('class', 'left')
    ntd.append(opts(GR[i] if GR and i < len(GR) else None)); td.addnext(ntd)
out = LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')
def rep(a, b):
    global out
    assert a in out, a[:60]; out = out.replace(a, b, 1)
rep('D: select the event type, one primary surveillance category and timing group. Copy the current relationship context and DD finding from the SART.',
    'D: select the event type, one primary surveillance category and timing group. Copy the current Clavien-Dindo grade, relationship context and DD finding from the SART.')
rep('Select one event type, primary category and timing group.', 'Select one event type, primary category and timing group.')
rep('Copy relationship contexts, the DD finding and assessment status from the current SART', 'Copy the Clavien-Dindo grade, relationship contexts, the DD finding and assessment status from the current SART')
grade_rows = [('I', 'Any deviation from the normal postoperative course without drugs, surgery or radiological intervention beyond antiemetics, antipyretics, analgesics, diuretics, electrolytes and physiotherapy; wounds opened at the bedside.', 'Superficial wound problem treated with dressings; transient nerve palsy resolving without treatment.'),
              ('II', 'Needs drug treatment beyond grade I, blood transfusion or parenteral nutrition.', 'Wound infection treated with antibiotics; thromboembolism treated with anticoagulation.'),
              ('IIIa', 'Needs a surgical, endoscopic or radiological intervention not under general anesthesia.', 'Closed reduction of a dislocation under sedation; aspiration of a hematoma.'),
              ('IIIb', 'Needs an intervention under general anesthesia.', 'Open reduction or revision for instability; liner exchange; washout for deep infection.'),
              ('IVa', 'Life-threatening, single organ dysfunction needing intermediate or intensive care.', 'Pulmonary embolism needing intensive care.'),
              ('IVb', 'Life-threatening, multiorgan dysfunction.', 'Septic shock from a periprosthetic infection.'),
              ('V', 'Death of the participant.', '')]
tbl = ('<div class="grade-ref"><table class="guide grade-guide"><colgroup><col style="width:8%"><col style="width:56%"><col style="width:36%"></colgroup>'
       '<thead><tr><th>Grade</th><th>Clavien-Dindo definition</th><th>Example in shoulder arthroplasty</th></tr></thead><tbody>' +
       ''.join(f'<tr><td>{g}</td><td class="left">{d}</td><td class="left">{e}</td></tr>' for g, d, e in grade_rows) +
       '</tbody></table><p class="note">The grade follows the treatment the event needed and is set in the SART. Add the suffix d when a disability remains at discharge (for example IIIb-d). A device deficiency without an adverse event takes N/A.</p></div>')
i = out.find('<footer')
assert i > 0
out = out[:i] + tbl + out[i:]
css = ('<style>.grade-guide td{font-size:8px!important;padding:2px 6px!important;height:auto!important;line-height:1.22}.grade-guide th{font-size:8.4px!important;padding:3px!important}'
       '.grade-ref{margin-top:6px}.grade-options{grid-template-columns:auto auto auto!important;column-gap:6px!important}.profile-log th{font-size:8.2px}</style>\n')
j = out.rfind('</head>'); out = out[:j] + css + out[j:]
open(OUT, 'w').write(out); print('ok')
