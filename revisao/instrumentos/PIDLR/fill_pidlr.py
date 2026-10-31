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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.4'
doc.find('.//title').text = 'PIDLR v0.4 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('PIDLR ID / revision', 'PIDLR-014-01 / r0'),
             ('Period covered / close-out date', '16 Jun 2026 to 30 Jun 2028 / 15 Sep 2028'), ('Evidence cut-off', '15 Sep 2028'), ('Document owner / role', 'Maria Silva / Study Coordinator'), ('PI', 'Dr Alex Morgan'),
             ('Reason for an early closure (if any)', 'Not applicable: completed as planned')]:
    meta(k, v)
mg = doc.xpath('//section[contains(@class,"meta-grid")]')[0]; tick(mg, 'Completed', 'Final')
for n, st in enumerate(doc.xpath('//section[contains(@class,"sheet-strip")]')):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        be.getparent().replace(be, E('span', 'demo-entry', {'PIDLR ID': 'PIDLR-014-01', 'Study / site': 'GLENOS-01 / 014', 'Investigation status / evidence cut-off': 'Completed / 15 Sep 2028', 'Sheet no. / total sheets': '1 of 1'}[lab]))
for r, b in zip(rows('bt'), [('MRL-014, milestones 1 to 3', 'Adequate', ''), ('PIR-014-2026-07 to -10', 'Adequate', ''), ('IMC-014-01, -02', 'Adequate', ''), ('CAPA-LOG-014, review 2', 'Adequate', ''),
                             ('SRR-014 v4', 'Adequate', ''), ('SART-014-001 to -005; CSST-014-02', 'Adequate', ''), ('FUCR-014-2026-07 to -10', 'Limited', 'October closed late (3 Nov); causes only partly reviewed'), ('SLCT S-01 to S-03', 'Adequate', 'Only 2 cases for S-03')]):
    td = r.findall('td'); put(td[1], b[0]); tick(td[2], b[1]); put(td[3], b[2])
PH = [('Imaging qualified before activation', 'SIRR-014 r1; core lab letter IQ-014, 9 Jun', 'Strength', 'L-01', ''),
      ('Every person released before study tasks', 'S-03 did 4 tasks before release; CAPA-014-01 reopened', 'Lesson', 'L-02', ''),
      ('Every decision evidenced before enrollment', '8 of 8 PSEAR decisions; one PI resolution (PSEAR-014-019, H-1)', 'Strength', 'L-03', ''),
      ('Sets complete; components traced', 'Labels 100%; 2 cases without trial liners (ICDL-014-002, -007)', 'Lesson', 'L-04', ''),
      ('Visits in window and complete', 'October 5 of 7 (FUCR-014-2026-10); research nurse away', 'Lesson', 'L-05', ''),
      ('Records reconciled; obligations handed over', 'SIFSL and PSEAR reconciled; 2 transfers still open at close-out', 'Strength', '', ''),
      ('', 'This debrief', 'No lesson', '', ''),
      ('Cases reported on time', '2 of 2 within the CIP interval (PIR indicator 4)', 'Strength', '', 'Too few cases to call a practice')]
for r, p in zip(rows('ct'), PH):
    td = r.findall('td'); put(td[1], p[0]); put(td[2], p[1]); tick(td[3], p[2]); put(td[4], p[3]); put(td[5], p[4])
DM = {0: ('PI review of escalations within a week (POT)', '', '', 'POT-014-07, -08', ''),
      2: ('Label sheet traceability, 8 of 8 cases', 'Loaner sets without trial liners', 'Check sheet copied from the supplier list and never reviewed (CAPA-014-04 analysis)', 'ICDL-014-002, -007; CAPA-014-04', 'L-04'),
      5: ('Reminder call before visits (no late visits for scheduling)', 'No cover during the nurse\'s absence', 'One research nurse for questionnaires and data entry', 'FUCR-014-2026-10; IMC-014-02', 'L-05'),
      7: ('', 'Two transcription errors in October', 'Same absence (hypothesis supported by timing)', 'CAPA-014-03', 'L-05')}
for i, r in enumerate(rows('dt')):
    if i in DM:
        td = r.findall('td')
        for k in range(5): put(td[k + 1], DM[i][k])
LS = [('L-01', 'Imaging', 'Keep', 'Test the transfer of the largest image set before activation', 'SIRR-014 r0, r1 (TT-014-01 failed, -02 passed)', 'Imaging start-up instruction', 'Medium'),
      ('L-02', 'Delegation', 'Change', 'Check the TRE release before a name goes on any task roster', 'CAPA-014-01; IMC-014-02', 'Delegation SOP', 'High'),
      ('L-03', 'Enrollment', 'Keep', 'Radiologist second read for imaging criteria; the PI settles a disagreement', 'PSEAR-014-019', 'Eligibility instruction', 'Low'),
      ('L-04', 'Surgery', 'Add', 'Check each loaner set against the full component list, trial liners included, the day before', 'ICDL-014-002, -007; CAPA-014-04; PIR E-1', 'OR checklist; sponsor; HUMERA-02', 'High'),
      ('L-05', 'Follow-up', 'Add', 'Name a trained backup for questionnaires and data entry before any planned absence', 'FUCR-014-2026-10; IMC-014-02', 'SRR R-13; staffing plan', 'Medium'),
      ('L-06', 'Safety', 'Limit', 'A link between fracture-sequelae cases and instability cannot be judged with 2 cases', 'CSST-014-02 E3; PIR E-3', 'CSST; sponsor', 'Medium')]
for r, l in zip(rows('et'), LS):
    td = r.findall('td'); put(td[0], l[0]); put(td[1], l[1]); tick(td[2], l[2]); put(td[3], l[3]); put(td[4], l[4]); put(td[5], l[5]); tick(td[6], l[6])
TR = [('L-02', 'Site practice', 'Add the release check to the delegation SOP', 'SOP-DEL-03 v4', 'Coordinator', '30 Nov 2026', 'Applied'),
      ('L-04', 'Site practice', 'Loaner-set check against the full list in the site OR procedure', 'OR-SOP-11 v5', 'OR nurse lead', '31 Oct 2028', 'Applied'),
      ('L-04', 'Sponsor', 'Trial liners in every loaner set of the sponsor', 'Close-out letter GS-CL-014', 'PI', '30 Sep 2028', 'Accepted'),
      ('L-05', 'Site practice', 'Staffing plan with a named backup', 'Site staffing plan v2', 'Coordinator', '31 Dec 2026', 'Applied'),
      ('L-01', 'Future study', 'Large-dataset transfer test in the imaging start-up checklist', 'SI-IMG-START v2 (draft)', 'Radiology tech', '15 Dec 2028', 'Planned')]
for r, t in zip(rows('ft'), TR):
    td = r.findall('td'); put(td[0], t[0]); tick(td[1], t[1]); put(td[2], t[2]); put(td[3], t[3]); put(td[4], t[4]); put(td[5], t[5]); tick(td[6], t[6])
g = rows('gt')[0].findall('td')
for k, v in enumerate(['L-06', 'Whether fracture-sequelae cases have more instability', '3 such cases in the whole investigation', 'Sponsor final report; complication review of the next shoulder study · Sub-I', 'First review of the next study']): put(g[k], v)
for r, h in zip(rows('ht'), [('L-02', 'Delegation SOP', 'Release checked before a name goes on a roster', 'SOP-DEL-03 v4 · 30 Nov 2026', 'Applied', ''),
                             ('L-04', 'OR procedure', 'Every loaner set checked against the full list, trial liners included', 'OR-SOP-11 v5 · 20 Oct 2028', 'Applied', ''),
                             ('L-04', 'Sponsor', 'Trial liners in every loaner set', 'GS-CL-014 · 30 Sep 2028', 'Not yet applied', 'PI; sponsor answer'),
                             ('L-05', 'Staffing plan', 'Named backup for questionnaires and data entry', 'Staffing plan v2 · Dec 2026', 'Applied', ''),
                             ('L-01', 'Imaging start-up', 'Large-dataset transfer test added', 'SI-IMG-START v2 draft · Sep 2028', 'Partly applied', 'Radiology tech · 15 Dec 2028')]):
    td = r.findall('td')
    for k in (0, 1, 2, 3, 5): put(td[k], h[k])
    tick(td[4], h[4])
rows('io')[1].xpath('.//span[@class="check"]')[0].set('class', 'check selected')
idr = rows('id')
for k, v in enumerate(['L-01 (radiology tech), L-04 sponsor part (PI)', 'SOP-DEL-03 v4, 30 Nov 2026; OR-SOP-11 v5, 20 Oct 2028', 'HUMERA-02 PI, memo M-014-41, 30 Sep 2028', 'ISF tab 3 / PIDLR-014-01; kept as long as the trial master file']):
    put(idr[k].findall('td')[1], v)
idr[4].findall('td')[1].append(E('span', 'demo-fill txt', 'Six lessons, each with evidence and a destination. Three are applied in site procedures; the imaging change is in draft and the sponsor has not yet answered on the loaner sets, both with an owner and a date. L-06 stays a residual limitation for the sponsor and the next shoulder study.'))
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Document owner', 'Maria Silva / Study Coordinator', 'M. Silva', '30 Sep 2028')
sign('Principal Investigator', 'Dr Alex Morgan', 'A. Morgan', '30 Sep 2028')
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
