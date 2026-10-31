# SIFSL v0.5 (blank) from v0.2, the Codex v0.4 alternative and the Codex analysis.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>SIFSL v0.5 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'sifsl-').replace('Editor do POT', 'Editor do SIFSL').replace('POT', 'SIFSL')
V, NP = 'SIFSL v0.5', 6
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
STATUS = [('Considered', 'The coded person was considered; no formal screening yet.', 'Date first considered'),
          ('Screening active', 'Screening has started and is in progress.', 'Date screening opened'),
          ('Awaiting eligibility decision', 'Evidence or review pending. Never treated as eligible.', 'PSEAR ID'),
          ('Eligible, awaiting enrollment', 'Eligible decision made; enrollment not yet done.', 'PSEAR ID and decision date'),
          ('Enrolled', 'Enrollment done.', 'PSEAR ID and enrollment record'),
          ('Not eligible', 'The PSEAR decision does not allow inclusion.', 'PSEAR ID and category'),
          ('Withdrawn before enrollment', 'The person or the process left screening before inclusion.', 'Category'),
          ('Closed: other outcome', 'An outcome not covered above.', 'Category and controlled reference')]
CATS = [('1 · Criterion not met', 'One or more criteria not met; details stay in the PSEAR.'),
        ('2 · Assessment incomplete or unavailable', 'A required assessment was not done or not available in time.'),
        ('3 · Consent or participant decision', 'Declined, withdrew consent or could not follow the consent route. No personal detail.'),
        ('4 · Screening stopped before a decision', 'Screening ended for a controlled reason before any decision.'),
        ('5 · Study or site constraint', 'Recruitment closed, quota, or a sponsor or site decision.'),
        ('6 · Other', 'Any other reason; cite the controlled record.')]
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('SIFSL ID / revision'),
               meta('Period covered / data cut-off'), meta('Log owner / role'), meta('Identity key location (kept separately)'), meta('Controlled location')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The SIFSL lists every person considered for the investigation under a code, whatever happened next, and keeps their current status and final outcome. It links each eligibility decision to its Participant Screening and Eligibility Assessment Record (PSEAR) and each enrollment to its record, so that at every cut-off the site can account for every candidate (E). It does not decide eligibility, which belongs to the PSEAR, and it does not calculate rates, which belong to the Performance Indicator Review (PIR).</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One coded person on one line, updated as the person moves through screening.</td>'
     '<td>Whether every candidate is accounted for, and whether any link between log, PSEAR and enrollment is missing or wrong.</td>'
     '<td>Candidate referrals, current CIP, PSEAR records, enrollment records.</td>'
     '<td>Counts by status and category (F) for the PIR; reconciliation issues (E) and their route.</td></tr></tbody></table>')
B = (sec('B', 'Rules for the log') +
     table('bt', [28, 72], None, [tr(el(a), td(b, 'left')) for a, b in [
         ('Codes only', 'No names, initials, birth dates, contact details or clinical details. The key linking codes to identity is kept separately under controlled access.'),
         ('One line per person', 'Update the same line when the status changes; never open a second line for the same person.'),
         ('Cite, do not copy', 'Write the PSEAR ID and the enrollment record; the reasons and evidence stay in those records.'),
         ('No PSEAR before screening', 'A person only considered does not need a PSEAR until formal screening starts.'),
         ('Continuation sheets', 'Reprint the register page with the next sheet number; lines are numbered across sheets.')]]))
pages.append(f'<main class="page">{top("Log identification, purpose and rules")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and rules", 1)}</main>')
# ---------- Page 2: C guide
C = (sec('C', 'Status and non-inclusion categories', 'Write the status in words in the register. A non-inclusion category applies only to Not eligible, Withdrawn before enrollment and Closed: other outcome; it is administrative and never replaces the PSEAR.') +
     table('cs', [30, 44, 26], ['Status', 'Use when', 'Required on the line'], [tr(el(a), td(b, 'left'), td(c, 'left')) for a, b, c in STATUS]) +
     '<div class="exh">Non-inclusion categories</div>' +
     table('cc', [36, 64], ['Category', 'Use when'], [tr(el(a), td(b, 'left')) for a, b in CATS]))
pages.append(f'<main class="page">{top("Status and non-inclusion categories")}<section class="section compact">{C}</section>{foot("Status and non-inclusion categories", 2)}</main>')
# ---------- Pages 3-4: D register (landscape)
DH = ['Line', 'Candidate code', 'First considered', 'Screening opened', 'Status (C)', 'Status date', 'PSEAR ID', 'Non-inclusion category (1–6)', 'Enrollment date · record', 'Issue ID (E)']
DW = [4, 11, 9, 9, 17, 9, 12, 9, 12, 8]
for k in range(2):
    body = (sec('D', 'Candidate register' + (' (continued)' if k else ''), None if k else 'One line per coded person, in the order first considered. Update the line when the status changes. Leave the category blank while the person is still in screening or enrolled.') +
            '<div class="sheet">Sheet no. <span class="inline-blank"></span></div>' +
            table('dt' + (' p2' if k else ''), DW, DH, [tr(td('', 'rid'), *[td() for _ in range(9)]) for i in range(12)]))
    pages.append(f'<main class="page landscape">{top("Candidate register")}<section class="section compact">{body}</section>{foot("Candidate register", 3 + k)}</main>')
# ---------- Page 5: E reconciliation
Q = ['Every line has a code and a current status; every closed line has a final outcome.',
     'Every eligibility decision (eligible or not) has a PSEAR ID.',
     'Every enrolled person has both a PSEAR ID and an enrollment record, with matching dates.',
     'Every person still in screening has someone following up; every closed non-inclusion has a category.',
     'No duplicate code, and no PSEAR or enrollment record missing from the log.']
E = (sec('E', 'Reconciliation at the cut-off', 'Check all sheets against the PSEAR and enrollment records. Correct a single issue in the record that owns it and note the correction here.') +
     table('et', [52, 12, 36], ['Check', 'Result', 'Evidence or issue ID'], [tr(el(q), td(YN('Yes', 'No')), td('', 'left')) for q in Q]) +
     '<div class="exh">Issues found</div>' +
     table('it', [10, 32, 26, 14, 18], ['Issue ID', 'Line or record · what is wrong', 'Correction (record and reference)', 'Owner · due date', 'Status'],
           [tr(td(), td('', 'left'), td('', 'left'), td(), td(YN('Open', 'Resolved'))) for _ in range(4)]))
pages.append(f'<main class="page">{top("Reconciliation")}<section class="section compact">{E}</section>{foot("Reconciliation", 5)}</main>')
# ---------- Page 6: F counts + G
st = [s[0] for s in STATUS] + ['Total coded candidates']
ca = [c[0] for c in CATS] + ['Total closed non-inclusions']
rows_ = []
for i in range(max(len(st), len(ca))):
    a = st[i] if i < len(st) else ''; b = ca[i] if i < len(ca) else ''
    rows_.append(tr(el(a) if a else td(), td() if a else td('', 'void'), el(b) if b else td('', 'void'), td() if b else td('', 'void')))
F = (sec('F', 'Counts at the cut-off', 'Count each person once by status and each closed non-inclusion once by category. These counts reconcile the population; the PIR judges enrollment quality.') +
     table('ft', [30, 10, 48, 12], ['Status', 'Count', 'Non-inclusion category', 'Count'], rows_) +
     table('rt', [30, 70], None, [tr(el('Sent to (record · owner · date), or none needed'), td('', 'left'))]))
G = (sec('G', 'Review and filing') +
     table('gt', [30, 70], None, [tr(el('Review result'), td(ck('Reconciled', 'Reconciled with open issues', 'Not reconciled', cls='opts left'), 'left')),
                                  tr(el('Remaining limits'), td('', 'left'))]) +
     '<div class="sig2"><div class="signature"><b>Log owner</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Counts, review and filing")}<section class="section compact">{F}</section><section class="section compact">{G}</section>{foot("Counts, review and filing", 6)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:70px}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}
.purpose td{font-size:9px;padding:5px 8px;vertical-align:top;text-align:left;height:70px;line-height:1.4}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}
td.rid{font-weight:700;color:#173c67;font-size:9px}td.void{background:#fff!important;border-color:transparent!important}
.exh{margin:9px 0 4px;font-weight:700;color:#173c67;font-size:9.6px}
.sheet{text-align:right;font-size:9px;color:#173c67;margin:0 0 4px}.inline-blank{display:inline-block;width:46px;border-bottom:1px solid #6d7a88;margin:0 3px}
.bt td{height:104px;font-size:9.4px;padding:3px 7px}
.cs td{height:57px;font-size:9px;padding:3px 7px}.cc td{height:55px;font-size:9px;padding:3px 7px}
.dt td{height:42px;font-size:8.8px;padding:2px 5px}.dt.p2 td{height:44px}.dt th{font-size:8.4px}
.et td{height:78px;font-size:9px;padding:3px 7px}.et .opts{font-size:7.8px}
.it td{height:102px;font-size:8.8px;padding:3px 6px}.it .opts{font-size:7.8px}
.ft td{height:48px;font-size:8.8px;padding:3px 7px}.rt{margin-top:6px}.rt td{height:80px;font-size:8.8px;padding:3px 7px}
.gt td{height:60px;font-size:8.8px;padding:3px 7px}
.sig2 .signature{min-height:150px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
