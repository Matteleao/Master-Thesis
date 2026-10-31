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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.8'
doc.find('.//title').text = 'FUCR v0.8 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('FUCR ID', 'FUCR-014-2026-10'),
             ('Period reviewed / data cut-off', '1 to 31 Oct 2026 / 31 Oct 2026'), ('Previous FUCR', 'FUCR-014-2026-09'), ('Review date', '3 Nov 2026'),
             ('Participants due (n) · visits expected (n)', '7 · 7 this period; 23 since July'), ('PFVRs used (IDs or range)', 'PFVR-014-001-W2 to PFVR-014-007-W2; none for the missed 6-week visit of 014-006'),
             ('Document owner / role', 'Nadia Costa / Research nurse')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Routine')
for st in doc.xpath('//section[contains(@class,"sheet-strip")]'):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        be.getparent().replace(be, E('span', 'demo-entry', {'FUCR ID': 'FUCR-014-2026-10', 'Site / code': 'Riverside / 014', 'Period / data cut-off': 'Oct 2026 / 31 Oct', 'Rule (PIR rule sheet, indicator 3)': 'PIR-03: 90% or more'}[lab]))
MAP = [('014-001', 'Complete', 'Complete', 'Complete', 'Not due', '', ''), ('014-002', 'Complete', 'Complete', 'Complete', 'Not due', '', ''),
       ('014-003', 'Complete', 'Complete', 'Incomplete', 'Not due', '', ''), ('014-004', 'Complete', 'Late', 'Complete', 'Not due', '', ''),
       ('014-005', 'Complete', 'Complete', 'Not due', '', '', ''), ('014-006', 'Complete', 'Missed', 'Not due', '', '', ''), ('014-007', 'Complete', 'Not due', '', '', '', '')]
for r, m in zip(rows('bm'), MAP):
    td = r.findall('td')
    for k in range(7): put(td[k], m[k])
CM = [('6 / 7', '42 to 100%', '22 / 23', '78 to 100%', '90% or more', 'Cannot tell yet'),
      ('5 / 6', '36 to 100%', '19 / 22', '65 to 97%', '90% or more', 'Cannot tell yet'),
      ('1 / 6', '0 to 64%', '2 / 22', '1 to 29%', '5% or less', 'Cannot tell yet'),
      ('1 / 7', '0 to 58%', '1 / 23', '0 to 22%', '5% or less', 'Cannot tell yet')]
for r, c in zip(rows('ct'), CM):
    td = r.findall('td')
    for k in range(5): put(td[k + 1], c[k])
    tick(td[6], c[5])
DC = [('7 / 7', '5 / 5', '4 / 4', '', '', ''), ('Not required', '5 / 5', '4 / 4', '', '', ''), ('7 / 7', '5 / 5', '3 / 4', '', '', ''), ('7 / 7', '5 / 5', '4 / 4', '', '', ''), ('7 / 7', '5 / 5', '4 / 4', '', '', '')]
for r, d in zip(rows('dct'), DC):
    td = r.findall('td')
    for k in range(6): put(td[k + 1], d[k])
for r, e in zip(rows('et'), [('7', '+1', '-2, +4', '0', '± 4 days'), ('5', '+3', '0, +9', '1 (014-004, +9)', '± 7 days'), ('4', '-3', '-4, +1', '0', '± 14 days'),
                             ('0', '', '', '', '± 30 days'), ('0', '', '', '', '± 30 days'), ('0', '', '', '', '± 30 days')]):
    td = r.findall('td')
    for k in range(5): put(td[k + 1], e[k])
for r, f in zip(rows('ft'), [('Research nurse away (questionnaires, data entry)', 'Visits during her absences (Aug and 1 to 14 Oct)', '2 / 4', '1 / 18', '0.07', 'Cannot tell yet'),
                             ('Participant travel', 'Participants living abroad part of the year', '1 / 1', '0 / 6', '0.14', 'Cannot tell yet')]):
    td = r.findall('td')
    for k in range(5): put(td[k], f[k])
    tick(td[5], f[5])
for r, g in zip(rows('gt'), [('FUCR-A1', 'Named backup for questionnaires and data entry during absence', 'SRR R-13; PIR-A2', 'Coordinator', '30 Nov', 'No incomplete questionnaire in Nov and Dec; repeat the test in F'),
                             ('FUCR-A2', 'Ask about travel at consent and book visits around it', 'Consent checklist', 'Research nurse', '15 Nov', 'No visit missed for travel in the next 3 months')]):
    td = r.findall('td')
    for k in range(6): put(td[k], g[k])
gi = rows('gi')[0].findall('td'); put(gi[0], 'FUCR-09-A1'); put(gi[1], 'Reminder call 3 days before each visit: no visit late for scheduling'); put(gi[2], 'Oct: 0 late for scheduling (E)'); tick(gi[3], 'Worked')
h = rows('ht'); tick(h[0], 'Watch next period')
h[1].findall('td')[1].append(E('span', 'demo-fill txt', 'Every interval still contains the 90% limit: four months of data cannot show whether follow-up is below the rule. The map puts the problems on two lines (014-003, 014-006) and the 6-week column; the 6-week visits also drift late (median +3 days). The absence test (p 0.07) points the same way without proving it. PIR indicator 3: 5 of 7 this period.'))
put(h[2].findall('td')[1], 'PIR-014-2026-10, indicator 3; SRR R-13')
put(h[3].findall('td')[1], 'FUCR-014-2026-11, 3 Dec 2026')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Document owner', 'Nadia Costa / Research nurse', 'N. Costa', '3 Nov 2026')
sign('Principal Investigator', 'Dr Alex Morgan', 'A. Morgan', '4 Nov 2026')
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
