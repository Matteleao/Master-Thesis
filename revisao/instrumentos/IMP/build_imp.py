# IMP v1.0 (blank), built from scratch from the Codex analysis and the thesis (internal verification).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>IMP v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'imp-').replace('Editor do POT', 'Editor do IMP').replace('POT', 'IMP')
V, NP = 'IMP v1.0', 7
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">IMP - Internal Monitoring Plan</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">IMP · v1.0</div></header>')
def sec(letter, title, guide=None):
    return f'<div class="section-header"><div class="letter">{letter}</div><div class="section-title">{title}</div></div>' + (f'<div class="guide">{guide}</div>' if guide else '')
def foot(txt, n): return f'<footer class="footer"><div>{V} | {txt}</div><div>Page {n} of {NP}</div></footer>'
def meta(label, inner='<span class="blank-entry"></span>'): return f'<div class="meta-cell"><b>{label}</b>{inner}</div>'
def strip(extra):
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['Study / site', 'IMP ID', 'Version / effective from', extra]) + '</section>'
def table(cls, widths, heads, rows):
    col = ''.join(f'<col style="width:{w}%">' for w in widths)
    th = ''.join(f'<th>{h}</th>' for h in heads) if heads else ''
    return f'<table class="{cls}"><colgroup>{col}</colgroup>' + (f'<thead><tr>{th}</tr></thead>' if heads else '') + '<tbody>' + ''.join(rows) + '</tbody></table>'
def tr(*cells): return '<tr>' + ''.join(cells) + '</tr>'
el = lambda t: f'<td class="el">{t}</td>'
td = lambda t='', c='': f'<td class="{c}">{t}</td>' if c else f'<td>{t}</td>'
num = lambda i: f'<td class="num">{i}</td>'
CHECKS = [('Sterile release to use', 'Integrity, expiry and storage confirmed before each device is used'),
          ('Implant traceability and component reconciliation', 'Implanted components match labels, lot/UDI, accountability and CRF'),
          ('Instrumentation and operating-room readiness', 'Instruments available, compatible and checked; substitutions recorded'),
          ('Operative documentation', 'Operative note lets a reader rebuild the final configuration and intraoperative decisions'),
          ('Imaging usability and timing', 'Image sets acquired in window, with the required views, and usable'),
          ('Follow-up execution', 'Visits done in window with all endpoint-critical components'),
          ('Endpoint data agreement', 'Endpoint-critical fields agree between source and CRF'),
          ('Timeliness and closure', 'Notes, data entry, queries, safety follow-up and actions closed on time'),
          ('External context', 'Safety notices, field actions and new literature on the device were looked for'),
          ('Complication monitoring', 'Complication reviews took place as planned and their signals were sent on')]
chk = lambda i: f'<td class="el"><b>{CHECKS[i][0]}</b><span class="sub">{CHECKS[i][1]}</span></td>'
pages = []
# ---------- Page 1: header, A, B
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('IMP ID'),
               meta('Version'), meta('Status', ck('Draft', 'Approved', 'Superseded', 'Retired', cls='opts left')), meta('Supersedes (ID / version)'), meta('Effective from'),
               meta('Next scheduled plan review'), meta('Prepared by / role'), meta('Approved by / date'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The IMP is the site\'s plan for checking its own work during the investigation, alongside the sponsor\'s monitoring. It is written and approved before the first participant is included. It does not record any review: each review is run and recorded in the Internal Monitoring Checklist (IMC), which cites the IMP version it followed.</p>'
     '<p>For each of the ten checks the plan fixes, in advance, what is checked (C), when and by whom (D), on which records and how many (E), what counts as done, evidenced and effective (F), what calls a review early (G) and where each kind of result goes (H). Rules are set before results exist. A change applies only from its effective date onward and is entered in J; reviews already done stay with the version they used.</p></div>'
     '<table class="purpose"><colgroup><col style="width:19%"><col style="width:81%"></colgroup><tbody>'
     '<tr><td>Unit of analysis</td><td>One site and one investigation, under one approved version of the plan.</td></tr>'
     '<tr><td>Decision supported</td><td>Whether the site\'s own verification is defined well enough to catch, in time, a failure in a control the site is responsible for: named reviewers, defined samples, named source records, fixed criteria and set routes.</td></tr>'
     '<tr><td>Inputs</td><td>Site risk register (SRR), delegation log and training records, the CIP and its manuals, and the records each check reads: ICDL, IQL, PFVR, FUCR, SART, SCML, CSST, PIR, CRF and source records.</td></tr>'
     '<tr><td>Outputs</td><td>The rules every IMC review follows. Findings are recorded in the IMC; those that need a corrective action go to the CAPA log; plan changes come back here through J.</td></tr></tbody></table>')
brow = lambda a, b='': tr(el(a), td(b, 'left'))
B = (sec('B', 'Plan boundary', 'What the plan covers and what it rests on. The plan covers controls the site is responsible for; it does not replace sponsor monitoring.') +
     table('bt', [32, 68], None, [
         brow('Investigation(s), sites and phases covered'),
         brow('Documents the plan is built on (ID / version)', '<span class="hint">CIP · imaging manual · SRR · delegation log · source document map</span>'),
         brow('Sponsor monitoring: what the sponsor checks and how its findings reach the site'),
         brow('Reviewer independence', ck('The reviewer never checks their own work', 'Small team: a trained peer reviews, with PI oversight (limitation below)', cls='opts col')),
         brow('Known constraints (staff, time, access to records)'),
         brow('Outside this plan')]) +
     '<div class="gate"><b>First review</b> · due after the first <span class="inline-blank"></span> inclusions or procedures, before routine reviews start, to catch workflow failures while few participants are exposed.</div>')
pages.append(f'<main class="page">{top("Plan identification, purpose and boundary")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and boundary", 1)}</main>')
# ---------- Page 2: C checks in scope (landscape)
C = (sec('C', 'Checks in scope', 'Keep all ten unless a check truly does not apply. A check left out needs the reason, who agreed and what would bring it back.') +
     table('lt', [3, 26, 13, 20, 16, 9, 13], ['#', 'Check', 'Included?', 'Control to verify (what must have happened)', 'Source record(s) used', 'Risk link (SRR ID)', 'If not included: reason, agreed by, condition to include'],
           [tr(num(i + 1), chk(i), td(ck('Included', 'Not included', 'Deferred until:', cls='opts col')), td('', 'left'), td('', 'left'), td(), td('', 'left')) for i in range(10)]))
pages.append(f'<main class="page landscape">{top("Checks in scope")}{strip("Plan status")}<section class="section compact">{C}</section>{foot("Checks in scope", 2)}</main>')
# ---------- Page 3: D schedule and reviewer (landscape)
D = (sec('D', 'Schedule and reviewer', 'Choose the timing that fits how fast each failure would spread: by calendar, by number of cases, by event or by study milestone. The reviewer is named by role and must be released for the task in the delegation log.') +
     table('lt', [3, 22, 12, 13, 9, 15, 10, 9, 7], ['#', 'Check', 'Timing basis', 'Routine frequency', 'First review', 'Earlier review for this check when…', 'Reviewer (role)', 'Backup (role)', 'Own work?'],
           [tr(num(i + 1), chk(i), td(ck('Calendar', 'Case count', 'Each event', 'Milestone', cls='opts col2')), td('', 'left'), td(), td('', 'left'), td(), td(), td(ck('No', 'Yes (B)', cls='opts col'))) for i in range(10)]))
pages.append(f'<main class="page landscape">{top("Schedule and reviewer")}{strip("Plan status")}<section class="section compact">{D}</section>{foot("Schedule and reviewer", 3)}</main>')
# ---------- Page 4: E sample (landscape)
E = (sec('E', 'What is reviewed and how much', 'Name the unit (procedure, component, image set, visit, field, event or search) and never mix units in one count. "A sample" is not a rule: say how units are picked. A small population is reviewed in full.') +
     table('lt', [3, 22, 10, 9, 15, 13, 14, 14], ['#', 'Check', 'Unit', 'Expected units per period', 'How units are picked', 'Minimum, and when all are reviewed', 'Sample grows when…', 'Selected record unavailable'],
           [tr(num(i + 1), chk(i), td(), td(), td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left')) for i in range(10)]))
pages.append(f'<main class="page landscape">{top("What is reviewed and how much")}{strip("Plan status")}<section class="section compact">{E}</section>{foot("What is reviewed and how much", 4)}</main>')
# ---------- Page 5: F criteria (landscape)
F = (sec('F', 'Criteria the reviewer applies', 'Write each criterion so two reviewers would reach the same answer. The IMC rates each check on these three questions separately.') +
     table('lt', [3, 22, 19, 19, 19, 18], ['#', 'Check', 'Execution: the control was done when…', 'Evidence: the record is sufficient when…', 'Effective: the control worked when…', 'Records the reviewer cites in the IMC'],
           [tr(num(i + 1), chk(i), td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left')) for i in range(10)]))
pages.append(f'<main class="page landscape">{top("Criteria the reviewer applies")}{strip("Plan status")}<section class="section compact">{F}</section>{foot("Criteria the reviewer applies", 5)}</main>')
# ---------- Page 6: G triggers + H responses
trig = ['Serious adverse event or serious device effect at the site', 'Complication cluster or signal from the CSST', 'Important protocol deviation', 'Repeated endpoint data discrepancy',
        'Pattern of unusable or late images (IQL)', 'Device, instrument or equipment malfunction', 'CIP amendment', 'Departure or change of a key person or of a reviewer',
        'Sponsor finding that needs a local response', 'Corrective action that failed or was reopened', '']
G = (sec('G', 'Triggers for an earlier review', 'Any trigger marked Yes calls a review before the next scheduled one, for the checks listed. A minor observation is not a trigger.') +
     table('gtt', [41, 13, 20, 14, 12], ['Trigger', 'Applies?', 'Checks reviewed early (#)', 'Called by (role)', 'Within (days)'],
           [tr(el(t) if t else td('', 'left'), td(ck('Yes', 'No')), td(), td(), td()) for t in trig]))
resp = [('Complete, adequate and effective', 'No further action. Recorded in the IMC.'),
        ('Observation: isolated, low consequence, corrected at review', 'Corrected and closed in the IMC action log, with owner and date.'),
        ('Partial execution or partial evidence', 'Corrected in the record that owns it (ICDL, IQL, PFVR, SART…); checked again at the next review.'),
        ('Not performed, or evidence missing', 'IMC action log; assess whether it is a deviation to report under the CIP.'),
        ('Not effective', 'CAPA log; SRR updated when a control is weaker than assumed.'),
        ('Not assessable', 'Reason recorded; the check is repeated or the sample enlarged.'),
        ('Recurrent, across units, or with material consequence', 'CAPA log and the PI through the POT; SRR updated.'),
        ('Possible harm to a participant or a reportable event', 'At once to the PI and the SART; the sponsor as the CIP requires. Not held for the review.')]
H = (sec('H', 'Where each result goes', 'The printed minimum applies to every check. Write the owning role and when the result is checked again.') +
     table('ht', [29, 43, 14, 14], ['Result in the IMC', 'Minimum response', 'Owner (role)', 'Checked again'],
           [tr(el(a), td(b, 'left'), td(), td()) for a, b in resp]))
pages.append(f'<main class="page">{top("Earlier reviews and responses")}{strip("Plan status")}<section class="section compact">{G}</section><section class="section compact">{H}</section>{foot("Earlier reviews and responses", 6)}</main>')
# ---------- Page 7: I approval + J change control
irow = lambda a, b: tr(el(a), td(b.replace('class="opts"', 'class="opts left"'), 'left'))
I = (sec('I', 'Ready to start', 'Confirm before the first inclusion. PI approval means the plan can be run with the people and time available.') +
     table('it', [46, 54], None, [
         irow('Every reviewer and backup is released for the task in the delegation log', ck('Yes', 'No: action and date')),
         irow('Staff who do the checked work know the plan', ck('Yes, on (date):', 'No: action and date')),
         irow('The IMC is prepared with this IMP ID and version', ck('Yes', 'No')),
         irow('First review due (date or after inclusion number)', '')]) +
     '<div class="sig2"><div class="signature"><b>Prepared by</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
J = (sec('J', 'Changes to the plan', 'A change applies from its effective date. A result already seen is never the reason to loosen a rule for the same period.') +
     table('jt', [9, 13, 20, 20, 16, 11, 11], ['Change ID', 'Section / check', 'Previous rule', 'New rule', 'Reason (IMC, CAPA, SRR, sponsor…)', 'Effective from', 'Approved by'],
           [tr(td(), td(), td('', 'left'), td('', 'left'), td('', 'left'), td(), td()) for _ in range(8)]))
pages.append(f'<main class="page">{top("Readiness, approval and changes")}{strip("Plan status")}<section class="section compact">{I}</section><section class="section compact">{J}</section>{foot("Readiness, approval and changes", 7)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:42px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.purpose td{font-size:9.2px;padding:3px 7px}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.el .sub{display:block;font-weight:400;color:#4d5b6b;font-size:7.8px;line-height:1.2;margin-top:1px}
td.num{font-weight:700;color:#173c67;font-size:9px}
.hint{color:#8a96a3;font-size:8px}
.bt td{height:56px;font-size:8.8px;padding:3px 6px}
.inline-blank{display:inline-block;width:46px;border-bottom:1px solid #6d7a88;margin:0 3px}
.gate{border:1px solid var(--grid);border-left:4px solid var(--navy);background:#f7f9fb;padding:7px 9px;margin-top:7px;font-size:9.4px;color:#173c67}
.opts.col2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:1px 6px}
.lt td{height:47px;font-size:8.6px;padding:2px 5px}.lt th{font-size:8.4px}.lt .opts{font-size:7.6px;line-height:1.15}
.gtt td{height:31px;font-size:8.8px;padding:2px 6px}
.ht td{height:44px;font-size:8.6px;padding:2px 6px}
.it td{height:34px;font-size:8.8px;padding:3px 6px}
.jt td{height:52px;font-size:8.6px;padding:2px 5px}
.sig2 .signature{min-height:96px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
