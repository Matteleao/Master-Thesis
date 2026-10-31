import sys, base64
from lxml import html as LH, etree
SRC, OUT = sys.argv[1], sys.argv[2]
doc = LH.document_fromstring(open(SRC).read())
def E(tag, cls, text):
    e = etree.Element(tag); e.set('class', cls); e.text = text; return e
def meta(label, val):
    c = [c for c in doc.xpath('//div[contains(@class,"meta-cell")]') if c.find('b') is not None and c.find('b').text_content().strip() == label][0]
    be = c.find('.//span[@class="blank-entry"]')
    if be is not None: be.getparent().replace(be, E('span', 'demo-entry', val))
    else: c.append(E('span', 'demo-entry', val))
def tick(scope, *labels):
    for lab in labels:
        for o in scope.xpath('.//span[contains(@class,"opt")]'):
            if o.text_content().strip() == lab:
                o.find('.//span[@class="check"]').set('class', 'check selected'); break
        else: raise Exception('no opt ' + lab)
def put(td, val):
    if val: td.append(E('span', 'demo-fill', val))
def tables(cls): return doc.xpath(f'//table[contains(concat(" ",@class," ")," {cls} ")]')
def rows(cls, i=0): return tables(cls)[i].xpath('./tbody/tr')
def byLabel(trs, label):
    for r in trs:
        if r.findall('td') and r.findall('td')[0].text_content().strip().startswith(label): return r
    raise Exception(label)
def fillrow(r, vals, start=1):
    td = r.findall('td')
    for t, v in zip(td[start:], vals): put(t, v)
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.7'
doc.find('.//title').text = 'PFVR v0.7 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('PFVR ID', 'PFVR-014-002-M3'),
             ('Participant code', '014-002'), ('Visit (name / nominal day)', '3 months / day 90'), ('Index procedure date (ICDL ID)', '8 Jul 2026 (ICDL-014-002)'), ('Target date', '6 Oct 2026'),
             ('Window (first and last day)', '22 Sep to 20 Oct 2026 (day 76 to 104)'), ('Completed by / role', 'Nadia Costa / Research nurse'), ('Controlled location', 'ISF tab 6 (Follow-up) / PFVR-014-002-M3')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Attended')
for st in doc.xpath('//section[@class="sheet-strip"]'):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        be.getparent().replace(be, E('span', 'demo-entry', {'PFVR ID': 'PFVR-014-002-M3', 'Participant code': '014-002', 'Visit': '3 months', 'Window': '22 Sep to 20 Oct 2026'}[lab]))
for r, b in zip(rows('bt'), [('2 Oct 2026 · in person', '86', '1, 3 to 6; 2 in part', 'Clinic visit; ASES page 2 not done (participant had to leave). Clinic note CN-014-002-M3'),
                             ('9 Oct 2026 · in person', '93', '2', 'ASES page 2 completed in clinic; same questionnaire Q-014-002-M3'), ('', '', '', '')]):
    td = r.findall('td')
    for k in range(4): put(td[k + 1], b[k])
C = [('Constant score', 'Yes', 'Clinician-administered, dynamometer · as required', '2 Oct · day 86', 'Complete', 'In window', 'Score sheet Q-014-002-M3', ''),
     ('ASES questionnaire', 'Yes', 'Self-completed · as required', '2 and 9 Oct · day 86, 93', 'Complete', 'In window', 'Q-014-002-M3', '1'),
     ('Pain score 0 to 10', 'Yes', 'Self-reported · as required', '2 Oct · day 86', 'Complete', 'In window', 'Q-014-002-M3', ''),
     ('X-ray: true AP, Velpeau axillary, scapular Y', 'Yes', 'SIRR IMG-05 · as required', '2 Oct · day 86', 'Complete', 'In window', 'IQL-014-024', ''),
     ('Range of motion', 'No', 'Goniometer · as required', '2 Oct · day 86', 'Complete', 'In window', 'CN-014-002-M3', ''),
     ('Interval safety review', 'No', 'Interview and examination · as required', '2 Oct · day 86', 'Complete', 'In window', 'CN-014-002-M3; SART-014-003', '2')]
for r, c in zip(rows('ct'), C):
    td = r.findall('td'); put(td[1], c[0]); tick(td[2], c[1]); put(td[3], c[2]); put(td[4], c[3]); tick(td[5], c[4]); tick(td[6], c[5]); put(td[7], c[6]); put(td[8], c[7])
d = rows('dt')[0].findall('td')
put(d[0], '4'); put(d[1], 'IQL-014-024'); tick(d[2], 'Adequate'); put(d[3], 'Dr H. Meyer · 3 Oct'); put(d[4], 'Implant seated; humeral head centered; no dislocation'); put(d[5], 'None')
for r, e in zip(rows('et'), [('"It feels like it slips out at the back when I reach behind me."', 'About 2 weeks; twice a week; moderate', 'Worse', 'Seen by the PI the same day; SART-014-003 opened (H-2)'),
                             ('"The pain is less than at six weeks."', '3 / 10 now; 5 / 10 at 6 weeks', 'Better', 'None'),
                             ('"I can put a cup on the kitchen shelf."', 'Since about 3 weeks', 'Better', 'None')]):
    td = r.findall('td'); put(td[0], e[0]); put(td[1], e[1]); tick(td[2], e[2]); put(td[3], e[3])
for r, f in zip(rows('ft'), [('Stability', 'Dr L. Ortiz', 'Apprehension test', 'Positive in internal rotation; new since 6 weeks', 'PI review 2 Oct; SART-014-003'),
                             ('Range of motion', 'Dr L. Ortiz', 'Goniometer', 'Forward elevation 120 degrees (6 weeks: 90)', 'None'),
                             ('Wound', 'Dr L. Ortiz', 'Inspection', 'Healed; unchanged', 'None'),
                             ('Axillary nerve', 'Dr L. Ortiz', 'Sensation and deltoid', 'Intact; unchanged', 'None')]):
    td = r.findall('td')
    for k in range(5): put(td[k], f[k])
for r, g in zip(rows('gt'), [('Elena Martin', 'Yes', ''), ('Dr Lena Ortiz', 'Yes', ''), ('Grace Park', 'No', 'N. Costa on leave on 2 Oct; G. Park, trained on Constant scoring (TRE-014-09), scored under Dr L. Ortiz')]):
    td = r.findall('td'); put(td[1], g[0]); tick(td[2], g[1]); put(td[3], g[2])
for r, h in zip(rows('ht'), [('2: ASES page 2 not done on 2 Oct; participant had to leave', 'Completed 9 Oct, day 93, in window; no data lost', 'Q-014-002-M3', 'Research nurse', '9 Oct', 'Closed'),
                             ('6 and E-1: new instability symptoms', 'PI review; SART-014-003 (grade I); physiotherapy for stabilization; event indexed in SCML-014-09', 'SART-014-003; SCML-014-09', 'PI', '16 Oct', 'Closed')]):
    td = r.findall('td')
    for k in range(5): put(td[k + 1], h[k])
    tick(td[6], h[5])
for r, w in zip(rows('it'), ['B: first contact day 86, window day 76 to 104', 'C: 6 of 6 complete', 'C and D: 4 of 4 in window; X-ray adequate (IQL-014-024)', 'H: 2 of 2 closed']):
    tick(r.findall('td')[1], 'Yes'); put(r.findall('td')[2], w)
rows('io')[1].xpath('.//span[@class="check"]')[0].set('class', 'check selected')
rows('ir')[0].findall('td')[1].append(E('span', 'demo-fill txt', 'All components complete and in window; the ASES finished on a second contact inside the window. New instability symptoms were sent to the PI and the SART; they are a clinical finding, not a gap in the visit data.'))
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Completed by', 'Nadia Costa / Research nurse', 'N. Costa', '9 Oct 2026')
sign('Reviewed by (investigator)', 'Dr Alex Morgan', 'A. Morgan', '12 Oct 2026')
F = '/tmp/claude-0/-home-user-Master-Thesis/c35b56ea-6e37-57ca-a7f6-4cae380cc50e/scratchpad/fonts/'
hand = base64.b64encode(open(F + '4UaErEJDsxBrF37olUeD_xHMwps.ttf', 'rb').read()).decode()
sig = base64.b64encode(open(F + 'dancing.ttf', 'rb').read()).decode()
st = etree.SubElement(doc.find('.//head'), 'style')
st.text = ('@font-face{font-family:"SimHand";font-weight:400 700;src:url(data:font/ttf;base64,' + hand + ')}'
           '@font-face{font-family:"SimSig";src:url(data:font/ttf;base64,' + sig + ')}'
           '.demo-fill,.demo-entry{font-family:"Segoe Print","Bradley Hand","Comic Sans MS","SimHand",cursive!important;color:#174f88!important;font-weight:600!important;line-height:1.18!important}'
           'td .demo-fill{display:block;text-align:center!important;font-size:10.4px}.et td .demo-fill,.gt td .demo-fill,.ft td .demo-fill{font-size:9.6px}.demo-fill.txt{text-align:left!important;font-size:10.6px;line-height:1.45!important}.signature .demo-fill{font-size:11px}td:has(>.demo-fill){text-align:center!important}.demo-fill.inl{display:inline!important}td.left:has(>.demo-fill.inl){text-align:left!important}'
           '.meta-cell .demo-entry{display:block;text-align:left;font-size:10px;margin-top:3px}'
           '.wbox.lim .demo-fill{display:block;font-size:10.4px;line-height:1.45!important;margin-top:8px}'
           '.sig-ink{font-family:"Snell Roundhand","Brush Script MT","Segoe Script","Lucida Handwriting","SimSig",cursive!important;font-size:15px!important;color:#174f88}')
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
