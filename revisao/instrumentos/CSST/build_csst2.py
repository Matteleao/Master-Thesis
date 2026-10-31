# CSST v2.0 (blank), second iteration: author's v0.1 and v1.0, the Codex analysis, SCML v0.7 categories and the thesis (4.3.3).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>CSST v2.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'csst-').replace('Editor do POT', 'Editor do CSST').replace('POT', 'CSST')
V, NP = 'CSST v2.0', 10
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">CSST - Complication Signal Surveillance Template</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">v2.0</div></header>')
def sec(letter, title, guide=None):
    return f'<div class="section-header"><div class="letter">{letter}</div><div class="section-title">{title}</div></div>' + (f'<div class="guide">{guide}</div>' if guide else '')
def foot(txt, n): return f'<footer class="footer"><div>{V} | {txt}</div><div>Page {n} of {NP}</div></footer>'
def meta(label, inner='<span class="blank-entry"></span>'): return f'<div class="meta-cell"><b>{label}</b>{inner}</div>'
def strip(sheet):
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['Study / site', 'MRL plan ID / revision used', 'Review ID', sheet]) + '</section>'
strip_idx = '<section class="sheet-strip">' + ''.join(meta(c) for c in ['Study / site', 'MRL plan ID', 'Index sheet no. / total', 'Last entry date']) + '</section>'
def table(cls, widths, heads, rows):
    col = ''.join(f'<col style="width:{w}%">' for w in widths)
    th = ''.join(f'<th>{h}</th>' for h in heads) if heads else ''
    return f'<table class="{cls}"><colgroup>{col}</colgroup>' + (f'<thead><tr>{th}</tr></thead>' if heads else '') + '<tbody>' + ''.join(rows) + '</tbody></table>'
def tr(*cells): return '<tr>' + ''.join(cells) + '</tr>'
el = lambda t: f'<td class="el">{t}</td>'
td = lambda t='', c='': f'<td class="{c}">{t}</td>' if c else f'<td>{t}</td>'
pages = []
lbl = lambda t, cs='': f'<td class="lbl"{cs}>{t}</td>'
ul = lambda *xs: '<ul class="pl">' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
grp = lambda t, n: f'<tr class="grp"><td colspan="{n}">{t}</td></tr>'
# ---------- Page 1: header, A, B
hdr = ''.join(meta(c) for c in ['Study / protocol', 'CIP version', 'Site / code', 'CSST review ID / revision', 'Review type', 'Review period / data cut-off',
                                 'Device / procedure reviewed', 'Previous CSST review ID', 'SCML snapshot ID', 'Analysis file (if used)', 'Prepared by / role', 'Controlled location'])
hdr = hdr.replace('<b>Review type</b><span class="blank-entry"></span>', '<b>Review type</b>' + ck('Scheduled', 'Triggered', cls='opts left'))
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The CSST is the site\'s review of its complications taken together. A single event is assessed in the SART and indexed in the SCML; the CSST looks at all of them at once, on the site\'s own schedule and after a trigger, to see whether events that each seemed explicable share a cause: the same component, the same surgeon, the same moment of follow-up or the same kind of case. A concentration of events is a question to test, not a conclusion about a device or a surgeon.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One review of the site\'s complications for one period, or one review opened by a trigger.</td>'
     '<td>Whether the data show no material pattern, a pattern to watch more closely, a signal to send on, or a result limited by the data.</td>'
     '<td>SCML events, ICDL procedures and context, PFVR follow-up reached, SLCT surgeon sequence, SART event status and the previous CSST.</td>'
     '<td>Counts by time point (C)<br>Triggers met (D)<br>Signals assessed (F)<br>Routes to the receiving records (H)</td></tr></tbody></table>')
src_rows = [('SCML snapshot', 'Events and their categories'), ('ICDL procedure records', 'Procedures, components, configuration, context'), ('PFVR / visit schedule', 'Participants who reached each follow-up time point'),
            ('SLCT', 'Surgeon codes and case sequence'), ('SART', 'Event type, seriousness and status'), ('Previous CSST review', 'Signals to follow up in G')]
B = (sec('B', 'Sources and their limitations', 'With limitation means the review goes ahead: name the records that are missing or incomplete. Not available means the counts that need that source cannot be made in this review.') +
     table('bt', [15, 18, 22, 13, 32], ['Source', 'Used for', 'ID · extraction date', 'Status', 'Limitation (records missing or incomplete)'],
           [tr(td(a, 'dl'), td(b, 'left'), td(), td(ck('Complete', 'With limitation', 'Not available', cls='opts col')), td()) for a, b in src_rows]))
pages.append(f'<main class="page">{top("Review identification, purpose and sources")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and sources", 1)}</main>')
# ---------- Page 2: C1
c1 = ['Participants enrolled', 'Investigational procedures performed', 'Surgeons operating', 'Surgeons with a first study case in this period',
      'Procedures within a surgeon\'s first ___ study cases', 'Revision procedures (component exchanged or removed)', 'Explanted components returned', 'Follow-up visits due', 'Follow-up visits done in window', 'Follow-up visits missed']
fu = ['Operated (intraoperative)', 'Reached discharge', 'Reached first postoperative visit', 'Reached 6 weeks', 'Reached 3 months', 'Reached 6 months', 'Reached 12 months', 'Reached 24 months']
C1 = (sec('C1', 'Cases and follow-up reached', 'These numbers are the denominators for C2 and C3. Procedures and surgeons come from the ICDL and the SLCT, enrollment from the PSEAR, follow-up from the PFVR. The time points match the columns of C2. Adapt the time points to the CIP visit schedule.') +
      table('kc1', [40, 15, 15, 15, 15], ['Count', 'This period (n)', 'Previous period (n)', 'Change (%)', 'Cumulative (N)'], [tr(td(x, 'left'), td(), td(), td(), td()) for x in c1] +
            [grp('Participants who reached each time point (N for the columns of C2)', 5)] + [tr(td(t, 'left'), td(), td(), td(), td()) for t in fu] +
            [tr(td('Participants withdrawn or lost to follow-up', 'left'), td(), td(), td(), td())]))
pages.append(f'<main class="page">{top("Cases and follow-up reached")}<section class="section compact">{C1}</section>{foot("Cases and follow-up reached", 2)}</main>')
# ---------- Pages 3-4: C2 by time point (landscape)
TP = ['Intraoperative', 'Before discharge', 'First postop visit', '6 weeks', '3 months', '6 months', '12 months', '24 months']
C2W = [19] + [8.5] * 8 + [6, 7]
C2H = ['Event (SCML category)'] + [f'{t}<span class="u">(n / N) %</span>' for t in TP] + ['Total (n)', 'New this period']
nrow = tr(td('<b>N for this column (from C1)</b>', 'left nrow'), *[td('', 'nrow') for _ in range(10)])
g1 = [('Instability / dislocation', ['Dislocation', 'Subluxation or instability symptoms']),
      ('Fracture', ['Intraoperative fracture', 'Periprosthetic fracture', 'Acromion or scapular spine fracture']),
      ('Infection / wound', ['Superficial wound problem', 'Deep or periprosthetic infection', 'Hematoma']),
      ('Neurologic / vascular', ['Nerve injury (axillary nerve, brachial plexus)', 'Vascular injury']),
      ('Device performance', ['Component loosening', 'Component disassociation (liner, glenosphere)', 'Implant breakage or wear', 'Radiographic change (notching, lucency, migration)'])]
g2 = [('Function and other', ['Stiffness or loss of motion', 'Persistent pain', 'Thromboembolic event', 'Other (SCML code): ______'])]
def c2rows(groups):
    out = [nrow]
    for g, evs in groups:
        out.append(grp(g, 11))
        out += [tr(td(e, 'left ev'), *[td() for _ in range(10)]) for e in evs]
    return out
C2a = (sec('C2', 'Complications by follow-up time point', 'Count each event once, in the time point where it occurred, against the N of that column. Reading across a row shows whether a problem appears early or grows with time.') +
       table('kc2', C2W, C2H, c2rows(g1)))
pages.append(f'<main class="page landscape">{top("Complications by time point · 1 of 2")}<section class="section compact">{C2a}</section>{foot("Complications by follow-up time point", 3)}</main>')
ov = ['Participants with at least one complication', 'Participants with more than one complication', 'Reoperations', 'Revisions (component exchanged or removed)', 'Serious events (SAE / SADE)', 'Device deficiencies (all; counted apart from complications)']
C2b = (sec('C2', 'Complications by follow-up time point (continued)') +
       table('kc2', C2W, C2H, c2rows(g2)) +
       '<div class="exh">Overview</div>' +
       table('ov', [28, 11, 12, 11, 19, 19], ['Measure', 'This period (n)', 'Previous period (n)', 'Change (%)', 'Cumulative<span class="u">(n / N) %</span>', 'Cumulative at previous review<span class="u">(n / N) %</span>'], [tr(td(x, 'left ev'), td(), td(), td(), td(), td()) for x in ov]))
pages.append(f'<main class="page landscape">{top("Complications by time point · 2 of 2")}<section class="section compact">{C2b}</section>{foot("Complications by follow-up time point", 4)}</main>')
# ---------- Page 5: C3 context
mk = ['Unplanned configuration change', 'Component substitution', 'Technical deviation from the surgical technique', 'Intraoperative difficulty (bone quality, deformity, revision case)', 'Senior support or proctoring used',
      'Surgeon within first ___ study cases', 'Operation outside normal hours', 'Instrument or loaner set problem', 'Gap in the operative record', 'Other: ______']
C3 = (sec('C3', 'Procedure context', 'For each marker, compare the complication rate in procedures with it and without it. Context never changes the counts in C2; it helps explain them.') +
      table('kc3', [30, 16, 18, 18, 18], ['Context marker', 'Procedures with it<span class="u">(n / N) %</span>', 'With it: had a complication<span class="u">(n / n) %</span>', 'Without it: had a complication<span class="u">(n / n) %</span>', 'Source'],
            [tr(td(m, 'left ev'), td(), td(), td(), td()) for m in mk]) +
      '<div class="exh">Links between context and complications</div>' +
      table('lk', [24, 22, 26, 28], ['Context marker', 'Procedures (ICDL IDs)', 'Complication found (C2 event · SCML ID)', 'Comment'], [tr(td(), td(), td(), td()) for _ in range(4)]))
pages.append(f'<main class="page">{top("Procedure context")}<section class="section compact">{C3}</section>{foot("Procedure context", 5)}</main>')
# ---------- Page 6: E comparisons
E = (sec('E', 'Comparison by surgeon, component and case type', 'A group stands out when its share of complications is clearly larger than its share of procedures. Use the surgeon codes of the SLCT and the component, lot and configuration recorded in the ICDL.') +
     '<div class="exh">E1 · By surgeon (SLCT code)</div>' +
     table('ex', [16, 16, 18, 16, 18, 16], ['Surgeon', 'Procedures<span class="u">(n) % of all</span>', 'With a complication<span class="u">(n / n) %</span>', 'Share of all complications<span class="u">%</span>', 'In the first ___ cases<span class="u">(n / n) %</span>', 'Note'], [tr(*[td() for _ in range(6)]) for _ in range(5)]) +
     '<div class="exh">E2 · By component, lot or configuration (ICDL)</div>' +
     table('ex', [26, 16, 18, 16, 24], ['Component · lot · configuration', 'Procedures<span class="u">(n) % of all</span>', 'With a complication<span class="u">(n / n) %</span>', 'Share of all complications<span class="u">%</span>', 'Note'], [tr(*[td() for _ in range(5)]) for _ in range(5)]) +
     '<div class="exh">E3 · By case type</div>' +
     table('ex', [26, 16, 18, 16, 24], ['Case type (indication, primary or revision)', 'Procedures<span class="u">(n) % of all</span>', 'With a complication<span class="u">(n / n) %</span>', 'Share of all complications<span class="u">%</span>', 'Note'], [tr(*[td() for _ in range(5)]) for _ in range(5)]))
pages.append(f'<main class="page">{top("Comparison by surgeon, component and case type")}<section class="section compact">{E}</section>{foot("Comparison by surgeon, component and case type", 6)}</main>')
# ---------- Page 7: D triggers (landscape)
tg = [('T1', 'Rate above the agreed limit', 'Any category at any time point (C2).'),
      ('T2', 'Rate rising with time', 'The same category grows from earlier to later time points (C2 row).'),
      ('T3', 'Rise since the previous review', 'Same category and time point, compared with the previous CSST.'),
      ('T4', 'New category', 'A category with no earlier events now has events (C2, New this period).'),
      ('T5', 'Surgeon share', 'A surgeon\'s share of complications exceeds their share of procedures (E1).'),
      ('T6', 'Component or configuration share', 'Same comparison by component, lot or configuration (E2).'),
      ('T7', 'Early learning cases', 'Complication rate in a surgeon\'s first cases above their later cases (E1, C1).'),
      ('T8', 'Context association', 'Rate with a context marker above the rate without it (C3).'),
      ('T9', 'Serious events grouped', 'Serious events in one category within a short window (SART, C2).'),
      ('T10', 'Device deficiencies of one type', 'Repeated deficiencies of the same type or component (C2, SART).')]
D = (sec('D', 'Signal triggers', 'Apply each trigger and write the value found. A trigger met opens a signal in F.') +
     table('dt', [5, 17, 25, 14, 12, 15, 12], ['ID', 'Trigger', 'What is compared · where', 'Agreed limit', 'Source of the limit', 'Value found<span class="u">(n / N) %</span>', 'Met?'],
           [tr(td(i, 'cat'), td(f'<b>{a}</b>', 'left ev'), td(b, 'left small'), td(), td(), td(), td(ck('Yes', 'No', 'Not assessable', cls='opts col'))) for i, a, b in tg]) +
     '<div class="note">These triggers are examples. Before the first inclusion, review them and set each limit with the site\'s clinical team and, where it applies, the sponsor; write the agreed limit and its source (CIP, sponsor guidance, site procedure). A limit changed later applies only to later reviews.</div>')
pages.append(f'<main class="page landscape">{top("Signal triggers")}<section class="section compact">{D}</section>{foot("Signal triggers", 7)}</main>')
# ---------- Page 8: F signals (landscape)
hyp = ck('Device, component or lot', 'Procedure or technique', 'Surgeon or learning curve', 'Case complexity or participant', 'Data or documentation', 'Local process', 'Undetermined', cls='opts col')
disp = ck('No material pattern', 'Closer surveillance', 'Sent on (see H)', 'Inconclusive: data limitation', cls='opts col')
F = (sec('F', 'Assessment of each signal', 'One row per trigger met. Describe the pattern and the explanations still to test; do not conclude the cause. Set how the next review will show whether the response worked.') +
     table('ft', [7, 10, 23, 18, 15, 27], ['Signal ID', 'Trigger (D) · events (SCML IDs)', 'Pattern described', 'Explanations to test', 'Disposition', 'What will show the response worked'],
           [tr(td(), td(), td(), td(hyp), td(disp), td()) for _ in range(4)]))
pages.append(f'<main class="page landscape">{top("Assessment of each signal")}<section class="section compact">{F}</section>{foot("Assessment of each signal", 8)}</main>')
# ---------- Page 9: G follow-up, H routes
G = (sec('G', 'Signals from earlier reviews', 'Check each earlier signal against the criterion set for it in F.') +
     table('gt', [11, 27, 26, 16, 20], ['Signal ID · review', 'Criterion set then', 'Result in this review', 'Outcome', 'Next step'],
           [tr(td(), td(), td(), td(ck('Effective', 'Partly effective', 'Not effective', 'Not assessable', cls='opts col')), td()) for _ in range(4)]))
routes = [('SLCT', 'Could surgeon-dependent variation explain the pattern?'), ('Sponsor device-deficiency route', 'Does the signal point to a device, component, configuration or lot?'),
          ('SART', 'Are the individual events complete and routed through the safety pathway?'), ('SRR', 'Does the signal show a local process weakness to enter as a risk?'),
          ('CAPA log', 'Did a first response fail, or does a process failure recur?'), ('POT', 'Does the PI need to restrict, supervise more, continue or escalate?'), ('PIR / IMC', 'Should the result inform an indicator or an internal check?')]
H = (sec('H', 'Where each signal goes', 'The action is followed in the receiving record; this review records only that it was sent.') +
     table('ht', [14, 36, 10, 22, 18], ['Route', 'Question for this review', 'Signal ID (F)', 'Receiving record · date sent', 'Status'],
           [tr(td(a, 'dl'), td(b, 'left'), td(), td(), td(ck('Sent', 'Not required', 'Pending', cls='opts col'))) for a, b in routes]))
pages.append(f'<main class="page">{top("Earlier signals and routes")}<section class="section compact">{G}</section><section class="section compact">{H}</section>{foot("Earlier signals and routes", 9)}</main>')
# ---------- Page 10: conclusion and sign-off
K = (sec('I', 'Conclusion and sign-off', 'The conclusion reflects the most serious open signal.') +
     table('dtb', [26, 74], None, [
         tr(lbl('Review conclusion'), td(ck('No material pattern', 'Closer surveillance', 'Signal sent on', 'Inconclusive: data limitation', cls='opts left wide'), 'left')),
         tr(lbl('Next review · date and what will be checked again'), td('', 'tall'))]) +
     '<div class="wbox lim"><b>Limitations and rationale</b></div>'
     '<div class="sig2"><div class="signature"><b>Reviewer</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>PI / accountable approver</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Conclusion and sign-off")}<section class="section compact">{K}</section>{foot("Conclusion and sign-off", 10)}</main>')
css = """<style>
.meta-grid .meta-cell{min-height:64px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:3px 0}
.opts.wide{gap:22px;flex-wrap:wrap}
th{text-align:center!important}th .u{display:block;font-weight:400;font-size:7.6px;opacity:.9}
td.cat{text-align:center;font-weight:700;color:#173c67;background:#f3f6f9!important;font-size:9px}
td.dl{text-align:center;font-weight:700;color:#173c67;background:#f3f6f9!important;font-size:8.8px}
td.left{text-align:left}td.small{font-size:8.2px!important;line-height:1.25}td.ev{font-size:8.6px;color:#173c67}
tr.grp td{background:#dbe7f3!important;color:#173c67;font-weight:700;font-size:8.6px;text-align:left;padding:3px 7px;height:auto!important}
td.nrow{background:#f7f9fb!important;font-size:8.4px;color:#173c67}
.pl{margin:2px 0 0 0;padding-left:16px}.pl li{margin:2px 0;font-size:9.6px;line-height:1.35}p.how{margin:6px 0 0}
.bt td{height:70px;font-size:8.6px;padding:3px 6px}.bt .opts{font-size:7.8px}
.kc1 td{height:42px;font-size:8.8px;padding:2px 7px}
.kc2 td{height:28px;font-size:8.2px;padding:1px 4px}.kc2 th{font-size:8px;padding:3px 2px}.ov td{height:56px;font-size:8.6px;padding:2px 6px}
.kc3 td{height:52px;font-size:8.8px;padding:3px 6px}.kc3 th{font-size:8.4px}
.exh+table{margin-top:0!important}.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9px;padding:3px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:8px}
.ex td{height:44px;font-size:8.6px;padding:2px 5px}.ex th{font-size:8.2px}
.dt td{height:46px;font-size:8.6px;padding:2px 5px}.dt .opts{font-size:7.8px}
.note{margin-top:6px;font-size:8.8px;color:#33475b;border:1px solid var(--grid);border-left:4px solid var(--navy);padding:5px 9px;background:#f7f9fb;line-height:1.35}
.ft td{height:131px;font-size:8.6px;padding:2px 5px}.ft .opts{font-size:7.8px;line-height:1.15}
td.lbl{background:#3a78b5!important;color:#fff;font-size:8.4px;text-align:center;font-weight:600;padding:3px 6px}
.gt td{height:74px;font-size:8.6px;padding:2px 5px}.gt .opts{font-size:7.8px}
.ht td{height:58px;font-size:8.6px;padding:3px 6px}.ht .opts{font-size:8px;gap:4px 0}
.dtb{margin-top:6px}.dtb td{height:44px;font-size:8.6px;padding:3px 6px}.dtb td.tall{height:90px}.dtb .opts{font-size:8.4px}
.wbox.lim{min-height:540px;margin-top:8px}
.sig2 .signature{min-height:110px!important}
.letter{font-size:15px!important}
.purpose th{text-align:center}.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:56px;line-height:1.4}.purpose td:first-child{font-weight:400;color:inherit;background:none}
.lk td{height:56px;font-size:8.6px;padding:2px 5px}
</style>
"""
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
