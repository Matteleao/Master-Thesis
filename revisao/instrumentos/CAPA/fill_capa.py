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
for v in doc.xpath('//div[@class="version"]'): v.text = 'SIMULATED · v1.0'
doc.find('.//title').text = 'CAPA v1.0 - Simulated Editable'
for k, v in [('Study / protocol', 'GLENOS-01 / GS-2026-01'), ('Site / code', 'Riverside Orthopedic Center / 014'), ('CAPA log ID', 'CAPA-LOG-014 / review 2'), ('Review period / cut-off', '1 Aug to 5 Nov 2026 / 5 Nov 2026'),
             ('Authoritative CAPA source (QMS extract)', 'Hospital QMS extract QMS-014-1105'), ('Log owner / role', 'Maria Silva / Study Coordinator'), ('Previous review', 'CAPA-LOG-014 review 1 (31 Jul 2026)')]:
    meta(k, v)
tick(doc.xpath('//section[contains(@class,"meta-grid")]')[0], 'Periodic')
for n, st in enumerate(doc.xpath('//section[contains(@class,"sheet-strip")]')):
    for c in st.xpath('./div[contains(@class,"meta-cell")]'):
        lab = c.find('b').text_content().strip(); be = c.find('.//span[@class="blank-entry"]')
        be.getparent().replace(be, E('span', 'demo-entry', {'CAPA log ID': 'CAPA-LOG-014 / review 2', 'Site / code': 'Riverside / 014', 'Review period / cut-off': '1 Aug to 5 Nov 2026', 'Sheet no. / total sheets': '1 of 1', 'Previous review': 'Review 1, 31 Jul 2026'}[lab]))
REG = [('CAPA-014-01', '20 Jul · 30 Sep', 'Reopened', 'Study tasks done before release on the delegation log', 'IMC-014-01; reopened by IMC-014-02', '7', 'Medium', 'Reopened', 'Coordinator'),
       ('CAPA-014-02', '26 Aug · 31 Oct', 'New', 'Image sets taken late at the 2-week visit', 'IQL-014 review, Aug', '4', 'Low', 'Closed: effective', 'Radiology tech'),
       ('CAPA-014-03', '22 Oct · open', 'New', 'Constant scores transcribed wrongly into the CRF', 'IMC-014-02, check 9', '6', 'Medium', 'In progress', 'Coordinator'),
       ('CAPA-014-04', '5 Nov · open', 'New', 'Loaner sets reach theatre without trial liners', 'PIR-014-2026-10, E-1', '9', 'High', 'Open', 'OR nurse lead')]
for r, g in zip(rows('ct'), REG):
    td = r.findall('td'); put(td[0], g[0]); put(td[1], g[1]); tick(td[2], g[2]); put(td[3], g[3]); put(td[4], g[4]); put(td[5], g[5]); tick(td[6], g[6]); put(td[7], g[7]); put(td[8], g[8])
for r, (res, ev) in zip(rows('rt'), [('Yes', 'QMS-014-1105: 4 CAPAs'), ('Yes', ''), ('Yes', ''), ('No', 'CAPA-014-02 shown as open in the QMS; closed 31 Oct, QMS corrected 6 Nov')]):
    td = r.findall('td'); tick(td[1], res); put(td[2], ev)
X = {4: ('', '', '1', '1', 'CAPA-014-02'), 6: ('', '1', '', '1', 'CAPA-014-03'), 7: ('', '1', '', '1', 'CAPA-014-01'), 9: ('1', '', '', '1', 'CAPA-014-04')}
xt = rows('xt')
for i, r in enumerate(xt[:9]):
    td = r.findall('td'); v = X.get(i + 1, ('', '', '', '0', ''))
    for k in range(5): put(td[k + 1], v[k])
for k, v in enumerate(['1', '2', '1', '4', '']): put(xt[9].findall('td')[k + 1], v)
for r, e in zip(rows('et'), [('Two CAPAs come from a check made against a list that was incomplete: the delegation log (01) and the loaner-set check sheet (04)', '01, 04', 'Both checks were done and signed; the list itself missed the item (new surgeon, trial liners). Review 1: 0 such CAPAs', 'Supported', 'SRR: new risk "checklist content not reviewed"; PIR indicator 2'),
                             ('Transcription errors appear in the weeks the research nurse was away', '03', 'CAPA-014-03 and FUCR-014-2026-10: same 1 to 14 Oct window', 'Supported', 'SRR R-13 (cover plan)'),
                             ('Imaging delays', '02', 'One CAPA, closed effective; no repeat in Sep and Oct', 'Not supported', 'None')]):
    td = r.findall('td')
    for k in range(3): put(td[k + 1], e[k])
    tick(td[4], e[3]); put(td[5], e[4])
for r, f in zip(rows('ft'), [('CAPA-014-01', 'Check TRE release before a name goes on the task roster; audit 10 tasks', 'Coordinator', '30 Nov', 'Roster check sheet; audit result', 'POT-014-07'),
                             ('CAPA-014-03', 'Second check of every endpoint entry since August', 'Coordinator', '15 Nov', 'Second-check log', 'None'),
                             ('CAPA-014-04', 'Root cause with the sponsor; trial liners on the check sheet', 'OR nurse lead', '15 Nov', 'Revised check sheet LS-07 rev. 2', 'PI (high criticality)')]):
    td = r.findall('td')
    for k in range(6): put(td[k], f[k])
for r, g in zip(rows('gt'), [('CAPA-014-02', 'No late 2-week image set for two months', 'Sep and Oct', 'IQL: 0 late sets of 9', 'Close: effective', 'None · M. Silva, 31 Oct'),
                             ('CAPA-014-01', 'No study task before release for three months', 'Aug to Oct', 'IMC-014-02: 4 tasks by S-03 before release (Oct)', 'Reopen', 'Earlier closure (30 Sep) was too early · M. Silva')]):
    td = r.findall('td')
    for k in (0, 1, 2, 3, 5): put(td[k], g[k])
    tick(td[4], g[4])
for r, h in zip(rows('ht'), [('New risk: checklist content not reviewed when people or kits change', 'Pattern E-1', 'SRR-014 v4', '7 Nov'), ('Cover plan for research nurse absence', 'Pattern E-2', 'SRR R-13', '7 Nov'), ('CAPA-014-04 reviewed by the PI', 'CAPA-014-04', 'POT-014-08', '6 Nov')]):
    td = r.findall('td')
    for k in range(4): put(td[k], h[k])
hd = rows('hd'); tick(hd[0], 'Under control with open CAPAs'); put(hd[1].findall('td')[1], '3 · high: CAPA-014-04')
hd[2].findall('td')[1].append(E('span', 'demo-fill txt', 'Four CAPAs, all reconciled with the QMS. One closed effective; one reopened because the first closure came before its check could show anything. Two CAPAs share the same weakness: the checks were done, but against lists nobody reviewed when people or kits changed. Residual risk stays until CAPA-014-04 is effective; the PI reviews it in POT-014-08.'))
put(hd[3].findall('td')[1], 'Review 3, 5 Feb 2027; earlier if CAPA-014-04 slips')
def sign(title, name, ink, date):
    sg = [s for s in doc.xpath('//div[@class="signature"]') if s.find('b').text_content().strip() == title][0]
    fl = sg.xpath('./div[@class="sig-field"]'); fl[0].append(E('span', 'demo-fill inl', name))
    line = fl[1].find('span[@class="sig-line"]'); ik = E('span', 'sig-ink', ink); ik.tail = '  '; line.append(ik); line.append(E('span', 'demo-fill inl', date))
sign('Log owner', 'Maria Silva / Study Coordinator', 'M. Silva', '6 Nov 2026')
sign('Principal Investigator', 'Dr Alex Morgan', 'A. Morgan', '7 Nov 2026')
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
