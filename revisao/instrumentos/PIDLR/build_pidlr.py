# PIDLR v0.4 (blank): post-investigation debrief, v0.2 architecture A-I kept.
import re, sys
POT = '/home/user/Master-Thesis/revisao/instrumentos/POT/POT_v1.1_blank.html'
OUT = sys.argv[1]
p = open(POT).read()
head = re.sub(r'<title>.*?</title>', '<title>PIDLR v0.4 - Blank Editable</title>', p[:p.find('<body')])
ed_style = p[p.find('<style id="pot-editor-style">'):]; ed_style = ed_style[:ed_style.find('</style>') + 8]
ed_script = p[p.find('<script id="pot-editor-script">'):]; ed_script = ed_script[:ed_script.find('</script>') + 9]
ed = (ed_style + '\n' + ed_script).replace('pot-', 'pidlr-').replace('Editor do POT', 'Editor do PIDLR').replace('POT', 'PIDLR')
V, NP = 'PIDLR v0.4', 7
def ck(*labels, cls='opts'):
    return f'<span class="{cls}">' + ''.join(f'<span class="opt"><span class="check"></span>{l}</span>' for l in labels) + '</span>'
def top(sub):
    return (f'<header class="topbar"><div><div class="title">PIDLR - Post-Investigation Debrief and Lessons Record</div>'
            f'<div class="subtitle">{sub}</div></div><div class="version">PIDLR · v0.4</div></header>')
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
pages = []
YN = lambda *l: ck(*l, cls='opts col')
def strip():
    return '<section class="sheet-strip">' + ''.join(meta(c) for c in ['PIDLR ID', 'Study / site', 'Debrief type / evidence cut-off', 'Sheet no. / total sheets']) + '</section>'
# ---------- Page 1
hdr = ''.join([meta('Study / protocol'), meta('CIP version'), meta('Site / code'), meta('PIDLR ID / revision'),
               meta('Investigation status', ck('Completed', 'Suspended', 'Terminated', 'Ongoing', cls='opts left')), meta('Debrief type', ck('Final', 'Interim', 'Early closure', cls='opts left')),
               meta('Period covered / close-out date'), meta('Evidence cut-off'), meta('Prepared by / role'), meta('PI'), meta('Reason for an interim or early debrief', cls=' span2')])
A = (sec('A', 'Purpose and use') +
     '<div class="box"><p>The PIDLR turns what the site learned in one investigation into lessons that reach a controlled destination. It reviews the investigation by phase (C) and by domain (D), records each lesson with its evidence (E), sends it to the record that will own the change (F), states what remains uncertain (G) and checks that the transfer happened (H) before the debrief is closed (I). It never reclassifies a safety event or a deviation, and it does not replace the CAPA log: it cites them.</p></div>'
     '<table class="purpose"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
     '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
     '<td>One investigation at one site, up to a stated evidence cut-off.</td>'
     '<td>Whether the debrief can close, and which lessons must be transferred and to whom.</td>'
     '<td>MRL, PIR, IMC, CAPA log, SRR, safety and follow-up records (B).</td>'
     '<td>Lessons with owners and destinations; revised procedures; notices to other studies.</td></tr></tbody></table>')
INP = ['Milestone Review Log (MRL)', 'Performance Indicator Records (PIR)', 'Internal monitoring (IMC)', 'CAPA log', 'Site Risk Register (SRR)', 'Safety and complications (SART, SCML, CSST)', 'Follow-up (FUCR)', 'Learning curve (SLCT)']
B = (sec('B', 'Inputs used', 'Cite the exact records. Limited or missing inputs restrict the lessons that can be drawn; say how.') +
     table('bt', [30, 26, 16, 28], ['Input', 'Record IDs or range', 'Available?', 'Limit on the lessons'], [tr(el(x), td('', 'left'), td(ck('Adequate', 'Limited', 'Missing', cls='opts col')), td('', 'left')) for x in INP]))
pages.append(f'<main class="page">{top("Debrief identification, purpose and inputs")}<section class="meta-grid">{hdr}</section><section class="section compact">{A}</section><section class="section compact">{B}</section>{foot("Identification, purpose and inputs", 1)}</main>')
# ---------- Page 2: C (landscape)
PH = [('1 · Feasibility', 'Site capability fits the investigation'), ('2 · Start-up', 'Controls, roles and release ready'), ('3 · Enrollment', 'Eligibility and consent controlled'),
      ('4 · Surgery', 'Technique, device traceability, learning curve'), ('5 · Follow-up', 'Assessments in window, retention'), ('6 · Close-out', 'Records reconciled, obligations handed over'),
      ('7 · Continuous improvement', 'Lessons handed over (E to I)'), ('Across phases: safety', 'Surveillance, reporting, escalation')]
C = (sec('C', 'Review by phase', 'Only what supports a strength, a limitation or a lesson; case details stay in their records. N/A or Not assessable needs the reason.') +
     table('ct', [16, 18, 26, 16, 12, 12], ['Phase', 'Expected', 'What happened (record)', 'Review result', 'Lesson ID', 'Note'],
           [tr(el(f'<b>{a}</b><span class="sub">{b}</span>'), td('', 'left'), td('', 'left'), td(ck('No lesson', 'Strength', 'Limitation', 'Lesson', cls='opts col2')), td(), td('', 'left')) for a, b in PH]))
pages.append(f'<main class="page landscape">{top("Review by phase")}{strip()}<section class="section compact">{C}</section>{foot("Review by phase", 2)}</main>')
# ---------- Page 3: D (landscape)
DOM = ['Governance and accountability', 'Risk management and escalation', 'Surgery and device traceability', 'Enrollment and eligibility', 'Imaging and assessment', 'Follow-up and retention', 'Safety surveillance and reporting', 'Data integrity']
D = (sec('D', 'Review by domain', 'A strength to keep, a limitation, and what contributed. Label an unconfirmed explanation as a hypothesis. Only the domains that apply.') +
     table('dt', [17, 18, 18, 19, 16, 12], ['Domain', 'Strength kept', 'Limitation', 'What contributed', 'Evidence (records)', 'Lesson ID'],
           [tr(el(x), td('', 'left'), td('', 'left'), td('', 'left'), td('', 'left'), td()) for x in DOM]))
pages.append(f'<main class="page landscape">{top("Review by domain")}{strip()}<section class="section compact">{D}</section>{foot("Review by domain", 3)}</main>')
# ---------- Page 4: E (landscape)
E = (sec('E', 'Lessons', 'A lesson names a practice to keep or change, its evidence and where it goes. Type: Keep, Change, Add, Stop, Escalate, or Limit (an uncertainty to preserve). Priority High: safety, endpoint, traceability or a repeated failure; Medium: likely to recur; Low: refinement.') +
     table('et', [8, 13, 11, 30, 16, 14, 8], ['Lesson ID', 'Domain', 'Type', 'Lesson (one sentence)', 'Evidence (records)', 'Destination', 'Priority'],
           [tr(td('', 'rid'), td(), td(ck('Keep', 'Change', 'Add', 'Stop', 'Escalate', 'Limit', cls='opts col2')), td('', 'left'), td('', 'left'), td('', 'left'), td(ck('High', 'Medium', 'Low', cls='opts col'))) for _ in range(7)]))
pages.append(f'<main class="page landscape">{top("Lessons")}{strip()}<section class="section compact">{E}</section>{foot("Lessons", 4)}</main>')
# ---------- Page 5: F (landscape)
F = (sec('F', 'Transfer of lessons', 'The Lesson ID goes into each receiving record, which owns the change. A document released is not yet a practice in use.') +
     table('ft', [8, 15, 23, 17, 11, 8, 18], ['Lesson ID', 'Scope', 'Change needed', 'Receiving record · version', 'Owner', 'Due', 'Stage'],
           [tr(td('', 'rid'), td(ck('Site practice', 'Future study', 'Ongoing study', 'Sponsor', 'No transfer', cls='opts col')), td('', 'left'), td('', 'left'), td(), td(), td(ck('Planned', 'Accepted', 'Transferred', 'In use', cls='opts col2'))) for _ in range(6)]))
pages.append(f'<main class="page landscape">{top("Transfer of lessons")}{strip()}<section class="section compact">{F}</section>{foot("Transfer of lessons", 5)}</main>')
# ---------- Page 6: G + H
G = (sec('G', 'What remains uncertain', 'What could not be settled here, why, and who reviews it next.') +
     table('gt', [10, 30, 22, 20, 18], ['Lesson ID', 'Uncertainty', 'Why it remains', 'Receiving record · owner', 'Next review'], [tr(td(), td('', 'left'), td('', 'left'), td('', 'left'), td()) for _ in range(3)]))
H = (sec('H', 'Was the transfer made, and did it work?', 'Transferred: handoff documented. In use: evidence the practice is used. Effective: the planned check is met, which may happen after the debrief closes.') +
     table('ht', [10, 22, 26, 20, 22], ['Lesson ID', 'Receiving record', 'Evidence checked · date', 'Effect', 'Next decision · owner'],
           [tr(td(), td('', 'left'), td('', 'left'), td(ck('Pending', 'Supported', 'Not supported', cls='opts col')), td('', 'left')) for _ in range(4)]))
pages.append(f'<main class="page">{top("Uncertainties and transfer check")}{strip()}<section class="section compact">{G}</section><section class="section compact">{H}</section>{foot("Uncertainties and transfer check", 6)}</main>')
# ---------- Page 7: I
I = (sec('I', 'Closing the debrief', 'Closing the debrief, putting a change into practice and showing it works are three separate decisions.') +
     table('io', [34, 56, 10], ['Closure', 'Use when', 'Select'], [tr(el(a), td(b, 'left'), td(ck('', cls='opts'))) for a, b in [
         ('Debrief closed', 'All lessons transferred; no open limitation of the debrief.'),
         ('Closed with tracked transfers', 'Each open transfer or limit has a receiving record, owner and review date.'),
         ('Not ready to close', 'A lesson lacks evidence, a destination or an owner.')]]) +
     table('id', [34, 66], None, [tr(el(x), td('', 'left')) for x in ['Open transfers (lesson IDs · owners)', 'Revised procedures (version · release date)', 'Other studies notified', 'Debrief file location and retention']] +
           [tr(el('Rationale and remaining limits'), td('', 'left tall'))]) +
     '<div class="sig2"><div class="signature"><b>Prepared by</b><div class="sig-field">Name / role: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div>'
     '<div class="signature"><b>Principal Investigator</b><div class="sig-field">Name: </div><div class="sig-field">Signature / date:<span class="sig-line"></span></div></div></div>')
pages.append(f'<main class="page">{top("Closing the debrief")}{strip()}<section class="section compact">{I}</section>{foot("Closing the debrief", 7)}</main>')
css = '''<style>
.meta-grid .meta-cell{min-height:52px}.meta-cell.span2{grid-column:span 2}.opts.left{justify-content:flex-start}.opts.col{display:grid;grid-template-columns:auto;justify-content:start;text-align:left;gap:2px 0}.opts.col2{display:grid;grid-template-columns:auto auto;justify-content:start;text-align:left;gap:2px 6px}
.purpose td{font-size:9px;padding:4px 8px;vertical-align:top;text-align:left;height:44px;line-height:1.35}.purpose td:first-child{font-weight:400;color:inherit;background:none}.purpose th{text-align:center}
td.el{text-align:left;font-weight:700;color:#173c67;background:#f7f9fb!important;font-size:8.8px}td.el .sub{display:block;font-weight:400;color:#4d5b6b;font-size:7.8px;margin-top:2px}td.num,td.rid{font-weight:700;color:#173c67;font-size:9px}
.bt td{height:62px;font-size:8.8px;padding:2px 6px}.bt .opts{font-size:7.6px;line-height:1.15}
.ct td{height:61px;font-size:8.6px;padding:2px 5px}.ct .opts{font-size:7.6px}
.dt td{height:61px;font-size:8.6px;padding:2px 5px}
.et td{height:68px;font-size:8.6px;padding:2px 5px}.et .opts{font-size:7.6px;line-height:1.15}
.ft td{height:81px;font-size:8.6px;padding:2px 5px}.ft .opts{font-size:7.4px;line-height:1.15}
.gt td{height:105px;font-size:8.8px;padding:3px 6px}.ht td{height:100px;font-size:8.8px;padding:3px 6px}.ht .opts{font-size:7.8px}
.io td{height:60px;font-size:8.8px;padding:3px 7px}.id{margin-top:7px}.id td{height:64px;font-size:8.8px;padding:3px 7px}.id td.el{background:#dbe7f3!important;text-align:center;vertical-align:middle}.id td.tall{height:200px}
.sig2 .signature{min-height:150px!important}.letter{font-size:15px!important}
</style>
'''
open(OUT, 'w').write(head + '<body class="blank-template">\n' + '\n'.join(pages) + '\n' + css + ed + '\n</body></html>\n')
print('ok')
