# Simulated (filled) SART v1.1: GLENOS-01, Riverside 014, dislocation from liner separation (SART-014-005): SADE with a device deficiency, late report.
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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v1.1'
doc.find('.//title').text = 'SART v1.1 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('Current CIP / version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('SART case ID / revision', 'SART-014-005 / r4'),
             ('Participant code (or N/A and why)', '014-0005'), ('Procedure, visit or exposure (or N/A)', 'Reverse shoulder arthroplasty, 9 Oct 2026 (ICDL-014-005); revision 28 Oct 2026'), ('Site awareness: date / time', '28 Oct 2026, 08:05'),
             ('Person who received the first information', 'Maria Silva (P-06), from the hospital admission list'), ('PI / authorized site assessor', 'Dr Alex Morgan (on leave 27 Oct to 2 Nov); backup Dr R. Teixeira'), ('Sponsor safety system / route', 'GLENOS EDC: SAE form and DD form'),
             ('Sponsor safety case ID (if issued)', 'GS-SAE-014-0003'), ('Study / site', 'GLENOS-01 / 014'), ('Participant code or N/A', '014-0005'),
             ('Assessment date', '28 Oct 2026; updated 13 Nov'), ('Sponsor safety case ID', 'GS-SAE-014-0003'), ('Sheet number / total sheets', '1 / 1'), ('Local closure date', 'Open; next review 15 Jan 2027')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Open')
def fill3(cls, idx, spec):
    for row, (opts, ref) in zip(rows(cls, idx), spec):
        tds = row.findall('td')
        if opts:
            tick(tds[1], *([opts] if isinstance(opts, str) else opts))
        put(tds[-1], ref)
fill3('bt', 0, [('Known', '27 Oct 2026, 21:30, at home, while dressing (day 18)'),
    (None, '28 Oct 2026, 08:05; Maria Silva (P-06), from the hospital admission list; emergency department note'),
    ('Adverse event', 'Dislocation. The device deficiency was found at revision (Section E, line 1)'),
    ('Yes', 'Dislocated shoulder; participant admitted'),
    (None, 'Closed reduction failed in the emergency department; admitted. Backup PI Dr R. Teixeira informed 28 Oct, 08:40; open revision 28 Oct, 14:00'),
    (None, 'GLENOS v2; humeral liner 36 mm +3, lot GS-L36-2607 (read from the explant label: missing in ICDL-014-005); assembly of the liner on the stem')])
put(doc.xpath('//div[contains(@class,"wbox") and contains(@class,"fact")]')[0], 'Eighteen days after a reverse shoulder arthroplasty, the participant felt the shoulder give way while dressing and came to the emergency department, where closed reduction failed. At open revision on 28 Oct the humeral liner was found separated from the stem, with the locking ring not engaged. The liner was replaced, the shoulder was stable at closure, and the removed liner was kept for return to the sponsor.')
for row, vals in zip(rows('src2', 0), [('Emergency department note and admission', 'EHR, 28 Oct 2026', 'Presentation, failed reduction, admission'), ('Revision operative note', 'EHR / ICDL-014-005-R', 'Liner separated; locking ring not engaged; liner replaced'),
                                        ('Explant and return record', 'RMA-0045, 30 Oct 2026', 'Liner kept and returned to the sponsor'), ('Index procedure log', 'ICDL-014-005, Section E', 'Liner lot not recorded at the index procedure'),
                                        ('Sponsor SAE and DD forms', 'GS-SAE-014-0003; GS-DD-014-0012', 'Formal report and follow-up'), ('Device analysis report', 'DA-0045, 19 Nov 2026', 'Locking ring out of tolerance in lot GS-L36-2607')]):
    for td, v in zip(row.findall('td'), vals): put(td, v)
for row, vals in zip(rows('src2', 1), [('Sponsor lot investigation outcome', 'P-01', 'Sponsor; ask at the next contact'), ('3-month visit after revision', 'P-06', 'Visit window 20 Jan to 3 Feb 2027')]):
    for td, v in zip(row.findall('td'), vals): put(td, v)
fill3('ct', 0, [('Yes', 'Emergency department note, 28 Oct'), ('In-patient or prolonged hospitalization', 'Admitted for revision surgery'), ('Severe', 'CIP v4.2 intensity scale'), ('IIIb', 'Open revision under general anesthesia, 28 Oct'),
    ('Yes', 'Liner separation caused the dislocation'), ('N/A', 'Single-arm study'), ('No', 'Event linked to the device, not to an added procedure'),
    ('Pending', 'Dislocation is in the risk assessment; liner separation is not'), ('SADE', 'Anticipated status for the sponsor')])
fill3('ct', 1, [('Yes', 'Found at revision'), (['Performance', 'Malfunction'], 'Locking ring did not hold the liner'), ('Yes', 'Both pathways apply'), ('Yes', 'It did lead to one'), ('Done', 'Liner returned, RMA-0045')])
fill3('ct', 2, [(['Device', 'Operator or technique'], 'Liner seating not documented at the index procedure'), ('Pending', 'Sponsor checking lot GS-L36-2607 at other sites')])
fill3('ct', 3, [('Final (PI)', 'A. Morgan, 3 Nov 2026'), ('Received', '13 Nov 2026, SAF-GS-0031: USADE, device-related'), ('Agree', 'PI had left the anticipated status to the sponsor'), (None, 'Operator contribution to liner seating; P-01, after the device analysis')])
fill3('dt', 0, [('Yes', 'CIP v4.2 section 9.4: SAEs and DDs that could have led to a SADE within 72 hours of awareness'), (['SAE form', 'DD form'], 'GLENOS EDC'), (None, '28 Oct 2026, 08:05'), (None, '72 hours; due 31 Oct 2026, 08:05'),
    (None, '1 Nov 2026, 11:30; M. Silva (P-06); GS-SAE-014-0003 and GS-DD-014-0012'), ('Yes', 'GS-SAE-014-0003'), ('No', 'Sent 27 hours late'), ('Incomplete', 'Liner lot missing; sent 2 Nov after the explant label was read'),
    ('Internal escalation', 'Backup PI informed but not told the case was reportable; PI on leave'), (None, 'Backup notification rule added to POT Section C; deviation PD-014-12; CAPA-014-2026-004'), ('Not required', 'Not assigned to the site by the CIP')])
e = rows('et')
EV = [('29 Oct 2026, 09:10', 'Revision findings: liner separated, locking ring not engaged; liner kept (ICDL-014-005-R)', 'DD pathway opened; device relation confirmed', 'N/A', 'N/A', 'Added to the first report', 'N/A', 'P-06: complete C2'),
      ('3 Nov 2026, 14:00', 'Sponsor asks for the liner lot and the assembly steps (MM-Q-131)', 'None', 'MM-Q-131', '6 Nov 2026', 'Answered 5 Nov; EDC receipt', 'Yes', 'P-01: reply with ICDL and explant label'),
      ('13 Nov 2026, 16:20', 'Sponsor determination: USADE; lot GS-L36-2607 quarantined at all sites', 'Anticipated status resolved', 'SAF-GS-0031', 'N/A', 'N/A', 'N/A', 'P-01: quarantine stock; tell the team'),
      ('19 Nov 2026, 10:00', 'Device analysis: locking ring out of tolerance (DA-0045)', 'Device cause confirmed; operator contribution reduced', 'DA-0045', 'N/A', 'N/A', 'N/A', 'P-01: update the SCML context'),
      ('9 Dec 2026, 11:00', '6-week visit after revision: stable, no further dislocation (PFVR-014-005-R6)', 'Outcome: recovering', 'N/A', '16 Dec 2026', 'Sent 10 Dec; EDC update', 'Yes', 'P-06: 3-month visit, Jan 2027')]
for row, vals in zip(e, EV):
    tds = row.findall('td')
    for td, v in zip(tds[1:7], vals[:6]): put(td, v)
    tick(tds[7], vals[6]); put(tds[8], vals[7])
F = [('Linked', 'SCML-014-004, 28 Oct 2026'), ('Linked', 'PD-014-12, 1 Nov 2026'), ('Linked', 'Early CSST review, 4 Nov 2026 (serious event, new category)'), ('Linked', 'POT-014-T-2026-11, triggered review'),
     ('Linked', 'CAPA-014-2026-004: escalation while the PI is away'), ('Linked', 'PIR-014-2026-11, November 2026'), ('Linked', 'GS-DD-014-0012; RMA-0045')]
for row, (o, ref) in zip(rows('ft'), F):
    tds = row.findall('td'); put(tds[2], ref); tick(tds[3], o)
G = [('Yes', 'Emergency department and revision notes'), ('Yes', 'Section B source map'), ('Yes', 'C4, 3 Nov 2026'), ('Yes', 'GS-SAE-014-0003, GS-DD-014-0012'),
     ('Yes', 'Late and incomplete: D, PD-014-12'), ('Yes', 'Open: 3-month visit, Jan 2027'), ('Yes', 'SAF-GS-0031, 13 Nov 2026'), ('Yes', 'F, all seven linked')]
for row, (o, ref) in zip(rows('gt'), G):
    tds = row.findall('td'); tick(tds[1], o); put(tds[2], ref)
cr = doc.xpath('//div[@class="close-row"]')[0]; tick(cr, 'Open follow-up')
meta('Current outcome and open items', 'Recovering after revision. Open: sponsor lot investigation and the 3-month visit.')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    f = sg.xpath('./div[@class="sig-field"]'); f[0].append(E('span', 'demo-fill', name))
    line = f[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '   '; line.append(ik); line.append(E('span', 'demo-fill', date))
sign('Case reporter / initial site assessor', 'Dr R. Teixeira / Sub-investigator, PI backup', 'R. Teixeira', '28 Oct 2026')
sign('PI / accountable investigator', 'Dr Alex Morgan / PI', 'A. Morgan', '10 Dec 2026')
sign('Safety coordinator (if applicable)', 'Maria Silva / Study Coordinator', 'M. Silva', '10 Dec 2026')
put(doc.xpath('//div[contains(@class,"writeline") and contains(@class,"loc")]')[0], 'Investigator site file, tab 6 (Safety) / SART-014-005; GLENOS EDC GS-SAE-014-0003 and GS-DD-014-0012; SCML-014; RMA-0045')
st = etree.SubElement(doc.find('.//head'), 'style'); st.text = '.ft td{height:32px!important}.gt td{height:25px!important}.ct .demo-fill,.dt .demo-fill,.et .demo-fill,.ft .demo-fill,.gt .demo-fill,.bt .demo-fill,.src2 .demo-fill{font-size:8.8px}'
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
