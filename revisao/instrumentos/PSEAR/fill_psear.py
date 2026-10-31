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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.94'
doc.find('.//title').text = 'PSEAR v0.94 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version / amendment', 'CIP v4.2 / none'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('PSEAR ID / revision', 'PSEAR-014-007 / r0'),
             ('Participant code', '014-007'), ('Screening number', 'SCR-014-019'), ('Screening log entry (SIFSL)', 'SIFSL-014-019'), ('Date first identified', '4 Aug 2026'),
             ('Screening opened', '11 Aug 2026'), ('Responsible assessor / role', 'Dr Lena Ortiz / Sub-investigator'), ('Identification key location', 'Locked cabinet R-214, key log v2'), ('Controlled location', 'ISF tab 5 (Screening) / PSEAR-014-007')]:
    meta(k, v)
for r, v in zip(rows('bt'), [('Confirmed', 'CIP v4.2 §5; screening pathway in site instruction SI-SCR-01 v2', ''),
                             ('Confirmed', 'ICF v3.0 signed 11 Aug 2026 09:10; first study activity 11 Aug 09:40 (consent folder, ISF tab 4)', ''),
                             ('Confirmed', 'Delegation log rev. 6: L. Ortiz, N. Costa, H. Meyer', ''),
                             ('Confirmed', 'SIFSL-014-019 entered 4 Aug 2026', '')]):
    td = r.findall('td'); tick(td[1], v[0]); put(td[2], v[1]); put(td[3], v[2])
C = [('Informed consent (ICF v3.0)', 'Yes', '11 Aug 2026', 'Research nurse', 'Consent folder, ISF tab 4', 'Complete'),
     ('Medical history, prior shoulder surgery and infection', 'Yes', '11 Aug 2026', 'Sub-I', 'Clinic note EHR 11 Aug', 'Complete'),
     ('Physical examination: deltoid and axillary nerve', 'Yes', '11 Aug 2026', 'Sub-I', 'Clinic note EHR 11 Aug', 'Complete'),
     ('Constant score and ASES at baseline', 'Yes', '11 Aug 2026', 'Research nurse', 'Questionnaires Q-014-007-SCR', 'Complete'),
     ('Shoulder X-ray, three views', 'Yes', '14 Aug 2026', 'Radiology technologist', 'IQL-014-012; report RR-55120', 'Complete'),
     ('CT shoulder for glenoid assessment', 'Yes', '14 Aug 2026', 'Radiology technologist', 'IQL-014-013; report RR-55121', 'Complete'),
     ('C-reactive protein', 'Yes', '12 Aug 2026', 'Laboratory', 'Lab system, sample L-88310', 'Complete'),
     ('Family doctor record on prior infection', 'Yes', '21 Aug 2026', 'Research nurse', 'Letter scanned to EHR 21 Aug', 'Complete')]
for r, c in zip(rows('ct'), C):
    td = r.findall('td'); put(td[1], c[0]); tick(td[2], c[1]); put(td[3], c[2]); put(td[4], c[3]); put(td[5], c[4]); tick(td[6], c[5])
for r, d in zip(rows('dt'), [('Shoulder function', 'Constant score', '11 Aug 2026', '38 / 100', 'Q-014-007-SCR', 'N. Costa'),
                             ('Shoulder function, self-reported', 'ASES', '11 Aug 2026', '31 / 100', 'Q-014-007-SCR', 'N. Costa'),
                             ('Pain despite 6 months of non-operative care', 'Pain scale 0 to 10; history', '11 Aug 2026', '7 / 10; physiotherapy since Dec 2025', 'Clinic note 11 Aug', 'L. Ortiz'),
                             ('Active forward elevation', 'Goniometer', '11 Aug 2026', '70 degrees', 'Clinic note 11 Aug', 'L. Ortiz'),
                             ('Deltoid and axillary nerve', 'Muscle grading; sensation', '11 Aug 2026', 'Deltoid M5; sensation intact', 'Clinic note 11 Aug', 'L. Ortiz')]):
    td = r.findall('td')
    for k in range(6): put(td[k], d[k])
for r, e in zip(rows('e1t'), [('X-ray, three views', '14 Aug 2026', 'Right shoulder', 'IQL-014-012; RR-55120', 'Yes', 'Hamada grade 4a; superior migration of the head'),
                              ('CT', '14 Aug 2026', 'Right glenoid and scapula', 'IQL-014-013; RR-55121', 'Yes', 'Walch B2, retroversion 12 degrees; see E2'),
                              ('C-reactive protein', '12 Aug 2026', 'Blood', 'Sample L-88310', 'Yes', '3 mg/L (normal)')]):
    td = r.findall('td'); put(td[1], e[0]); put(td[2], e[1]); put(td[3], e[2]); put(td[4], e[3]); tick(td[5], e[4]); put(td[6], e[5])
for r, e in zip(rows('e2t'), [('Cuff tear arthropathy present (inclusion 2)?', 'Yes: Hamada 4a meets the CIP definition.', 'RR-55120 · Dr H. Meyer, 15 Aug'),
                              ('Glenoid bone loss needing a graft (exclusion 4)?', 'No: B2 with 12 degrees retroversion, correctable by reaming. First read by the Sub-I as possible B3; settled by the PI (H-1).', 'RR-55121 · Dr H. Meyer, 15 Aug; PI 21 Aug')]):
    td = r.findall('td')
    for k in range(3): put(td[k], e[k])
for r, f in zip(rows('ftb'), [('Cuff tear arthropathy with loss of active elevation', 'Clinic note 11 Aug · L. Ortiz', 'Confirmed'),
                              ('Primary reverse arthroplasty, deltopectoral approach', 'CIP §6.1 · L. Ortiz', 'Confirmed'),
                              ('GLENOS baseplate 25 mm, glenosphere 36 from CT plan PLAN-014-007', 'Planning software report · L. Ortiz', 'Confirmed'),
                              ('', '', 'N/A')]):
    td = r.findall('td'); put(td[1], f[0]); put(td[2], f[1]); tick(td[3], f[2])
G = [('Inclusion', 'Inclusion 1 · Age 60 years or older', 'ID card copy, 11 Aug · 11 Aug', 'Met', 'L. Ortiz 21 Aug', '', ''),
     ('Inclusion', 'Inclusion 2 · Cuff tear arthropathy, Hamada 2 or higher', 'E1-1, E2-1 · 15 Aug', 'Met', 'L. Ortiz 21 Aug', 'H. Meyer 15 Aug', ''),
     ('Inclusion', 'Inclusion 3 · Pain 5 or more after 6 months of non-operative care', 'D-3 · 11 Aug', 'Met', 'L. Ortiz 21 Aug', '', ''),
     ('Inclusion', 'Inclusion 4 · Planned primary reverse arthroplasty with GLENOS', 'F-1 to F-3 · 15 Aug', 'Met', 'L. Ortiz 21 Aug', '', ''),
     ('Inclusion', 'Inclusion 5 · Able to attend visits to 24 months', 'Clinic note 11 Aug · 11 Aug', 'Met', 'L. Ortiz 21 Aug', '', ''),
     ('Exclusion', 'Exclusion 1 · Previous arthroplasty of the same shoulder', 'C-2, clinic note · 11 Aug', 'Met', 'L. Ortiz 21 Aug', '', ''),
     ('Exclusion', 'Exclusion 2 · Shoulder infection in the past 12 months', 'C-7, C-8, E1-3 · 21 Aug', 'Met', 'L. Ortiz 21 Aug', '', 'H-2'),
     ('Exclusion', 'Exclusion 3 · Deltoid deficiency or axillary nerve palsy', 'D-5 · 11 Aug', 'Met', 'L. Ortiz 21 Aug', '', ''),
     ('Exclusion', 'Exclusion 4 · Glenoid bone loss needing a graft', 'E1-2, E2-2 · 15 Aug; PI 21 Aug', 'Met', 'L. Ortiz 21 Aug', 'H. Meyer 15 Aug', 'H-1'),
     ('Exclusion', 'Exclusion 5 · Neuromuscular disease of the upper limb', 'Clinic note 11 Aug · 11 Aug', 'Met', 'L. Ortiz 21 Aug', '', ''),
     ('Exclusion', 'Exclusion 6 · In another interventional study', 'Participant statement, SIFSL · 11 Aug', 'Met', 'L. Ortiz 21 Aug', '', '')]
for r, g in zip(rows('gt'), G):
    td = r.findall('td'); tick(td[1], g[0]); put(td[2], g[1]); put(td[3], g[2]); tick(td[4], g[3]); put(td[5], g[4]); put(td[6], g[5]); put(td[7], g[6])
for r, w in zip(rows('ht'), ['C: 8 of 8 activities complete', 'G: 5 of 5 inclusions met; 6 of 6 exclusions absent', 'B: consent 09:10, first activity 09:40 on 11 Aug', 'H: 2 of 2 items resolved by 21 Aug']):
    tick(r.findall('td')[1], 'Yes'); put(r.findall('td')[2], w)
hd = rows('hd'); tick(hd[0], 'Eligible')
hd[1].findall('td')[1].append(E('span', 'demo-fill txt', 'C complete (8 of 8). G: all 5 inclusions met and all 6 exclusions absent; exclusion 4 settled by the PI on 21 Aug (H-1), exclusion 2 by the family doctor letter (H-2). Consent before the first study activity (B-2).'))
for r, i in zip(rows('it'), [('Exclusion 4: Sub-I read the CT as possible B3; radiologist read B2', 'No decision until settled; PI to review CT with both readers', 'PI', '22 Aug 2026', 'Resolved: PI agrees B2, no graft (note 21 Aug)'),
                             ('Exclusion 2: infection history before 2024 not in the hospital record', 'No decision until known; letter requested from the family doctor', 'Research nurse', '22 Aug 2026', 'Resolved: letter 21 Aug, no infection')]):
    td = r.findall('td'); put(td[1], i[0]); put(td[2], i[1]); put(td[3], i[2]); put(td[4], i[3]); tick(td[5], 'Resolved'); put(td[5], i[4])
for r, j in zip(rows('jt'), ['21 Aug 2026, 16:40', '21 Aug 2026, 17:05 · EDC subject 014-007', 'SIFSL-014-019: enrolled, 21 Aug 2026', 'Surgery booked 2 Oct 2026; ICDL-014-007 opened 1 Oct', 'Not applicable']):
    put(r.findall('td')[1], j)
for r, k in zip(rows('kt'), ['ISF tab 5 (Screening) / PSEAR-014-007', 'EHR; consent folder ISF tab 4; IQL-014-012, -013', 'SIFSL-014-019']):
    put(r.findall('td')[1], k)
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Primary screening assessor', 'Dr L. Ortiz / Sub-I', 'L. Ortiz', '21 Aug 2026, 16:40')
sign('Investigator', 'Dr A. Morgan / PI', 'A. Morgan', '21 Aug 2026, 16:55')
sign('Second reviewer (if required)', 'Dr H. Meyer / MSK radiologist', 'H. Meyer', '15 Aug 2026, 11:20')
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
