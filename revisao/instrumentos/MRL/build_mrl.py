# MRL v1.0 (blank), from the author's v0.7, the Codex analysis (v0.3) and the thesis (4.2.1 review points, 4.6 lifecycle, Figure 4.1).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>MRL v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'mrl-').replace('Editor do POT', 'Editor do MRL').replace('POT', 'MRL')
V, NP = 'MRL v1.0', 8
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">MRL - Milestone Review Log</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">v1.0</div></header>')
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
P1, P2 = 'Part 1 · Milestone plan', 'Part 2 · Gate review record'
# ---------- Page 1: header, A, B
hdr = ''.join(meta(c) for c in ['Study / protocol', 'CIP version / date', 'Site / code', 'MRL plan ID', 'Plan revision', 'Effective date', 'Principal Investigator', 'Date opened',
                                 'Linked SRR ID / revision', 'Linked POT plan ID', 'Plan prepared by / role', 'Controlled location of plan and reviews'])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>A <b>milestone</b> is a point in the investigation where a failure, if it goes unnoticed, repeats in every case that follows: the first procedures, the immediate postoperative period, the approach to endpoint assessment, close-out. At each milestone the PI takes a <b>gate decision</b>: the unit concerned (the site, a surgeon, a process or a cohort) may take its next step, may take it only within stated limits, or must wait. Participants move through the phases at different times, so a gate decides a step for its unit, not a pause for the whole study.</p>'
     '<p>The MRL has two parts. Part 1 is the plan: which milestones this investigation uses, what triggers each one and what must be shown at it, approved by the PI before the first participant, with an index of every gate decision taken. Part 2 records one gate review, in a new copy each time. The MRL cites the records that hold the evidence; it does not repeat them, and its decisions do not close them.</p></div>'
     '<table class="parts"><colgroup><col style="width:16%"><col style="width:42%"><col style="width:42%"></colgroup>'
     '<thead><tr><th class="blank"></th><th>Part 1 · Milestone plan</th><th>Part 2 · Gate review record</th></tr></thead><tbody>'
     '<tr><td class="rl">Sections</td><td>A to F</td><td>I to V</td></tr>'
     '<tr><td class="rl">Completed</td><td>Once, before the first participant. Changes go in D and apply only from their effective date.</td><td>At each gate review, in a new copy. V only when a condition or block needs clearing.</td></tr>'
     '<tr><td class="rl">By</td><td>Record owner; approved by the PI.</td><td>Evidence reviewer prepares I to III; the PI decides in IV.</td></tr>'
     '<tr><td class="rl">Reads</td><td>CIP, SRR and the POT plan.</td><td>The records cited as evidence: ICDL, SLCT, PFVR, FUCR, IQL, IMC, SART, CSST, PIR, CAPA log and others.</td></tr></tbody></table>')
dec = [('Pass', 'The trigger was reached for the right unit and denominator, the evidence supports the next step and known limitations do not prevent it.', 'The scope now permitted. Pass does not mean clinical results are good.'),
       ('Pass with conditions', 'The evidence supports the next step only within an explicit limit.', 'Permitted and prohibited scope; for each condition its owner, destination record, clearing evidence, re-review trigger and what happens if it is not met.'),
       ('Blocked', 'The trigger, an essential control, an authorization or decision-critical evidence is missing, insufficient or materially uncertain.', 'Exactly what cannot proceed and the evidence needed to re-review. A block need not stop the whole study.')]
B = (sec('B', 'Decision standard') +
     table('bst', [18, 41, 41], ['Gate decision', 'Use when', 'The decision must state'], [tr(td(a, 'dl'), td(b, 'left'), td(c, 'left')) for a, b, c in dec]))
pages.append(f'<main class="page">{top(P1 + " · Purpose and decision standard")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Part 1 · Purpose and decision standard", 1)}</main>')
# ---------- Page 2: C milestones (landscape)
ms = [('M0', 'Feasibility', 'Site capability accepted', 'Operating, imaging and rehabilitation capacity; imaging gap assessment; long-term follow-up logistics. Feasibility record, SIRR.'),
      ('M1', 'Start-up', 'Release to enroll', 'Delegation with criticality codes; surgeons released and device training documented; assessors certified; instruments calibrated; imaging charter agreed; SRR open; IMP approved. RACI, CCDM, DTRM, TRE, SCR, SIRR, SRR, IMP.'),
      ('M2', 'First enrollments', 'Continue or expand enrollment', 'Consent, eligibility evidence, dual review where imaging decides, PI resolution of borderline cases, screening log. PSEAR, SIFSL.'),
      ('M3', 'Procedural implementation', 'Next procedural scope', 'Release current for each case, implant traceability, critical steps and substitutions documented, due learning-curve review. SCR, TRE, ICDL, SLCT.'),
      ('M4', 'Immediate postoperative period', 'Pathway continues for the cohort', 'Immediate review of complications and device performance; postoperative images usable. ICDL, IQL, SART, SCML.'),
      ('M5', 'Approach to endpoint assessment', 'Endpoint assessment proceeds', 'Visits in window, PROMs on schedule, images usable, endpoint data agreement. PFVR, FUCR, IQL, IMC, PIR.'),
      ('M6', 'Close-out', 'Controlled close-out', 'Device reconciliation signed; data completeness per participant; final safety report; archive. Accountability, IMC, PIR, SART.'),
      ('M7', 'Continuous improvement', 'Lifecycle closure', 'Corrective actions closed and effective in their records; lessons in standing procedures. CAPA log, PIDLR.')]
C = (sec('C', 'Milestones used in this investigation', 'Options, not a fixed sequence: use a milestone only when its decision changes what the site may do next, and set it before the evidence exists. A calendar date alone is not a trigger.') +
     table('ct', [4, 15, 27, 5, 10, 15, 9, 15], ['ID', 'Milestone · decision it enables', 'What to verify · typical records', 'Use?', 'Unit', 'Trigger and denominator', 'Review window', 'Permitted next step'],
           [tr(td(i, 'cat'), td(f'<b>{a}</b><span class="sub">{b}</span>', 'left ms'), td(c, 'left small'), td(ck('Yes', 'No', cls='opts col')), td(ck('Site', 'Surgeon', 'Process', 'Cohort', cls='opts g2')), td(), td(), td()) for i, a, b, c in ms] +
           [tr(td('M_', 'cat'), td('', 'left ms'), td('', 'left small'), td(ck('Yes', 'No', cls='opts col')), td(ck('Site', 'Surgeon', 'Process', 'Cohort', cls='opts g2')), td(), td(), td())]) +
     '<div class="note">M0 does not replace sponsor site selection or institutional approval. M1 is executable readiness, not completed forms. M3 does not certify a completed learning curve (SLCT). M5 is readiness of the assessment process, not final results. M6 leaves open cases and CAPAs in their own records. The safety stream is not a milestone: it is checked in every gate review (Part 2, III).</div>')
pages.append(f'<main class="page landscape">{top(P1 + " · Milestones")}<section class="section compact">{C}</section>{foot("Part 1 · Milestones used in this investigation", 2)}</main>')
# ---------- Page 3: D changes, E approval
D = (sec('D', 'Changes to the plan', 'A change applies from its effective date; decisions already taken stay with the plan revision they used.') +
     table('chg', [9, 9, 22, 22, 18, 10, 10], ['Change ID', 'Milestone', 'Previous setting', 'New setting', 'Reason', 'Effective from', 'Approved by'],
           [tr(td(), td(), td(), td(), td(), td(), td()) for _ in range(8)]))
E = (sec('E', 'Plan approval', 'The PI approves the plan before the first participant and at each revision.') +
     table('dtb', [22, 28, 22, 28], None, [tr(lbl('Plan revision approved'), td(), lbl('Approval date'), td())]) +
     '<div class="sig2"><div class="signature"><b>Plan prepared by</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top(P1 + " · Changes and approval")}<section class="section compact">{D}</section><section class="section compact">{E}</section>{foot("Part 1 · Changes and approval", 3)}</main>')
# ---------- Page 4: F index
F = (sec('F', 'Gate decision index', 'One line per signed gate decision, including re-reviews, so the sequence can be read at a glance. The detail stays in the Part 2 copy with the same Review ID.') +
     table('bx', [10, 9, 13, 11, 10, 14, 17, 16], ['Review ID', 'Milestone', 'Unit', 'Trigger met (date)', 'Decision date', 'Decision', 'Scope now permitted', 'Next milestone or re-review trigger'],
           [tr(td(), td(), td(), td(), td(), td(ck('Pass', 'With conditions', 'Blocked', cls='opts col')), td(), td()) for _ in range(13)]))
pages.append(f'<main class="page">{top(P1 + " · Gate decision index")}{strip_idx}<section class="section compact">{F}</section>{foot("Part 1 · Gate decision index", 4)}</main>')
# ---------- Page 5: I identification, II evidence
I = (sec('I', 'Gate identification') +
     table('itb', [22, 28, 22, 28], None, [
         tr(lbl('Milestone (Part 1, C)'), td(), lbl('Implementation unit'), td()),
         tr(lbl('Trigger met · date'), td(), lbl('Count reached · denominator'), td()),
         tr(lbl('Evidence period · cut-off'), td(), lbl('Next step requested'), td()),
         tr(lbl('Previous decision (re-review)'), td(), lbl('Prepared by · date'), td())]))
II = (sec('II', 'Evidence package', 'Cite each record so it can be found again: instrument, record ID, version or date, case or period covered, location. Adequate describes the item; it does not decide the gate.') +
      table('evt', [6, 20, 28, 12, 13, 21], ['Item', 'Control or element', 'Source · record ID · date · location', 'Coverage', 'Status', 'What it shows for this gate'],
            [tr(td(f'E-{n:02d}', 'cat'), td(), td(), td(), td(ck('Adequate', 'Partial', 'Unavailable', 'N/A', cls='opts col')), td()) for n in range(1, 7)]))
pages.append(f'<main class="page">{top(P2 + " · Identification and evidence")}{strip("Sheet no. / total")}<section class="section compact">{I}</section><section class="section compact">{II}</section>{foot("Part 2 · Identification and evidence", 5)}</main>')
# ---------- Page 6: III sufficiency
groups = [('1 · Trigger and scope', [('S-01', 'The configured trigger was reached for the right unit and the actual denominator.'), ('S-02', 'The population, evidence period and requested next step match the plan.')]),
          ('2 · Controls and evidence', [('S-03', 'The critical controls for this gate were in place and their use is evidenced.'), ('S-04', 'Release, authorization, qualification and supervision are current in their records.'), ('S-05', 'Source records and internal verification are retrievable and enough to reconstruct what was done.'), ('S-06', 'Required safety records, due follow-up and the latest trend review are current.')]),
          ('3 · Sufficiency', [('S-07', 'The evidence supports the next step with no material unknown impact from a critical gap.'), ('S-08', 'Open issues have an accountable route and their limits fit the proposed scope.')])]
III = sec('III', 'Sufficiency for this gate', 'For this milestone and unit only: judge whether the evidence in II is enough for the decision. Do not repeat the review done by the IMC or the specialist record.')
for g, qs in groups:
    III += '<div class="exh">' + g + '</div>' + table('sft', [7, 45, 17, 12, 19], ['ID', 'Question', 'Result', 'Evidence item', 'Note'], [tr(td(i, 'cat'), td(q, 'left'), td(ck('Complete', 'Partial', 'Not shown', 'N/A', cls='opts g2')), td(), td()) for i, q in qs])
III += '<div class="wbox gap"><b>Decision-limiting gap or unknown impact</b> (if none, say so and cite the basis)</div>'
pages.append(f'<main class="page">{top(P2 + " · Sufficiency")}{strip("Sheet no. / total")}<section class="section compact">{III}</section>{foot("Part 2 · Sufficiency for this gate", 6)}</main>')
# ---------- Page 7: IV decision
IV = (sec('IV', 'PI gate decision', 'Choose one decision and state what the team may now do. The decision does not close safety, risk, CAPA or authorization records.') +
      table('dtb', [24, 76], None, [
          tr(lbl('Gate decision'), td(ck('Pass', 'Pass with conditions', 'Blocked', cls='opts left wide'), 'left')),
          tr(lbl('Scope permitted from now on'), td('', 'tall')),
          tr(lbl('Scope still not permitted'), td('', 'tall')),
          tr(lbl('PI rationale (cite II and III items)'), td('', 'tall2')),
          tr(lbl('Next milestone'), td(ck('Open', 'Pending', 'Blocked', cls='opts left wide') + '<span class="lab2">Objective trigger:</span>', 'left'))]) +
      '<div class="exh">Conditions</div>' +
      table('cnd', [8, 24, 16, 18, 18, 16], ['Condition ID', 'Restriction', 'Destination record · owner', 'Evidence that clears it', 'Re-review trigger · latest date', 'If not met'],
            [tr(td(), td(), td(), td(), td(), td()) for _ in range(3)]) +
      '<div class="sig2"><div class="signature"><b>Principal Investigator · decision</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
      '<div class="signature"><b>Evidence reviewer</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top(P2 + " · PI decision")}{strip("Sheet no. / total")}<section class="section compact">{IV}</section>{foot("Part 2 · PI gate decision", 7)}</main>')
# ---------- Page 8: V clearance
V_ = (sec('V', 'Condition clearance and re-review', 'Only for a condition or block. Cite the evidence actually reviewed. Clearing an MRL condition does not close its destination record; if the permitted scope changes, sign a new Part 2 decision.') +
      table('clr', [9, 12, 30, 15, 22, 12], ['Condition ID', 'Destination record', 'Evidence reviewed · period', 'Result', 'PI conclusion / new Review ID', 'PI initials · date'],
            [tr(td(), td(), td(), td(ck('Cleared', 'Partly cleared', 'Not cleared', cls='opts col')), td(), td()) for _ in range(8)]))
pages.append(f'<main class="page">{top(P2 + " · Condition clearance")}{strip("Sheet no. / total")}<section class="section compact">{V_}</section>{foot("Part 2 · Condition clearance and re-review", 8)}</main>')
css = """<style>
.meta-grid .meta-cell{min-height:60px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:3px 0}
.opts.g2{display:grid;grid-template-columns:auto auto;justify-content:start;gap:5px 8px}.opts.wide{gap:28px}
th{text-align:center!important}
td.cat{text-align:center;font-weight:700;color:#173c67;background:#f3f6f9!important;font-size:9px}
td.dl{text-align:center;font-weight:700;color:#173c67;background:#f3f6f9!important;font-size:9.2px}
td.left{text-align:left}td.ms b{display:block;font-size:8.8px;color:#173c67}.sub{display:block;font-size:8px;color:#5f6670;margin-top:2px}td.small{font-size:8px!important;line-height:1.25}
.parts{margin-top:6px}.parts th.blank{background:#1f4173}.parts td{font-size:9px;padding:4px 7px;text-align:left;height:32px}.parts td.rl{font-weight:700;color:#173c67;background:#f3f6f9!important}
.bst td{height:72px;font-size:9px;padding:4px 7px;line-height:1.3}
.ct td{height:57px;font-size:8.6px;padding:3px 5px}.ct th{font-size:8.4px}.ct .opts{font-size:7.8px}
.note{margin-top:6px;font-size:8.6px;color:#33475b;border-left:3px solid var(--navy);padding:4px 8px;background:#f7f9fb;line-height:1.3}
td.lbl{background:#3a78b5!important;color:#fff;font-size:8.4px;text-align:center;font-weight:600;padding:3px 6px}
.chg td{height:70px;font-size:8.6px;padding:2px 5px}
.dtb{margin-top:6px}.dtb td{height:40px;font-size:8.6px;padding:3px 6px}.dtb td.tall{height:95px}.dtb td.tall2{height:130px}.dtb .opts{font-size:8.4px}
.lab2{display:block;font-size:8px;color:#5f6670;margin-top:5px}
.bx td{height:62px;font-size:8.6px;padding:2px 5px}.bx th{font-size:8.4px}.bx .opts{font-size:7.8px}
.itb td{height:44px;font-size:8.4px;padding:3px 6px}
.evt td{height:96px;font-size:8.6px;padding:2px 5px}.evt .opts{font-size:7.8px}
.exh+table{margin-top:0!important}.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9px;padding:3px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:7px}
.sft td{height:64px;font-size:8.6px;padding:3px 6px}.sft .opts{font-size:7.8px}
.wbox.gap{min-height:170px;margin-top:8px}
.cnd td{height:76px;font-size:8.6px;padding:2px 5px}.cnd th{font-size:8.4px}
.clr td{height:98px;font-size:8.6px;padding:2px 5px}.clr .opts{font-size:7.8px}
.sig2 .signature{min-height:96px!important}
.letter{font-size:15px!important}
</style>
"""
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
