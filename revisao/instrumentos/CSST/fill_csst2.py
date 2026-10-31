# Simulated (filled) CSST v2.0: GLENOS-01, Riverside 014, triggered review CSST-014-02 after the dislocation in SART-014-005 (cut-off 31 Oct 2026).
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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v2.0'
doc.find('.//title').text = 'CSST v2.0 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('CSST review ID / revision', 'CSST-014-02 / r1'),
             ('Review period / data cut-off', '1-31 Oct 2026; cut-off 31 Oct'), ('Device / procedure reviewed', 'GLENOS reverse shoulder, all study procedures'), ('Previous CSST review ID', 'CSST-014-01 (30 Sep 2026)'),
             ('SCML snapshot ID', 'SCML-014, snapshot 31 Oct 2026'), ('Analysis file (if used)', 'None: counted on this form'), ('Prepared by / role', 'Maria Silva / Study Coordinator'), ('Controlled location', 'ISF tab 6 (Safety) / CSST-014-02')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Triggered')
B = [('SCML-014 snapshot · 31 Oct', 'Complete', ''), ('ICDL-014-001 to -008 · 31 Oct', 'With limitation', 'ICDL-014-005: liner lot missing; read from the explant label'),
     ('PFVR export · 31 Oct', 'With limitation', '014-0003: 6-week visit on day 52 (outside window)'), ('SLCT-014 · 31 Oct', 'Complete', ''), ('SART export · 31 Oct', 'Complete', ''), ('CSST-014-01 · 30 Sep', 'Complete', '')]
for r, (a, st, lim) in zip(rows('bt'), B):
    td = r.findall('td'); put(td[2], a); tick(td[3], st); put(td[4], lim)
k1 = rows('kc1')
for lab, vals in [('Participants enrolled', ['4', '4', '0%', '8']),
                  ('Investigational procedures performed', ['4', '4', '0%', '8']), ('Surgeons operating', ['3', '2', '+50%', '3']), ('Surgeons with a first study case', ['1', '2', '-50%', '3']),
                  ('Procedures within', ['3', '4', '-25%', '7']), ('Revision procedures', ['1', '0', '-', '1']), ('Explanted components returned', ['0 (1 pending)', '0', '-', '0']),
                  ('Follow-up visits due', ['9', '4', '+125%', '13']), ('Follow-up visits done in window', ['7', '4', '+75%', '11']), ('Follow-up visits missed', ['1', '0', '-', '1']),
                  ('Operated', ['4', '4', '0%', '8']), ('Reached discharge', ['4', '4', '0%', '8']), ('Reached first postoperative visit', ['4', '4', '0%', '8']), ('Reached 6 weeks', ['3', '2', '+50%', '5']), ('Reached 3 months', ['2', '0', '-', '2']),
                  ('Reached 6 months', ['0', '0', '-', '0']), ('Reached 12 months', ['0', '0', '-', '0']), ('Reached 24 months', ['0', '0', '-', '0']), ('Participants withdrawn', ['0', '0', '-', '0'])]:
    fillrow(byLabel(k1, lab), vals)
td = byLabel(k1, 'Procedures within').findall('td')[0]; td.text = None
for c in list(td): td.remove(c)
td.text = 'Procedures within a surgeon\'s first '; u = E('span', 'demo-fill inl', '5'); u.tail = ' study cases'; td.append(u)
k2 = rows('kc2', 0) + rows('kc2', 1)
nr = ['8', '8', '8', '5', '2', '0', '0', '0', '', '']
for r in [x for x in k2 if x.findall('td') and x.findall('td')[0].text_content().strip().startswith('N for this column')]: fillrow(r, nr)
C2 = {'Dislocation': ['', '', '', '(1 / 5) 20%', '', '', '', '', '1', '1'], 'Subluxation or instability symptoms': ['', '', '', '', '(1 / 2) 50%', '', '', '', '1', '1'],
      'Superficial wound problem': ['', '(1 / 8) 12.5%', '', '', '', '', '', '', '1', '0'], 'Hematoma': ['', '(1 / 8) 12.5%', '', '', '', '', '', '', '1', '1'],
      'Nerve injury': ['', '', '(1 / 8) 12.5%', '', '', '', '', '', '1', '0'], 'Component disassociation': ['', '', '', '(1 / 5) 20%', '', '', '', '', '1', '1']}
for lab, vals in C2.items(): fillrow(byLabel(k2, lab), vals)
for r in k2:
    td = r.findall('td')
    if len(td) == 11 and not any(t.find('span[@class="demo-fill"]') is not None for t in td[1:]) and not r.get('class'):
        for t in td[9:11]: put(t, '0')
for lab, vals in [('Participants with at least one complication', ['3', '2', '+50%', '(5 / 8) 62.5%', '(2 / 4) 50%']), ('Participants with more than one', ['1', '0', '-', '(1 / 8) 12.5%', '(0 / 4) 0%']),
                  ('Reoperations', ['1', '0', '-', '(1 / 8) 12.5%', '(0 / 4) 0%']), ('Revisions', ['1', '0', '-', '(1 / 8) 12.5%', '(0 / 4) 0%']), ('Serious events', ['1', '0', '-', '(1 / 8) 12.5%', '(0 / 4) 0%']),
                  ('Device deficiencies', ['1', '0', '-', '(1 / 8) 12.5%', '(0 / 4) 0%'])]:
    fillrow(byLabel(rows('ov'), lab), vals)
k3 = rows('kc3')
for lab, vals in [('Unplanned configuration change', ['(1 / 8) 12.5%', '(1 / 1) 100%', '(4 / 7) 57%', 'ICDL-014-005']), ('Component substitution', ['(0 / 8) 0%', '-', '(5 / 8) 62.5%', 'ICDL']),
                  ('Technical deviation', ['(0 / 8) 0%', '-', '(5 / 8) 62.5%', 'ICDL']), ('Intraoperative difficulty', ['(2 / 8) 25%', '(1 / 2) 50%', '(4 / 6) 67%', 'ICDL-014-002, -007']),
                  ('Senior support', ['(2 / 8) 25%', '(1 / 2) 50%', '(4 / 6) 67%', 'ICDL / SLCT']), ('Surgeon within first', ['(7 / 8) 87.5%', '(5 / 7) 71%', '(0 / 1) 0%', 'SLCT']),
                  ('Operation outside normal hours', ['(1 / 8) 12.5%', '(1 / 1) 100%', '(4 / 7) 57%', 'ICDL-014-005']), ('Instrument or loaner set problem', ['(1 / 8) 12.5%', '(1 / 1) 100%', '(4 / 7) 57%', 'ICDL-014-002']),
                  ('Gap in the operative record', ['(1 / 8) 12.5%', '(1 / 1) 100%', '(4 / 7) 57%', 'ICDL-014-005'])]:
    fillrow(byLabel(k3, lab), vals)
for r, vals in zip(rows('lk'), [['Unplanned configuration change', 'ICDL-014-005', 'Dislocation and liner disassociation (SCML-014-07, -08)', 'Planned +6 liner not in the set; +3 used. Same case had the weekend list and the missing lot.'],
                                 ['Instrument or loaner set problem', 'ICDL-014-002', 'Subluxation symptoms at 3 months (SCML-014-09)', 'Trial liner missing from the loaner set; liner chosen without a trial reduction.']]):
    fillrow(r, vals, 0)
for r, vals in zip(rows('ex', 0), [['S-01', '(3) 37.5%', '(1 / 3) 33%', '20%', '(1 / 3) 33%', 'PI; experienced'], ['S-02', '(3) 37.5%', '(2 / 3) 67%', '40%', '(2 / 3) 67%', 'Sub-I'], ['S-03', '(2) 25%', '(2 / 2) 100%', '40%', '(2 / 2) 100%', 'New in Oct; both cases with a complication']]):
    fillrow(r, vals, 0)
for r, vals in zip(rows('ex', 1), [['Liner 36 +3 · lot GS-L36-2607', '(2) 25%', '(2 / 2) 100%', '40%', 'Includes ICDL-014-005 (dislocation)'], ['Liner 36 +6', '(4) 50%', '(1 / 4) 25%', '20%', ''], ['Glenosphere 36 · all cases', '(8) 100%', '(5 / 8) 62.5%', '100%', 'No comparison possible']]):
    fillrow(r, vals, 0)
for r, vals in zip(rows('ex', 2), [['Cuff tear arthropathy, primary', '(5) 62.5%', '(2 / 5) 40%', '40%', ''], ['Fracture sequelae, primary', '(2) 25%', '(2 / 2) 100%', '40%', 'Both instability events'], ['Massive cuff tear with arthritis', '(1) 12.5%', '(1 / 1) 100%', '20%', '']]):
    fillrow(r, vals, 0)
D = {'T1': ('Instability > 10% at any time point', 'Site rule, 20 Aug 2026 (POT)', '(1 / 5) 20% at 6 wk; (1 / 2) 50% at 3 mo', 'Yes'),
     'T2': ('Higher at a later time point, 2+ events', 'Site rule, 20 Aug 2026', 'Instability 0% → 20% → 50%', 'Yes'),
     'T3': ('Double the previous review', 'Site rule, 20 Aug 2026', 'Instability 0 → 2 events', 'Yes'),
     'T4': ('Any first event in a category', 'Site rule, 20 Aug 2026', 'Instability; device performance', 'Yes'),
     'T5': ('Share of complications 2x share of procedures, 2+ events', 'Site rule, 20 Aug 2026', 'S-03: 40% vs 25% (1.6x)', 'No'),
     'T6': ('Same rule as T5', 'Site rule, 20 Aug 2026', 'Liner +3: 40% vs 25% (1.6x)', 'No'),
     'T7': ('Assessable from 6 cases per surgeon', 'Sponsor guidance GS-RA-01', 'All surgeons have 3 cases or fewer', 'Not assessable'),
     'T8': ('Rate with marker 2x without, 2+ events', 'Site rule, 20 Aug 2026', 'Each marker has 1 event only', 'No'),
     'T9': ('2 serious events, same category, 90 days', 'CIP 11.6', '1 SADE (dislocation)', 'No'),
     'T10': ('2 deficiencies of the same type', 'CIP 11.6', '1 (liner disassociation)', 'No')}
for r in rows('dt'):
    td = r.findall('td'); a = td[0].text_content().strip()
    if a in D:
        lim, srcl, val, met = D[a]; put(td[3], lim); put(td[4], srcl); put(td[5], val); tick(td[6], met)
f = rows('ft')[0].findall('td')
put(f[0], 'S-01'); put(f[1], 'T1-T4 · SCML-014-07, -08, -09')
put(f[2], 'Two instability events in 8 procedures, both after discharge and rising at later visits. One with liner disassociation after an unplanned +3 liner (planned +6 missing from the set); one after a loaner set without a trial liner. Fracture sequelae cases and S-03 overlap.')
tick(f[3], 'Device, component or lot', 'Procedure or technique', 'Surgeon or learning curve'); tick(f[4], 'Sent on (see H)')
put(f[5], 'No new instability in the next 8 procedures; full liner range and trial liners in every set (ICDL); CSST monthly for 3 months.')
g = rows('gt')[0].findall('td')
put(g[0], 'S-01 · CSST-014-01'); put(g[1], 'No further nerve injury in the next 4 procedures'); put(g[2], '0 nerve injuries in 4 procedures (Oct)'); tick(g[3], 'Effective'); put(g[4], 'Close; keep in the routine count')
H = {'SLCT': ('SLCT S-03 review, 5 Nov 2026', 'Sent'), 'Sponsor device-deficiency route': ('GS-DD-014-0012, 28 Oct 2026', 'Sent'), 'SART': ('SART-014-005; SART-014-006 opened, 30 Oct', 'Sent'),
     'SRR': ('SRR-002 reopened; SRR-006, 31 Oct', 'Sent'), 'CAPA log': ('First occurrence; no failed response yet', 'Not required'), 'POT': ('POT review 3 Nov: S-03 proctored for 3 cases', 'Sent'), 'PIR / IMC': ('IMP v1.1 CH-03: CSST monthly', 'Sent')}
for r in rows('ht'):
    td = r.findall('td'); a = td[0].text_content().strip()
    if a in H: put(td[2], 'S-01' if H[a][1] == 'Sent' else '-'); put(td[3], H[a][0]); tick(td[4], H[a][1])
dt = rows('dtb'); tick(dt[0], 'Signal sent on'); put(dt[1].findall('td')[1], '30 Nov 2026, then monthly to January: instability by time point, liner +3 cases, S-03 cases, liner range in every set.')
wb = doc.xpath('//div[contains(@class,"lim")]')[0]
put(wb, 'Very small numbers: 8 procedures, 2 participants at 3 months; the percentages move a lot with one event and no test of difference is attempted. The explanted liner has not yet been returned to the sponsor, so the device route has no result yet. ICDL-014-005 lot was read from the explant label.')
put(wb, 'Rationale: three triggers on instability point to the same few cases; device, technique and the new surgeon cannot be separated yet. Each route was sent so that each owner can test its own explanation.')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '   '; line.append(ik); line.append(E('span', 'demo-fill', date))
sign('Reviewer', 'Maria Silva / Study Coordinator', 'M. Silva', '31 Oct 2026')
sign('PI / accountable approver', 'Dr Alex Morgan / PI', 'A. Morgan', '3 Nov 2026')
F = '/tmp/claude-0/-home-user-Master-Thesis/c35b56ea-6e37-57ca-a7f6-4cae380cc50e/scratchpad/fonts/'
hand = base64.b64encode(open(F + '4UaErEJDsxBrF37olUeD_xHMwps.ttf', 'rb').read()).decode()
sig = base64.b64encode(open(F + 'dancing.ttf', 'rb').read()).decode()
st = etree.SubElement(doc.find('.//head'), 'style')
st.text = ('@font-face{font-family:"SimHand";font-weight:400 700;src:url(data:font/ttf;base64,' + hand + ')}'
           '@font-face{font-family:"SimSig";src:url(data:font/ttf;base64,' + sig + ')}'
           '.demo-fill,.demo-entry{font-family:"Segoe Print","Bradley Hand","Comic Sans MS","SimHand",cursive!important;color:#174f88!important;font-weight:600!important;line-height:1.18!important}'
           'td .demo-fill{display:block;text-align:center!important;font-size:9.2px}.kc2 td .demo-fill,.dt td .demo-fill,.ft td .demo-fill{font-size:8.6px}td:has(>.demo-fill){text-align:center!important}.demo-fill.inl{display:inline!important}td.left:has(>.demo-fill.inl){text-align:left!important}'
           '.meta-cell .demo-entry{display:block;text-align:left;font-size:10px;margin-top:3px}'
           '.wbox.lim .demo-fill{display:block;font-size:10.4px;line-height:1.45!important;margin-top:8px}'
           '.sig-ink{font-family:"Snell Roundhand","Brush Script MT","Segoe Script","Lucida Handwriting","SimSig",cursive!important;font-size:15px!important;color:#174f88}')
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
