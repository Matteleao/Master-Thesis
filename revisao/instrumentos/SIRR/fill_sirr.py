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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.6'
doc.find('.//title').text = 'SIRR v0.6 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('SIRR ID / revision', 'SIRR-014 / r1'),
             ('Assessment date', '2 Jun 2026'), ('Imaging charter or manual / version / effective date', 'GLENOS imaging manual IMG-MAN v2.0 / effective 1 Apr 2026'),
             ('Charter received / confirmed by / date', 'Received 7 Apr 2026 / Elena Martin / 9 Apr 2026'), ('Reassessment trigger (if any)', 'Sponsor reply to Q-IMG-02 (3-month axillary view)'),
             ('Radiology contact / role', 'Elena Martin / Radiology research technologist (P-09)'), ('Controlled location', 'Investigator site file, tab 7 (Imaging) / SIRR-014')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Reassessment')
for r, v in zip(rows('ct'), [('Technologist checks views and labels at the console, logs the set in the IQL and sends it through the sponsor portal.', 'Research technologist'),
                             ('Technologist records the limitation in the IQL; local reviewer decides within 2 working days if it can be repeated in window.', 'Local imaging reviewer'),
                             ('Repeat in window when possible; if not, IQL limitation and deviation check by the coordinator; PI decides on clinical need.', 'Local reviewer, PI'),
                             ('Coordinator recovers the set or its source; if lost, IQL and deviation log; sponsor told within 5 days.', 'Study coordinator')]):
    td = r.findall('td'); put(td[1], v[0]); put(td[2], v[1])
D = [('§3.1', 'Before surgery · ≤ 90 days', 'CT shoulder, whole scapula; 0.625 mm slices; bone kernel', 'CT-2 · preset GLENOS-SH · WI-IMG-02', 'Ready', 'Adequate', '', ''),
     ('§3.2', 'Before surgery · ≤ 30 days', 'X-ray: true AP (Grashey), axillary, scapular Y', 'XR-3 · order set SH-3V', 'Ready', 'Adequate', '', ''),
     ('§4.1', 'Before discharge', 'X-ray: true AP, axillary', 'XR-3 or ward unit · order set SH-2V', 'Ready', 'Adequate', '', ''),
     ('§4.2', '6 weeks · day 42 ± 7', 'X-ray: true AP, axillary, scapular Y', 'XR-3 · order set SH-3V · booking rule BR-06', 'Ready', 'Adequate', '', ''),
     ('§4.3', '3 months · day 90 ± 14', 'X-ray: true AP, axillary, scapular Y', 'XR-3 · order set SH-3V', 'Ready', 'Adequate', 'Axillary often impossible at 3 months; Velpeau view accepted by sponsor (r1)', 'A-01'),
     ('§4.4', '12 months · day 365 ± 30', 'X-ray: true AP, axillary, scapular Y', 'XR-3 · order set SH-3V', 'Ready', 'Adequate', '', ''),
     ('§4.5', '24 months · day 730 ± 30', 'X-ray: true AP, axillary, scapular Y', 'XR-3 · order set SH-3V', 'Ready', 'Adequate', '', ''),
     ('§5.1', 'Unplanned · ≤ 7 days after instability or revision', 'X-ray: true AP, axillary', 'Emergency XR-1 · order set SH-2V', 'Partial', 'Partial', 'Out-of-hours sets not labeled with study ID; observation', 'A-03')]
for r, d in zip(rows('dt'), D):
    td = r.findall('td'); put(td[1], d[0]); put(td[2], d[1]); put(td[3], d[2]); put(td[4], d[3]); tick(td[5], d[4]); tick(td[6], d[5]); put(td[7], d[6]); put(td[8], d[7])
E5 = [('CT-2 (Siemens SOMATOM)', 'Preset GLENOS-SH checked 20 May 2026 against §3.1', 'Ready', ''),
      ('XR-3 (digital radiography)', 'Order sets SH-2V and SH-3V live 18 May 2026', 'Ready', ''),
      ('CT-2, XR-3, XR-1', 'Service reports: CT-2 valid to 3 Apr 2027; XR-3 to 12 Mar 2027; XR-1 to 30 Jan 2027', 'Ready', ''),
      ('TT-014-01, TT-014-02', 'TT-01 failed on CT over 500 slices; TT-02 passed 28 May 2026, receipt and retrieval confirmed by the core lab', 'Ready', 'A-02 closed'),
      ('Hospital PACS', 'Retrieval of test set by study ID checked 28 May 2026', 'Ready', '')]
for r, e in zip(rows('et'), E5):
    td = r.findall('td'); put(td[1], e[0]); put(td[2], e[1]); tick(td[3], e[2]); put(td[4], e[3])
F5 = [('Elena Martin / Radiology research technologist', 'Acquires and checks views; sends sets; escalates a limited set to the reviewer', 'Delegation log rev. 5; TRE-014-07 (IMG-MAN v2.0)', 'Yes'),
      ('Dr Helen Meyer / MSK radiologist', 'Rates usability and clinical concern; refers disagreement with the core lab to the PI', 'Delegation log rev. 5; TRE-014-08', 'Yes'),
      ('Dr Alex Morgan / Principal Investigator', 'Decides on repeat imaging and clinical action; receives core-lab disagreements', 'Delegation log rev. 5; GCP certificate 2025', 'Yes')]
for r, f in zip(rows('ft'), F5):
    td = r.findall('td'); put(td[1], f[0]); put(td[2], f[1]); put(td[3], f[2]); tick(td[4], f[3])
G5 = [('IQL; GLENOS imaging portal', 'Technologist sends within 5 days', 'Defined and tested', 'TT-014-02'),
      ('IQL exception; deviation log', 'Technologist to reviewer; PI if no repeat', 'Defined and tested', 'Dry run 30 May 2026'),
      ('PSEAR; PACS report', 'Reviewer report to PI before surgery', 'Defined and tested', 'Dry run 30 May 2026'),
      ('IQL action; original and repeat set linked', 'Technologist; coordinator checks the link', 'Defined and tested', 'TT-014-02'),
      ('Core-lab query; SRR, POT or CAPA', 'PI with the core lab', 'Partial', 'Route agreed by email only; A-04')]
for r, g in zip(rows('gt'), G5):
    td = r.findall('td'); put(td[1], g[0]); put(td[2], g[1]); tick(td[3], g[2]); put(td[4], g[3])
H5 = [('A-01', 'IMG-05', 'Q-IMG-02 to sponsor: is a Velpeau axillary acceptable at 3 months?', 'No', 'Technologist', '30 May 2026', 'Closed: sponsor reply SP-IMG-0214, 31 May 2026'),
      ('A-02', 'Transfer', 'CT over 500 slices failed transfer test TT-014-01', 'Yes', 'Technologist', '28 May 2026', 'Closed: TT-014-02 passed'),
      ('A-03', 'IMG-08', 'Out-of-hours X-ray not labeled with study ID', 'No', 'Coordinator', '30 Jun 2026', 'Open: label request to radiology'),
      ('A-04', 'G, row 5', 'Core-lab disagreement route only agreed by email', 'No', 'PI', '15 Jun 2026', 'Open: written in site imaging instruction')]
for r, h in zip(rows('ht'), H5):
    td = r.findall('td')
    for k in (0, 1, 2, 4, 5, 6): put(td[k], h[k])
    tick(td[3], h[3])
it = rows('it'); [x for x in it[1].xpath('.//span[@class="check"]')][0].set('class', 'check selected')
put(it[4].findall('td')[1], 'A-03 (labels out of hours), A-04 (disagreement route): disclosed in the submission letter')
for r, j in zip(rows('jt'), [('r0', '20 May 2026', 'Initial · IMG-MAN v2.0 · all', 'Action required before submission (A-01, A-02)', 'After A-01 and A-02'),
                             ('r1', '2 Jun 2026', 'Sponsor reply SP-IMG-0214; TT-014-02 · v2.0 · IMG-05, transfer', 'Ready, with a documented observation', 'Charter amendment or IQL signal')]):
    td = r.findall('td')
    for k in range(5): put(td[k], j[k])
kt = rows('kt')
put(kt[0].findall('td')[1], 'SIRR-014 r1 package, sent to the GLENOS core lab / 3 Jun 2026')
put(kt[1].findall('td')[1], 'Core lab qualification letter IQ-014 / 9 Jun 2026: site qualified for imaging')
put(kt[2].findall('td')[1], 'Sponsor activation letter GS-ACT-014 / 16 Jun 2026')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Technical acquisition', 'E. Martin / P-09', 'E. Martin', '2 Jun 2026')
sign('Local imaging reviewer', 'Dr H. Meyer / MSK', 'H. Meyer', '2 Jun 2026')
sign('Principal Investigator', 'Dr A. Morgan / PI', 'A. Morgan', '3 Jun 2026')
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
