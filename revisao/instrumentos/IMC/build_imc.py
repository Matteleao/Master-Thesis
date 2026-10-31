# IMC v1.5 (blank) from v1.4, the Codex analysis and the IMP v1.0 (twelve checks).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>IMC v1.5 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'imc-').replace('Editor do POT', 'Editor do IMC').replace('POT', 'IMC')
V, NP = 'IMC v1.5', 7
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">IMC - Internal Monitoring Checklist</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">IMC · v1.5</div></header>')
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
grp = lambda t, n: f'<tr class="grp"><td colspan="{n}">{t}</td></tr>'
# name, question (E), execution means, evidence may include, effective when, primary records (D)
CHECKS = [
 ('Participant entry: consent and eligibility', 'Was consent signed on the current version before any study procedure, and eligibility confirmed by the PI before surgery?',
  'Consent and eligibility of the participants included in the period were checked.', 'Signed consent forms, version log, eligibility checklist, PSEAR.', 'No procedure before consent; eligibility signed before surgery; any gap reported as a deviation.', 'PSEAR / consent forms'),
 ('Delegation and training', 'Was everyone who did a study task delegated and trained for it on that date?',
  'Study tasks done in the period were matched to the delegation log and training records.', 'Delegation log, training records, task records (ICDL, PFVR).', 'No task done before delegation and training; gaps closed and routed.', 'Delegation log / training file'),
 ('Sterile release to use', 'Were package integrity, expiry, storage and any breach or replacement reviewed and reconciled?',
  'Release, package, expiry and storage checks for the period were reviewed.', 'ICDL, release record, storage and expiry record, substitution record.', 'Release status and any breach or substitution reconciled and routed.', 'ICDL / storage records'),
 ('Implant traceability and component reconciliation', 'Did implanted components match labels, lot or UDI, accountability and CRF, with discrepancies routed?',
  'Planned configuration, implanted components and accountability were compared.', 'ICDL, implant labels, accountability log, operative note, CRF.', 'Lot, UDI and configuration agree, or each discrepancy is explained and routed.', 'ICDL / accountability / CRF'),
 ('Instrumentation and operating-room readiness', 'Were instruments available, compatible and checked, and every substitution or malfunction recorded?',
  'Readiness, compatibility and malfunction records were reviewed.', 'ICDL, room readiness record, deficiency record.', 'Missing, incompatible or faulty equipment recorded and dealt with.', 'ICDL / deficiency route'),
 ('Operative documentation', 'Does each operative note let a reader rebuild the final configuration and intraoperative decisions?',
  'Operative notes were read for configuration, decisions, substitutions and complications.', 'Operative note, ICDL, SART reference, CRF query.', 'Notes complete enough to read safety and outcome later.', 'Operative note / ICDL'),
 ('Imaging usability and timing', 'Were image sets taken in window, with the required views, and usable, with a disposition for any that were not?',
  'Imaging timing, views and usability were reviewed.', 'IQL, imaging source, PFVR, repeat record.', 'Each unusable or late set has a disposition, repeat or limitation.', 'IQL / PFVR'),
 ('Follow-up execution', 'Were visits done in window with all endpoint-critical components, and attendance not taken as completeness?',
  'Follow-up outputs were reviewed for timing and components.', 'PFVR, FUCR, source and CRF.', 'Missing components have a cause and a recovery route.', 'PFVR / FUCR'),
 ('Endpoint data agreement', 'Did the sampled endpoint-critical fields agree between source and CRF, with discrepancies corrected and explained?',
  'A sample of endpoint-critical fields was compared with the source.', 'Source record, CRF entry, comparison sheet, query log.', 'Sampled fields agree, or each discrepancy is corrected and explained.', 'Source / CRF / query log'),
 ('Timeliness and closure', 'Were notes, data entry, queries, safety follow-up and actions closed on time, or escalated?',
  'Items due in the period were checked against their deadlines.', 'Query log, action log, CAPA log, time stamps.', 'Backlog visible, owned and inside the agreed limit.', 'Query / action / CAPA logs'),
 ('External context', 'Were safety notices, field actions and new literature on the device looked for and read against local findings?',
  'The planned search of external information was done.', 'Search record, field notice, sponsor letter, PI note.', 'Relevant information read against local data and sent on when needed.', 'External review record'),
 ('Complication monitoring', 'Did complication reviews take place as planned, and were their signals sent on?',
  'Planned CSST reviews and their routing were checked.', 'SCML, CSST, SART.', 'Reviews on schedule; each signal has a route; no event left unindexed.', 'SCML / CSST / SART'),
]
N = len(CHECKS)
chk = lambda i, q=False: (f'<td class="el"><b>{CHECKS[i][0]}</b>' + (f'<span class="sub">{CHECKS[i][1]}</span>' if q else '') + '</td>') if i < N else '<td class="el"></td>'
pages = []
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('IMC ID'),
               meta('IMP ID / version applied'), meta('Review type', ck('Scheduled', 'Focused', 'Triggered', cls='opts left')), meta('Review period / data cut-off'), meta('Date of review'),
               meta('Trigger or reason (if not scheduled)', cls=' span2'), meta('Reviewer / role'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The IMC records one internal review of the site\'s own controls, run as the Internal Monitoring Plan (IMP) sets out. For each check in scope the reviewer rates three things separately: whether the control was done (execution), whether the records show it (evidence) and whether it worked (effectiveness). The IMC cites the IMP version it followed; it does not change the plan\'s rules after seeing the results.</p>'
     '<p>It refers to records by ID and does not copy their content. It does not judge a single participant, image or event, which stay in their own records, and it does not replace sponsor monitoring, safety reporting or CAPA.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One site, one review period or trigger, and the checks in scope.</td>'
     '<td>Whether each control was done, evidenced and effective, and what must be corrected, sent on or verified next.</td>'
     '<td>IMP, records named for each check, previous IMC and open actions.</td>'
     '<td>Findings and actions (G), routes to the PI Oversight Template (POT), SRR, CAPA and PIR, and the effectiveness check (I).</td></tr></tbody></table>')
# ---------- Page 2: B classification guide
cl = [('Execution', [('Complete', 'All planned activity for the period was done, even if it found a problem.', 'Rate evidence and effectiveness.'),
                     ('Partial', 'Part of the planned activity was done, or a smaller sample than the IMP without approval.', 'Record what is missing; action with owner and date.'),
                     ('Not performed', 'The activity was due and not done, or cannot be confirmed.', 'Action with owner and date; consider escalation.'),
                     ('Not applicable', 'The check does not apply to this phase or scope.', 'Reason in D.')]),
      ('Evidence', [('Adequate', 'Records confirm what was done and what was found.', 'None.'),
                    ('Partial', 'Records confirm only part of it, or are scattered or late.', 'Name the missing record; evidence action.'),
                    ('Insufficient', 'Records missing, contradictory or not retrievable.', 'Action; effectiveness is not assessable.'),
                    ('Not applicable', 'Only when execution is also not applicable.', 'Reason in D.')]),
      ('Effectiveness', [('Effective', 'The control works and no relevant signal is open.', 'None.'),
                         ('Observation', 'Minor, isolated point with no sign of control failure.', 'Record; action only if follow-up is needed.'),
                         ('Not effective', 'Recurrence, material gap, failed response or open signal.', 'Finding, action, owner, date and route.'),
                         ('Not assessable', 'Cannot be judged from the records available.', 'State the limitation; action to complete it.')])]
rows = []
for dim, items in cl:
    rows.append(grp(dim, 3)); rows += [tr(el(a), td(b, 'left'), td(c, 'left')) for a, b, c in items]
B = (sec('B', 'Classification guide', 'Rate the three dimensions separately for each check in E. A negative or uncertain rating always needs a finding, limitation or action.') +
     table('bg', [20, 50, 30], ['Rating', 'Use when', 'Minimum response'], rows))
combo = [('Complete · Adequate · Effective', 'The control works and can be shown.', 'Record the result.'),
         ('Complete · Adequate · Not effective', 'The control was done and recorded but did not prevent or catch the problem.', 'Finding and action; consider CAPA or SRR.'),
         ('Complete · Insufficient · Not assessable', 'Said to be done, but the records cannot show it.', 'Evidence action; re-rate at the next review.'),
         ('Not performed · Adequate', 'Only when records show that the activity did not happen. A record of absence never shows execution.', 'Action with owner and date.')]
B2 = (sec('B', 'Classification guide (continued): combinations that change the response') +
      table('bc', [30, 42, 28], ['Execution · Evidence · Effectiveness', 'Meaning', 'Minimum response'], [tr(el(a), td(b, 'left'), td(c, 'left')) for a, b, c in combo]))
pages.append(f'<main class="page">{top("Review identification, purpose and classification guide")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section>'
             f'<section class="section compact">{B}</section>{foot("Identification, purpose and classification guide", 1)}</main>')
# ---------- Page 3: C check guide
C = (sec('C', 'What each check looks for', 'A general guide. The site-specific criteria are in IMP section E and prevail over this table.') +
     table('cg', [4, 21, 25, 25, 25], ['#', 'Check', 'Execution means', 'Evidence may include', 'Effective when'],
           [tr(num(i + 1), chk(i), td(CHECKS[i][2], 'left'), td(CHECKS[i][3], 'left'), td(CHECKS[i][4], 'left')) for i in range(N)]))
pages.append(f'<main class="page">{top("Rating combinations and what each check looks for")}<section class="section compact">{B2}</section><section class="section compact">{C}</section>{foot("Rating combinations and check guide", 2)}</main>')
# ---------- Page 4: D scope and sample
D = (sec('D', 'Checks in this review and what was reviewed', 'Scope and sample follow the IMP; a different rule is also entered in IMP section I, never applied silently. Write how many units were reviewed out of how many, and the records and range used. A check left out needs the reason and who approved it.') +
     table('dt', [4, 22, 11, 15, 25, 23], ['#', 'Check', 'In scope?', 'Sample reviewed<span class="u">(n of N)</span>', 'Records, ID range and cut-off', 'If not in scope or sample changed: reason, approved by'],
           [tr(num(i + 1), chk(i), td(ck('Yes', 'No')), td(), td('', 'left'), td('', 'left')) for i in range(N + 2)]) +
     '<div class="addnote">Rows 13 and 14 are for checks the site added in the IMP. Use the same row number in E.</div>')
pages.append(f'<main class="page">{top("Scope and sample")}<section class="section compact">{D}</section>{foot("Scope and sample", 3)}</main>')
# ---------- Pages 5-6: E review (landscape)
EX = ck('Complete', 'Partial', 'Not performed', 'Not applicable', cls='opts col')
EV = ck('Adequate', 'Partial', 'Insufficient', 'Not applicable', cls='opts col')
EF = ck('Effective', 'Observation', 'Not effective', 'Not assessable', cls='opts col')
for k, rg in enumerate([range(0, 7), range(7, N + 2)]):
    body = (sec('E', 'Review of each check' + (' (continued)' if k else ''), None if k else 'One row per check in scope. Leave rows out of scope blank. Cite record IDs; do not copy their content.') +
            table('et' + (' p2' if k else ''), [3, 25, 10, 10, 10, 21, 21], ['#', 'Check and question', 'Execution', 'Evidence', 'Effectiveness', 'Finding, signal or limitation (record IDs)', 'Action ID · route · owner · due date'],
                  [tr(num(i + 1), chk(i, True), td(EX), td(EV), td(EF), td('', 'left'), td('', 'left')) for i in rg]))
    pages.append(f'<main class="page landscape">{top("Review of each check · " + ("checks 1–7" if not k else "checks 8–12 and added checks"))}<section class="section compact">{body}</section>{foot("Review of each check", 4 + k)}</main>')
# ---------- Page 7: F signals + G actions
sig = ['Same problem in more than one check', 'Participant safety concern', 'Endpoint or data reliability concern', 'Device traceability or deficiency concern', 'Need for closer PI oversight', 'Need for CAPA or a change in the SRR']
F = (sec('F', 'Signals across checks', 'Use only for a problem that does not fit in one row of E. Route: POT, SRR, CAPA, CSST, PIR, sponsor or safety route, or Not required with the reason.') +
     table('ft', [24, 9, 25, 18, 24], ['Signal', 'Seen?', 'What was seen · checks (#)', 'Immediate containment', 'Route · record ID · owner'],
           [tr(el(s), td(ck('Yes', 'No', cls='opts col')), td('', 'left'), td('', 'left'), td('', 'left')) for s in sig]))
G = (sec('G', 'Action log', 'Every action has an owner and a due date. CAPA content stays in the CAPA log; write its ID here.') +
     table('gt', [8, 9, 27, 13, 12, 10, 12, 9], ['Action ID', 'From (# / F)', 'Action', 'Type', 'Owner (role)', 'Due date', 'Linked record', 'Status'],
           [tr(td(), td(), td('', 'left'), td(ck('Containment', 'Corrective', 'Preventive', 'Verification', cls='opts col')), td(), td(), td(), td(ck('Open', 'Closed', 'Transferred', cls='opts col'))) for _ in range(6)]))
pages.append(f'<main class="page">{top("Signals and actions")}<section class="section compact">{F}</section><section class="section compact">{G}</section>{foot("Signals and actions", 6)}</main>')
# ---------- Page 8: H, I, J, K
H = (sec('H', 'Review outcome', 'The outcome comes only from the checks in scope.') +
     table('ht', [30, 70], None, [
         tr(el('Overall outcome'), td(ck('Controls effective', 'Observations only', 'Action required', 'Escalation required', cls='opts left'), 'left')),
         tr(el('Checks needing follow-up (#)'), td('', 'left')),
         tr(el('Summary of findings'), td('', 'left tall')),
         tr(el('PI review required?'), td(ck('Yes, POT ID:', 'No, reason:', cls='opts left'), 'left')),
         tr(el('Next IMC due'), td('', 'left'))]))
I = (sec('I', 'Effectiveness check of actions', 'An action is closed only when later evidence shows it worked, not when it is done.') +
     table('it', [12, 13, 33, 26, 16], ['Action ID', 'Check date', 'Evidence reviewed (record ID)', 'Result', 'Reviewer'],
           [tr(td(), td(), td('', 'left'), td(ck('Effective', 'Partly effective', 'Not effective', 'Not assessable', cls='opts col2')), td()) for _ in range(3)]))
J = (sec('J', 'Reviewer certification') +
     '<div class="box cert"><p>I confirm that this review covered the stated scope and period, that the records cited were reviewed in proportion to the checks in scope, and that every negative or uncertain rating has a finding, limitation, action or route.</p>'
     f'<p>{ck("I did not do the work I reviewed.", "Exception recorded in POT:", cls="opts left")}</p></div>'
     '<div class="sig2"><div class="signature"><b>Reviewer</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator (if required)</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>'
     '<div class="addnote">File this checklist with the records it cites. A focused or triggered review does not replace the next scheduled IMC unless H changes its date.</div>')
pages.append(f'<main class="page">{top("Outcome and certification")}<section class="section compact">{H}</section><section class="section compact">{I}</section><section class="section compact">{J}</section>{foot("Outcome and certification", 7)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:58px}.meta-cell.span2{grid-column:span 2}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.opts.col2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:2px 8px}
.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:56px;line-height:1.4}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.el .sub{display:block;font-weight:400;color:#4d5b6b;font-size:7.9px;line-height:1.25;margin-top:2px}
td.num{font-weight:700;color:#173c67;font-size:9px}
tr.grp td{background:#dce7f3!important;color:#173c67;font-weight:700;text-align:left;font-size:9px;padding:3px 7px;height:auto!important}
.exh{margin:9px 0 4px;font-weight:700;color:#173c67;font-size:9.6px}
.addnote{margin-top:6px;font-size:8.6px;color:#4d5b6b;border-left:3px solid var(--navy);padding:3px 8px;background:#f7f9fb}
.gate{border:1px solid var(--grid);border-left:4px solid var(--navy);background:#f7f9fb;padding:7px 9px;margin-top:10px;font-size:9.4px;color:#173c67}
.bg td{height:33px;font-size:9px;padding:2px 7px}.bc td{height:40px;font-size:9.2px;padding:3px 7px}
.cg td{height:52px;font-size:8.8px;padding:3px 6px}
.dt td{height:58px;font-size:8.8px;padding:3px 6px}.dt .u{display:block;font-weight:400;font-size:7.6px}
.et td{height:75px;font-size:8.6px;padding:2px 5px}.et.p2 td{height:80px}.et .opts{font-size:7.6px;line-height:1.2}
.ft td{height:58px;font-size:8.8px;padding:3px 6px}
.gt td{height:66px;font-size:8.6px;padding:2px 5px}.gt .opts{font-size:7.6px}
.ht td{height:44px;font-size:8.8px;padding:3px 7px}.ht td.tall{height:130px}
.it td{height:64px;font-size:8.8px;padding:3px 6px}.it .opts{font-size:7.8px}
.box.cert p{margin:4px 0;font-size:9.2px}
.sig2 .signature{min-height:100px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
