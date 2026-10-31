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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.7'
doc.find('.//title').text = 'FUCR v0.7 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('FUCR ID', 'FUCR-014-2026-10'),
             ('Period reviewed / data cut-off', '1 to 31 Oct 2026 / 31 Oct 2026'), ('Previous FUCR', 'FUCR-014-2026-09'), ('Review date', '3 Nov 2026'),
             ('Reason or trigger (if not routine)', 'Not applicable: monthly review'), ('Prepared by / role', 'Nadia Costa / Research nurse'), ('Accountable reviewer / role', 'Dr Alex Morgan / PI')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Routine')
for st in doc.xpath('//section[contains(@class,"sheet-strip")]'):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        be.getparent().replace(be, E('span', 'demo-entry', {'FUCR ID': 'FUCR-014-2026-10', 'Site / code': 'Riverside / 014', 'Period / data cut-off': 'Oct 2026 / 31 Oct', 'Previous FUCR': 'FUCR-014-2026-09'}[lab]))
for r, b in zip(rows('bt'), ['7 participants (014-001 to -007)', '7 visits (3-month: 4; 6-week: 2; 2-week: 1)', 'PFVR-014-001-M3 to PFVR-014-007-W2 (6 records); no PFVR for the missed 6-week visit of 014-006', 'FUCR-014-2026-09: same CIP v4.2 and schedule; comparable']):
    put(r.findall('td')[1], b)
CM = [('6', '7', '86', '7 / 7 (100%)', '-14 points', 'Closer review', '014-006 missed'),
      ('5', '6', '83', '6 / 7 (86%)', '-3 points', 'Action required', 'PFVR-014-003-M3'),
      ('1', '6', '17', '1 / 7 (14%)', 'Same', 'Action required', 'PFVR-014-003-M3 (ASES)'),
      ('1', '7', '14', '0 / 7', '+1', 'Closer review', '014-006 (3 calls, letter)')]
for r, c in zip(rows('ct'), CM):
    td = r.findall('td'); put(td[1], c[0]); put(td[2], c[1]); put(td[3], c[2]); put(td[4], c[3]); put(td[5], c[4]); tick(td[6], c[5]); put(td[7], c[6])
for r, d in zip(rows('dct'), [('6', '6', '0', '100', ''), ('4', '4', '0', '100', ''), ('6', '5', '1', '83', 'PFVR-014-003-M3 (ASES not done)'), ('6', '6', '0', '100', ''), ('6', '6', '0', '100', ''), ('Not required', '', '', '', '')]):
    td = r.findall('td')
    for k in range(5): put(td[k + 1], d[k])
for r, e in zip(rows('et'), [('6', '7', '86', 'All 6 PFVRs'), ('0', '7', '0', ''), ('0', '7', '0', ''), ('0', '7', '0', ''), ('1', '7', '14', '014-006 (outreach log OL-014-006)')]):
    td = r.findall('td')
    for k in range(4): put(td[k + 1], e[k])
for r, f in zip(rows('ft'), [('1', '4', 'Participant', '014-006 outreach log', 'Abroad 5 to 30 Oct'),
                             ('', '', '', '', ''),
                             ('2', '2, 3', 'Site', 'PFVR-014-003-M3; PFVR-014-002-M3', 'Both 1 to 14 Oct, research nurse on leave'),
                             ('', '', '', '', ''), ('', '', '', '', ''), ('', '', '', '', '')]):
    td = r.findall('td'); put(td[1], f[0]); put(td[2], f[1])
    if f[2]: tick(td[3], f[2])
    put(td[4], f[3]); put(td[5], f[4])
g = rows('gt')[0].findall('td'); put(g[0], 'Not needed'); put(g[1], 'Missing ASES is a staffing gap, not a method problem (F)')
for r, h in zip(rows('ht'), [('FUCR-A1', 'Cover plan for questionnaires when the research nurse is away (staffing)', 'SRR R-13; PIR-A2', 'Coordinator', '30 Nov', 'No missing questionnaire in November and December'),
                             ('FUCR-A2', 'Offer 014-006 an unscheduled visit to collect the 6-week scores', 'PFVR-014-006-W6', 'Research nurse', '10 Nov', 'Scores collected, or the limit recorded in the PFVR')]):
    td = r.findall('td')
    for k in range(6): put(td[k], h[k])
i = rows('it')[0].findall('td'); put(i[0], 'FUCR-09-A1'); put(i[1], 'Reminder call 3 days before each visit: no visit late for scheduling'); put(i[2], 'October: 0 visits late for scheduling'); tick(i[3], 'Worked')
j = rows('jt'); tick(j[0], 'Action required')
j[1].findall('td')[1].append(E('span', 'demo-fill txt', 'Six of seven visits in window; one participant abroad (014-006). The only missing component, the ASES at 014-003, and the late ASES page at 014-002 both fall in the two weeks the research nurse was away: a site cause with no cover plan. PIR indicator 3: 5 of 7 visits in window with all components.'))
put(j[2].findall('td')[1], 'PIR-014-2026-10, indicator 3; SRR R-13')
put(j[3].findall('td')[1], 'FUCR-014-2026-11, 3 Dec 2026')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Prepared by', 'Nadia Costa / Research nurse', 'N. Costa', '3 Nov 2026')
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
