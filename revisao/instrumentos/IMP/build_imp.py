# IMP v1.0 (blank), built from scratch from the Codex analysis and the thesis (internal verification).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>IMP v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'imp-').replace('Editor do POT', 'Editor do IMP').replace('POT', 'IMP')
V, NP = 'IMP v1.0', 9
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
          ('Complication monitoring', 'Complication reviews took place as planned and their signals were sent on'),
          ('Participant entry: consent and eligibility', 'Consent signed on the current version before any study procedure; eligibility confirmed by the PI before surgery'),
          ('Delegation and training', 'Everyone who did a study task was delegated and released for it on that date')]
chk = lambda i: f'<td class="el"><b>{CHECKS[i][0]}</b><span class="sub">{CHECKS[i][1]}</span></td>' if i < len(CHECKS) else '<td class="el"></td>'
PARTS = [(range(0, 7), 'checks 1–7'), (range(7, 14), 'checks 8–12 and added checks')]
ADDNOTE = '<div class="addnote">Rows 13 and 14 are for a check the site adds because a risk in the SRR is not covered by checks 1–12. Use the same row number in C, D and E.</div>'
def matrix(letter, title, guide, widths, heads, cells, sub, n0):
    for k, (rg, part) in enumerate(PARTS):
        body = sec(letter, title + (' (continued)' if k else ''), guide if not k else None) + table('lt', widths, heads, [tr(num(i + 1), chk(i), *cells()) for i in rg]) + (ADDNOTE if k else '')
        pages.append(f'<main class="page landscape">{top(sub + " · " + part)}<section class="section compact">{body}</section>{foot(sub, n0 + k)}</main>')
pages = []
# ---------- Page 1: header, A, B
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('IMP ID'),
               meta('Version'), meta('Status', ck('Draft', 'Approved', cls='opts left')), meta('Supersedes (ID / version)'), meta('Effective from'),
               meta('Next scheduled plan review'), meta('Plan owner / role'), meta('Approved by / date'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The IMP is the site\'s plan for checking its own work during the investigation, alongside the sponsor\'s monitoring. It is written and approved before the first participant is included. It does not record any review: each review is run and recorded in the Internal Monitoring Checklist (IMC), which cites the IMP version it followed.</p>'
     '<p>For each of the twelve checks, and any check the site adds, the plan fixes in advance what is checked (C), when, by whom, on which records and how many (D), and what counts as done, evidenced and effective (E). It also sets what calls a review early (F) and where each kind of result goes (G). Rules are set before results exist. A change applies only from its effective date onward and is entered in I; reviews already done stay with the version they used.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One site and one investigation, under one approved version of the plan.</td>'
     '<td>Whether the site\'s own verification is defined well enough to catch, in time, a failure in a control the site is responsible for.</td>'
     '<td>Site risk register (SRR), delegation log and training records, the CIP and its manuals, and the records each check reads.</td>'
     '<td>The rules every IMC review follows. Findings go to the IMC, corrective actions to the CAPA log, plan changes back to I.</td></tr></tbody></table>')
brow = lambda a, b='': tr(el(a), td(b, 'left'))
B = (sec('B', 'Plan boundary', 'What the plan covers and what it rests on. The plan covers controls the site is responsible for; it does not replace sponsor monitoring.') +
     table('bt', [32, 68], None, [
         brow('Investigation(s), sites and phases covered'),
         brow('Documents the plan is built on (ID / version)'),
         brow('Sponsor monitoring: what the sponsor checks and how its findings reach the site'),
         brow('Known constraints (staff, time, access to records)'),
         brow('If a record picked for review is unavailable (rule for every check)'),
         brow('Outside this plan')]) +
     '<div class="gate"><b>First review</b> · due after the first <span class="inline-blank"></span> inclusions or procedures, before routine reviews start, to catch workflow failures while few participants are exposed.</div>')
pages.append(f'<main class="page">{top("Plan identification, purpose and boundary")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and boundary", 1)}</main>')
# ---------- Pages 2-7: C, D, E (landscape, two pages each)
matrix('C', 'Checks in scope', 'Keep every check unless it truly does not apply. A check left out needs the reason, who agreed and what would bring it back. List the SRR risks whose controls each check verifies; an SRR control with no check here is a gap to raise.',
       [3, 20, 9, 20, 11, 17, 20], ['#', 'Check', 'Included?', 'Control to verify (what must have happened)', 'Source record(s) used', 'SRR risk IDs covered', 'If not included: reason, agreed by, condition to include'],
       lambda: (td(ck('Included', 'Not included', 'Deferred until:', cls='opts col')), td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left')), 'Checks in scope', 2)
matrix('D', 'Schedule, reviewer and sample', 'Time each check by how fast its failure would spread. The reviewer is named by role, released for the task, and does not review work they did. Name one unit per check (procedure, image set, visit, field, event…) and say how units are picked; a small population is reviewed in full.',
       [3, 17, 9, 9, 13, 10, 9, 11, 10, 9], ['#', 'Check', 'Timing basis', 'Routine frequency', 'Earlier review for this check when…', 'Reviewer / backup (roles)', 'Unit and number per period', 'How units are picked', 'Minimum, and when all are reviewed', 'Sample grows when…'],
       lambda: (td(ck('Calendar', 'Case count', 'Each event', 'Milestone', cls='opts col')),) + tuple(td('', 'left') for _ in range(7)), 'Schedule, reviewer and sample', 4)
matrix('E', 'Criteria the reviewer applies', 'Write each criterion so two reviewers would reach the same answer. The IMC rates each check on these three questions separately.',
       [3, 20, 19, 19, 19, 20], ['#', 'Check', 'Execution: the control was done when…', 'Evidence: the record is sufficient when…', 'Effective: the control worked when…', 'Records the reviewer cites in the IMC'],
       lambda: tuple(td('', 'left') for _ in range(4)), 'Criteria the reviewer applies', 6)
# ---------- Page 6: G triggers + H responses
trig = ['Serious adverse event or serious device effect at the site', 'Complication cluster or signal from the CSST', 'Important protocol deviation', 'Repeated endpoint data discrepancy',
        'Pattern of unusable or late images (IQL)', 'Device, instrument or equipment malfunction', 'CIP amendment', 'Departure or change of a key person or of a reviewer',
        'Sponsor finding that needs a local response', 'Corrective action that failed or was reopened']
F = (sec('F', 'Triggers for an earlier review', 'Any trigger marked Yes calls a review before the next scheduled one, for the checks listed. A minor observation is not a trigger.') +
     table('gtt', [41, 13, 20, 14, 12], ['Trigger', 'Applies?', 'Checks reviewed early (#)', 'Called by (role)', 'Within (days)'],
           [tr(el(t), td(ck('Yes', 'No')), td(), td(), td()) for t in trig]))
resp = ['Complete, adequate and effective', 'Observation: isolated, low consequence, corrected at review', 'Partial execution or partial evidence',
        'Not performed, or evidence missing', 'Not effective', 'Not assessable', 'Recurrent, across units, or with material consequence', 'Possible harm to a participant or a reportable event']
G = (sec('G', 'Where each result goes', 'For each result the IMC can give, write the minimum response the site commits to, the record it goes to, and who owns it.') +
     table('ht', [30, 52, 18], ['Result in the IMC', 'Minimum response and record it goes to', 'Owner (role)'],
           [tr(el(a), td('', 'left'), td()) for a in resp]))
pages.append(f'<main class="page">{top("Earlier reviews and responses")}<section class="section compact">{F}</section><section class="section compact">{G}</section>{foot("Earlier reviews and responses", 8)}</main>')
# ---------- Page 7: I approval + J change control
H = (sec('H', 'Ready to start', 'Confirm before the first inclusion. PI approval means the plan can be run with the people and time available.') +
     table('it', [44, 16, 40], ['Confirmation', 'Status', 'Date, or action and due date if No'], [
         tr(el('Every reviewer and backup is released for the task in the delegation log'), td(ck('Yes', 'No')), td()),
         tr(el('Staff who do the checked work know the plan'), td(ck('Yes', 'No')), td()),
         tr(el('The IMC is prepared with this IMP ID and version'), td(ck('Yes', 'No')), td()),
         tr(el('First review due (date or after inclusion number)'), td('', 'left" colspan="2'))]) +
     '<div class="sig2"><div class="signature"><b>Plan owner</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
I = (sec('I', 'Changes to the plan', 'A change applies from its effective date. A result already seen is never the reason to loosen a rule for the same period.') +
     table('jt', [9, 13, 20, 20, 16, 11, 11], ['Change ID', 'Section / check', 'Previous rule', 'New rule', 'Reason (IMC, CAPA, SRR, sponsor…)', 'Effective from', 'Approved by'],
           [tr(td(), td(), td('', 'left'), td('', 'left'), td('', 'left'), td(), td()) for _ in range(8)]))
pages.append(f'<main class="page">{top("Readiness, approval and changes")}<section class="section compact">{H}</section><section class="section compact">{I}</section>{foot("Readiness, approval and changes", 9)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:60px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.purpose td{font-size:9px;padding:4px 7px;vertical-align:top;text-align:left;height:52px}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{font-size:8.8px}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.el .sub{display:block;font-weight:400;color:#4d5b6b;font-size:7.8px;line-height:1.2;margin-top:1px}
td.num{font-weight:700;color:#173c67;font-size:9px}
.addnote{margin-top:6px;font-size:8.6px;color:#4d5b6b;border-left:3px solid var(--navy);padding:3px 8px;background:#f7f9fb}
.bt td{height:66px;font-size:8.8px;padding:3px 6px}
.inline-blank{display:inline-block;width:46px;border-bottom:1px solid #6d7a88;margin:0 3px}
.gate{border:1px solid var(--grid);border-left:4px solid var(--navy);background:#f7f9fb;padding:7px 9px;margin-top:7px;font-size:9.4px;color:#173c67}
.opts.col2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:1px 6px}
.lt td{height:70px;font-size:8.6px;padding:2px 5px}.lt th{font-size:8.4px}.lt .opts{font-size:7.6px;line-height:1.15}
.gtt td{height:34px;font-size:8.8px;padding:2px 6px}
.ht td{height:51px;font-size:8.6px;padding:2px 6px}
.it td{height:38px;font-size:8.8px;padding:3px 6px}
.jt td{height:57px;font-size:8.6px;padding:2px 5px}
.sig2 .signature{min-height:96px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
