# PIR v1.0 (blank): reads source results, computes trends across periods and links between indicators, drives improvement.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>PIR v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'pir-').replace('Editor do POT', 'Editor do PIR').replace('POT', 'PIR')
V, NP = 'PIR v1.0', 6
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">PIR - Performance Indicator Record</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">PIR · v1.0</div></header>')
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
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['PIR ID', 'Site / code', 'Period / data cut-off', 'Rule set (version)']) + '</section>'
IND = [('Enrollment quality', 'PSEAR, SIFSL, deviation record'), ('Protocol deviations', 'Deviation record, ICDL, IMC'), ('Follow-up compliance', 'FUCR, PFVR'),
       ('Safety reporting timeliness', 'SART'), ('Surgeon procedural consistency', 'SLCT, ICDL, CSST'), ('Critical data completeness', 'IMC, query log, operative notes')]
ind = lambda i: (f'<td class="el"><b>{i + 1} · {IND[i][0]}</b></td>' if i < 6 else '<td class="el"></td>')
DEC = ck('Within rule', 'Closer review', 'Action required', 'Not assessable', cls='opts col')
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('PIR ID'),
               meta('Period reviewed / data cut-off'), meta('Previous PIR'), meta('Rule set (version, effective date)'), meta('Review date'),
               meta('Review type', ck('Routine', 'Early cases', 'Triggered', 'Action check', cls='opts left')), meta('Prepared by / role'), meta('Accountable reviewer / role'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The PIR reviews the site\'s performance over one period through six indicators fixed before the first participant, plus any the site adds. It takes the results already reported by the source records (FUCR, SLCT, CSST, IMC, SART and others) and does not recount them. What it adds is the reading across time and across indicators: how each result moves over the last periods (D), and whether problems in different indicators share the same participants, surgeon, staff, time or process step (E). From that it decides what to correct (F), checks whether earlier actions worked (G) and concludes on the period (H).</p>'
     '<p>Every result keeps its count and denominator; a percentage alone hides small numbers. A rule is never changed to fit a result; a new rule applies from its effective date.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One site, one review period, each indicator with its own denominator.</td>'
     '<td>Whether each indicator is within its rule, needs closer review or action, and what the site must improve.</td>'
     '<td>Results of the source records; the previous PIR; the rule set.</td>'
     '<td>Trend and links (D, E); improvement actions with a check (F, G); routes to CAPA, SRR, POT, SLCT or the sponsor.</td></tr></tbody></table>')
B = (sec('B', 'Review boundary', 'Fix the boundary before reading any result.') +
     table('bt', [30, 70], None, [tr(el(x), td('', 'left')) for x in ['Records included (IDs or ranges, cut-off)', 'Records missing, late or excluded, and the effect on denominators', 'Rule or source changes in the period', 'Periods compared and whether they are comparable']]))
pages.append(f'<main class="page">{top("Review identification, purpose and boundary")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and boundary", 1)}</main>')
# ---------- Page 2: C rules (landscape)
C = (sec('C', 'Indicator rules', 'Set before the first participant and approved by the PI. Write each condition so that two reviewers reach the same decision. Rows 7 and 8 are for indicators the site adds.') +
     table('ct', [17, 14, 13, 14, 14, 14, 14], ['Indicator', 'Source records', 'Unit (denominator)', 'Within rule when', 'Closer review when', 'Action required when', 'Rule ID · version'],
           [tr(ind(i), td(IND[i][1] if i < 6 else '', 'src'), td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left'), td()) for i in range(8)]))
pages.append(f'<main class="page landscape">{top("Indicator rules")}{strip()}<section class="section compact">{C}</section>{foot("Indicator rules", 2)}</main>')
# ---------- Page 3: D results across periods (landscape)
D = (sec('D', 'Results across periods', 'Copy each result from its source record as count / denominator (%). Direction compares the last four periods: a change counts when it passes the closer-review margin or lasts two periods in a row; with fewer than three periods write Too few periods.') +
     table('dt', [16, 10, 10, 10, 11, 11, 14, 18], ['Indicator', 'Three periods back', 'Two periods back', 'Last period', 'This period', 'Cumulative', 'Direction', 'Decision (C)'],
           [tr(ind(i), td(), td(), td(), td(), td(), td(ck('Better', 'Stable', 'Worse', 'Too few periods', cls='opts col')), td(DEC)) for i in range(8)]))
pages.append(f'<main class="page landscape">{top("Results across periods")}{strip()}<section class="section compact">{D}</section>{foot("Results across periods", 3)}</main>')
# ---------- Page 4: E links (landscape)
E = (sec('E', 'Links between indicators', 'For every indicator not within its rule, look for the same participants, surgeon, staff member, time point, component or process step in the other indicators and in the source records. Write what was compared and the counts. A shared pattern is a lead to test, not a proof of cause.') +
     table('et', [4, 22, 14, 22, 20, 18], ['#', 'Pattern seen', 'Indicators involved', 'What was compared (records and counts)', 'Likely shared cause', 'Conclusion'],
           [tr(num(i), td('', 'left'), td(), td('', 'left'), td('', 'left'), td(ck('Supported', 'Not supported', 'Open: needs more data', cls='opts col'))) for i in range(1, 5)]))
pages.append(f'<main class="page landscape">{top("Links between indicators")}{strip()}<section class="section compact">{E}</section>{foot("Links between indicators", 4)}</main>')
# ---------- Page 5: F + G
F = (sec('F', 'Improvement actions', 'One action per cause found in D or E. Set the check that will show it worked before starting it. The receiving record owns the action.') +
     table('ft', [7, 26, 15, 12, 9, 31], ['Action', 'What will change (from D or E)', 'Receiving record', 'Owner', 'Due', 'How we will know it worked (indicator, value, period)'],
           [tr(td(), td('', 'left'), td('', 'left'), td(), td(), td('', 'left')) for _ in range(4)]))
G = (sec('G', 'Did earlier actions work?', 'Compare the indicator before and after with the check set in F. Done is not the same as effective.') +
     table('gt', [9, 24, 16, 16, 17, 18], ['Action', 'Check set when assigned', 'Value before', 'Value now', 'Result', 'Next step'],
           [tr(td(), td('', 'left'), td(), td(), td(ck('Worked', 'Did not work', 'Too early', cls='opts col')), td('', 'left')) for _ in range(4)]))
pages.append(f'<main class="page">{top("Improvement actions and their effect")}{strip()}<section class="section compact">{F}</section><section class="section compact">{G}</section>{foot("Improvement actions and their effect", 5)}</main>')
# ---------- Page 6: H conclusion
H = (sec('H', 'Period conclusion', 'The conclusion covers only the stated period, records and indicators; it does not certify the site.') +
     table('hc', [34, 12, 54], ['Decision', 'Count', 'Indicators'], [tr(el(x), td(), td('', 'left')) for x in ['Within rule', 'Closer review', 'Action required', 'Not assessable']]) +
     table('hd', [34, 66], None, [tr(el('Site performance over the periods'), td(ck('Improving', 'Stable', 'Declining', 'Mixed', cls='opts left'), 'left')),
                                  tr(el('What the site learned this period'), td('', 'left tall')),
                                  tr(el('Routes opened (CAPA, SRR, POT, SLCT, sponsor) or none'), td('', 'left')),
                                  tr(el('Next review (date or trigger)'), td('', 'left'))]) +
     '<div class="sig2"><div class="signature"><b>Prepared by</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Period conclusion")}{strip()}<section class="section compact">{H}</section>{foot("Period conclusion", 6)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:52px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:4px 8px;vertical-align:top;text-align:left;height:50px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}td.src{font-size:8.2px;color:#4d5b6b}
td.num{font-weight:700;color:#173c67;font-size:9px}
.bt td{height:112px;font-size:8.8px;padding:3px 7px}
.ct td{height:61px;font-size:8.6px;padding:2px 5px}.ct th{font-size:8.4px}
.dt td{height:59px;font-size:8.6px;padding:2px 5px}.dt .opts{font-size:7.4px;line-height:1.15}
.et td{height:118px;font-size:8.8px;padding:3px 6px}.et .opts{font-size:7.8px}
.ft td{height:93px;font-size:8.8px;padding:3px 6px}
.gt td{height:83px;font-size:8.8px;padding:3px 6px}.gt .opts{font-size:7.8px}
.hc td{height:55px;font-size:8.8px;padding:3px 7px}.hd{margin-top:7px}.hd td{height:70px;font-size:8.8px;padding:3px 7px}.hd td.tall{height:200px}
.sig2 .signature{min-height:150px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
