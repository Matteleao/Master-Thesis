# Simulated (filled) IQL v0.6: GLENOS-01, Riverside 014, October 2026 review. Links to SART-014-005 (post-op image could not show liner seating).
import sys
from lxml import html as LH, etree
SRC, OUT = sys.argv[1], sys.argv[2]
doc = LH.document_fromstring(open(SRC).read())
def E(tag, cls, text):
    e = etree.Element(tag); e.set('class', cls); e.text = text; return e
def meta(scope, label, val):
    cells = [c for c in scope.xpath('.//div[contains(@class,"meta-cell")]') if c.find('span[@class="meta-label"]') is not None and c.find('span[@class="meta-label"]').text_content().strip() == label]
    assert cells, label
    for c in cells: c.find('span[@class="meta-entry"]').append(E('span', 'demo-fill', val))
def tick(scope, *labels):
    for lab in labels:
        for o in scope.xpath('.//span[@class="option"]'):
            if o.text_content().strip() == lab:
                o.find('span[@class="check"]').set('class', 'check selected'); break
        else: raise Exception('no opt ' + lab)
def put(td, val):
    if val: td.append(E('span', 'demo-fill', val))
def rows(cls):
    return doc.xpath(f'//table[contains(concat(" ",@class," ")," {cls} ")]')[0].xpath('./tbody/tr')
body = doc.find('.//body'); body.set('class', (body.get('class') or '') + ' simulation')
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.6'
doc.find('.//title').text = 'IQL v0.6 - Simulated Editable'
p = doc.xpath('//main')
for k, v in [('Study / Protocol', 'GLENOS-01 / GS-2026-01'), ('CIP Version', 'CIP v4.2'), ('Site / Code', 'Riverside Orthopedic Center / 014'), ('IQL Record ID / Revision', 'IQL-014-10 / r1'),
             ('Review Period / Cut-off Date', 'Oct 2026; cut-off 31 Oct'), ('Imaging Charter / Manual ID and Version', 'GLENOS Imaging Manual v2.0'),
             ('Modalities and Time Points Covered', 'Shoulder XR at screening, day 1 and 6 weeks; CT at screening'), ('Imaging Unit / Equipment', 'Riverside Radiology room 2 (DR); ward portable unit'),
             ('Archive and Transfer Route (PACS, Sponsor Portal)', 'Hospital PACS; sponsor portal GS-IMG'), ('Local Imaging Reviewer / Role', 'Dr Lena Ortiz / Radiologist'),
             ('Log Owner / Role', 'Tom Reyes / Radiology research tech (P-09)'), ('Controlled Record Location', 'ISF tab 7 (Imaging) / IQL-014-10')]:
    meta(p[0], k, v)
for k, v in [('Study / Site Code', 'GLENOS-01 / 014'), ('IQL Record ID / Revision', 'IQL-014-10 / r1'), ('Review Period', 'Oct 2026'), ('Log Sheet No. / Total', '1 / 1')]:
    meta(p[1], k, v)
# C: image-set log
C = [('014-0006 / Screening', 'PSEAR-014-0006', 'Eligibility', 'Original', '', 'XR 4 views + CT', 'Within 60 d pre-op / 2 Oct', 'In window', 'Complete', 'Adequate', 'Usable', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-031', 'T. Reyes / 2 Oct', 'N/A'),
     ('014-0005 / Day 1', 'ICDL-014-005', 'Post-op check', 'Original', '', 'XR AP + Y', 'Day 0-2 / 10 Oct', 'In window', 'Complete', 'Limited', 'Limited use', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-034', 'L. Ortiz / 10 Oct', 'R01'),
     ('014-0003 / 6 weeks', 'PFVR-014-0003-W6', 'Follow-up', 'Original', '', 'XR 3 views', 'Day 35-49 / 21 Oct (d52)', 'Outside', 'Complete', 'Adequate', 'Limited use', ['Archived', 'Transferred'], 'TX-036', 'T. Reyes / 21 Oct', 'R02'),
     ('014-0004 / 6 weeks', 'PFVR-014-0004-W6', 'Follow-up', 'Original', '', 'XR 3 views', 'Day 35-49 / 24 Oct', 'In window', 'Partial', 'Adequate', 'Pending', ['Archived'], '', 'T. Reyes / 24 Oct', 'R03'),
     ('014-0004 / 6 weeks', 'PFVR-014-0004-W6', 'Follow-up', 'Repeat', '04', 'XR axillary', 'Day 35-49 / 28 Oct', 'In window', 'Complete', 'Adequate', 'Usable', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-038', 'L. Ortiz / 28 Oct', 'R03')]
for row, c in zip(rows('quality-log'), C):
    td = row.findall('td')
    put(td[1], c[0]); put(td[2], c[1]); tick(td[3], c[2]); tick(td[4], c[3])
    if c[4]: rel = td[4].find('span[@class="rel"]'); rel.text = 'Related: '; rel.append(E('span', 'demo-fill inl', c[4]))
    put(td[5], c[5]); put(td[6], c[6]); tick(td[7], c[7]); tick(td[8], c[8]); tick(td[9], c[9]); tick(td[10], c[10]); tick(td[11], *c[11])
    if c[12]: rel = td[11].find('span[@class="rel"]'); rel.text = 'Ref.: '; rel.append(E('span', 'demo-fill inl', c[12]))
    put(td[12], c[13]); put(td[13], c[14])
# D: period summary
meta(p[2], 'Image-set IDs Reviewed (range)', 'Sets 01-05, log sheet 1 of 1')
meta(p[2], 'Distinct Image Sets Reviewed (N, per set)', '5 sets (4 participants)')
D = [('1', 'Set 04: axillary view not taken (pain). Repeated as set 05, complete.'),
     ('1', 'Set 02: AP rotated, liner seating not visible. R01.'),
     ('1', 'Set 04 pending until the repeat; closed by set 05 on 28 Oct.'),
     ('1', 'Set 03 taken on day 52. Deviation DEV-014-007; reaches the FUCR through the PFVR.'),
     ('2', 'Set 05 repeats set 04. Set 02 read again by the radiologist after the dislocation (SART-014-005).'),
     ('1', 'Day-1 AP is taken on the ward with the arm in a sling; rotation cannot be reproduced. Raised with the sponsor 30 Oct (query Q-IMG-12).')]
for row, (a, b) in zip(rows('review-log'), D):
    td = row.findall('td'); put(td[1], a); put(td[2], b)
# E: resolution
Er = [('R01 / 02', 'AP rotated; liner seating not visible on the only post-op image before the dislocation. Second read 29 Oct.', 'Seating not assessable; use limited to the clinical check. No repeat possible (revised 28 Oct).', 'ICDL-014-005; SART-014-005; Q-IMG-12', 'L. Ortiz / 15 Nov', 'Handed off'),
      ('R02 / 03', 'Taken on day 52 (participant travel). Visit date confirmed with the PFVR.', 'Images adequate; usable for clinical follow-up, not for the 6-week endpoint.', 'PFVR-014-0003-W6; DEV-014-007', 'M. Silva / 5 Nov', 'Resolved'),
      ('R03 / 04, 05', 'Axillary view missing (pain). Repeat booked inside the window.', 'Set 05 on 28 Oct, complete and usable. Set 04 kept as recorded.', 'PFVR-014-0004-W6', 'T. Reyes / 28 Oct', 'Resolved')]
for row, r in zip(rows('resolution-log'), Er):
    td = row.findall('td')
    for t, v in zip(td[:5], r[:5]): put(t, v)
    tick(td[5], r[5])
# F: conclusion
cr = rows('conclusion-table')[2].findall('td'); tick(cr[2], 'Select'); put(cr[3], '31 Oct 2026 / next 30 Nov')
wb = doc.xpath('//div[contains(@class,"conclusion-basis")]')[0]
be = wb.find('.//span[@class="blank-entry"]')
put(be if be is not None else wb, 'R01 handed off: the day-1 ward image cannot show liner seating, and set 02 is the only post-op image of 014-0005 before the dislocation. Sponsor asked (Q-IMG-12) whether the day-1 AP can be taken in the radiology suite, out of the sling. R02 closed as a deviation; R03 closed by the repeat. No open issue in sets 01, 04 and 05.')
# G: sign-off
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    r = sg.xpath('./div[@class="sig-row"]/i')
    r[0].append(E('span', 'demo-fill', name)); r[1].append(E('span', 'demo-fill sig-ink', ink)); r[2].append(E('span', 'demo-fill', date))
sign('Local Imaging Reviewer / Radiology Liaison', 'Dr Lena Ortiz / Radiologist', 'L. Ortiz', '31 Oct 2026')
sign('PI Review / Acknowledgment — When Required', 'Dr Alex Morgan / PI', 'A. Morgan', '3 Nov 2026')
pc = doc.xpath('//div[contains(@class,"pi-cell")]')[0]; tick(pc, 'Required'); pc.find('span[@class="meta-entry"]').append(E('span', 'demo-fill', 'Image limitation linked to an SADE (SART-014-005)'))
meta(p[3], 'Next Review Date / Trigger', '30 Nov 2026, or the sponsor answer to Q-IMG-12')
import base64
F = '/tmp/claude-0/-home-user-Master-Thesis/c35b56ea-6e37-57ca-a7f6-4cae380cc50e/scratchpad/fonts/'
hand = base64.b64encode(open(F + '4UaErEJDsxBrF37olUeD_xHMwps.ttf', 'rb').read()).decode()
sig = base64.b64encode(open(F + 'dancing.ttf', 'rb').read()).decode()
st = etree.SubElement(doc.find('.//head'), 'style')
st.text = ('@font-face{font-family:"SimHand";font-weight:400 700;src:url(data:font/ttf;base64,' + hand + ')}'
           '@font-face{font-family:"SimSig";src:url(data:font/ttf;base64,' + sig + ')}'
           '.demo-fill{font-family:"Segoe Print","Bradley Hand","Comic Sans MS","SimHand",cursive!important;color:#174f88!important;font-weight:700!important;line-height:1.18!important}'
           '.demo-fill.inl{display:inline;font-size:8.4px!important}'
           '.meta-entry .demo-fill{font-size:10.4px}.quality-log .demo-fill{font-size:8.8px}.review-log .demo-fill,.resolution-log .demo-fill{font-size:9.6px}'
           '.conclusion-basis .demo-fill,.conclusion-table .demo-fill{font-size:10.4px}'
           '.sig-ink{font-family:"Bradley Hand","Segoe Script","SimSig",cursive!important;font-size:15px!important;font-weight:400!important}'
           '.record-location .meta-entry,.record-location .demo-fill{text-align:center}')
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
