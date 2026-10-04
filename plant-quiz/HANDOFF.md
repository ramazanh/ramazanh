# Plant quiz funnel: handoff

Not committed. Source is in `src/`, last built files are in `built/`.

## What it is
Mobile quiz funnel for US women, English copy. Persona Maya, 34: inherited her late uncle's 70-year-old ~15-ft leggy Monstera, grieving, afraid of killing it, family pressure, skeptical of salesy things. Must also work for any plant owner. Opens inside Facebook's in-app browser, so every step must fit one small screen (no scrolling, except long article pages).

## Build
`src/quiz.html` is the base (all JS and CSS in one file).
`python3 src/mkstyle.py` writes quiz_c.html (watercolor), quiz_d.html (retro 70s), quiz_g.html (game). It reads quiz.html from the current dir.
`python3 src/mkvariants.py` runs mkstyle then writes v_c_qf, v_c_long, v_c_plan, v_c_grow, v_d_long, v_g_game (a `var LV` landing variant per file).
Checks: `node src/fitcheck.js v_c_qf` (Playwright, set NODE_PATH=$(npm root -g), chromium at /opt/pw-browsers/chromium) tests overflow at 360x560 and 390x664. Run files one at a time, it is slow.
Publish with the Artifact tool. Capabilities for email: {"db":{"rules":[{"path":"signups","read":"owner","write":"owner"},{"path":"signups/{self}","read":"interact","write":"interact"}]},"user":{}}.

## Published artifacts (private)
1 C Long Read https://claude.ai/artifact/Rq9a91CBXKwAcyhZmQ2se9
2 C Quiz First https://claude.ai/artifact/DGqZ7yFv49GaJ1csXCrcdA
3 C Plan Preview https://claude.ai/artifact/FrajJ2C1N137zbcKM816Lz
4 C Growing Plant (animated) https://claude.ai/artifact/BvhqDHhMrMT245kotxEf2w
5 D Retro Long Read https://claude.ai/artifact/L5TMpSBCVjHBZqs14DCaEa
6 Game (Royal Match-inspired, not a copy) https://claude.ai/artifact/Cs1BCCMXmhqCNo7u9UtRtu
Also: landing options page https://claude.ai/artifact/8rhLZqUsJR6dt6m1sQZREs

## Flow
Landing (variant) -> "How did this plant find you?" -> "How does it look right now?" chips -> "Tonight's one thing" tip with animated finger test -> ~10 questions (few get replies, rest auto-advance) with a "Did you know" page and a community page -> name -> plan page (sticky "Save my plan") -> email page -> thank you (funnel ends).

## Decisions
- Final deciders: funnel/CRO expert and Genesis Media CMO. Both chose Quiz First as skeleton.
- No "Restart" button. Back links only.
- CTA must be fixed and always visible. Never use "free plan", "start my plan", "get my plan", "join", "unlock". Current labels: "Continue" (disabled "Choose one to continue" until a tap), "See what it needs", "Check on my plant".
- Copy: 5th-6th grade, no em-dashes, no fake numbers or testimonials, no survival promises. Botanist-checked facts only.
- Email caveat: db writes need Contributor access, anonymous ad visitors cannot save; nothing sends emails. A real form service is needed before launch.

## Open problems (do these first)
1. CONTRAST. The owner says colors are not contrasty. No numeric audit was ever run. Compute WCAG ratios for every text/background and button pair in all themes (light and dark) and fix tokens. Suspects: muted text, pink CTA with white text, watercolor outlines, retro browns, game white text on blue, disabled button. Target 4.5:1 body, 3:1 large text and UI edges.
2. Finish the fit check for v_c_plan and v_g_game at 360x560 (last fix not verified).
3. Apply the "comprehensive" plan: 10 plant cards (Monstera, Pothos, Philodendron, Fiddle or rubber, Snake or ZZ, Succulent/cactus/aloe, Peace lily, Orchid, Spider plant, Other), 8 situations, a "Building your plan" loader (only real inputs), a "Your plant profile" screen with 4 meters (Light, Water rhythm, Confidence, Pot setup), and a commitment screen.
4. Ad copy for each landing is in landing6.html ("Ad copy that leads here"). Avoid "Did you inherit..." (Meta personal-attribute rule).
