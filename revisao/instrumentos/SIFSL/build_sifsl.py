# SIFSL v0.5 (blank) from v0.2, the Codex v0.4 alternative and the Codex analysis.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>SIFSL v0.5 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'sifsl-').replace('Editor do POT', 'Editor do SIFSL').replace('POT', 'SIFSL')
V, NP = 'SIFSL v0.5', 5
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">SIFSL - Subject Identification and Failure Screening Log</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">SIFSL · v0.5</div></header>')
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
def strip():
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['SIFSL ID / revision', 'Site / code', 'Data cut-off', 'Sheet no. / total sheets']) + '</section>'
bar = lambda t: f'<div class="exh">{t}</div>'
STATUS = [('Considered', 'Considered under a code; no formal screening yet.', 'First considered date'),
          ('Screening active', 'Screening has started and is in progress.', 'Screening opened date'),
          ('Awaiting eligibility decision', 'Evidence or review pending; never treated as eligible.', 'PSEAR ID'),
          ('Eligible, awaiting enrollment', 'Eligible decision made; not yet enrolled.', 'PSEAR ID'),
          ('Enrolled', 'Enrollment done.', 'PSEAR ID, enrollment record'),
          ('Not eligible', 'The PSEAR decision does not allow inclusion.', 'PSEAR ID, category'),
          ('Withdrawn before enrollment', 'The person or the process left before inclusion.', 'Category'),
          ('Closed: other outcome', 'An outcome not covered above.', 'Category, controlled reference')]
CATS = [('1 · Criterion not met', 'One or more criteria not met; details stay in the PSEAR.'),
        ('2 · Assessment incomplete or unavailable', 'A required assessment was not done or not available in time.'),
        ('3 · Consent or participant decision', 'Declined or withdrew; no personal detail.'),
        ('4 · Screening stopped before a decision', 'Screening ended for a controlled reason before any decision.'),
        ('5 · Study or site constraint', 'Recruitment closed, quota, or a sponsor or site decision.'),
        ('6 · Other', 'Any other reason; cite the controlled record.')]
# ---------- Page 1: header, A, B
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('SIFSL ID / revision'),
               meta('Period covered / data cut-off'), meta('Log owner / role'), meta('Identity key location (kept separately)'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SIFSL lists every person considered for the investigation under a code, whatever happened next, with their current status and final outcome. It links each eligibility decision to its Participant Screening and Eligibility Assessment Record (PSEAR) and each enrollment to its record, so that at every cut-off the site can account for every candidate (D). It does not decide eligibility, which belongs to the PSEAR, and it does not calculate rates, which belong to the Performance Indicator Review (PIR).</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One coded person on one line.</td>'
     '<td>Whether every candidate is accounted for and linked to the PSEAR and enrollment records.</td>'
     '<td>Referrals, current CIP, PSEAR and enrollment records.</td>'
     '<td>Counts for the PIR (E); reconciliation issues (D).</td></tr></tbody></table>')
B = (sec('B', 'Status and non-inclusion categories', 'A category applies only to Not eligible, Withdrawn before enrollment and Closed: other outcome. It is administrative; the reasons stay in the PSEAR.') +
     bar('Status') + table('cs', [30, 46, 24], ['Status', 'Use when', 'Also write on the line'], [tr(el(a), td(b, 'left'), td(c, 'left')) for a, b, c in STATUS]) +
     bar('Non-inclusion categories') + table('cc', [38, 62], ['Category', 'Use when'], [tr(el(a), td(b, 'left')) for a, b in CATS]))
pages.append(f'<main class="page">{top("Log identification, purpose, status and categories")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose, status and categories", 1)}</main>')
# ---------- Pages 2-3: C register (landscape)
DH = ['#', 'Candidate code', 'First considered', 'Screening opened', 'Status', 'Status date', 'PSEAR ID', 'Non-inclusion category no.', 'Enrollment date · record', 'Issue ID']
DW = [4, 11, 9, 9, 17, 9, 12, 9, 12, 8]
GUIDE = ('One line per coded person, numbered across sheets in the order first considered; update the same line when the status changes. Codes only: no names, initials, birth dates or contact details. '
         'Write the status name from B, and the category number only for a closed non-inclusion. Cite the PSEAR ID and the enrollment record; the content stays in those records. Issue ID comes from D.')
for k in range(2):
    body = sec('C', 'Candidate register', GUIDE) + table('dt' + (' p2' if k else ''), DW, DH, [tr(td('', 'rid'), *[td() for _ in range(9)]) for i in range(12)])
    pages.append(f'<main class="page landscape">{top("Candidate register")}{strip()}<section class="section compact">{body}</section>{foot("Candidate register", 2 + k)}</main>')
# ---------- Page 4: D reconciliation
Q = ['Every line has a code and a current status; every closed line has a final outcome.',
     'Every eligibility decision (eligible or not) has a PSEAR ID.',
     'Every enrolled person has both a PSEAR ID and an enrollment record, with matching dates.',
     'Every person still in screening has someone following up; every closed non-inclusion has a category.',
     'No duplicate code, and no PSEAR or enrollment record missing from the log.']
D = (sec('D', 'Reconciliation at the cut-off', 'Check all sheets against the PSEAR and enrollment records. Correct a single issue in the record that owns it and note the correction here.') +
     bar('Checks') + table('et', [52, 12, 36], ['Check', 'Result', 'Evidence or issue ID'], [tr(el(q), td(YN('Yes', 'No')), td('', 'left')) for q in Q]) +
     bar('Issues found') + table('it', [10, 32, 26, 14, 18], ['Issue ID', 'Line or record · what is wrong', 'Correction (record and reference)', 'Owner · due date', 'Status'],
           [tr(td(), td('', 'left'), td('', 'left'), td(), td(YN('Open', 'Resolved'))) for _ in range(4)]))
pages.append(f'<main class="page">{top("Reconciliation")}<section class="section compact">{D}</section>{foot("Reconciliation", 4)}</main>')
# ---------- Page 5: E counts + F review
ST = [s[0] for s in STATUS]
E = (sec('E', 'Counts at the cut-off', 'Count from all sheets. The PIR uses these counts; it, not this log, judges enrollment quality.') +
     bar('1 · Candidates by status') +
     table('nt', [40, 14, 46], ['Status', 'Count', 'Lines (#)'], [tr(el(s), td(), td('', 'left')) for s in ST] +
           [tr(el('All coded candidates (equals the last line number)'), td('', 'tot'), td('', 'tot'), cls='tot')]) +
     bar('2 · Closed non-inclusions by category and status') +
     table('xt', [34, 16, 18, 16, 16], ['Category', 'Not eligible', 'Withdrawn before enrollment', 'Closed: other outcome', 'Total'],
           [tr(el(c[0]), td(), td(), td(), td()) for c in CATS] + [tr(el('Total (equals the counts in table 1)'), td('', 'tot'), td('', 'tot'), td('', 'tot'), td('', 'tot'), cls='tot')]) +
     table('rt', [34, 66], None, [tr(el('Counts sent to (record · owner · date)'), td('', 'left'))]))
F = (sec('F', 'Review and filing') +
     table('gt', [34, 66], None, [tr(el('Review result'), td(ck('Reconciled', 'Reconciled with open issues', 'Not reconciled', cls='opts left'), 'left')),
                                  tr(el('Remaining limits'), td('', 'left'))]) +
     '<div class="sig2"><div class="signature"><b>Log owner</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Counts, review and filing")}<section class="section compact">{E}</section><section class="section compact">{F}</section>{foot("Counts, review and filing", 5)}</main>')
css = """<style>
.meta-grid .meta-cell{min-height:50px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:4px 8px;vertical-align:top;text-align:left;height:30px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.rid{font-weight:700;color:#173c67;font-size:9px}
.exh{background:#dbe7f3;color:#173c67;font-weight:700;font-size:9px;padding:3px 8px;border:1px solid var(--grid);border-bottom:0;margin-top:7px}.exh+table{margin-top:0!important}
.cs td{height:33px;font-size:8.8px;padding:2px 7px}.cc td{height:33px;font-size:8.8px;padding:2px 7px}
.dt td{height:39px;font-size:8.8px;padding:2px 5px}.dt th{font-size:8.4px}
.et td{height:75px;font-size:9px;padding:3px 7px}.et .opts{font-size:7.8px}
.it td{height:98px;font-size:8.8px;padding:3px 6px}.it .opts{font-size:7.8px}
.nt td{height:27px;font-size:8.8px;padding:2px 7px}.xt td{height:27px;font-size:8.8px;padding:2px 7px}.xt th{font-size:8.4px}
tr.tot td{font-weight:700;background:#eef3f9!important}
.rt{margin-top:7px}.rt td{height:44px;font-size:8.8px;padding:3px 7px}
.gt td{height:40px;font-size:8.8px;padding:3px 7px}
.sig2 .signature{min-height:92px!important}.letter{font-size:15px!important}
</style>
"""
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
