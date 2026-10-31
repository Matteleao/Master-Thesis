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
hdr = ['Set ID', 'Participant /<br>Time Point', 'Linked Record ID', 'Purpose', 'Set Type /<br>Related Set', 'Modality /<br>Required Set', 'Window /<br>Acquired',
       'Timing', 'Completeness', 'Technical Quality', 'Local Use', 'Archive', 'Reviewer /<br>Date', 'Resolution /<br>Route ID']
w = [4, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 6, 7]
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
rep('Record the distinct-set count and relevant IDs; categories may overlap.', 'For each aspect, give the number of sets affected out of the N reviewed above; a set may appear in more than one row. These set-based counts go to the FUCR (follow-up sets) and the PIR.')
rep('<tr><td class="first-col">Repeat acquisition / second review required during period</td><td></td><td></td></tr>',
    '<tr><td class="first-col">Timing — acquired outside its window</td><td></td><td></td></tr>'
    '<tr><td class="first-col">Repeat acquisition / second review required during period</td><td></td><td></td></tr>'
    '<tr><td class="first-col">Scheduled time unsuitable for a reproducible position (raised with the sponsor)</td><td></td><td></td></tr>')
# E guide
rep('<div class="guide">Record immediate resolution and evidence of the resulting use decision. Cite a CAPA, risk, deviation or safety record when that route is needed.',
    '<div class="guide">Open a line only for a set with an issue, limitation, repeat, second review or route. Record immediate resolution and evidence of the resulting use decision. Cite a CAPA, risk, deviation, safety or sponsor record when that route is needed.')
# F guide: covers only the reviewed sets
rep('<div class="guide">Select the status reflecting the highest unresolved issue in the reviewed scope.', '<div class="guide">Select the status reflecting the highest unresolved issue in the reviewed scope; it covers only the sets reviewed in this period.')

# ---- round 2 (31/10): header, purpose, page strips, PI box
s = re.sub(r'<div class="title">IQL — Imaging Quality Log</div><div class="version">v0\.6 · ([^<]*)</div>',
           lambda m: f'<div><div class="title">IQL — Imaging Quality Log</div><div class="subtitle">{m.group(1)}</div></div><div class="version">v0.6</div>', s)
subs = iter(['Identification, purpose and classification guide', 'Image-set log', 'Period summary and resolution', 'Conclusion and sign-off'])
s = re.sub(r'<div class="subtitle">[^<]*</div>', lambda m: f'<div class="subtitle">{next(subs)}</div>', s)
i = s.find('<section class="meta-grid log-meta">'); j = s.find('</section>', i) + len('</section>')
cells = ['Study / Protocol', 'CIP Version', 'Site / Code', 'IQL Record ID / Revision', 'Review Period / Cut-off Date', 'Imaging Charter / Manual ID and Version',
         'Modalities and Time Points Covered', 'Imaging Unit / Equipment', 'Archive and Transfer Route (PACS, Sponsor Portal)', 'Local Imaging Reviewer / Role', 'Log Owner / Role', 'Controlled Record Location']
s = s[:i] + '<section class="meta-grid log-meta">' + ''.join(f'<div class="meta-cell"><span class="meta-label">{c}</span><span class="meta-entry"></span></div>' for c in cells) + '</section>' + s[j:]
i = s.find('<div class="box">', s.find('Purpose and Use')); j = s.find('</table>', i) + len('</table>')
s = s[:i] + ('<div class="box"><p>Record each required image set when it is acquired or first available, against the sponsor imaging charter or manual: timing, completeness, technical quality, the local use decision and where the images are kept.</p>'
             '<p>Section C is the log: one row per set, on as many log sheets as needed. Sections D to G are completed once per review period and cover every set logged in it. The record that uses the set (PSEAR, ICDL or PFVR) keeps its consequence for the participant; the IQL keeps the technical assessment.</p></div>'
             '<table class="scope-table purpose-h"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup>'
             '<thead><tr><th>Unit of analysis</th><th>Decision supported</th><th>Inputs</th><th>Outputs</th></tr></thead><tbody><tr>'
             '<td>One image set: one participant, one time point.</td><td>Whether the set is complete, adequate and usable for its stated purpose.</td>'
             '<td>Imaging charter or manual; the images and their metadata; the linked PSEAR, ICDL or PFVR.</td><td>Set status for the linked record; set counts for the FUCR and the PIR; routes for open issues.</td></tr></tbody></table>') + s[j:]
s = re.sub(r'<section class="meta-grid continuation-meta">.*?</section>', '', s, flags=re.S)
rep('Accountable Local Review and Record Location', 'Accountable Local Review')
strip = '<section class="meta-grid continuation-meta">' + ''.join(f'<div class="meta-cell"><span class="meta-label">{c}</span><span class="meta-entry"></span></div>' for c in ['Study / Site Code', 'IQL Record ID / Revision', 'Review Period', 'Log Sheet No. / Total']) + '</section>'
k = s.find('</header>', s.find('<main class="page p2')) + len('</header>'); s = s[:k] + strip + s[k:]
rep('<span class="meta-label">Review Period / Image-set IDs Reviewed (source range)</span>', '<span class="meta-label">Log Sheets Reviewed</span>')
rep('<span class="meta-label">Distinct Image Sets Reviewed (N, counted per set, not per participant)</span>', '<span class="meta-label">Distinct Image Sets Reviewed (N)</span>')
i = s.find('<div class="writebox pi-basis">'); j = s.find('</section>', s.find('<section class="meta-grid record-location">')) + len('</section>')
s = s[:i] + ('<section class="meta-grid record-location"><div class="meta-cell"><span class="meta-label">PI Review · Trigger or Governing Reference</span>'
             '<div class="options inline pi-opts"><span class="option"><span class="check"></span><span>Required</span></span><span class="option"><span class="check"></span><span>Not required</span></span></div><span class="meta-entry"></span></div>'
             '<div class="meta-cell"><span class="meta-label">Next Review Date / Trigger</span><span class="meta-entry"></span></div></section>') + s[j:]

# ---- round 3 (31/10): D and E headers, extra E row, centered headers and PI cell
rep('<th>Count / N and Image-set IDs</th><th>Finding / No Further Action or Linked Route</th>', '<th>Sets Affected</th><th>Finding or Linked Route</th>')
rep('<th>Resolution ID / Set ID / Issue / Use Impact</th><th>Immediate Response / Repeat / Second Review</th><th>Resolution Evidence / Updated Local Use / Date</th><th>Linked Participant / Governed Record</th><th>Owner / Due Date</th><th>Status</th>',
    '<th>Resolution ID /<br>Set ID</th><th>Issue and Immediate Response</th><th>Evidence /<br>Updated Use</th><th>Linked Record</th><th>Owner /<br>Due Date</th><th>Status</th>')
i = s.find('<table class="resolution-log"'); j = s.find('</tbody>', i); k = s.rfind('<tr>', i, j)
s = s[:j] + s[k:j] + s[j:]
rep('<div class="meta-cell"><span class="meta-label">PI Review · Trigger or Governing Reference</span>', '<div class="meta-cell pi-cell"><span class="meta-label">PI Review · Trigger or Governing Reference</span>')
css = '<style>.quality-log .rel{display:block;margin-top:2px;font-size:7.4px;color:#5f6670;text-align:left}.quality-log th{font-size:7.6px;padding:3px 2px}.quality-log .options{font-size:7.2px}.review-log td{height:50px!important;padding:3px 6px!important}.reference-guide td{height:58px!important;padding:3px 6px!important;line-height:1.22}.scope-table td{padding:3px 6px!important;line-height:1.22}.topbar .subtitle{font-size:9.5px;color:#d7e2ee;margin-top:2px;text-transform:none}.purpose-h th{text-align:center}.purpose-h td{height:40px;vertical-align:top;text-align:left;font-weight:400!important;color:inherit!important;background:none!important}.log-meta .meta-cell{min-height:58px!important}.pi-opts{display:flex;gap:28px;margin:10px 7px 0;justify-content:center}.record-location .meta-label{text-align:center}.reference-guide th,.review-log th,.resolution-log th,.conclusion-table th{text-align:center!important}.log-meta .meta-cell{min-height:66px!important}.reference-guide td{height:84px!important}.quality-log td{height:91px!important}.review-log td{height:55px!important}.resolution-log td{height:75px!important}.conclusion-table td{height:62px!important}.conclusion-basis{min-height:240px!important}.signature{min-height:170px!important}.record-location .meta-cell{min-height:62px}</style>\n'
i = s.rfind('</head>'); s = s[:i] + css + s[i:]
open(OUT, 'w').write(s); print('ok')
