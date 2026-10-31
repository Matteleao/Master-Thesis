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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v0.5'
doc.find('.//title').text = 'SIFSL v0.5 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('CIP version', 'CIP v4.2'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('SIFSL ID / revision', 'SIFSL-014 / rev. 23'),
             ('Period covered / data cut-off', '16 Jun to 15 Oct 2026 / 15 Oct 2026'), ('Log owner / role', 'Maria Silva / Study Coordinator'),
             ('Identity key location (kept separately)', 'Locked cabinet R-214, key log v2'), ('Controlled location', 'ISF tab 5 (Screening) / SIFSL-014')]:
    meta(k, v)
L = [('CAND-014-001', '17 Jun', '18 Jun', 'Enrolled', '24 Jun', 'PSEAR-014-001', '', '24 Jun · 014-001', ''),
     ('CAND-014-002', '17 Jun', '', 'Withdrawn before enrollment', '19 Jun', '', '3', '', ''),
     ('CAND-014-003', '18 Jun', '22 Jun', 'Enrolled', '30 Jun', 'PSEAR-014-003', '', '30 Jun · 014-002', ''),
     ('CAND-014-004', '22 Jun', '24 Jun', 'Not eligible', '3 Jul', 'PSEAR-014-004', '1', '', ''),
     ('CAND-014-005', '25 Jun', '29 Jun', 'Enrolled', '8 Jul', 'PSEAR-014-005', '', '8 Jul · 014-003', ''),
     ('CAND-014-006', '1 Jul', '', 'Withdrawn before enrollment', '3 Jul', '', '3', '', ''),
     ('CAND-014-007', '2 Jul', '6 Jul', 'Enrolled', '15 Jul', 'PSEAR-014-007', '', '15 Jul · 014-004', ''),
     ('CAND-014-008', '9 Jul', '13 Jul', 'Not eligible', '20 Jul', 'PSEAR-014-008', '1', '', ''),
     ('CAND-014-009', '14 Jul', '16 Jul', 'Enrolled', '27 Jul', 'PSEAR-014-009', '', '27 Jul · 014-005', ''),
     ('CAND-014-010', '20 Jul', '22 Jul', 'Closed: other outcome', '4 Aug', 'PSEAR-014-010', '2', '', ''),
     ('CAND-014-011', '23 Jul', '27 Jul', 'Not eligible', '5 Aug', 'PSEAR-014-011', '1', '', ''),
     ('CAND-014-012', '28 Jul', '30 Jul', 'Enrolled', '12 Aug', 'PSEAR-014-012', '', '12 Aug · 014-006', ''),
     ('CAND-014-013', '30 Jul', '', 'Withdrawn before enrollment', '31 Jul', '', '3', '', ''),
     ('CAND-014-014', '31 Jul', '4 Aug', 'Not eligible', '14 Aug', 'PSEAR-014-014', '1', '', ''),
     ('CAND-014-015', '1 Aug', '5 Aug', 'Not eligible', '13 Aug', 'PSEAR-014-015', '1', '', ''),
     ('CAND-014-016', '3 Aug', '', 'Considered', '3 Aug', '', '', '', 'REC-01'),
     ('CAND-014-017', '4 Aug', '7 Aug', 'Not eligible', '19 Aug', 'PSEAR-014-017', '2', '', ''),
     ('CAND-014-018', '4 Aug', '10 Aug', 'Withdrawn before enrollment', '28 Aug', 'PSEAR-014-018', '3', '', ''),
     ('CAND-014-019', '4 Aug', '11 Aug', 'Enrolled', '21 Aug', 'PSEAR-014-019', '', '21 Aug · 014-007', ''),
     ('CAND-014-020', '2 Sep', '8 Sep', 'Enrolled', '18 Sep', 'PSEAR-014-020', '', '18 Sep · 014-008', 'REC-02'),
     ('CAND-014-021', '22 Sep', '25 Sep', 'Awaiting eligibility decision', '6 Oct', 'PSEAR-014-021', '', '', ''),
     ('CAND-014-022', '9 Oct', '13 Oct', 'Screening active', '13 Oct', 'PSEAR-014-022', '', '', ''),
     ('CAND-014-023', '12 Oct', '', 'Considered', '12 Oct', '', '', '', '')]
reg = rows('dt', 0) + rows('dt', 1)
for i, (r, l) in enumerate(zip(reg, L)):
    td = r.findall('td'); put(td[0], str(i + 1))
    for k, v in enumerate(l): put(td[k + 1], v)
for n, st in enumerate(doc.xpath('//section[@class="sheet-strip"]')):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        val = {'SIFSL ID / revision': 'SIFSL-014 / rev. 23', 'Site / code': 'Riverside / 014', 'Data cut-off': '15 Oct 2026', 'Sheet no. / total sheets': f'{n + 1} of 2'}[lab]
        be.getparent().replace(be, E('span', 'demo-entry', val))
et = rows('et')
for r, (res, ev) in zip(et, [('Yes', '23 lines; 11 closed with outcome'), ('Yes', '18 PSEAR IDs, all found in ISF tab 5'), ('No', 'REC-02'), ('No', 'REC-01'), ('Yes', 'EDC export 15 Oct: 8 enrolled, all in the log')]):
    td = r.findall('td'); tick(td[1], res); put(td[2], ev)
for r, v in zip(rows('it'), [('REC-01', 'Line 16: considered since 3 Aug, no follow-up recorded', 'Research nurse to contact the referring clinic; close or open screening', 'Research nurse · 22 Oct', 'Open'),
                             ('REC-02', 'Line 20: log enrollment date 17 Sep, EDC 18 Sep', 'Log corrected to 18 Sep (EDC is the source); note in log rev. 23', 'Coordinator · 16 Oct', 'Resolved')]):
    td = r.findall('td')
    for k in range(4): put(td[k], v[k])
    tick(td[4], v[4])
NT = [('2', '16, 23'), ('1', '22'), ('1', '21'), ('0', ''), ('8', '1, 3, 5, 7, 9, 12, 19, 20'), ('6', '4, 8, 11, 14, 15, 17'), ('4', '2, 6, 13, 18'), ('1', '10'), ('23', '1 to 23')]
for r, (c, l) in zip(rows('nt'), NT):
    td = r.findall('td'); put(td[1], c); put(td[2], l)
XT = [('5', '0', '0', '5'), ('1', '0', '1', '2'), ('0', '4', '0', '4'), ('0', '0', '0', '0'), ('0', '0', '0', '0'), ('0', '0', '0', '0'), ('6', '4', '1', '11')]
for r, x in zip(rows('xt'), XT):
    td = r.findall('td')
    for k in range(4): put(td[k + 1], x[k])
put(rows('rt')[0].findall('td')[1], 'PIR-014-Q3 enrollment section · coordinator · 20 Oct 2026: counts and categories; no pattern needing action')
g = rows('gt'); tick(g[0], 'Reconciled with open issues'); put(g[1].findall('td')[1], 'REC-01 open until 22 Oct; line 16 stays Considered meanwhile.')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Log owner', 'Maria Silva / Study Coordinator', 'M. Silva', '16 Oct 2026')
sign('Principal Investigator', 'Dr Alex Morgan', 'A. Morgan', '17 Oct 2026')
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
