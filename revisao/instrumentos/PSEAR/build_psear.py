# PSEAR v0.94 (blank) from v0.91, the Codex v0.93 alternative and the Codex analysis (A-K kept).
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>PSEAR v0.94 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'psear-').replace('Editor do POT', 'Editor do PSEAR').replace('POT', 'PSEAR')
V, NP = 'PSEAR v0.94', 7
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">PSEAR - Participant Screening and Eligibility Assessment Record</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">PSEAR · v0.94</div></header>')
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
pages = []
YN = lambda *l: ck(*l, cls='opts col')
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('CIP version / amendment'), meta('Site / code'), meta('PSEAR ID / revision'),
               meta('Participant code'), meta('Screening number'), meta('Screening log entry (SIFSL)'), meta('Date first identified'),
               meta('Screening opened'), meta('Responsible assessor / role'), meta('Identification key location'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The PSEAR records one coded participant\'s eligibility decision before enrollment: consent in place (B), the screening done (C), the findings that matter for eligibility (D to F), each criterion of the current CIP checked against its evidence (G), open questions and exceptions (H), and the decision (I). No participant is eligible while an item in H is open. Enrollment and handoff follow in J.</p>'
     '<p>Write only what changes, explains or qualifies the decision, and cite the source for the rest. Consent forms, clinical notes, image reports and the CRF stay in their own records; the screening log (SIFSL) keeps every candidate and links to this record.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One coded participant and one eligibility decision.</td>'
     '<td>Whether the candidate may be enrolled, is not eligible, or is held until an open item is resolved.</td>'
     '<td>Current CIP, consent source, clinical records, image reports and Image Quality Log (IQL), laboratory results.</td>'
     '<td>The decision with its evidence (I), the screening outcome for the SIFSL and the handoff to enrollment (J).</td></tr></tbody></table>')
B = (sec('B', 'Before screening starts', 'An incomplete gate blocks an eligible decision; open an item in H. Not applicable needs the CIP basis in the reference column.') +
     table('bt', [34, 14, 30, 22], ['Gate', 'Status', 'Evidence or reference', 'Limitation · H reference'], [
         tr(el(g), td(YN('Confirmed', 'Incomplete', 'N/A')), td('', 'left'), td('', 'left')) for g in
         ['Current CIP and screening pathway confirmed', 'Consent on the current form signed before any study-specific activity (version, date and time)', 'People doing the assessments delegated and trained', 'Candidate entered in the screening log (SIFSL)']]))
pages.append(f'<main class="page">{top("Participant identification, purpose and screening gates")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and screening gates", 1)}</main>')
# ---------- Page 2: C
C = (sec('C', 'Screening activities', 'List only the activities the CIP requires for this decision. No results here: they go in D to F or stay in the source. Use a numbered continuation sheet if more rows are needed.') +
     table('ct', [4, 26, 12, 10, 14, 20, 14], ['#', 'Activity or assessment', 'Required by the CIP?', 'Date', 'Done by (role)', 'Source record', 'Status'],
           [tr(num(i), td('', 'left'), td(YN('Yes', 'No')), td(), td(), td('', 'left'), td(YN('Complete', 'Incomplete', 'Unavailable'))) for i in range(1, 11)]))
pages.append(f'<main class="page">{top("Screening activities")}<section class="section compact">{C}</section>{foot("Screening activities", 2)}</main>')
# ---------- Page 3: D + E1
D = (sec('D', 'Clinical, functional and participant-reported findings', 'Only components the CIP requires or that bear on a criterion. Enter the value or a short conclusion and its source.') +
     table('dt', [24, 18, 11, 19, 16, 12], ['Component', 'Instrument or method', 'Date', 'Finding or score', 'Source record', 'Assessor'],
           [tr(td('', 'left'), td('', 'left'), td(), td('', 'left'), td('', 'left'), td()) for _ in range(6)]))
E1 = (sec('E1', 'Imaging and objective tests', 'One short finding only when it explains eligibility. Image-set quality is in the IQL; the full report stays in its source.') +
      table('e1t', [4, 15, 10, 13, 19, 11, 28], ['#', 'Modality or test', 'Date', 'Region or target', 'Report or source (IQL ID)', 'Adequate for the decision?', 'Finding relevant to eligibility'],
            [tr(num(i), td('', 'left'), td(), td('', 'left'), td('', 'left'), td(YN('Yes', 'No')), td('', 'left')) for i in range(1, 5)]))
pages.append(f'<main class="page">{top("Clinical findings, imaging and objective tests")}<section class="section compact">{D}</section><section class="section compact">{E1}</section>{foot("Clinical findings, imaging and objective tests", 3)}</main>')
# ---------- Page 4: E2 + F
E2 = (sec('E2', 'What the images mean for eligibility', 'Only for image findings that decide a criterion. The criterion outcome itself goes in G.') +
      table('e2t', [26, 50, 24], ['Imaging question', 'Interpretation for eligibility', 'Source · reviewer'], [tr(td('', 'left'), td('', 'left'), td('', 'left')) for _ in range(4)]))
F = (sec('F', 'Indication and planned procedure', 'Complete only when the CIP makes compatibility part of eligibility. Do not repeat D or E.') +
     table('ftb', [28, 38, 20, 14], ['Element', 'Compatibility statement', 'Source · reviewer', 'Status'],
           [tr(el(x), td('', 'left'), td('', 'left'), td(YN('Confirmed', 'Not confirmed', 'N/A'))) for x in
            ['Indication for the planned procedure', 'Procedure or treatment pathway in the CIP', 'Planned device, size or configuration', 'Other study-specific requirement']]))
pages.append(f'<main class="page">{top("Imaging interpretation and planned procedure")}<section class="section compact">{E2}</section><section class="section compact">{F}</section>{foot("Imaging interpretation and planned procedure", 4)}</main>')
# ---------- Page 5: G (landscape)
G = (sec('G', 'Each criterion against its evidence', 'One row per inclusion or exclusion criterion of the current CIP. For an exclusion, Met means the exclusion is absent. Cite where the evidence is and the date it became available. Missing or conflicting evidence is Incomplete: open an item in H. A second reviewer only where the CIP or site pathway requires it; the PI settles a disagreement in H.') +
     table('gt', [3, 6, 27, 22, 10, 11, 11, 10], ['#', 'Type', 'CIP criterion (number and short text)', 'Evidence location · date available', 'Outcome', 'Primary reviewer · date', 'Second reviewer · date', 'H reference'],
           [tr(num(i), td(YN('Inclusion', 'Exclusion')), td('', 'left'), td('', 'left'), td(YN('Met', 'Not met', 'Incomplete')), td(), td(), td()) for i in range(1, 13)]))
pages.append(f'<main class="page landscape">{top("Eligibility criteria")}<section class="section compact">{G}</section>{foot("Eligibility criteria", 5)}</main>')
# ---------- Page 6: H + I
I = (sec('I', 'Eligibility decision', 'Eligible needs every gate Yes. Write what confirms each gate (counts, times, item numbers); cite sections and records in the rationale; do not repeat findings.') +
     table('ht', [44, 14, 42], ['Gate', 'Result', 'Confirmed in (section and what was checked)'], [
         tr(el('Required screening activities complete'), td(ck('Yes', 'No', cls='opts')), td('', 'left')),
         tr(el('Every criterion met, including absence of each exclusion'), td(ck('Yes', 'No', cls='opts')), td('', 'left')),
         tr(el('Consent confirmed before study-specific activity'), td(ck('Yes', 'No', cls='opts')), td('', 'left')),
         tr(el('No open item or exception'), td(ck('Yes', 'No', cls='opts')), td('', 'left'))]) +
     table('hd', [30, 70], None, [tr(el('Decision'), td(ck('Eligible', 'Not eligible', 'Held: item open in H', cls='opts left'), 'left')),
                                  tr(el('Rationale (sections and records)'), td('', 'left tall'))]))
H = (sec('H', 'Open items and exceptions', 'Only for missing, conflicting or unavailable eligibility information. No eligible decision while an item is open. Routine care and CAPA stay in their own records.') +
     table('it', [5, 26, 27, 13, 11, 18], ['#', 'Missing item · criterion affected', 'Effect and immediate action', 'Owner (role)', 'Due date', 'Status · resolution'],
           [tr(num(i), td('', 'left'), td('', 'left'), td(), td(), td(ck('Open', 'Resolved', cls='opts col'))) for i in range(1, 5)]))
pages.append(f'<main class="page">{top("Open items and decision")}<section class="section compact">{H}</section><section class="section compact">{I}</section>{foot("Open items and decision", 6)}</main>')
# ---------- Page 7: J + K
J = (sec('J', 'Enrollment and handoff', 'Enrollment only after an eligible decision. These entries show the sequence; the decision stays in I.') +
     table('jt', [34, 66], None, [tr(el(x), td('', 'left')) for x in ['Decision date and time', 'Enrollment date and time · enrollment record', 'Screening log (SIFSL) entry updated', 'Next record opened (for example the ICDL)', 'If not enrolled: reason entered in the SIFSL']]))
K = (sec('K', 'Signatures and filing', 'The signatures confirm the current CIP, dated evidence, any required second review and the decision.') +
     '<div class="sig3">' + ''.join(f'<div class="signature"><b>{t}</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date and time:<span class="sig-line"></span></div></div>'
                                    for t in ['Primary screening assessor', 'Investigator', 'Second reviewer (if required)']) + '</div>' +
     table('kt', [34, 66], None, [tr(el(x), td('', 'left')) for x in ['PSEAR filed at', 'Source records at', 'Linked screening log']]))
pages.append(f'<main class="page">{top("Enrollment, signatures and filing")}<section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Enrollment, signatures and filing", 7)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:62px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:52px;line-height:1.4}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.num{font-weight:700;color:#173c67;font-size:9px}
.bt td{height:110px;font-size:8.8px;padding:3px 7px}.bt .opts{font-size:7.8px}
.ct td{height:83px;font-size:8.8px;padding:3px 6px}.ct .opts{font-size:7.8px}
.dt td{height:70px;font-size:8.8px;padding:3px 6px}
.e1t td{height:78px;font-size:8.8px;padding:3px 6px}.e1t .opts{font-size:7.8px}
.e2t td{height:120px;font-size:8.8px;padding:3px 6px}
.ftb td{height:68px;font-size:8.8px;padding:3px 6px}.ftb .opts{font-size:7.8px}
.gt td{height:42px;font-size:8.6px;padding:2px 5px}.gt .opts{font-size:7.4px;line-height:1.15}.gt th{font-size:8.4px}
.ht td{height:50px;font-size:8.8px;padding:3px 7px}.hd{margin-top:6px}.hd td{height:40px;font-size:8.8px;padding:3px 7px}.hd td.tall{height:150px}
.it td{height:90px;font-size:8.8px;padding:3px 6px}.it .opts{font-size:7.8px}
.jt td{height:62px;font-size:8.8px;padding:3px 7px}.jt td.el{text-align:center;font-size:9.6px}.kt{margin-top:8px}.kt td{height:74px;font-size:8.8px;padding:3px 7px}
.sig3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:2px}.sig3 .signature{min-height:215px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
