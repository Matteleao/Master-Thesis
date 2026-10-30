# Simulated (filled) SART v1.0: GLENOS-01, Riverside 014, case 2 greater tuberosity fracture (SART-014-002).
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
doc.find('.//title').text = 'SART v1.0 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('Current CIP / version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('SART case ID / revision', 'SART-014-002 / r2'),
             ('Participant code (or N/A and why)', '014-0002'), ('Procedure, visit or exposure (or N/A)', 'Reverse shoulder arthroplasty, 2 Oct 2026 (ICDL-014-002)'), ('Site awareness: date / time', '2 Oct 2026, 10:42'),
             ('Person who received the first information', 'Dr R. Teixeira, operating surgeon'), ('PI / authorized site assessor', 'Dr Alex Morgan'), ('Sponsor safety system / route', 'GLENOS EDC, adverse event page'),
             ('Sponsor safety case ID (if issued)', 'GS-AE-014-0007'), ('Study / site', 'GLENOS-01 / 014'), ('Participant code or N/A', '014-0002'),
             ('Assessment date', '2 Oct 2026 (PI)'), ('Sponsor safety case ID', 'GS-AE-014-0007'), ('Sheet number / total sheets', '1 / 1'), ('Local closure date', '16 Nov 2026')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Closed locally')
# B (page 1)
r = rows('bt')
B = [('Known', '2 Oct 2026, 10:40, during humeral preparation'), (None, '2 Oct 2026, 10:42; Dr R. Teixeira, in theatre; ICDL-014-002 Section G'),
     ('Adverse event', 'Intraoperative event'), ('No', 'Fracture fixed; participant stable at closure'),
     (None, 'Fixed with two transosseous sutures; PI called before closure (POT trigger 10), 10:55'), (None, 'GLENOS v2 humeral stem 12 mm, lot GS-H12-2609; no device implicated; humeral preparation step')]
for row, (opt, ref) in zip(r, B):
    tds = row.findall('td')
    if opt: tick(tds[1], opt)
    put(tds[2], ref)
put(doc.xpath('//div[contains(@class,"wbox") and contains(@class,"fact")]')[0], 'During humeral preparation in case 2, a non-displaced greater tuberosity fracture was seen. It was fixed with two transosseous sutures and the planned implant was placed. The shoulder was stable at closure, and the immediate postoperative radiograph shows the implant and the fixation in position.')
for row, vals in zip(rows('src2', 0), [('Operative note', 'EHR, 2 Oct 2026', 'Fracture, fixation and final configuration'), ('ICDL', 'ICDL-014-002, Sections F and G', 'Time of the event and of the call to the PI'),
                                        ('Immediate postoperative image', 'IQL-014-002-PO', 'Implant and fixation position'), ('6-week visit record', 'PFVR-014-002-V1', 'Healing of the tuberosity'), ('eCRF', 'GLENOS EDC, AE-07', 'Report to the sponsor')]):
    for td, v in zip(row.findall('td'), vals): put(td, v)
for row, vals in zip(rows('src2', 1), [('6-week radiograph result', 'P-04', 'At the 6-week visit, 13 Nov 2026')]):
    for td, v in zip(row.findall('td'), vals): put(td, v)
# C
c = rows('ct', 0)
spec = [('Yes', ''), ('Does not meet seriousness criteria', ''), ('Mild', 'CIP v4.2 intensity scale'), ('No', 'Bone event during preparation; implant not involved'),
        ('N/A', 'Single-arm study'), ('No', 'Implantation is the study procedure, not an added one'), ('N/A', 'Not a SADE'), ('Non-serious AE', '')]
for row, (o, ref) in zip(c, spec):
    tds = row.findall('td'); tick(tds[1], o); put(tds[2], ref)
c2 = rows('ct', 1)
tick(c2[0].findall('td')[1], 'No'); put(c2[0].findall('td')[2], 'No deficiency observed')
tick(c2[4].findall('td')[1], 'N/A')
c3 = rows('ct', 2)
tick(c3[0].findall('td')[1], 'Procedure', 'Operator or technique'); put(c3[0].findall('td')[2], 'Early case in the surgeon\'s sequence (SLCT case 2)')
tick(c3[1].findall('td')[1], 'No')
c4 = rows('ct', 3)
tick(c4[0].findall('td')[1], 'Final (PI)'); put(c4[0].findall('td')[2], 'A. Morgan, 2 Oct 2026')
tick(c4[1].findall('td')[1], 'Received'); put(c4[1].findall('td')[2], '20 Oct 2026, MM-Q-114 closed')
tick(c4[2].findall('td')[1], 'Agree'); put(c4[2].findall('td')[2], 'Non-serious, not device-related')
put(c4[3].findall('td')[1], 'None')
# D
d = rows('dt')
D = [('Yes', 'CIP v4.2 section 9.3: every AE entered in the eCRF within 5 working days'), ('eCRF', 'GLENOS EDC adverse event page'), (None, '2 Oct 2026, 10:42'), (None, '5 working days; due 9 Oct 2026'),
     (None, '3 Oct 2026, 16:10; M. Silva (P-06); EDC entry AE-07'), ('Yes', 'GS-AE-014-0007'), ('Yes', 'Sent 1 working day after awareness'), ('Complete', 'No query on the first report'),
     (None, 'N/A: on time and complete'), (None, 'N/A'), ('Not required', 'Not assigned to the site by the CIP')]
for row, (o, ref) in zip(d, D):
    tds = row.findall('td')
    if o: tick(tds[1], o)
    put(tds[2], ref)
# E
e = rows('et')
EV = [('6 Oct 2026, 09:00', 'Read at the scheduled oversight review with SLCT case 2; no pattern (POT-014-R-2026-10)', 'None', 'N/A', 'N/A', 'N/A', 'N/A', 'P-01: SLCT review at case 5'),
      ('14 Oct 2026, 11:20', 'Sponsor medical monitor asks for the fixation details (MM-Q-114)', 'None', 'MM-Q-114', '21 Oct 2026', 'Answered 15 Oct; EDC receipt', 'Yes', 'P-06: await the determination'),
      ('20 Oct 2026, 15:05', 'Sponsor confirms: non-serious, not device-related; MM-Q-114 closed', 'Confirms the PI assessment', 'MM-Q-114 closure', 'N/A', 'N/A', 'N/A', 'P-06: record in C4'),
      ('13 Nov 2026, 10:30', '6-week visit: tuberosity healed on radiograph (PFVR-014-002-V1; IQL-014-002-W6)', 'Outcome: recovered', 'N/A', '20 Nov 2026', 'Sent 14 Nov; EDC AE-07 v2', 'Yes', 'P-06: close locally')]
for row, vals in zip(e, EV):
    tds = row.findall('td')
    for td, v in zip(tds[1:7], vals[:6]): put(td, v)
    tick(tds[7], vals[6]); put(tds[8], vals[7])
# F
F = [('Linked', 'SCML-014-001, 2 Oct 2026'), ('Not required', ''), ('Not required', 'No trigger'), ('Linked', 'POT-014-R-2026-10, 6 Oct 2026'), ('Not required', 'Single case'), ('Linked', 'PIR-014-2026-10, October 2026'), ('Not required', 'No deficiency')]
for row, (o, ref) in zip(rows('ft'), F):
    tds = row.findall('td'); put(tds[2], ref); tick(tds[3], o)
G = ['Clinical record, 2 Oct', 'Section B source map', 'C4', 'D: AE-07 / GS-AE-014-0007', 'D: on time, complete', 'E line 4', 'C4: 20 Oct 2026', 'F']
for row, ref in zip(rows('gt'), G):
    tds = row.findall('td'); tick(tds[1], 'Yes'); put(tds[2], ref)
cr = doc.xpath('//div[@class="close-row"]')[0]; tick(cr, 'Closed locally')
meta('Current outcome and open items', 'Recovered; tuberosity healed at 6 weeks. No open items.')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    f = sg.xpath('./div[@class="sig-field"]'); f[0].append(E('span', 'demo-fill', name))
    line = f[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '   '; line.append(ik); line.append(E('span', 'demo-fill', date))
sign('Case reporter / initial site assessor', 'Dr R. Teixeira / Sub-investigator', 'R. Teixeira', '2 Oct 2026')
sign('PI / accountable investigator', 'Dr Alex Morgan / PI', 'A. Morgan', '16 Nov 2026')
sign('Safety coordinator (if applicable)', 'Maria Silva / Study Coordinator', 'M. Silva', '16 Nov 2026')
put(doc.xpath('//div[contains(@class,"writeline") and contains(@class,"loc")]')[0], 'Investigator site file, tab 6 (Safety) / SART-014-002; GLENOS EDC AE-07; SCML-014')
st = etree.SubElement(doc.find('.//head'), 'style'); st.text = '.ft td{height:32px!important}.gt td{height:25px!important}.ct .demo-fill,.dt .demo-fill,.et .demo-fill,.ft .demo-fill,.gt .demo-fill,.bt .demo-fill,.src2 .demo-fill{font-size:8.8px}'
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
