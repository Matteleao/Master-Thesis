# Simulated (filled) IMC v1.5: GLENOS-01, Riverside 014, second scheduled review IMC-014-02 under IMP-014 v1.0 (cut-off 15 Oct 2026).
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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v1.5'
doc.find('.//title').text = 'IMC v1.5 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('IMC ID', 'IMC-014-02'),
             ('IMP ID / version applied', 'IMP-014 v1.0'), ('Review period / data cut-off', '12 Aug to 15 Oct 2026 / 15 Oct 2026'), ('Date of review', '21 Oct 2026'),
             ('Trigger or reason (if not scheduled)', 'Not applicable: second quarterly review set in the IMP'), ('Reviewer / role', 'Dr Lena Ortiz / Sub-investigator (P-02)'),
             ('Controlled location', 'Investigator site file, tab 3 (Quality) / IMC-014-02')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Scheduled')
# D: scope and sample
D = [('Yes', '3 of 3', 'PSEAR-014-006 to -008; consent v3.0', ''),
     ('Yes', '14 of 58', 'Task list 12 Aug to 15 Oct; TRE-014-01 to -11', 'Sample of 10 widened to all 4 tasks of S-03 (IMP expansion trigger).'),
     ('Yes', '4 of 4', 'ICDL-014-005 to -008; storage log Aug to Oct', ''),
     ('Yes', '16 of 16', 'ICDL label sheets, accountability log, CRF implant pages', ''),
     ('Yes', '1 of 4', 'ICDL-014-007 (every 5th by date)', ''),
     ('Yes', '2 of 4', 'Latest note of S-01 and S-03', ''),
     ('Yes', '8 of 8', 'IQL-014-021 to -028', ''),
     ('Yes', '6 of 11', 'PFVR-014-014 to -024, random 6', ''),
     ('Yes', '5 visits, 118 fields', 'PFVR-014-015, -017, -019, -021, -023; CRF', ''),
     ('Yes', '10 queries, 1 SAE', 'Query report 15 Oct; SART-014-004', ''),
     ('No', '', '', 'Deferred in IMP-014 v1.0: sponsor screens literature and vigilance (CIP §12.4).'),
     ('Yes', '1 of 1', 'CSST-014-01 (30 Sep 2026); SCML snapshot 30 Sep', ''),
     ('No', '', '', 'No explant in the period; check stays in the IMP.'),
     None]
for i, (r, d) in enumerate(zip(rows('dt'), D)):
    if not d: continue
    td = r.findall('td'); tick(td[2], d[0]); put(td[3], d[1]); put(td[4], d[2]); put(td[5], d[3])
put(rows('dt')[12].findall('td')[1], 'Explant handling and return')
# E: review
E5 = [('Complete', 'Adequate', 'Effective', '3 participants consented on v3.0 before any procedure; PI sign-off dated before surgery.', 'None'),
      ('Complete', 'Adequate', 'Not effective', 'S-03 entered ICDL-014-007 on 2 Oct and 3 more tasks before release on 6 Oct (TRE-014-11).', 'A-02-01, A-02-02 · POT-014-07 · PI, coordinator · 31 Oct'),
      ('Complete', 'Adequate', 'Effective', 'All 4 devices checked before opening; no expiry or storage breach.', 'None'),
      ('Complete', 'Adequate', 'Observation', 'Glenosphere lot in CRF of ICDL-014-006 mistyped; label and log agree. Corrected at review (Q-014-31).', 'None; corrected'),
      ('Complete', 'Adequate', 'Not effective', 'Loaner set for ICDL-014-007 had no trial liners; set check sheet does not list them.', 'A-02-03 · SRR R-09 · OR nurse lead · 4 Nov'),
      ('Complete', 'Partial', 'Observation', 'Note of S-03 (ICDL-014-007) does not state liner offset (Q-014-33).', 'Q-014-33 · Sub-I · 28 Oct'),
      ('Complete', 'Adequate', 'Observation', 'IQL-014-026 taken 3 days late; usable, reason recorded.', 'None; watch at next review'),
      ('Complete', 'Adequate', 'Observation', 'PFVR-014-019: ASES missing at 6 weeks; recovery started.', 'A-02-04 · research nurse · 5 Nov'),
      ('Complete', 'Adequate', 'Not effective', '2 Constant scores transcribed wrongly (PFVR-014-017, -021); both corrected. Expansion trigger met.', 'A-02-05, A-02-06 · CAPA-014-03 · coordinator · 31 Oct'),
      ('Complete', 'Adequate', 'Observation', '4 of 10 queries open over 10 days; SAE reported in time.', 'Coordinator clears by 31 Oct'),
      None,
      ('Complete', 'Adequate', 'Effective', 'CSST-014-01 held in the planned month; one signal sent with recipient ID.', 'None'),
      None, None]
et = rows('et', 0) + rows('et', 1)
for r, e in zip(et, E5):
    if not e: continue
    td = r.findall('td'); tick(td[2], e[0]); tick(td[3], e[1]); tick(td[4], e[2]); put(td[5], e[3]); put(td[6], e[4])
put(et[12].findall('td')[1], 'Explant handling and return')
# F
FS = {'Same problem in more than one check': ('No', '', '', ''), 'Participant safety concern': ('No', '', '', ''),
      'Endpoint or data reliability concern': ('Yes', 'Transcription errors and a missing ASES (8, 9)', 'All entries since Aug second-checked', 'PIR, CAPA-014-03 · coordinator'),
      'Device traceability or deficiency concern': ('No', 'Lot error corrected at review (4)', '', ''),
      'Need for closer PI oversight': ('Yes', 'Tasks done before release (2)', 'S-03 tasks paused until released', 'POT-014-07 · PI'),
      'Need for CAPA or a change in the SRR': ('Yes', 'Trial liners missing (5); transcription (9)', 'Trial liners added to the set by hand', 'SRR R-09 update; CAPA-014-03 · coordinator')}
for r in rows('ft'):
    td = r.findall('td'); a = td[0].text_content().strip()
    if a in FS:
        s = FS[a]; tick(td[1], s[0]); put(td[2], s[1]); put(td[3], s[2]); put(td[4], s[3])
# G
GA = [('A-02-01', '2', 'Review the 4 tasks done by S-03 before release, with the PI', 'Containment', 'PI', '22 Oct 2026', 'POT-014-07', 'Open'),
      ('A-02-02', '2', 'Check the TRE release before a name goes on the task roster', 'Corrective', 'Coordinator', '31 Oct 2026', 'Delegation log rev. 8', 'Open'),
      ('A-02-03', '5', 'Add trial liners to the loaner-set check sheet', 'Preventive', 'OR nurse lead', '4 Nov 2026', 'SRR R-09', 'Open'),
      ('A-02-04', '8', 'Recover ASES for PFVR-014-019 or record the limitation', 'Corrective', 'Research nurse', '5 Nov 2026', 'PFVR-014-019', 'Open'),
      ('A-02-05', '9 / F', 'Second check of every endpoint entry since August', 'Corrective', 'Coordinator', '31 Oct 2026', 'CAPA-014-03', 'Transferred'),
      ('A-02-06', '9', 'Sample 5 more visits for endpoint agreement', 'Verification', 'Sub-I', '15 Jan 2027', 'IMC-014-03', 'Open')]
for r, g in zip(rows('gt'), GA):
    td = r.findall('td')
    for k in (0, 1, 2, 4, 5, 6): put(td[k], g[k])
    tick(td[3], g[3]); tick(td[7], g[7])
# H
h = rows('ht')
tick(h[0], 'Escalation required'); put(h[1].findall('td')[1], '2, 5, 6, 8, 9, 10')
s = E('span', 'demo-fill txt', 'Most controls worked. Two need correction: a new surgeon did study tasks before release, and the loaner set check does not cover trial liners. Endpoint transcription failed twice in 118 fields and goes to CAPA. No participant safety concern.')
h[2].findall('td')[1].append(s)
tick(h[3], 'Yes, POT ID:'); o = [x for x in h[3].xpath('.//span[contains(@class,"opt")]') if x.text_content().strip() == 'Yes, POT ID:'][0]
ins = E('span', 'demo-fill inl', ' POT-014-07'); o.append(ins)
put(h[4].findall('td')[1], '15 Jan 2027')
# I
for r, v in zip(rows('it'), [('A-01-03', '30 Sep 2026', 'IQL-014-021 to -028: no repeat needed', 'Effective', 'L. Ortiz'), ('A-02-01', '29 Oct 2026', 'POT-014-07; TRE-014-11; S-03 tasks after 6 Oct', 'Effective', 'L. Ortiz')]):
    td = r.findall('td'); put(td[0], v[0]); put(td[1], v[1]); put(td[2], v[2]); tick(td[3], v[3]); put(td[4], v[4])
tick(doc.xpath('//div[contains(@class,"cert")]')[0], 'I did not do the work I reviewed.')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '   '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Reviewer', 'Dr Lena Ortiz / Sub-investigator', 'L. Ortiz', '21 Oct 2026')
sign('Principal Investigator (if required)', 'Dr Alex Morgan', 'A. Morgan', '22 Oct 2026')
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
