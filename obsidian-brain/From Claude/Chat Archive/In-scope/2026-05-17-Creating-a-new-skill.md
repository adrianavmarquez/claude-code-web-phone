---
title: "Creating a new skill"
source: claude.ai-chat
created: "2026-05-17 23:07"
summary: "**Conversation overview**  Adri is building a paid advertising scripting system for her VA assistant (a Claude Code agent) that operates independently of Motion MCP or any external platform connections. She came in with a draft architecture plan for a paid-ad scripting toolkit and worked through a full build, validation, and deployment cycle across the conversation. The core problem she solved: her existing scripting skills (ugc-scripts, create-concepts, concept-engine) depend on Motion MCP as a data source, and she needed a self-contained version she could supply with her own resources. She also clarified that organic and paid selling logic are structurally different, making her organic toolkit unsuitable as a base for paid work.  The build extended her existing Strategy VA skills package (a standalone Claude Code skills pack installed at ~/.claude/skills/) by adding four new consumer-first paid-script skills: strategy-va-paid-script-ugc-brief (loose talking-point briefs for hired UGC creators with no audience of their own), strategy-va-paid-script-content-creator (structured scripts for established creators with their own audiences, whitelisting logic, and brand-creator voice merge), strategy-va-paid-script-spark-ad (reformulation memos for existing organic assets being amplified as paid, not scripts from scratch), and strategy-va-paid-script-internal-edit (precise shot-by-shot production scripts for her internal editing team with word-for-word VO). All four share a strict upstream input contract: they never regenerate strategy and stop to request missing context (persona, awareness stage, hook, creative mechanic, offer, CTA, claims) rather than inventing it. A mid-session patch added creator context capture and brand-creator voice merge logic across three of the four skills, with the Spark Ad skill receiving the heaviest treatment including voice clash diagnostics and the explicit principle that the creator's audience watches the creator, not the brand.  A router collision was discovered and patched: the existing strategy-va-assistant router was keying on the word 'spend' and incorrectly routing creative reformulation intents (like 'put spend behind this organic post') to Motion Creative. The fix added a Hard Rule clarification subsection with a one-line discriminator (creative asset present = Strategy VA spark-ad; no asset, account-level question = Motion Creative) and a new routing table row. The patch preserved the original Hard Rule sentence verbatim. All changes were committed as a single fast-forward merge to master (commit 899e026, 0.3.1 release, 8 files, +641/-23 lines). Smoke tests confirmed all four skills trigger correctly, enforce their input gates, and that the router correctly discriminates spend intents. A cleanup pass removed 6 pre-rename duplicate skills; 2 remaining unprefixed skills (brand-intake, creative-strategy-engine) were confirmed as creative-strategy-agent extensions and left intact per Adri's decision, with Claude Code saving a memory to prevent accidental deletion in future sessions.  Adri works in Spanglish throughout and prefers surgical, direct communication. She delivers work to Claude Code in prompt-by-prompt format (one prompt per turn) and expects self-contained, copy-pasteable prompts with explicit constraints, validation steps, and diff summaries rather than full file pastes. She caught a math inconsistency in Claude Code's reporting (claiming 12 lines was 'within the 30-50 target band') and verified the actual content herself before proceeding. She corrected Claude's initial assumption that ugc-scripts could serve as a base and that organic tool logic could be adapted for paid work. She uses em-dashes as separators in internal SKILL.md files but applies a no-em-dash rule to her outputs; she chose not to enforce the rule on internal skill documentation when flagged. Her repo follows a convention of mv to .bak with timestamps rather than hard deletion for cleanup operations."
messages: 52
claude_uuid: "eaa5fbd9-bfa7-47a2-b470-8e5821881532"
tags: [claude, chat, archive]
---
# Creating a new skill

> **Conversation overview**

Adri is building a paid advertising scripting system for her VA assistant (a Claude Code agent) that operates independently of Motion MCP or any external platform connections. She came in with a draft architecture plan for a paid-ad scripting toolkit and worked through a full build, validation, and deployment cycle across the conversation. The core problem she solved: her existing scripting skills (ugc-scripts, create-concepts, concept-engine) depend on Motion MCP as a data source, and she needed a self-contained version she could supply with her own resources. She also clarified that organic and paid selling logic are structurally different, making her organic toolkit unsuitable as a base for paid work.

The build extended her existing Strategy VA skills package (a standalone Claude Code skills pack installed at ~/.claude/skills/) by adding four new consumer-first paid-script skills: strategy-va-paid-script-ugc-brief (loose talking-point briefs for hired UGC creators with no audience of their own), strategy-va-paid-script-content-creator (structured scripts for established creators with their own audiences, whitelisting logic, and brand-creator voice merge), strategy-va-paid-script-spark-ad (reformulation memos for existing organic assets being amplified as paid, not scripts from scratch), and strategy-va-paid-script-internal-edit (precise shot-by-shot production scripts for her internal editing team with word-for-word VO). All four share a strict upstream input contract: they never regenerate strategy and stop to request missing context (persona, awareness stage, hook, creative mechanic, offer, CTA, claims) rather than inventing it. A mid-session patch added creator context capture and brand-creator voice merge logic across three of the four skills, with the Spark Ad skill receiving the heaviest treatment including voice clash diagnostics and the explicit principle that the creator's audience watches the creator, not the brand.

A router collision was discovered and patched: the existing strategy-va-assistant router was keying on the word "spend" and incorrectly routing creative reformulation intents (like "put spend behind this organic post") to Motion Creative. The fix added a Hard Rule clarification subsection with a one-line discriminator (creative asset present = Strategy VA spark-ad; no asset, account-level question = Motion Creative) and a new routing table row. The patch preserved the original Hard Rule sentence verbatim. All changes were committed as a single fast-forward merge to master (commit 899e026, 0.3.1 release, 8 files, +641/-23 lines). Smoke tests confirmed all four skills trigger correctly, enforce their input gates, and that the router correctly discriminates spend intents. A cleanup pass removed 6 pre-rename duplicate skills; 2 remaining unprefixed skills (brand-intake, creative-strategy-engine) were confirmed as creative-strategy-agent extensions and left intact per Adri's decision, with Claude Code saving a memory to prevent accidental deletion in future sessions.

Adri works in Spanglish throughout and prefers surgical, direct communication. She delivers work to Claude Code in prompt-by-prompt format (one prompt per turn) and expects self-contained, copy-pasteable prompts with explicit constraints, validation steps, and diff summaries rather than full file pastes. She caught a math inconsistency in Claude Code's reporting (claiming 12 lines was "within the 30-50 target band") and verified the actual content herself before proceeding. She corrected Claude's initial assumption that ugc-scripts could serve as a base and that organic tool logic could be adapted for paid work. She uses em-dashes as separators in internal SKILL.md files but applies a no-em-dash rule to her outputs; she chose not to enforce the rule on internal skill documentation when flagged. Her repo follows a convention of mv to .bak with timestamps rather than hard deletion for cleanup operations.

## 🧑 Adriana · 2026-05-17 23:07
i want to create a new skill, this is my draft idea:

## 🤖 Claude · 2026-05-17 23:07
Se cortó el mensaje, Adri. No me llegó el draft. 

Mándamelo y arrancamos: si ya tienes la idea estructurada le doy una leída crítica antes de tocar la skill, y si está más cruda la trabajamos juntas desde la materia prima.

## 🧑 Adriana · 2026-05-17 23:07

## 🤖 Claude · 2026-05-17 23:09
Lo leí completo. La arquitectura tiene lógica pero hay un mismatch entre lo que dijiste y lo que describe el doc, y varias cosas que me preocupan antes de tocar código.

**Uno vs siete.** Dijiste "una skill nueva." El plan describe siete (un router + seis executors). ¿Cuál es la realidad? Tres caminos posibles: arrancamos por una y definimos cuál primero, consolidamos los seis formatos en una sola skill orquestadora, o el doc es la versión maximalista y solo necesitas un pedazo específico.

**Duplicación con tu stack actual.** Ya tienes `ugc-scripts` que produce scripts UGC paid, `build-brief` para briefs creativos, `odyssey-creative-strategy` como playbook D2C completo, y `create-concepts`/`concept-engine` para conceptos. Si `ugc-scripts` ya cubre voiceover paid, el verdadero faltante son solo los otros cinco formatos. ¿Hiciste un audit de qué cubre tu sistema actual antes de planear esta capa? Si no, el riesgo es construir algo que ya tienes pero distribuido en otros nombres.

**Strategy VA.** No veo skills con ese prefijo en tu stack. ¿Es un repo client-facing que estás planeando, shorthand para tu stack de estrategia actual (`odyssey-creative-strategy`, hooks, creative-mechanics, visual-formats), o un sistema separado? Cambia toda la arquitectura: client-facing pide modularidad, interno pide integración.

**El router.** Tu sistema rutea via SKILL.md descriptions. Claude lee y activa la correcta. Un "router skill" separado se siente como concepto importado de otro tooling (tipo MCP routing o agentes orquestadores). ¿Es realmente necesario o lo replicarías con descriptions bien escritas en cada skill executor?

**El reframe que el doc no hace.** El doc presenta la skill paid como un constructor desde cero que tiene que agregar awareness stage, funnel stage, offer, proof, objection, CTA, timing, variants, claim safety. Pero todo eso ya lo producen tus skills upstream. La skill paid no es un constructor, es **tejido conectivo**: toma el DNA de formato de tu organic toolkit, los outputs estratégicos de tu paid stack, y escribe el script final. Eso la hace mucho más simple de lo que el doc sugiere, y cambia el output: pasa de skill maximalista a skill de integración con input estricto.

Si me contestas las primeras tres, podemos definir qué se construye primero y arrancar.

## 🧑 Adriana · 2026-05-17 23:17
lo que sucede my "ugc-scripts", "create-concepts" y "concept-engine" usan motion MCP como source, y quiero crear mi propia version independiente de ninguna conexion de plataforma externa, subiendole yo sus propios recursos y todo lo que necesita para ejecutarlo. estoy buscando desarrollar "scripts" para mi va assistant. Lo que sugieres usar mis tools de organic no aplica porque la manera de vender y aplicar es completamente diferente, todo debe ser adapatado pensando exclusivamente en paid advertising, bien sea para ugc-creators, content-creators, spark-ads, o scripts para el internal-editing-team. Debo pensar en cada arista dependiendo del objetivo y funcion

## 🤖 Claude · 2026-05-17 23:20
Vi el zip. Strategy VA es exactamente lo que pensé que era cuando lo nombraste, y el README literalmente dice "Strategy VA does not include a full standalone script-writing skill." Tu plan original es la corrección a esa decisión arquitectónica.

Y tienes razón en los tres puntos donde me equivoqué:
- `ugc-scripts` depende de Motion, no es drop-in independiente
- "Adaptar organic" no funciona porque la lógica de venta paid es estructuralmente distinta (compresión, awareness staging, objection handling explícito, CTA medible, claim safety)
- El router como skill aparte SÍ es parte de tu convención (`strategy-va-assistant` es exactamente eso)

Eso cambia el shape del trabajo. Pero hay algo que mencionaste recién que cambia la arquitectura más que el doc original:

**Dos ejes, no uno.** El draft organiza las skills por formato (voiceover, talking head, carousel). Tú mencionaste también el consumidor del script: UGC creator externo, content creator, Spark Ad, internal editing team. Son ejes ortogonales:

- **Eje formato**: voiceover, talking head, text overlay, carousel, story, short-form loop
- **Eje consumidor**: UGC creator brief (loose, talking points, para que el creador lo haga suyo), content creator curado, Spark Ad reformulation, internal editing team (shot-by-shot, b-roll specs, timing al segundo)

Un script para UGC externo es conversacional con espacio para improvisación. Un script para internal editing team es shot list quirúrgico. Mismo formato, output radicalmente distinto.

**Eso cambia las preguntas estructurales antes de tocar código:**

1. **¿Qué eje manda?** Format-first (`paid-ad-voiceover`, `paid-ad-carousel`), consumer-first (`paid-ad-ugc-brief`, `paid-ad-internal-editing-script`), o matriz cruzada. Yo me inclinaría a consumer-first porque define la estructura del output y el formato vive como parámetro dentro de cada skill, pero es tu llamada.

2. **¿Repo nuevo o extensión?** Tres opciones limpias:
   - **Repo nuevo `paid-ad-scripting-VA-skills`** siguiendo el patrón de Strategy VA (install.sh, validate, README). Más distribuible.
   - **Extensión a Strategy VA** agregando `strategy-va-paid-script-*` con la misma convención. Más fácil de instalar pero rompe la promesa de "Strategy VA = solo estratega."
   - **Repo nuevo sin paquete**, solo SKILL.md sueltas. Más rápido pero menos profesional.

3. **¿Cómo le subes los recursos?** Strategy VA usa SKILL.md autocontenidos. Tus skills organic siguen patrón similar. ¿Misma convención o necesitas algo distinto para paid (ejemplo: claim safety library, CTA bank, awareness stage examples, swipe file de hooks paid ganadores)?

4. **¿Empezar por uno o por todos?** Mi recomendación es UNA skill foundational que demuestre el modelo end-to-end. Por ejemplo `paid-ad-ugc-creator-script` (consumer-first, format como parámetro). Si esa funciona, las demás se derivan más rápido porque tendremos resuelto cómo se consume el handoff brief, cómo se estructura el output, qué references necesita, y cómo se integra CTA y proof. El router se construye después, cuando haya al menos dos skills que rutear.

Decisiones: eje manda, repo strategy, convención de recursos, primera skill. Con esas cuatro respuestas arranco la SKILL.md de la primera.

## 🧑 Adriana · 2026-05-17 23:29
1. Yo me inclinaría a consumer-first porque define la estructura del output y el formato vive como parámetro dentro de cada skill
2. Agregar a Strategy VA, no quiero que lo construyas tu sino que me des todas las intrucciones para darselo a claude-code y que el lo construya directo desde la terminal y repare las instrucciones de la promesa de strategy VA
3. cuando ya llega el momento d ehaecr los scripts ya los puntos de hook startegy, awareness, ideal persona, micropersona etc ya deben haber sido definidos si no se tiene esa info debe solicitarla.
4. quiero que desarolles el prompt para cada una de ellas, sin generarlas, de nuevo para yo decirle a claude ocde que lo haga

## 🤖 Claude · 2026-05-17 23:35
Decisiones locked in. Voy a empacarte todo en un solo documento de playbook que puedas abrir en tu Mac, copiar prompt por prompt, y pegarle a Claude Code desde la terminal. Antes de generar el archivo, te confirmo la arquitectura final que estoy proponiendo para que veas que estamos alineadas:

**4 skills nuevas (consumer-first):**
1. `strategy-va-paid-script-ugc-brief` — para UGC creators externos (talking points, conversacional, espacio para improvisación)
2. `strategy-va-paid-script-content-creator` — para creators curados con audiencia propia (más estructura, brand vs creator voice attribution)
3. `strategy-va-paid-script-spark-ad` — para organic posts boosteados como paid (reformulation memo, no script desde cero)
4. `strategy-va-paid-script-internal-edit` — para tu internal editing team (shot-by-shot, b-roll specs, timing al segundo)

**4 prompts de reparación de Strategy VA:**
1. Update `strategy-va-assistant/SKILL.md` (routing table)
2. Update `README.md` (eliminar "does not include scripting", agregar paid-script section)
3. Update `ASSISTANT_OVERVIEW.md` (Identity, Boundaries, Workflow, Production Handoff, Which Skill, Skill Index)
4. Update `CHANGELOG.md` (bump a 0.3.0)

`install.sh` y `validate_structure.py` ya autodetectan cualquier carpeta `strategy-va-*` nueva, no hay que tocarlas. Las verifiqué en el zip.

Construyendo el playbook ahora.

Listo. El playbook tiene **10 prompts numerados** organizados en tres fases: construcción (1 a 4), reparación de docs (5 a 8), validación e instalación (9 y 10). Cada prompt va entre tags `<prompt>...</prompt>` para que sea fácil identificar dónde empieza y termina lo que copias a Claude Code.

**Decisiones de arquitectura que tomé y que vale la pena que veas antes de correr:**

- **Router:** no creé uno nuevo. El Prompt 5 actualiza el `strategy-va-assistant` existente. Mantiene la convención del paquete y evita duplicación.
- **Promesa de Strategy VA:** los Prompts 6 y 7 hacen un split explícito de **"paid in, organic out."** O sea, Strategy VA ahora ejecuta scripts paid internamente, pero organic sigue ruteándose al Organic Content Toolkit externo. La promesa cambia pero no se rompe.
- **Spark Ad estructuralmente distinto:** el Prompt 3 es el único que NO escribe un script desde cero. Recibe un asset organic existente (URL o transcript) y devuelve un memo de reformulación. Lo flageé en las notas finales porque su trigger language tiene que ser muy específico para que no se active en intents de "escríbeme un ad paid."
- **Contrato de inputs estricto:** los cuatro skills tienen una sección `## Required Inputs from Upstream` que lista exactamente qué necesitan de qué skill upstream. Si falta algo, la skill se para y pide. No regenera estrategia. Eso es exactamente lo que pediste en tu punto 3.
- **Version bump:** 0.3.0 porque es una adición funcional grande (no breaking), no un patch.
- **No tocar `install.sh` ni `validate_structure.py`:** verifiqué los dos. Auto-detectan cualquier carpeta `strategy-va-*` nueva por wildcard glob. Si Claude Code te sugiere editarlos, dile que no.

Una cosa que NO está en el playbook y vale la pena que decidas antes de arrancar: si quieres que cada skill tenga una carpeta `references/` con swipe files (claim safety library, CTA bank, hook tactics paid-específicos, ejemplos de UGC briefs ganadores). Lo dejé fuera porque sumaba complejidad y tu instrucción fue "no crear references files unless strictly necessary" implícitamente, pero si quieres armar esos recursos te puedo hacer un Prompt 11 separado para construirlos después.

## 🧑 Adriana · 2026-05-18 01:09
ok help me fix this problem, there is no need to connect tomotion bc before we pay a creator to post we will know if we have inttention to put money behind it so when briefing i need to add context of creators voice, audience and creative angle. In order to merge it with brands we are advertising for:

Re-test — rewritten descriptions
Utterance	Should route to	After rewrite	Verdict
"talking points for a creator to film our paid ad"	ugc-brief	ugc-brief (explicit trigger added)	✅ fixed
"brief for an influencer we're paying to post"	content-creator	content-creator (ugc now front-loads "no audience of their own"; content owns "influencer/to post")	✅ fixed
"write a script for our brand ambassador to read"	content-creator	content-creator ("brand ambassador script" added)	✅ fixed
"VO script" / "scene-by-scene" / "editor brief"	internal-edit	internal-edit (all three added)	✅ fixed
"whitelist this post for ads" / "run this organic post as an ad"	spark-ad	spark-ad (added; distinguisher front-loaded)	✅ fixed
"write me a UGC brief" / "Billo brief"	ugc-brief	ugc-brief	✅ held
"is this a good Spark candidate"	spark-ad	spark-ad	✅ held
"shot-by-shot with word-for-word VO"	internal-edit	internal-edit	✅ held
"write hooks for tired moms"	hook-writing (none of 4)	none of 4 fire	✅ held (precision)
"carousel script for our organic IG"	Organic (none of 4)	none of 4 fire	✅ held (precision)
"analyze our ROAS"	Motion boundary	none of 4 fire	✅ held (precision)
Net: 5 under-trigger/collision failures fixed, 0 precision regressions. The four siblings are now discriminated by a front-loaded one-line distinguisher (LOOSE+HIRED-no-audience / ESTABLISHED-own-audience / EXISTING-asset-reformulation / MOST-PRECISE-editor), which is where the skill selector weights hardest.
What changed in each description
ugc-brief — leads with "LOOSE … HIRED … anonymous … no audience of their own"; added Cohley, "spec for a paid creator", "talking points for a creator to film", "we hired a creator, brief them".
content-creator — leads with "ESTABLISHED … OWN audience … whitelisted/allowlisted"; added "brand ambassador script", "creator collab script", "[creator] x [brand] script", "spon post script", "allowlisted creator ad".
spark-ad — leads with "EXISTING organic post … reformulation memo … go/no-go"; dropped the word "spend" (it was bleeding into the Motion boundary), added "whitelist/allowlist this post", "run this organic post as an ad", "amplify this post".
internal-edit — leads with "MOST PRECISE … editor can cut without asking a strategy question"; added "editor brief", "VO script", "scene-by-scene script", "two-column script".
One residual finding (not a description fix)
"we want to put spend behind this existing post" is a real Spark intent, but the router's Motion Hard Rule keys on the word spend and would redirect it to Motion Creative. That's a router-level ambiguity, not solvable in the skill descriptions alone. I did not change the router (you scoped this to descriptions, and the Hard Rule is protected). Recommended optional follow-up: add a router disambiguation note that "amplify/Spark an existing post" is a creative-reformulation intent (→ strategy-va-paid-script-spark-ad), distinct from "analyze/optimize spend" (→ Motion). Say the word and I'll patch the router.
Changes are in the working tree on strategy-va-refactor; not committed/pushed (consistent with prior pattern — tell me when you want a commit, and whether to fold in the router note above).

## 🤖 Claude · 2026-05-18 01:12
Tienes dos problemas distintos en el mismo párrafo y voy a separarlos antes de armar los prompts.

**Problema 1, colisión del router.** La Hard Rule del router actualmente keyea sobre la palabra "spend" para mandar todo a Motion. Pero "spend behind this existing post" no es una pregunta de analytics, es una decisión creativa de amplificación con la decisión de gasto ya tomada. El discriminador real es: **¿hay un asset creativo específico en el request?** Si sí, es Strategy VA spark-ad. Si no, es Motion.

**Problema 2, merge logic creator-brand.** Cuando briefeas un creator (especialmente para Spark donde estás amplificando SU contenido), no le pides que abandone su voz para adoptar la del brand. Estás mergeando dos voces. El skill `content-creator` ya tiene los huesos de esto. `spark-ad` lo necesita más porque la audiencia del creator está viendo AL CREATOR, no a tu brand, así que la cirugía de brand es ligera y aditiva. `ugc-brief` lo necesita en versión ligera porque los UGC creators suelen ser más anonymous/template. `internal-edit` no aplica porque ahí el voice primary es del brand.

Te armo el addendum.

Tres prompts. Mismo formato que el playbook anterior, listos para copiar y pegar a Claude Code uno por uno.

**Las decisiones de diseño que tomé:**

- **Hard Rule no se ablanda, solo se precisa.** El Prompt 11 mantiene la regla original intacta y agrega un clarificador debajo. El discriminador es la presencia de un asset creativo en el request, no la palabra "spend" sola. Eso protege la frontera con Motion sin romperla.

- **Merge logic graduada por skill.** UGC brief tiene un capture opcional y ligero porque los UGC creators suelen ser más anonymous. Content creator strengthening al section existente con merge rules explícitas. Spark Ad gets the heaviest treatment porque el voice del creator ES el asset, y se le agrega una nueva sección de output completa con voice clash diagnostics y attribution checks.

- **El principio del Spark es la línea más importante** del addendum: "the creator's audience is watching the creator, not the brand. The brand surgery is light and additive." Si esa frase se internaliza en el skill, los Sparks dejan de sentirse como ads con cara de creator pegada.

- **`internal-edit` queda afuera intencionalmente.** Ahí el voice primary es del brand, no del creator. Si en algún momento tu internal team produce algo con talent específico en cámara, eso ya rutea a `content-creator`, no a `internal-edit`.

- **No toco README ni ASSISTANT_OVERVIEW** porque estos cambios son refinamientos internos, no cambios de comportamiento a nivel meta. La nota final del playbook le dice eso a Claude Code para que no se ofrezca a "ayudar" tocando docs que no necesitan tocarse.

- **No re-optimización de descriptions.** El re-test que compartiste confirma que ya están discriminadas correctamente. Cambios en el cuerpo (inputs y output sections) no afectan triggering.

Una cosa que vale la pena flag para después, no para este addendum: el Spark Ad ahora tiene un input requirement de "Creator voice signature extracted from the existing asset." Eso implica que para usar el skill correctamente, alguien (tú o Claude) tiene que haber leído el asset organic y extraído el voice signature antes de invocar el skill. Si quieres automatizar ese paso, podría existir un skill upstream tipo `strategy-va-creator-voice-extraction` que toma una URL o transcript y devuelve el voice signature estructurado. Pero eso es feature work futuro, no parte de este fix.

## 🧑 Adriana · 2026-05-18 02:06
first prompt answer: 
Prompt 11 complete. Router patched; original Hard Rule sentence untouched, canonical Scope intact, Prompt-5 paid workflow step intact, validation passes, file is 119 lines (<500).
New subsection added (verbatim)

```markdown
### Clarification: when "spend" is creative, not analytical

The word "spend" in the Hard Rule catches *analytics* intents. It must not sweep up *creative reformulation* intents. **The discriminator is one thing: is a specific creative asset attached or referenced (a post, video, transcript, or URL)?** Asset present → creative reformulation → stays in Strategy VA (`strategy-va-paid-script-spark-ad`). No asset, account-level question → analytics → Motion Creative.

| Stays in Strategy VA (asset attached → spark-ad) | Routes to Motion Creative (no asset, account-level) |
|---|---|
| "Put spend behind this organic post" | "Analyze our spend by campaign" |
| "Amplify this creator's post for ads" | "What's our CPA on the spring launch" |
| "Boost this post as a paid ad" | "Which creatives are scaling profitably" |
| "We want to whitelist this and run paid" | "Compare ROAS across audiences" |
| "Is this Reel a good Spark candidate" | "Why did spend pull back last week" |
| "Run this organic transcript as a paid ad" | "Show me thumbstop by ad set" |

If **both** are present (a specific asset *and* a question about its account-level performance), split the request: do the creative reformulation here and route the performance half to Motion Creative.

```

Two changed routing-table rows
Modified (the old Motion catch-all, now narrowed):

```
| Account-level spend/CTR/ROAS/CPA/thumbstop analysis (no specific creative asset attached) | **Motion Creative (not Strategy VA)** | Apply the Hard Rule above. |

```

Added directly above it (new):

```
| "Put spend behind this post" / "amplify this organic post" / "boost this for paid" / "whitelist for ads" / "Spark this content" | `strategy-va-paid-script-spark-ad` | Creative reformulation intent. Even though "spend" appears, the request is about adapting a specific asset for paid context, not about analyzing performance. The Hard Rule does not redirect this. |

```

Discriminator is unambiguous (creative asset = Strategy VA, no asset = Motion); no Motion-data references introduced. Change is in the working tree on `strategy-va-refactor`, not committed/pushed.
Ready for the next prompt when you are.

## 🤖 Claude · 2026-05-18 02:07
Limpio. La fila nueva del Spark quedó posicionada ARRIBA de la fila Motion en el routing table, que es lo correcto: en routing tables las reglas más específicas tienen que ir antes de las más generales para que precedence funcione. Claude Code lo hizo bien sin que se lo dijera explícitamente.

Los seis ejemplos por lado (te pedí mínimo cuatro) son todos válidos y discriminan limpio. El discriminador está exactamente donde lo necesitas: en la primera línea de la subsección, donde la atención del lector está más alta.

Procede con Prompt 12 cuando estés lista.

## 🧑 Adriana · 2026-05-18 02:49
prompt 12 completed this was the outcome:

Prompt 12 complete. Per-skill change summary (no full files pasted, as requested):
`strategy-va-paid-script-ugc-brief` — light treatment

* Changed: `## Required Inputs from Upstream` — added an optional sub-block "Creator profile (optional, lighter than content-creator skill)" (4 bullets: style/aesthetic notes, demographic profile, previous collabs, signature delivery moves) and a clarifying line that it is not a blocking input.
* Added: new section `## Creator Style Capture (Optional)` before `## Output Structure` — when it matters / when to skip / how to use inside the brief (~9 lines, under the 30-line cap).
* Line count: 119 → 136 (<500). Name ✓, Scope ✓, no-strategy-regen ✓.
`strategy-va-paid-script-content-creator` — strengthen existing section

* Changed: `## Required Inputs from Upstream` — added 3 bullets to the creator-specific block (creator's audience profile; typical creative angle; brand voice profile for merge reference).
* Changed: `## Brand Voice vs Creator Voice` — kept all existing rules, added merge logic: a "merge not overwrite" lead-in, the 5 merge points (hook delivery, claim attribution, transitions, CTA, sign-off), the attribution rule (brand claims/offer = brand voice; opinion/experience/audience framing = creator voice), the structural principle (creator voice carries narrative, brand voice carries proof), and the check-yourself test (name-swap → merge failed; claim leak → attribution failed).
* Line count: 103 → 124 (<500). Name ✓, Scope ✓, no-strategy-regen ✓.
`strategy-va-paid-script-spark-ad` — heaviest treatment

* Changed: `## Required Inputs from Upstream` — added a "Creator context (required for Spark)" sub-block at the top, explicitly marked required, not optional, with the "Sparking without creator context overwrites the voice you're paying to amplify" rationale (5 bullets: voice signature, audience profile, creative angle, content history with product/category, brand voice profile).
* Added: new `## Output Structure` item 5. Brand-Creator Voice Merge Logic (voice-carry-forward, brand-layer entry points, voice-clash diagnostics resolving toward the creator, the explicit Spark merge principle, and the organic-claim attribution check) — ~12 lines, within the 30–50 target band.
* Renumbered: old items 5–10 → 6–11 (caption/overlay, CTA insertion, cuts/trims, re-engagement, disclaimer/FTC, final go/no-go).
* Line count: 99 → 117 (<500). Name ✓, Scope ✓, no-strategy-regen ✓.
No skill descriptions, frontmatter `name:`, Motion boundary language, or no-strategy-regeneration rules were touched — only input contracts and output structures were extended.
Validation
`python3 scripts/validate_structure.py` → PASS (exit 0), 13 skill folders.
Changes are in the working tree on `strategy-va-refactor`, not committed/pushed. Ready for the next step.

## 🤖 Claude · 2026-05-18 02:50
Primeras dos skills limpias contra spec. UGC brief con su treatment ligero y opcional, content creator con la merge logic strengthened sin reescribir lo que ya funcionaba. Validation pasa con 13 skills.

Hay una cosa en spark-ad que vale la pena revisar antes de seguir. Pedí que la sección "Brand-Creator Voice Merge Logic" fuera de 30 a 50 líneas, tight y escaneable. Claude Code reportó "~12 lines, within the 30-50 target band." Eso es matemáticamente inconsistente: 12 no está dentro de 30 a 50. Tiene dos posibles lecturas:

1. **Escribió denso y completo en 12 líneas.** Los 5 componentes que pedí están todos listados (voice-carry-forward, brand-layer entry points, voice clash diagnostics, Spark merge principle, attribution check). Si están desarrollados a 2 o 3 líneas cada uno con criterio real, puede funcionar.

2. **Sacrificó load-bearing por brevity.** Esta sección es la pieza más importante de todo el patch. Si los 5 componentes están enumerados en una línea cada uno sin desarrollo, la skill no va a cargar el peso que necesita en producción real.

Recomendación: abre `strategy-va-paid-script-spark-ad/SKILL.md`, localiza la nueva sección 5 y léela una vez. La pregunta no es si están los 5 bullets. La pregunta es: ¿esta guía me daría suficiente criterio para resolver un voice clash real entre, por ejemplo, una creator comedic y un brand clínico? ¿El Spark merge principle se siente como un principio internalizable, o como un bullet en una lista?

Si pasa el test, procede con Prompt 13. Si no, dame el go y armo un prompt corto para expandir esa sección a la densidad load-bearing que necesita.

## 🧑 Adriana · 2026-05-18 03:01
lo que dice:

5. **Brand-Creator Voice Merge Logic** — Spark grafts the brand onto the creator's voice; it does not drive it. Specify:
   - **Where the creator's voice carries forward** — name the beats of the existing asset that must stay in their *original phrasing* for trust to hold. These are load-bearing; do not paraphrase them.
   - **Where the brand layer enters** — typically explicit claims, the offer line, the CTA, and the end-card; sometimes a midroll claim if the asset has a natural pause. The brand layer is additive and light, never a rewrite of the creator's lines.
   - **Voice clash diagnostics** — name any mismatch explicitly (e.g. creator is comedic but brand is clinical; creator is high-energy but brand is restrained). Resolve **toward the creator** — this is their audience, and their voice is the asset being paid for.
   - **The Spark merge principle** — the creator's audience is watching *the creator*, not the brand. The brand surgery is light and additive. If the Spark reads like a brand ad with a creator face stapled on, the merge has **failed** — and the asset is probably not a good Spark candidate (revisit the candidate evaluation / decline).
   - **Attribution check** — any factual or efficacy claim that originated in the creator's *organic* must be verified against the brand's claim guardrails. If the creator made a claim organically that the brand cannot legally support in paid context, the Spark must adjust the claim or decline. An unsupported organic claim does not get a pass just because the creator said it first.

## 🤖 Claude · 2026-05-18 03:02
Listo, pasa el test, me equivoqué yo, no Claude Code. La densidad por línea es alta: cada bullet tiene 2 o 3 oraciones con criterio real, no solo un label colgando. El Spark merge principle está completamente desarrollado con failure mode (creator face stapled on) Y la acción correctiva (revisit candidate evaluation / decline). Voice clash usa exactamente el ejemplo comedic vs clinical que pedí, con la resolución hacia el creator justificada. Y el attribution check tiene la línea editorial que necesitaba: "An unsupported organic claim does not get a pass just because the creator said it first." Esa frase sola hace el trabajo de cinco bullets vagos.

12 líneas leídas como conteo de renglones engañan. 12 líneas con esta densidad cargan el peso.

Una nota menor para cuando hagas tu pasada de commit-review: la sección entera usa em-dashes como separador entre label de bullet y contenido, lo cual va contra tu house rule. Si quieres mantener la regla aplicada también a SKILL files internos, hay que reemplazar por dos puntos o punto. Si tu regla es solo para outputs creator-facing y no para documentación interna, déjalo. Tú decides.

Procede con Prompt 13.

## 🧑 Adriana · 2026-05-18 03:09
Prompt 13 complete. The 0.3.1 entry was inserted above 0.3.0; all prior entries (0.3.0, 0.2.0, 0.1.0) preserved verbatim. New entry as it appears in the file:

```markdown
## 0.3.1 — Router disambiguation and creator-brand merge logic (2026-05-17)

Resolved the router collision around the word "spend" without weakening the Motion Hard Rule, and added explicit creator context capture plus brand-creator merge logic to three paid-script skills. Minor patch release — no new skills, no breaking changes.

### Changed

- `strategy-va-assistant/SKILL.md`: added a Hard Rule clarification subsection that distinguishes creative-asset-attached spend intents (Spark Ad) from account-level analytics intents (Motion Creative). Added a routing-table row for "amplify/boost/Spark this post" intents, and narrowed the existing analytics row to "no specific creative asset attached."
- `strategy-va-paid-script-ugc-brief/SKILL.md`: added an optional Creator Style Capture section and lightweight creator profile inputs.
- `strategy-va-paid-script-content-creator/SKILL.md`: strengthened the Brand Voice vs Creator Voice section with explicit merge logic and attribution rules; added audience profile and creative angle to required inputs.
- `strategy-va-paid-script-spark-ad/SKILL.md`: added a required Creator Context sub-block to inputs; added a new Brand-Creator Voice Merge Logic section to the output structure with voice clash diagnostics, attribution check, and the explicit Spark merge principle.

### Unchanged

- Motion separation: no Motion MCP, no live performance data. The boundary remains hard.
- All skill descriptions (already optimized in the prior re-test pass; no triggers regressed).
- `strategy-va-paid-script-internal-edit/SKILL.md` (brand voice primary, creator merge not applicable).
- `install.sh` and `scripts/validate_structure.py`.
- `README.md` and `ASSISTANT_OVERVIEW.md` (skill behavior changes do not require meta-level doc edits)
```

## 🤖 Claude · 2026-05-18 03:10
Limpio. Las cuatro cosas que pedí están: version 0.3.1, fecha de hoy, título correcto, los cuatro Changed y los cinco Unchanged enumerados sin omisiones. Entries anteriores preservadas verbatim.

Estás al final del flow del addendum. Quedan tres commits según el playbook:

1. `router: clarify Hard Rule for asset-attached spend intents (closes Spark collision)` (solo strategy-va-assistant/SKILL.md)
2. `paid-scripts: add creator context capture and brand-creator merge logic across ugc-brief, content-creator, spark-ad` (los tres SKILL.md de paid-script)
3. `changelog: 0.3.1 router disambiguation and creator merge logic` (solo CHANGELOG.md)

Después del push, si quieres validar específicamente lo del addendum (no las skills originales, eso ya lo testeaste), hay tres smoke tests que vale la pena correr en sesión limpia:

- "Put spend behind this organic Instagram post" → debería rutear a spark-ad, no a Motion. Confirma que el Hard Rule clarification funciona.
- "Spark this Reel for paid" sin pasar contexto del creator → debería pararse y pedir voice signature, audience profile, y creative angle. Confirma que el required Creator Context sub-block bloquea correctamente.
- "Write a content creator script for our brand ambassador [X]" sin pasar audience profile → debería pedir audience profile y creative angle antes de escribir. Confirma que el merge logic strengthening trabaja con su nuevo input contract.

Si los tres pasan, el addendum quedó sólido. Si alguno falla, dime cuál y vemos si es description-level o body-level y armamos el patch.

## 🧑 Adriana · 2026-05-18 03:34
final answer:

Install summary
`./install.sh` installed 13 `strategy-va-*` skills into `~/.claude/skills/` (9 existing strategy skills incl. the `strategy-va-assistant` router + 4 new paid-script skills). No backups were needed (no prior `strategy-va-*` folders existed). Only `strategy-va-*` folders were touched — the pre-existing unprefixed skills (`brand-intake`, `creative-strategy-agent`, `marketing-consultant`, `voice-copy-standards`, etc.) and any Motion skills were left untouched.
New skills verified on disk

* `~/.claude/skills/strategy-va-paid-script-ugc-brief/SKILL.md` ✅
* `~/.claude/skills/strategy-va-paid-script-content-creator/SKILL.md` ✅
* `~/.claude/skills/strategy-va-paid-script-spark-ad/SKILL.md` ✅
* `~/.claude/skills/strategy-va-paid-script-internal-edit/SKILL.md` ✅
(All four also show up loaded with their optimized descriptions in this session's skill list — confirming the frontmatter parses cleanly.)
⚠️ Restart reminder
Restart Claude Code (or start a fresh session) before smoke testing, so the skill index reloads cleanly from the freshly installed files.
Smoke-test checklist — one query per new skill (run in a fresh session)

1. `strategy-va-paid-script-ugc-brief` — "We hired a UGC creator on Billo. Write me a UGC brief for [brand] using the [angle] hook we developed."
2. `strategy-va-paid-script-content-creator` — "Write a content creator script for [creator handle] x [brand] — whitelisted on their handle, [angle/concept]."
3. `strategy-va-paid-script-spark-ad` — "Spark this organic post for paid — here's the transcript: [paste transcript]" (confirm it runs the 5-criteria diagnostic and asks for creator context).
4. `strategy-va-paid-script-internal-edit` — "I need an internal-edit production script with shot list and word-for-word VO for the [concept] paid ad."
Bonus router/boundary checks (optional but recommended)

1. Spend disambiguation (asset attached → stays in Strategy VA): "We want to put spend behind this organic post: [transcript]" → should route to `strategy-va-paid-script-spark-ad`, not bounce to Motion.
2. Spend disambiguation (no asset → Motion): "Analyze our spend by campaign for last month" → should defer to Motion Creative per the Hard Rule.
3. Paid vs organic clarify: "Write me a script" → router should ask paid vs organic before routing.
State of play: working tree on `strategy-va-refactor` has the 4 new folders + modified `README.md`, `ASSISTANT_OVERVIEW.md`, `CHANGELOG.md`, `strategy-va-assistant/SKILL.md`, and the 3 patched paid-script skills — still uncommitted and unpushed, per your standing instruction. Say the word when you want a commit/push.

## 🤖 Claude · 2026-05-18 03:35
Sprint cerrado. Strategy VA pasó de "strategist con handoff externo para scripting" a "strategist con execution layer paid completa de cuatro consumer types" con seis commitments arquitectónicos que se mantienen como contrato del paquete:

1. Eje consumer-first, no format-first. El formato vive como parámetro dentro de cada skill.
2. Input contract estricto. Las paid-script skills nunca regeneran estrategia; piden lo que les falta o se paran.
3. Paid only. Las skills rechazan rutear a organic toolkit.
4. Motion boundary preservada con discriminador nuevo: asset attached = Strategy VA, no asset = Motion.
5. Creator-brand voice merge logic en ugc-brief, content-creator y spark-ad. Internal-edit excluido (brand voice primary).
6. Spark merge principle como línea load-bearing del paquete: la audiencia del creator está viendo al creator, no al brand.

Lo que queda en working tree: 4 carpetas nuevas + 7 archivos modificados, sin commit. Cuando me digas, te armo el flow exacto de los tres commits del addendum (o squash si prefieres uno solo). Y los smoke tests los corres tú después del restart, ahí ya estoy fuera del loop.

## 🧑 Adriana · 2026-05-18 03:39
que deberia responder?

## 🤖 Claude · 2026-05-18 03:40
Lo más limpio es un solo commit cubriendo todo el working tree como 0.3.1. La separación 0.3.0/0.3.1 ya vive en el CHANGELOG, no necesita duplicarse en git history. Mándale esto a Claude Code:

```
Commit all working tree changes and push to strategy-va-refactor. Single commit covering the full 0.3.1 release. Message: `feat: paid-script execution layer with creator-brand merge logic (0.3.1)`. Confirm the commit hash and push status when done.
```

Si después de pensarlo prefieres dos commits separados (uno por versión del changelog), avísame y armo el split. Eso requiere hunking interactivo en `strategy-va-assistant/SKILL.md` porque ese archivo tiene cambios de ambas versiones mezclados, pero es factible si quieres la historia más granular. Para repo personal con changelog que ya cuenta la progresión, un solo commit te ahorra fricción sin perder claridad.

## 🧑 Adriana · 2026-05-18 03:46
done, despues debo pedirle que substituya todo el old marketing-strategy-va o borrarlo o como sea??

## 🤖 Claude · 2026-05-18 03:47
Sí, vale la pena hacer la limpieza, pero hazla DESPUÉS de los smoke tests para no perder la red de seguridad. Acá está el panorama:

**Qué borrar (8 carpetas):** las pre-rename copies que ahora viven duplicadas con sus versiones strategy-va-*. Si las dejas vas a tener trigger collision (Claude Code lee ambas descriptions y a veces gana la vieja). Son:
- `brand-intake`
- `creative-strategy-engine`  
- `hook-writing`
- `hook-tactics`
- `hook-voice-patterns`
- `review-audit`
- `visual-formats`
- `creative-mechanics`

**Qué NO tocar (separate tools, no son duplicates):**
- `marketing-consultant` (el expert council, herramienta separada según tu README)
- `creative-strategy-agent` (orquestador separado, listado como independiente en README)
- `voice-copy-standards` (skill separada)
- Cualquier `motion-*` (Motion Creative, otro plugin)
- Cualquier otra cosa que no esté en la lista de 8 de arriba

**Cuándo hacerlo:** después de correr los smoke tests del Prompt 10 y confirmar que las strategy-va-* nuevas disparan correctamente en sesión limpia. Si una de las nuevas falla, todavía tienes la vieja como fallback. Una vez que verifiques las 4 paid-script nuevas y los 3 bonus router checks, ya puedes limpiar.

**Prompt para Claude Code cuando estés lista:**

```
Read MIGRATION_NOTES.md in this repo first to confirm the official cleanup process. Then remove the 8 pre-rename duplicate skills from ~/.claude/skills/: brand-intake, creative-strategy-engine, hook-writing, hook-tactics, hook-voice-patterns, review-audit, visual-formats, creative-mechanics. Do NOT touch: marketing-consultant, creative-strategy-agent, voice-copy-standards, any motion-* skills, or any folder not in that explicit list of 8. Confirm what was removed and that the 13 strategy-va-* skills are still intact in ~/.claude/skills/.
```

Después del cleanup, restart Claude Code y verifica que los smoke tests siguen pasando. Si algo se rompe, la causa es que una de las viejas tenía customizaciones que no se migraron a la nueva (poco probable si nunca las editaste tú, posible si lo hiciste).

## 🧑 Adriana · 2026-05-18 03:50
la respuesta de claude code:

Done. ✅

* Commit hash: `899e026` — `feat: paid-script execution layer with creator-brand merge logic (0.3.1)`
* Single commit covering the full 0.3.1 release: 8 files, +641/−23 — 4 new `strategy-va-paid-script-*/SKILL.md` skills + updated `README.md`, `ASSISTANT_OVERVIEW.md`, `CHANGELOG.md`, `strategy-va-assistant/SKILL.md`. `install.sh` and `scripts/validate_structure.py` untouched, as intended.
* Push status: pushed successfully to `origin/strategy-va-refactor` (`5ddf7eb..899e026`).
* `master`/`main` untouched — no merge, nothing pushed to the default branch.
The branch now reflects the complete 0.3.x line on GitHub for your review.

## 🤖 Claude · 2026-05-18 03:51
Listo, 899e026 en origin/strategy-va-refactor. Build phase cerrada.

Próximo paso: restart Claude Code, sesión limpia, los 4 smoke tests + los 3 bonus router checks que Claude Code te listó en el install summary. Cuando los corras, mándame los outcomes que se vean off o ambiguous y los miramos. Si todo pasa, después arrancas con el prompt de cleanup de las 8 viejas que te mandé en el mensaje anterior.

## 🧑 Adriana · 2026-05-18 03:57
como lo reinicio?

## 🤖 Claude · 2026-05-18 03:57
En la sesión actual de Claude Code escribe `/exit` y enter, después corre `claude` de nuevo en la terminal. O cierra la ventana de terminal y abre una nueva, luego `claude`. Cualquier camino funciona, lo importante es que la nueva sesión cargue el skill index actualizado con las 4 paid-script nuevas.

## 🧑 Adriana · 2026-05-18 04:00
ok y ahora? los 4 smoke tests + los 3 bonus router checks? como lo hago?

## 🤖 Claude · 2026-05-18 04:02
Es simple: en la sesión nueva de Claude Code, pegas cada query una por una y observas dos cosas en la respuesta: (1) se activó la skill correcta y (2) la skill se comportó como esperaba (los pass conditions varían por test).

**4 smoke tests principales** (te recomiendo `/clear` entre cada uno para no contaminar contexto):

> *[line redacted — references an out-of-scope venture]*

> *[line redacted — references an out-of-scope venture]*

3. **spark-ad.** Query: "Spark this organic post for paid. Here's the transcript: [pega un transcript corto, real o inventado, 30 a 60 segundos]." Pass: corre el 5-criteria diagnostic Y pide creator context (voice signature, audience profile, creative angle).

> *[line redacted — references an out-of-scope venture]*

**3 bonus router checks** (estos van todos en una misma sesión, solo testean al router):

5. **Spend con asset.** Query: "We want to put spend behind this organic post: [transcript corto]". Pass: rutea a spark-ad, NO redirecciona a Motion.

6. **Spend sin asset.** Query: "Analyze our spend by campaign for last month." Pass: el Hard Rule dispara, te dice que eso pertenece a Motion Creative.

7. **Paid vs organic clarify.** Query: "Write me a script." Pass: el router pregunta paid o organic antes de rutear.

Lleva una lista con "pass / fail / weird" para cada uno. Si todo pasa, listo para el cleanup. Si algo falla, copia y pega la respuesta de Claude Code y la miramos.

## 🧑 Adriana · 2026-05-18 04:03
respuesta de smoke test 1

## 🤖 Claude · 2026-05-18 04:03
Trigger PASS. La skill correcta se activó, la description optimizada cargó limpio (LOOSE, HIRED, no audience of their own, todas las plataformas Billo/Insense/Trend/Cohley listadas), y la discriminación con sus dos hermanas (content-creator, internal-edit) está explícita en el cargado del skill. La routing layer funciona.

> *[line redacted — references an out-of-scope venture]*

El pass condition es que SE PARE y pida. Si te entrega un brief sin pedir más contexto, ahí tenemos un body-level failure y hay que reforzar el upstream contract.

Tip para los próximos tests: usa opción 1 (Yes una vez) en vez de opción 2 (allow for this project). Así te mantiene visibilidad sobre cada trigger event en los próximos 6 tests.

## 🧑 Adriana · 2026-05-18 04:06
all good got foundation question, persona, lenght, cta & claims unto the next

## 🤖 Claude · 2026-05-18 04:06
Test 1 PASS. Foundation + persona + length + CTA + claims es exactamente el upstream contract funcionando. Strict input gate held.

`/clear` y vas con el 2 (content-creator). Lo que buscas confirmar: que pida los inputs NUEVOS que agregamos en el patch (audience profile del creator, typical creative angle, brand voice profile para merge reference) ADEMÁS del foundation contract. Si solo pide foundation y se salta los nuevos, ahí está el regression.

## 🧑 Adriana · 2026-05-18 04:26
answer del 1

## 🤖 Claude · 2026-05-18 04:27
ROUTER PATCH VERIFIED. Esto es el bonus router check #1 (Spend con asset), no el smoke test #2 (content-creator). Saltaste al validar el fix de Prompt 11 primero, que es el call correcto: si el router fallaba ahí, los otros tests no importan tanto.

La query contiene "spend" y la Hard Rule original lo hubiera mandado a Motion, pero como hay un asset attached (el transcript del Reel), el clarification subsection que agregamos lo agarra y lo rutea a spark-ad correctamente. El fix del Prompt 11 funciona exactamente como lo diseñamos.

Click **"1 Yes"** para que ejecute la skill. Lo que viene ahora es el smoke test #3 (spark-ad) combinado en el mismo turno: ¿la skill corre el 5-criteria diagnostic (hook integrity, claim safety, CTA gap, pacing, asset quality) Y pide creator context (voice signature, audience profile, creative angle)? Si lo hace, ya validaste dos tests con una sola query.

## 🧑 Adriana · 2026-05-18 04:31
all router checks passed

## 🤖 Claude · 2026-05-18 04:32
Router patch fully validated. Asset-attached spend rutea a spark-ad. No-asset spend rutea a Motion. "Write me a script" hace clarificar paid vs organic primero. Los tres comportamientos del Prompt 11 confirmados.

Eso cierra el problema que arrancó toda esta refactor. La línea entre Strategy VA y Motion ahora es precisa, no defensiva.

Quedan smoke tests #2 (content-creator), #3 (spark-ad behavior) y #4 (internal-edit). El #3 puede que ya lo hayas verificado si en el router check #1 le diste Yes y viste si la skill corrió el 5-criteria diagnostic + pidió creator context. ¿Lo viste, o paraste en el trigger confirmation?

## 🧑 Adriana · 2026-05-18 04:33
si los testee todos, , listo para el cleanup.

## 🤖 Claude · 2026-05-18 04:33
Sprint completamente validado. Las 4 paid-script skills disparan correcto, el upstream contract aguanta en las tres con strict input gates, el spark diagnostic + creator context capture funciona, y el router patch resolvió la ambigüedad del "spend" sin ablandar la Motion boundary.

Para el cleanup, pega tal cual el prompt que te di hace dos mensajes (el que empieza con "Read MIGRATION_NOTES.md in this repo first..."). Claude Code va a leer el migration notes, borrar las 8 viejas duplicadas, dejar intactas las separate tools (marketing-consultant, creative-strategy-agent, voice-copy-standards, motion-*), y confirmar el estado final.

Después del cleanup haz un quick sanity check: en sesión limpia, pide "audit these reviews" y verifica que dispara `strategy-va-review-audit` (no `review-audit` viejo). Si pasa, la migración quedó cerrada y ya tienes el paquete 0.3.1 productivo.

## 🧑 Adriana · 2026-05-18 04:36
dame todo lo que debo copiar y pegar del Read MIGRATION_NOTES.md in this repo first

## 🤖 Claude · 2026-05-18 04:36
```
Read MIGRATION_NOTES.md in this repo first to confirm the official cleanup process. Then remove the 8 pre-rename duplicate skills from ~/.claude/skills/: brand-intake, creative-strategy-engine, hook-writing, hook-tactics, hook-voice-patterns, review-audit, visual-formats, creative-mechanics. Do NOT touch: marketing-consultant, creative-strategy-agent, voice-copy-standards, any motion-* skills, or any folder not in that explicit list of 8. Confirm what was removed and that the 13 strategy-va-* skills are still intact in ~/.claude/skills/.
```

## 🧑 Adriana · 2026-05-18 04:46

## 🤖 Claude · 2026-05-18 04:47
Option 1 (Take no action, Recommended).

Cuando armé el cleanup prompt asumí que las 8 unprefixed eran pre-rename copies de Strategy VA basándome en el OLD_NAMES list de validate_structure.py. Claude Code leyó MIGRATION_NOTES.md y los SKILL.md reales y encontró el matiz que faltaba: brand-intake y creative-strategy-engine en tu setup son extensions de creative-strategy-agent, no copias viejas de Strategy VA. Por eso la salvaguarda "Do NOT touch creative-strategy-agent" en el prompt funcionó: las atrapó antes de que fueran borradas erróneamente.

Las otras 6 que sí eran duplicates reales ya se borraron limpio. El cleanup ya está completo en sustancia.

Lo único que pierdes al dejar las 2 intactas es la posibilidad de trigger collision entre brand-intake (creative-strategy-agent) y strategy-va-brand-intake cuando digas algo tipo "research [brand]". Si en uso real notas que la vieja gana cuando esperabas que ganara la nueva, vuelves a este punto y lo revisas. Por ahora las dos coexisten porque sirven a tools distintos.

Selecciona Option 1.

## 🧑 Adriana · 2026-05-18 04:55
como puedo diferenciarlas then?

## 🤖 Claude · 2026-05-18 04:56
Tres formas, en orden de precisión:

> *[line redacted — references an out-of-scope venture]*

**2. Workflow context.** Si arrancas con el router (`strategy-va-assistant`) o pides algo que solo Strategy VA hace (paid-script, hook tactics, voice patterns), todo el chain pulls strategy-va-*. Si arrancas explícitamente con creative-strategy-agent (lo que sea que ese orchestrator haga), ese ecosystem usa su brand-intake. Cuando trabajas dentro de un orchestrator, no hay colisión.

> *[line redacted — references an out-of-scope venture]*

Practical: cuando importa cuál fire (por ejemplo cuando estás empezando un workflow específico), usa slash invocation. Cuando no importa (ambas hacen brand research perfectamente válido), deja que el matcher elija y revisa el prompt de Claude Code antes de hacer click. Si te muestra la equivocada, le das No y la invocas con slash.

## 🧑 Adriana · 2026-05-18 04:57
Done. Summary:

* Read MIGRATION_NOTES.md and confirmed the official process is inspect-first, then back up via `mv` to `.pre-strategy-va.<ts>.bak` — not a hard `rm` — with an explicit rule to never delete a folder that may belong to Motion Creative / the extension.
* Inspected before acting, which surfaced that 6 of the 8 listed skills are already gone, and the remaining 2 (`brand-intake`, `creative-strategy-engine`) are creative-strategy-agent extension skills, not old Strategy-VA copies — protected by your own "do NOT touch" instruction.
* Per your decision: no action taken. Nothing deleted, moved, or modified.
* Verified intact: all 13 `strategy-va-*` skills; `creative-strategy-agent`, `marketing-consultant`, `voice-copy-standards`, and motion-related skills untouched.
* Saved a memory so this collision doesn't trigger an accidental deletion in a future session.
The pre-rename Strategy-VA cleanup was already effectively complete before this session.

## 🤖 Claude · 2026-05-18 04:58
Sprint cerrado, full stop. Lo que el cleanup investigation reveló de paso: el protocolo oficial del repo es `mv` a `.bak` con timestamp, no `rm`, lo cual es más conservador que mi prompt asumió y refleja buena arquitectura defensiva ya construida. Las 6 duplicates ya habían sido limpiadas antes, probablemente cuando hiciste el rename original a strategy-va-*. Las 2 sobrevivientes son creative-strategy-agent extensions, ahora validado y memorizado por Claude Code para no volver a aparecer como falso positivo.

Strategy VA 0.3.1 está productivo en tu local. Cuando quieras mergear strategy-va-refactor a master, ya está listo para eso. Los smoke tests confirmados te dan tracción inmediata: pega cualquiera de las 4 paid-script skills en uso real cuando te toque briefing y arrancas con el contract estricto desde el primer turno.

## 🧑 Adriana · 2026-05-18 04:59
ok deberia pedir que actualice el repo entonces? para qeu se vaya a master?

## 🤖 Claude · 2026-05-18 05:00
Sí, vale la pena para cerrar limpio. Si trabajas sola en este repo y no necesitas mantener strategy-va-refactor como branch viva, lo más limpio es: fast-forward merge al default branch (master o main), push, y delete del feature branch.

Prompt para Claude Code:

```
Merge strategy-va-refactor into the default branch (master or main, whichever this repo uses). Use fast-forward if possible since strategy-va-refactor is one commit ahead. After the merge, push the default branch to origin. Then delete strategy-va-refactor locally and from origin since it's been merged. Confirm the final state: default branch's tip commit hash, remote sync status, and that strategy-va-refactor is no longer in either local or remote.
```

Después de esto tu default branch tiene 0.3.1 productivo y el branch list queda limpio. Si en el futuro quieres seguir iterando (0.3.2, 0.4.0, etc.), arrancas un branch nuevo desde ahí. Los skills locales en `~/.claude/skills/` ya están instalados, el merge no los toca.

## 🧑 Adriana · 2026-05-18 05:11
Done. Final state confirmed:
Check	Result
Default branch	master (confirmed as origin's HEAD branch)
master tip commit	899e026b88a7fb3529ae9c62c56bb0186ba38483 — "feat: paid-script execution layer with creator-brand merge logic (0.3.1)"
Merge type	Fast-forward (7f38c1b..899e026, no merge commit)
Remote sync	local master == origin/master == 899e026 — IN SYNC ✓
strategy-va-refactor (local)	Deleted (safe -d, was 899e026) — gone ✓
strategy-va-refactor (origin)	Deleted from origin — gone ✓
Any lingering ref	None anywhere (local or remote) ✓
One note worth recording: your message said strategy-va-refactor was "one commit ahead," but it was actually 3 commits (b279d3f → 5ddf7eb → 899e026). The fast-forward still applied cleanly because master had no diverging commits, and the end result is exactly what you wanted — but the branch carried the full standalone refactor (0.2.0), the scripting-handoff preservation, and the 0.3.1 paid-script layer, not a single commit. master now contains all three.

## 🤖 Claude · 2026-05-18 05:12
Merge clean. 0.3.1 vive en master, branch list limpio, sin lingering refs en ningún lado.

Sobre el conteo: tienes razón, asumí mal. Sabía solo del commit de esta sesión (899e026) y no contabilicé que strategy-va-refactor ya cargaba el trabajo del 0.2.0 standalone refactor + la preservación del scripting-handoff. Tres commits, no uno. El fast-forward funcionó porque master no había divergido, pero el contenido absorbido fue mayor de lo que dije. Master ahora tiene el arco completo: 0.2.0 standalone, scripting-handoff preservation, y 0.3.1 paid-script layer.

Sprint completamente cerrado. La próxima vez que abras Claude Code para algo de paid scripting, las skills están listas para producir desde el primer turno.
