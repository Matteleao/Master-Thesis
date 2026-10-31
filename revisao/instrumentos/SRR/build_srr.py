# SRR v1.0 (blank), from the author's v0.2, the Codex analysis (v0.91) and the thesis (4.3, 4.3.1, Table 3.2).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>SRR v1.0 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'srr-').replace('Editor do POT', 'Editor do SRR').replace('POT', 'SRR')
V, NP = 'SRR v1.0', 6
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
lbl = lambda t, cs='': f'<td class="lbl"{cs}>{t}</td>'
# ---------- Page 1: header, A, B, C
hdr = ''.join(meta(c) for c in ['Study / protocol', 'CIP version / date', 'Site / code', 'SRR ID / revision', 'Principal Investigator', 'Register owner / role',
                                 'Sponsor risk information (ID / version)', 'Study phase', 'Date opened', 'Last review / next review', 'Current reviewer / role', 'Controlled location'])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SRR is the site\'s own record of the risks that its execution of the investigation creates: where local staffing, workflow, equipment or experience can compromise a condition that is critical to quality (CtQ). It is opened before the first participant is included, kept current until close-out, and complements the sponsor\'s risk assessment and the manufacturer\'s device risk file without copying them.</p>'
     '<p>Pages 1 and 2 are reference. The register is E and F: one row per risk, with the same Risk ID on both pages; reprint the pair when it fills. Every review of a risk goes in G, and an urgent local risk is captured in H before it enters the register. Decisions that change a risk\'s status or escalate it are signed in I; J closes each review of the register.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One local risk to one CtQ factor of this investigation.</td>'
     '<td>What threatens the factor, what risk remains with the controls in place, what happens next, who owns it and when it is reviewed again.</td>'
     '<td>CIP, sponsor risk information, local workflow and capacity; findings from the IMC, PIR, CSST, SLCT, SART and CAPA log.</td>'
     '<td>Controls for the IMP to verify; PI decisions in the POT; milestone conditions for the MRL; CAPA, sponsor and safety routes.</td></tr></tbody></table>')
cats = [('Safety / clinical event', 'Delayed safety awareness, incomplete assessment or missed reporting.', 'Participant protection and timely clinical decisions.'),
        ('Procedure / surgeon performance', 'Learning-curve drift, unplanned substitution or inconsistent technique.', 'Procedural consistency and interpretation of outcomes.'),
        ('Device accountability', 'Mixed or poorly segregated stock, missing identifiers or reconciliation gaps.', 'Component selection and participant-device traceability.'),
        ('Data / endpoint reliability', 'Missing assessment, unresolved critical query or source-to-CRF mismatch.', 'Complete, reliable and interpretable study data.'),
        ('Operational / staffing', 'No assessor on needed days, turnover, workload or unclear handover.', 'Capacity to deliver required study activities.'),
        ('Consent / eligibility', 'Wrong consent version, delayed re-consent or unsupported eligibility.', 'Participant rights and valid enrollment.'),
        ('Imaging / assessment workflow', 'Wrong projection, missed window or inconsistent assessment method.', 'Comparable and interpretable endpoint assessments.'),
        ('Vendor / external data', 'Delayed external records, inaccessible results or missing transfers.', 'Availability of safety and endpoint evidence.')]
B = (sec('B', 'Risk categories') +
     table('bt', [25, 42, 33], ['Risk category', 'Typical local vulnerability', 'What may be affected'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left')) for a, b, c in cats]))
doms = [('Site capability, readiness and capacity maintenance', 'Staff, volume, facilities, equipment, imaging and follow-up capacity'),
        ('Participant selection and baseline characterization', 'Eligibility criteria, baseline assessment, documented selection decision'),
        ('Informed consent and participant understanding', 'Consent process, version control, comprehension, re-consent on amendment'),
        ('Device management, accountability and traceability', 'Receipt, storage, use in a named participant, identifiers, reconciliation'),
        ('Procedural delivery and surgical technique standardization', 'Approach, positioning, soft tissue, intraoperative decision thresholds'),
        ('Training, credentialing and learning-curve control', 'Competency, device release, maintained authorization, learning effects'),
        ('Perioperative and postoperative care pathway and follow-up retention', 'Care pathway, visit scheduling and windows, retention'),
        ('Endpoint framework and outcome-assessment standardization', 'Assessor consistency, administration conditions, PRO timing and mode'),
        ('Imaging acquisition, interpretation and endpoint control', 'Acquisition parameters, operator consistency, local review, timing'),
        ('Safety surveillance and adverse device event management', 'Detection, classification, causality and reporting of AEs and DDs'),
        ('Data capture, source documentation and data-flow integrity', 'Source adequacy for reconstruction, source-to-record consistency'),
        ('Regulatory compliance and deviation management', 'Detection, documentation and correction of deviations')]
C = (sec('C', 'CtQ domains', 'In the register, give the domain code and write the concrete factor of this investigation that the risk threatens, with its source (CIP, sponsor risk information, local workflow). A domain name is not a factor.') +
     table('ct', [9, 45, 46], ['Code', 'CtQ domain', 'What it covers'], [tr(td(f'CtQ{i + 1}', 'cat'), td(a, 'left'), td(b, 'left')) for i, (a, b) in enumerate(doms)]))
pages.append(f'<main class="page">{top("Purpose and risk categories")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Purpose and risk categories", 1)}</main>')
# ---------- Page 2: C domains + D rating guide
rate = [('Probability', 'Unlikely or isolated vulnerability.', 'Plausible in normal site conduct.', 'Likely, recurrent or already observed.'),
        ('Safety', 'No expected effect on safety or participant protection.', 'May affect timely clinical review, protection or safety documentation.', 'May cause or hide serious harm, a serious device effect or a major safety concern.'),
        ('Procedure', 'No expected effect on the conduct of the procedure.', 'May affect consistency, documentation or protocol adherence.', 'May affect surgical appropriateness, intraoperative decisions or technique.'),
        ('Device', 'No traceability or selection concern.', 'Recoverable discrepancy or delayed reconciliation.', 'Missing or conflicting identifiers, wrong component or broken participant-device link.'),
        ('Data', 'No expected effect on critical data.', 'May affect completeness, timeliness or source-to-CRF consistency.', 'May compromise endpoint interpretation, eligibility evidence or critical data.'),
        ('Detection', 'Easy: found by routine checks before it has an effect.', 'Moderate: found only at a planned review, reconciliation or second check.', 'Difficult: may stay hidden until endpoint review, inspection or recurrence.')]
D = (sec('D', 'Risk rating guide', 'Rate with the controls already in place; a planned action does not lower a score. Write N/A, with a short reason, when a dimension does not apply. Do not average or multiply. A reportable event follows its CIP route at every priority.') +
     table('dt', [16, 28, 28, 28], ['Rating field', '1', '2', '3'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left'), td(d, 'left')) for a, b, c, d in rate]) +
     table('pt', [25, 25, 25, 25], ['Low', 'Moderate', 'High', 'Critical'], [tr(
         td('All impact dimensions are 1, probability is low and the problem is easy to detect.', 'left b1'),
         td('At least one dimension is 2, or probability is medium, but no dimension is 3 and controls appear adequate.', 'left b2'),
         td('Any dimension is 3, or the problem recurs, is poorly controlled, hard to detect or needs active PI review.', 'left b3'),
         td('Immediate or unresolved safety risk, broken participant-device link, unrecoverable endpoint data, or an event to escalate now.', 'left b4'))]))
FH = ['Risk ID', 'Date opened', 'Category', 'CtQ domain, factor and source', 'Local vulnerability and possible consequence', 'Existing controls and evidence', 'Prob.', 'Safety', 'Proc.', 'Device', 'Data', 'Detect.', 'Priority']
GW = [5, 9, 15, 18, 13, 12, 12, 9, 7]
GH = ['Risk ID', 'Risk owner (role)', 'Review trigger or threshold', 'Planned action / owner / due', 'Linked records and evidence', 'PI / sponsor route and deadline', 'Risk status', 'Action status', 'Last / next review']
pages.append(f'<main class="page">{top("CtQ domains and rating guide")}<section class="section compact">{C}</section><section class="section compact">{D}</section>{foot("CtQ domains and rating guide", 2)}</main>')
# ---------- Page 3: F (landscape)
fac = '<span class="lab">Domain:</span><span class="lab f2">Factor:</span><span class="lab f2">Source:</span>'
pri = ck('Low', 'Moderate', 'High', 'Critical', cls='opts col')
FWr = [5, 6.5, 8, 16.5, 17, 14.2, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 6.4]
F = (sec('E', 'Main register · identification and rating', 'Name the domain, the concrete factor threatened and its source; describe the local vulnerability and its consequence; list the controls already in place with their evidence; then rate. Continue the same Risk ID in F.') +
     table('ft', FWr, FH, [tr(td(), td(), td(), td(fac, 'left'), td(), td(), td(), td(), td(), td(), td(), td(), td(pri)) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Main register · identification and rating")}{strip("Register sheet no. / total")}<section class="section compact">{F}</section>{foot("Main register · identification and rating", 3)}</main>')
# ---------- Page 4: G (landscape)
G = (sec('F', 'Main register · ownership, action and status', 'Risk status says whether the risk still applies; action status says where the response stands. Implemented is not Effective until a review in G shows the control works.') +
     table('gt', GW, GH, [tr(td(), td(), td(), td(), td(), td(), td(ck('Open', 'Controlled', 'Accepted', 'Closed', cls='opts g2')), td(ck('Not started', 'In progress', 'Implemented', 'Effective', 'Not effective', cls='opts col')), td()) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Main register · ownership, action and status")}{strip("Register sheet no. / total")}<section class="section compact">{G}</section>{foot("Main register · ownership, action and status", 4)}</main>')
# ---------- Page 5: H review log, I urgent entry
H = (sec('G', 'Risk review log', 'One line per risk reviewed, at the scheduled review or when a trigger occurs. Never overwrite an earlier line.') +
     table('htl', [11, 8, 24, 15, 13, 18, 11], ['Date / reviewer', 'Risk ID', 'Trigger and evidence reviewed', 'Control effectiveness', 'Current priority and status', 'Decision / linked record', 'Next review'],
           [tr(td(), td(), td(), td(ck('Effective', 'Partly effective', 'Not effective', 'Not assessable', cls='opts col')), td(), td(), td()) for _ in range(6)]))
I = (sec('H', 'Emerging or urgent risk entry', 'Act on the safety, PI or sponsor route at once; enter the risk in the register afterwards. Clinical details stay in the SART or the source record.') +
     table('itb', [22, 28, 22, 28], None, [
         tr(lbl('Date / time identified'), td(), lbl('Detected by / role'), td()),
         tr(lbl('Category'), td(ck('Safety', 'Procedure', 'Device', 'Data / endpoint', 'Consent / eligibility', 'Imaging', 'Follow-up', 'Other', cls='opts left wrap'), 'left" colspan="3')),
         tr(lbl('Local risk identified'), td('', 'tall" colspan="3')),
         tr(lbl('Immediate containment and receiving record'), td('', 'tall" colspan="3')),
         tr(lbl('PI notified'), td(ck('Yes', 'Pending', 'Not required', cls='opts left')), lbl('Register entry'), td(ck('New risk', 'Update', 'Not required', cls='opts left'))),
         tr(lbl('Risk ID / owner / due'), td('', '" colspan="3'))]))
pages.append(f'<main class="page">{top("Review log and emerging risk")}{strip("Review log sheet no. / total")}<section class="section compact">{H}</section><section class="section compact">{I}</section>{foot("Review log and emerging risk", 5)}</main>')
# ---------- Page 6: J decision log, K certification
rules = ('<div class="rules"><b>Lower the priority:</b> only after a review in G shows the controls work; a planned or completed action is not enough. '
         '<b>Accept the residual risk:</b> no further action is proportionate; record why and keep the trigger. '
         '<b>Close the risk:</b> the condition no longer applies or the vulnerability was removed with evidence; a closed CAPA alone does not close a risk. '
         '<b>Escalate:</b> to the CAPA log when a control failed or the problem recurs; to the PI (POT) or a milestone review (MRL) when a decision or a phase gate is affected; to the sponsor when the effect may reach beyond the site or the CIP requires it; to the SART when a safety event may be involved.</div>')
J = (sec('I', 'Status and escalation decisions', 'Lowering a High or Critical risk, accepting, closing and escalating are decided and signed here; F is then updated.') + rules +
     table('jlog', [10, 8, 20, 30, 18, 14], ['Date', 'Risk ID', 'Decision', 'Rule met and evidence', 'Route / record link', 'Decided by (PI or delegate)'],
           [tr(td(), td(), td(ck('Lower priority', 'Accept residual', 'Close', 'Escalate', cls='opts col')), td(), td(), td()) for _ in range(6)]))
K = (sec('J', 'Register review certification') +
     table('ktb', [24, 26, 24, 26], None, [
         tr(lbl('Certification'), td('I confirm that the risks in this register were reviewed against current evidence and the controls in place, and that actions, triggers and communications are assigned or linked. This does not mean the risks are gone.', 'left stmt" colspan="3')),
         tr(lbl('Open High / Critical risks'), td('', '" colspan="3')),
         tr(lbl('Accepted residual risks'), td('', '" colspan="3')),
         tr(lbl('Next scheduled SRR review'), td(), lbl('Linked POT / MRL review ID'), td()),
         tr(lbl('Register owner · name / role'), td(), lbl('Signature / date'), td()),
         tr(lbl('Principal Investigator · name'), td(), lbl('Signature / date'), td())]))
pages.append(f'<main class="page">{top("Decisions and review certification")}<section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Decisions and review certification", 6)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:52px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.opts.g2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:2px 6px}.opts.wrap{flex-wrap:wrap;gap:3px 12px}
th{text-align:center!important}
td.cat{text-align:center;font-weight:400;color:#1d2a38;background:#f3f6f9!important;font-size:8.4px}
td.left{text-align:left}
.purpose th{text-align:center}.purpose td{font-size:9px;padding:4px 7px;vertical-align:top;text-align:left;height:50px}.purpose td:first-child{font-weight:400;color:inherit;background:none}
.bt td{height:60px;font-size:9.2px;padding:3px 7px}.bt th,.ct th{font-size:9px;padding:4px}
.ct td{height:28px;font-size:8.8px;padding:2px 6px}
.dt td{height:52px;font-size:8.6px;padding:3px 6px;line-height:1.22}.dt th{font-size:8.8px;padding:3px}
.pt{margin-top:6px}.pt td{height:62px;font-size:8.6px;padding:4px 6px;vertical-align:top;line-height:1.25}.pt th{font-size:8.8px;padding:3px}
td.b1{background:#e6f2e7!important}td.b2{background:#fff3cf!important}td.b3{background:#fde3cf!important}td.b4{background:#f6d6d6!important}
.exh+table{margin-top:0!important}.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:8.6px;padding:2px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:9px}
.exrow{display:grid;grid-template-columns:57fr 43fr;gap:8px}
.ex td{height:66px;font-size:8.4px;padding:2px 5px;line-height:1.22}.ex.exf td{height:66px}.ex th{font-size:7.8px;padding:2px}
.lab{display:block;font-size:7.6px;color:#5f6670;text-align:left}.lab.f2{margin-top:12px}
.ft td{height:69px;font-size:8.6px;padding:2px 5px}.ft th,.gt th{font-size:8.2px}
.gt td{height:69px;font-size:8.6px;padding:2px 5px}.gt .opts,.htl .opts,.ft .opts,.jlog .opts{font-size:7.6px;line-height:1.15}
.htl td{height:67px;font-size:8.6px;padding:2px 5px}.htl th{font-size:8.4px}
td.lbl{background:#3a78b5!important;color:#fff;font-size:8.4px;text-align:center;font-weight:600;padding:3px 6px}
.itb td{height:40px;font-size:8.4px;padding:3px 6px}.itb td.tall{height:78px}.itb .opts{font-size:8px}
.rules{border:1px solid var(--grid);background:#f7f9fb;padding:5px 8px;font-size:8.4px;line-height:1.35;color:#1d2a38;margin-top:5px}.rules b{color:#173c67}
.jlog{margin-top:5px}.jlog td{height:70px;font-size:8.4px;padding:2px 5px}
.ktb td{height:52px;font-size:8.4px;padding:3px 6px}.ktb td.stmt{line-height:1.3;height:52px}
.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
