# SIRR v0.6 (blank) from v0.4, the Codex v0.5 alternative and the Codex analysis.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>SIRR v0.6 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'sirr-').replace('Editor do POT', 'Editor do SIRR').replace('POT', 'SIRR')
V, NP = 'SIRR v0.6', 5
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">SIRR - Site Imaging Readiness Record</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">SIRR · v0.6</div></header>')
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
pages = []
# ---------- Page 1: header, A, B, C
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('SIRR ID / revision'),
               meta('Assessment type', ck('Initial', 'Reassessment', cls='opts left')), meta('Assessment date'), meta('Imaging charter or manual / version / effective date', cls=' span2'),
               meta('Charter received / confirmed by / date'), meta('Reassessment trigger (if any)'), meta('Radiology contact / role'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SIRR records whether the site can carry out the imaging the sponsor\'s charter requires before the first participant is imaged. Each requirement of the charter is mapped to the local equipment, workflow and people that will deliver it (D to G), gaps get an action (H), and the site concludes whether it can submit its readiness to the sponsor or CRO (I). The charter stays under sponsor control: a requirement the site cannot meet is recorded as a gap or a question, never rewritten.</p>'
     '<p>The SIRR is about the local arrangement, not about any single image set, which is judged in the Image Quality Log (IQL). Signatures attest the site\'s self-assessment; they do not activate the site, which stays a sponsor decision referenced in K.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>The site\'s imaging arrangement for one version of the sponsor\'s charter.</td>'
     '<td>Whether the site can submit its readiness for sponsor or CRO review, and with which limits.</td>'
     '<td>CIP, imaging charter or manual, equipment records, transfer test, delegation and training records.</td>'
     '<td>Requirement IDs that the IQL cites, gaps and actions, the site conclusion, and the reassessment history.</td></tr></tbody></table>')
B = (sec('B', 'What the site verifies', 'Each element is assessed in the section shown.') +
     table('bt', [24, 54, 22], ['Element', 'What the site verifies', 'Section'], [
         tr(el('Acquisition'), td('Modality, views, positioning, parameters, laterality and timing can be delivered locally.', 'left'), td('D')),
         tr(el('Equipment, transfer and archive'), td('Equipment evidence is current; images keep their identifiers through export, transfer, receipt and retrieval.', 'left'), td('E')),
         tr(el('People and review'), td('Acquisition, local review and clinical decision have named, trained people and a handoff to central review.', 'left'), td('F, G')),
         tr(el('Response to a problem image'), td('Who records, repeats, escalates and closes a limited or non-conforming image set.', 'left'), td('C, G'))]))
C = (sec('C', 'Local response to each image-set category', 'Use the sponsor\'s categories if they differ. The IQL applies this response to each image set; the SIRR only defines it.') +
     table('ct', [26, 52, 22], ['Category', 'Local response (who records, repeats, reviews, escalates)', 'Responsible role'], [
         tr(el('Acceptable<span class="sub">Complete, traceable, meets the requirement</span>'), td('', 'left'), td()),
         tr(el('Limited<span class="sub">Usable with a stated limitation</span>'), td('', 'left'), td()),
         tr(el('Non-conforming<span class="sub">Does not meet the requirement</span>'), td('', 'left'), td()),
         tr(el('Not assessable<span class="sub">Set, source or reviewer unavailable</span>'), td('', 'left'), td())]))
pages.append(f'<main class="page">{top("Assessment identification, purpose and local response")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section><section class="section compact">{C}</section>{foot("Identification, purpose and local response", 1)}</main>')
# ---------- Page 2: D mapping (landscape)
IMPL = ck('Ready', 'Partial', 'Not ready', 'N/A', cls='opts col')
EVD = ck('Adequate', 'Partial', 'Missing', cls='opts col')
D = (sec('D', 'Charter requirements and local implementation', 'One row per requirement. Keep the ID stable: the IQL, PFVR and IMC cite SIRR ID and requirement ID. Copy the requirement as written; a question to the sponsor goes to H. N/A needs the reason in the gap column.') +
     table('dt', [6, 11, 12, 21, 14, 9, 9, 11, 7], ['Req. ID', 'Charter section', 'Time point · window', 'Modality · views · positioning · parameters', 'Local equipment · workflow (ref.)', 'Implementation', 'Evidence', 'Gap · impact on readiness', 'Action ID (H)'],
           [tr(td(f'IMG-{i:02d}', 'rid'), td(), td(), td('', 'left'), td('', 'left'), td(IMPL), td(EVD), td('', 'left'), td()) for i in range(1, 9)]))
pages.append(f'<main class="page landscape">{top("Charter requirements and local implementation")}<section class="section compact">{D}</section>{foot("Charter requirements and local implementation", 2)}</main>')
# ---------- Page 3: E technical + F roles
ST = ck('Ready', 'Partial', 'Not ready', cls='opts col')
E = (sec('E', 'Equipment, transfer and archive', 'Cite the current certificate or test and its expiry. A transfer test covers identifiers, export, receipt, local retrieval and retrieval through the sponsor route when it can be tested. No images are copied here.') +
     table('et', [24, 18, 24, 12, 22], ['Control', 'Equipment or test ID', 'Current evidence · valid until', 'Status', 'Gap · action ID (H)'], [
         tr(el('Equipment and preset (1)'), td(), td('', 'left'), td(ST), td('', 'left')),
         tr(el('Equipment and preset (2)'), td(), td('', 'left'), td(ST), td('', 'left')),
         tr(el('Maintenance and calibration'), td(), td('', 'left'), td(ST), td('', 'left')),
         tr(el('Transfer and retrieval test'), td(), td('', 'left'), td(ST), td('', 'left')),
         tr(el('Local archive and display'), td(), td('', 'left'), td(ST), td('', 'left'))]))
F = (sec('F', 'People and review boundary', 'Cite the delegation and training records; this table does not authorize anyone. Sponsor central review and endpoint adjudication keep their own authority.') +
     table('ft', [21, 18, 29, 20, 12], ['Function', 'Name / role', 'Scope · when to escalate', 'Delegation · training record', 'Ready?'], [
         tr(el('Technical acquisition and transfer'), td('', 'left'), td('', 'left'), td('', 'left'), td(ck('Yes', 'No', cls='opts col'))),
         tr(el('Local imaging review'), td('', 'left'), td('', 'left'), td('', 'left'), td(ck('Yes', 'No', cls='opts col'))),
         tr(el('Clinical decision and repeat imaging (PI)'), td('', 'left'), td('', 'left'), td('', 'left'), td(ck('Yes', 'No', cls='opts col')))]))
pages.append(f'<main class="page">{top("Equipment, transfer and people")}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Equipment, transfer and people", 3)}</main>')
# ---------- Page 4: G pathways + H actions
PS = ck('Defined and tested', 'Partial', 'Not defined', cls='opts col')
G = (sec('G', 'What happens to an image set', 'For each situation, name the record or system and who acts. The IQL records each set; the PFVR links a visit to its IQL entry.') +
     table('gt', [24, 21, 21, 14, 20], ['Situation', 'Record or system', 'Responsible role · handoff', 'Pathway', 'Evidence · action ID (H)'], [
         tr(el(s), td('', 'left'), td('', 'left'), td(PS), td('', 'left')) for s in
         ['Acceptable set sent to central review', 'Limited or non-conforming set', 'Image needed for eligibility or a clinical decision', 'Repeat acquisition or corrected transfer', 'Recurrent problem or central-reader disagreement']]))
H = (sec('H', 'Gaps, questions and actions', 'A gap in acquisition, timing, people, transfer or retrieval blocks submission until it is closed. Close an action only with evidence.') +
     table('ht', [9, 10, 28, 11, 13, 10, 19], ['Action ID', 'Req. ID / control', 'Gap or question to the sponsor', 'Blocks submission?', 'Owner (role)', 'Due date', 'Status · closing evidence'],
           [tr(td(), td(), td('', 'left'), td(ck('Yes', 'No', cls='opts col')), td(), td(), td('', 'left')) for _ in range(6)]))
pages.append(f'<main class="page">{top("Image-set pathways, gaps and actions")}<section class="section compact">{G}</section><section class="section compact">{H}</section>{foot("Image-set pathways, gaps and actions", 4)}</main>')
# ---------- Page 5: I, J, K
concl = [('Ready for sponsor or CRO review', 'Every requirement is mapped and supported by current evidence.'),
         ('Ready, with a documented observation', 'An open point that does not block any requirement; it has an owner, a due date and is disclosed to the sponsor.'),
         ('Action required before submission', 'A gap in H blocks submission.'),
         ('Not ready: sponsor clarification or escalation', 'The site cannot meet a requirement as written.')]
I = (sec('I', 'Site conclusion', 'Select one for this version of the charter.') +
     table('it', [34, 56, 10], ['Conclusion', 'Meaning', 'Select'], [tr(el(a), td(b, 'left'), td(ck('', cls='opts'))) for a, b in concl] +
           [tr(el('Open observations (action IDs)'), td('', 'left" colspan="2'))]))
J = (sec('J', 'Assessment history', 'Reopen the SIRR after a charter or CIP change, new equipment, software or archive, failed maintenance, a change of acquisition staff or reviewer, positioning that cannot be reproduced, or a recurrent problem in the IQL or an IMC finding. Keep earlier rows.') +
     table('jt', [9, 13, 34, 26, 18], ['Rev.', 'Date', 'Trigger · charter version · requirements affected', 'Conclusion', 'Next review or trigger'],
           [tr(td(), td(), td('', 'left'), td('', 'left'), td('', 'left')) for _ in range(4)]))
K = (sec('K', 'Attestation and sponsor references', 'Copy sponsor or CRO references from their controlled records. Activation is the sponsor\'s decision.') +
     table('kt', [32, 68], None, [tr(el('Submitted to sponsor or CRO (reference / date)'), td('', 'left')),
                                   tr(el('Sponsor or CRO response (reference / date)'), td('', 'left')),
                                   tr(el('Site activation record (reference / date)'), td('', 'left'))]) +
     '<div class="sig3">' + ''.join(f'<div class="signature"><b>{t}</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
                                    for t in ['Technical acquisition', 'Local imaging reviewer', 'Principal Investigator']) + '</div>')
pages.append(f'<main class="page">{top("Conclusion, history and attestation")}<section class="section compact">{I}</section><section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Conclusion, history and attestation", 5)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:56px}.meta-cell.span2{grid-column:span 2}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:52px;line-height:1.4}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.el .sub{display:block;font-weight:400;color:#4d5b6b;font-size:7.9px;line-height:1.25;margin-top:2px}
td.rid{font-weight:700;color:#173c67;font-size:8.8px}
.bt td{height:38px;font-size:9px;padding:3px 7px}.ct td{height:50px;font-size:9px;padding:3px 7px}
.dt td{height:66px;font-size:8.6px;padding:2px 5px}.dt th{font-size:8.4px}.dt .opts{font-size:7.6px;line-height:1.2}
.et td{height:80px;font-size:8.8px;padding:3px 6px}.et .opts{font-size:7.8px}
.ft td{height:108px;font-size:8.8px;padding:3px 6px}
.gt td{height:78px;font-size:8.8px;padding:3px 6px}.gt .opts{font-size:7.8px}
.ht td{height:58px;font-size:8.6px;padding:2px 5px}.ht .opts{font-size:7.8px}
.it td{height:44px;font-size:8.8px;padding:3px 7px}
.jt td{height:50px;font-size:8.6px;padding:3px 6px}
.kt td{height:30px;font-size:8.8px;padding:3px 7px}
.sig3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:8px}.sig3 .signature{min-height:86px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
