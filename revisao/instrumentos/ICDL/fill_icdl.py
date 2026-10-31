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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.15'
doc.find('.//title').text = 'ICDL v0.15 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('Participant code', '014-002'), ('ICDL ID', 'ICDL-014-002'),
             ('Procedure date', '8 Jul 2026'), ('Procedure / side', 'Reverse shoulder arthroplasty / right'), ('Operating room', 'OR 4'), ('Primary surgeon (code)', 'Dr Lena Ortiz (S-02)'),
             ('Device / system', 'GLENOS reverse shoulder system'), ('CIP and surgical technique (version)', 'CIP v4.2; technique GS-ST v3.1'), ('Accountability record location', 'Device accountability log DAL-014, pharmacy store'),
             ('Controlled location', 'ISF tab 8 (Surgery) / ICDL-014-002')]:
    meta(k, v)
for st in doc.xpath('//section[contains(@class,"sheet-strip")]'):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        be.getparent().replace(be, E('span', 'demo-entry', {'ICDL ID': 'ICDL-014-002', 'Participant code': '014-002', 'Procedure date': '8 Jul 2026', 'Primary surgeon (code)': 'S-02'}[lab]))
for r, b in zip(rows('bt'), ['SCR-014-02 release 20 Jun 2026; delegation log rev. 5', 'Time-out 08:05, theatre checklist', 'PSEAR-014-003; consent v3.0', 'Loaner set LS-07 checked 7 Jul (check sheet)', 'Checked by the scrub nurse at opening', 'CT plan PLAN-014-002 on screen']):
    td = r.findall('td'); tick(td[1], 'Yes'); put(td[2], b)
bd = rows('bd')[0].findall('td'); tick(bd[0], 'Released'); put(bd[1], '08:10'); put(bd[2], 'Dr L. Ortiz / Sub-investigator')
for r, c in zip(rows('ct'), [('Glenoid exposure and reaming to plan', 'Complete', 'PLAN-014-002', 'Acceptable', 'LO'),
                             ('Baseplate inclination and version with the guide', 'Complete', 'Guide G-014-002', 'Acceptable', 'LO'),
                             ('Central and peripheral screw fixation', 'Complete', 'Screw lengths in E', 'Acceptable', 'LO'),
                             ('Humeral cut and stem trial', 'Complete', 'Trial stem 10', 'Acceptable', 'LO'),
                             ('Trial reduction with trial liner and stability check', 'Partial', 'No trial liners in the set; checked with the final liner', 'Observation', 'LO · F-1')]):
    td = r.findall('td'); put(td[1], c[0]); tick(td[2], c[1]); put(td[3], c[2]); tick(td[4], c[3]); put(td[5], c[4])
for r, d in zip(rows('dt'), [('08:22', '', 'LO'), ('08:58', 'Lot labels on the sheet', 'AR'), ('10:05', 'Stable in all positions', 'LO'), ('10:31', 'Duration 2 h 9 min', 'AR')]):
    td = r.findall('td'); put(td[1], d[0]); put(td[2], d[1]); put(td[3], d[2])
dh = rows('dh'); put(dh[0].findall('td')[1], 'Level 1: primary, cuff tear arthropathy (SLCT definitions v1)'); tick(dh[1], 'None'); put(dh[2].findall('td')[1], 'SLCT S-02, case 2')
E5 = [('Baseplate · implant', 'GLENOS · GS-BP', 'GS-BP25', '07612345000123', 'LOT 2604-118', '25 mm', 'Implanted', 'Yes'),
      ('Central screw · implant', 'GLENOS · GS-CS', 'GS-CS30', '07612345000130', 'LOT 2603-044', '30 mm', 'Implanted', 'Yes'),
      ('Peripheral screws (2) · implant', 'GLENOS · GS-PS', 'GS-PS34', '07612345000147', 'LOT 2603-090', '2 × 34 mm', 'Implanted', 'Yes'),
      ('Glenosphere · implant', 'GLENOS · GS-GL', 'GS-GL36', '07612345000154', 'LOT 2605-012', '36 mm, neutral', 'Implanted', 'Yes'),
      ('Humeral stem · implant', 'GLENOS · GS-HS', 'GS-HS10', '07612345000161', 'LOT 2604-201', 'Size 10, press-fit', 'Implanted', 'Yes'),
      ('Liner · implant', 'GLENOS · GS-L', 'GS-L36P6', '07612345000178', 'LOT 2606-033', '36, +6 mm', 'Implanted', 'Yes'),
      ('Trial stem · instrument', 'GLENOS · loaner set LS-07', 'GS-TS10', '', '', 'Size 10', 'Trial', 'No')]
for r, e in zip(rows('etb'), E5):
    td = r.findall('td')
    for k in range(6): put(td[k + 1], e[k])
    tick(td[7], e[6]); tick(td[8], e[7])
ef = rows('ef'); put(ef[0].findall('td')[1], 'Baseplate 25 with 30 mm central and 2 × 34 mm screws; glenosphere 36 neutral; stem 10 press-fit, 20 degrees retroversion; liner 36 +6')
put(ef[1].findall('td')[1], 'Accountability log DAL-014 p. 3; operative note ON-014-002; label sheet')
f = rows('ft')[0].findall('td')
put(f[1], '10:00: trial liners 36 +3, +6 and +9 not in the loaner set; no trial reduction'); put(f[2], 'Set check sheet LS-07 does not list trial liners')
put(f[3], 'Liner chosen on soft-tissue tension; stability less certain'); put(f[4], 'Final +6 liner fitted after stability and range checked; DEV-014-2026-002; sponsor told (J-1)')
put(rows('gt')[0].findall('td')[1], 'None')
for r, h in zip(rows('ht'), [('Adequate', 'ON-014-002; IQL-014-005', ''), ('Adequate', 'DAL-014 p. 3; label sheet', ''), ('Adequate', 'Clinic note 8 Jul, 12:00', ''),
                             ('Adequate', 'X-ray 9 Jul; IQL-014-005', ''), ('Adequate', 'DEV-014-2026-002', 'J-1 · coordinator')]):
    td = r.findall('td'); tick(td[1], h[0]); put(td[2], h[1]); put(td[3], h[2])
rows('hs')[0].findall('td')[1].append(E('span', 'demo-fill txt', 'Record usable. One change to the plan: no trial reduction because the loaner set had no trial liners (F-1). The deviation is recorded and the sponsor has been asked to complete the sets (J-1).'))
it = rows('it')[0].findall('td'); tick(it[0], 'Complete with open action'); put(it[1], '10:55'); put(it[2], 'Dr L. Ortiz / Sub-investigator'); put(it[3], 'J-1')
j = rows('jt')[0].findall('td')
put(j[1], 'Trial liners missing from loaner set (F)'); put(j[2], 'Sponsor logistics request GS-LOG-0711'); put(j[3], 'Coordinator'); put(j[4], '31 Jul 2026'); put(j[5], ''); tick(j[6], 'Open')
for r, k in zip(rows('kt'), ['ISF tab 8 (Surgery) / ICDL-014-002', 'DAL-014, pharmacy store, p. 3', 'DEV-014-2026-002; IQL-014-005; no SART']):
    put(r.findall('td')[1], k)
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Completed by (in theatre)', 'Ana Ruiz / OR nurse lead', 'A. Ruiz', '8 Jul 2026, 10:55')
sign('Operating surgeon', 'Dr L. Ortiz / Sub-I', 'L. Ortiz', '8 Jul 2026, 11:10')
sign('Principal Investigator (if required)', 'Dr A. Morgan / PI', 'A. Morgan', '9 Jul 2026, 08:30')
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
