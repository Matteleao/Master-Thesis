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
def rows(cls, idx=0):
    return doc.xpath(f'//table[contains(concat(" ",@class," ")," {cls} ")]')[idx].xpath('./tbody/tr')
body = doc.find('.//body'); body.set('class', (body.get('class') or '') + ' simulation')
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.6'
doc.find('.//title').text = 'IQL v0.6 - Simulated Editable'
import copy
m2 = doc.xpath('//main')[1]; m2.addnext(copy.deepcopy(m2))
for k, tdn in enumerate(doc.xpath('//main')[2].xpath('.//table[contains(@class,"quality-log")]/tbody/tr/td[1]')): tdn.text = f'{k + 6:02d}'
p = doc.xpath('//main')
for k, v in [('Study / Protocol', 'GLENOS-01 / GS-2026-01'), ('CIP Version', 'CIP v4.2'), ('Site / Code', 'Riverside Orthopedic Center / 014'), ('IQL Record ID / Revision', 'IQL-014-10 / r1'),
             ('Review Period / Cut-off Date', 'Oct 2026; cut-off 31 Oct'), ('Imaging Charter / Manual ID and Version', 'GLENOS Imaging Manual v2.0'),
             ('Modalities and Time Points Covered', 'Shoulder XR at screening, day 1 and 6 weeks; CT at screening'), ('Imaging Unit / Equipment', 'Riverside Radiology room 2 (DR); ward portable unit'),
             ('Archive and Transfer Route (PACS, Sponsor Portal)', 'Hospital PACS; sponsor portal GS-IMG'), ('Local Imaging Reviewer / Role', 'Dr Lena Ortiz / Radiologist'),
             ('Log Owner / Role', 'Tom Reyes / Radiology research tech (P-09)'), ('Controlled Record Location', 'ISF tab 7 (Imaging) / IQL-014-10')]:
    meta(p[0], k, v)
for n in (1, 2):
    for k, v in [('Study / Site Code', 'GLENOS-01 / 014'), ('IQL Record ID / Revision', 'IQL-014-10 / r1'), ('Review Period', 'Oct 2026'), ('Log Sheet No. / Total', f'{n} / 2')]:
        meta(p[n], k, v)
# C: image-set log
C = [('014-0006 / Screening', 'PSEAR-014-0006', 'Eligibility', 'Original', '', 'XR 4 views + CT', 'Within 60 d pre-op / 2 Oct', 'In window', 'Complete', 'Adequate', 'Usable', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-031', 'T. Reyes / 2 Oct', 'N/A'),
     ('014-0005 / Day 1', 'ICDL-014-005', 'Post-op check', 'Original', '', 'XR AP + Y', 'Day 0-2 / 10 Oct', 'In window', 'Complete', 'Limited', 'Limited use', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-034', 'L. Ortiz / 10 Oct', 'R01'),
     ('014-0003 / 6 weeks', 'PFVR-014-0003-W6', 'Follow-up', 'Original', '', 'XR 3 views', 'Day 35-49 / 21 Oct (d52)', 'Outside', 'Complete', 'Adequate', 'Limited use', ['Archived', 'Transferred'], 'TX-036', 'T. Reyes / 21 Oct', 'R02'),
     ('014-0004 / 6 weeks', 'PFVR-014-0004-W6', 'Follow-up', 'Original', '', 'XR 3 views', 'Day 35-49 / 24 Oct', 'In window', 'Partial', 'Adequate', 'Pending', ['Archived'], '', 'T. Reyes / 24 Oct', 'R03'),
     ('014-0004 / 6 weeks', 'PFVR-014-0004-W6', 'Follow-up', 'Repeat', '04', 'XR axillary', 'Day 35-49 / 28 Oct', 'In window', 'Complete', 'Adequate', 'Usable', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-038', 'L. Ortiz / 28 Oct', 'R03'),
     ('014-0007 / Screening', 'PSEAR-014-0007', 'Eligibility', 'Original', '', 'XR 4 views + CT', 'Within 60 d pre-op / 14 Oct', 'In window', 'Complete', 'Adequate', 'Usable', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-039', 'T. Reyes / 14 Oct', 'N/A'),
     ('014-0006 / Day 1', 'ICDL-014-006', 'Post-op check', 'Original', '', 'XR AP + Y', 'Day 0-2 / 17 Oct', 'In window', 'Complete', 'Limited', 'Limited use', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-040', 'L. Ortiz / 17 Oct', 'R01'),
     ('014-0005 / After revision', 'SART-014-005', 'Other', 'Supplemental', '02', 'XR AP + Y', 'Unscheduled / 29 Oct', 'N/A', 'Complete', 'Adequate', 'Usable', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-041', 'L. Ortiz / 29 Oct', 'N/A'),
     ('014-0002 / 3 months', 'PFVR-014-0002-M3', 'Follow-up', 'Original', '', 'XR 3 views', 'Day 76-104 / 22 Oct', 'In window', 'Complete', 'Non-conforming', 'Not usable', ['Archived'], '', 'T. Reyes / 22 Oct', 'R04'),
     ('014-0001 / 3 months', 'PFVR-014-0001-M3', 'Follow-up', 'Original', '', 'XR 3 views', 'Day 76-104 / 27 Oct', 'In window', 'Complete', 'Adequate', 'Usable', ['Archived', 'Transferred', 'Receipt confirmed'], 'TX-043', 'T. Reyes / 27 Oct', 'N/A')]
for row, c in zip(rows('quality-log', 0) + rows('quality-log', 1), C):
    td = row.findall('td')
    put(td[1], c[0]); put(td[2], c[1]); tick(td[3], c[2]); tick(td[4], c[3])
    if c[4]: rel = td[4].find('span[@class="rel"]'); rel.text = 'Related: '; rel.append(E('span', 'demo-fill inl', c[4]))
    put(td[5], c[5]); put(td[6], c[6]); tick(td[7], c[7]); tick(td[8], c[8]); tick(td[9], c[9]); tick(td[10], c[10]); tick(td[11], *c[11])
    if c[12]: rel = td[11].find('span[@class="rel"]'); rel.text = 'Ref.: '; rel.append(E('span', 'demo-fill inl', c[12]))
    put(td[12], c[13]); put(td[13], c[14])
# D: period summary
meta(p[3], 'Log Sheets Reviewed', '2')
meta(p[3], 'Distinct Image Sets Reviewed (N)', '10')
D = [('1 of 10', 'Set 04: axillary view not taken (pain). Repeated as set 05, complete.'),
     ('3 of 10', 'Sets 02 and 07 rotated on the ward (liner seating not visible); set 09 wrong Y-view projection. R01, R04.'),
     ('2 of 10', 'Set 04 pending until the repeat (closed 28 Oct). Set 09 not usable; repeat booked 4 Nov.'),
     ('1 of 10', 'Set 03 taken on day 52. Deviation DEV-014-007; reaches the FUCR through the PFVR.'),
     ('3 of 10', 'Set 05 repeats 04; set 02 read again after the dislocation (SART-014-005); set 09 to be repeated.'),
     ('2 of 10', 'Day-1 AP taken on the ward with the arm in a sling (sets 02, 07). Raised with the sponsor 30 Oct, query Q-IMG-12.')]
for row, (a, b) in zip(rows('review-log'), D):
    td = row.findall('td'); put(td[1], a); put(td[2], b)
# E: resolution
Er = [('R01 / 02, 07', 'Ward AP in a sling, rotated in two participants; set 02 is the only post-op image of 014-0005 before the dislocation.', 'Seating not assessable in either set; use limited to the clinical check.', 'ICDL-014-005, -006; SART-014-005; Q-IMG-12', 'L. Ortiz / 15 Nov', 'Handed off'),
      ('R02 / 03', 'Taken on day 52 (participant travel). Visit date confirmed with the PFVR.', 'Images adequate; usable for clinical follow-up, not for the 6-week endpoint.', 'PFVR-014-0003-W6; DEV-014-007', 'M. Silva / 5 Nov', 'Resolved'),
      ('R03 / 04, 05', 'Axillary view missing (pain). Repeat booked inside the window.', 'Set 05 on 28 Oct, complete and usable. Set 04 kept as recorded.', 'PFVR-014-0004-W6', 'T. Reyes / 28 Oct', 'Resolved'),
      ('R04 / 09', 'Y view taken in the wrong projection by a new technologist. Repeat booked 4 Nov, still in window.', 'Pending the repeat; technologist briefed on the manual 23 Oct.', 'PFVR-014-0002-M3', 'T. Reyes / 4 Nov', 'Open')]
for row, r in zip(rows('resolution-log'), Er):
    td = row.findall('td')
    for t, v in zip(td[:5], r[:5]): put(t, v)
    tick(td[5], r[5])
# F: conclusion
cr = rows('conclusion-table')[2].findall('td'); tick(cr[2], 'Select'); put(cr[3], '31 Oct 2026 / next 30 Nov')
wb = doc.xpath('//div[contains(@class,"conclusion-basis")]')[0]
be = wb.find('.//span[@class="blank-entry"]')
put(be if be is not None else wb, 'Day-1 ward images failed twice (sets 02 and 07): liner seating cannot be seen, and set 02 is the only post-op image of 014-0005 before the dislocation. R01 handed off to the sponsor (Q-IMG-12: day-1 AP in the radiology suite, out of the sling). R04 open until the 4 Nov repeat of set 09. R02 closed as a deviation; R03 closed by the repeat.')
# G: sign-off
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    r = sg.xpath('./div[@class="sig-row"]/i')
    r[0].append(E('span', 'demo-fill', name)); r[1].append(E('span', 'demo-fill sig-ink', ink)); r[2].append(E('span', 'demo-fill', date))
sign('Local Imaging Reviewer / Radiology Liaison', 'Dr Lena Ortiz / Radiologist', 'L. Ortiz', '31 Oct 2026')
sign('PI Review / Acknowledgment — When Required', 'Dr Alex Morgan / PI', 'A. Morgan', '3 Nov 2026')
pc = doc.xpath('//div[contains(@class,"pi-cell")]')[0]; tick(pc, 'Required'); pc.find('span[@class="meta-entry"]').append(E('span', 'demo-fill', 'Image limitation linked to an SADE (SART-014-005)'))
meta(p[4], 'Next Review Date / Trigger', '30 Nov 2026, or the sponsor answer to Q-IMG-12')
import base64
F = '/tmp/claude-0/-home-user-Master-Thesis/c35b56ea-6e37-57ca-a7f6-4cae380cc50e/scratchpad/fonts/'
hand = base64.b64encode(open(F + '4UaErEJDsxBrF37olUeD_xHMwps.ttf', 'rb').read()).decode()
sig = base64.b64encode(open(F + 'dancing.ttf', 'rb').read()).decode()
st = etree.SubElement(doc.find('.//head'), 'style')
st.text = ('@font-face{font-family:"SimHand";font-weight:400 700;src:url(data:font/ttf;base64,' + hand + ')}'
           '@font-face{font-family:"SimSig";src:url(data:font/ttf;base64,' + sig + ')}'
           '.demo-fill{font-family:"Segoe Print","Bradley Hand","Comic Sans MS","SimHand",cursive!important;color:#174f88!important;font-weight:600!important;line-height:1.18!important}'
           'td:has(>.demo-fill),td .demo-fill,.meta-entry,.meta-entry .demo-fill{text-align:center!important}.meta-entry .demo-fill{display:block!important;width:100%}.demo-fill.inl{display:inline;font-size:8.4px!important}'
           '.meta-entry .demo-fill{font-size:10.4px}.quality-log .demo-fill{font-size:8.8px}.review-log .demo-fill,.resolution-log .demo-fill{font-size:9.6px}'
           '.conclusion-basis .demo-fill,.conclusion-table .demo-fill{font-size:10.4px}'
           '.sig-ink{font-family:"Snell Roundhand","Brush Script MT","Segoe Script","Lucida Handwriting","SimSig",cursive!important;font-size:15px!important;font-weight:400!important;text-align:left!important}')
open(OUT, 'w').write(LH.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')); print('ok')
