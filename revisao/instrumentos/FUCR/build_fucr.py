# FUCR v0.7 (blank): aggregates PFVRs for one period; four measures, components, timing, causes, actions.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>FUCR v0.7 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'fucr-').replace('Editor do POT', 'Editor do FUCR').replace('POT', 'FUCR')
V, NP = 'FUCR v0.7', 5
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">FUCR - Follow-up Compliance Review</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">FUCR · v0.7</div></header>')
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
bar = lambda t: f'<div class="exh">{t}</div>'
def strip():
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['FUCR ID', 'Site / code', 'Period / data cut-off', 'Previous FUCR']) + '</section>'
DEC = ck('Within rule', 'Closer review', 'Action required', 'Not assessable', cls='opts col2')
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('FUCR ID'),
               meta('Period reviewed / data cut-off'), meta('Previous FUCR'), meta('Review type', ck('Routine', 'Intensified', 'Triggered', cls='opts left')), meta('Review date'),
               meta('Reason or trigger (if not routine)', cls=' span2'), meta('Prepared by / role'), meta('Accountable reviewer / role')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The FUCR reviews follow-up across all participants due in one period. It counts what the Participant Follow-up Visit Records (PFVR) show and does not reopen them: whether visits happened in their window (C, E), whether each required component was done (D), why something was missed (F) and what the site will change (H). Its result feeds indicator 3 of the Performance Indicator Record (PIR), which applies the rule.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One site and one period: visits expected, completed and their components.</td>'
     '<td>Whether follow-up is under control or needs correction, and where the problem sits.</td>'
     '<td>PFVRs of the period, CIP visit schedule, outreach records, IQL for images.</td>'
     '<td>The four measures for the PIR; causes, actions and their check.</td></tr></tbody></table>')
B = (sec('B', 'Review base', 'Fix the base before counting. Write counts with their units; never change a denominator to make periods look alike.') +
     table('bt', [34, 66], None, [tr(el(x), td('', 'left')) for x in ['Participants with a visit due in the period', 'Visits expected in the period', 'PFVRs used (IDs or range) and any missing', 'Comparable previous period (same CIP and schedule?)']]))
pages.append(f'<main class="page">{top("Review identification, purpose and base")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and base", 1)}</main>')
# ---------- Page 2: C + D (landscape)
MEAS = ['Visits completed within their window', 'Visits with every required component', 'Visits missing an endpoint component', 'Participants not seen despite documented efforts']
BASE = ['Expected visits', 'Completed visits', 'Completed visits needing it', 'Participants due']
C = (sec('C', 'The four follow-up measures', 'Count from the PFVRs. The decision applies the rule of PIR indicator 3.') +
     table('ct', [21, 7, 12, 8, 10, 8, 20, 14], ['Measure', 'Count', 'Base', 'Result (%)', 'Previous period', 'Change', 'Decision', 'PFVRs counted'],
           [tr(el(f'{i + 1} · {m}'), td(), td(f'<span class="u">{BASE[i]}</span>'), td(), td(), td(), td(DEC), td('', 'left')) for i, m in enumerate(MEAS)]))
COMP = ['Imaging', 'Clinical scores (for example Constant)', 'Participant questionnaires', 'Range of motion and examination', 'Interval safety review', 'Other component of the CIP']
D = (sec('D', 'Components', 'Count a component only at visits where the CIP requires it; write Not required, not zero.') +
     table('dct', [26, 10, 10, 10, 10, 34], ['Component', 'Expected', 'Complete', 'Missing', 'Complete (%)', 'PFVRs with a missing component'],
           [tr(el(c), td(), td(), td(), td(), td('', 'left')) for c in COMP]))
pages.append(f'<main class="page landscape">{top("Follow-up measures and components")}{strip()}<section class="section compact">{C}</section><section class="section compact">{D}</section>{foot("Follow-up measures and components", 2)}</main>')
# ---------- Page 3: E + F
TIM = ['Within the window', 'Early, outside the window', 'Late, up to 7 days outside', 'Late, more than 7 days outside', 'Not obtained after documented efforts']
E = (sec('E', 'Timing', 'Each expected visit counted once.') +
     table('et', [40, 12, 12, 12, 24], ['Timing', 'Count', 'Base', 'Result (%)', 'PFVRs'], [tr(el(t), td(), td(), td(), td('', 'left')) for t in TIM]))
CAUSE = ['Participant availability', 'Scheduling', 'Staffing or absence', 'Imaging', 'Assessment not done correctly', 'Protocol design']
F = (sec('F', 'Main causes', 'One main cause per problem, from the PFVR. Look for concentration: same staff member, week, visit type or component.') +
     table('ft', [24, 8, 14, 22, 16, 16], ['Cause', 'Count', 'Measure affected (#)', 'Attribution', 'PFVRs', 'Concentration seen'],
           [tr(el(c), td(), td(), td(ck('Site', 'Participant', 'Protocol', 'Mixed', cls='opts col2')), td('', 'left'), td('', 'left')) for c in CAUSE]))
pages.append(f'<main class="page">{top("Timing and causes")}{strip()}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Timing and causes", 3)}</main>')
# ---------- Page 4: G + H
G = (sec('G', 'Method check (when needed)', 'Only when C to F point to how an assessment is done. Otherwise write Not needed and why.') +
     table('gt', [24, 26, 26, 24], ['Area checked', 'Why and which PFVRs', 'What was found', 'Linked record'], [tr(td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left')) for _ in range(2)]))
H = (sec('H', 'Actions', 'One row per cause the site must correct, not per missed visit. Set the check that will show the action worked.') +
     table('ht', [8, 26, 16, 12, 9, 29], ['Action', 'What will change (cause in F)', 'Receiving record', 'Owner', 'Due', 'How we will know it worked'], [tr(td(), td('', 'left'), td('', 'left'), td(), td(), td('', 'left')) for _ in range(4)]))
pages.append(f'<main class="page">{top("Method check and actions")}{strip()}<section class="section compact">{G}</section><section class="section compact">{H}</section>{foot("Method check and actions", 4)}</main>')
# ---------- Page 5: I + J
I = (sec('I', 'Did earlier actions work?', 'Done is not the same as effective.') +
     table('it', [12, 34, 30, 24], ['Action', 'Check set when assigned', 'What this period shows', 'Result'], [tr(td(), td('', 'left'), td('', 'left'), td(ck('Worked', 'Did not work', 'Too early', cls='opts col'))) for _ in range(2)]))
J = (sec('J', 'Conclusion') +
     table('jt', [30, 70], None, [tr(el('Follow-up in this period'), td(ck('Under control', 'Under control, watch next period', 'Action required', 'Escalation required', cls='opts left'), 'left')),
                                  tr(el('Basis (measures, causes, records)'), td('', 'left tall')),
                                  tr(el('Sent to (PIR indicator 3, IMC, CAPA, SRR, POT)'), td('', 'left')),
                                  tr(el('Next review'), td('', 'left'))]) +
     '<div class="sig2"><div class="signature"><b>Prepared by</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Earlier actions and conclusion")}{strip()}<section class="section compact">{I}</section><section class="section compact">{J}</section>{foot("Earlier actions and conclusion", 5)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:52px}.meta-cell.span2{grid-column:span 2}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}.opts.col2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:2px 8px}
.purpose td{font-size:9px;padding:4px 8px;vertical-align:top;text-align:left;height:46px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}td .u{display:block;font-size:8px;color:#4d5b6b}
.bt td{height:130px;font-size:8.8px;padding:3px 7px}
.ct td{height:49px;font-size:8.6px;padding:2px 5px}.ct .opts{font-size:7.4px;line-height:1.15}
.dct td{height:32px;font-size:8.6px;padding:2px 6px}
.et td{height:59px;font-size:8.8px;padding:3px 6px}
.ft td{height:68px;font-size:8.8px;padding:3px 6px}.ft .opts{font-size:7.8px}
.gt td{height:135px;font-size:8.8px;padding:3px 6px}
.ht td{height:110px;font-size:8.8px;padding:3px 6px}
.it td{height:110px;font-size:8.8px;padding:3px 6px}.it .opts{font-size:7.8px}
.jt td{height:56px;font-size:8.8px;padding:3px 7px}.jt td.tall{height:215px}.jt .opts{font-size:7.8px}
.sig2 .signature{min-height:140px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
