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
import re as _re
A_NEW = ('<div class="box"><p>The SCML indexes the site’s complications, adverse events, adverse device effects and device deficiencies so they can be compared across cases. Each case is assessed in the Safety and Adverse Effect Reporting Template (SART); the log keeps only the current classification and the links to its sources. Urgent care and safety reporting never wait for this log.</p></div>'
         '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
         '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
         '<td>One event, as assessed in its SART case.</td>'
         '<td>How the event is profiled for review across cases, and where its follow-up is sent.</td>'
         '<td>SART case and grade, Intraoperative Checklist and Device Log (ICDL), imaging source.</td>'
         '<td>Indexed events for the Complication Signal Surveillance Template (CSST); status for the PI Oversight Template (POT).</td></tr></tbody></table>')
out = _re.sub(r'<div class="box"><p>This log brings together.*?</div>', lambda m: A_NEW, out, count=1, flags=_re.S)
B_ROWS = [('Link the event', 'C: give a unique SCML Event ID; enter the SART case ID and event reference. Use participant and surgeon codes.', 'Keep the Event ID in C and D. Cite the ICDL and imaging source; do not copy narratives.'),
          ('Apply a profile', 'D: select event type, one primary category and timing group. Copy the Clavien-Dindo grade, relationship context and DD finding from the SART.', 'Use Pending for open items. Other codes come from the study category set.'),
          ('Review and follow through', 'E: cite the events or group and the receiving record. F: check the status of an existing action.', 'Rates and signal decisions sit in the CSST; case follow-up stays in the SART or quality record.')]
B_NEW = '<tbody>' + ''.join(f'<tr><td>{x}</td><td class="left">{y}</td><td class="left">{z}</td></tr>' for x, y, z in B_ROWS) + '</tbody>'
out = _re.sub(r'<tbody><tr><td>Link the event</td>.*?</tbody>', lambda m: B_NEW, out, count=1, flags=_re.S)
out = out.replace('Recording and Source-Link Guide', 'Recording and source-link guide', 1)
out = _re.sub(r'<p class="note">Open the index while.*?</p>', '<p class="note">One event keeps one Event ID, even when both the AE and DD pathways apply.</p>', out, count=1, flags=_re.S)
rep('Copy relationship contexts, the DD finding and assessment status from the current SART', 'Copy the Clavien-Dindo grade, relationship contexts, the DD finding and assessment status from the current SART')
grade_rows = [('I', 'Deviation from the normal course needing no treatment beyond simple drugs (analgesics, antiemetics, antipyretics, diuretics, electrolytes) or physiotherapy.', 'Superficial wound problem treated with dressings; transient nerve palsy resolving without treatment.'),
              ('II', 'Needs drug treatment beyond grade I, blood transfusion or parenteral nutrition.', 'Wound infection treated with antibiotics; thromboembolism treated with anticoagulation.'),
              ('IIIa', 'Needs a surgical, endoscopic or radiological intervention not under general anesthesia.', 'Closed reduction of a dislocation under sedation; aspiration of a hematoma.'),
              ('IIIb', 'Needs an intervention under general anesthesia.', 'Open reduction or revision for instability; liner exchange; washout for deep infection.'),
              ('IVa', 'Life-threatening, single organ dysfunction needing intermediate or intensive care.', 'Pulmonary embolism needing intensive care.'),
              ('IVb', 'Life-threatening, multiorgan dysfunction.', 'Septic shock from a periprosthetic infection.'),
              ('V', 'Death of the participant.', '')]
tbl = ('<div class="grade-ref"><table class="guide grade-guide"><colgroup><col style="width:23%"><col style="width:39%"><col style="width:38%"></colgroup>'
       '<thead><tr><th>Grade</th><th>Clavien-Dindo definition</th><th>Example in shoulder arthroplasty</th></tr></thead><tbody>' +
       ''.join(f'<tr><td>{g}</td><td class="left">{d}</td><td class="left">{e}</td></tr>' for g, d, e in grade_rows) +
       '</tbody></table></div>')
i = out.find('<footer')
assert i > 0
out = out[:i] + tbl + out[i:]
css = ('<style>.guide td{height:42px!important;font-size:9.2px!important;line-height:1.3!important;padding:3px 7px!important}.guide th{font-size:9.6px!important}'
       '.purpose th{text-align:center}.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:44px;line-height:1.4;font-weight:400!important;color:inherit!important}'
       '.grade-ref{margin-top:8px}.grade-options{grid-template-columns:auto auto auto!important;column-gap:6px!important}.profile-log th{font-size:8.2px}</style>\n')
j = out.rfind('</head>'); out = out[:j] + css + out[j:]
open(OUT, 'w').write(out); print('ok')
