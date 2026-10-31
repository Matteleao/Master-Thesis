# PFVR v0.7 (blank) from v0.4, the Codex v0.6 alternative and the Codex analysis of v0.5.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>PFVR v0.7 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'pfvr-').replace('Editor do POT', 'Editor do PFVR').replace('POT', 'PFVR')
V, NP = 'PFVR v0.7', 5
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">PFVR - Participant Follow-up Visit Record</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">PFVR · v0.7</div></header>')
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
def strip(sheet=False):
    cells = ['PFVR ID', 'Participant code', 'Visit', 'Window'] + (['Sheet no. / total sheets'] if sheet else [])
    return f'<section class="sheet-strip{" s5" if sheet else ""}">' + ''.join(meta(c) for c in cells) + '</section>'
# ---------- Page 1: header, A, B
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('PFVR ID'),
               meta('Participant code'), meta('Visit (name / nominal day)'), meta('Index procedure date (ICDL ID)'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The PFVR records one participant\'s one follow-up visit: when it happened (C), each component the CIP requires with its date, completion and timing (D), whether images and tests are usable (E), what the participant reports (F), the clinical assessment (G) and who did it (H). Problems that need a response go to I, and the visit is classified in J.</p>'
     '<p>A component done on a later contact for the same visit stays in this record with its own date. Write the short finding that matters and cite the clinical source, the Image Quality Log (IQL) or the SART for the rest.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One participant and one follow-up visit of the CIP.</td>'
     '<td>Whether the visit is complete and usable, usable with a limit, or needs follow-up.</td>'
     '<td>CIP visit schedule, clinical source, questionnaires, IQL, earlier PFVR.</td>'
     '<td>Visit outcome (J) and component counts for the Follow-up Compliance Review (FUCR); exceptions and routes (I).</td></tr></tbody></table>')
fam = [('Imaging and objective tests', ['X-ray', 'CT', 'MRI', 'Ultrasound', 'Laboratory', 'Other test'], 'D: done, date, window · E: usable?'),
       ('Participant-reported outcomes', ['Pain', 'Function', 'Instability', 'Swelling', 'New symptom', 'Satisfaction'], 'D: each instrument · F: change reported'),
       ('Clinical and functional assessment', ['Examination', 'Range of motion', 'Strength', 'Stability', 'Wound', 'Functional score'], 'D: done · G: result'),
       ('Care and safety review', ['Physiotherapy', 'Medication review', 'Safety review', 'Referral'], 'D: done · I: response · SART if an event')]
B = (sec('B', 'Applicable visit component guide', 'The CIP visit schedule defines the components; tick the families and examples that apply to this visit, then list each one in D.') +
     table('bg', [26, 50, 24], ['Component family', 'Examples that may apply', 'Recorded in'], [tr(el(f), td(ck(*ex, cls='opts left wrap'), 'left'), td(r)) for f, ex, r in fam]))
C = (sec('C', 'Visit timing and contacts', 'This section records when the visit happened. Whether it is complete and usable is decided in J from D and E.') +
     table('tt', [27, 27, 23, 23], ['Nominal target date (reference event)', 'Window: first and last day (CIP rule)', 'Actual visit date', 'Days from target'], [tr(td(), td(), td(), td())]) +
     table('bt', [13, 19, 12, 16, 40], ['Contact', 'Date · mode', 'Day from index', 'Components done (# in D)', 'Purpose · source reference'],
           [tr(el(c), td(), td(), td(), td()) for c in ['First', 'Return', 'Return']]) +
     table('rj', [27, 73], None, [tr(el('Reason for delay, missed contact efforts or reschedule'), td('', 'left'))]))
pages.append(f'<main class="page">{top("Visit identification, purpose, components and timing")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section><section class="section compact">{C}</section>{foot("Identification, purpose, components and timing", 1)}</main>')
# ---------- Page 2: C components (landscape)
D = (sec('D', 'Required components', 'One line per component the CIP requires for this visit, taken from the visit schedule. Completion and timing are rated separately: a component can be complete but outside its window. Partial, not performed or outside the window needs an exception in I.') +
     table('ct', [3, 19, 6, 13, 10, 11, 12, 18, 8], ['#', 'Component', 'Critical to quality?', 'Method required · used', 'Date · day from index', 'Completion', 'Timing', 'Evidence or record (IQL, questionnaire, note)', 'Exception (# in I)'],
           [tr(num(i), td('', 'left'), td(YN('Yes', 'No')), td('', 'left'), td(), td(YN('Complete', 'Partial', 'Not performed', 'N/A')), td(YN('In window', 'Outside window', 'N/A')), td('', 'left'), td()) for i in range(1, 9)]))
pages.append(f'<main class="page landscape">{top("Required components")}{strip(True)}<section class="section compact">{D}</section>{foot("Required components", 2)}</main>')
# ---------- Page 3: D + E
E = (sec('E', 'Images and objective tests', 'Only for components in D that produce an image or a test result. The image-set quality itself is judged in the IQL.') +
     table('dt', [8, 18, 15, 14, 27, 18], ['# in D', 'Record (IQL or test ID)', 'Usable?', 'Reviewer · date', 'Finding that matters for the visit', 'Action or route'],
           [tr(td(), td('', 'left'), td(YN('Adequate', 'Limited', 'Unavailable')), td(), td('', 'left'), td('', 'left')) for _ in range(3)]))
F = (sec('F', 'What the participant reports', 'The participant\'s own words, including improvement. A report is not classified as an adverse event here; send it for assessment when needed.') +
     table('et', [30, 18, 14, 38], ['Reported change or concern', 'Onset · severity', 'Since last visit', 'Action or referral · record'],
           [tr(td('', 'left'), td('', 'left'), td(YN('Better', 'Worse', 'Same')), td('', 'left')) for _ in range(4)]))
pages.append(f'<main class="page">{top("Image and test usability, participant report")}{strip()}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Image and test usability, participant report", 3)}</main>')
# ---------- Page 4: F + G + H
G = (sec('G', 'Clinical assessment', 'The result and how it compares with the last visit; the full note stays in the clinical source.') +
     table('ft', [22, 16, 16, 26, 20], ['Assessment', 'Assessor', 'Method', 'Result · compared with last visit', 'Action · record'],
           [tr(td('', 'left'), td(), td('', 'left'), td('', 'left'), td('', 'left')) for _ in range(4)]))
H = (sec('H', 'Who did the assessments', 'A change of person matters when a measure depends on the assessor; note the handover.') +
     table('gt', [26, 26, 14, 34], ['Role', 'Name', 'Same as last visit?', 'Handover or supervision note'],
           [tr(el(r), td('', 'left'), td(YN('Yes', 'No', 'N/A')), td('', 'left')) for r in ['Imaging', 'Clinical assessor', 'Questionnaires and scores']]))
I = (sec('I', 'Exceptions and response', 'Only for a problem that needs a response: a partial, missing or late component, an unusable result, or a finding that needs a referral. Safety and deviation assessments stay in their own records.') +
     table('ht', [4, 24, 28, 15, 13, 9, 7], ['#', 'Component (# in D) · cause', 'Effect on the participant or the data · response', 'Linked record', 'Owner', 'Due', 'Status'],
           [tr(num(i), td('', 'left'), td('', 'left'), td('', 'left'), td(), td(), td(YN('Open', 'Closed'))) for i in range(1, 4)]))
pages.append(f'<main class="page">{top("Clinical assessment, personnel and exceptions")}{strip()}<section class="section compact">{G}</section><section class="section compact">{H}</section><section class="section compact">{I}</section>{foot("Clinical assessment, personnel and exceptions", 4)}</main>')
# ---------- Page 5: I + J
outc = [('Complete and usable', 'All components complete, in window and usable.'),
        ('Complete, with a documented observation', 'Complete and usable; an observation in I does not limit the data.'),
        ('Usable with a limitation', 'A component is late, partial or limited; the limit is stated in I.'),
        ('Incomplete: follow-up required', 'A component is still missing and can be recovered.'),
        ('Not usable for the intended assessment', 'A critical-to-quality component cannot be used.'),
        ('Missed', 'The visit did not take place.')]
J = (sec('J', 'Visit outcome', 'Write what confirms each point (counts, days, item numbers). The classification comes from C to I; an exception does not make a visit unusable by itself.') +
     table('it', [44, 14, 42], ['Point', 'Result', 'Confirmed in (section and what was checked)'],
           [tr(el(x), td(ck('Yes', 'No', cls='opts')), td('', 'left')) for x in ['Visit in its window', 'Every required component complete', 'Every critical-to-quality component in window and usable', 'No open exception']]) +
     table('io', [40, 50, 10], ['Outcome', 'Meaning', 'Select'], [tr(el(a), td(b, 'left'), td(ck('', cls='opts'))) for a, b in outc]) +
     table('ir', [30, 70], None, [tr(el('Rationale'), td('', 'left'))]))
K = (sec('K', 'Sign-off') +
     '<div class="sig2"><div class="signature"><b>Completed by</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Reviewed by (investigator)</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Visit outcome and sign-off")}{strip()}<section class="section compact">{J}</section><section class="section compact">{K}</section>{foot("Visit outcome and sign-off", 5)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:46px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:44px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.num{font-weight:700;color:#173c67;font-size:9px}
.bg td{height:46px;font-size:8.8px;padding:3px 7px}.bg td:last-child{font-size:8.4px}.opts.wrap{flex-wrap:wrap;gap:3px 10px}.tt td{height:34px;font-size:8.8px}.bt{margin-top:6px}.bt td{height:36px;font-size:8.8px;padding:2px 6px;text-align:center!important;vertical-align:middle}.bt td.el{text-align:center!important}.rj{margin-top:6px}.rj td{height:56px;font-size:8.8px;padding:3px 7px}.sheet-strip.s5{grid-template-columns:repeat(5,1fr)!important}
.ct td{height:59px;font-size:8.6px;padding:2px 5px}.ct th{font-size:8.2px}.ct .opts{font-size:7.6px;line-height:1.2}
.dt td{height:105px;font-size:8.8px;padding:3px 6px}.dt .opts{font-size:7.8px}
.et td{height:100px;font-size:8.8px;padding:3px 6px}.et .opts{font-size:7.8px}
.ft td{height:60px;font-size:8.8px;padding:3px 6px}
.gt td{height:46px;font-size:8.8px;padding:3px 6px}.gt .opts{font-size:7.8px}
.ht td{height:66px;font-size:8.8px;padding:3px 6px}.ht .opts{font-size:7.8px}
.it td{height:48px;font-size:8.8px;padding:3px 7px}
.io{margin-top:6px}.io td{height:40px;font-size:8.8px;padding:2px 7px}
.ir{margin-top:6px}.ir td{height:140px;font-size:8.8px;padding:3px 7px}
.sig2 .signature{min-height:130px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
