---
name: viz-design-conventions
description: "Felipe's design conventions for the thesis governance diagrams (accountability web, delegation network)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 33696f8b-709d-44a6-a8bf-1fce257e8102
---

For the master's-thesis interactive HTML diagrams (Accountability Web, Delegation Network — surgical shoulder device site), Felipe has repeatedly asked for these conventions:

- **Valence-shell concentric layout**: PI at core, then shells outward (Shell 1 = direct PI contact, Shell 2 = via nucleus leader, Shell 3 = operational). A dashed boundary circle separates SITE from EXTERNAL OVERSIGHT. Guide rings must be **visible** (not near-transparent).
- **Generous spacing** — nodes should not crowd; aim ~30–40px gaps. He dislikes compacted/overlapping nodes.
- **Colour = the node's nucleus/area** (clinical=blue, coordination=teal, data=purple, nursing=green, quality=orange, regulatory=red, PI=gold, external=slate). Edge **labels/chips AND arrows must inherit the colour of the receiving/target role** — never all-green.
- **Edge label chips**: small rounded boxes with the role-coloured border, placed **beside** the arrow (offset), never on top of the line; text must be fully readable.
- **Text must stay fully inside circles** (wrap to lines + auto-shrink font).
- **Hover a node → tooltip box** listing that role's tasks. Click = pinned detail panel.
- Avoid "negative-looking" UI (no red ✕ badges for PI's retained duties — those are responsibilities, show positively or just in hover).
- Two distinct relationship axes: **accountability** (vertical, transitive to PI, solid) vs **lateral/operational coordination** (between areas, dashed teal). Keep them visually separate.

**Why:** these came from multiple rounds of explicit correction.
**How to apply:** reuse the same palette + valence-shell geometry across all thesis diagrams for consistency; the Figma version should match. See [[surgical-site-roles]] for which roles belong.
