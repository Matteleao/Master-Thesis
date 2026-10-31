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
lbl = lambda t, cs='': f'<td class="lbl"{cs}>{t}</td>'
# ---------- Page 1: header, A, B CtQ profile
hdr = ''.join(meta(c) for c in ['Study / protocol', 'CIP version / date', 'Site / code', 'SRR ID / revision', 'Principal Investigator', 'Register owner / role',
                                 'Sponsor risk information (ID / version)', 'Study phase', 'Date opened', 'Last review / next review', 'Current reviewer / role', 'Controlled location'])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SRR is the site\'s own record of the risks that its execution of the investigation creates: where local staffing, workflow, equipment or experience can compromise a condition that is critical to quality (CtQ). It is opened before the first participant is included, kept current until close-out, and complements the sponsor\'s risk assessment and the manufacturer\'s device risk file without copying them.</p>'
     '<p>Start with B: turn each CtQ domain into the concrete factors this investigation must protect. Each risk in the register (F and G, one row per risk, same Risk ID on both pages) cites the factor it threatens. Every review of a risk goes in H; an urgent local risk is captured in I before it enters the register. C, D and E are reference; J sets how a risk changes status or is escalated; K closes each review of the register.</p></div>')
doms = [('Site capability, readiness and capacity', 'Staff, volume, facilities, equipment, follow-up capacity'),
        ('Participant selection and baseline characterization', 'Eligibility, baseline assessment, selection decision'),
        ('Informed consent and participant understanding', 'Consent process, version control, re-consent'),
        ('Device management, accountability and traceability', 'Storage, use in a named participant, identifiers, reconciliation'),
        ('Procedural delivery and surgical technique', 'Approach, positioning, intraoperative decision thresholds'),
        ('Training, credentialing and learning-curve control', 'Competency, device release, learning effects'),
        ('Care pathway and follow-up retention', 'Postoperative pathway, visit windows, retention'),
        ('Endpoint framework and outcome assessment', 'Assessor consistency, PRO timing and mode'),
        ('Imaging acquisition, interpretation and endpoint control', 'Acquisition, operator consistency, local review, timing'),
        ('Safety surveillance and adverse device events', 'Detection, classification, causality, reporting'),
        ('Data capture, source documentation and data flow', 'Source adequacy, source-to-record consistency'),
        ('Regulatory compliance and deviation management', 'Detection, documentation and correction of deviations')]
B = (sec('B', 'CtQ profile of this investigation', 'For each domain, write the factors this investigation must protect, as conditions that can be checked in daily work (for example: "every implanted component is reconciled to the participant before case closure"). Give each factor an ID (4.1, 4.2…) and its source: CIP section, sponsor risk item or local workflow. Mark a domain that does not apply and say why.') +
     table('bp', [6, 27, 8, 7, 37, 15], ['Code', 'CtQ domain', 'Applies?', 'Factor ID', 'Factor to protect in this investigation', 'Source'],
           [tr(td(f'CtQ{i + 1}', 'cat'), td(f'<b>{a}</b><span class="sub">{b}</span>', 'left dom'), td(ck('Yes', 'No', cls='opts col')), td(), td(), td()) for i, (a, b) in enumerate(doms)]))
pages.append(f'<main class="page">{top("Purpose and CtQ profile")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Purpose and CtQ profile", 1)}</main>')
# ---------- Page 2: C categories, D rating guide
cats = [('Safety / clinical event', 'Delayed safety awareness, incomplete assessment or missed reporting.', 'Participant protection and timely clinical decisions.'),
        ('Procedure / surgeon performance', 'Learning-curve drift, unplanned substitution or inconsistent technique.', 'Procedural consistency and interpretation of outcomes.'),
        ('Device accountability', 'Mixed or poorly segregated stock, missing identifiers or reconciliation gaps.', 'Component selection and participant-device traceability.'),
        ('Data / endpoint reliability', 'Missing assessment, unresolved critical query or source-to-CRF mismatch.', 'Complete, reliable and interpretable study data.'),
        ('Operational / staffing', 'No assessor on needed days, turnover, workload or unclear handover.', 'Capacity to deliver required study activities.'),
        ('Consent / eligibility', 'Wrong consent version, delayed re-consent or unsupported eligibility.', 'Participant rights and valid enrollment.'),
        ('Imaging / assessment workflow', 'Wrong projection, missed window or inconsistent assessment method.', 'Comparable and interpretable endpoint assessments.'),
        ('Vendor / external data', 'Delayed external records, inaccessible results or missing transfers.', 'Availability of safety and endpoint evidence.')]
C = (sec('C', 'Risk categories', 'The category says where in local operations the risk sits; the factor (B) says what it threatens.') +
     table('bt', [25, 42, 33], ['Risk category', 'Typical local vulnerability', 'What may be affected'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left')) for a, b, c in cats]))
rate = [('Probability', 'Unlikely or isolated vulnerability.', 'Plausible in normal site conduct.', 'Likely, recurrent or already observed.'),
        ('Safety', 'No expected effect on safety or participant protection.', 'May affect timely clinical review, protection or safety documentation.', 'May cause or hide serious harm, a serious device effect or a major safety concern.'),
        ('Procedure', 'No expected effect on the conduct of the procedure.', 'May affect consistency, documentation or protocol adherence.', 'May affect surgical appropriateness, intraoperative decisions or technique.'),
        ('Device', 'No traceability or selection concern.', 'Recoverable discrepancy or delayed reconciliation.', 'Missing or conflicting identifiers, wrong component or broken participant-device link.'),
        ('Data', 'No expected effect on critical data.', 'May affect completeness, timeliness or source-to-CRF consistency.', 'May compromise endpoint interpretation, eligibility evidence or critical data.'),
        ('Detection', 'Easy: found by routine checks before it has an effect.', 'Moderate: found only at a planned review, reconciliation or second check.', 'Difficult: may stay hidden until endpoint review, inspection or recurrence.')]
D = (sec('D', 'Risk rating guide', 'Rate with the controls already in place; a planned action does not lower a score. Write N/A, with a short reason, when a dimension does not apply. Do not average or multiply.') +
     table('dt', [15, 28.3, 28.3, 28.4], ['Rating field', '1', '2', '3'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left'), td(d, 'left')) for a, b, c, d in rate]) +
     table('pt', [25, 25, 25, 25], ['Low', 'Moderate', 'High', 'Critical'], [tr(
         td('All impact dimensions are 1, probability is low and the problem is easy to detect. No PI escalation normally needed.', 'left b1'),
         td('At least one dimension is 2, or probability is medium, but no dimension is 3 and the controls in place appear adequate.', 'left b2'),
         td('Any dimension is 3, or the problem recurs, is poorly controlled or hard to detect, or needs active PI review.', 'left b3'),
         td('Immediate or unresolved safety risk, broken participant-device link, unrecoverable endpoint data, or an event that must be escalated now.', 'left b4'))]) +
     '<div class="note">A reportable event follows its CIP route at every priority; reporting never waits for the SRR.</div>')
pages.append(f'<main class="page">{top("Risk categories and rating guide")}<section class="section compact">{C}</section><section class="section compact">{D}</section>{foot("Risk categories and rating guide", 2)}</main>')
# ---------- Page 3: E worked example (landscape)
FW = [5, 6.5, 8, 7, 22, 21, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 8.5]
FH = ['Risk ID', 'Date opened', 'Category', 'CtQ factor (B)', 'Local vulnerability and possible consequence', 'Existing controls and evidence', 'Prob.', 'Safety', 'Proc.', 'Device', 'Data', 'Detect.', 'Current priority']
GW = [5, 9, 15, 18, 13, 12, 12, 9, 7]
GH = ['Risk ID', 'Risk owner (role)', 'Review trigger or threshold', 'Planned action / owner / due', 'Linked records and evidence', 'PI / sponsor route and deadline', 'Risk status', 'Action status', 'Last / next review']
exF = tr(td('SRR-003'), td('28 Jun 2026'), td('Device accountability'), td('4.1'), td('UDI is copied from the OR team without a second check; a missing or wrong UDI may not be caught before case closure and the participant-device link breaks.'), td('OR sticker sheet; accountability log; same-day reconciliation by the coordinator (cases 001-005).'), td('2'), td('2'), td('2'), td('3'), td('3'), td('2'), td('High', 'b3'))
exG = tr(td('SRR-003'), td('Study coordinator'), td('Any missing or conflicting UDI; reconciliation after 24 h'), td('Second-person UDI check before case closure · QA lead · 15 Jul'), td('CAPA-014-002; IMP check 4'), td('PI informed 28 Jun; no sponsor route'), td('Open'), td('In progress'), td('28 Jun / 31 Jul'))
exH = tr(td('31 Jul · QA lead'), td('SRR-003'), td('Scheduled review; IMC-014-03 and ICDL cases 006-007: second check done in both'), td('Effective'), td('Moderate · Controlled'), td('Lower to Moderate; keep the trigger, the risk still applies'), td('31 Oct'))
E = (sec('E', 'Worked example: how one risk entry is completed', 'Factor 4.1 in B: "every implanted component is reconciled to the participant before case closure". The same Risk ID runs through F, G and H. After the review showed the new check works, the priority fell from High to Moderate; the risk stays Controlled, not Closed.') +
     '<div class="exh">F · Identification and rating</div>' + table('ex exf', FW, FH, [exF]) +
     '<div class="exh">G · Ownership, action and status</div>' + table('ex', GW, GH, [exG]) +
     '<div class="exh">H · Review</div>' + table('ex', [10, 6, 30, 11, 13, 22, 8], ['Date / reviewer', 'Risk ID', 'Trigger and evidence reviewed', 'Control effectiveness', 'Current priority and status', 'Decision / linked record', 'Next review'], [exH]))
pages.append(f'<main class="page landscape">{top("Worked example")}<section class="section compact">{E}</section>{foot("Worked example", 3)}</main>')
# ---------- Page 4: F register identification and rating (landscape)
pri = ck('Low', 'Moderate', 'High', 'Critical', cls='opts col')
F = (sec('F', 'Main register · identification and rating', 'Cite the factor ID from B, describe the local vulnerability and its consequence, list the controls already in place with their evidence, then rate. Continue the same Risk ID in G.') +
     table('ft', FW, FH, [tr(td(), td(), td(), td(), td(), td(), td(), td(), td(), td(), td(), td(), td(pri)) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Main register · identification and rating")}{strip("Register sheet no. / total")}<section class="section compact">{F}</section>{foot("Main register · identification and rating", 4)}</main>')
# ---------- Page 5: G register ownership (landscape)
G = (sec('G', 'Main register · ownership, action and status', 'Risk status says whether the risk still applies; action status says where the response stands. Implemented is not Effective until a review in H shows the control works.') +
     table('gt', GW, GH, [tr(td(), td(), td(), td(), td(), td(), td(ck('Open', 'Controlled', 'Accepted', 'Closed', cls='opts g2')), td(ck('Not started', 'In progress', 'Implemented', 'Effective', 'Not effective', cls='opts col')), td()) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Main register · ownership, action and status")}{strip("Register sheet no. / total")}<section class="section compact">{G}</section>{foot("Main register · ownership, action and status", 5)}</main>')
# ---------- Page 6: H review log, I urgent entry
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
pages.append(f'<main class="page">{top("Review log and emerging risk")}{strip("Review log sheet no. / total")}<section class="section compact">{H}</section><section class="section compact">{I}</section>{foot("Review log and emerging risk", 6)}</main>')
# ---------- Page 7: J status changes and escalation, K certification
chg = [('Lower the priority', 'Controls are implemented and a review in H shows they work. Re-rate every field; keep the trigger.', 'A planned or completed action without a review.', 'PI for High or Critical; register owner for Moderate.'),
       ('Accept the residual risk', 'No further action is proportionate. Record the reason, keep the trigger and set the next review.', '"No further action" with no reason.', 'PI; may delegate Low and Moderate.'),
       ('Close the risk', 'The condition no longer applies: the phase ended, the process changed or the vulnerability was removed with evidence.', 'A closed CAPA; time passing without events.', 'PI if it ever touched safety, traceability, endpoint data or a CAPA.')]
esc = [('CAPA log', 'A control failed, the problem recurred or is systemic, or the response needs several steps and an effectiveness check.', 'CAPA ID in G'),
       ('PI decision (POT)', 'Priority, acceptance, restriction, resources or oversight intensity needs the PI.', 'POT entry in G'),
       ('Milestone review (MRL)', 'The risk bears on starting, continuing or closing a phase.', 'MRL entry in G'),
       ('Sponsor or CRO', 'The effect may reach beyond the site, or the CIP or a sponsor threshold requires it, even before an event.', 'Communication reference in G'),
       ('Safety record (SART)', 'The risk has produced, or may hide, a safety event or device deficiency.', 'SART ID in I or G')]
J = (sec('J', 'Changing a risk\'s status and escalating it', 'Every decision is entered in H with its evidence; G is then updated.') +
     '<div class="exh">Status changes</div>' + table('jtb', [20, 38, 22, 20], ['Decision', 'Allowed when', 'Not enough on its own', 'Who decides'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left'), td(d, 'left')) for a, b, c, d in chg]) +
     '<div class="exh">Escalation routes</div>' + table('jtb2', [20, 58, 22], ['Route', 'Use when', 'Where it is linked'], [tr(td(a, 'cat'), td(b, 'left'), td(c, 'left')) for a, b, c in esc]))
K = (sec('K', 'Register review certification') +
     table('ktb', [24, 26, 24, 26], None, [
         tr(lbl('Certification'), td('I confirm that the risks in this register were reviewed against current evidence and the controls in place, and that actions, triggers and communications are assigned or linked. This does not mean the risks are gone.', 'left stmt" colspan="3')),
         tr(lbl('Open High / Critical risks'), td('', '" colspan="3')),
         tr(lbl('Accepted residual risks'), td('', '" colspan="3')),
         tr(lbl('Open conditions and follow-up'), td('', 'tall" colspan="3')),
         tr(lbl('Next scheduled SRR review'), td(), lbl('Linked POT / MRL review ID'), td()),
         tr(lbl('Register owner · name / role'), td(), lbl('Signature / date'), td()),
         tr(lbl('Principal Investigator · name'), td(), lbl('Signature / date'), td())]))
pages.append(f'<main class="page">{top("Decision rules and review certification")}<section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Decision rules and review certification", 7)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:40px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:1px 0}
.opts.g2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:2px 6px}.opts.wrap{flex-wrap:wrap;gap:3px 12px}
th{text-align:center!important}
td.cat{text-align:center;font-weight:400;color:#1d2a38;background:#f3f6f9!important;font-size:8.4px}
td.left{text-align:left}td.dom b{display:block;font-size:8.4px;color:#173c67}.sub{display:block;font-size:7.6px;color:#5f6670;margin-top:1px}
.bp td{height:43px;font-size:8.4px;padding:2px 5px}.bp th{font-size:8.6px;padding:3px}.bp .opts{font-size:7.8px}
.bt td{height:34px;font-size:8.4px;padding:2px 6px}.bt th{font-size:8.6px;padding:3px}
.dt td{height:54px;font-size:8.4px;padding:2px 6px;line-height:1.2}
.pt{margin-top:6px}.pt td{height:70px;font-size:8.4px;padding:4px 6px;vertical-align:top;line-height:1.25}
td.b1{background:#e6f2e7!important}td.b2{background:#fff3cf!important}td.b3{background:#fde3cf!important}td.b4{background:#f6d6d6!important}
.note{margin-top:6px;font-size:8.8px;color:#33475b;border-left:3px solid var(--navy);padding:4px 8px;background:#f7f9fb;line-height:1.3}
.exh+table{margin-top:0!important}.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9px;padding:3px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:14px}
.ex td{height:115px;font-size:9px;padding:3px 6px;line-height:1.28}.ex.exf td{height:140px}.ex th{font-size:8.2px;padding:3px 2px}
.ft td{height:69px;font-size:8.6px;padding:2px 5px}.ft th,.gt th{font-size:8.2px}
.gt td{height:69px;font-size:8.6px;padding:2px 5px}.gt .opts,.htl .opts,.ft .opts{font-size:7.6px;line-height:1.15}
.htl td{height:67px;font-size:8.6px;padding:2px 5px}.htl th{font-size:8.4px}
td.lbl{background:#3a78b5!important;color:#fff;font-size:8.4px;text-align:center;font-weight:600;padding:3px 6px}
.itb td{height:40px;font-size:8.4px;padding:3px 6px}.itb td.tall{height:78px}.itb .opts{font-size:8px}
.jtb td,.jtb2 td{height:38px;font-size:8.4px;padding:3px 6px;line-height:1.22}
.ktb td{height:46px;font-size:8.4px;padding:3px 6px}.ktb td.stmt{line-height:1.3;height:52px}.ktb td.tall{height:140px}
.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
