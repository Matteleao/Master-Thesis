# CSST v2.0 (blank), rebuilt from the Codex analysis, the thesis guide and the SCML v0.7 categories.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>CSST v2.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'csst-').replace('Editor do POT', 'Editor do CSST').replace('POT', 'CSST')
V, NP = 'CSST v2.0', 5
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">CSST - Complication Signal Surveillance Template</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">CSST · v2.0</div></header>')
def sec(letter, title, guide=None):
    return f'<div class="section-header"><div class="letter">{letter}</div><div class="section-title">{title}</div></div>' + (f'<div class="guide">{guide}</div>' if guide else '')
def foot(txt, n): return f'<footer class="footer"><div>{V} | {txt}</div><div>Page {n} of {NP}</div></footer>'
def meta(label, inner='<span class="blank-entry"></span>'): return f'<div class="meta-cell"><b>{label}</b>{inner}</div>'
def strip(extra):
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['Study / site', 'CSST review ID / revision', 'Review period / data cut-off', extra]) + '</section>'
def table(cls, widths, heads, rows):
    col = ''.join(f'<col style="width:{w}%">' for w in widths)
    th = ''.join(f'<th>{h}</th>' for h in heads) if heads else ''
    return f'<table class="{cls}"><colgroup>{col}</colgroup>' + (f'<thead><tr>{th}</tr></thead>' if heads else '') + '<tbody>' + ''.join(rows) + '</tbody></table>'
def tr(*cells): return '<tr>' + ''.join(cells) + '</tr>'
el = lambda t: f'<td class="el">{t}</td>'
td = lambda t='', c='': f'<td class="{c}">{t}</td>' if c else f'<td>{t}</td>'
pages = []
# ---------- Page 1: header, A, B
hdr = ''.join([meta('Study / protocol'), meta('Current CIP / version'), meta('Site / code'), meta('CSST review ID / revision'),
               meta('Review type', ck('Scheduled', 'Triggered: ________', cls='opts left')), meta('Review period / data cut-off'), meta('Device / procedure population reviewed'), meta('Ruleset ID / version / effective date'),
               meta('SCML snapshot ID(s)'), meta('Analysis file or report (if used)'), meta('Prepared by / role'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The CSST is the site\'s periodic or triggered review of its complications taken together. It reads the reconciled events of the SCML against the right population at risk, applies the tests fixed in the ruleset, looks for clusters by component, surgeon, timing or case context, and decides whether a pattern needs a response and where that response goes.</p>'
     '<p>The tests, thresholds, denominators and counting rule come from the ruleset approved at start-up. A rule changed after a review applies only to later periods. A concentration of events is a hypothesis to test: the CSST does not decide causality, the competence of a surgeon or the quality of a device.</p></div>'
     '<table class="purpose"><colgroup><col style="width:19%"><col style="width:81%"></colgroup><tbody>'
     '<tr><td>Unit of analysis</td><td>One review of one device or procedure population for one period, or one review opened by a trigger set in the ruleset.</td></tr>'
     '<tr><td>Decision supported</td><td>Whether the data show no material pattern, a pattern to watch more closely, a signal to send to another record, or a result that cannot be read because of a data limitation.</td></tr>'
     '<tr><td>Inputs</td><td>SCML snapshot (events); procedure counts from the ICDL or the procedure log (denominators); follow-up maturity from the visit schedule; SLCT context for any surgeon stratum.</td></tr>'
     '<tr><td>Outputs</td><td>Counts with their denominators, test results, the disposition of each signal and its transfer to the SLCT, the sponsor device-deficiency route, the SRR, the CAPA or the POT.</td></tr></tbody></table>')
B = (sec('B', 'Data used and readiness', 'Name each source with its ID and extraction date. Individual cases stay in the SCML and the SART; refer to them by ID.') +
     table('bt', [30, 26, 22, 22], ['Source', 'ID / extraction date', 'Status', 'Limitation'],
           [tr(el(a), td(), td(ck('Complete', 'With limitation', 'Not available', cls='opts col')), td('', 'left')) for a in
            ['SCML snapshot: event population', 'Procedure count (ICDL or procedure log): denominators', 'Follow-up schedule: which procedures reached each follow-up window', 'SLCT: sequence, complexity and support (only for surgeon strata)', 'Other controlled source']]) +
     '<div class="gate"><b>Gate 1 · Can the dataset be reviewed?</b>' + ck('Yes', 'Yes, with the limitation above', 'No: reconcile first (owner and date under Limitations, Section G)', cls='opts left') + '</div>')
pages.append(f'<main class="page">{top("Review identification, purpose and data")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and data", 1)}</main>')
# ---------- Page 2: C counts
C1 = table('ct', [8, 44, 16, 16, 16], ['ID', 'Population at risk (denominator)', 'This period (N)', 'Cumulative (N)', 'Source'],
           [tr(td(i), el(t), td(), td(), td()) for i, t in [('N1', 'Investigational procedures performed'), ('N2', 'Procedures that reached the early follow-up window set in the ruleset'), ('N3', 'Procedures with enough follow-up for late outcomes'), ('N4', 'Procedures exposed to the device for device deficiencies (as the ruleset defines)'), ('N5', '')]])
cats = ['Instability / dislocation', 'Fracture', 'Infection / wound', 'Neurologic / vascular', 'Device performance', 'Other (SCML code): ______']
C2 = table('ct', [26, 14, 15, 15, 15, 15], ['Event category (SCML)', 'Denominator ID', 'This period n / N', 'Previous period n / N', 'Cumulative n / N', 'SCML event IDs'],
           [tr(el(c), td(), td(), td(), td(), td()) for c in cats] + [tr(el('<b>All complications (distinct events)</b>'), td(), td(), td(), td(), td()), tr(el('Device deficiencies (own row; not added to complications)'), td(), td(), td(), td(), td())])
C3 = table('ct', [34, 22, 22, 22], ['Procedure-context marker', 'n / N (N1)', 'Source (ICDL, SLCT)', 'Note'],
           [tr(el(m), td(), td(), td()) for m in ['Unplanned configuration change (SCML category)', 'Component substitution', 'Technical deviation', 'Senior support or proctoring used', 'Documentation gap']])
C = (sec('C', 'Counts against the population at risk', 'Write every count as n / N with the denominator ID. Give a percentage only when the ruleset allows it for that denominator. An event with both an adverse-event and a device-deficiency pathway counts once among the complications.') +
     '<div class="subhead">C1 · Populations at risk</div>' + C1 + '<div class="subhead">C2 · Complications and device deficiencies</div>' + C2 +
     '<div class="subhead">C3 · Procedure-context markers: read with the counts, never added to them</div>' + C3)
pages.append(f'<main class="page">{top("Counts and denominators")}{strip("Ruleset ID / version")}<section class="section compact">{C}</section>{foot("Counts against the population at risk", 2)}</main>')
# ---------- Page 3: D tests (landscape)
tests = ['Rate above the threshold set in the ruleset (by category)', 'Sharp rise since the previous period', 'New event category', 'Concentration in one surgeon', 'Concentration in one component, configuration or lot', 'Serious event or cluster that opened this review', '', '']
D = (sec('D', 'Tests from the ruleset', 'Gate 2. Apply only the tests the ruleset contains, with its thresholds. Write the result as n / N and mark whether the trigger was met.') +
     table('dt', [5, 25, 10, 12, 13, 15, 20], ['Rule ID', 'Test', 'Denominator ID', 'Result (n / N)', 'Threshold in the ruleset', 'Trigger met?', 'Limitation / reference'],
           [tr(td(), el(t) if t else td('', 'left'), td(), td(), td(), td(ck('Yes', 'No', 'Not assessable', cls='opts col')), td('', 'left')) for t in tests]))
pages.append(f'<main class="page landscape">{top("Tests from the ruleset")}{strip("SCML snapshot ID")}<section class="section compact">{D}</section>{foot("Tests from the ruleset", 3)}</main>')
# ---------- Page 4: E strata + F signal assessment (landscape)
basis = ck('Same device / procedure population', 'Comparable follow-up maturity', 'Surgeon sequence reviewed (SLCT)', 'Case complexity / indication reviewed', 'Comparison limited (reason in reading)', cls='opts col')
E = (sec('E', 'Strata and clusters', 'Read each stratum against its own denominator and say what the comparison could and could not take into account. No statistical adjustment is implied unless an approved method is cited.') +
     table('et', [13, 10, 8, 8, 10, 25, 26], ['Stratum type', 'Stratum (code)', 'Events (n)', 'At risk (N)', 'Previous period n / N', 'Comparison basis', 'Reading'],
           [tr(td(ck('Surgeon', 'Component / lot', 'Timing', 'Indication / complexity', cls='opts col')), td(), td(), td(), td(), td(basis), td('', 'left')) for _ in range(3)]))
hyp = ck('Device / component / lot', 'Procedure / technique', 'Operator / learning curve', 'Case complexity / participant', 'Data or documentation limitation', 'Local process weakness', 'Undetermined', cls='opts col')
F = (sec('F', 'Assessment of each signal', 'For each trigger met, describe the pattern and the explanations still to be tested. A pattern in one surgeon goes to the SLCT for review; it is not a finding about that surgeon.') +
     table('ft', [9, 17, 26, 26, 22], ['Signal (rule ID)', 'SCML event IDs / snapshot', 'Pattern described', 'Explanations to test', 'Disposition'],
           [tr(td(), td(), td('', 'left'), td(hyp), td(ck('No material pattern', 'Closer surveillance', 'Sent on (Section G)', 'Inconclusive: data limitation', cls='opts col'))) for _ in range(2)]))
pages.append(f'<main class="page landscape">{top("Strata, clusters and signal assessment")}{strip("SCML snapshot ID")}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Strata, clusters and signal assessment", 4)}</main>')
# ---------- Page 5: G routes + conclusion + sign-off
routes = [('SLCT', 'A pattern calls for reviewing a surgeon\'s sequence, support or proctoring'), ('Sponsor device-deficiency route', 'The signal centers on a device, component, configuration, lot or deficiency'),
          ('SRR', 'A weakness in a local process or control should enter the risk register'), ('CAPA', 'A first response failed, or a process failure recurs'),
          ('POT', 'The PI must decide on restriction, closer supervision, continuation or escalation'), ('PIR', 'The result informs the surgeon procedural consistency indicator'), ('IMC', 'A control in internal monitoring should be checked')]
G = (sec('G', 'Gate 3 · Decision and transfer', 'Record where each signal goes and the receiving record\'s ID. The action is followed in that record; this review records only whether surveillance continues.') +
     table('gt', [20, 46, 18, 16], ['Route', 'Use when the assessment concludes that…', 'Recipient ID / date', 'Status'],
           [tr(el(a), td(b, 'left'), td(), td(ck('Sent', 'Not required', 'Pending'))) for a, b in routes]) +
     '<div class="close-row"><div class="meta-cell"><b>Review conclusion</b><span class="gap"></span>' + ck('No material pattern', 'Closer surveillance', 'Signal sent on', 'Inconclusive: data limitation', cls='opts left') + '</div>'
     '<div class="meta-cell"><b>Next review or reassessment: date and what will be checked again</b><span class="blank-entry"></span></div></div>'
     '<div class="wbox small2"><b>Limitations and rationale</b></div>'
     '<div class="sig2"><div class="signature"><b>Reviewer</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>PI / accountable approver</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Decision, transfer and sign-off")}{strip("Review conclusion date")}<section class="section compact">{G}</section>{foot("Decision, transfer and sign-off", 5)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:42px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.purpose td{font-size:9.2px;padding:3px 7px}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
.bt td{height:44px;font-size:8.8px;padding:3px 6px}
.gate{border:1px solid var(--grid);border-left:4px solid var(--navy);background:#f7f9fb;padding:6px 9px;margin-top:7px;font-size:9.4px;color:#173c67}.gate .opts{margin-top:4px;font-size:8.6px}
.ct td{height:30px;font-size:8.8px;padding:3px 6px}.ct th{font-size:8.6px}
.dt td{height:52px;font-size:8.8px;padding:3px 6px}
.et td{height:72px;font-size:8.4px;padding:2px 5px}.et .opts{font-size:7.4px;line-height:1.15}
.ft td{height:92px;font-size:8.4px;padding:2px 5px}.ft .opts{font-size:7.4px;line-height:1.15}
.gt td{height:40px;font-size:8.8px;padding:3px 6px}
.close-row{display:grid;grid-template-columns:1fr 1fr;border-left:1px solid var(--grid);border-top:1px solid var(--grid);margin-top:7px}.close-row .meta-cell{min-height:58px}
.gap{display:block;height:7px}.wbox.small2{min-height:190px}
.sig2 .signature{min-height:120px!important}.subhead{margin-top:6px}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
