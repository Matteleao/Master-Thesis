# MRL v1.0 (blank), from the author's v0.7, the Codex analysis (v0.3) and the thesis (4.2.1 review points, 4.6 lifecycle, Figure 4.1).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>MRL v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'mrl-').replace('Editor do POT', 'Editor do MRL').replace('POT', 'MRL')
V, NP = 'MRL v1.0', 6
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
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['Study / site', 'MRL ID', 'Review ID', sheet]) + '</section>'
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
# ---------- Page 1: header, A, B
hdr = ''.join(meta(c) for c in ['Study / protocol', 'CIP version / date', 'Site / code', 'MRL ID / revision', 'Principal Investigator', 'Record owner / role',
                                 'Milestone configuration version (C)', 'Current phase(s)', 'Date opened', 'Last decision / next milestone', 'SRR reference', 'Controlled location'])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The MRL records the PI\'s formal decision at the points where the investigation\'s most consequential risks concentrate: whether a defined unit (the site, a surgeon, a process or a cohort) may take its next step, may take it only under stated conditions, or must wait. Participants move through the phases at different times, so a gate decides a transition for its unit, not a pause for the whole study. The MRL cites the records that hold the evidence; it does not repeat them or close them.</p>'
     '<p class="how"><b>How the form works</b></p>' +
     ul('<b>C</b>, before the first inclusion: choose the milestones this investigation needs and set each one\'s unit, trigger and review window. A calendar date alone is not a trigger.',
        '<b>D and E</b> are one gate review: the evidence and its sufficiency (D), then the PI decision, permitted scope and conditions (E). Reprint the pair for each review.',
        '<b>B</b> lists every gate decision, so the sequence can be read at a glance. <b>F</b> clears each condition; <b>G</b> records changes to the configuration, which apply only from their effective date.',
        '<b>H</b> locates the instrument records the site uses.') + '</div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One gate decision for one milestone and one implementation unit.</td>'
     '<td>Pass, pass with conditions or blocked, and the scope permitted from now on.</td>'
     '<td>Milestone configuration (C) and the records that hold the evidence: SRR, IMP and IMC, POT, ICDL, SLCT, PFVR, FUCR, IQL, SART, CSST, PIR and CAPA log.</td>'
     '<td>Permitted scope (E)<br>Conditions to their owning records<br>Next milestone or re-review trigger<br>Risk updates to the SRR</td></tr></tbody></table>')
B = (sec('B', 'Gate decision index', 'One line per gate decision, including re-reviews. The detail stays in D and E under the same Review ID.') +
     table('bx', [10, 9, 12, 11, 10, 15, 18, 15], ['Review ID', 'Milestone', 'Unit', 'Trigger met (date)', 'Decision date', 'Decision', 'Scope now permitted', 'Next milestone or re-review trigger'],
           [tr(td(), td(), td(), td(), td(), td(ck('Pass', 'With conditions', 'Blocked', cls='opts col')), td(), td()) for _ in range(6)]))
pages.append(f'<main class="page">{top("Purpose and gate decision index")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Purpose and gate decision index", 1)}</main>')
# ---------- Page 2: C configuration (landscape)
ms = [('M0', 'Feasibility', 'Site capability accepted', 'Operating, imaging and rehabilitation capacity; imaging gap assessment; long-term follow-up logistics. Feasibility record, SIRR.'),
      ('M1', 'Start-up', 'Release to enroll', 'Authorization; delegation with criticality codes; surgeons released and device training documented; assessors certified and reliability tested; instruments calibrated; imaging charter agreed; SRR open; IMP approved. RACI, CCDM, DTRM, TRE, SCR, SIRR, SRR, IMP.'),
      ('M2', 'First enrollments', 'Inclusion decisions hold up', 'Consent, eligibility evidence, dual review where imaging decides, PI resolution of borderline cases, screening log. PSEAR, SIFSL.'),
      ('M3', 'Procedural implementation', 'Surgeon or process may continue its scope', 'Release current for each case, implant traceability, critical steps and substitutions documented, due learning-curve review. SCR, TRE, ICDL, SLCT.'),
      ('M4', 'Immediate postoperative period', 'Pathway works for the cohort', 'Immediate review of complications and device performance; postoperative images usable. ICDL, IQL, SART, SCML.'),
      ('M5', 'Approach to endpoint assessment', 'Endpoint data will be usable', 'Visits in window, PROMs on schedule and completion reviewed monthly, images usable, endpoint data agreement. PFVR, FUCR, IQL, IMC, PIR.'),
      ('M6', 'Close-out', 'Site may close out', 'Device reconciliation signed; data completeness per participant, gaps justified; final safety report; archive. Accountability, IMC, PIR, SART.'),
      ('M7', 'Continuous improvement', 'Lifecycle may close', 'Corrective actions closed and effective in their records; lessons turned into standing procedures. CAPA log, PIDLR.')]
C = (sec('C', 'Milestone configuration', 'Options, not a fixed sequence. Use a milestone only when its decision changes what the site may do next, and set it before the evidence exists. Changes go in G and apply prospectively.') +
     table('ct', [4, 17, 32, 6, 10, 20, 11], ['ID', 'Milestone · decision it enables', 'What to verify · typical records', 'Use?', 'Unit', 'Trigger and denominator', 'Review window'],
           [tr(td(i, 'cat'), td(f'<b>{a}</b><span class="sub">{b}</span>', 'left ms'), td(c, 'left small'), td(ck('Yes', 'No', cls='opts col')), td(ck('Site', 'Surgeon', 'Process', 'Cohort', cls='opts g2')), td(), td()) for i, a, b, c in ms] +
           [tr(td('', 'cat'), td('', 'left ms'), td('', 'left small'), td(ck('Yes', 'No', cls='opts col')), td(ck('Site', 'Surgeon', 'Process', 'Cohort', cls='opts g2')), td(), td())]) +
     '<div class="note">The transversal safety stream is not a milestone: required SART records, due follow-up and the monthly trend review are checked in every gate review (D).</div>')
pages.append(f'<main class="page landscape">{top("Milestone configuration")}<section class="section compact">{C}</section>{foot("Milestone configuration", 2)}</main>')
# ---------- Page 3: D evidence and sufficiency
ident = table('itb', [22, 28, 22, 28], None, [
    tr(lbl('Milestone (C)'), td(), lbl('Implementation unit'), td()),
    tr(lbl('Trigger met · date'), td(), lbl('Denominator · evidence cut-off'), td()),
    tr(lbl('Prepared by / role'), td(), lbl('Previous review (if re-review)'), td())])
D = (sec('D', 'Gate review · evidence and sufficiency', 'Cite each record so it can be found again: instrument, record ID, version or date, case or period covered, location. The evidence supports the decision; it does not replace the originating record.') + ident +
     table('evt', [22, 30, 12, 13, 23], ['Evidence for this gate', 'Source · record ID · date · location', 'Coverage', 'Status', 'What it shows for this gate'],
           [tr(td(), td(), td(), td(ck('Complete', 'Limited', 'Missing', cls='opts col')), td()) for _ in range(6)]) +
     table('sft', [34, 30, 36], ['For this milestone and unit…', 'Answer', 'Basis or limitation'], [tr(lbl(q), td(ck('Yes', 'With limitation', 'No', cls='opts row3')), td()) for q in [
         'Trigger and scope: was the milestone reached for the right unit and denominator?',
         'Controls and evidence: did the controls exist, were they used, can the records be reconstructed?',
         'Safety stream: are required safety records, due follow-up and the trend review current?',
         'Sufficiency: does the evidence allow the next step with no material unknown impact?']]))
pages.append(f'<main class="page">{top("Gate review · evidence and sufficiency")}{strip("Sheet no. / total")}<section class="section compact">{D}</section>{foot("Gate review · evidence and sufficiency", 3)}</main>')
# ---------- Page 4: E decision
E = (sec('E', 'Gate review · PI decision', 'Pass means the evidence is sufficient for this gate, not that results are good. Blocked applies to the stated scope, not necessarily to the whole study.') +
     table('dtb', [22, 78], None, [
         tr(lbl('Decision'), td(ck('Pass', 'Pass with conditions', 'Blocked', cls='opts left wide'), 'left')),
         tr(lbl('Scope permitted from now on'), td('', 'tall')),
         tr(lbl('Scope still not permitted'), td('', 'tall')),
         tr(lbl('PI rationale'), td('', 'tall2'))]) +
     '<div class="exh">Conditions</div>' +
     table('cnd', [9, 25, 11, 14, 17, 15, 9], ['Condition ID', 'Condition or restriction', 'Owner', 'Destination record', 'Evidence that clears it', 'Re-review trigger', 'Latest date'],
           [tr(td(), td(), td(), td(), td(), td(), td()) for _ in range(5)]) +
     table('dtb', [22, 28, 22, 28], None, [
         tr(lbl('Next milestone'), td(ck('Open', 'Pending', 'Blocked', cls='opts left')), lbl('Linked POT / SRR / CAPA'), td()),
         tr(lbl('Principal Investigator · name'), td(), lbl('Signature / date'), td())]))
pages.append(f'<main class="page">{top("Gate review · PI decision")}{strip("Sheet no. / total")}<section class="section compact">{E}</section>{foot("Gate review · PI decision", 4)}</main>')
# ---------- Page 5: F clearance, G configuration changes
F = (sec('F', 'Condition clearance and re-review', 'For an action owned by another record, cite its verification; verify here only what the MRL itself required. A condition not cleared keeps its owner and gets a new trigger.') +
     table('clr', [9, 9, 30, 15, 25, 12], ['Condition ID', 'Review ID', 'Verification date · evidence reviewed', 'Result', 'Decision / next step', 'PI initials · date'],
           [tr(td(), td(), td(), td(ck('Cleared', 'Partly cleared', 'Not cleared', 'Not assessable', cls='opts col')), td(), td()) for _ in range(6)]))
G = (sec('G', 'Changes to the milestone configuration', 'A change applies from its effective date; decisions already taken stay with the configuration they used.') +
     table('chg', [9, 9, 22, 22, 18, 10, 10], ['Change ID', 'Milestone', 'Previous setting', 'New setting', 'Reason', 'Effective from', 'Approved by'],
           [tr(td(), td(), td(), td(), td(), td(), td()) for _ in range(4)]))
pages.append(f'<main class="page">{top("Condition clearance and configuration changes")}<section class="section compact">{F}</section><section class="section compact">{G}</section>{foot("Condition clearance and configuration changes", 5)}</main>')
# ---------- Page 6: H instrument records
ins = ['CCDM · Criticality-Coded Delegation Matrix', 'DTRM · Device and Study Training Requirements Matrix', 'TRE · Training Record Evaluation and Release', 'RACI · Responsibility Assignment Matrix', 'SCR · Surgical Credentialing Record', 'POT · PI Oversight Template',
       'SRR · Site Risk Register', 'SLCT · Surgeon Learning Curve Tracking Log', 'SCML · Site Complication Monitoring Log', 'SART · Safety Assessment, Reporting and Tracking', 'CSST · Complication Signal Surveillance Template', 'IMP · Internal Monitoring Plan',
       'IMC · Internal Monitoring Checklist', 'SIRR · Site Imaging Readiness Record', 'IQL · Imaging Quality Log', 'PSEAR · Participant Screening and Eligibility Assessment Record', 'SIFSL · Subject Identification and Failure Screening Log', 'PFVR · Participant Follow-up Visit Record',
       'ICDL · Intraoperative Checklist and Device Log', 'PIR · Performance Indicator Record', 'FUCR · Follow-up Compliance Review', 'CAPA · Corrective and Preventive Action Log', 'PIDLR · Post-Investigation Debrief and Lessons Record']
H = (sec('H', 'Instrument records in use', 'Where each record lives, when it was activated and in which phases it is used. N/A or combined with another record needs a short reason.') +
     table('ht', [34, 14, 18, 20, 14], ['Instrument', 'Activated (date · phase)', 'Phases in use', 'Record ID · location', 'Status'],
           [tr(td(x, 'left ins'), td(), td(), td(), td()) for x in ins]))
pages.append(f'<main class="page">{top("Instrument records in use")}<section class="section compact">{H}</section>{foot("Instrument records in use", 6)}</main>')
css = """<style>
.meta-grid .meta-cell{min-height:56px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:3px 0}
.opts.g2{display:grid;grid-template-columns:auto auto;justify-content:start;gap:5px 8px}
.opts.row3{display:flex;gap:4px 12px;flex-wrap:wrap;justify-content:center}.opts.wide{gap:28px}
th{text-align:center!important}
td.cat{text-align:center;font-weight:700;color:#173c67;background:#f3f6f9!important;font-size:9px}
td.left{text-align:left}td.ms b{display:block;font-size:8.8px;color:#173c67}.sub{display:block;font-size:8px;color:#5f6670;margin-top:2px}td.small{font-size:8px!important;line-height:1.25}
.purpose th{text-align:center}.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:50px;line-height:1.4}.purpose td:first-child{font-weight:400;color:inherit;background:none}
.pl{margin:2px 0 0 0;padding-left:16px}.pl li{margin:2px 0;font-size:9.6px;line-height:1.35}p.how{margin:6px 0 0}
.bx td{height:54px;font-size:8.6px;padding:2px 5px}.bx th{font-size:8.4px}.bx .opts{font-size:7.8px}
.ct td{height:57px;font-size:8.6px;padding:3px 5px}.ct th{font-size:8.4px}.ct .opts{font-size:7.8px}
.note{margin-top:6px;font-size:8.8px;color:#33475b;border-left:3px solid var(--navy);padding:4px 8px;background:#f7f9fb;line-height:1.3}
td.lbl{background:#3a78b5!important;color:#fff;font-size:8.4px;text-align:center;font-weight:600;padding:3px 6px}
.itb{margin-top:6px}.itb td{height:34px;font-size:8.4px;padding:3px 6px}
.evt{margin-top:6px}.evt td{height:68px;font-size:8.6px;padding:2px 5px}.evt .opts{font-size:7.8px}
.sft{margin-top:6px}.sft td{height:64px;font-size:8.4px;padding:3px 6px}.sft td.lbl{text-align:left}.sft .opts{font-size:8px}
.dtb{margin-top:6px}.dtb td{height:38px;font-size:8.6px;padding:3px 6px}.dtb td.tall{height:90px}.dtb td.tall2{height:130px}.dtb .opts{font-size:8.4px}
.exh+table{margin-top:0!important}.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9px;padding:3px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:8px}
.cnd td{height:70px;font-size:8.6px;padding:2px 5px}.cnd th{font-size:8.4px}
.clr td{height:80px;font-size:8.6px;padding:2px 5px}.clr .opts{font-size:7.8px}
.chg td{height:60px;font-size:8.6px;padding:2px 5px}
.ht td{height:36px;font-size:8.6px;padding:2px 6px}td.ins{font-size:8.4px}
.letter{font-size:15px!important}
</style>
"""
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
