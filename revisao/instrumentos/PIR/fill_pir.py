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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v1.0'
doc.find('.//title').text = 'PIR v1.0 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('PIR ID', 'PIR-014-2026-10'),
             ('Period reviewed / data cut-off', '1 to 31 Oct 2026 / 31 Oct 2026'), ('Previous PIR', 'PIR-014-2026-09'), ('Rule set (version, effective date)', 'PIR-RS-014 v1, 12 Aug 2026'), ('Review date', '5 Nov 2026'),
             ('Document owner / role', 'Maria Silva / Study Coordinator'), ('Accountable reviewer / role', 'Dr Alex Morgan / PI'), ('Controlled location', 'ISF tab 3 (Quality) / PIR-014-2026-10')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Routine')
for st in doc.xpath('//section[contains(@class,"sheet-strip")]'):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        be.getparent().replace(be, E('span', 'demo-entry', {'PIR ID': 'PIR-014-2026-10', 'Site / code': 'Riverside / 014', 'Period / data cut-off': 'Oct 2026 / 31 Oct', 'Rule set (version)': 'PIR-RS-014 v1', 'Rule set ID / version': 'PIR-RS-014 / v1', 'Effective from': '12 Aug 2026', 'Approved by (PI) / date': 'Dr A. Morgan / 11 Aug 2026', 'Replaces version': 'None (first version)'}[lab]))
for r, b in zip(rows('bt'), ['SIFSL-014 rev. 23; PSEAR-014-019 to -022; ICDL-014-007, -008; FUCR-014-2026-10; SLCT S-01 to S-03; CSST-014-02; IMC-014-02; SART-014-004, -005; query report 31 Oct',
                             'FUCR for October closed 3 Nov (late); its counts are final. No record excluded.',
                             'None. Rule set v1 in force for July to October.',
                             'July to October, same rules and units; July and August have few cases']):
    put(r.findall('td')[1], b)
CR = [('Inclusion decisions', 'Every criterion evidenced before the decision; no important eligibility deviation', 'A clarification after enrollment', 'Any important eligibility deviation', 'PIR-01'),
      ('Procedures', 'No important deviation of the same type in two periods', 'One important deviation in the period', 'Same type again after a correction', 'PIR-02'),
      ('Expected visits', 'In window with all components: 90% or more', '80 to 89%, or worse two periods in a row', 'Below 80%', 'PIR-03'),
      ('Reportable cases', 'All sent within the CIP interval', 'One complete first report missing', 'Any late report', 'PIR-04'),
      ('Procedures per surgeon', 'At most one unplanned event (substitution, deviation, unplanned support, grade IIIa or higher) in a surgeon\'s last 5 cases', 'Two unplanned events in a surgeon\'s last 5 cases', 'Three or more in the last 5 cases, or a grade IIIa or higher complication repeated', 'PIR-05'),
      ('Endpoint fields sampled', 'Agreement 97% or more; fewer than 5 queries open over 10 days', 'Agreement 95 to 96.9%, or 5 or more queries over 10 days', 'Agreement below 95%', 'PIR-06')]
for r, c in zip(rows('ct'), CR):
    td = r.findall('td')
    for k in range(5): put(td[k + 2], c[k])
DR = [('3 / 3 (100%)', '2 / 2 (100%)', '1 / 1 (100%)', '0 / 0', '8 / 8 (100%)', 'Stable', 'Within rule'),
      ('1 / 3', '0 / 1', '0 / 2', '2 / 2', '3 / 8', 'Worse', 'Action required'),
      ('3 / 3 (100%)', '5 / 6 (83%)', '6 / 7 (86%)', '5 / 7 (71%)', '19 / 23 (83%)', 'Worse', 'Action required'),
      ('0 / 0', '0 / 0', '1 / 1', '1 / 1', '2 / 2', 'Too few periods', 'Not assessable'),
      ('1 / 3', '0 / 1', '1 / 2', '1 / 2', 'S-01 0 / 3; S-02 1 / 3; S-03 2 / 2', 'Stable', 'Closer review'),
      ('60 / 60', '118 / 118', '120 / 120', '116 / 118 (98.3%)', '414 / 416 (99.5%)', 'Worse', 'Within rule')]
for r, d in zip(rows('dt'), DR):
    td = r.findall('td')
    for k in range(5): put(td[k + 1], d[k])
    tick(td[6], d[5]); tick(td[7], d[6])
ER = [('Instability events concentrate in cases with a missing trial liner or an unplanned liner change', '2, 5 and CSST', 'ICDL-014-002 F-1; ICDL-014-005 F; ICDL-014-007 F; CSST-014-02 C2 and E2; SLCT S-02, S-03', 'Such cases: 3 (002, 005, 007), instability in 2. Other cases: 5, instability in 0', 'Loaner-set check sheet does not list trial liners; not the surgeon alone', 'Supported'),
      ('Follow-up gaps and transcription errors in the same weeks', '3 and 6', 'FUCR-014-2026-10; PFVR-014-002-M3 H; IMC-014-02 checks 8 and 9', 'Issues on visits 1 to 14 Oct (nurse on leave): 3 of 4. Rest of the period: 1 of 4', 'No cover plan for questionnaires and data entry during absence', 'Supported'),
      ('Both instability events in fracture-sequelae cases', '1, 5 and CSST', 'CSST-014-02 E3; PSEAR of both participants (indication)', 'Fracture sequelae: 2 cases, instability in 2. Other types: 6 cases, instability in 0', 'Case type; numbers too small', 'Open: needs more data')]
for r, e in zip(rows('et'), ER):
    td = r.findall('td')
    for k in range(5): put(td[k + 1], e[k])
    tick(td[6], e[5])
for r, f in zip(rows('ft'), [('PIR-A1', 'Trial liners on the loaner-set check sheet; no case starts without them (E-1)', 'CAPA-014-04; SRR R-09', 'OR nurse lead', '15 Nov', 'Indicator 2: no trial-less case in the next 5 procedures'),
                             ('PIR-A2', 'Cover plan for questionnaires and data entry when the research nurse is away (E-2)', 'SRR R-13; delegation log', 'Coordinator', '30 Nov', 'Indicator 3 at 90% or more and indicator 6 at 99% or more in Nov and Dec'),
                             ('PIR-A3', 'Report instability by case type to the sponsor at the next safety call (E-3)', 'Sponsor call minutes', 'PI', '20 Nov', 'Sponsor answer recorded; case type added to the next CSST')]):
    td = r.findall('td')
    for k in range(6): put(td[k], f[k])
for r, g in zip(rows('gt'), [('ICDL J-1', 'Sponsor completes the loaner sets (July)', 'Jul: 1 trial-less case', 'Oct: 1 trial-less case', 'Did not work', 'Replaced by PIR-A1 (site check, not sponsor request)'),
                             ('IMC A-01-03', 'No late image set in two months', 'Jul: 2 late', 'Sep, Oct: 0 late', 'Worked', 'Close')]):
    td = r.findall('td')
    for k in (0, 1, 2, 3, 5): put(td[k], g[k])
    tick(td[4], g[4])
for r, (c, l) in zip(rows('hc'), [('2', '1 · Enrollment quality; 6 · Critical data completeness (worse, still within rule)'), ('1', '5 · Surgeon procedural consistency (S-03: 2 unplanned events in 2 cases)'), ('2', '2 · Protocol deviations; 3 · Follow-up compliance'), ('1', '4 · Safety reporting timeliness (only 2 cases so far)')]):
    td = r.findall('td'); put(td[1], c); put(td[2], l)
hd = rows('hd'); tick(hd[0], 'Mixed')
hd[1].findall('td')[1].append(E('span', 'demo-fill txt', 'Two indicators need action and one needs closer review in October, and they trace back to two process causes: loaner sets without trial liners (indicators 2 and 5, and the instability in the CSST) and no cover when the research nurse is away (indicator 3, and the small drop in indicator 6). The July request to the sponsor did not fix the sets; the fix has to be the site\'s own check before each case.'))
put(hd[2].findall('td')[1], 'CAPA-014-04; SRR R-09 and R-13 updated; POT-014-08 (S-03 proctoring continues); sponsor call 20 Nov')
put(hd[3].findall('td')[1], 'PIR-014-2026-11, 5 Dec 2026; earlier if a trial-less case occurs')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Document owner', 'Maria Silva / Study Coordinator', 'M. Silva', '5 Nov 2026')
sign('Principal Investigator', 'Dr Alex Morgan', 'A. Morgan', '6 Nov 2026')
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
           '.check.selected{background:#fff!important;border-color:#6d7a88!important;position:relative}'
           '.check.selected:after{content:"X"!important;position:absolute;left:0.5px;top:-4.5px;width:auto!important;height:auto!important;border:0!important;transform:none!important;font:700 12px "Segoe Print","Bradley Hand","Comic Sans MS","SimHand",cursive;color:#174f88}'
           '.sig-ink{font-family:"Snell Roundhand","Brush Script MT","Segoe Script","Lucida Handwriting","SimSig",cursive!important;font-size:15px!important;color:#174f88}')
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
