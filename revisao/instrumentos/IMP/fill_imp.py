# Simulated (filled) IMP v1.0: GLENOS-01, Riverside 014, plan revision v1.1 after the second internal review and the SART-014-005 case.
import sys
from lxml import html as LH, etree
SRC, OUT = sys.argv[1], sys.argv[2]
doc = LH.document_fromstring(open(SRC).read())
def E(tag, cls, text):
    e = etree.Element(tag); e.set('class', cls); e.text = text; return e
def meta(label, val):
    cells = [c for c in doc.xpath('//div[contains(@class,"meta-cell")]') if c.find('b') is not None and c.find('b').text_content().strip() == label]
    assert cells, label
    for c in cells:
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
def rows(cls, idx=0):
    return doc.xpath(f'//table[contains(concat(" ",@class," ")," {cls} ")]')[idx].xpath('./tbody/tr')
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v1.0'
doc.find('.//title').text = 'IMP v1.0 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('IMP ID', 'IMP-014'),
             ('Version', 'v1.1'), ('Supersedes (ID / version)', 'IMP-014 v1.0 (approved 12 Aug 2026)'), ('Effective from', '4 Nov 2026'),
             ('Next scheduled plan review', '4 May 2027'), ('Plan owner / role', 'Maria Silva / Study Coordinator'), ('Approved by / date', 'Dr Alex Morgan / 3 Nov 2026'),
             ('Controlled location', 'Investigator site file, tab 3 (Quality) / IMP-014')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Approved')
for row, val in zip(rows('bt'), ['GLENOS-01 at site 014 only; from start-up to close-out.',
        'CIP v4.2; imaging manual v2.0; SRR-014 v3; delegation log rev. 7; source document map v1.2.',
        'Sponsor CRA visit every 8 weeks with 20% source check of endpoint fields. Findings arrive by follow-up letter to the PI and the coordinator.',
        'One coordinator does most data entry. Radiology archive open to the team on weekdays only. PI on leave 27 Oct to 2 Nov 2026.',
        'Logged in the IMC as unavailable; the next unit in the list is taken. If more than 1 in 5 picked units are unavailable, the check is rated not assessable.',
        'Sponsor central image reading; sponsor vigilance and literature screening (until check 11 is included); hospital sterile services audits.']):
    put(row.findall('td')[1], val)
ib = doc.xpath('//span[@class="inline-blank"]')[0]; ib.getparent().replace(ib, E('span', 'demo-entry', ' 3 '))
# C: checks in scope (rows 1-14 over two tables)
C = [('Included', 'Signed consent on the version approved on the signing date; PI eligibility sign-off dated before surgery', 'Consent forms, PSEAR, EC approvals', 'R-01, R-02', ''),
     ('Included', 'Each task in ICDL, PFVR and IQL done by someone delegated and released on that date', 'Delegation log, TRE, SCR', 'R-03, R-04, R-05', ''),
     ('Included', 'Expiry, package integrity and storage temperature recorded before opening', 'ICDL p. 1, accountability log, storage temperature log', 'R-06', ''),
     ('Included', 'Every implanted component has REF and lot in the ICDL label sheet, accountability log and CRF', 'ICDL label sheet, accountability log, CRF implant page', 'R-07, R-08, R-17', ''),
     ('Included', 'Loaner set checked complete the day before; any substitution recorded', 'ICDL readiness section, loaner-set check sheet', 'R-09', ''),
     ('Included', 'Note states final configuration, liner size and offset, and any deviation', 'Operative note, ICDL', 'R-10', ''),
     ('Included', 'Post-op and 3-month radiographs in window, required views, usable', 'IQL, PACS', 'R-11, R-12', ''),
     ('Included', 'Visits in window with Constant score and ASES complete', 'PFVR, FUCR', 'R-13', ''),
     ('Included', 'Constant score, ASES and implant position fields match the source', 'Source questionnaires, PFVR, CRF', 'R-14', ''),
     ('Included', 'Operative note within 24 h, CRF entry within 5 working days, queries within 10 days, SAE within the CIP limit', 'EDC audit trail, query report, SART', 'R-15, R-16', ''),
     ('Deferred until:', '', 'Sponsor safety letters, field notices', 'R-18', 'Sponsor screens literature and vigilance (CIP §12.4). Agreed by PI, 12 Aug 2026. Include at the first sponsor safety letter or any field notice on GLENOS.'),
     ('Included', 'CSST review held as planned and each signal sent on with a recipient ID', 'CSST, SCML', 'R-17, R-19', ''),
     ('Included', 'Explanted components labeled, quarantined and returned to the sponsor with an RMA number', 'SART, explant log, RMA forms', 'R-17', ''),
     None]
lt = rows('lt', 0) + rows('lt', 1)
for row, c in zip(lt, C):
    if not c: continue
    tds = row.findall('td'); tick(tds[2], c[0])
    for td, val in zip(tds[3:], c[1:]): put(td, val)
put(lt[12].findall('td')[1], 'Explant handling and return')
# D: schedule, reviewer and sample
D = [('Case count', 'Each of the first 5 inclusions, then quarterly', 'Re-consent due after an amendment', 'Research nurse (P-04) / PI', 'Participant; about 4 per quarter', 'All new inclusions', 'All (fewer than 10)', 'Any version mismatch: all participants'),
     ('Calendar', 'Quarterly', 'New staff member or new task delegated', 'Sub-I (P-02) / PI', 'Study task; about 60 per quarter', 'Every 5th task in the task list, random start', '10 tasks', 'A task done before release: all tasks of that person'),
     ('Each event', 'Every procedure', 'Temperature excursion or damaged package', 'OR nurse lead (P-08) / coordinator', 'Procedure; about 4 per quarter', 'All', 'All', ''),
     ('Each event', 'Within 5 days of each procedure', 'Lot or REF missing in any record', 'Coordinator (P-06) / research nurse', 'Implanted component; about 16 per quarter', 'All', 'All', ''),
     ('Case count', 'First 3 procedures per surgeon, then every 5th', 'Instrument malfunction or substitution', 'OR nurse lead / Sub-I', 'Procedure', 'Every 5th procedure by date', 'At least 1 per quarter', 'Unrecorded substitution: all since last review'),
     ('Case count', 'First 3 per surgeon, then quarterly', 'A new surgeon starts', 'Sub-I / PI', 'Operative note; about 4 per quarter', 'Latest note of each surgeon', '2 per quarter', 'Liner size or offset missing: all'),
     ('Calendar', 'Monthly', 'More than 1 in 5 image sets repeated', 'Radiology research tech (P-09) / research nurse', 'Image set; about 8 per month', 'All', 'All (fewer than 10)', ''),
     ('Calendar', 'Quarterly', 'Missed visit', 'Research nurse / coordinator', 'Visit; about 12 per quarter', 'Random 6 from the PFVR visit list', '6; all if fewer than 10', 'A missed endpoint component: all'),
     ('Calendar', 'Quarterly', 'Discrepancy in an endpoint field', 'Research nurse (P-04) / Sub-I', 'Endpoint field; about 120 per quarter', 'All fields of 5 visits picked at random', '5 visits; all affected fields after a discrepancy', '2 discrepancies in one review'),
     ('Calendar', 'Monthly', 'An SAE reported late', 'Coordinator / PI', 'Item with a deadline', 'All SAE reports; queries open over 10 days', 'All SAE; 10 queries', 'One late SAE report: every deadline that month'),
     ('Milestone', 'From the first sponsor safety letter', 'Field notice on GLENOS', 'PI / Sub-I', 'Search', '', '', ''),
     ('Calendar', 'Quarterly; monthly for 3 months after a CSST signal', 'SADE, or 2 dislocations in a quarter', 'Sub-I / PI', 'CSST review', 'All', 'All', ''),
     ('Each event', 'Each explant', 'Explant not returned within 30 days', 'Coordinator / OR nurse lead', 'Explanted component', 'All', 'All', ''),
     None]
dt = rows('dt', 0) + rows('dt', 1)
for row, d in zip(dt, D):
    if not d: continue
    tds = row.findall('td'); tick(tds[2], d[0])
    for td, val in zip(tds[3:], d[1:]): put(td, val)
put(dt[12].findall('td')[1], 'Explant handling and return')
# E: criteria
EC = [('Consent and PI sign-off exist for every participant reviewed', 'Signed, dated pages present; version legible', 'No procedure before consent; no surgery before PI sign-off', 'PSEAR IDs, consent version'),
      ('Each sampled task matches a delegated, released person', 'Initials traceable in the delegation log', 'No task done before the release date', 'Delegation log rev., TRE IDs'),
      ('Checks recorded before opening for every device', 'ICDL p. 1 signed; temperature log for the day', 'No expired or breached device used', 'ICDL IDs'),
      ('REF and lot in all three records', 'Label sheet attached to the ICDL', 'Records agree; implanted matches planned or the change is explained', 'ICDL IDs, CRF pages'),
      ('Set check done the day before', 'Signed check sheet', 'No delay or substitution from a missing instrument', 'ICDL IDs'),
      ('Note signed within 24 h', 'Configuration, sizes and deviations stated', 'A reader can rebuild the procedure from the note alone', 'Note dates, ICDL IDs'),
      ('Images acquired in window', 'IQL entry with views and quality', 'Usable for the endpoint without repeat', 'IQL IDs'),
      ('Visit done in window', 'PFVR complete, endpoint components marked', 'No endpoint component missing', 'PFVR IDs'),
      ('Fields compared for each sampled visit', 'Source questionnaire kept', 'No discrepancy, or each corrected and explained', 'PFVR IDs, CRF pages'),
      ('Dates retrieved for each item', 'Audit trail export kept', 'All within the limits in C', 'Report export date'),
      ('', '', '', ''),
      ('Review held in the planned month', 'Signed CSST with snapshot ID', 'Each signal has a recipient ID', 'CSST IDs'),
      ('Explant labeled and quarantined on the day', 'Explant log and RMA form', 'Returned within 30 days with lot readable', 'SART IDs, RMA numbers'),
      None]
ect = rows('ec', 0) + rows('ec', 1)
for row, e in zip(ect, EC):
    if not e: continue
    tds = row.findall('td')
    for td, val in zip(tds[2:], e): put(td, val)
put(ect[12].findall('td')[1], 'Explant handling and return')
# F: triggers
F = [('Yes', '3, 4, 6, 10, 12, 13', 'PI', '5'), ('Yes', '5, 6, 12', 'PI', '10'), ('Yes', '1, 2 and the related check', 'Coordinator', '10'), ('Yes', '8, 9', 'Research nurse', '10'),
     ('Yes', '7', 'Radiology tech', '14'), ('Yes', '3, 5', 'OR nurse lead', '5'), ('Yes', '1, 2, 8', 'Coordinator', '30'), ('Yes', '2', 'PI', '14'),
     ('Yes', 'As named in the finding', 'PI', '14'), ('Yes', 'The check that raised it', 'PI', '14'), ('Yes', '4, 13', 'Coordinator', '5')]
gtt = rows('gtt')
for row, (o, a, b, c) in zip(gtt, F):
    tds = row.findall('td'); tick(tds[1], o); put(tds[2], a); put(tds[3], b); put(tds[4], c)
put(gtt[10].findall('td')[0], 'Explant not returned to the sponsor within 30 days')
# G: responses
G = [('None; the result stays in the IMC.', 'Reviewer'), ('Fixed at the review; IMC action log with date.', 'Reviewer'),
     ('Corrected in the owning record (ICDL, PFVR, IQL…); rechecked at the next review.', 'Owner of the record'),
     ('IMC action log; coordinator decides within 5 days whether it is a deviation to report.', 'Coordinator'),
     ('CAPA log; SRR rating revisited at the next SRR review.', 'PI'), ('Repeated within 30 days, or with a larger sample.', 'Reviewer'),
     ('CAPA log; PI decision recorded in the POT; SRR updated.', 'PI'), ('PI and SART the same day; sponsor as the CIP requires; IMC keeps only the reference.', 'PI / coordinator')]
for row, (a, b) in zip(rows('ht'), G):
    tds = row.findall('td'); put(tds[1], a); put(tds[2], b)
# H: readiness
H = [('Yes', 'Released 30 Oct 2026 (TRE-014-11 for P-09)'), ('No', 'OR nurses not yet briefed on check 13: briefing 11 Nov 2026 (M. Silva)'), ('Yes', 'IMC-014-03 set up on 3 Nov 2026')]
it = rows('it')
for row, (o, v) in zip(it, H):
    tds = row.findall('td'); tick(tds[1], o); put(tds[2], v)
put(it[3].findall('td')[1], 'IMC-014-03 due 30 Nov 2026 (first review under v1.1); v1.0 first review IMC-014-01 held 30 Sep 2026 after inclusion 3')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    f = sg.xpath('./div[@class="sig-field"]'); f[0].append(E('span', 'demo-fill', name))
    line = f[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '   '; line.append(ik); line.append(E('span', 'demo-fill', date))
sign('Plan owner', 'Maria Silva / Study Coordinator', 'M. Silva', '3 Nov 2026')
sign('Principal Investigator', 'Dr Alex Morgan', 'A. Morgan', '3 Nov 2026')
# I: changes
I = [('CH-01', 'D · 9', '5 visits per quarter, no expansion', '5 visits; all affected fields after a discrepancy; expand at 2', 'IMC-014-02: 3 ASES discrepancies; CAPA-014-003', '4 Nov 2026', 'A. Morgan'),
     ('CH-02', 'C, D, E · 13; F · 11', 'No check on explants', 'Check 13 added: explant handling and return', 'SART-014-005: explant lot missing in the ICDL; SRR R-17', '4 Nov 2026', 'A. Morgan'),
     ('CH-03', 'D · 12', 'Quarterly', 'Monthly for 3 months after any CSST signal', 'CSST-014-02 dislocation signal', '4 Nov 2026', 'A. Morgan'),
     ('CH-04', 'D · 2', 'Reviewer: coordinator', 'Reviewer: Sub-I; the coordinator keeps the log', 'IMC-014-02: coordinator reviewed her own delegation entries', '4 Nov 2026', 'A. Morgan')]
for row, r in zip(rows('jt'), I):
    for td, val in zip(row.findall('td'), r): put(td, val)
st = etree.SubElement(doc.find('.//head'), 'style'); st.text = '.lt .demo-fill,.gtt .demo-fill,.ht .demo-fill,.it .demo-fill,.jt .demo-fill,.bt .demo-fill{font-size:8.6px;line-height:1.2}'
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
