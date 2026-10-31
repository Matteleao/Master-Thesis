# IQL v0.6 blank from the author's v0.5 blank: Codex analysis + guide gaps + author decisions (30-31/10/2026).
import re, sys
SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c >= 1, ('missing', a[:90]); assert n == 0 or c == n, ('count', a[:90], c); s = s.replace(a, b)
def opts(*labels):
    return '<div class="options stack ">' + ''.join(f'<span class="option"><span class="check"></span><span>{l}</span></span>' for l in labels) + '</div>'
rep('v0.5', 'v0.6', 0)
rep('authorised', 'authorized', 0)
rep('Summarise', 'Summarize', 0)
rep('Not conforming', 'Non-conforming', 0)
# A
rep('<p>Link to PSEAR (screening and eligibility) or PFVR (follow-up) as applicable. Clinical interpretation, eligibility decisions and sponsor or central endpoint review remain in their authoritative records.</p>',
    '<p>Link each set to the record that uses it: PSEAR (screening and eligibility), ICDL (immediate postoperative image) or PFVR (follow-up). Those records keep the consequence of the image for the participant; the IQL keeps the technical assessment. Clinical interpretation, eligibility decisions and sponsor or central endpoint review remain in their authoritative records.</p>')
rep('<td>IQL Record ID + image-set ID; participant, time point and linked PSEAR/PFVR ID.</td>', '<td>IQL Record ID + image-set ID; participant, time point and linked PSEAR, ICDL or PFVR ID.</td>')
rep('<td>Whether the set is complete, technically adequate and locally usable for its defined purpose; identify any limitation, repeat or second review needed.</td>',
    '<td>Whether the set is complete, technically adequate and usable for its stated purpose (eligibility, postoperative check or follow-up); identify any limitation, repeat or second review needed.</td>')
rep('<td>Traceable image-set status for PSEAR/PFVR and a linked response for unresolved or recurring quality issues.</td><td>Image-set resolution record; SART, deviation, IMC, SRR or CAPA ID when applicable. FUCR receives visit evidence from PFVR.</td>',
    '<td>Traceable image-set status for the PSEAR, ICDL or PFVR; set-based counts for the FUCR and the PIR; a linked response for unresolved or recurring quality issues.</td><td>Image-set log (C) and period summary (D). The FUCR reads visit counts from the PFVR and image-set counts from the IQL. SART, deviation, IMC, SRR or CAPA ID when applicable.</td>')
# B guide rows: clarify Not assessed vs Not usable, add set relationship
m = re.search(r'(<table class="reference-guide">.*?<tbody>)(.*?)(</tbody>)', s, re.S)
rows = m.group(2)
rows = rows.replace('No images available: Not assessed.', 'No images available, or not yet reviewed: Not assessed (local use is then normally Pending).')
rows = rows.replace('A necessary second review is outstanding: Pending.', 'A necessary second review is outstanding: Pending. Not usable means the set was assessed and cannot serve its stated purpose.')
rows += ('<tr><td class="first-col">Set relationship</td><td>Identify a repeat or supplemental set and link it to the original.</td>'
         '<td>A repeat gets a new Set ID and names the original in "Related set". The original entry, with its timing, stays as recorded.</td></tr>')
s = s[:m.start(2)] + rows + s[m.end(2):]
# C table: new columns
t0 = s.find('<table class="quality-log">'); t1 = s.find('</table>', t0) + len('</table>')
hdr = ['Set ID', 'Participant / Time Point', 'Linked Record (PSEAR, ICDL or PFVR) ID', 'Purpose of Local Use', 'Set Type / Related Set', 'Modality / Required Set / Requirement Ref.', 'Planned Window / Actual Acquisition Date',
       'Timing', 'Required Set Complete?', 'Technical Quality', 'Local Use Decision', 'Archive / Transfer / Receipt', 'Reviewer / Date', 'Resolution / Route ID']
w = [4, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 9, 6, 5]
col = ''.join(f'<col style="width:{x}%">' for x in w)
body = ''
for i in range(1, 6):
    body += (f'<tr><td class="first-col">0{i}</td><td></td><td></td>'
             f'<td>{opts("Eligibility", "Post-op check", "Follow-up", "Other")}</td>'
             f'<td>{opts("Original", "Repeat", "Supplemental")}<span class="rel">Related: ____</span></td><td></td><td></td>'
             f'<td>{opts("In window", "Outside", "Pending", "N/A")}</td><td>{opts("Complete", "Partial", "Missing", "N/A")}</td>'
             f'<td>{opts("Adequate", "Limited", "Non-conforming", "Not assessed")}</td><td>{opts("Usable", "Limited use", "Pending", "Not usable")}</td>'
             f'<td>{opts("Archived", "Transferred", "Receipt confirmed")}<span class="rel">Ref.: ____</span></td><td></td><td></td></tr>')
s = s[:t0] + f'<table class="quality-log"><colgroup>{col}</colgroup><thead><tr>' + ''.join(f'<th>{h}</th>' for h in hdr) + f'</tr></thead><tbody>{body}</tbody></table>' + s[t1:]
rep('<div class="guide">One row per image set. Link PSEAR/PFVR when applicable.', '<div class="guide">One row per image set. Link the PSEAR, ICDL or PFVR that uses it, and state the purpose for which the set is judged.')
# D: period, denominator, unit, overlap; extra rows
rep('<div class="meta-cell"><span class="meta-label">Image-set IDs / Scope Reviewed</span><span class="meta-entry"></span></div><div class="meta-cell"><span class="meta-label">Distinct Image Sets Reviewed (N)</span><span class="meta-entry"></span></div>',
    '<div class="meta-cell"><span class="meta-label">Review Period / Image-set IDs Reviewed (source range)</span><span class="meta-entry"></span></div><div class="meta-cell"><span class="meta-label">Distinct Image Sets Reviewed (N, counted per set, not per participant)</span><span class="meta-entry"></span></div>')
rep('Record the distinct-set count and relevant IDs; categories may overlap.', 'Record the distinct-set count and relevant IDs; a set may appear in more than one row. These set-based counts go to the FUCR (follow-up sets) and the PIR.')
rep('<tr><td class="first-col">Repeat acquisition / second review required during period</td><td></td><td></td></tr>',
    '<tr><td class="first-col">Timing — acquired outside its window</td><td></td><td></td></tr>'
    '<tr><td class="first-col">Repeat acquisition / second review required during period</td><td></td><td></td></tr>'
    '<tr><td class="first-col">Scheduled time unsuitable for a reproducible position (raised with the sponsor)</td><td></td><td></td></tr>')
# E guide
rep('<div class="guide">Record immediate resolution and evidence of the resulting use decision. Cite a CAPA, risk, deviation or safety record when that route is needed.',
    '<div class="guide">Open a line only for a set with an issue, limitation, repeat, second review or route. Record immediate resolution and evidence of the resulting use decision. Cite a CAPA, risk, deviation, safety or sponsor record when that route is needed.')
# F guide: covers only the reviewed sets
rep('<div class="guide">Select the status reflecting the highest unresolved issue in the reviewed scope.', '<div class="guide">Select the status reflecting the highest unresolved issue in the reviewed scope; it covers only the sets reviewed in this period.')
css = '<style>.quality-log .rel{display:block;margin-top:2px;font-size:7.4px;color:#5f6670;text-align:left}.quality-log th{font-size:7.6px;padding:3px 2px}.quality-log .options{font-size:7.2px}.review-log td{height:50px!important;padding:3px 6px!important}.reference-guide td{height:58px!important;padding:3px 6px!important;line-height:1.22}.scope-table td{padding:3px 6px!important;line-height:1.22}</style>\n'
i = s.rfind('</head>'); s = s[:i] + css + s[i:]
open(OUT, 'w').write(s); print('ok')
