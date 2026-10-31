# Simulated (filled) SRR v1.0: GLENOS-01, Riverside 014, register as reviewed on 31 Oct 2026 (after SART-014-005 and IQL-014-10).
import sys, base64
from lxml import html as LH, etree
SRC, OUT = sys.argv[1], sys.argv[2]
doc = LH.document_fromstring(open(SRC).read())
def E(tag, cls, text):
    e = etree.Element(tag); e.set('class', cls); e.text = text; return e
def meta(scope, label, val):
    cells = [c for c in scope.xpath('.//div[contains(@class,"meta-cell")]') if c.find('b') is not None and c.find('b').text_content().strip() == label]
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
def rows(cls):
    return doc.xpath(f'//table[contains(concat(" ",@class," ")," {cls} ")]')[0].xpath('./tbody/tr')
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v1.0'
doc.find('.//title').text = 'SRR v1.0 - Simulated Editable'
P = doc.xpath('//main')
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version / date', 'CIP v4.2 / 12 Jun 2026'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('SRR ID / revision', 'SRR-014 / r3'),
             ('Principal Investigator', 'Dr Alex Morgan'), ('Register owner / role', 'Maria Silva / Study Coordinator'), ('Sponsor risk information (ID / version)', 'GS-RA-01 v2 (sponsor risk assessment)'),
             ('Study phase', 'Enrollment and follow-up'), ('Date opened', '2 Jun 2026'), ('Last review / next review', '31 Oct 2026 / 31 Jan 2027'),
             ('Current reviewer / role', 'Dr R. Teixeira / Sub-investigator'), ('Controlled location', 'ISF tab 3 (Quality) / SRR-014')]:
    meta(P[0], k, v)
for n, sheet in [(2, ('Register sheet no. / total', '1 / 1')), (3, ('Register sheet no. / total', '1 / 1')), (4, ('Review log sheet no. / total', '1 / 1')), (5, ('Sheet no. / total', '1 / 1'))]:
    for k, v in [('Study / site', 'GLENOS-01 / 014'), ('SRR ID / revision', 'SRR-014 / r3'), ('Revision effective date', '31 Oct 2026'), sheet]:
        meta(P[n], k, v)
# E: identification and rating
Er = [('SRR-001', '2 Jun 2026', 'Operational / staffing', ('CtQ7', '6-week and 3-month visits done in window with the Constant score complete', 'CIP 9.2'), 'Only one physiotherapist is trained for the Constant score and is off on Tue/Thu; visits on those days lose the strength measurement.', 'Visits booked Mon/Wed/Fri where possible.', ['2', 'N/A', 'N/A', 'N/A', '3', '1'], 'High'),
      ('SRR-002', '2 Jun 2026', 'Device accountability', ('CtQ4', 'GLENOS liners kept apart from marketed liners of the same size', 'CIP 7.4; GS-RA-01 item 6'), 'Study and marketed liners share shelf B in the OR store, in similar boxes; a wrong liner may be implanted.', 'OR nurse reads the label aloud at picking.', ['2', '2', '2', '3', '2', '2'], 'High'),
      ('SRR-003', '2 Jun 2026', 'Device accountability', ('CtQ4', 'every implanted component reconciled to the participant before case closure', 'CIP 8.3'), 'UDI copied from the OR team without a second check; a missing lot is not caught before case closure.', 'OR sticker sheet; same-day reconciliation by the coordinator.', ['2', '2', '1', '3', '3', '2'], 'High'),
      ('SRR-004', '2 Jun 2026', 'Safety / clinical event', ('CtQ10', 'SAE reported to the sponsor within 24 h of site awareness', 'CIP 11.3'), 'Only the coordinator uses the EDC safety form; when she is away nobody can report.', 'Sub-I listed as backup in the delegation log (not trained on the form).', ['2', '3', 'N/A', 'N/A', '2', '2'], 'High'),
      ('SRR-005', '30 Oct 2026', 'Imaging / assessment workflow', ('CtQ9', 'day-1 AP shows liner seating in a reproducible position', 'Imaging manual v2.0, 4.2'), 'Day-1 AP is taken on the ward with the arm in a sling; rotation cannot be controlled and seating is not visible.', 'None specific; local read of each set (IQL).', ['3', '2', 'N/A', 'N/A', '3', '3'], 'High'),
      ('SRR-006', '30 Oct 2026', 'Device accountability', ('CtQ4', 'explanted components quarantined and returned with the lot readable', 'CIP 7.9'), 'No local explant procedure: the liner explanted on 28 Oct stayed unlabeled in theatre for two days.', 'Coordinator bagged and labeled it on 30 Oct (ad hoc).', ['2', '2', 'N/A', '3', '2', '3'], 'High')]
for row, r in zip(rows('ft'), Er):
    td = row.findall('td')
    for t, v in zip(td[:3], r[:3]): put(t, v)
    for lab, v in zip(td[3].xpath('./span[contains(@class,"lab")]'), r[3]):
        val = E('span', 'demo-fill fac', ' ' + v); lab.addnext(val); val.addnext(etree.Element('br'))
    put(td[4], r[4]); put(td[5], r[5])
    for t, v in zip(td[6:12], r[6]): put(t, v)
    tick(td[12], r[7])
# F: ownership, action and status
Fr = [('SRR-001', 'Physio lead', 'Any Tue/Thu visit without strength measurement', 'Train a second physiotherapist · physio lead · 31 Aug', 'TRE-014-09; PFVR', 'None needed', 'Controlled', 'Effective', '31 Aug / 31 Jan'),
      ('SRR-002', 'OR nurse lead', 'Any liner picked from the wrong bin; any near miss', 'Separate locked, labeled bin · OR nurse lead · 30 Jun', 'ICDL readiness; IMP check 5', 'None needed', 'Controlled', 'Effective', '30 Jul / 31 Jan'),
      ('SRR-003', 'Study coordinator', 'Missing or conflicting UDI; reconciliation after 24 h', 'Second UDI check, including weekend lists · QA lead · 30 Nov', 'CAPA-014-002 (reopened); SART-014-005', 'PI informed 28 Oct; sponsor DD route', 'Open', 'Not effective', '31 Oct / 30 Nov'),
      ('SRR-004', 'Principal Investigator', 'Coordinator away for more than one working day', 'Train the Sub-I on the EDC safety form · coordinator · 15 Nov (was 30 Jun)', 'TRE-014-12 pending; SART-014-005', 'POT 3 Nov; sponsor told of late report', 'Open', 'In progress', '31 Oct / 15 Nov'),
      ('SRR-005', 'Radiology research tech', 'Any rotated day-1 image', 'Ask sponsor to allow day-1 AP in the radiology suite · PI · 30 Nov', 'IQL-014-10 (R01); Q-IMG-12', 'Sponsor query 30 Oct', 'Open', 'Not started', '31 Oct / 30 Nov'),
      ('SRR-006', 'OR nurse lead', 'Any explant', 'Write a local explant procedure · coordinator · 30 Nov', 'SART-014-005; IMP-014 v1.1 (check 13)', 'Sponsor RMA route', 'Open', 'In progress', '31 Oct / 30 Nov')]
for row, r in zip(rows('gt'), Fr):
    td = row.findall('td')
    for t, v in zip(td[:6], r[:6]): put(t, v)
    tick(td[6], r[6]); tick(td[7], r[7]); put(td[8], r[8])
# G: review log
Gr = [('30 Jul · Sub-I', 'SRR-002', 'Scheduled', 'IMC-014-01: bin in use in all 3 cases; no near miss', 'Effective', 'Moderate · Controlled', 'Lower priority (I, 30 Jul)', '31 Jan'),
      ('31 Aug · Sub-I', 'SRR-001', 'Scheduled', 'TRE-014-09: second physio released; no Tue/Thu loss since', 'Effective', 'Moderate · Controlled', 'Lower priority (I, 31 Aug)', '31 Jan'),
      ('30 Sep · QA lead', 'SRR-003', 'Scheduled', 'IMC-014-01: second check done in cases 006-007', 'Effective', 'Moderate · Controlled', 'Keep the trigger', '31 Oct'),
      ('28 Oct · coordinator', 'SRR-003', 'Urgent (H)', 'SART-014-005: lot missing in ICDL-014-005; second check skipped (weekend, one nurse)', 'Not effective', 'High · Open', 'Escalate to CAPA (I, 28 Oct)', '30 Nov'),
      ('28 Oct · Sub-I', 'SRR-004', 'Trigger', 'SADE reported 27 h after awareness; coordinator away, backup untrained', 'Not effective', 'High · Open', 'Escalate to POT (I, 3 Nov)', '15 Nov'),
      ('31 Oct · PI', 'SRR-005', 'Urgent (H)', 'IQL-014-10: day-1 sets 02 and 07 rotated', 'Not assessable', 'High · Open', 'Sponsor query Q-IMG-12', '30 Nov'),
      ('31 Oct · PI', 'SRR-006', 'Urgent (H)', 'Explant left unlabeled for two days', 'Not assessable', 'High · Open', 'Check 13 added to IMP v1.1', '30 Nov')]
for row, r in zip(rows('htl'), Gr):
    td = row.findall('td')
    put(td[0], r[0]); put(td[1], r[1]); tick(td[2], r[2]); put(td[3], r[3]); tick(td[4], r[4]); put(td[5], r[5]); put(td[6], r[6]); put(td[7], r[7])
# H: urgent entries
Hr = [('1 · 28 Oct, 08:40', 'Coordinator (P-06)', 'Dislocation (SART-014-005): liner lot missing in ICDL-014-005; no rule for handling the explant.', 'Lot read from the explant label; explant bagged and labeled 30 Oct; SART-014-005.', 'Yes', ['Update', 'New risk'], '003; 006'),
      ('2 · 30 Oct, 10:15', 'Radiology tech (P-09)', 'Day-1 ward images rotated twice; liner seating not visible.', 'Sponsor query Q-IMG-12; IQL-014-10, R01.', 'Yes', ['New risk'], '005')]
for row, r in zip(rows('ulog'), Hr):
    td = row.findall('td')
    for t, v in zip(td[:4], r[:4]): put(t, v)
    tick(td[4], r[4]); tick(td[5], *r[5])
    lab = td[5].xpath('./span[contains(@class,"lab")]')[0]; lab.addnext(E('span', 'demo-fill', r[6]))
# I: decisions
Ir = [('30 Jul', 'SRR-002', 'Lower priority', 'Review G 30 Jul shows the bin works; re-rated Device 3 to 2', 'IMC-014-01', 'A. Morgan (PI)'),
      ('31 Aug', 'SRR-001', 'Lower priority', 'Second physio released; Data 3 to 2', 'TRE-014-09', 'A. Morgan (PI)'),
      ('28 Oct', 'SRR-003', 'Escalate', 'Control failed after a CAPA: recurrence', 'CAPA-014-002 reopened', 'R. Teixeira (backup PI)'),
      ('3 Nov', 'SRR-004', 'Escalate', 'Backup never trained; SADE reported late', 'POT 3 Nov; sponsor letter', 'A. Morgan (PI)')]
for row, r in zip(rows('jlog'), Ir):
    td = row.findall('td')
    put(td[0], r[0]); put(td[1], r[1]); tick(td[2], r[2]); put(td[3], r[3]); put(td[4], r[4]); put(td[5], r[5])
# J: certification
k = rows('ktb')
for i, vals in [(0, ['31 Oct 2026', 'Quarterly, and after any SADE']), (1, ['SRR-003, SRR-004, SRR-005, SRR-006']), (2, ['None']), (3, ['31 Jan 2027, or earlier on a trigger', 'POT 3 Nov 2026'])]:
    cells = [t for t in k[i].findall('td') if 'lbl' not in (t.get('class') or '')]
    for t, v in zip(cells, vals): put(t, v)
wb = doc.xpath('//div[contains(@class,"assess")]')[0]
put(wb, 'October changed the picture. Two of our controls failed in the same case (SART-014-005): the second UDI check was skipped on a weekend with one nurse, and the backup for safety reporting had never been trained. Both rest on single people. The day-1 image problem and the missing explant procedure were invisible until the dislocation.')
put(wb, 'Most exposed: weekend and holiday cover for OR and safety tasks. Next: train the Sub-I on the EDC safety form by 15 Nov, extend the second check to weekend lists, and get the sponsor\'s answer on day-1 imaging before the next inclusion.')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    f = sg.xpath('./div[@class="sig-field"]'); f[0].append(E('span', 'demo-fill', name))
    line = f[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '   '; line.append(ik); line.append(E('span', 'demo-fill', date))
sign('Register owner', 'Maria Silva / Study Coordinator', 'M. Silva', '31 Oct 2026')
sign('Principal Investigator', 'Dr Alex Morgan', 'A. Morgan', '3 Nov 2026')
F = '/tmp/claude-0/-home-user-Master-Thesis/c35b56ea-6e37-57ca-a7f6-4cae380cc50e/scratchpad/fonts/'
hand = base64.b64encode(open(F + '4UaErEJDsxBrF37olUeD_xHMwps.ttf', 'rb').read()).decode()
sig = base64.b64encode(open(F + 'dancing.ttf', 'rb').read()).decode()
st = etree.SubElement(doc.find('.//head'), 'style')
st.text = ('@font-face{font-family:"SimHand";font-weight:400 700;src:url(data:font/ttf;base64,' + hand + ')}'
           '@font-face{font-family:"SimSig";src:url(data:font/ttf;base64,' + sig + ')}'
           '.demo-fill,.demo-entry{font-family:"Segoe Print","Bradley Hand","Comic Sans MS","SimHand",cursive!important;color:#174f88!important;font-weight:600!important;line-height:1.18!important}'
           'td .demo-fill{display:block;text-align:center!important;font-size:8.4px}td:has(>.demo-fill){text-align:center!important}'
           '.demo-fill.fac{display:inline!important;text-align:left!important;font-size:8px}.ft td:nth-child(4):has(.fac) .lab{display:inline;margin:0!important}.ft td:nth-child(4){line-height:1.2}'
           '.meta-cell .demo-entry{display:block;text-align:left;font-size:10px;margin-top:3px}'
           '.wbox.assess .demo-fill{display:block;font-size:10.6px;line-height:1.45!important;margin-top:8px}'
           '.sig-ink{font-family:"Snell Roundhand","Brush Script MT","Segoe Script","Lucida Handwriting","SimSig",cursive!important;font-size:15px!important;color:#174f88}')
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
