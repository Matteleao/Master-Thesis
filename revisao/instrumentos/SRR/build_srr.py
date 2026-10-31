# SRR v1.0 (blank), from the author's v0.2, the Codex analysis (v0.91) and the thesis (4.3, 4.3.1, Table 3.2).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>SRR v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'srr-').replace('Editor do POT', 'Editor do SRR').replace('POT', 'SRR')
V, NP = 'SRR v1.0', 7
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">SRR - Site Risk Register</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">v1.0</div></header>')
def sec(letter, title, guide=None):
    return f'<div class="section-header"><div class="letter">{letter}</div><div class="section-title">{title}</div></div>' + (f'<div class="guide">{guide}</div>' if guide else '')
def foot(txt, n): return f'<footer class="footer"><div>{V} | {txt}</div><div>Page {n} of {NP}</div></footer>'
def meta(label, inner='<span class="blank-entry"></span>'): return f'<div class="meta-cell"><b>{label}</b>{inner}</div>'
def strip(sheet):
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['Study / site', 'SRR ID / revision', 'Revision effective date', sheet]) + '</section>'
def table(cls, widths, heads, rows):
    col = ''.join(f'<col style="width:{w}%">' for w in widths)
    th = ''.join(f'<th>{h}</th>' for h in heads) if heads else ''
    return f'<table class="{cls}"><colgroup>{col}</colgroup>' + (f'<thead><tr>{th}</tr></thead>' if heads else '') + '<tbody>' + ''.join(rows) + '</tbody></table>'
def tr(*cells): return '<tr>' + ''.join(cells) + '</tr>'
el = lambda t: f'<td class="el">{t}</td>'
td = lambda t='', c='': f'<td class="{c}">{t}</td>' if c else f'<td>{t}</td>'
pages = []
# ---------- Page 1: header, A, B
hdr = ''.join(meta(c) for c in ['Study / protocol', 'CIP version / date', 'Site / code', 'SRR ID / revision', 'Principal Investigator', 'Register owner / role',
                                 'Sponsor risk information (ID / version)', 'Study phase', 'Date opened', 'Last review / next review', 'Current reviewer / role', 'Controlled location'])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SRR is the site\'s own record of the risks that its execution of the investigation creates: where local staffing, workflow, equipment or experience can compromise a condition that is critical to quality (CtQ) for this investigation. It is opened before the first participant is included and kept current until close-out. It complements the sponsor\'s risk assessment and the manufacturer\'s device risk file; it does not copy them.</p>'
     '<p>Pages 1 to 3 are reference: categories, CtQ domains, rating rules and decision rules. The register is G and H: one row per risk, with the same Risk ID on both pages; reprint the pair when it fills. Every review of a risk is entered in I. An urgent local risk is captured in J and then entered in the register. K closes each review of the register.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One local risk to one CtQ factor of this investigation.</td>'
     '<td>What threatens the factor, what risk remains with the controls in place, what happens next, who owns it and when it is reviewed again.</td>'
     '<td>CIP, sponsor risk information, local workflow and capacity; findings from the IMC, PIR, CSST, SLCT, SART and CAPA log.</td>'
     '<td>Controls for the IMP to verify; PI decisions in the POT; milestone conditions for the MRL; CAPA, sponsor and safety routes.</td></tr></tbody></table>')
cats = [('Safety / clinical event', 'Delayed safety awareness, incomplete assessment or missed reporting.', 'Participant protection and timely clinical decisions.'),
        ('Procedure / surgeon performance', 'Learning-curve drift, unplanned substitution or inconsistent technique.', 'Procedural consistency and interpretation of outcomes.'),
        ('Device accountability', 'Mixed or poorly segregated stock, missing identifiers or reconciliation gaps.', 'Correct component selection and participant-device traceability.'),
        ('Data / endpoint reliability', 'Missing assessment, unresolved critical query or source-to-CRF mismatch.', 'Complete, reliable and interpretable study data.'),
        ('Operational / staffing', 'No assessor on needed days, turnover, workload or unclear handover.', 'Capacity to deliver required study activities.'),
        ('Consent / eligibility', 'Wrong consent version, delayed re-consent or unsupported eligibility.', 'Participant rights and valid enrollment.'),
        ('Imaging / assessment workflow', 'Wrong projection, missed window or inconsistent assessment method.', 'Comparable and interpretable endpoint assessments.'),
        ('Vendor / external data', 'Delayed external records, inaccessible results or missing transfers.', 'Availability of safety and endpoint evidence.')]
B = (sec('B', 'Risk categories', 'The category says where in local operations the risk sits. It is not the CtQ domain: one staffing risk can threaten follow-up, safety and data at once.') +
     table('bt', [24, 42, 34], ['Category', 'Typical local vulnerability', 'What may be affected'], [tr(el(a), td(b, 'left'), td(c, 'left')) for a, b, c in cats]) +
     '<div class="note"><b>Common review triggers:</b> repeated protocol deviations; missed assessment or visit window; delayed safety reporting; device discrepancy or wrong selection; learning-curve or performance signal; monitoring or audit finding; recurrent or ineffective action; change in staffing, training or capacity; change in CIP, device or workflow.</div>')
pages.append(f'<main class="page">{top("Identification, purpose and risk categories")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and categories", 1)}</main>')
# ---------- Page 2: C domains, D rating
doms = [('CtQ1', 'Site capability, readiness and capacity maintenance', 'Staff, procedure volume, facilities, equipment, imaging, rehabilitation and follow-up capacity'),
        ('CtQ2', 'Participant selection and baseline characterization', 'Eligibility criteria, baseline assessment, documented selection decision'),
        ('CtQ3', 'Informed consent and participant understanding', 'Consent process, version control, comprehension, re-consent on amendment'),
        ('CtQ4', 'Device management, accountability and traceability', 'Receipt, storage, access, use in a named participant, identifiers, reconciliation'),
        ('CtQ5', 'Procedural delivery and surgical technique standardization', 'Approach, positioning, soft tissue, intraoperative decision thresholds'),
        ('CtQ6', 'Training, credentialing and learning-curve control', 'Eligibility, procedure competency, device release, maintained authorization'),
        ('CtQ7', 'Perioperative and postoperative care pathway and follow-up retention', 'Care pathway, visit scheduling and windows, retention over long follow-up'),
        ('CtQ8', 'Endpoint framework and outcome-assessment standardization', 'Assessor consistency, administration conditions, PRO timing and mode'),
        ('CtQ9', 'Imaging acquisition, interpretation and endpoint control', 'Acquisition parameters, equipment and operator consistency, local review, timing'),
        ('CtQ10', 'Safety surveillance and adverse device event management', 'Detection, classification, causality and reporting of AEs, device effects and DDs'),
        ('CtQ11', 'Data capture, source documentation and data-flow integrity', 'Source adequacy for reconstruction, source-to-record consistency'),
        ('CtQ12', 'Regulatory compliance and deviation management', 'Detection, documentation, classification and correction of deviations')]
C = (sec('C', 'CtQ domains and the factor to protect', 'In the register, give the domain code and then write, in one sentence, the factor this investigation must protect. A domain name is not a factor. Cite where the factor comes from (CIP, sponsor risk information, local workflow); if it is still unclear, write "to be clarified with the sponsor".') +
     table('ct', [8, 42, 50], ['Code', 'Domain', 'What it covers'], [tr(td(a, 'code'), el(b), td(c, 'left')) for a, b, c in doms]))
rate = [('Probability (P)', 'Unlikely; isolated vulnerability.', 'Plausible in normal site conduct.', 'Likely, recurrent or already observed.'),
        ('Safety (S)', 'No expected effect on safety or participant protection.', 'May affect timely clinical review, protection or safety documentation.', 'May cause or hide serious harm, a serious device effect or a major safety concern.'),
        ('Procedure (Pr)', 'No expected effect on the conduct of the procedure.', 'May affect consistency, documentation or protocol adherence.', 'May affect surgical appropriateness, intraoperative decisions or technical execution.'),
        ('Device (Dv)', 'No expected traceability or selection concern.', 'Recoverable discrepancy or delayed reconciliation.', 'May compromise identifiers, component selection or the participant-device link.'),
        ('Data (Da)', 'No expected effect on critical study data.', 'May affect completeness, timing or source-to-CRF consistency.', 'May compromise endpoint interpretation, eligibility evidence or critical data.'),
        ('Detection (D)', 'Easy: routine checks find it before it has an effect.', 'Moderate: found only by a planned review, reconciliation or second check.', 'Difficult: may stay hidden until endpoint review, inspection or recurrence.')]
D = (sec('D', 'Rating rules', 'Rate with the controls already in place: the result is the current risk. A planned action does not lower a score. Mark a dimension N/A when it does not apply and say why in a few words; N/A is not 1. Do not average or multiply.') +
     table('dt', [16, 28, 28, 28], ['Field', '1', '2', '3'], [tr(el(a), td(b, 'left'), td(c, 'left'), td(d, 'left')) for a, b, c, d in rate]) +
     table('pt', [25, 25, 25, 25], ['Low', 'Moderate', 'High', 'Critical'], [tr(
         td('Every applicable field is 1.', 'left'), td('The highest applicable field is 2.', 'left'), td('Any applicable field is 3.', 'left'),
         td('A condition, not a score: an unresolved serious safety threat, a broken participant-device link, unrecoverable endpoint-critical data, or a threshold the study defines as critical.', 'left'))]) +
     '<div class="note">A reportable event follows its CIP route at every priority; reporting never waits for the SRR. A study rule that sets a higher priority prevails; cite it.</div>')
pages.append(f'<main class="page">{top("CtQ domains and rating rules")}<section class="section compact">{C}</section><section class="section compact">{D}</section>{foot("CtQ domains and rating rules", 2)}</main>')
# ---------- Page 3: E examples, F decision rules
ex = [('<b>CtQ7 · Follow-up</b><br>Factor: participants complete the required follow-up assessments within their windows.', 'No physiotherapist is available for the assessment on Tuesdays and Thursdays. Participants who can attend only on those days may miss the visit or leave it incomplete.', 'Assess the real flexibility of appointments, other qualified staff and referral options. Do not assume a safety effect or a high score without looking at the study and the controls in place.'),
      ('<b>CtQ4 · Device management</b><br>Factor: the correct study component is selected and stays traceable to the participant.', 'Study and marketed components with similar labels share storage without clear segregation, so a wrong component can be picked or the traceability link broken.', 'Assess labeling, segregation, access and reconciliation already in place. A dedicated room is not the criterion; how well the current controls work is.')]
E = (sec('E', 'How to write an entry', 'Illustrations of the reasoning, not entries to copy. Write the vulnerability and its consequence, not the domain name.') +
     table('et', [30, 36, 34], ['Domain and factor to protect', 'Local vulnerability and possible consequence', 'How to judge the current risk'], [tr(td(a, 'left'), td(b, 'left'), td(c, 'left')) for a, b, c in ex]))
dec = [('Lower the priority', 'Controls are implemented and a review (I) shows they work. Re-rate every field and keep the trigger. A planned or completed action alone is not enough.', 'PI for High or Critical; otherwise the register owner at the oversight review.'),
       ('Accept the residual risk', 'The risk remains but no further action is proportionate. Record the reason, keep the trigger active and set the next review.', 'PI, or the role the PI authorizes for Low and Moderate.'),
       ('Close the risk', 'The condition no longer applies: the phase ended, the process changed or the vulnerability was removed with evidence. A closed CAPA does not close a risk by itself.', 'PI when the risk concerns safety, traceability, endpoint data or a CAPA.'),
       ('Escalate to the CAPA log', 'A control failed or the problem recurs, it is systemic, or the action needs several steps and an effectiveness check. Link an existing CAPA when one covers it.', 'PI or the authorized corrective-action route.'),
       ('Escalate to the PI (POT) or a milestone (MRL)', 'A PI decision is needed: priority, acceptance, restriction, resources or oversight intensity; or the risk bears on a phase gate.', 'PI; urgent matters use the immediate route.'),
       ('Escalate to the sponsor or CRO', 'The effect may reach beyond the site, or the CIP or a sponsor threshold requires it. A threat can be escalated before any event occurs.', 'PI, within the CIP route and timing.')]
F = (sec('F', 'Decision rules after a review', 'Each decision is recorded in I with its evidence; the status in H is then updated.') +
     table('ft', [22, 50, 28], ['Decision', 'When it applies', 'Who decides'], [tr(el(a), td(b, 'left'), td(c, 'left')) for a, b, c in dec]))
pages.append(f'<main class="page">{top("Entry examples and decision rules")}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Entry examples and decision rules", 3)}</main>')
# ---------- Page 4: G register identification and rating (landscape)
fac = '<span class="lab">Domain:</span><span class="lab f2">Factor / source:</span>'
G = (sec('G', 'Register · identification and rating', 'One row per risk. Write the factor to protect, the local vulnerability and its consequence, and the controls already in place with their evidence; then rate with those controls. Use the same Risk ID in H.') +
     table('gt', [5, 6, 8, 17, 18, 15, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 10], ['Risk ID', 'Date opened', 'Category', 'CtQ domain, factor and source', 'Local vulnerability and possible consequence', 'Existing controls and evidence', 'P', 'S', 'Pr', 'Dv', 'Da', 'D', 'Current priority'],
           [tr(td(), td(), td(), td(fac, 'left'), td('', 'left'), td('', 'left'), td(), td(), td(), td(), td(), td(), td(ck('Low', 'Moderate', 'High', 'Critical', cls='opts col'))) for _ in range(5)]))
pages.append(f'<main class="page landscape">{top("Register · identification and rating")}{strip("Register sheet no. / total")}<section class="section compact">{G}</section>{foot("Register · identification and rating", 4)}</main>')
# ---------- Page 5: H controls, ownership (landscape)
H = (sec('H', 'Register · ownership, action and status', 'Continue the Risk IDs from G on the same sheet number. Risk status says whether the risk still applies; action status says where the response stands. Implemented is not Effective until a review in I shows the control works.') +
     table('ht', [5, 9, 15, 16, 14, 12, 9, 11, 9], ['Risk ID', 'Risk owner (role)', 'Review trigger or threshold', 'Planned action / owner / due', 'Linked records and evidence', 'PI / sponsor route and deadline', 'Risk status', 'Action status', 'Last / next review'],
           [tr(td(), td(), td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left'), td(ck('Open', 'Controlled', 'Accepted', 'Closed', cls='opts col')), td(ck('Not started', 'In progress', 'Implemented', 'Effective', 'Not effective', cls='opts col')), td()) for _ in range(5)]))
pages.append(f'<main class="page landscape">{top("Register · ownership, action and status")}{strip("Register sheet no. / total")}<section class="section compact">{H}</section>{foot("Register · ownership, action and status", 5)}</main>')
# ---------- Page 6: I review log (landscape)
I = (sec('I', 'Risk review log', 'One line per risk reviewed, at the scheduled review or when a trigger occurs. Record the evidence, whether the control worked and the current scores; never overwrite an earlier line.') +
     table('it', [9, 6, 10, 18, 11, 12, 9, 16, 9], ['Date / reviewer', 'Risk ID', 'Scheduled or trigger', 'Evidence reviewed', 'Control effectiveness', 'Current P S Pr Dv Da D / priority', 'Risk status', 'Decision and linked record', 'Next review'],
           [tr(td(), td(), td('', 'left'), td('', 'left'), td(ck('Effective', 'Partly effective', 'Not effective', 'Not assessable', cls='opts col')), td(), td(ck('Open', 'Controlled', 'Accepted', 'Closed', cls='opts col')), td('', 'left'), td()) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Risk review log")}{strip("Review log sheet no. / total")}<section class="section compact">{I}</section>{foot("Risk review log", 6)}</main>')
# ---------- Page 7: J urgent entry, K review sign-off
jrow = lambda a, b='': tr(el(a), td(b, 'left'))
J = (sec('J', 'Emerging or urgent risk', 'Capture a new local vulnerability or an urgent change here, act on the safety, PI or sponsor route at once, and then enter it in the register. Clinical details stay in the SART or the source record.') +
     table('jt', [30, 70], None, [
         jrow('Identified by · date and time'), jrow('Source record and location'), jrow('Local risk or change identified'), jrow('Immediate response and receiving record'),
         jrow('PI notification', ck('Notified', 'Pending', 'Not required (state why)', cls='opts left')), jrow('Escalation · recipient, route and deadline'),
         jrow('Register entry', ck('New risk', 'Update of an existing risk', 'Pending review', 'Not required (state why)', cls='opts left')), jrow('Risk ID · follow-up owner and due date')]))
K = (sec('K', 'Review of the register', 'The register owner and the PI confirm that every open risk was reviewed against current evidence and that actions, triggers and communications are assigned. This does not say the risks are gone.') +
     table('kt', [25, 25, 25, 25], ['Open High or Critical (Risk IDs)', 'Accepted residual risks (Risk IDs)', 'Next scheduled review', 'Linked POT or MRL review'], [tr(td(), td(), td(), td())]) +
     '<div class="wbox kbox"><b>Open conditions and follow-up</b></div>'
     '<div class="sig2"><div class="signature"><b>Register owner</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Urgent entry and review sign-off")}<section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Urgent entry and review sign-off", 7)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:52px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.purpose th{text-align:center}.purpose td{font-size:9px;padding:4px 7px;vertical-align:top;text-align:left;height:44px}.purpose td:first-child{font-weight:400;color:inherit;background:none}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.code{font-weight:700;color:#173c67;font-size:8.8px}
th{text-align:center!important}
.note{margin-top:6px;font-size:8.8px;color:#33475b;border-left:3px solid var(--navy);padding:4px 8px;background:#f7f9fb;line-height:1.3}
.bt td{height:50px;font-size:8.8px;padding:3px 6px}
.ct td{height:29px;font-size:8.6px;padding:2px 6px}
.dt td{height:46px;font-size:8.4px;padding:2px 6px;line-height:1.2}
.pt{margin-top:6px}.pt td{height:46px;font-size:8.4px;padding:3px 6px;vertical-align:top;line-height:1.2}
.et td{height:120px;font-size:8.8px;padding:4px 7px;line-height:1.25;vertical-align:top}
.ft td{height:87px;font-size:8.8px;padding:3px 7px;line-height:1.25}
.gt td{height:96px;font-size:8.6px;padding:2px 5px}.gt .opts{font-size:7.8px}.gt th{font-size:8.2px}
.lab{display:block;font-size:7.8px;color:#5f6670}.lab.f2{margin-top:16px}
.ht td{height:96px;font-size:8.6px;padding:2px 5px}.ht .opts,.it .opts{font-size:7.8px;line-height:1.15}.ht th,.it th{font-size:8.2px}
.it td{height:69px;font-size:8.6px;padding:2px 5px}
.jt td{height:48px;font-size:8.8px;padding:3px 6px}
.kt td{height:40px}.wbox.kbox{min-height:180px}
.sig2 .signature{min-height:100px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
