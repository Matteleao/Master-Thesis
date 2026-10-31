# CAPA Log v1.0 (blank): site portfolio of CAPAs for one review period.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>CAPA v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'capa-').replace('Editor do POT', 'Editor do CAPA').replace('POT', 'CAPA')
V, NP = 'CAPA v1.0', 6
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">CAPA - Corrective and Preventive Action Log</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">CAPA · v1.0</div></header>')
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
pages = []
YN = lambda *l: ck(*l, cls='opts col')
bar = lambda t: f'<div class="exh">{t}</div>'
def strip(sheet=False):
    cells = ['CAPA log ID', 'Site / code', 'Review period / cut-off'] + (['Sheet no. / total sheets'] if sheet else ['Previous review'])
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in cells) + '</section>'
CATS = [('Participant rights and consent', 'Consent, confidentiality, participant rights'), ('Protocol and procedure', 'A CIP requirement or procedure step not followed'),
        ('Safety and device', 'Safety reporting, device deficiency, accountability'), ('Endpoint, imaging and assessment', 'Image, score or measurement quality'),
        ('Follow-up and retention', 'Visit timing, completeness, recovery'), ('Data and documentation', 'Source, CRF, queries, filing'),
        ('Training and delegation', 'Training, release, delegation, supervision'), ('Oversight and governance', 'PI oversight, review, escalation'),
        ('Systems and suppliers', 'Equipment, supplier, loaner sets, facilities')]
CRIT = [('High', 'Can harm a participant, the device evidence or an endpoint; PI review now'), ('Medium', 'Repeats or affects several records; PI review at the next review'), ('Low', 'Isolated, no effect on safety or endpoints')]
STAT = [('Open', 'Analysis or plan pending'), ('In progress', 'Actions being carried out'), ('Effect pending', 'Actions done; effect not yet shown'),
        ('Closed: effective', 'Check met'), ('Closed with limit', 'Limit and residual risk accepted by the PI'), ('Reopened', 'Problem came back; same ID')]
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('Site / code'), meta('CAPA log ID'), meta('Review period / cut-off'),
               meta('Review type', ck('Periodic', 'Triggered', 'Close-out', cls='opts left')), meta('Authoritative CAPA source (QMS extract)'), meta('Log owner / role'), meta('Previous review')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The CAPA log lists every corrective and preventive action (CAPA) of the site in one review period and reads them together: whether the list matches the authoritative CAPA source (D), where they concentrate (D), whether separate CAPAs share a cause (E), which ones are still active (F) and whether closed ones worked (G). Each CAPA keeps its own investigation and plan in its own record; the log cites them and does not repeat them.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>The site\'s CAPAs for one period, one line each.</td>'
     '<td>Whether the portfolio is under control, which CAPAs need follow-up, closure or reopening, and whether a pattern needs escalation.</td>'
     '<td>CAPA records, the deviation, IMC, PIR, CSST and SRR records that raised them.</td>'
     '<td>Distribution, patterns, follow-up and effectiveness; updates to the SRR, PIR and POT.</td></tr></tbody></table>')
cat_rows = [tr(td(str(i + 1), 'num'), el(a), td(b, 'left')) for i, (a, b) in enumerate(CATS)]
B = (sec('B', 'Classifications', 'One category, one criticality and the status from the authoritative source for each CAPA.') +
     bar('Category') + table('cat', [6, 34, 60], ['No.', 'Category', 'Use when the main problem is'], cat_rows) +
     '<div class="two">' + '<div>' + bar('Criticality') + table('crt', [24, 76], ['Criticality', 'Use when'], [tr(el(a), td(b, 'left')) for a, b in CRIT]) + '</div>' +
     '<div>' + bar('Status') + table('stt', [36, 64], ['Status', 'Meaning'], [tr(el(a), td(b, 'left')) for a, b in STAT]) + '</div></div>')
pages.append(f'<main class="page">{top("Log identification, purpose and classifications")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and classifications", 1)}</main>')
# ---------- Page 2: C register (landscape)
C = (sec('C', 'CAPA register', 'One line per CAPA in the period: New (opened in the period), Carried (active at the start) or Reopened. A reopened CAPA keeps its ID. Problem in one factual sentence; the content stays in the CAPA record.') +
     table('ct', [9, 10, 9, 26, 14, 7, 9, 9, 7], ['CAPA ID', 'Opened · closed', 'Basis', 'Problem (one sentence)', 'Raised by (record)', 'Category no.', 'Criticality', 'Status', 'Owner'],
           [tr(td('', 'rid'), td(), td(ck('New', 'Carried', 'Reopened', cls='opts col')), td('', 'left'), td('', 'left'), td(), td(ck('High', 'Medium', 'Low', cls='opts col')), td(), td()) for _ in range(10)]))
pages.append(f'<main class="page landscape">{top("CAPA register")}{strip(True)}<section class="section compact">{C}</section>{foot("CAPA register", 2)}</main>')
# ---------- Page 3: D reconciliation + distribution
rec = ['Every CAPA in the authoritative source for the period is in the register', 'No CAPA in the register is missing from the source', 'No duplicate CAPA ID', 'Status in the register matches the source']
D = (sec('D', 'Reconciliation and distribution', 'Check the register against the authoritative source before counting. Count each CAPA once.') +
     bar('Reconciliation') + table('rt', [56, 12, 32], ['Check', 'Result', 'Source extract · correction'], [tr(el(r), td(ck('Yes', 'No', cls='opts')), td('', 'left')) for r in rec]) +
     bar('Distribution by category and criticality') +
     table('xt', [36, 11, 11, 11, 11, 20], ['Category', 'High', 'Medium', 'Low', 'Total', 'CAPA IDs'], [tr(el(f'{i + 1} · {a}'), td(), td(), td(), td(), td('', 'left')) for i, (a, b) in enumerate(CATS)] +
           [tr(el('Total'), td('', 'tot'), td('', 'tot'), td('', 'tot'), td('', 'tot'), td('', 'tot'), cls='tot')]))
pages.append(f'<main class="page">{top("Reconciliation and distribution")}{strip()}<section class="section compact">{D}</section>{foot("Reconciliation and distribution", 3)}</main>')
# ---------- Page 4: E + F (landscape)
E = (sec('E', 'Patterns across CAPAs', 'Look for CAPAs that share a cause, a process step, a person, a supplier or a period, and compare with earlier reviews. Cite the CAPA records; do not repeat their investigation.') +
     table('et', [4, 22, 12, 26, 18, 18], ['#', 'Pattern seen', 'CAPA IDs', 'What was compared (records and counts)', 'Shared cause?', 'Decision · route'],
           [tr(num(i), td('', 'left'), td(), td('', 'left'), td(ck('Supported', 'Not supported', 'Open', cls='opts col')), td('', 'left')) for i in range(1, 4)]))
F = (sec('F', 'Active CAPAs', 'Every CAPA that is open, in progress, effect pending or reopened. The plan stays in the CAPA record.') +
     table('ft', [10, 12, 26, 12, 10, 18, 12], ['CAPA ID', 'Status', 'Next step', 'Owner', 'Due', 'Evidence expected or missing', 'Escalation'],
           [tr(td(), td(), td('', 'left'), td(), td(), td('', 'left'), td('', 'left')) for _ in range(5)]))
pages.append(f'<main class="page landscape">{top("Patterns and active CAPAs")}{strip()}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Patterns and active CAPAs", 4)}</main>')
# ---------- Page 5: G effectiveness (landscape)
G = (sec('G', 'Effectiveness, closure and reopening', 'Use the check set in each CAPA. Done is not the same as effective; a closure with a limit needs the residual risk accepted by the PI.') +
     table('gt', [9, 23, 14, 22, 13, 19], ['CAPA ID', 'Check set in the CAPA', 'Period checked', 'Evidence and result', 'Decision', 'Limit · residual risk · evaluator'],
           [tr(td(), td('', 'left'), td(), td('', 'left'), td(ck('Close: effective', 'Close with limit', 'Keep open', 'Reopen', cls='opts col')), td('', 'left')) for _ in range(5)]))
pages.append(f'<main class="page landscape">{top("Effectiveness and closure")}{strip()}<section class="section compact">{G}</section>{foot("Effectiveness and closure", 5)}</main>')
# ---------- Page 6: H
H = (sec('H', 'Outputs and conclusion', 'Only outputs created by this review; the receiving record keeps the content.') +
     table('ht', [30, 16, 24, 30], ['Output or update', 'From (CAPA or pattern)', 'Sent to (record)', 'Confirmed (date)'], [tr(td('', 'left'), td(), td('', 'left'), td()) for _ in range(4)]) +
     table('hd', [30, 70], None, [tr(el('Portfolio'), td(ck('Under control', 'Under control with open CAPAs', 'Not under control: escalation', cls='opts left'), 'left')),
                                  tr(el('Active CAPAs (number) · high criticality (IDs)'), td('', 'left')),
                                  tr(el('Rationale and residual risk'), td('', 'left tall')),
                                  tr(el('Next review'), td('', 'left'))]) +
     '<div class="sig2"><div class="signature"><b>Log owner</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Outputs and conclusion")}{strip()}<section class="section compact">{H}</section>{foot("Outputs and conclusion", 6)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:52px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:4px 8px;vertical-align:top;text-align:left;height:50px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}td.num,td.rid{font-weight:700;color:#173c67;font-size:9px}
.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9px;padding:3px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:6px}.exh+table{margin-top:0!important}
.cat td,.crt td,.stt td{height:30px;font-size:8.6px;padding:2px 6px}.crt td{height:60px}.two{display:grid;grid-template-columns:47% 52%;gap:1%}
.ct td{height:47px;font-size:8.6px;padding:2px 5px}.ct .opts{font-size:7.4px;line-height:1.15}
.rt td{height:56px;font-size:8.8px;padding:3px 7px}.rt .opts{font-size:7.8px}.xt td{height:51px;font-size:8.8px;padding:2px 6px}tr.tot td{font-weight:700;background:#eef3f9!important}
.et td{height:62px;font-size:8.8px;padding:3px 6px}.et .opts{font-size:7.8px}.ft td{height:42px;font-size:8.8px;padding:3px 6px}
.gt td{height:98px;font-size:8.8px;padding:3px 6px}.gt .opts{font-size:7.8px}
.ht td{height:70px;font-size:8.8px;padding:3px 6px}.hd{margin-top:7px}.hd td{height:56px;font-size:8.8px;padding:3px 7px}.hd td.tall{height:190px}.hd .opts{font-size:7.8px}
.sig2 .signature{min-height:120px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
