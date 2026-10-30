# Builds SART v1.0 (blank) from scratch, reusing the house look and editor of the concluded POT v1.1.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = p[:p.find('<body')]
head = re.sub(r'<title>.*?</title>', '<title>SART v1.0 - Blank Editable</title>', head)
ed_style = p[p.find('<style id="pot-editor-style">'):]
ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]
ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'sart-').replace("'pot-'", "'sart-'").replace('Editor do POT', 'Editor do SART').replace('POT', 'SART')
V = 'SART v1.0'
NP = 6
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">SART - Safety Assessment, Reporting and Tracking Template</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">SART · v1.0</div></header>')
def sec(letter, title, guide=None):
    g = f'<div class="guide">{guide}</div>' if guide else ''
    return f'<div class="section-header"><div class="letter">{letter}</div><div class="section-title">{title}</div></div>{g}'
def foot(txt, n):
    return f'<footer class="footer"><div>{V} | {txt}</div><div>Page {n} of {NP}</div></footer>'
def strip(extra='Sheet number / total sheets'):
    cells = ['Study / site', 'SART case ID / revision', 'Participant code or N/A', extra]
    return '<section class="sheet-strip">' + ''.join(f'<div class="meta-cell"><b>{c}</b><span class="blank-entry"></span></div>' for c in cells) + '</section>'
def meta(label, inner='<span class="blank-entry"></span>', cls='meta-cell'):
    return f'<div class="{cls}"><b>{label}</b>{inner}</div>'

pages = []
# ---------------- Page 1: header + A
hdr = ''.join([
    meta('Study / protocol'), meta('Current CIP / version'), meta('Site / code'), meta('SART case ID / revision'),
    meta('Participant code (or N/A and why)'), meta('Procedure, visit or exposure (or N/A)'), meta('Site awareness: date / time'), meta('Person who received the first information'),
    meta('PI / authorized site assessor'), meta('Sponsor safety system / route'), meta('Sponsor safety case ID (if issued)'),
    meta('Current local case status', ck('Open', 'Awaiting sponsor', 'Closed locally', cls='opts left')),
])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SART is the site\'s record of one safety case, from the moment the site becomes aware of it until the site\'s part of the case is closed. '
     'It shows that the site recognized the information, protected the person, made its own assessment, reported through the sponsor\'s route within the CIP window, followed the case and linked it to its other records.</p>'
     '<p>Open the SART at awareness, without waiting for a complete classification. Sections B to D are completed in the first days; Section E grows with each new piece of information; Sections F and G close the site\'s part.</p></div>'
     '<div class="boundary"><b>Boundary.</b> This is a controlled site coordination record. It does not replace source records, the sponsor safety form, the eCRF, the sponsor safety portal, the device-accountability record, the deviation record, the SCML, the CSST, the CAPA log, a regulatory submission or the sponsor/CEC safety determination. It records the site\'s part of the case and the references to those records.</div>'
     '<table class="purpose"><colgroup><col style="width:19%"><col style="width:81%"></colgroup><tbody>'
     '<tr><td>Unit of analysis</td><td>One safety case at the site: one adverse event, one observed device deficiency or one piece of new safety information.</td></tr>'
     '<tr><td>Decision supported</td><td>Whether the site recognized, protected, assessed, reported, followed and closed its part of the case in a controlled way.</td></tr>'
     '<tr><td>Inputs</td><td>Source records, participant or user contact, device and accountability records, procedure or visit records (ICDL, PFVR, IQL), sponsor communications, the current CIP and risk information.</td></tr>'
     '<tr><td>Outputs</td><td>The local trail of the case; references to the sponsor system; the reporting data read by the PIR (safety reporting timeliness); the links to the SCML, the deviation record and, when triggered, the CSST, POT, SRR or CAPA.</td></tr>'
     '</tbody></table>'
     '<p class="rule"><b>Rule:</b> if an adverse event is associated with an observed device deficiency, apply both the adverse-event pathway and the device-deficiency pathway (Section C).</p>')

# ---------------- Page 2: B
rowsB = [
    ('Occurrence, deficiency detection or new information: date / time', ck('Known', 'Estimated', 'Not yet known')),
    ('Site awareness: date / time, and who brought the information (person and source)', ''),
    ('Initial trigger', ck('Adverse event', 'Observed device deficiency', 'AE associated with an observed DD', 'New safety information', 'Other CIP-defined trigger', cls='opts left')),
    ('Immediate safety concern for the participant, user or another person', ck('Yes', 'No', 'Not yet determined')),
    ('Immediate action taken: clinical care, device containment or communication (who, when)', ''),
    ('Device and procedure context: system and component; model, lot, serial or UDI; size; technical step (or N/A)', ''),
]
tb = ''.join(f'<tr><td class="el">{a}</td><td class="opts-cell">{b}</td><td class="left"></td></tr>' for a, b in rowsB)
B = (sec('B', 'Awareness, immediate protection and source map', 'Record what is known at awareness and where it is documented. Do not copy narratives from the clinical record or the sponsor form.') +
     '<table class="bt"><colgroup><col style="width:34%"><col style="width:24%"><col style="width:42%"></colgroup><thead><tr><th>Item</th><th>Status</th><th>Record / reference</th></tr></thead><tbody>' + tb + '</tbody></table>'
     '')
B2 = (sec('B', 'Awareness, immediate protection and source map (continued)') +
     '<div class="wbox fact"><b>Factual summary (what happened, as known now)</b></div>'
     '<div class="subhead">Source map</div><table class="src2"><colgroup><col style="width:30%"><col style="width:30%"><col style="width:40%"></colgroup><thead><tr><th>Source record</th><th>ID / location</th><th>What it holds for this case</th></tr></thead><tbody>' + '<tr><td></td><td></td><td></td></tr>' * 6 + '</tbody></table>'
     '<div class="subhead">Missing information</div><table class="src2"><colgroup><col style="width:52%"><col style="width:22%"><col style="width:26%"></colgroup><thead><tr><th>Information still missing</th><th>Owner (Role ID)</th><th>Next step / due</th></tr></thead><tbody>' + '<tr><td></td><td></td><td></td></tr>' * 5 + '</tbody></table>')
pages.append(('', f'<main class="page">{top("Case opening, purpose and awareness")}<section class="meta-grid">{hdr}</section><section class="section">{A}</section><section class="section compact">{B}</section>{foot("Case identification, purpose and awareness", 1)}</main>'))
pages.append(('', f'<main class="page">{top("Awareness and immediate protection")}{strip("Site awareness: date / time")}<section class="section compact">{B2}</section>{foot("Factual summary and source map", 2)}</main>'))

# ---------------- Page 3: C
def q(row, opts, extra=True):
    return f'<tr><td class="el">{row}</td><td class="opts-cell">{opts}</td><td class="left"></td></tr>'
C1 = ''.join([
    q('Adverse event identified?', ck('Yes', 'No', 'Pending')),
    q('Seriousness (mark all that apply)', ck('Death', 'Life-threatening illness or injury', 'Permanent impairment of a body structure or function', 'In-patient or prolonged hospitalization', 'Intervention to prevent the above', 'Fetal distress, fetal death or congenital abnormality', 'Does not meet seriousness criteria', 'Pending', cls='opts col')),
    q('Clinical severity (intensity, on the CIP scale): kept apart from seriousness', ck('Mild', 'Moderate', 'Severe', 'Pending')),
    q('Related to the investigational device?', ck('Yes', 'No', 'Pending')),
    q('Related to the comparator?', ck('Yes', 'No', 'Pending', 'N/A')),
    q('Related to a CIP-required procedure outside routine practice?', ck('Yes', 'No', 'Pending', 'N/A')),
    q('If a SADE: identified in the current risk assessment?', ck('ASADE', 'USADE', 'Pending', 'N/A')),
    q('Resulting local category', ck('Non-serious AE', 'SAE', 'ADE', 'SADE', 'ASADE', 'USADE', 'Pending', cls='opts left')),
])
C2 = ''.join([
    q('Observed device deficiency?', ck('Yes', 'No', 'Pending')),
    q('Type (mark all that apply)', ck('Identity', 'Quality', 'Durability', 'Reliability', 'Usability', 'Safety', 'Performance', 'Malfunction', 'Use error', 'Information or label', cls='opts left')),
    q('Associated with an adverse event? (Yes: apply both pathways)', ck('Yes', 'No', 'Pending')),
    q('Could it have led to a SADE?', ck('Yes', 'No', 'Pending')),
    q('Device containment, return or analysis (reference)', ck('Done', 'Pending', 'N/A')),
])
C3 = ''.join([
    q('Contributing context, as now assessed (for the SCML; mark all that apply)', ck('Device', 'Procedure', 'Operator or technique', 'Patient', 'Undetermined', cls='opts left')),
    q('Serious health threat (imminent risk needing rapid action to protect others)?', ck('Yes', 'No', 'Pending')),
])
C = (sec('C', 'Current PI / site assessment', 'This is the site\'s assessment and may change. The sponsor or CEC determination is recorded apart, in the last table. Rationale and source go in the right-hand column.') +
     '<div class="subhead">C1 · Adverse-event pathway</div><table class="ct"><colgroup><col style="width:33%"><col style="width:39%"><col style="width:28%"></colgroup><tbody>' + C1 + '</tbody></table>'
     '<div class="subhead">C2 · Device-deficiency pathway</div><table class="ct"><colgroup><col style="width:33%"><col style="width:39%"><col style="width:28%"></colgroup><tbody>' + C2 + '</tbody></table>'
     '<div class="subhead">C3 · Context and urgency</div><table class="ct"><colgroup><col style="width:33%"><col style="width:39%"><col style="width:28%"></colgroup><tbody>' + C3 + '</tbody></table>'
     '<div class="subhead">C4 · Who has assessed the case</div><table class="ct auth"><colgroup><col style="width:33%"><col style="width:39%"><col style="width:28%"></colgroup><tbody>'
     + q('Current PI / site assessment: status, assessor, date', ck('Pending', 'Preliminary', 'Final (PI)'))
     + q('Sponsor / CEC determination: date and reference', ck('Not yet received', 'Received'))
     + q('Agreement between the two', ck('Agree', 'Disagree', 'Not yet known'))
     + q('Open classification question and owner', '')
     + '</tbody></table>')
pages.append(('', f'<main class="page">{top("Current PI / site assessment")}{strip("Assessment date")}<section class="section compact">{C}</section>{foot("Current PI / site assessment", 3)}</main>'))

# ---------------- Page 4: D
rowsD = [
    ('Reportable under the current CIP or sponsor procedure? (rule reference)', ck('Yes', 'No', 'Pending')),
    ('Route used', ck('Sponsor portal', 'eCRF', 'SAE form', 'DD form', 'Emergency route', 'Other', cls='opts left')),
    ('Site awareness: date / time (from Section B)', ''),
    ('CIP reporting window, and due date / time', ''),
    ('Initial notification sent: date / time, by whom, system reference', ''),
    ('Receipt confirmed / sponsor safety case ID', ck('Yes', 'Pending')),
    ('Initial notification on time?', ck('Yes', 'No', 'Pending', 'N/A')),
    ('First report complete?', ck('Complete', 'Incomplete', 'Pending', 'N/A')),
    ('If late or incomplete: where the delay arose', ck('Recognition', 'Internal escalation', 'PI assessment', 'Access to documentation', 'Transmission', 'Other', cls='opts left')),
    ('Correction made, and deviation record ID if the notification was late', ''),
    ('Ethics committee or authority communication, only if the CIP assigns it to the site', ck('Sent', 'Not required', 'Pending')),
]
D = (sec('D', 'Reporting to the sponsor', 'Record the proof of reporting, not the content of the sponsor form. Every time limit comes from the CIP or the sponsor procedure. The PIR reads its safety reporting timeliness counts from this section.') +
     '<table class="dt"><colgroup><col style="width:36%"><col style="width:30%"><col style="width:34%"></colgroup><thead><tr><th>Reporting step</th><th>Status</th><th>Record / reference</th></tr></thead><tbody>' +
     ''.join(f'<tr><td class="el">{a}</td><td class="opts-cell">{b}</td><td class="left"></td></tr>' for a, b in rowsD) + '</tbody></table>')
pages.append(('', f'<main class="page">{top("Reporting to the sponsor")}{strip()}<section class="section compact">{D}</section>{foot("Reporting to the sponsor", 4)}</main>'))

# ---------------- Page 5: E (landscape, repeatable)
E = (sec('E', 'Follow-up and new information', 'One line for each new piece of information or sponsor request. Add lines; never overwrite an earlier one.') +
     '<table class="et"><colgroup><col style="width:4%"><col style="width:9%"><col style="width:20%"><col style="width:13%"><col style="width:12%"><col style="width:8%"><col style="width:11%"><col style="width:7%"><col style="width:16%"></colgroup>'
     '<thead><tr><th>No.</th><th>Date / time received</th><th>New clinical, technical or device information, and its source</th><th>Effect on the site assessment</th><th>Sponsor request or communication (reference)</th><th>Follow-up due</th><th>Sent / receipt reference</th><th>On time?</th><th>Owner (Role ID) and next step</th></tr></thead><tbody>' +
     ''.join(f'<tr><td>{i}</td>' + '<td></td>' * 6 + f'<td>{ck("Yes", "No", "N/A", cls="opts col")}</td><td class="left"></td></tr>' for i in range(1, 9)) +
     '</tbody></table><p class="table-note">If more lines are needed, reprint this sheet, number it and continue the numbering.</p>')
pages.append(('landscape', f'<main class="page landscape">{top("Follow-up and new information")}{strip()}<section class="section compact">{E}</section>{foot("Follow-up and new information (sheet)", 5)}</main>'))

# ---------------- Page 6: F + G
rowsF = [
    ('SCML', 'Every adverse event or device deficiency at the site', 'SCML event ID'),
    ('Deviation record', 'The initial notification was late; the sponsor\'s criteria decide its importance', 'Deviation ID'),
    ('CSST, early review', 'Serious health threat, cluster, new category, or concentration in one component or surgeon', 'Review reference'),
    ('POT', 'The case, a delay or a pending decision needs the PI\'s oversight', 'POT review ID'),
    ('SRR or CAPA', 'A recurring failure or a weak local control; not for a single case', 'Record ID'),
]
F = (sec('F', 'Links to other records') +
     '<table class="ft"><colgroup><col style="width:16%"><col style="width:40%"><col style="width:24%"><col style="width:20%"></colgroup><thead><tr><th>Record</th><th>When it applies</th><th>ID / date</th><th>Status</th></tr></thead><tbody>' +
     ''.join(f'<tr><td class="el">{a}</td><td class="left">{b}<small> · {c}</small></td><td></td><td>{ck("Linked", "Not required", "Pending")}</td></tr>' for a, b, c in rowsF) + '</tbody></table>')
gates = ['Immediate protection and care documented (or N/A, with the reason)', 'Source references enough to reconstruct the case', 'Current PI / site assessment documented', 'Sponsor submission and receipt documented', 'Timeliness and completeness known, or the limitation recorded', 'Follow-up completed, transferred or explicitly open', 'Sponsor / CEC determination recorded, or recorded as pending', 'Links in Section F completed']
G = (sec('G', 'Closing the site\'s part of the case') +
     '<table class="gt"><colgroup><col style="width:56%"><col style="width:16%"><col style="width:28%"></colgroup><thead><tr><th>Before closing, confirm that…</th><th>Result</th><th>Reference / limitation</th></tr></thead><tbody>' +
     ''.join(f'<tr><td class="left">{g}</td><td>{ck("Yes", "No", "N/A")}</td><td></td></tr>' for g in gates) + '</tbody></table>'
     '<div class="close-row"><div class="meta-cell"><b>Local closure status</b>' + ck('Closed locally', 'Open follow-up', 'Transferred', 'Not yet eligible', cls='opts left') + '</div><div class="meta-cell"><b>Current outcome and open items</b><span class="blank-entry"></span></div></div>'
     '<p class="table-note">Local closure does not close the sponsor, CEC, ethics committee or regulatory process.</p>'
     '<div class="sig3"><div class="signature"><b>Case reporter / initial site assessor</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>PI / accountable investigator</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Safety coordinator (if applicable)</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>'
     '<div class="writeline" style="border-top:1px solid var(--grid);margin-top:6px"><b>Controlled location of the SART and linked system references:</b> </div>')
pages.append(('', f'<main class="page">{top("Links and closure")}{strip()}<section class="section compact">{F}</section><section class="section compact">{G}</section>{foot("Links, closure and sign-off", 6)}</main>'))

css = '''<style>
.meta-grid{grid-template-columns:repeat(4,1fr)}.meta-grid .meta-cell{min-height:44px}
.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.boundary{border:1px solid var(--grid);border-left:4px solid var(--navy);background:#f7f9fb;padding:7px 10px;margin-top:7px;font-size:9.6px;line-height:1.35;color:#2f4558;text-align:justify}
.rule{margin:7px 0 0;font-size:9.8px;color:#173c67}
.purpose td{font-size:9.4px}
td.opts-cell{text-align:left}td.opts-cell .opts{justify-content:flex-start}
.bt td{height:40px;font-size:9px;padding:4px 6px}.bt td.el,.ct td.el,.dt td.el,.ft td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.9px}
.wbox.fact{min-height:300px}
.src2 td{height:36px}
.ct td{height:32px;font-size:8.8px;padding:3px 6px}.ct .opts{font-size:8px;gap:1px 7px}
.dt td{height:64px;font-size:9px;padding:4px 6px}
.et td{height:47px;font-size:8.8px;padding:3px 5px}.et th{font-size:8.4px}
.ft td{height:38px;font-size:8.8px;padding:3px 6px}.ft small{color:#5f6670}
.gt td{height:27px;font-size:8.9px;padding:3px 6px}
.close-row{display:grid;grid-template-columns:1fr 1.2fr;border-left:1px solid var(--grid);border-top:1px solid var(--grid);margin-top:7px}.close-row .meta-cell{min-height:52px}
.sig3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:8px}.sig3 .signature{min-height:104px!important}
.subhead{margin-top:7px}
.letter{font-size:15px!important}
</style>
'''
html = head + '<body class="blank-template">\n' + '\n'.join(pg for _, pg in pages) + '\n' + css + ed + '\n</body></html>\n'
open(OUT, 'w').write(html)
print('ok')
