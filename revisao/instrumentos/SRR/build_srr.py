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
# ---------- Page 1: header, A, B, triggers, C
hdr = ''.join(meta(c) for c in ['Study / protocol', 'CIP version / date', 'Site / code', 'SRR ID / revision', 'Principal Investigator', 'Register owner / role',
                                 'Sponsor risk information (ID / version)', 'Study phase', 'Date opened', 'Last review / next review', 'Current reviewer / role', 'Controlled location'])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SRR is the site\'s own record of the risks that its execution of the investigation creates: where local staffing, workflow, equipment or experience can compromise a condition that is critical to quality (CtQ) for this investigation. It is opened before the first participant is included, kept current until close-out, and complements the sponsor\'s risk assessment and the manufacturer\'s device risk file without copying them.</p>'
     '<p>Pages 1 and 2 are reference, with a worked example. The register is F and G: one row per risk, with the same Risk ID on both pages; reprint the pair when it fills. Every review of a risk goes in H, and an urgent local risk is captured in I before it enters the register. J sets the rules for lowering, accepting, closing and escalating a risk; K closes each review of the register.</p></div>')
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
trg = ['Repeated protocol deviations', 'Missed assessment or visit window', 'Delayed safety reporting', 'Device discrepancy or wrong selection', 'Learning-curve or performance signal',
       'Monitoring or audit finding', 'Recurrent or ineffective action', 'Staffing, training or capacity change', 'CIP, device or workflow change']
T = ('<div class="trg"><div class="trg-h">Common review triggers</div><div class="trg-g">' + ''.join(f'<span>{t}</span>' for t in trg) + '</div></div>')
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
C = (sec('C', 'CtQ domains and the factor to protect', 'In the register, give the domain code and write in one sentence the factor this investigation must protect, with its source (CIP, sponsor risk information, local workflow). A domain name is not a factor.') +
     table('ct', [9, 45, 46], ['Code', 'CtQ domain', 'What it covers'], [tr(td(f'CtQ{i + 1}', 'cat'), td(a, 'left'), td(b, 'left')) for i, (a, b) in enumerate(doms)]))
pages.append(f'<main class="page">{top("Purpose, categories and CtQ domains")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}{T}</section><section class="section compact">{C}</section>{foot("Purpose, categories and CtQ domains", 1)}</main>')
# ---------- Page 2: D rating guide, E worked example (landscape)
rate = [('Probability (P)', 'Low: unlikely or isolated vulnerability.', 'Medium: plausible in normal site conduct.', 'High: likely, recurrent or already observed.'),
        ('Safety (S)', 'No expected effect on safety or participant protection.', 'May affect timely clinical review, protection or safety documentation.', 'May cause or hide serious harm, a serious device effect or a major safety concern.'),
        ('Procedure (Pr)', 'No expected effect on the conduct of the procedure.', 'May affect consistency, documentation or protocol adherence.', 'May affect surgical appropriateness, intraoperative decisions or technique.'),
        ('Device (Dv)', 'No traceability or selection concern.', 'Recoverable discrepancy or delayed reconciliation.', 'Missing or conflicting identifiers, wrong component or broken participant-device link.'),
        ('Data (Da)', 'No expected effect on critical data.', 'May affect completeness, timeliness or source-to-CRF consistency.', 'May compromise endpoint interpretation, eligibility evidence or critical data.'),
        ('Detection (D)', 'Easy: found by routine checks before it has an effect.', 'Moderate: found only at a planned review, reconciliation or second check.', 'Difficult: may stay hidden until endpoint review, inspection or recurrence.')]
D = (sec('D', 'Risk rating guide', 'Rate with the controls already in place; a planned action does not lower a score. Use N/A, with a short reason, when a dimension does not apply; N/A is not 1. Do not average or multiply: the highest applicable field sets the band.') +
     table('dt', [14, 28.6, 28.7, 28.7], ['Rating field', '1', '2', '3'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left'), td(d, 'left')) for a, b, c, d in rate]) +
     table('pt', [25, 25, 25, 25], ['Low', 'Moderate', 'High', 'Critical'], [tr(
         td('Every applicable field is 1.', 'left b1'), td('The highest applicable field is 2.', 'left b2'), td('Any applicable field is 3.', 'left b3'),
         td('A condition, not a score: unresolved serious safety threat, broken participant-device link, unrecoverable endpoint data, or a threshold the study defines as critical. Reporting follows the CIP at every band.', 'left b4'))]))
exF = tr(td('SRR-003'), td('28 Jun 2026'), td('Device accountability'), td('CtQ4 · The implanted component can be reconstructed and reconciled to the participant. Source: CIP 8.3'), td('UDI copied from the OR team without a second check; a missing or wrong UDI may not be caught before case closure.'), td('OR sticker sheet; accountability log; same-day reconciliation (cases 001-005).'), td('2'), td('2'), td('2'), td('3'), td('3'), td('2'), td('High', 'b3'))
exG = tr(td('SRR-003'), td('Study coordinator'), td('Any missing or conflicting UDI; reconciliation after 24 h'), td('Second-person check before case closure · QA lead · 15 Jul'), td('CAPA-014-002; IMC check 4'), td('PI aware; no sponsor route'), td('Open'), td('In progress'), td('28 Jun / 31 Jul'))
exH = tr(td('31 Jul · QA lead'), td('SRR-003'), td('Scheduled · IMC-014-03, ICDL cases 006-007'), td('Effective'), td('Moderate · Controlled'), td('Keep trigger; the risk still applies'), td('31 Oct'))
E = (sec('E', 'Worked example: how one risk entry is completed', 'The same Risk ID runs through F, G and H. The check lowered the band from High to Moderate after a review showed it works; the risk stays Controlled, not Closed.') +
     '<div class="exh">F · Identification and rating</div>' + table('ex', [5, 6, 8, 16, 17, 15, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 12], ['Risk ID', 'Date opened', 'Category', 'CtQ domain, factor and source', 'Local vulnerability and consequence', 'Existing controls and evidence', 'P', 'S', 'Pr', 'Dv', 'Da', 'D', 'Current priority'], [exF]) +
     '<div class="exh">G · Ownership, action and status</div>' + table('ex', [5, 9, 15, 17, 12, 11, 8, 10, 13], ['Risk ID', 'Risk owner', 'Review trigger', 'Planned action / owner / due', 'Linked records', 'PI / sponsor route', 'Risk status', 'Action status', 'Last / next review'], [exG]) +
     '<div class="exh">H · Review</div>' + table('ex', [10, 7, 25, 12, 14, 22, 10], ['Date / reviewer', 'Risk ID', 'Trigger and evidence reviewed', 'Control effectiveness', 'Current priority and status', 'Decision / linked record', 'Next review'], [exH]))
pages.append(f'<main class="page landscape">{top("Rating guide and worked example")}<section class="section compact">{D}</section><section class="section compact">{E}</section>{foot("Rating guide and worked example", 2)}</main>')
# ---------- Page 3: F register identification and rating (landscape)
fac = '<span class="lab">Domain:</span><span class="lab f2">Factor / source:</span>'
pri = ck('Low', 'Moderate', 'High', 'Critical', cls='opts g2')
F = (sec('F', 'Main register · identification and rating', 'Complete this page first, then continue the same Risk ID in G.') +
     table('ft', [5, 6, 8, 17, 18, 15, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 10], ['Risk ID', 'Date opened', 'Category', 'CtQ domain, factor and source', 'Local vulnerability and possible consequence', 'Existing controls and evidence', 'P', 'S', 'Pr', 'Dv', 'Da', 'D', 'Current priority'],
           [tr(td(), td(), td(), td(fac, 'left'), td(), td(), td(), td(), td(), td(), td(), td(), td(pri)) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Main register · identification and rating")}{strip("Register sheet no. / total")}<section class="section compact">{F}</section>{foot("Main register · identification and rating", 3)}</main>')
# ---------- Page 4: G register ownership (landscape)
G = (sec('G', 'Main register · ownership, action and status', 'Risk status says whether the risk still applies; action status says where the response stands. Implemented is not Effective until a review in H shows the control works.') +
     table('gt', [5, 9, 15, 17, 12, 11, 10, 12, 9], ['Risk ID', 'Risk owner (role)', 'Review trigger or threshold', 'Planned action / owner / due', 'Linked records and evidence', 'PI / sponsor route and deadline', 'Risk status', 'Action status', 'Last / next review'],
           [tr(td(), td(), td(), td(), td(), td(), td(ck('Open', 'Controlled', 'Accepted', 'Closed', cls='opts g2')), td(ck('Not started', 'In progress', 'Implemented', 'Effective', 'Not effective', cls='opts col')), td()) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Main register · ownership, action and status")}{strip("Register sheet no. / total")}<section class="section compact">{G}</section>{foot("Main register · ownership, action and status", 4)}</main>')
# ---------- Page 5: H review log, I urgent entry
H = (sec('H', 'Risk review log', 'One line per risk reviewed, at the scheduled review or when a trigger occurs. Never overwrite an earlier line.') +
     table('htl', [11, 8, 24, 15, 13, 18, 11], ['Date / reviewer', 'Risk ID', 'Trigger and evidence reviewed', 'Control effectiveness', 'Current priority and status', 'Decision / linked record', 'Next review'],
           [tr(td(), td(), td(), td(ck('Effective', 'Partly effective', 'Not effective', 'Not assessable', cls='opts col')), td(), td(), td()) for _ in range(6)]))
I = (sec('I', 'Emerging or urgent risk entry', 'Act on the safety, PI or sponsor route at once; enter the risk in the register afterwards. Clinical details stay in the SART or the source record.') +
     table('itb', [22, 28, 22, 28], None, [
         tr(lbl('Date / time identified'), td(), lbl('Detected by / role'), td()),
         tr(lbl('Category'), td(ck('Safety', 'Procedure', 'Device', 'Data / endpoint', 'Consent / eligibility', 'Imaging', 'Follow-up', 'Other', cls='opts left wrap'), 'left" colspan="3')),
         tr(lbl('Local risk identified'), td('', 'tall" colspan="3')),
         tr(lbl('Immediate containment and receiving record'), td('', 'tall" colspan="3')),
         tr(lbl('PI notified'), td(ck('Yes', 'Pending', 'Not required', cls='opts left')), lbl('Register entry'), td(ck('New risk', 'Update', 'Not required', cls='opts left'))),
         tr(lbl('Risk ID / owner / due'), td('', '" colspan="3'))]))
pages.append(f'<main class="page">{top("Review log and emerging risk")}{strip("Review log sheet no. / total")}<section class="section compact">{H}</section><section class="section compact">{I}</section>{foot("Review log and emerging risk", 5)}</main>')
# ---------- Page 6: J decisions, K certification
dec = [('Lower the priority', 'Controls implemented and a review in H shows they work; every field re-rated; the trigger kept.', 'Yes for High or Critical; at the oversight review for Moderate.'),
       ('Accept the residual risk', 'No further action is proportionate; reason, owner, active trigger and next review recorded.', 'Yes; the PI may delegate Low and Moderate.'),
       ('Close the risk', 'The condition no longer applies: phase ended, process changed or vulnerability removed with evidence. A closed CAPA alone does not close a risk.', 'Yes if the risk ever touched safety, traceability, endpoint data or a CAPA.'),
       ('Escalate to the CAPA log', 'Control failed, problem recurred or is systemic, or the action needs several steps and an effectiveness check.', 'Yes.'),
       ('Escalate to the POT or MRL', 'A PI decision on priority, acceptance, restriction, resources or oversight, or a bearing on a phase gate.', 'Yes.'),
       ('Escalate to the sponsor or CRO', 'The effect may reach beyond the site, or the CIP or a sponsor threshold requires it, even before an event.', 'Yes, within the CIP route and timing.')]
J = (sec('J', 'Lowering, accepting, closing and escalating') +
     table('jtb', [21, 47, 20, 12], ['Decision', 'Minimum evidence', 'PI review needed?', 'Record link'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left'), td()) for a, b, c in dec]))
K = (sec('K', 'Register review certification') +
     table('ktb', [24, 26, 24, 26], None, [
         tr(lbl('Certification'), td('I confirm that the risks in this register were reviewed against current evidence and the controls in place, and that actions, triggers and communications are assigned or linked. This does not mean the risks are gone.', 'left stmt" colspan="3')),
         tr(lbl('Open High / Critical risks'), td('', '" colspan="3')),
         tr(lbl('Accepted residual risks'), td('', '" colspan="3')),
         tr(lbl('Open conditions and follow-up'), td('', 'tall" colspan="3')),
         tr(lbl('Next scheduled SRR review'), td(), lbl('Linked POT / MRL review ID'), td()),
         tr(lbl('Register owner · name / role'), td(), lbl('Signature / date'), td()),
         tr(lbl('Principal Investigator · name'), td(), lbl('Signature / date'), td())]))
pages.append(f'<main class="page">{top("Decision criteria and review certification")}<section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Decision criteria and review certification", 6)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:44px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.opts.g2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:2px 8px}.opts.wrap{flex-wrap:wrap;gap:3px 12px}
th{text-align:center!important}
td.cat{text-align:center;font-weight:400;color:#1d2a38;background:#f3f6f9!important;font-size:8.4px}
td.left{text-align:left}
.bt td{height:18px;font-size:8.2px;padding:2px 6px}.bt th,.ct th{font-size:8.6px;padding:3px}
.trg{border:1px solid var(--grid);margin-top:6px}.trg-h{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9.4px;padding:4px 8px;border-bottom:1px solid var(--grid)}
.trg-g{display:grid;grid-template-columns:repeat(3,1fr)}.trg-g span{font-size:8.2px;padding:3px 8px;border-bottom:1px solid var(--grid);border-right:1px solid var(--grid)}.trg-g span:nth-child(3n){border-right:0}
.ct td{height:18px;font-size:8.2px;padding:1px 6px}
.dt td{height:24px;font-size:8.2px;padding:2px 6px;line-height:1.2}
.pt{margin-top:5px}.pt td{height:34px;font-size:8.2px;padding:3px 6px;vertical-align:top;line-height:1.2}
.pt th:nth-child(1){background:#4e8a5c}.pt th:nth-child(2){background:#b38a1f}.pt th:nth-child(3){background:#c26a2f}.pt th:nth-child(4){background:#a83c3c}
td.b1{background:#e6f2e7!important}td.b2{background:#fff3cf!important}td.b3{background:#fde3cf!important}td.b4{background:#f6d6d6!important}
.exh+table{margin-top:0!important}.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9px;padding:3px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:5px}
.ex td{height:34px;font-size:7.8px;padding:2px 4px;line-height:1.18}.ex th{font-size:7.8px;padding:2px}
.ft td{height:69px;font-size:8.6px;padding:2px 5px}.ft th,.gt th{font-size:8.2px}
.lab{display:block;font-size:7.6px;color:#5f6670;text-align:left}.lab.f2{margin-top:14px}
.gt td{height:60px;font-size:8.6px;padding:2px 5px}.gt .opts,.htl .opts,.ft .opts{font-size:7.6px;line-height:1.15}
.htl td{height:67px;font-size:8.6px;padding:2px 5px}.htl th{font-size:8.4px}
td.lbl{background:#3a78b5!important;color:#fff;font-size:8.4px;text-align:center;font-weight:600;padding:3px 6px}
.itb td{height:40px;font-size:8.4px;padding:3px 6px}.itb td.tall{height:78px}.itb .opts{font-size:8px}
.jtb td{height:46px;font-size:8.4px;padding:3px 6px;line-height:1.22}
.ktb td{height:62px;font-size:8.4px;padding:3px 6px}.ktb td.stmt{line-height:1.3;height:60px}.ktb td.tall{height:150px}
.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
