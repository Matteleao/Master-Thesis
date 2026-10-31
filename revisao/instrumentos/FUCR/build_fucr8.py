# FUCR v0.8 (blank): visit map, exact intervals, components by time point, concentration test.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>FUCR v0.8 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'fucr-').replace('Editor do POT', 'Editor do FUCR').replace('POT', 'FUCR')
V, NP = 'FUCR v0.8', 4
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">FUCR - Follow-up Compliance Review</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">FUCR · v0.8</div></header>')
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
bar = lambda t: f'<div class="exh">{t}</div>'
def strip():
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['FUCR ID', 'Site / code', 'Period / data cut-off', 'Rule (PIR rule sheet, indicator 3)']) + '</section>'
TP = ['2 weeks', '6 weeks', '3 months', '6 months', '12 months', '24 months']
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('FUCR ID'),
               meta('Period reviewed / data cut-off'), meta('Previous FUCR'), meta('Review type', ck('Routine', 'Intensified', 'Triggered', cls='opts left')), meta('Review date'),
               meta('Participants due (n) · visits expected (n)'), meta('PFVRs used (IDs or range)', cls=' span2'), meta('Document owner / role')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The FUCR reads follow-up across all participants and visits, using the Participant Follow-up Visit Records (PFVR) without reopening them. It maps every visit (B), gives each follow-up measure with an exact 95% interval so that small numbers are not over-read (C), shows which components fail at which time point (D) and how far visits drift from target (E), and tests whether problems concentrate on a person, a period or a component (F). Its result feeds indicator 3 of the Performance Indicator Record (PIR).</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One site and one period, read against all visits to date.</td>'
     '<td>Whether follow-up is under control, where problems sit and whether they share a cause.</td>'
     '<td>PFVRs, CIP visit schedule, outreach records, the PIR rule sheet.</td>'
     '<td>Measures with intervals for the PIR; causes and actions with their check.</td></tr></tbody></table>')
B = (sec('B', 'Visit map', 'One line per participant due, every visit to date. Write in each cell: Complete, Late, Incomplete, Missed or Not due. A column or a line with several problems shows where they sit.') +
     table('bm', [16] + [14] * 6, ['Participant'] + TP, [tr(td('', 'rid'), *[td() for _ in TP]) for _ in range(10)]))
pages.append(f'<main class="page">{top("Review identification, purpose and visit map")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and visit map", 1)}</main>')
# ---------- Page 2: C + D (landscape)
MEAS = ['Visits completed within their window', 'Visits with every required component', 'Visits missing an endpoint component', 'Participants not seen despite documented efforts']
C = (sec('C', 'Follow-up measures with exact intervals', 'Give n / N and the exact (Clopper-Pearson) 95% interval for this period and for all periods to date. Read the rule limit against the interval: interval wholly on the right side of the limit, within rule; limit inside the interval, the data cannot yet tell (closer review); interval wholly on the wrong side, action required.') +
     table('ct', [22, 10, 12, 10, 12, 10, 24], ['Measure', 'This period n / N', '95% interval', 'All periods n / N', '95% interval', 'Rule limit', 'Reading against the limit'],
           [tr(el(f'{i + 1} · {m}'), td(), td(), td(), td(), td(), td(ck('Within rule', 'Cannot tell yet', 'Action required', cls='opts col'))) for i, m in enumerate(MEAS)]))
COMP = ['Imaging', 'Clinical scores', 'Participant questionnaires', 'Examination and range of motion', 'Interval safety review']
D = (sec('D', 'Components by time point', 'Write complete / required for each component at each time point; Not required where the CIP does not ask for it.') +
     table('dct', [24] + [12.66] * 6, ['Component'] + TP, [tr(el(c), *[td() for _ in TP]) for c in COMP]))
pages.append(f'<main class="page landscape">{top("Measures and components")}{strip()}<section class="section compact">{C}</section><section class="section compact">{D}</section>{foot("Measures and components", 2)}</main>')
# ---------- Page 3: E + F
E = (sec('E', 'Distance from target by time point', 'From the PFVRs: days between the target date and the visit. A drift towards the window edge warns before visits fall outside it.') +
     table('et', [22, 12, 16, 16, 14, 20], ['Time point', 'Visits done', 'Median days from target', 'Range (earliest, latest)', 'Outside window', 'Window (CIP)'], [tr(el(t), td(), td(), td(), td(), td()) for t in TP]))
F = (sec('F', 'Causes and concentration', 'For each cause, compare the problem rate where it is suspected (a person, weeks, a component) with the rest, and give the two-sided Fisher exact p. With small numbers a high p does not clear a cause; it means the data cannot show it yet.') +
     table('ft', [20, 20, 15, 15, 10, 20], ['Cause (from the PFVRs)', 'Where it is suspected', 'Problems there (n / N)', 'Problems elsewhere (n / N)', 'Fisher p', 'Conclusion'],
           [tr(td('', 'left'), td('', 'left'), td(), td(), td(), td(ck('Concentrated', 'Not concentrated', 'Cannot tell yet', cls='opts col'))) for _ in range(4)]))
pages.append(f'<main class="page">{top("Distance from target and causes")}{strip()}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Distance from target and causes", 3)}</main>')
# ---------- Page 4: G + H
G = (sec('G', 'Actions and earlier actions', 'One action per cause found in F, with the check that will show it worked; then the actions from earlier reviews.') +
     table('gt', [9, 27, 15, 12, 8, 29], ['Action', 'What will change (cause in F)', 'Receiving record', 'Owner', 'Due', 'How we will know it worked'], [tr(td(), td('', 'left'), td('', 'left'), td(), td(), td('', 'left')) for _ in range(3)]) +
     table('gi', [12, 34, 32, 22], ['Earlier action', 'Check set when assigned', 'What this period shows', 'Result'], [tr(td(), td('', 'left'), td('', 'left'), td(ck('Worked', 'Did not work', 'Too early', cls='opts col'))) for _ in range(2)]))
H = (sec('H', 'Conclusion') +
     table('ht', [32, 68], None, [tr(el('Follow-up in this period'), td(ck('Under control', 'Watch next period', 'Action required', 'Escalation required', cls='opts left'), 'left')),
                                  tr(el('Basis (measures, map, causes)'), td('', 'left tall')),
                                  tr(el('Sent to (PIR indicator 3, IMC, CAPA, SRR, POT)'), td('', 'left')),
                                  tr(el('Next review'), td('', 'left'))]) +
     '<div class="sig2"><div class="signature"><b>Document owner</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Actions and conclusion")}{strip()}<section class="section compact">{G}</section><section class="section compact">{H}</section>{foot("Actions and conclusion", 4)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:50px}.meta-cell.span2{grid-column:span 2}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:4px 8px;vertical-align:top;text-align:left;height:44px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}td.rid,td.num{font-weight:700;color:#173c67;font-size:9px}
.bm td{height:48px;font-size:8.6px;padding:2px 5px}
.ct td{height:52px;font-size:8.6px;padding:2px 5px}.ct .opts{font-size:7.6px}.ct th{font-size:8.2px}
.dct td{height:37px;font-size:8.6px;padding:2px 5px}
.et td{height:54px;font-size:8.8px;padding:3px 6px}
.ft td{height:88px;font-size:8.8px;padding:3px 6px}.ft .opts{font-size:7.8px}
.gt td{height:70px;font-size:8.8px;padding:3px 6px}.gi{margin-top:7px}.gi td{height:64px;font-size:8.8px;padding:3px 6px}.gi .opts{font-size:7.8px}
.ht td{height:44px;font-size:8.8px;padding:3px 7px}.ht td.tall{height:110px}.ht td.el{background:#dbe7f3!important;text-align:center;vertical-align:middle}.ht .opts{font-size:7.8px}
.sig2 .signature{min-height:100px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
