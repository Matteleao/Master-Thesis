# ICDL v0.15 (blank) from v0.12, the Codex v0.14 alternative and the Codex analysis (A-K kept).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>ICDL v0.15 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'icdl-').replace('Editor do POT', 'Editor do ICDL').replace('POT', 'ICDL')
V, NP = 'ICDL v0.15', 6
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">ICDL - Intraoperative Checklist and Device Log</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">ICDL · v0.15</div></header>')
def sec(letter, title, guide=None):
    return f'<div class="section-header"><div class="letter">{letter}</div><div class="section-title">{title}</div></div>' + (f'<div class="guide">{guide}</div>' if guide else '')
def foot(txt, n): return f'<footer class="footer"><div>{V} | {txt}</div><div>Page {n} of {NP}</div></footer>'
def meta(label, inner='<span class="blank-entry"></span>', cls=''): return f'<div class="meta-cell{cls}"><b>{label}</b>{inner}</div>'
def table(cls, widths, heads, rows):
    col = ''.join(f'<col style="width:{w}%">' for w in widths)
    th = ''.join(f'<th>{h}</th>' for h in heads) if heads else ''
    return f'<table class="{cls}"><colgroup>{col}</colgroup>' + (f'<thead><tr>{th}</tr></thead>' if heads else '') + '<tbody>' + ''.join(rows) + '</tbody></table>'
def tr(*cells, cls=''): return (f'<tr class="{cls}">' if cls else '<tr>') + ''.join(cells) + '</tr>'
el = lambda t: f'<td class="el">{t}</td>'
td = lambda t='', c='': f'<td class="{c}">{t}</td>' if c else f'<td>{t}</td>'
num = lambda i: f'<td class="num">{i}</td>'
pages = []
YN = lambda *l: ck(*l, cls='opts col')
def strip():
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['ICDL ID', 'Participant code', 'Procedure date', 'Primary surgeon (code)']) + '</section>'
# ---------- Page 1: header, A, B
hdr = ''.join([meta('Study / protocol'), meta('Site / code'), meta('Participant code'), meta('ICDL ID'),
               meta('Procedure date'), meta('Procedure / side'), meta('Operating room'), meta('Primary surgeon (code)'),
               meta('Device / system'), meta('CIP and surgical technique (version)'), meta('Accountability record location'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The ICDL is filled in during one participant\'s procedure, not afterwards, because what happens in the operating room cannot be rebuilt reliably later. It records the release to start (B), the critical steps (C), the times and the case data the surgeon\'s learning curve record needs (D), every component used with its identifiers (E), changes to the plan (F), complications and device problems (G), the review right after surgery (H) and whether the case can be closed (I). Open actions go to J.</p>'
     '<p>It does not replace the operative note, the device accountability record, safety reporting or the formal deviation record; it captures what is first known here and points to them.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One participant and one procedure.</td>'
     '<td>Whether the case can be closed: critical steps, device identity, changes and immediate outcome documented or sent on.</td>'
     '<td>CIP and surgical plan, surgeon release (SCR, TRE), device instructions, accountability materials.</td>'
     '<td>Case entry for the SLCT; components for accountability; events to the SCML and SART; images to the IQL; deviations and CAPA.</td></tr></tbody></table>')
rel = ['Surgeon released for this procedure (SCR) and on the delegation log', 'Participant, procedure and side match the schedule and source records',
       'Consent, eligibility (PSEAR) and pre-operative checks available', 'Device system, components and instruments available and compatible',
       'Packaging, expiry, storage and sterile release acceptable', 'Planning images, measurements and case materials available']
B = (sec('B', 'Release to start', 'All items before the first incision. A No stops the start until it is resolved or a hold is recorded.') +
     table('bt', [42, 11, 26, 21], ['Control', 'Status', 'Evidence or reference', 'Exception · hold · route'], [tr(el(r), td(YN('Yes', 'No', 'N/A')), td('', 'left'), td('', 'left')) for r in rel]) +
     table('bd', [40, 20, 40], ['Release decision', 'Time', 'Responsible (name / role) · hold record'],
           [tr(td(ck('Released', 'Released with observation', 'Hold', cls='opts left')), td(), td('', 'left'))]))
pages.append(f'<main class="page">{top("Case identification, purpose and release to start")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and release to start", 1)}</main>')
# ---------- Page 2: C + D (landscape)
C = (sec('C', 'Critical steps', 'Use the critical steps of the CIP, surgical technique or site checklist. Record any step left out, adapted, repeated or out of order. N/A needs the reason; Partial, Not performed, Not acceptable or Not assessable needs a row in F or J.') +
     table('ct', [3, 25, 15, 22, 18, 17], ['#', 'Critical step', 'Done', 'Evidence or reference', 'Result', 'Initials · note'],
           [tr(num(i), td('', 'left'), td(ck('Complete', 'Partial', 'Not performed', 'N/A', cls='opts col2')), td('', 'left'), td(ck('Acceptable', 'Observation', 'Not acceptable', 'Not assessable', cls='opts col2')), td('', 'left')) for i in range(1, 6)]))
D = (sec('D', 'Times and case data for the learning curve record', 'Duration is taken from first incision to closure. Complexity uses the levels defined for the SLCT.') +
     '<div class="dwrap">' +
     table('dt', [36, 16, 30, 18], ['Time point', 'Time', 'Condition or status', 'Initials'], [tr(el(t), td(), td('', 'left'), td()) for t in ['First incision', 'Device opened / first component used', 'Final implant and configuration confirmed', 'Closure / end of procedure']]) +
     table('dh', [40, 60], ['Case data for the SLCT', 'Entry'], [tr(el('Complexity level (source)'), td('', 'left')),
                                                            tr(el('Senior support or proctoring'), td(ck('None', 'Planned', 'Unplanned', cls='opts left'), 'left')),
                                                            tr(el('SLCT entry'), td('', 'left'))]) + '</div>')
pages.append(f'<main class="page landscape">{top("Critical steps, times and case data")}{strip()}<section class="section compact">{C}</section><section class="section compact">{D}</section>{foot("Critical steps, times and case data", 2)}</main>')
# ---------- Page 3: E (landscape)
E = (sec('E', 'Components used and traceability', 'Every component used, including trials, replacements, explanted or discarded ones. Copy identifiers from the label at the time of use; never fill a missing identifier later. Reconcile with the operative note and the accountability record before closure; if it does not reconcile, the case is not closed as complete (F).') +
     table('etb', [3, 16, 15, 11, 14, 14, 10, 10, 7], ['#', 'Component · role', 'Manufacturer · model', 'Catalogue no.', 'UDI-DI', 'Lot or serial', 'Size · configuration', 'Disposition', 'Label on sheet?'],
           [tr(num(i), td('', 'left'), td('', 'left'), td(), td(), td(), td(), td(ck('Implanted', 'Trial', 'Returned', 'Discarded', 'Explanted', cls='opts col2')), td(YN('Yes', 'No'))) for i in range(1, 8)]) +
     table('ef', [26, 74], None, [tr(el('Final implanted configuration'), td('', 'left')), tr(el('Reconciled with (record and reference)'), td('', 'left'))]))
pages.append(f'<main class="page landscape">{top("Components and traceability")}{strip()}<section class="section compact">{E}</section>{foot("Components and traceability", 3)}</main>')
# ---------- Page 4: F + G
F = (sec('F', 'Changes to the plan, substitutions and exceptions', 'Whenever a planned step, component, condition or sequence is changed, left out, repeated or uncertain. It does not replace the formal deviation record.') +
     table('ft', [4, 22, 22, 22, 30], ['#', 'What happened and when', 'Reason', 'Possible effect', 'Immediate response · linked record'],
           [tr(num(i), td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left')) for i in range(1, 4)]))
G = (sec('G', 'Complications and device performance', 'Describe briefly and send on at once; the safety assessment is done in the SART.') +
     table('gt', [4, 22, 24, 18, 16, 16], ['#', 'Event or device concern', 'What was seen', 'Related to device or procedure?', 'Treatment in theatre', 'SART · SCML'],
           [tr(num(i), td('', 'left'), td('', 'left'), td(YN('Device', 'Procedure', 'Both', 'Not related', 'Unknown')), td('', 'left'), td('', 'left')) for i in range(1, 4)]) +
     '<div class="addnote">Anything that may affect participant safety, device accountability or endpoint data is sent through the local and sponsor route now; it never waits for a later review.</div>')
pages.append(f'<main class="page">{top("Changes, complications and device performance")}{strip()}<section class="section compact">{F}</section><section class="section compact">{G}</section>{foot("Changes, complications and device performance", 4)}</main>')
# ---------- Page 5: H + I
rev = ['Final configuration and implant position documented in the operative note and the linked image',
       'Component list complete and reconciled with labels and the accountability record',
       'Immediate post-operative condition documented in the source record',
       'Post-operative image taken or ordered and logged in the IQL',
       'Every safety, deviation and device-deficiency signal has a linked route']
H = (sec('H', 'Review right after surgery', 'Before closing the case, confirm the record is usable and every route is linked.') +
     table('ht', [44, 14, 24, 18], ['Item', 'Status', 'Evidence or reference', 'Open action · owner'], [tr(el(r), td(YN('Adequate', 'Partial', 'Not adequate', 'N/A')), td('', 'left'), td('', 'left')) for r in rev]) +
     table('hs', [26, 74], None, [tr(el('Summary of the review'), td('', 'left'))]))
I = (sec('I', 'Case closure', 'Complete: record usable and every route linked. Complete with open action: owner, due date and destination in J. Hold: not closed until the blocker is solved or escalated.') +
     table('it', [30, 14, 28, 28], ['Closure status', 'Time', 'Responsible (name / role)', 'Linked open action or record'],
           [tr(td(ck('Complete', 'Complete with open action', 'Hold', cls='opts col')), td(), td('', 'left'), td('', 'left'))]))
pages.append(f'<main class="page">{top("Post-operative review and case closure")}{strip()}<section class="section compact">{H}</section><section class="section compact">{I}</section>{foot("Post-operative review and case closure", 5)}</main>')
# ---------- Page 6: J + K
J = (sec('J', 'Open actions and follow-up', 'Only for an issue from B to I still open at closure. The receiving record keeps its own content; this table keeps the handoff, owner, due date and proof the action worked.') +
     table('jt', [4, 22, 20, 13, 10, 19, 12], ['#', 'Issue (section)', 'Sent to (record)', 'Owner', 'Due date', 'Proof it worked', 'Status'],
           [tr(num(i), td('', 'left'), td('', 'left'), td(), td(), td('', 'left'), td(YN('Open', 'Closed'))) for i in range(1, 5)]))
K = (sec('K', 'Signatures and filing') +
     '<div class="sig3">' + ''.join(f'<div class="signature"><b>{t}</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date and time:<span class="sig-line"></span></div></div>'
                                    for t in ['Completed by (in theatre)', 'Operating surgeon', 'Principal Investigator (if required)']) + '</div>' +
     table('kt', [30, 70], None, [tr(el(x), td('', 'left')) for x in ['ICDL filed at', 'Accountability record', 'Linked safety, deviation and image records']]))
pages.append(f'<main class="page">{top("Open actions, signatures and filing")}{strip()}<section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Open actions, signatures and filing", 6)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:48px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}.opts.col2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:2px 6px}
.purpose td{font-size:9px;padding:4px 8px;vertical-align:top;text-align:left;height:48px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.num{font-weight:700;color:#173c67;font-size:9px}
.addnote{margin-top:6px;font-size:8.6px;color:#4d5b6b;border-left:3px solid var(--navy);padding:3px 8px;background:#f7f9fb}
.bt td{height:58px;font-size:8.8px;padding:3px 6px}.bt .opts{font-size:7.8px}.bd{margin-top:6px}.bd td{height:56px;font-size:8.8px;padding:3px 6px}.bd .opts{font-size:7.8px}
.ct td{height:54px;font-size:8.6px;padding:2px 5px}.ct .opts{font-size:7.6px;line-height:1.2}
.dwrap{display:grid;grid-template-columns:62% 37%;gap:1%}.dwrap table{margin-top:0}.dt td{height:31px;font-size:8.6px;padding:2px 6px}.dh td{height:44px;font-size:8.6px;padding:2px 6px}.dh .opts{font-size:7.8px}
.etb td{height:56px;font-size:8.6px;padding:2px 5px}.etb th{font-size:8.2px}.etb .opts{font-size:7.4px;line-height:1.15}
.ef{margin-top:6px}.ef td{height:34px;font-size:8.8px;padding:3px 7px}
.ft td{height:114px;font-size:8.8px;padding:3px 6px}
.gt td{height:114px;font-size:8.8px;padding:3px 6px}.gt .opts{font-size:7.8px}
.ht td{height:86px;font-size:8.8px;padding:3px 6px}.ht .opts{font-size:7.8px}
.hs{margin-top:6px}.hs td{height:150px;font-size:8.8px;padding:3px 7px}
.it td{height:110px;font-size:8.8px;padding:3px 6px}.it .opts{font-size:7.8px}
.jt td{height:100px;font-size:8.8px;padding:3px 6px}.jt .opts{font-size:7.8px}
.kt{margin-top:8px}.kt td{height:60px;font-size:8.8px;padding:3px 7px}
.sig3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:2px}.sig3 .signature{min-height:150px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
