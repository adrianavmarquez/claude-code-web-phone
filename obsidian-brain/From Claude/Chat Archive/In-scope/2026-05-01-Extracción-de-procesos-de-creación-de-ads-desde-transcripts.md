---
title: "Extracción de procesos de creación de ads desde transcripts"
source: claude.ai-chat
created: "2026-05-01 00:28"
summary: "**Conversation Overview**  The person is building an AI-powered creative strategy system for performance advertising (Meta/TikTok), working within a framework derived from a Motion Creative Strategy Bootcamp covering weeks 3 through 7. They had already developed a 'motor de estrategia creativa' skill and were seeking to extract structured process documentation from bootcamp transcripts, then progressively architect a complete modular agent skill system. The person demonstrated deep familiarity with performance creative terminology including hooks, thumb stop rates, hold rates, ROAS, CPM, Andromeda algorithm behavior, NanoBanana 2, Veo 3.1, and UGC frameworks.  The conversation moved through several distinct phases. First, Claude analyzed five weeks of bootcamp transcripts (VTT, PDF, and DOCX formats) to produce a structured technical report covering objectives, workflows, critical variables, and exceptions for each week. The person then shared their own extraction notes, and Claude performed a gap analysis identifying what each version captured that the other missed — notably that the person's notes had richer operational detail on the Harry's case study, the Caraway UGC program structure (360 active UGC ads, Concept Formula, cross-functional team roles), Happy Mammoth's Creative Scaling Engine with Color Tags System, and the James Webb Young ideation framework adapted by Viti Videtta. Claude's extraction was stronger on technical stack specifics like NanoBanana 2 prompt length requirements, Veo 3.1 JSON-only protocol, and quantitative benchmarks like First Frame Retention at 90%.  From this consolidated knowledge base, the person requested modular agent skills following Anthropic's Agent Skills standard. Claude built five individual SKILL.md files (W3 through W7), then consolidated them into a single orchestrator skill with a Resource Collection Gate (Paso 0), stage selection routing, per-stage SOPs and guardrails, and a Feedback Loop closing W7 back into W3. Supporting files included a `references/schemas.md` with typed JSON output schemas for all five stages, and an `evals/evals.json` with four test cases following the exact schema standard. The person then requested a workflow configuration file, which Claude produced as `pipeline_workflow.json` defining five transitions with explicit field mappings between output and input fields, 19 validation rules across three severity levels (HARD_BLOCK, BLOCK, WARN), a Hard Pivot Rule for systemic failure scenarios, and six global rules including the critical gate blocking W6 (Exploration) without a completed W5 (Analysis).  Throughout the build, the person provided iterative feedback that shaped the architecture: adding production capacity constraints to W3, introducing creative fatigue detection and Thumb Stop vs. CTR correlation diagnosis to W5, adding placement adaptation logic to W7, introducing a Crisis eval (Eval 4) testing Hard Pivot judgment, and specifying that the Resource Collection Gate should request all available resources upfront rather than blocking on optional inputs. The person also proposed a four-layer framework incorporating Atria for financial validation, Foreplay boards for visual inspiration, and a closed Feedback Loop — which Claude implemented with the distinction that Atria is a VALIDADOR (continues with warning if absent) rather than a CRÍTICO (hard block), to avoid unnecessary pipeline paralysis. The person's stated preference throughout was for plain Markdown output rather than HTML, and for robust breakdowns that compound across sessions rather than starting fresh each time."
messages: 28
claude_uuid: "af997354-c6a2-469f-a6ad-0da37754d93b"
tags: [claude, chat, archive]
---
# Extracción de procesos de creación de ads desde transcripts

> **Conversation Overview**

The person is building an AI-powered creative strategy system for performance advertising (Meta/TikTok), working within a framework derived from a Motion Creative Strategy Bootcamp covering weeks 3 through 7. They had already developed a "motor de estrategia creativa" skill and were seeking to extract structured process documentation from bootcamp transcripts, then progressively architect a complete modular agent skill system. The person demonstrated deep familiarity with performance creative terminology including hooks, thumb stop rates, hold rates, ROAS, CPM, Andromeda algorithm behavior, NanoBanana 2, Veo 3.1, and UGC frameworks.

The conversation moved through several distinct phases. First, Claude analyzed five weeks of bootcamp transcripts (VTT, PDF, and DOCX formats) to produce a structured technical report covering objectives, workflows, critical variables, and exceptions for each week. The person then shared their own extraction notes, and Claude performed a gap analysis identifying what each version captured that the other missed — notably that the person's notes had richer operational detail on the Harry's case study, the Caraway UGC program structure (360 active UGC ads, Concept Formula, cross-functional team roles), Happy Mammoth's Creative Scaling Engine with Color Tags System, and the James Webb Young ideation framework adapted by Viti Videtta. Claude's extraction was stronger on technical stack specifics like NanoBanana 2 prompt length requirements, Veo 3.1 JSON-only protocol, and quantitative benchmarks like First Frame Retention at 90%.

From this consolidated knowledge base, the person requested modular agent skills following Anthropic's Agent Skills standard. Claude built five individual SKILL.md files (W3 through W7), then consolidated them into a single orchestrator skill with a Resource Collection Gate (Paso 0), stage selection routing, per-stage SOPs and guardrails, and a Feedback Loop closing W7 back into W3. Supporting files included a `references/schemas.md` with typed JSON output schemas for all five stages, and an `evals/evals.json` with four test cases following the exact schema standard. The person then requested a workflow configuration file, which Claude produced as `pipeline_workflow.json` defining five transitions with explicit field mappings between output and input fields, 19 validation rules across three severity levels (HARD_BLOCK, BLOCK, WARN), a Hard Pivot Rule for systemic failure scenarios, and six global rules including the critical gate blocking W6 (Exploration) without a completed W5 (Analysis).

Throughout the build, the person provided iterative feedback that shaped the architecture: adding production capacity constraints to W3, introducing creative fatigue detection and Thumb Stop vs. CTR correlation diagnosis to W5, adding placement adaptation logic to W7, introducing a Crisis eval (Eval 4) testing Hard Pivot judgment, and specifying that the Resource Collection Gate should request all available resources upfront rather than blocking on optional inputs. The person also proposed a four-layer framework incorporating Atria for financial validation, Foreplay boards for visual inspiration, and a closed Feedback Loop — which Claude implemented with the distinction that Atria is a VALIDADOR (continues with warning if absent) rather than a CRÍTICO (hard block), to avoid unnecessary pipeline paralysis. The person's stated preference throughout was for plain Markdown output rather than HTML, and for robust breakdowns that compound across sessions rather than starting fresh each time.

## 🧑 Adriana · 2026-05-01 00:28
te voy a adjuntar los transcripts de todas estas clases:  
Week 3 - Prioritize your ad ideas 
Week 4 - Make some ads! 
Week 5 - Analyze your ads 
Week 6 - Sprint #1 - Iterate on your ads 
Week 7 - Sprint #2 - Adapt winning ads into new formats   

El goal es el siguiente, toda esta informacion te lleva de la mano para crear ads.  Ya tengo todo un breakadown con el que hice un skill de "motor de estrategia creativa". 

Donde subo toda la data del scrapping que he hecho y se encarga de dejar una base solida para basar esta siguiente fase de la creacion de ads.   

Habiendo dicho esto, necesito extraer de estos transcripts; Actúa como un analista de procesos senior. He adjuntado una transcripción. Tu tarea es extraer paso a paso:Objetivos clave: ¿Qué se intentaba resolver?Flujo de trabajo: Lista numerada de cada acción realizada.Variables críticas: Datos que cambian (IDs, fechas, nombres de productos).Excepciones: ¿Qué errores ocurrieron y cómo se resolvieron?Presenta esto en un formato de reporte técnico estructurado.

## 🤖 Claude · 2026-05-01 00:28

## 🧑 Adriana · 2026-05-01 00:30
te voy a adjuntar los transcripts de todas estas clases:  
Week 3 - Prioritize your ad ideas 
Week 4 - Make some ads! 
Week 5 - Analyze your ads 
Week 6 - Sprint #1 - Iterate on your ads 
Week 7 - Sprint #2 - Adapt winning ads into new formats   

El goal es el siguiente, toda esta informacion te lleva de la mano para crear ads.  Ya tengo todo un breakadown con el que hice un skill de "motor de estrategia creativa". 

Donde subo toda la data del scrapping que he hecho y se encarga de dejar una base solida para basar esta siguiente fase de la creacion de ads.   

Habiendo dicho esto, necesito extraer de estos transcripts; Actúa como un analista de procesos senior. He adjuntado una transcripción. Tu tarea es extraer paso a paso:Objetivos clave: ¿Qué se intentaba resolver?Flujo de trabajo: Lista numerada de cada acción realizada.Variables críticas: Datos que cambian (IDs, fechas, nombres de productos).Excepciones: ¿Qué errores ocurrieron y cómo se resolvieron?Presenta esto en un formato de reporte técnico estructurado.

## 🤖 Claude · 2026-05-01 00:30

## 🧑 Adriana · 2026-05-01 00:31
te voy a adjuntar los transcripts de todas estas clases:  
Week 3 - Prioritize your ad ideas 
Week 4 - Make some ads! 
Week 5 - Analyze your ads 
Week 6 - Sprint #1 - Iterate on your ads 
Week 7 - Sprint #2 - Adapt winning ads into new formats   

El goal es el siguiente, toda esta informacion te lleva de la mano para crear ads.  Ya tengo todo un breakadown con el que hice un skill de "motor de estrategia creativa". 

Donde subo toda la data del scrapping que he hecho y se encarga de dejar una base solida para basar esta siguiente fase de la creacion de ads.   

Habiendo dicho esto, necesito extraer de estos transcripts; 
Actúa como un analista de procesos senior. 
He adjuntado una transcripción. Tu tarea es extraer paso a paso:
Objetivos clave: ¿Qué se intentaba resolver?
Flujo de trabajo: Lista numerada de cada acción realizada.
Variables críticas: Datos que cambian (IDs, fechas, nombres de productos).
Excepciones: ¿Qué errores ocurrieron y cómo se resolvieron?
Presenta esto en un formato de reporte técnico estructurado.

## 🤖 Claude · 2026-05-01 00:38
Now I have enough content from all 5 weeks. Let me compile the full report.

Tengo suficiente contenido de las 5 semanas. Ahora voy a construir el reporte técnico completo.

Ahora tengo todo lo que necesito. Voy a construir el reporte técnico estructurado en HTML.

Acá está el reporte completo. Lo que extraje de cada semana:

**W3 (Dara Denny):** El proceso de personas. Cómo usar Claude para analizar la ads library del competidor, cruzarlo con el CSV de reviews para detectar la brecha entre "quién ves en tus ads" vs "quién realmente compra." De ahí sale el roadmap priorizado.

**W4 (Will Sartorius):** El workflow de producción con AI. Dos métodos: el quick win (deconstruir DNA de un ad competidor en Claude → adaptar al brand → generar con NanoBanana 2 en Fal.ai) y el método escalable con Claude Code. Más la pieza de animación con Veo 3.1 usando JSON prompts obligatorios.

**W5 (Evan Lee):** El stack de métricas en orden: First Frame Retention → Thumb Stop → Hold Rate → CTR → Goal Metric. Cómo diagnosticar en qué eslabón se rompe el ad antes de decidir qué iterar.

**W6 (Jade + Daniel):** Fase Explore. El caso de Calm detectando el bilateral stimulation audio en un TikTok orgánico y convirtiéndolo en una USP nueva. El proceso: señal → hypothesis → investigación → test mínimo de 3 ads → validación → escala.

**W7 (Sophia + Viti + Janae):** Fase Exploit. Cómo construir ad families post-Andromeda con variación real: talent, persona, formato, estructura narrativa. Más el framework de James Webb Young de Viti para generar ideas net new que no sean copias.

La tabla maestra al final condensa todo el flujo end-to-end de las 5 semanas. Sirve como referencia rápida antes de cualquier sesión de producción.

## 🧑 Adriana · 2026-05-01 00:43
te voy a adjuntar lo que yo extraje, quiero que veas si hay algo que falto en lo que tu extrajiste, como se pueden complementar, quiero un creakdown robusto, no quiero que lo vuelvas a hacer en formato html

## 🤖 Claude · 2026-05-01 00:45
Tengo todo. Ahora voy directo al análisis de gaps y al breakdown consolidado.

---

## Lo que tú capturaste que yo no tuve

El gap más importante está en **la profundidad operativa** de cada semana. Tu extracción fue más fiel a las citas directas y a la granularidad de los frameworks. Estos son los elementos que me faltaron o que traté de forma superficial:

**Week 3 (Dara):** Tuve la estructura general pero me faltaron cosas críticas. El **Evidence Ranking System** (high confidence vs. low confidence evidence), el **Icebox** como concepto específico de repositorio de ideas sin filtrar, la estructura de 4 partes del roadmap con Creators/Icebox/Quarterly/Monthly separados, la granularidad del **EGC (Employee Generated Content)**, y los umbrales de decisión concretos como "si puede salir en menos de una semana, agregar al sprint semanal" o "rediagnóstico quarterly." También perdí el ejemplo específico de la marca de skincare que targeting hombres porque los founders eran hombres, cuando el comprador real era mujeres afroamericanas preocupadas por makeup flaking. Ese ejemplo es mucho más nítido que el de OATS que sí tenía. También perdí la distinción entre el rol del creative strategist ("it's not your job to be creative, it's your job to make the business money") que es un reframe filosófico importante, y el punto de que los top brands no son los más creativos, son los que más duplican lo que funciona.

**Week 4 (Will):** Aquí es donde la diferencia más grande vive. Yo capturé los 3 métodos pero me perdí toda la **arquitectura del sistema escalable** en detalle. El Layer 2 (Brand Reference Cards como imágenes, no texto, con la distinción Brand Spec Card vs. Visual Style Card), el Layer 3 (recolectar 50-100 ads del mismo formato con ImageEye para generar el template como recipe card), y el Layer 4 (Copywriting Agents con roles específicos incluyendo el Grammar Agent con la instrucción explícita de "no m-dashes") son los más relevantes para el sistema que estás construyendo. También perdí el hack de fonts/colors via inspección de HTML, el problema específico de que Claude no puede extraer fonts/colors bien, el hit rate diferencial entre método quick (60-70%) vs. sistema escalable (90-95%), y el error de subir PDFs directamente a Claude. El punto sobre AI UGC fue truncado en tu extracción pero tú tenías la intención clara: Will lo desaconseja.

**Week 5 (Evan):** Aquí los gaps son más de matiz que de contenido. Yo tenía las métricas pero me faltaron los **niveles de hipótesis** (individual, team, org), la vista de bar chart específica con ejes X=Spend/Y=Bottom Line como metodología de análisis, el diagnóstico en tabla de 3x3 (alto watch/bajo CTR, bajo watch/alto CTR, etc.), los datos concretos del ejemplo de Tara (41% a 25% de completion, CTR de 7.91%), y el punto filosófico más importante: cada ad es una hipótesis que termina clasificada como TRUE / FALSE / NEEDS MORE TIME. También perdí el Motion MCP como integración para conectar Claude con los datos de la cuenta sin riesgo, y el benchmark de TikTok siendo 2 o 6 segundos vs. los 3 de Meta.

**Week 6 (Jade + Daniel):** Tu versión es considerablemente más rica. Yo capturé el caso Calm bien, pero me perdí la especificidad del caso Harry's. Los 4 errores que documentaste de ese caso son altamente accionables: el error de credenciales que no viajan geográficamente (Kiehl's no significa nada en el Midwest), el error de lenguaje técnico que el target no entiende (parabens, sulfates), el error de luxury positioning a alguien que no se identifica con la indulgencia, y la distinción entre **product truths vs. customer truths** como concepto nombrado. La metáfora de "digging for wells" de Daniel tampoco la tenía. También me faltaron los affirmations de Daniel ("nothing is wasted, it didn't fail, it only clarified") que aunque suenan motivacionales tienen implicación estratégica real: documentar cada test fallido como claridad, no como pérdida. El número de $10M+ sobre múltiples años atribuido al bilateral stimulation USP es un dato que cambia el peso de todo el caso.

**Week 7 (Sophia + Viti + Janae):** Aquí el gap más grande es **Janae y el programa UGC de Caraway**, que en mi extracción prácticamente no existía. Tú capturaste el framework completo: equipo cross-funcional con roles específicos (Performance Creative, Influencer Team, Growth/Media Buying), la distinción Core Persona Retainers vs. Expansion Creators, los Content Buckets (Evergreen/BAU, Product Launches, Seasonal), el proceso de research pre-briefing con las 4 preguntas secuenciales (qué funcionó el año pasado, qué está funcionando ahora, cuál es la hipótesis), y la **Concept Formula** (Title + Angle + Creative Guardrails + Objection Handling). Ese framework de Caraway es probablemente el más aplicable para briefing de UGC a escala y yo lo reducí a un párrafo. También perdí los números reales: 360 ads UGC vivos en 2026 YTD, 2.14X ROAS promedio, y los 500 ads por semana de Happy Mammoth. Del framework de Viti me faltó el **Creative Scaling Engine** de 7 pasos como concepto nombrado, el Color Tags System (verde = massive winner = biggest swings, scale up = smaller swings), y el criterio de "winner válido" con los 5 indicadores concretos (stable CPA, strong CTR, run across many audiences, engagement healthy, spend picking up). El "Terminator 1 y 2" como analogía del refresh también lo perdí, y es memorable.

---

## Breakdown consolidado: lo que falta unificar semana a semana

**W3: Lo que hay que agregar al reporte original**

Sobre diagnóstico: la frase exacta "if you don't have a diagnosis, you don't really have a real strategy, you just have aimless week to week testing" define el diagnóstico como el anchor point, no solo como un output. El diagnóstico se rediagnostica quarterly. El criterio de decisión para usar creator vs. statics es la intensidad emocional del insight, no solo el tipo de ad.

Sobre el roadmap: la estructura de 4 partes es operativa y secuencial. Creators primero (pipeline de talento, incluyendo para partnership ads). Icebox segundo (absolutamente sin filtro, nadie es juzgado por lo que está ahí, es responsabilidad del lead hacer que el equipo documente). Quarterly tercero (mapeo de holidays, product launches, personas asignadas a momentos del año). Monthly cuarto (ideas detalladas con persona, idea en 1-2 oraciones y 3 variaciones de messaging por idea, se duplica mes a mes para histórico).

Sobre priorización: el Evidence Ranking System tiene dos categorías muy concretas. High confidence: formatos, messaging y creators ya pressure tested. Low confidence: "el competidor lo lleva corriendo X tiempo" (porque puede estar buried en retargeting), "porque el competidor lo hizo" sin más contexto. La única evidencia del running time de un competidor sin conectar con personas, research o awareness levels es motivo de rechazo inmediato.

Sobre el rol: "it's not your job to be creative, it's your job to make the business money." Los top brands no son los más creativos, son los que más duplican lo que ya funciona. Seed Health: 1 de cada 7 ads usa el mismo ángulo. Everyday Dose: duplica hooks ganadores de video en formato static. El antídoto a la parálisis por originalidad es buscar los creative pillars y crear variaciones de ellos.

**W4: Lo que hay que agregar**

El sistema escalable tiene capas con consecuencias técnicas específicas que son relevantes para el skill. Claude no puede extraer fonts y colores correctamente, es un error documentado en el transcript. El workaround es inspeccionar el HTML de la página, buscar "font", copiar el código y pasárselo a Claude para que actualice las spec cards. Las Brand Reference Cards deben ser imágenes (PNG), no texto, porque NanoBanana 2 necesita ver para reproducir. Brand Spec Card contiene logos, fonts (headline, UI, subheaders, body), colores, do's/don'ts, CTAs. Visual Style Card contiene dirección de fotografía, styling rules, quote del founder, ejemplos de ads, do's/don'ts visuales.

Los Copywriting Agents son archivos .md con role, job description y scoring criteria. Los 6 agentes: Persona Fit, Angle, Emotion, Brand Fit, Conversion, Grammar. El Grammar Agent incluye explícitamente "no m-dashes." El proceso de agent review es automático, tarda ~20 minutos, y el threshold es 90+/100 por cada agente. El flujo es Brief Generation → Agent Review → Conversión a NanoBanana prompt → Fal.ai. Los PDFs deben convertirse a markdown antes de subir a Claude porque Claude los trata como imágenes de página.

El hit rate del método quick win es 60-70%. El del sistema escalable es 90-95%. Esa diferencia es el argumento para invertir el tiempo en construir el sistema.

**W5: Lo que hay que agregar**

El marco filosófico: cada ad es una hipótesis. Los analytics no son un dashboard pasivo, son la prueba de que entiendes a tu cliente mejor que nadie. El movimiento es de consumidor de dashboards a detective que forma perspectiva independiente. El resultado de cada hipótesis se clasifica en 3 categorías: TRUE, FALSE, NEEDS MORE TIME.

Los 3 niveles de hipótesis: Individual (este CTA va a aumentar mi CTR), Team (creator ads van a outperformar los in-house), Org (¿en qué productos tiene sentido invertir el spend?). El nivel Org es el que más se pasa por alto y es el que conecta creative strategy con decisiones de negocio reales.

La vista de bar chart es la vista correcta para identificar top performers, no la vista de creativos. Eje X: Spend, eje Y: Bottom line metric. Cuando el análisis empieza desde esa vista, la conversación con el cliente o el equipo cambia porque ya no es "me gusta este ad" sino "este ad está retornando con ese spend."

Para benchmarks: anclar primero contra tu propia cuenta, no contra benchmarks de industria. Un benchmark de industria de 40 no significa nada si tu promedio histórico es 70 o es 20. Estás compitiendo contra ti mismo.

El diagrama de diagnóstico de watch rate más CTR es una decisión tree: alto watch + bajo CTR = CTA débil, acción es fortalecer CTA al final. Bajo watch + alto CTR = video demasiado largo, acción es acortar y subir el CTA más arriba. Siempre convertir % de completion a segundos reales antes de diagnosticar.

**W6: Lo que hay que agregar**

El caso Harry's merece el mismo nivel de detalle que el caso Calm. Los 3 ángulos que fallaron son transferibles: credibilidad que no viaja geográficamente (Kiehl's no funciona en el Midwest), lenguaje técnico que el target no puede decodificar (parabens, sulfates), y luxury positioning que aliena a alguien que se define como "not indulgent." El insight de que las mujeres compraban body wash para sus maridos redefinió completamente el brief. Eso es la diferencia entre product truths y customer truths.

La metáfora de Daniel sobre digging for wells tiene estructura: leer el terreno antes de cavar (surroundings, lush land, animal tracks), cada intento fallido clarifica dónde está el agua, no se desperdicia nada. Es una forma de pensar sobre los tests fallidos que cambia cómo el equipo documenta y usa esos learnings.

Los datos del caso Calm: $10M+ a lo largo de múltiples años como atribución al bilateral stimulation USP. Ads individuales de ese vertical con spend de $100K+. La reducción de costo fue de aproximadamente la mitad en el primer mes de iteración. Estos números le dan peso a toda la historia del caso.

**W7: Lo que hay que agregar**

El programa UGC de Caraway es el framework más completo de operación a escala que cubrió el bootcamp y prácticamente no estaba en mi extracción. El equipo cross-funcional tiene responsabilidades claras: Performance Creative hace briefing strategy y concepting, Influencer Team hace sourcing/vetting y gestiona el inicio del programa, Growth/Media Buying entrega data de performance en tiempo real. Esos 3 equipos co-crean el brief, no es un proceso unilateral.

La selección de creators tiene dos categorías operativas. Core Persona Retainers son la mayoría del pool: creators que matchan las personas con mejor conversión histórica, con el estilo de contenido que ya resuena, son el reliability baseline. Expansion Creators son la minoría: ligeramente fuera de la persona core, abren audiencias nuevas. Post-Andromeda el niche importa: no es "gym person," es "biohacker que enfoca en macros."

Los Content Buckets de Caraway son Evergreen/BAU (core themes que se refrescan constantemente), Product Launches (lanzamientos específicos del brand), Seasonal/Brand Specific (Mother's Day, Father's Day). El proceso de research pre-briefing tiene 4 preguntas secuenciales: ¿qué funcionó el año pasado? ¿qué está funcionando en el wild ahora? ¿cuál es nuestra hipótesis? ¿cuál es el nivel de convicción? La Concept Formula es: título del concepto + ángulo (por qué funciona) + creative guardrails (delivery, tono) + objection handling anticipado.

El Creative Scaling Engine de Happy Mammoth es un ciclo de 7 pasos nombrado como tal: Find Winner → Deconstruct → Multiply → Test Fast → Scale → Refresh → Find New Winner. El Color Tags System es operativo: verde es massive winner, se hacen los swings más grandes (cambiar creator, producto, script, género, acento, bureau). Scale Up es doing great pero no massive, se hacen swings más pequeños primero para ver si tiene capacidad de llegar a verde.

El umbral de decisión para un winner válido tiene 5 indicadores simultáneos que deben cumplirse: CPA estable, CTR fuerte o strong engagement grade, corriendo en múltiples audiencias, engagement sano, spend acelerando. No es una métrica, son 5 condiciones. El refresh total (Version 2.0) solo ocurre cuando el winner fatiga Y todas las iteraciones dejaron de funcionar. La analogía del Terminator: el alma del ad debe ser reconocible en la versión 2.0, aunque el script, los visuals y los hooks sean nuevos.

---

## Lo que yo capturé que tú no tuviste

Las cosas que estaban en los transcripts y que no aparecen en tus reportes son más de contexto técnico y de stack tecnológico que de frameworks estratégicos.

El benchmark de **First Frame Retention >90%** como umbral específico no aparece en tus reportes, solo mencionas las métricas sin los números. La distinción entre **NanoBanana Pro vs. NanoBanana 2** en términos de comportamiento (Pro adivina, llena huecos; 2 no adivina, necesita instrucción explícita para cada elemento) tampoco aparece explícitamente. El uso de **"frames" en lugar de "ingredients"** en Veo como instrucción técnica específica aparece en mis notas pero no en las tuyas. El **Motion MCP** lo mencionas brevemente pero sin el detalle de que permite conectar Claude directamente a los datos del ad account sin riesgo de seguridad. La **frecuencia de 68Hz** del cuerpo humano que Bed Threads usó en un ad específico (de tu W3) es un dato de color que tú sí tenías pero que también es relevante como ejemplo de USP técnico convertido en creative.

Lo que más me faltó a mí y que no se puede recuperar de tu extracción: hay una sección del caso Harry's en el Week 6 que tu archivo marca como "información truncada en el segmento de Harry's." Eso significa que el transcript también fue truncado para ese segmento, así que hay contexto que ninguno de los dos tiene completo.

## 🧑 Adriana · 2026-05-01 00:53
"Basado en el análisis anterior, diseña Skils' modulares para un agente de IA.

* Nombre de la Skill: (Ej: Gestion_Reclamaciones)
* Descripción: Explica para qué sirve (esto es lo que el agente leerá para decidir si usarla).
* Trigger: ¿En qué frase o situación exacta debe activarse?
* Instrucciones (Instructions): Redacta directrices concisas tipo 'Si X, haz Y' evitando narrativas largas.
* Herramientas necesarias: ¿Qué software o APIs debería 'llamar' el agente para completar esto?"
* Define los 'Inputs Requeridos' para esta skill. Por ejemplo: para la Semana 5 (Análisis), el input debe ser un CSV de métricas de Meta Ads o un pantallazo del Ads Manager. Si falta el dato, el agente debe pedirlo antes de proceder.
* Incluye una sección de 'Razonamiento Interno'. Antes de dar el output, el agente debe listar mentalmente los criterios de la clase (ej: 'Primero miro el CTR, luego el Hook Rate, luego el ROAS') y justificar su decisión basándose en el transcript.

## 🧑 Adriana · 2026-05-01 00:54
"Basado en el análisis anterior, diseña Skils' modulares para un agente de IA.

* Nombre de la Skill: (Ej: Gestion_Reclamaciones)
* Descripción: Explica para qué sirve (esto es lo que el agente leerá para decidir si usarla).
* Trigger: ¿En qué frase o situación exacta debe activarse?
* Instrucciones (Instructions): Redacta directrices concisas tipo 'Si X, haz Y' evitando narrativas largas.
* Herramientas necesarias: ¿Qué software o APIs debería 'llamar' el agente para completar esto?"
* Define los 'Inputs Requeridos' para esta skill. Por ejemplo: para la Semana 5 (Análisis), el input debe ser un CSV de métricas de Meta Ads o un pantallazo del Ads Manager. Si falta el dato, el agente debe pedirlo antes de proceder.
* Incluye una sección de 'Razonamiento Interno'. Antes de dar el output, el agente debe listar mentalmente los criterios de la clase (ej: 'Primero miro el CTR, luego el Hook Rate, luego el ROAS') y justificar su decisión basándose en el transcript.
* Define 'Escenarios de Error'. ¿Qué debe hacer el agente si los datos de la clase de Priorización (Semana 3) son contradictorios? Ejemplo: 'Si el cliente tiene poco presupuesto, prioriza ideas de bajo costo de producción (UGC) sobre producciones caras'."
* El resultado de esta skill debe ser un bloque de código estructurado (Markdown o JSON). Esto permitirá que la salida de la Skill X sea leída automáticamente como entrada por la Skill Y

La skill debe estructurarse así:Contexto de Activación: Cuándo y por qué se usa esta skill.Contrato de Entrada: Lista exacta de datos/archivos necesarios.Protocolo de Razonamiento: Pasos lógicos que el agente debe seguir 'en silencio' antes de responder.Instrucciones Operativas (SOP): Reglas directas extraídas del transcript (Si pasa A, haz B).Guardrails: Qué tiene prohibido hacer el agente en esta etapa.Esquema de Salida: Define un formato de entrega que sirva de input para la siguiente semana.

## 🤖 Claude · 2026-05-01 00:57
Voy directo. Una skill por semana, más una de orquestación que las conecta todas. Formato limpio, sin HTML.

---

# SISTEMA DE SKILLS MODULARES
## Motion Creative Strategy Bootcamp — Agente de IA

---

## SKILL 1: RESEARCH_TO_STRATEGY

**Nombre:** `Research_To_Strategy`

**Descripción:** Convierte research crudo (reviews, ads library, datos de Motion) en un diagnóstico de marca accionable y un creative roadmap priorizado. Resuelve el problema de parálisis por análisis: equipos que acumulan data pero no saben qué producir ni en qué orden. Se activa cuando hay research disponible pero no hay claridad sobre qué ads hacer primero.

**Trigger:**
- "No sé qué ads hacer con toda esta data"
- "Tengo los reviews del cliente, ¿qué hago ahora?"
- "Ayúdame a priorizar las ideas creativas"
- "Necesito armar el roadmap del mes"
- "¿Qué debería producir este sprint?"
- Cuando el usuario comparte un CSV de reviews sin un plan de acción
- Cuando hay ads library de un competidor sin un ángulo definido

**Inputs requeridos:**

El agente debe verificar que existan ANTES de proceder. Si falta alguno, pedirlo explícitamente en este orden de prioridad:

| Input | Formato | ¿Obligatorio? | Si falta, pedir: |
|---|---|---|---|
| CSV de reviews del brand | Archivo CSV | Obligatorio | "Necesito el CSV de reviews para extraer las personas reales. ¿Puedes exportarlo desde tu plataforma de reviews?" |
| URL de ads library del brand o competidor | URL directa | Obligatorio | "¿Tienes el link a la ads library del brand en Meta? Lo necesito para comparar a quién apuntan los ads vs. quién compra." |
| Nombre del brand y descripción del producto | Texto libre | Obligatorio | "Dame el nombre del brand y una descripción corta del producto para contextualizar el análisis." |
| Diagnóstico previo (si existe) | Texto o doc | Opcional | Si no existe: arrancar diagnóstico desde cero. Notificar al usuario. |
| Calendario de marketing del trimestre | Texto o doc | Opcional | Si no existe: el roadmap se construye sin fechas de producto/holidays. Notificar. |

**Razonamiento interno (el agente debe ejecutar este checklist antes de producir el output):**

```
PASO 1: ¿Tengo el CSV de reviews? 
  → Si no: detener y pedir.
  → Si sí: extraer 5 personas con nombre de trigger. 
    Verificar que el AI justifique cada persona con citas reales de reviews.
    Si no hay citas, marcar la persona como "no verificada" y pedirle al usuario confirmación.

PASO 2: ¿Tengo la ads library?
  → Analizar a quién parecen apuntar los ads actuales (personas de ads).
  → Extraer: personas primarias, personas secundarias, patrones de hook, % de partnership ads.

PASO 3: Comparar personas de ads vs. personas de reviews.
  → ¿Hay gap? El gap es la oportunidad. Nombrarlo explícitamente.
  → ¿Personas con alta intensidad emocional pero bajo volumen en reviews? 
    Marcarlas como "alto potencial no explotado."

PASO 4: Construir el diagnóstico.
  → El diagnóstico es UN statement de 1-2 oraciones que explica el WHY detrás de los ads a producir.
  → Criterio de validez: debe poder responder "¿por qué estamos produciendo esto ahora?"
  → Si el diagnóstico es "hagamos de todo," no es un diagnóstico válido. Iterar.

PASO 5: Clasificar las ideas por nivel de evidencia.
  → High confidence: formatos, messaging o personas ya pressure-tested que funcionan.
  → Low confidence: ideas basadas solo en que el competidor lo hace o en running time sin contexto.
  → Rechazar automáticamente evidencia de tipo "el competidor lo lleva X días corriendo" sin más datos.

PASO 6: Construir el roadmap.
  → Estructura de 4 partes: Creators / Icebox / Quarterly / Monthly.
  → El Icebox no se filtra. Todo entra. Nadie es juzgado por lo que está ahí.
  → El Monthly prioriza: qué puede salir esta semana (low hanging fruit) vs. qué requiere producción mayor.
```

**Instrucciones:**

Si el usuario pide priorizar más de 2 personas al mismo tiempo para testing, recomendar empezar con 1-2 y distribuir el resto quarterly. No testear 5 personas simultáneamente.

Si el diagnóstico resulta en "producir de todo sin foco," hacer push back. El diagnóstico debe tener un "why" claro.

Si una idea en el roadmap tiene como única evidencia el running time del competidor, clasificarla como Low Confidence y explicar por qué: el ad puede estar buried en retargeting.

Si la persona que compra (reviews) difiere significativamente de la persona que targeteamos en ads, hacer de ese gap el primer item del roadmap.

Si el usuario pide incluir ads promocionales no-evergreen (Mother's Day, descuentos de temporada) como prioridad principal, recordar que el rol del creative strategist no es producir esos materiales. Sugerir un MVP process separado para sacarlos rápido y no contaminar el roadmap estratégico.

Si el AI extrajo personas sin citas de reviews para respaldarlas, agregar nota: "Solicitar al LLM que justifique cada persona con quotes específicas antes de usarlas como base creativa."

El diagnóstico se rediagnostica cada trimestre. Incluir esa cadencia en el output.

**Output esperado:**
1. 5 personas con nombre de trigger, core story, demo básico y citas de reviews que las respaldan
2. Comparación visual: personas de ads vs. personas de reviews, con el gap marcado
3. Diagnóstico en 1-2 oraciones
4. Clasificación de ideas: High Confidence / Low Confidence
5. Roadmap en 4 secciones: Creators / Icebox / Quarterly / Monthly
6. Tier de edits recomendados para la primera semana: Tier 1 (iteration) / Tier 2 (post-production) / Tier 3 (net new)

**Herramientas necesarias:**
- Claude Cowork o equivalente con acceso a URLs (para analizar ads library)
- Capacidad de leer CSV (para procesar reviews)
- Motion (para cruzar con AI tagging de intended audience si está disponible)
- Meta Ads Library (URL pública, no requiere auth)

---

## SKILL 2: AD_PRODUCTION_AI

**Nombre:** `Ad_Production_AI`

**Descripción:** Produce ads estáticos y animados usando AI. Tiene dos modos: Quick Win (clonar el DNA visual de un ad competidor y adaptarlo al brand propio) y Sistema Escalable (generar múltiples ads con consistencia de marca usando Brand Spec Cards, Format Templates y Copywriting Agents). Se activa cuando el usuario tiene un brief o una idea y quiere materializar un ad con AI.

**Trigger:**
- "Quiero hacer un ad con AI"
- "Ayúdame a clonar este ad de la competencia"
- "Necesito animar este static"
- "Genera un headline ad para este producto"
- "Quiero construir el sistema de producción con Claude Code"
- Cuando el usuario comparte una imagen de un ad competidor y pide adaptarlo
- Cuando el usuario tiene un brief aprobado y necesita generar el visual

**Inputs requeridos:**

| Input | Formato | ¿Obligatorio? | Si falta, pedir: |
|---|---|---|---|
| Modo de producción | Selección: Quick Win o Sistema Escalable | Obligatorio | "¿Quieres un resultado rápido (Quick Win) o estás construyendo un sistema para generar muchos ads consistentes (Sistema Escalable)?" |
| Ad de referencia a clonar (Quick Win) | Imagen o URL | Obligatorio en QW | "¿Tienes el ad de referencia que quieres usar como base de DNA visual? Sube la imagen." |
| 2-3 ads propios como referencia de brand | Imágenes | Obligatorio | "Necesito 2-3 ads del brand con fonts y colores claros para que el modelo pueda matchear la identidad visual." |
| Imagen del producto | PNG/JPG | Obligatorio | "Necesito la imagen del producto con fondo transparente o limpio, descargada desde el website." |
| URL + descripción del producto | Texto | Obligatorio | "Dame la URL del producto y una descripción. Si quieres, copia todo el texto de la página del producto." |
| Brand guidelines (Sistema Escalable) | PDF o doc | Opcional | Si existe: convertir a markdown primero. Si no existe: construir desde brand extraction prompt. |
| Persona, ángulo y emoción del ad | Texto | Obligatorio en SE | "Para el Sistema Escalable necesito: ¿a qué persona va dirigido este ad? ¿Cuál es el ángulo (problema que resuelve)? ¿Qué emoción quieres activar?" |

**Razonamiento interno:**

```
PASO 1: ¿Cuál es el modo? Quick Win o Sistema Escalable.

--- SI ES QUICK WIN ---

PASO 2: ¿Tengo el ad de referencia?
  → Si no: detener y pedir.
  → Si sí: extraer el DNA visual completo:
    - Formato del ad (headline, before/after, statistics, etc.)
    - Estructura de copy
    - Layout y composición
    - Background
    - Tipografía (familia, peso, jerarquía)
    - Dispositivos visuales
    - Paleta de colores
    - Espaciado

PASO 3: Adaptar al brand propio.
  → Reemplazar copy basado en la descripción del producto.
  → El copy cambia completamente. El DNA visual se mantiene.
  → No clonar verbatim. Extraer la estructura, no el contenido.

PASO 4: Verificar que el prompt para NanoBanana 2 tenga entre 1000 y 1500 palabras.
  → Si es menor a 800: demasiado corto. El modelo va a hacer suposiciones malas. Expandir.
  → Si supera 2000: puede generar inconsistencias. Reducir.
  → Regla: si quieres algo específico (un rayo de luz tocando el producto), escríbelo explícitamente.

PASO 5: ¿Las fonts y colores se están pasando como texto (hex codes)?
  → Si sí: STOP. NanoBanana 2 no entiende hex codes en texto.
  → Solución: inspeccionar el HTML del website, buscar "font", copiar código, crear Brand Spec Card como imagen PNG.
  → Claude no puede extraer fonts y colores correctamente. No intentarlo.

--- SI ES SISTEMA ESCALABLE ---

PASO 2: ¿Existen Brand Spec Card y Visual Style Card?
  → Si no existen: construirlas primero. Sin ellas el sistema no funciona.
  → Brand Spec Card: logos, fonts (headline/UI/subheaders/body), colores, do's/don'ts, CTAs → convertir a PNG.
  → Visual Style Card: dirección de fotografía, styling rules, quote del founder, ejemplos de ads → convertir a PNG.
  → Guardar ambas en el proyecto. Si no se guardan, nada más funciona.

PASO 3: ¿Existe el Format Template para el formato solicitado?
  → Si no existe: recolectar 50-100 ads del mismo formato (usar ImageEye desde Facebook Ads Library).
  → Subir a Claude: "Clasifica estos como diferentes tipos de ads."
  → El template define: estructura de copy, layout, dispositivos visuales. Es el recipe card.
  → Guardar como .md en el proyecto.

PASO 4: ¿Existen los Copywriting Agents?
  → Los 6 agentes necesarios: Persona Fit / Angle / Emotion / Brand Fit / Conversion / Grammar.
  → El Grammar Agent debe incluir explícitamente: "no m-dashes."
  → Cada agente tiene: role, job description, scoring criteria.
  → Threshold mínimo para aprobar: 90/100 por cada agente.
  → Si algún agente no existe, construirlo antes de proceder.

PASO 5: Generar el brief.
  → Input: persona + ángulo + emoción + brand bible + format template.
  → Output: headlines, subheaders, copy, dirección creativa.

PASO 6: Ejecutar agent review.
  → Proceso automático, ~20 minutos.
  → Si algún agente da menos de 90: iterar hasta alcanzar el threshold en todos.

PASO 7: Convertir brief aprobado a prompt de NanoBanana 2.
  → 1000-1500 palabras. Mismo criterio que Quick Win.

PASO 8: ¿Se va a animar el static?
  → ¿El static es el start frame o el end frame?
  → Generar el frame faltante con NanoBanana 2.
  → Ser explícito en el prompt de Claude: "This image is my start frame. This image is my end frame."
  → El prompt para Veo 3.1 debe ser JSON. No text-based. Sin JSON, el modelo hace suposiciones.
  → Usar "frames" en Veo, no "ingredients."
  → Primera pasada probablemente imperfecta. Descargar como GIF, volver a Claude con los problemas específicos, pedir JSON corregido. Repetir 2-3 veces.
```

**Instrucciones:**

Si el usuario intenta subir un static directamente a Veo/Cling para animarlo sin definir start y end frame: detener. Explicar que no funciona. El static es uno de los dos frames, no el input completo.

Si el usuario pide pasar hex codes de colores al modelo en texto: detener. Crear Brand Spec Card como imagen primero.

Si el usuario pide usar AI para UGC: informar que esta práctica tiene implicaciones éticas y de percepción de mercado documentadas. No ejecutar sin que el usuario confirme que es una decisión consciente y asume las consecuencias.

Si el usuario pide guardar el sistema en Claude Chat en lugar de Claude Code: advertir que Chat requiere guardado manual. Si un archivo no se guarda en el proyecto antes de cerrar la sesión, se pierde. Claude Code guarda automáticamente. Recomendar Claude Code para el sistema escalable.

Si el usuario sube un PDF como brand guidelines: convertir a markdown primero. Claude no lee PDFs de forma confiable para extracción de datos estructurados.

Si el usuario quiere multiplicar un ad ganador en otros formatos: usar el prompt "I have this winning ad. Here are my other format templates. For each format, rewrite the brief to match that template. Same persona, angle, emotion."

**Output esperado (Quick Win):**
1. DNA visual extraído del ad de referencia (8 componentes)
2. Prompt de NanoBanana 2 adaptado al brand (1000-1500 palabras)
3. Checklist de assets necesarios para ejecutar en Fal.ai
4. Si aplica: concepto de animación + JSON prompt para Veo 3.1

**Output esperado (Sistema Escalable):**
1. Brand Spec Card + Visual Style Card (instrucciones de construcción si no existen)
2. Format Template en .md
3. 6 Copywriting Agents en .md con thresholds
4. Brief aprobado por todos los agentes
5. Prompt de NanoBanana 2 (1000-1500 palabras)
6. Instrucciones de ejecución en Fal.ai con spec cards

**Herramientas necesarias:**
- Claude (Chat o Code, preferentemente Code para sistema escalable)
- Fal.ai (acceso a NanoBanana 2, $0.08/generación)
- Google Labs / Veo 3.1 (para animaciones, JSON prompts)
- ImageEye o Image Downloader (Chrome plugin, para recolectar ads de Facebook Ads Library)
- Motion o Meta Ads Library (para research de ads de referencia)

---

## SKILL 3: CREATIVE_ANALYTICS

**Nombre:** `Creative_Analytics`

**Descripción:** Analiza el performance de ads activos para diagnosticar qué no está funcionando y qué debe iterarse, basándose en una jerarquía de métricas específicas. No reporta lo que pasó: forma una perspectiva analítica independiente y produce hipótesis accionables clasificadas en TRUE, FALSE o NEEDS MORE TIME. Se activa cuando el usuario tiene datos de performance y necesita saber qué hacer con ellos.

**Trigger:**
- "¿Por qué este ad no está funcionando?"
- "Analiza estos resultados de mis ads"
- "¿Qué itero primero?"
- "Mi CTR está bajo, ¿qué hago?"
- "Mi hook rate está bien pero no convierto"
- Cuando el usuario pega métricas de Meta Ads Manager
- Cuando el usuario comparte un screenshot o export de Motion
- Cuando el usuario pregunta qué ad debería escalar

**Inputs requeridos:**

| Input | Formato | ¿Obligatorio? | Si falta, pedir: |
|---|---|---|---|
| Métricas de performance | CSV, screenshot o tabla pegada | Obligatorio | "Necesito los datos de performance. Puedes pegar la tabla directamente, compartir un screenshot del Ads Manager, o subir el CSV exportado de Motion." |
| Etapa de funnel analizada | Prospecting o Retargeting | Obligatorio | "¿Estos ads son de prospecting (audiencias frías) o retargeting (quienes ya interactuaron)? No puedo mezclar ambos en el mismo análisis." |
| Goal metric del negocio | ROAS / CPP / CPL / Cost per form | Obligatorio | "¿Cuál es el bottom line metric para este brand? ¿ROAS, costo por compra, costo por lead?" |
| Duración de los videos (si aplica) | Segundos por ad | Recomendado | "¿Cuánto duran los videos que estoy analizando? Lo necesito para interpretar los porcentajes de completion en segundos reales." |
| Benchmark histórico propio | Promedio de cuenta | Opcional | "¿Tienes el promedio histórico de tu cuenta para First Frame Retention y Thumb Stop? Si no, usaré los benchmarks generales como referencia." |

**Razonamiento interno:**

```
ANTES DE ANALIZAR: 
  → ¿Los datos son solo de prospecting? Si hay retargeting mezclado: detener y separar.
  → La mezcla de ambas etapas invalida el análisis. Son comportamientos fundamentalmente distintos.

JERARQUÍA DE ANÁLISIS (en este orden, siempre):

NIVEL 1: Bottom Line Metric + Spend
  → ¿Hay ads con alto spend Y buen goal metric? Esos son los winners.
  → Si hay spend alto pero mal goal metric: no es winner aunque tenga buen engagement.
  → Decisión para winners: escalar spend o producir más ads muy similares.
  → Si no hay ningún winner claro: el problema puede ser la oferta o la landing, no el creative.

NIVEL 2: First Frame Retention
  → Benchmark: >90%.
  → Si está por debajo de 90%: el problema está en el thumbnail o el primer frame.
  → Acción: cambiar la primera imagen/frame antes de tocar cualquier otra cosa.
  → DIFERENCIA CLAVE con Thumb Stop: First Frame mide si alguien INICIÓ el video. 
    Thumb Stop mide si alguien vio al menos 3 segundos.

NIVEL 3: Thumb Stop Ratio (Hook Rate)
  → Mide los primeros 3 segundos (Meta). Los primeros 2 o 6 segundos en TikTok.
  → Si es bajo pero First Frame está bien: el hook falla, no el thumbnail.
  → Benchmark: anclar contra el propio histórico de cuenta PRIMERO, no contra industria.
  → Si no hay histórico: usar los mejores ads de la cuenta actual como referencia.
  → Hipótesis a formular: "quiero aumentar el thumb stop manteniendo el CTR actual."

NIVEL 4: 100% Video Play Rate (Hold Rate)
  → Analizar junto con el CTR, nunca solo.
  → Alto hold rate + bajo CTR: el CTA es el problema. Mover el CTA más arriba o hacerlo más fuerte.
  → Bajo hold rate + alto CTR: el video es demasiado largo. La gente convierte antes de terminar de ver. Acortar.
  → SIEMPRE convertir % de completion a segundos reales. 
    25% de un video de 20 segundos = 5 segundos. Ese es el dato relevante.
  → Drop-off alto + CTR alto = la gente está clickeando, no huyendo. No es un problema.
  → Drop-off alto + CTR bajo = misión crítica. Hay atención sin conversión.

NIVEL 5: CTR
  → Mide si el contenido está motivando acción.
  → Un CTR alto con bajo goal metric indica problema en la landing o en la oferta, no en el creative.
  → Un CTR bajo con buen hold rate indica que el CTA no está funcionando.

FORMULAR HIPÓTESIS:
  → Para cada ad problemático, formular una hipótesis específica.
  → Formato: "El problema es [métrica X]. La hipótesis es que [cambio Y] va a [resultado Z]."
  → Cada hipótesis se clasifica: TRUE / FALSE / NEEDS MORE TIME post-testing.

DIAGNÓSTICO DE ITERACIÓN:
  → Tier 1: Si el problema es solo el hook → swap de los primeros 3 segundos.
  → Tier 2: Si el problema es el messaging completo → cambiar voice overlay o copy.
  → Tier 3: Si el problema es estructural → nuevo creator con el mismo winning formula.
```

**Instrucciones:**

Si el usuario pide comparar sus métricas contra benchmarks de industria como primer paso: redirigir. El benchmark correcto es la propia cuenta primero. Los benchmarks de industria son referencia secundaria.

Si el hold rate es bajo pero el CTR es alto: no tratar como problema. Explicar que la gente está clickeando antes de terminar el video, lo cual es el comportamiento deseado.

Si el usuario quiere iterar sin haber identificado primero cuáles son sus top performers: detener. El análisis siempre empieza por identificar los winners (alto spend + buen goal metric). Las iteraciones se diseñan mirando los winners, no los losers.

Si hay ads con alto engagement pero sin spend: pueden estar en fase de aprendizaje o el algoritmo no está encontrando un responsive pocket para esa señal creativa. No es rechazo. Sugerir cambiar targeting o estructura antes de descartar el ad.

Si el usuario pide interpretar métricas de video sin saber la duración del video: pedir la duración antes de diagnosticar. Un 25% de completion es completamente diferente en un video de 10 segundos vs. uno de 60.

**Output esperado:**
1. Tabla de top performers identificados (alto spend + strong goal metric)
2. Diagnóstico por ad problemático: qué métrica específica falla y en qué nivel de la jerarquía
3. Lista de hipótesis accionables en formato: problema → cambio propuesto → resultado esperado
4. Tier de iteración recomendado para cada hipótesis (1, 2 o 3)
5. Clasificación post-testing esperada: TRUE / FALSE / NEEDS MORE TIME

**Herramientas necesarias:**
- Motion (vista de bar chart con ejes Spend/Goal Metric, funnel de video 25-50-75-100%, hover para fórmulas de métricas)
- Meta Ads Manager (fuente de datos si no se usa Motion)
- Capacidad de leer CSV o interpretar screenshots

---

## SKILL 4: EXPLORE_NEW_ANGLE

**Nombre:** `Explore_New_Angle`

**Descripción:** Detecta cuándo el messaging actual de un brand se está agotando y construye el proceso para identificar, validar e iterar un nuevo ángulo o USP. No genera creativos: genera la hipótesis estratégica y el plan de validación mínimo. Se activa cuando los ads actuales están perdiendo eficiencia sin una causa técnica clara, o cuando el usuario quiere abrir un nuevo ángulo de comunicación.

**Trigger:**
- "Mis ads ya no convierten igual y no sé por qué"
- "Necesito un ángulo nuevo para este brand"
- "El mensaje que teníamos ya no está funcionando"
- "¿Cómo encuentro un nuevo USP?"
- "Vi algo en TikTok que puede ser un insight"
- "El mercado está hablando diferente al brand"
- Cuando el usuario reporta caída de performance sin cambios técnicos en la cuenta

**Inputs requeridos:**

| Input | Formato | ¿Obligatorio? | Si falta, pedir: |
|---|---|---|---|
| Descripción del messaging actual | Texto libre | Obligatorio | "¿Cuál es el mensaje principal que estás usando ahora en tus ads? ¿Cómo describes el producto en los hooks actuales?" |
| Señal de mercado o insight detectado | Texto, URL, screenshot | Obligatorio | "¿Hay algo que hayas visto en orgánico, en comentarios, en reviews o en Google Trends que te haga pensar que hay algo ahí? Compártelo." |
| Brand + categoría de producto | Texto | Obligatorio | "¿De qué brand y categoría de producto estamos hablando?" |
| Datos de performance reciente | Métricas o descripción | Recomendado | "¿Tienes datos de los últimos 30 días que muestren la caída? Aunque sea una descripción de qué está pasando con el CPA o el hook rate." |
| Restricciones de claim (salud, legal, etc.) | Texto | Condicional | "¿Hay restricciones en lo que puedes decir sobre el producto? ¿Es una categoría regulada (salud, finanzas, suplementos)?" |

**Razonamiento interno:**

```
PASO 1: ¿El messaging actual se está agotando o hay un problema técnico?
  → Si hay caída de performance sin cambio en targeting/presupuesto: probable saturación de mensaje.
  → Si la caída es simultánea con cambio de presupuesto o audience: problema técnico, no de ángulo.
  → Si no hay certeza: recomendar análisis con CREATIVE_ANALYTICS primero.

PASO 2: ¿Cuál es la señal de mercado que disparó esto?
  → Fuentes válidas de señal: TikTok orgánico, comentarios de YouTube, Google Trends, reviews, Reddit, comentarios de Facebook.
  → La señal no necesita ser viral. Necesita tener respuesta emocional real ("anecdotally in the comments, people were like, oh my God").
  → Si la señal es solo "vi que un competidor lo está haciendo": Low Confidence. Puede estar buried en retargeting.

PASO 3: ¿La señal conecta con algo que el producto ya puede ofrecer?
  → Buscar la conexión entre el insight de mercado y los assets/features existentes.
  → Si requiere un feature nuevo: documentar el insight y escalar al equipo de producto. 
    El strategist tiene el poder de influir en el producto, no solo en los ads.
  → Si hay conexión con algo existente: definir el nuevo ángulo.

PASO 4: ¿Hay implicaciones de claim que necesiten investigación?
  → Si la categoría es salud, finanzas, suplementos: investigar la ciencia o regulación antes de continuar.
  → Establecer distinciones claras si el ángulo roza claims terapéuticos o técnicos.
  → El objetivo es "posicionar como soporte" no "claims clínicos."

PASO 5: ¿El lenguaje del mercado está cambiando?
  → Verificar: ¿sigue siendo el lenguaje del messaging actual el que usa la gente?
  → Ejemplo: "ansiedad" vs. "regulación del sistema nervioso." Mismo problema, lenguaje diferente.
  → El ángulo nuevo debe hablar el idioma actual, no el idioma del año pasado.

PASO 6: Diseñar el plan de validación mínima.
  → Mínimo: 3 ads para validar la hipótesis. No escalar antes de validación.
  → Distribución recomendada: 2 ads in-house con scripts ligeramente distintos + 1 UGC simple.
  → En el primer batch: testear el messaging. No sobreoptimizar la producción.
  → Métricas de validación: hook rate, hold rate, y si el algoritmo está "amando" los ads (spend acelerando).
  → Si a los 30 días el CPA no mejora pero las métricas de engagement son positivas: continuar iterando (no pivotear todavía).
  → Si engagement Y CPA fallan: pivotar.

PASO 7: Formular la hipótesis del ángulo nuevo.
  → Formato: "La hipótesis es que [target persona] está buscando [resultado específico] usando el lenguaje de [insight de mercado]. Si comunicamos el producto como [posicionamiento], esperamos ver [métrica específica] mejorar."
```

**Instrucciones:**

Si el usuario quiere escalar el nuevo ángulo antes de tener datos de validación: detener. El mínimo son 3 ads y datos de al menos 2-3 semanas antes de escalar presupuesto.

Si la señal de mercado viene únicamente de que "el competidor lo está haciendo": tratar como Low Confidence. Buscar señal primaria en comentarios, reviews o trends antes de construir el ángulo.

Si el ángulo toca claims de salud o finanzas: incluir paso de investigación científica o legal antes de producir los ads. El riesgo de no hacerlo es compliance.

Si el usuario dice "ya probamos eso y no funcionó": preguntar cuándo, con qué presupuesto y con qué formato. El sesgo de "ya lo intentamos" descarta oportunidades válidas que fallaron por mala ejecución, no por mal ángulo. Las cosas cambian.

Si el producto necesita un feature nuevo para que el ángulo funcione: documentar el insight y recomendar escalar al equipo de producto. El creative strategist tiene impacto más allá de los ads.

**Output esperado:**
1. Diagnóstico: ¿el problema es saturación de mensaje o algo técnico? ¿Por qué?
2. Análisis de la señal de mercado: fuente, respuesta emocional observada, nivel de confianza
3. Conexión entre la señal y el producto (qué puede ofrecer ya vs. qué requeriría desarrollo)
4. Nuevo ángulo propuesto con hipótesis formulada en formato estándar
5. Plan de validación mínima: 3 ads con distribución, métricas de éxito y criterio de decisión a 30 días
6. Red flags de claim a verificar antes de producir

**Herramientas necesarias:**
- Google Trends (verificar volumen de términos)
- TikTok / YouTube / Reddit (para leer señales orgánicas)
- Motion (para correlacionar caída de performance con timeline)
- Claude (para analizar comentarios y patterns de lenguaje)

---

## SKILL 5: EXPLOIT_WINNER

**Nombre:** `Exploit_Winner`

**Descripción:** Toma un ad ganador validado y construye el plan completo de escalado: qué iteraciones hacer en qué orden, cómo construir ad families, cómo generar ideas originales cuando las iteraciones se agotan, y cómo estructurar un programa UGC a escala. Opera en la fase Exploit del ciclo creativo. Se activa cuando el usuario tiene un winner con datos suficientes y quiere extraerle el máximo valor antes de que se fatigue.

**Trigger:**
- "Tengo un ad ganador, ¿cómo lo escalo?"
- "¿Qué hago con este winner?"
- "Quiero hacer iteraciones de este ad"
- "El ad se está fatigando, ¿qué hago?"
- "Necesito más variaciones de lo que está funcionando"
- "¿Cómo armo un programa UGC?"
- Cuando el usuario comparte métricas de un ad con CPA estable + CTR fuerte + spend acelerando

**Inputs requeridos:**

| Input | Formato | ¿Obligatorio? | Si falta, pedir: |
|---|---|---|---|
| El ad ganador (video o imagen) | Archivo o URL | Obligatorio | "Necesito ver el ad ganador. ¿Puedes subir el video o compartir el link?" |
| Métricas de validación del winner | Números o descripción | Obligatorio | "¿Cuáles son las métricas de este ad? Necesito confirmar que cumple los criterios de winner antes de armar el plan de escala." |
| Componente ganador identificado | Texto | Obligatorio | "¿Sabes qué parte del ad está funcionando? ¿Es el script, el talent, el hook visual, o no estás seguro?" |
| Pool de creators disponibles (si aplica) | Lista o descripción | Para escala UGC | "¿Tienes creators con los que puedas trabajar? ¿Son retainers o trabajas por proyecto?" |
| Footage library existente | Descripción | Opcional | "¿Tienes footage grabado que no haya sido usado? ¿Con qué tipo de shots cuentas?" |

**Razonamiento interno:**

```
PASO 1: Verificar que el ad cumple criterios de winner válido.
  Los 5 indicadores deben cumplirse simultáneamente:
  → CPA estable (no mejorando ni empeorando drásticamente)
  → CTR fuerte o engagement grade positivo
  → Corriendo en múltiples audiencias (no solo una)
  → Engagement sano (hook rate, hold rate)
  → Spend acelerando (el algoritmo lo está entregando)
  
  Si falta algún indicador: no es un winner confirmado. Recomendar más tiempo de datos.

PASO 2: Identificar el componente ganador.
  → ¿Es el script? → Aplicarlo a nueva persona o nuevo talent.
  → ¿Es el talent? → Replicar el formato con el mismo talent + variaciones.
  → ¿Es el hook visual? → Mantenerlo como base de todas las iteraciones.
  → Si no está claro: el primer batch de iteraciones sirve para descubrirlo.

PASO 3: Clasificar el winner por nivel (Color Tags):
  → Massive Winner (verde): CPA muy bajo, spend muy alto, corriendo en muchas audiencias.
    → Hacer los swings más grandes: cambiar creator, producto, script completo, género, acento.
  → Scale Up (haciendo bien pero no masivo):
    → Hacer swings pequeños primero. Ver si puede llegar a verde.

PASO 4: Definir el plan de iteración por capas (Easy Scales primero).
  
  CAPA 1 — Easy Scales (ejecutables con recursos existentes):
  → Visual refresh con footage del library (mismas personas, diferentes shots)
  → Talent refresh (mismo script, nuevo creator)
  → Format testing (mismo messaging en static vs. video vs. carousel)
  → Testing de longitud del video (cortar o extender el mismo ad)
  → Testing de orden de messaging (cambiar qué va primero en el script)
  
  IMPORTANTE POST-ANDROMEDA: Solo cambiar el hook o el primer frame visual puede NO ser 
  suficiente para que el algoritmo genere una señal creativa diferente. 
  Necesita variación más significativa.

  CAPA 2 — Expansion Phase (mayor esfuerzo):
  → Nuevo footage con nuevo talent
  → Formatos que requieren diseño específico (animaciones, GIFs, carousels elaborados)
  → Nueva persona + script adaptado (misma emoción, distinto segmento demográfico)
  → Nuevo pain point (mismo producto, diferente problema que resuelve)
  → Nueva estructura narrativa completa

PASO 5: Construir el plan de Ad Families.
  → El winner base + todas sus iteraciones = una familia.
  → Objetivo: cuando el ad base se fatigue, la familia sigue convirtiendo.
  → Luego: generar nuevos standalone ads que puedan crear sus propias familias.
  → El account sano tiene múltiples familias activas en paralelo.

PASO 6: ¿El winner está fatigando Y las iteraciones también?
  → Solo entonces ejecutar el Refresh Total (Versión 2.0).
  → Script nuevo + hooks nuevos + visuals nuevos.
  → El alma del ad debe reconocerse en la versión 2.0 aunque todo lo demás cambie.
  → Analogía interna: Terminator 1 y Terminator 2.

PASO 7: ¿Se necesitan ideas net new? (Cuando el winner y sus familias se han agotado)
  → Aplicar el proceso de James Webb Young adaptado:
    1. Gather: inputs específicos del producto/marca + inputs generales (cultura, psicología, memes, life events)
    2. Mental Mashup: forzar combinaciones entre inputs específicos y generales.
       Ejemplo: "magnesio reduce ansiedad" + "browser con 47 tabs abiertos" = headline.
    3. Validar la idea con 3 criterios:
       → ¿Se siente verdad? ("okay, yeah, that's me")
       → ¿Es específica? (no puede decirla cualquier brand)
       → ¿El ángulo es fresco? (no es solo un claim mejor escrito)
    4. Generar mínimo 10 combinaciones antes de elegir la mejor.
       El error más común: quedarse con la primera idea.

PASO 8: Si el plan incluye UGC a escala, verificar estructura del programa.
  → Equipo necesario: Performance Creative (brief y concepto) + Influencer Team (creators) + 
    Growth/Media Buying (datos de performance en tiempo real).
  → Selección de creators:
    → Core Persona Retainers: mayoría del pool. Matchan la persona con mejor historial de conversión. Son el reliability baseline.
    → Expansion Creators: minoría. Ligeramente fuera de la persona core. Abren audiencias.
    → Post-Andromeda: el niche importa. No "persona de fitness" sino "biohacker que enfoca en macros."
  → Content Buckets: Evergreen/BAU + Product Launches + Seasonal.
  → Pre-brief research: ¿qué funcionó el año pasado? ¿qué está funcionando ahora en el wild? ¿cuál es la hipótesis? ¿nivel de convicción?
  → Concept Formula por cada brief: Título + Ángulo (por qué funciona) + Creative Guardrails (tono, delivery) + Objection Handling anticipado.
```

**Instrucciones:**

Si el usuario quiere iterar un ad que no tiene todos los indicadores de winner confirmados: advertir. Escalar un ad que no es winner real gasta presupuesto en señales equivocadas.

Si el usuario solo quiere cambiar el hook y el primer visual esperando resultados post-Andromeda: informar que eso puede no ser suficiente variación para que el algoritmo genere una nueva señal creativa. Necesita variación más significativa en al menos uno de estos ejes: talent, persona, formato, estructura narrativa, pain point.

Si el usuario interpreta "no spend" en un nuevo ad como rechazo: corregir. El algoritmo no está encontrando un responsive pocket para esa señal creativa específica. Sugerir cambiar targeting o estructura antes de descartar.

Si el usuario quiere copiar directamente el ad de un competidor como iteración de su winner: distinguir entre "extraer DNA visual como referencia" y "copiar verbatim." El segundo siempre produce resultados inferiores. Usar el proceso de James Webb Young para generar ideas originales a partir del insight, no copia directa.

Si el usuario está generando ideas pero se detiene en la primera: insistir en generar al menos 10 combinaciones antes de elegir. La primera idea rara vez es la más específica ni la más fresca.

**Output esperado:**
1. Confirmación o cuestionamiento del status de winner (basado en los 5 indicadores)
2. Componente ganador identificado o plan para descubrirlo
3. Clasificación: Massive Winner (verde) o Scale Up
4. Plan de iteración en capas: Easy Scales → Expansion Phase → Refresh Total
5. Estructura de Ad Family con el winner como base
6. Si aplica: proceso de ideación net new con Mental Mashup y criterios de validación
7. Si aplica: estructura completa del programa UGC con Concept Formula

**Herramientas necesarias:**
- Motion (para confirmar métricas del winner y monitorear performance de iteraciones)
- Claude (para Mental Mashup y generación de ideas net new)
- Meta Ads Manager (para monitorear spend y delivery post-lanzamiento de iteraciones)
- Foreplay / Atria (para competitive tracking si se necesita inspiración de mercado)
- Sistema de producción AI si las iteraciones incluyen nuevas versiones generadas (ver SKILL 2)

---

## SKILL 0: BOOTCAMP_ORCHESTRATOR

**Nombre:** `Bootcamp_Orchestrator`

**Descripción:** Skill de orquestación que determina cuál de las skills anteriores activar basándose en la situación del usuario. Lee el contexto, identifica en qué fase del ciclo creativo está el usuario (Research / Producción / Análisis / Exploración / Escalado) y rutea a la skill correcta. También detecta cuando el usuario está en un estado intermedio entre fases y necesita claridad antes de proceder.

**Trigger:**
- Cualquier input que no active directamente una de las 5 skills anteriores
- "¿Por dónde empiezo?"
- "No sé qué hacer con mis ads"
- "Ayúdame con mi estrategia creativa"
- Cuando el usuario describe una situación sin pedir algo específico

**Razonamiento interno:**

```
Leer el input del usuario y mapear a una de estas situaciones:

¿Tiene research pero no sabe qué producir?
  → RESEARCH_TO_STRATEGY

¿Tiene un brief o idea y quiere hacer el ad?
  → AD_PRODUCTION_AI

¿Tiene ads corriendo y quiere saber qué está pasando / qué iterar?
  → CREATIVE_ANALYTICS

¿Sus ads están perdiendo fuerza y no sabe si el mensaje se agotó?
  → EXPLORE_NEW_ANGLE

¿Tiene un winner y quiere escalarlo?
  → EXPLOIT_WINNER

¿No está claro?
  → Hacer 3 preguntas de diagnóstico:
    1. "¿Tienes ads corriendo ahora mismo?"
    2. "¿Tienes data de performance o estás en la fase de producción?"
    3. "¿Sabes qué quieres producir o necesitas definir eso primero?"
  → Basado en las respuestas, rutear a la skill correspondiente.
```

**Instrucciones:**

Si el usuario mezcla dos fases en un mismo request (ej: "quiero analizar mis ads Y hacer nuevos al mismo tiempo"): separar las tareas y ejecutarlas en orden. Primero CREATIVE_ANALYTICS, luego AD_PRODUCTION_AI o EXPLOIT_WINNER según lo que arroje el análisis.

Nunca saltar a producción sin antes verificar que hay un diagnóstico o un brief. La producción sin dirección estratégica es el error más costoso del ciclo.

---

## MAPA DE CONEXIÓN ENTRE SKILLS

```
RESEARCH_TO_STRATEGY
        ↓
   Diagnóstico + Roadmap
        ↓
AD_PRODUCTION_AI ←→ CREATIVE_ANALYTICS
        ↓                    ↓
    Ads live          Métricas de performance
                             ↓
              ┌──────────────┴──────────────┐
              ↓                             ↓
    EXPLORE_NEW_ANGLE              EXPLOIT_WINNER
    (Si el mensaje se agotó)       (Si hay un winner)
              ↓                             ↓
    Nueva hipótesis validada    Ad families + UGC escalado
              ↓                             ↓
         AD_PRODUCTION_AI ←────────────────┘
              ↓
    Vuelta a CREATIVE_ANALYTICS
```

El ciclo no tiene fin. Cada winner genera ad families, cada familia se fatiga eventualmente, y el ciclo vuelve a EXPLORE o a RESEARCH. El sistema está diseñado para operar indefinidamente, no para resolver un problema puntual.

## 🤖 Claude · 2026-05-01 01:02
Voy a leer los skills del usuario antes de construir nada.

Perfecto. Tengo todo el contexto que necesito del breakdown consolidado de las semanas + la arquitectura de skills. Voy a construir los 5 skills directamente como archivos `.md` listos para instalar, con el pipeline de output → input entre semanas.

Ahora verifico que todo esté en orden y presento los archivos.

5 skills listos. Acá está el breakdown de lo que construí y por qué cada decisión de diseño:

**El pipeline completo funciona así:**

W3 produce un JSON con `w4_handoff` → W4 lo lee y sabe qué producir sin preguntar → W4 produce un JSON con `w5_handoff` → W5 sabe qué ads analizar y con qué hipótesis → W5 produce `w6_handoff` con `explore_trigger` → W6 diseña el test mínimo viable → W6 produce `w7_handoff` con la hipótesis validada → W7 escala. Cuando el winner fatiga, W7 apunta de vuelta a W3 con `w3_rediagnosis_trigger`.

**Las decisiones de diseño que importan:**

El Contrato de Entrada en cada skill es el elemento que hace que el agente no avance con información incompleta. Antes de cualquier razonamiento, verifica que tenga los datos mínimos. Si falta el CSV de métricas en W5, pide el CSV antes de proceder, no improvisa.

El Protocolo de Razonamiento Interno es lo que hace que el output sea consistente. En W5 el agente siempre corre el diagnóstico secuencial en silencio: primero spend, luego first frame, luego thumb stop, luego hold rate, luego CTR, luego goal metric. Ese orden específico viene del transcript de Evan. No es opcional.

Los Guardrails con ✗ son prohibiciones absolutas extraídas de los errores documentados en el bootcamp. El más importante de todos: en W4, NanoBanana 2 no puede recibir fonts/colores en texto, tiene que recibirlos como imagen PNG. Ese error específico destruye el output del ad. Está codificado como guardrail, no como recomendación.

Los Escenarios de Error cubren los casos reales que aparecieron en las clases: el cliente que insiste en una idea de low confidence, el producto nuevo que asume el mismo playbook del anterior (Protocolo Harry's), el ad que no gasta que se interpreta como rechazo cuando Andromeda simplemente no encontró un responsive pocket.

El Grammar Agent en W4 tiene explícitamente "no m-dashes" en sus instrucciones porque Will lo mencionó en el transcript. Eso es nivel de detalle que hace que el sistema produzca copy dentro de tus estándares de escritura sin que tengas que revisarlo.

## 🧑 Adriana · 2026-05-01 01:08
Genera ahora el archivo `skill.md` final siguiendo el estándar de Agent Skills. Debe incluir:

1. Frontmatter YAML: Con los metadatos (nombre, descripción, versión).
2. Sección de Lógica: El paso a paso refinado.
3. Casos de prueba: Crea 3 ejemplos de entradas de usuario que deberían activar esta habilidad y la respuesta esperada. Entrega el resultado como un bloque de código Markdown listo para copiar.

## 🤖 Claude · 2026-05-01 01:14
Voy a leer el estándar real de skill creation antes de escribir una sola línea.

Tengo todo lo que necesito. El estándar es claro: YAML frontmatter + body markdown + evals en `evals/evals.json` separado. Voy a construir el skill maestro del pipeline completo, que es lo que falta: un skill orquestador que activa los 5 y los conecta como sistema.

Pero antes, hay que tomar una decisión de diseño: la solicitud dice "el archivo `skill.md` final" (singular). Lo correcto dado el contexto es generar el **skill orquestador del pipeline completo**, el que activa los 5 como sistema, más el `evals.json` separado como manda el estándar.

3 archivos, estructura completa. Acá el breakdown de las decisiones de diseño:

**Por qué un skill orquestador en vez de 5 skills separados**

El estándar de Anthropic dice que la descripción es el mecanismo de triggering principal. 5 skills separados significan 5 descripciones que compiten, y un agente que necesita saber cuál activar antes de saber en qué etapa está el usuario. Con un orquestador, el agente activa el skill una vez y la tabla de selección de etapa hace el routing internamente. Más limpio, menos fricción.

**Por qué 3 archivos y no 1**

Progressive disclosure es el principio. El `SKILL.md` tiene 359 líneas, dentro del límite de 500. Los esquemas JSON de los 5 outputs sumaban otros 317 líneas, así que van en `references/schemas.md` y el skill los llama solo cuando necesita generar el output de una etapa. El `evals.json` sigue el schema exacto del estándar (`id`, `prompt`, `expected_output`, `files`, `expectations`).

**Las 3 pruebas cubren los 3 entry points más probables**

Eval 1 entra en W3 con el problema más común: "tengo todo pero no sé qué hacer primero." Eval 2 entra directamente en W5 con datos reales de performance diseñados para que el diagnóstico secuencial produzca resultados distintos en cada ad. Eval 3 entra en W7 con un winner que cumple los criterios, para verificar que el agente no solo escala sino que diseña el sistema de ad families. Las `expectations` son assertions verificables, no descripciones vagas, para que el grader del skill-creator pueda evaluarlas en TRUE/FALSE.

## 🧑 Adriana · 2026-05-01 01:18
Aquí tienes cómo complementarlos para llevarlos al siguiente nivel:
1. Mejoras al Eval 1 (Priorización - W3)

* Lo que falta: Gestión de recursos. Un error común de los agentes es proponer 10 ideas geniales que el equipo no puede producir.
* Complemento sugerido: Añade una restricción de "Capacidad de Producción".
* Nueva Expectativa: "El agente debe preguntar o asumir un límite de producción (ej. 3-5 conceptos nuevos) y priorizar basándose no solo en el 'Evidence Ranking', sino en la facilidad de ejecución (Low Hanging Fruit) para desbloquear el CPA rápido."
2. Mejoras al Eval 2 (Análisis - W5)

* Lo que falta: Fatiga de creativos y frecuencia. A veces las métricas son buenas pero el anuncio está "muriendo".
* Complemento sugerido: Introduce la métrica de Frecuencia y Spend Trend.
* Nueva Expectativa: "Si el AD-001 tiene un ROAS de 2.8x pero la frecuencia en los últimos 7 días subió un 20%, el agente debe advertir sobre 'Creative Fatigue' y sugerir una iteración preventiva (W6) a pesar de ser un Winner hoy."
* Ajuste Técnico: "El agente debe detectar si el CTR y el Thumbstop están correlacionados. Si el Thumbstop es alto pero el CTR es bajo, debe diagnosticar específicamente que el problema es el 'Body' o la oferta, no el Hook."
3. Mejoras al Eval 3 (Escalado - W7)

* Lo que falta: Diversificación de plataformas (Omnicanalidad).
* Complemento sugerido: Adaptación de formatos para escala horizontal.
* Nueva Expectativa: "El agente debe sugerir no solo iteraciones de contenido, sino adaptaciones técnicas para diferentes ubicaciones (Placements). Ej: Convertir el 9:16 (Reels) a 1:1 o 4:5 con overlays de texto específicos para el Feed de Facebook, manteniendo el mismo script ganador."
Lo que yo agregaría: Un "Eval de Crisis" (Eval 4)
Falta un escenario donde nada funciona. Esto prueba si el agente tiene "juicio" o si solo sigue pasos mecánicamente.

* Prompt de Crisis: "Llevamos 2 semanas probando los 5 nuevos conceptos de la W3. Todos tienen ROAS < 0.5 y Thumbstop < 10%. El cliente está furioso y quiere pausar todo. ¿Qué hacemos?"
* Expectativa Maestra: El agente NO debe sugerir más iteraciones pequeñas. Debe activar un "Hard Pivot" (W3 Rediagnosis). Debe identificar que el ángulo de comunicación o la oferta misma (Product-Market Fit) es el problema, no el video.

## 🤖 Claude · 2026-05-01 01:23
Voy a leer el evals.json actual antes de modificar nada.

Bien. Ahora voy a leer también el SKILL.md para entender qué cambios de lógica necesito propagar adentro junto con los evals.

Tengo todo el contexto. Ahora voy a hacer los cambios: actualizar el `SKILL.md` con la nueva lógica en W3, W5 y W7, y reescribir el `evals.json` completo con las 4 pruebas mejoradas.

Ahora el `evals.json` completo con las 4 pruebas mejoradas:

4 evals, JSON válido, 382 líneas en el SKILL.md (dentro del límite de 500). Acá el breakdown de cada cambio y por qué va donde va:

**Lo que cambió en el SKILL.md junto con los evals**

Los evals no son solo pruebas, son contratos. Si el eval dice que el agente debe detectar fatiga creativa pero el SKILL.md no tiene esa lógica, el eval falla siempre aunque el agente sea bueno. Por eso cada mejora al eval tiene su contraparte en el skill:

Eval 1 requería que el agente preguntara por capacidad de producción. El SKILL.md ahora tiene ese campo como OBLIGATORIO en el Contrato de Entrada de W3, y el paso 6 del Protocolo de Razonamiento filtra explícitamente por capacidad antes de armar el sprint. El guardrail dice "no proponer más ideas de las que el equipo puede ejecutar" con la razón: el agente no produce los ads, el equipo sí.

Eval 2 introdujo frecuencia y la correlación Thumb Stop vs CTR. En el SKILL.md, el Protocolo de Razonamiento de W5 tiene ahora un paso 5 dedicado exclusivamente a esa correlación, con el diagnóstico diferencial escrito: Thumb Stop alto + CTR bajo = el hook no es el problema, y un guardrail específico que prohíbe recomendar swap de hook cuando el Thumb Stop es alto. El paso 7 es nuevo: detección de fatiga creativa como condición separada del FALSE/TRUE, produciendo la clasificación TRUE+FATIGUE_WARNING.

Eval 3 pedía adaptación de placements. El SKILL.md ahora tiene eso en Easy Scales de W7 con la lógica técnica: 9:16 a 1:1/4:5, text overlays para compensar el reencuadre, y la razón estratégica de por qué importa (CPMs distintos, audiencias que no se solapan con Reels).

Eval 4 es el más importante conceptualmente porque prueba que el agente tiene juicio y no solo sigue pasos mecánicamente. En el SKILL.md eso vive en dos lugares: el guardrail de W7 que dice explícitamente "no sugerir más iteraciones pequeñas cuando todos los conceptos fallaron de forma sistemática", y una nueva fila en la tabla de errores que nombra el patrón exacto (ROAS < 0.5, Thumb Stop < 10% en todos) y lo mapea al Hard Pivot como resolución, no como opción.

## 🧑 Adriana · 2026-05-01 01:28
no le esta faltando el doc de schemas o el nteior sigue funcionando perfectamente?

## 🤖 Claude · 2026-05-01 01:29
El anterior sigue funcionando perfectamente. No necesita actualizarse.

Hay 3 campos nuevos que sí necesitan actualizarse. El `schemas.md` no está roto, pero le faltan campos que los evals ahora exigen en el output del agente. Si el agente los omite, el grader los marcaría como faltantes.

Exacto: el anterior no estaba roto, pero sí incompleto para los 4 evals actualizados. Estos fueron los 4 campos nuevos que se agregaron:

**W3:** `production_capacity` en el roadmap (el número declarado o asumido), y `sprint_slot: "NOW | NEXT_SPRINT | BACKLOG"` dentro del icebox para que quede claro cuándo cada idea entra a producción. `lhf_priority: true` en las ideas del sprint activo para marcar cuáles son Low Hanging Fruit.

**W5:** `fatigue_signal` como objeto completo en cada diagnóstico de ad, con `frequency_7d`, `frequency_change_pct`, `spend_trend` y `recommendation`. Y `bottleneck_layer` como campo separado de `bottleneck_identified` para especificar si el problema está en el hook de 3 segundos, en el body del video, en la oferta, o en el CTA. Esa distinción es exactamente lo que separa el Eval 2 de una respuesta genérica.

**W7:** `placement_details` dentro de cada easy_scale con `source_format`, `target_format`, `text_overlay_required` y `overlay_rationale`. Y `hard_pivot_triggered` + `hard_pivot_reason` en la salida final, que es el campo que el Eval 4 necesita para ser verificable por el grader.

Sin estos campos en el schema, los evals tenían expectations que el agente podría cumplir verbalmente pero nunca en el JSON estructurado, lo que hace el grader inútil para esas expectations específicas.

## 🧑 Adriana · 2026-05-01 02:01
tengo unas sugerencias para mejorar los schemas, que opinas?

1. El Bloque de Contexto Maestro (Copiar y Pegar)"A partir de ahora, tu razonamiento debe regirse por este Framework de 4 Capas:Financial Layer (Rentabilidad Real): No confíes solo en el ROAS de Meta. Usa los datos de Atria para validar el LTV y el margen neto. Si Atria dice que el ROAS real es bajo, prohíbe escalar aunque Meta sea optimista.Psychological Hook Mapping: En las fases de creación (W3/W4), cruza obligatoriamente las reviews de Amazon/[Reviews.io](http://Reviews.io) con los conceptos creativos. Cada 'Hook' debe nacer de un dolor real extraído de la voz del cliente.Andromeda Signal & Formatos: En la fase de escala (W7), deconstruye los winners para generar variantes nativas. Usa los boards de Foreplay para inspiración visual y adapta el contenido a formatos específicos (TikTok vs. Reels vs. Shorts).Feedback Loop (Ciclo Cerrado): Cada éxito en el escalado (W7) debe actualizar automáticamente el diagnóstico de la Semana 3. Lo que funciona hoy es la 'verdad' del próximo ciclo."2. Instrucción para el Manejo de ReportesPara que la IA sepa que debe pedirte los archivos, añade esta instrucción de control:"Actúa bajo el modelo Orchestrator-Workers. Antes de dar un diagnóstico:Solicita el reporte de Motion App para analizar métricas visuales (Thumbstop/Hold Rate) en la Semana 5.Solicita el reporte de Atria para validar la rentabilidad antes de autorizar cualquier escala en la Semana 7.Solicita los boards de Foreplay para asegurar que la producción en la Semana 4 sigue tendencias [validadas.Si](http://validadas.Si) no tengo estos archivos, detén el proceso y pídeme que los suba."3. ¿Por qué es necesario esto?Como mencionan expertos en arquitectura de agentes IA, el problema no es el modelo, sino el contexto de datos. Al darle esta estructura, evitas que la IA genere respuestas genéricas y la obligas a usar "juicio de negocio" basado en tu ecosistema real (Motion, Atria, Foreplay).

## 🤖 Claude · 2026-05-01 02:01
Buenas sugerencias, pero antes de implementar quiero darte mi lectura honesta porque hay cosas que sí mejoran el sistema y cosas que lo complican sin ganancia real.

---

**Lo que sí funciona y debe entrar**

El Feedback Loop (punto 1, capa 4) es la única pieza que cierra un gap real de arquitectura. Hoy el pipeline termina en W7 con `w3_rediagnosis_trigger` como campo de texto libre, pero no hay ninguna instrucción que diga qué datos específicos de W7 deben alimentar el próximo diagnóstico de W3. Eso sí debe codificarse: los winners validados en W7 son la evidencia HIGH CONFIDENCE del siguiente roadmap. Sin ese puente explícito, el ciclo se rompe en la práctica.

El modelo Orchestrator-Workers del punto 2 también resuelve algo real: hoy los contratos de entrada de cada etapa listan los inputs necesarios, pero no dicen qué pasa si el agente no los tiene. La instrucción de "detener y pedir antes de diagnosticar" es el comportamiento correcto y ya está parcialmente en los contratos, pero no está lo suficientemente explícita como regla global. Eso también entra.

---

**Lo que tiene un problema de arquitectura**

El Financial Layer con Atria (punto 1, capa 1) tiene un problema de diseño: Atria no es una fuente que el agente puede interrogar en tiempo real a menos que tengas el MCP de Atria conectado o el usuario suba el reporte manualmente. Si el agente dice "valida el LTV en Atria antes de autorizar escala" pero Atria no está disponible como tool, el skill queda bloqueado en W7 cada vez que el usuario no sube ese archivo. Eso no es un guardrail, es un punto de falla.

La forma correcta de codificarlo es como campo opcional con fallback explícito: si hay data de Atria, úsala como validador del ROAS de Meta. Si no hay data de Atria, declarar explícitamente que el ROAS de Meta se toma como proxy y marcar el análisis como `validation_incomplete`. No bloquear el pipeline, advertir.

Lo mismo aplica al Psychological Hook Mapping (capa 2) y a los boards de Foreplay (capa 3). La lógica de cruzar reviews con hooks ya está en W3. Lo de Foreplay para inspiración visual ya está mencionado en W7. El problema es elevarlos a "obligatorios bloqueantes" cuando son inputs que el usuario puede o no tener. Un skill que se detiene cada vez que falta Foreplay es un skill que nadie va a usar consistentemente.

---

**Lo que cambia y lo que no**

Aquí está mi propuesta concreta de qué entra, cómo, y dónde:

## 🧑 Adriana · 2026-05-01 02:30
Ok pero ene se caso entonces antes de correr el agente debe pedir todos los recursos que necesita, que se suba todo lo que si se tiene y lo que no se tiene se obvia como sugieres pero hace un ALTO antes de empezar para asegurarse de que tiene la mayor cantidad de recursos posibles

## 🤖 Claude · 2026-05-01 02:33
Correcto. Eso es lo que se llama un **Resource Collection Gate**: el agente hace un alto completo al inicio, mapea qué tiene y qué le falta, clasifica cada input como crítico u opcional, y solo entonces arranca.

Lo implemento como una sección global antes de la selección de etapa, más los cambios correspondientes en el `schemas.md`.

Tengo todo lo que necesito. Ahora hago el edit: primero el Resource Collection Gate global, luego el Feedback Loop en W7, y el schemas.md.

Ahora el schemas.md: agregar los campos del Gate y del Feedback Loop.

475 líneas en el SKILL.md, dentro del límite de 500. Bien.

Los dos archivos están actualizados. Acá exactamente qué cambió y por qué cada decisión.

**Lo que entró en el SKILL.md**

El Resource Collection Gate vive como Paso 0, antes de la selección de etapa. Eso es intencional: el agente necesita saber qué tiene antes de saber qué hacer con ello. La tabla de recursos mapea cada input a la etapa que lo necesita y a su clasificación, CRÍTICO / VALIDADOR / ENRIQUECEDOR, que es la distinción que evita que el sistema se bloquee innecesariamente.

El formato de presentación del Gate está escrito como bloque literal de texto que el agente debe producir, con los checkboxes y el mensaje de cierre. Eso no es decorativo, es un contrato de output: si el agente no produce ese bloque, no ejecutó el Gate. Y el guardrail global dice explícitamente qué responder cuando el usuario pide saltar el paso: "Un diagnóstico sin los inputs correctos no es un diagnóstico rápido, es un diagnóstico incorrecto."

En W7 se agregó el guardrail del veto de Atria con su campo `atria_veto: true`, y la sección de Feedback Loop con los 4 campos que se propagan al próximo W3: `winners_validated`, `personas_confirmed`, `angles_exhausted`, y `atria_validation`. Ese bloque es lo que convierte el pipeline de lineal a cíclico de verdad. Sin él, cada W3 empieza de cero aunque el equipo ya tenga semanas de data acumulada.

**Lo que entró en schemas.md**

El bloque `resource_gate` en la salida de W3 permite que el siguiente agente que lea ese JSON sepa exactamente con qué calidad de inputs se produjo ese diagnóstico. Si `reviews_csv: "missing_using_hypothesis"`, el agente de W4 sabe que las personas son hipótesis, no personas validadas, y puede ajustar el nivel de confianza de los ads que produzca.

El bloque `feedback_loop` en la salida de W7 estructura los 4 campos que necesita el próximo W3: los winners como evidencia HIGH_CONFIDENCE, las personas confirmadas con tag `FIRST_SPRINT`, los ángulos agotados con tag `DO_NOT_REPEAT_YET`, y la validación de Atria con el delta entre ROAS de Meta y ROAS real.

**Lo que decidí no hacer**

No convertí Foreplay ni Atria en inputs CRÍTICOS bloqueantes. Foreplay es enriquecedor porque hay veces que no tienes acceso a los boards de ese cliente o simplemente no usas esa herramienta. Atria es validador porque entra en W7, que es una etapa de escala, no de producción: si no tienes el reporte puedes escalar con advertencia, no puedes escalar a ciegas pero tampoco queda todo bloqueado. La distinción importa porque un skill que se paraliza con demasiada frecuencia termina siendo ignorado.

## 🧑 Adriana · 2026-05-01 04:02
algo que deba ajustarse en evals?

## 🤖 Claude · 2026-05-01 04:03
Sí. El Eval 4 (Crisis) es el único que necesita ajuste. Los otros 3 están bien.

El problema del Eval 4 es doble. El prompt no menciona que el agente debería ejecutar el Resource Collection Gate antes de proponer el Hard Pivot, que es el comportamiento nuevo que el skill ahora exige. Y le falta una expectativa que pruebe el Feedback Loop: si el agente recomienda W3, debe especificar qué información del sprint fallido alimenta ese W3 (los ángulos agotados con tag `DO_NOT_REPEAT_YET`, no solo "volvamos a empezar").

Los Evals 1, 2 y 3 tienen un gap menor: ninguno prueba que el agente ejecute el Gate antes de arrancar. No necesitan reescribirse, solo agregar una expectativa cada uno.

Los 3 cambios que se hicieron y por qué:

**Evals 1, 2 y 3: una expectativa nueva cada uno.** La misma en los tres: que el agente ejecute el Resource Collection Gate y publique el bloque de estado antes de cualquier análisis. No reescribí los prompts porque no hace falta: el Gate debe activarse con cualquier entrada, incluyendo prompts que no lo mencionan explícitamente. Si el agente lo salta porque el usuario no lo pidió, el eval falla y eso es exactamente lo que debe detectar.

El Eval 2 además agrega que el agente pregunta por Atria en el Gate, porque W5 es la etapa donde la validación de rentabilidad real empieza a importar antes de recomendar iteraciones de escala.

El Eval 3 es el más estricto con el Gate porque W7 es la etapa donde Atria pasa de ENRIQUECEDOR a VALIDADOR real: el agente debe pedirlo explícitamente antes de autorizar escala, no como cortesía sino como paso obligatorio del protocolo.

**Eval 4: reescritura del expected_output y 3 expectativas nuevas.** El cambio más importante es el Feedback Loop: el agente antes podía aprobar el eval diciendo "volvamos a W3" de forma genérica. Ahora tiene que demostrar que sabe exactamente qué lleva de vuelta: los 5 ángulos con tag `DO_NOT_REPEAT_YET`, las personas marcadas como `HYPOTHESIS_UNCONFIRMED`, y el diagnóstico anterior marcado como `REQUIRES_REVISION`. Sin esa especificidad, el W3 siguiente empieza de cero en lugar de empezar con los learnings del sprint fallido, que es precisamente el error que el Feedback Loop existe para prevenir.

## 🧑 Adriana · 2026-05-01 04:15
Genera ahora el archivo `skill.md` final siguiendo el estándar de Agent Skills. Debe incluir:

1. Frontmatter YAML: Con los metadatos (nombre, descripción, versión).
2. Sección de Lógica: El paso a paso refinado.
3. Casos de prueba: Crea 3 ejemplos de entradas de usuario que deberían activar esta habilidad y la respuesta esperada. Entrega el resultado como un bloque de código Markdown listo para copiar.

## 🤖 Claude · 2026-05-01 04:19
Antes de escribir una línea, leo el estándar real y el estado actual del skill.

Ahora leo el estado actual del SKILL.md para no reescribir lo que ya está bien.

Tengo todo. El skill actual tiene 476 líneas: está al límite. La solicitud pide agregar 3 casos de prueba como bloques de código Markdown. Si los meto adentro del SKILL.md, lo quiebro en tamaño. La solución correcta según el estándar es exactamente lo que ya existe: los casos de prueba viven en `evals/evals.json`, no en el SKILL.md.

Lo que sí falta, y es lo que la solicitud está pidiendo realmente, es un bloque de código listo para copiar que muestre el skill completo como documento final integrado. Eso se entrega como un solo codeblock Markdown, no como archivo nuevo.

````markdown
```markdown
---
name: motion-creative-pipeline
description: >
  Sistema modular de creative strategy para ads de performance (Meta/TikTok).
  Cubre el ciclo completo: priorizar ideas → producir con AI → analizar métricas
  → explorar nuevos USPs → explotar winners. Actívalo SIEMPRE que el usuario
  mencione ads, creativos, Meta, TikTok, hooks, personas, ROAS, CTR, winners,
  ad library, NanoBanana, Veo, UGC, roadmap creativo, diagnóstico de marca,
  iterar ads, escalar winners, o cualquier combinación de creative strategy y
  paid social. También activar cuando el usuario diga frases como "no sé qué
  producir", "mis ads dejaron de funcionar", "necesito más volumen de creativos",
  "¿cómo analizo esto?", "tengo un winner, ¿qué hago?". Si hay duda, activar.
version: "1.1"
compatibility: >
  Requiere acceso a: Claude (Chat o Code), Fal.ai (NanoBanana 2), Google Labs
  (Veo 3.1), Motion o Meta Ads Library. Validadores opcionales: Atria (LTV/margen),
  Foreplay (inspiración visual). Para el sistema escalable: Claude Desktop o
  Claude Code con filesystem local.
---

# Motion Creative Pipeline
## Sistema de 5 etapas: W3 Priorizar → W4 Producir → W5 Analizar → W6 Explorar → W7 Explotar

El pipeline convierte research en ads, ads en data, y data en decisiones de escala.
Cada etapa produce un JSON estructurado que es el input exacto de la siguiente.
El ciclo termina en W7 y reinicia en W3 cuando hay señal de rediagnóstico.
Los esquemas exactos de salida de cada etapa están en `references/schemas.md`.
Los casos de prueba y evals están en `evals/evals.json`.

---

## Paso 0 — Resource Collection Gate

**Obligatorio antes de cualquier análisis, sin importar la etapa.**

### Mapa de recursos

| Recurso | Etapa | Tipo | Si falta |
|---|---|---|---|
| CSV de reviews (Amazon, Reviews.io, Trustpilot) | W3 | CRÍTICO | Pedir antes de continuar |
| URL o capturas de Meta Ads Library | W3 | CRÍTICO | Pedir antes de continuar |
| Capacidad de producción del equipo (# conceptos/mes) | W3 | CRÍTICO | Asumir 3-5, declararlo |
| Reporte de Motion App (Thumb Stop, Hold Rate, CTR) | W5 | CRÍTICO | Pedir antes de continuar |
| Datos de Atria (LTV, margen neto, ROAS real) | W7 | VALIDADOR | Continuar con advertencia |
| Boards de Foreplay (inspiración visual) | W4/W7 | ENRIQUECEDOR | Continuar, declarar ausencia |
| Brand guidelines o Brand Spec Cards | W4 | ENRIQUECEDOR | Generar durante W4 |
| Footage library (shots para refresh) | W7 | ENRIQUECEDOR | Limitar Easy Scales |
| Objetivo de negocio del trimestre | W3/W7 | ENRIQUECEDOR | Pedir si hay oportunidad |

**CRÍTICO:** el agente se detiene y lo pide. Sin él el análisis no es confiable.
**VALIDADOR:** si falta, declarar `validation_incomplete: true` y continuar con advertencia.
**ENRIQUECEDOR:** no bloquea el pipeline. Solicitar si el usuario lo tiene a mano.

### Protocolo del Gate

1. Identificar la etapa objetivo.
2. Presentar este bloque antes de cualquier análisis:

```
RESOURCE COLLECTION GATE — [Etapa]

CRÍTICOS (necesito estos antes de continuar):
[ ] [recurso] — [instrucción de cómo subirlo]

VALIDADORES (si los tienes, súbelos ahora):
[ ] [recurso] — [instrucción]

ENRIQUECEDORES (opcional, útil si lo tienes):
[ ] [recurso] — [instrucción]

¿Qué tienes disponible ahora mismo?
```

3. Esperar respuesta. No continuar sin los CRÍTICOS o confirmación de que no existen.
4. Publicar estado antes de avanzar:

```
ESTADO DE RECURSOS:
✓ Reviews CSV — recibido (450 reviews)
✓ Ads Library URL — recibido
⚠ Atria report — no disponible → validation_incomplete
✗ Foreplay boards — no disponible → continuamos sin inspiración visual
→ LISTO PARA CONTINUAR CON W[X]
```

5. Fallbacks si falta un CRÍTICO confirmado:
   - Reviews: buscar fuentes alternativas (Google, Instagram, encuestas). Si no hay: personas como HIPÓTESIS, confidence bajo.
   - Motion report: exportar CSV de Meta Ads Manager. Si no: pegar métricas a mano.
   - Ads Library: capturas de pantalla de top ads activos. Nunca analizar sin referencia visual.

**Guardrail global:** si el usuario dice "empieza ya", responder:
> "Entendido. Para darte un análisis útil en lugar de uno genérico, necesito 2 minutos. Dime qué tienes disponible y arrancamos."

---

## Selección de Etapa

| Señal del usuario | Etapa |
|---|---|
| "No sé qué producir / necesito un roadmap" | W3 Priorizar |
| "Quiero hacer el ad / clonar este competidor" | W4 Producir |
| "Analiza mis métricas / qué está funcionando" | W5 Analizar |
| "Lo que funcionaba ya no funciona / nuevo ángulo" | W6 Explorar |
| "Tengo un winner y quiero escalarlo" | W7 Explotar |
| JSON con campo `w4_handoff` | W4 Producir |
| JSON con campo `w5_handoff` | W5 Analizar |
| JSON con campo `w6_handoff` | W6 Explorar |
| JSON con campo `w7_handoff` | W7 Explotar |

Si no es clara: "¿Estás en la fase de producir ads, analizar performance, o escalar un winner?"

---

## W3 — Priorizar Ideas

**Cuándo:** el usuario no sabe qué producir o quiere un roadmap.

### Contrato de entrada W3
- **[CRÍTICO]** CSV de reviews (mín. 50) o URL del producto.
- **[CRÍTICO]** URL de Ads Library o capturas de top ads.
- **[CRÍTICO]** Capacidad de producción (default asumido: 3-5 conceptos/mes).
- **[ENRIQUECEDOR]** Objetivo del trimestre, budget de producción.

Si budget es bajo: recomendar solo Tier 1. Si marca <6 meses: testing amplio antes de duplicar.

### Protocolo de razonamiento W3
1. Analizar ads actuales: personas targetadas, awareness level, % partnership ads.
2. Extraer 5 personas reales de reviews: rankeadas por volumen e intensidad emocional. Cada persona necesita mínimo 3 citas reales. Sin citas: persona inválida.
3. Mapear el GAP: quién compra (reviews) vs. quién aparece en ads. El gap es la primera recomendación.
4. Formular diagnóstico: 1-2 oraciones que responden "¿qué debe hacer este brand con sus ads ahora?" Sin diagnóstico no hay estrategia.
5. Clasificar por Evidence Ranking: HIGH CONFIDENCE (data propia pressure-tested) vs. LOW CONFIDENCE (running time de competidor sin contexto, intuición sin respaldo).
6. Filtrar por capacidad de producción: del universo HIGH CONFIDENCE, seleccionar las que caben en el límite declarado. Priorizar Tier 1 primero — Low Hanging Fruit desbloquea señal de CPA rápido. Ideas que no caben: Icebox con etiqueta NEXT SPRINT.
7. Construir roadmap en 4 partes: Creators / Icebox / Quarterly / Monthly.

### SOP W3
- Máximo 1-2 personas activas simultáneamente.
- Si única evidencia de una idea es running time del competidor: RECHAZAR con explicación (puede estar en retargeting).
- Icebox: sin filtro, nadie es juzgado.
- Monthly: idea + persona + 3 variaciones de messaging.
- Sprint inmediato: producible en ≤1 semana (Tier 1), dentro de la capacidad declarada.
- Rediagnóstico: quarterly. Marcar fecha.

**Tiers de edits:** Tier 1: hook swap, text overlay (<1 semana). Tier 2: voice overlay, nuevo messaging (1-2 semanas). Tier 3: nuevo creator con formula ganadora (2-4 semanas).

### Guardrails W3
- No recomendar 5 personas simultáneas.
- No usar running time de competidor como evidencia principal.
- No aplicar playbook de producto A a producto nuevo B sin research.
- No producir roadmap sin diagnóstico.
- No proponer más ideas en el sprint que las que el equipo puede ejecutar.

### Salida W3
JSON con `resource_gate` y `w4_handoff` → ver `references/schemas.md`.

---

## W4 — Producir Ads con AI

**Cuándo:** el usuario quiere hacer el ad.

Seleccionar método:

| Situación | Método | Hit rate |
|---|---|---|
| Resultado rápido con ad de referencia | Quick Win | 60-70% |
| Volumen alto con consistencia de marca | Sistema Escalable | 90-95% |
| Static ganador → más reach a menor CPM | Animación | variable |

### Contrato de entrada W4
- **[CRÍTICO]** Ad de competidor a clonar O idea propia.
- **[CRÍTICO]** URL del brand + producto + descripción.
- **[CRÍTICO]** 2-3 ads propios con fonts y colores visibles.
- **[CRÍTICO para animación]** Static ad a animar.

### Quick Win (pasos 1-6)
1. Encontrar ad a clonar en Motion o Meta Ads Library.
2. Deconstruir DNA visual con Claude: formato, copy, layout, background, tipografía, visual devices, color palette, spacing. Solo describir elementos, no interpretar el messaging.
3. Reworkear para el brand: URL + producto + descripción. Copy cambia completamente, estructura visual se mantiene.
4. Descargar assets: 2-3 ads propios + imagen del producto + ad clonado.
5. Generar prompt NanoBanana 2 (target: 1,000-1,500 palabras. Nunca <800, nunca >2,000).
6. Ejecutar en Fal.ai: NanoBanana 2, subir prompt + refs + product image, generar 4 variaciones.

### Animación (pasos 7-11)
7. Decidir: ¿el static es start frame o end frame?
8. Generar frame faltante con NanoBanana 2. Ser explícito sobre qué remover/añadir.
9. En Claude: subir ambos frames + concepto de movimiento → solicitar JSON prompt para Veo 3.1.
10. En Veo 3.1: seleccionar FRAMES (no ingredients), 9:16, generar 4 variaciones.
11. Iterar: descargar GIF → describir problema específico a Claude → solicitar JSON corregido. Máx. 3 iteraciones.

### Sistema Escalable (pasos 12-21)
12. Setup: Claude Code o Claude Chat con proyecto.
13. Layer 1: Brand Extraction. Hack fonts: inspeccionar HTML del sitio → copiar sección "font" → subir a Claude. Convertir PDFs a markdown antes de subir.
14. Layer 2: Brand Reference Cards como imágenes PNG (obligatorio). Brand Spec Card: logos, fonts, colores, do's/don'ts. Visual Style Card: dirección fotográfica, styling, ejemplos de ads.
15. Layer 3: recolectar 50-100 ads del mismo formato con ImageEye → clasificar en templates tipo recipe card → guardar como `.md`.
16. Layer 4: Copywriting Agents `.md`. Seis agentes: Persona Fit, Angle, Emotion, Brand Fit, Conversion, Grammar (incluir: "no em-dashes"). Scoring 0-100.
17. Brief Generation: "Crea [formato]. Persona: [X]. Ángulo: [Y]. Emoción: [Z]."
18. Agent Review: "Itera hasta que cada agente dé 90+/100." (~20 min automático).
19. Convertir a prompt NanoBanana 2 (1,000-1,500 palabras).
20. Ejecutar en Fal.ai con Brand Spec Card + Visual Style Card.
21. Multiplicar: mismo ángulo en todos los format templates → agent review → prompt → generar.

### Guardrails W4
- No clonar ads verbatim. Extraer DNA visual, repurposear con copy propio.
- No especificar fonts/colores en texto en el prompt. Siempre como PNG.
- Máx. 2-3 brand references. Más = información contradictoria.
- No text-based prompts en Veo 3.1. Solo JSON.
- Seleccionar FRAMES en Veo, no ingredients.
- No subir static directamente a Kling/Veo sin los dos frames.
- Convertir PDFs a markdown antes de subir a Claude.
- No usar AI UGC (avatares generados).

### Salida W4
JSON con `w5_handoff` → ver `references/schemas.md`.

---

## W5 — Analizar Ads

**Cuándo:** el usuario quiere diagnosticar performance.

Filosofía: cada ad es una hipótesis. Resultado siempre es TRUE / TRUE+FATIGUE_WARNING / FALSE / NEEDS_MORE_TIME. El objetivo no es reportar lo que pasó — es diagnosticar qué cambio produce el mejor resultado.

### Contrato de entrada W5
- **[CRÍTICO]** Datos de performance: CSV de Meta, captura de Motion, screenshot de Ads Manager, o métricas pegadas a mano.
- **[CRÍTICO]** Confirmar que son SOLO datos de prospecting. Si hay mezcla: pedir segmentación antes.
- **[CRÍTICO]** Tipo de negocio → goal metric: D2C (ROAS o CPP), SaaS (CPL o Cost per Appt), otro (definir).
- **[VALIDADOR]** Atria report para validar rentabilidad real.
- **[ENRIQUECEDOR]** Benchmark histórico de la propia cuenta.

Dato mínimo por ad: Spend + 2 métricas de engagement. Si hay menos: INSUFFICIENT DATA.

### Protocolo de razonamiento W5
Para cada ad, en silencio:

1. **Spend + tendencia:** ¿analizable? Sin spend: INSUFFICIENT DATA. Bajo sin razón: posible "no responsive pocket" → NEEDS_MORE_TIME. Si hay frecuencia y spend_trend: evaluar trayectoria de fatiga (paso 7).
2. **Goal metric:** ¿gana en bottom line? Sí → verificar fatiga (paso 7). No → identificar dónde se rompe el funnel.
3. **First Frame Retention:** benchmark ≥90%. Debajo: problema en thumbnail o primer frame.
4. **Thumb Stop (primeros 3s):** bajo + First Frame OK = hook de 3s no engancha. Bajo + First Frame bajo = problema de thumbnail.
5. **Correlación Thumb Stop vs. CTR:**
   - Thumb Stop alto + CTR bajo = el hook funciona. El body o la oferta no convencen. Diagnosticar Tier 2, NO cambiar el hook.
   - Thumb Stop bajo + CTR alto = audiencia muy calificada. Investigar antes de cambiar.
6. **Hold Rate:** alto + bajo CTR = CTA débil. Bajo + alto CTR = video largo (puede ser positivo). Convertir % a segundos reales.
7. **Fatiga creativa:** frecuencia subió >15% semana a semana con spend estable, o ROAS/CTR cayendo sin aumento de spend → TRUE+FATIGUE_WARNING. Acción: iteración preventiva ahora.
8. **Clasificar:** TRUE / TRUE+FATIGUE_WARNING / FALSE / NEEDS_MORE_TIME.
9. **Instrucción de iteración específica** con tier y cambio exacto. Nunca "mejora el hook": siempre "imita los primeros 3 segundos de [ad X]".

**Niveles de hipótesis:** Individual (este ad), Team (patrón en el conjunto), Org (implicación de inversión).

### SOP W5
- Anclar contra benchmark histórico propio. Si no hay: usar set actual como primera línea base.
- Thumb Stop alto + CTR bajo: NO recomendar cambiar el hook. El problema está en el body o la oferta.
- Un winner con señal de fatiga no es pánico: es iteración preventiva inmediata.

### Guardrails W5
- No analizar prospecting mezclado con retargeting.
- No usar benchmarks de industria como criterio principal.
- No declarar fracaso por bajo completion sin revisar CTR.
- No recomendar swap de hook cuando Thumb Stop es alto.
- No ignorar señales de fatiga porque "el ROAS todavía está bien".
- Cada ad debe tener clasificación. Sin clasificación: output inválido.

### Salida W5
JSON con `w6_handoff` → ver `references/schemas.md`.

---

## W6 — Explorar Nuevos USPs

**Cuándo:** lo que funcionaba dejó de funcionar, o se necesita un ángulo nuevo.

Esta etapa SOLO valida — no escala. Test mínimo viable: 3 ads, spend controlado.

### Contrato de entrada W6
- **[CRÍTICO]** Descripción de la señal que indica necesidad de explorar.
- **[CRÍTICO]** Producto a explorar. Si es nuevo en catálogo existente: activar Protocolo Harry's.
- **[ENRIQUECEDOR]** Google Trends, TikTok orgánico, reviews, foros.

Señales que activan exploración: declive en search trends del messaging core, saturación de competidores copiando el mismo formato, CPA subiendo sin cambios en el producto, nueva audiencia no explotada, nuevo producto sin playbook, cambio en el lenguaje del consumidor.

### Protocolo de razonamiento W6
1. Tipo de exploración: ¿cambió el lenguaje? ¿la audiencia? ¿el producto? ¿el mercado?
2. Rastrear señales: Google Trends, TikTok orgánico (comentarios, respuesta emocional), reviews, foros.
3. Conectar señal con assets existentes del producto.
4. Evaluar viabilidad del claim: ¿responsable? ¿con respaldo? ¿implicaciones clínicas o legales?
5. Formular hipótesis: "[señal] + [asset del producto] = [hipótesis de messaging]".
6. Test mínimo viable: 3 ads. 2 in-house scripts diferentes + 1 UGC simple. Solo cambia el messaging, los visuales son control.

**Protocolo Harry's (producto nuevo):** no aplicar playbook anterior sin validar. Confirmar si el comprador es el mismo. Testear si el target entiende el lenguaje técnico. Verificar que referencias de credibilidad resuenen en el segmento geográfico real. Traducir términos técnicos a beneficios antes de usar en ads.

### SOP W6
- Definir antes de lanzar: ¿qué métrica en qué umbral = "hay señal"?
- Umbral de referencia: si en un mes los costos se reducen ~50%, hay señal para escalar.
- "Ya lo probamos y no funcionó" es el sesgo más común. Preguntar: ¿cuándo? ¿con qué ejecución?
- Claims clínicos o regulados: usar el messaging más conservador que siga siendo verdadero.

### Guardrails W6
- No escalar antes de validar con 3 ads mínimos.
- No asumir que el playbook de un producto aplica a otro.
- No usar lenguaje técnico sin verificar comprensión del target.
- No descartar hipótesis tras un solo test sin analizar la ejecución.

### Salida W6
JSON con `w7_handoff` → ver `references/schemas.md`.

---

## W7 — Explotar Winners

**Cuándo:** el usuario tiene un winner validado y quiere escalarlo.

Verificar 5 criterios antes de escalar: CPA estable, CTR fuerte o engagement sano, corriendo en múltiples audiencias, spend acelerando, ROAS dentro de rango.

- 5/5: COLOR TAG VERDE → swings más grandes.
- 3-4/5: COLOR TAG SCALE UP → swings pequeños primero.
- <3/5: no es winner todavía. Pedir más data.

### Contrato de entrada W7
- **[CRÍTICO]** Winning ad (asset o descripción detallada).
- **[CRÍTICO]** Métricas que confirmen los 5 criterios.
- **[VALIDADOR]** Reporte de Atria: pedir explícitamente antes de autorizar escala. Si contradice el ROAS de Meta: marcar `atria_veto: true`, no escalar.
- **[ENRIQUECEDOR]** Footage library, pool de creators, boards de Foreplay.

### Protocolo de razonamiento W7
1. Deconstruir winner: hook (primeros 3s), angle, format, emotional driver. Identificar el driver.
2. Clasificar: VERDE o SCALE UP.
3. Easy Scales (primero): visual refresh con footage existente, talent refresh con mismo script, format testing, length testing, message order testing. En post-Andromeda solo cambiar el hook NO es suficiente. Incluir adaptaciones de placement: 9:16 → 1:1 o 4:5 para Feed con text overlays. Acceden a CPMs distintos y audiencias que no se cruzan con Reels.
4. Expansion Phase (después de Easy Scales): nuevo talent + diferente background + nueva estructura narrativa, persona testing con mismo script, mashup de elementos ganadores.
5. Ad Family: 3-5 batches de 3-5 ads. El 80% del scaling: hooks diferentes, mismo script distintos creators, distintos scripts mismo creator, mismo concepto distinto formato.
6. UGC estructurado (Caraway method): Core Persona Retainers vs. Expansion Creators. Content Buckets: Evergreen/BAU, Product Launches, Seasonal. Concept Formula antes de cada brief.
7. Refresh V2.0: SOLO cuando winner fatiga Y todas las iteraciones fallaron. Mismo alma, nueva producción.

**Concept Formula (obligatoria antes de brief UGC):**
```
1. Concept Title
2. Angle (Why This Works)
3. Creative Guardrails (tono, delivery, restricciones)
4. Objection Handling (objeción → reframe)
```

**Ideación net new (James Webb Young):**
1. Gather: inputs específicos (producto, brand, cliente) + generales (cultura, psicología).
2. Mental Mashup: forzar combinaciones. Ejemplo: "magnesio reduce ansiedad" + "47 tabs abiertos" = "Tu cerebro tiene 47 tabs. El magnesio los cierra todos."
3. Validar con 3 criterios: (a) feels true, (b) específica, (c) ángulo fresco.
4. Si no cumple los 3: volver al paso 2.

### Guardrails W7
- No escalar sin verificar los 5 criterios.
- Solo cambiar el hook no es iteración suficiente en post-Andromeda.
- "Ad que no gasta" ≠ rechazo. Es falta de responsive pocket.
- No hacer Refresh antes de agotar las iteraciones.
- No escalar a volumen alto sin el sistema de W4.
- No publicar la primera idea de ideación. Generar mínimo 5-10 combinaciones.
- Si TODOS los conceptos fallaron (ROAS <0.5, Thumb Stop <10%): activar Hard Pivot → W3 desde cero. El problema no es el video, es el ángulo o el PMF.
- Si Atria contradice ROAS de Meta: `atria_veto: true`. No escalar aunque Meta sea optimista.

### Salida W7 y Feedback Loop

JSON con `feedback_loop` y `w3_rediagnosis_trigger` → ver `references/schemas.md`.

Propagar explícitamente al próximo W3:
```
FEEDBACK LOOP → W3:
- winners_validated: ángulos validados → evidencia HIGH CONFIDENCE del próximo roadmap
- personas_confirmed: personas confirmadas → prioridad automática en el próximo sprint
- angles_exhausted: ángulos agotados → Icebox con etiqueta DO_NOT_REPEAT_YET
- atria_validation: delta entre ROAS Meta y ROAS real
```
Lo que funcionó en W7 es la verdad del próximo ciclo. El próximo W3 no parte de cero.

---

## Manejo de errores entre etapas

| Error | Etapa | Resolución |
|---|---|---|
| Persona inventada sin citas de reviews | W3 | Pedir citas. Sin citas: persona inválida |
| Sprint con más ideas que capacidad del equipo | W3 | Cortar en la capacidad. Resto: Icebox NEXT SPRINT |
| NanoBanana 2 genera elementos extraños | W4 | Añadir instrucción explícita sobre ese elemento |
| Datos de prospecting mezclados con retargeting | W5 | No analizar. Pedir segmentación primero |
| Thumb Stop alto + CTR bajo → recomendar cambiar el hook | W5 | El hook no es el problema. Diagnosticar body/oferta |
| Winner con fatiga ignorada por "ROAS todavía bien" | W5 | La fatiga es tendencia, no snapshot. Iteración preventiva |
| "Ya lo probamos" como razón para no explorar | W6 | Preguntar cuándo y con qué ejecución |
| "Winner" sin cumplir los 5 criterios | W7 | No escalar. Pedir más data |
| Usuario quiere escalar antes de validar | W6/W7 | Documentar el riesgo. Ofrecer 3 ads de test embebidos |
| Todos los conceptos fallaron sistemáticamente | W7 | Hard Pivot: W3 desde cero. No iterar sin señal de vida |

---

## Casos de prueba

Los casos de prueba detallados con sus expectations verificables están en `evals/evals.json`.
Los siguientes son los 3 casos de activación más representativos del skill:

---

**Caso 1 — Entrada en W3 (Priorización)**

*Prompt de prueba:*
> "Tengo una marca de suplementos de magnesio. Mis ads de Meta llevan 3 meses corriendo los mismos conceptos y el CPA subió un 38% el último mes. Tengo aquí el CSV de reviews de Amazon (450 reviews) y el link de mi ads library. No sé si seguir con lo mismo o cambiar de ángulo. ¿Por dónde empiezo?"

*Respuesta esperada:*
El agente ejecuta el Resource Collection Gate para W3. Presenta el bloque de inventario con los inputs CRÍTICOS (reviews, ads library, capacidad de producción) y los VALIDADORES/ENRIQUECEDORES. Espera confirmación. Publica el estado de recursos. Luego: analiza la ads library para extraer personas actualmente targetadas, extrae 5 personas reales del CSV con citas específicas, mapea el GAP entre ambas, formula el diagnóstico en 1-2 oraciones, aplica Evidence Ranking, filtra por capacidad de producción priorizando Tier 1 (Low Hanging Fruit primero para desbloquear señal de CPA rápido), y produce el JSON de salida W3 con `resource_gate` y `w4_handoff`. Las ideas HIGH CONFIDENCE que exceden la capacidad van al Icebox con etiqueta NEXT SPRINT.

*Lo que no debe hacer:*
Saltar el Gate y arrancar el análisis directamente. Recomendar 5 personas para testing simultáneo. Incluir ideas en el sprint que el equipo no puede producir. Aceptar como evidencia el running time de un competidor sin datos de audiencia.

---

**Caso 2 — Entrada en W5 (Análisis con fatiga y correlación Thumb Stop/CTR)**

*Prompt de prueba:*
> "Aquí están mis métricas de la última semana en Meta. Prospecting solamente. ROAS objetivo: 2.5x.
> AD-001: Spend $1,847 / First Frame 94% / Thumb Stop 31% / Hold Rate 18% / CTR 4.2% / ROAS 2.8x / Frecuencia 7d 2.8 (subió 22% vs semana anterior) / Spend trend estable.
> AD-002: Spend $620 / First Frame 88% / Thumb Stop 19% / Hold Rate 67% / CTR 1.1% / ROAS 0.9x.
> AD-003: Spend $340 / First Frame 91% / Thumb Stop 41% / Hold Rate 72% / CTR 6.8% / ROAS 3.1x.
> ¿Qué hago con cada uno?"

*Respuesta esperada:*
El agente ejecuta el Gate para W5: confirma que tiene el reporte de Motion (datos pegados), que son solo prospecting, y pregunta si hay reporte de Atria. Luego diagnostica: AD-001 → TRUE+FATIGUE_WARNING (gana en ROAS pero frecuencia +22% con spend estable es señal de fatiga inminente, iteración preventiva ahora). AD-002 → FALSE con diagnóstico de body/oferta: Thumb Stop bajo + Hold Rate alto (67%) + CTR muy bajo (1.1%) indica que el hook no es el único problema — el cuerpo del video o la oferta tampoco convencen. El agente NO recomienda solo swap de hook; prescribe Tier 2 o superior. AD-003 → TRUE, top performer del set.

*Lo que no debe hacer:*
Saltar el Gate. Recomendar cambiar el hook de AD-002 como solución principal (Thumb Stop es bajo, no alto). Ignorar la señal de fatiga de AD-001 porque "el ROAS todavía está bien".

---

**Caso 3 — Entrada en W7 con Hard Pivot (Escenario de crisis)**

*Prompt de prueba:*
> "Llevamos 2 semanas probando los 5 conceptos nuevos que salieron de la sesión de priorización de la semana pasada. Todos tienen ROAS < 0.5, Thumb Stop < 10% y los que llegaron a gastar algo se apagaron solos en 48 horas. El cliente está furioso y quiere pausar todo. ¿Qué hacemos?"

*Respuesta esperada:*
El agente ejecuta el Gate: pregunta por el reporte detallado de Motion de los 5 conceptos y si hay datos de Atria. Con los datos disponibles, diagnostica falla sistémica: ROAS <0.5 + Thumb Stop <10% en TODOS los conceptos (no en uno) indica que el problema no es la ejecución ni el video — es el ángulo de comunicación o el Product-Market Fit. Activa Hard Pivot hacia W3. No recomienda iterar hooks. Especifica el Feedback Loop: los 5 ángulos van al próximo W3 con tag DO_NOT_REPEAT_YET, las personas del sprint anterior se marcan como HYPOTHESIS_UNCONFIRMED para re-validar, el diagnóstico de marca anterior se marca como REQUIRES_REVISION. Puede validar la decisión de pausar el spend activo. Entrega una agenda estructurada para la sesión de rediagnóstico W3.

*Lo que no debe hacer:*
Saltar el Gate. Recomendar "probemos cambiando el hook del concepto 3". Decir "volvamos a W3" sin especificar qué información del sprint fallido alimenta ese W3. Usar lenguaje de pánico o culpa.
```
````

Eso es todo. El bloque de código es el documento completo listo para copiar, en 3 partes claras:

**Por qué esta estructura y no otra**

El estándar dice que los casos de prueba viven en `evals/evals.json`, no en el SKILL.md. Meter los 4 evals completos con sus expectations dentro del markdown habría llevado el archivo a 650+ líneas, que está sobre el límite de 500 que recomienda el estándar. La solución es exactamente lo que hace el estándar con sus propios skills de referencia: el SKILL.md apunta a los archivos externos, los casos viven en su propio archivo.

Los 3 casos incluidos en el bloque son un resumen ejecutivo de activación: prompt de prueba, respuesta esperada en prosa, y un bloque explícito de "lo que no debe hacer." Esta última sección es la que más valor agrega para entender el skill rápido, porque define los límites de comportamiento tan claramente como la respuesta positiva.

La versión cambió de `1.0` a `1.1` en el frontmatter porque el SKILL tiene cambios sustanciales (Gate, Feedback Loop, Atria, fatiga creativa) que no estaban en la primera versión.

## 🧑 Adriana · 2026-05-01 04:22
Crea un archivo de configuración de Workflow. Define cómo la salida de la `skill_semana_3` (Priorización) sirve como entrada para la `skill_semana_4` (Creación). Establece una regla de validación: el agente no puede pasar a 'Iteración' (Semana 6) sin haber procesado los datos de 'Análisis' (Semana 5).

## 🤖 Claude · 2026-05-01 04:25
Leo primero los schemas actuales para que el workflow hable exactamente los mismos campos que ya existen.

Tengo todos los campos exactos. Ahora construyo el workflow.

JSON válido. Estructura completa:

**5 stages, 5 transitions, 6 global rules, 30 field mappings, 19 validation rules.**

Acá el breakdown de cada decisión de diseño:

**Las 5 transiciones y su lógica**

T1 (W3→W4) tiene 7 field mappings porque es la transición más rica en información: las personas, las ideas, el format recommendation, el tier, la capacidad de producción, el estado de brand guidelines, y las citas de reviews que alimentan directamente el Persona Fit Agent de W4. Sin ese mapping, el agente de W4 produciría copy genérico en lugar de copy anclado en la voz real del cliente.

T3 (W5→W6) es la transición con el gate más duro del sistema porque era el requerimiento central de la solicitud. Tiene un `gate_rule` con `enforcement: "HARD_BLOCK"` separado de las `validation_rules`, con su propio `block_message` que le dice al agente exactamente qué tres cosas necesita de W5 antes de poder continuar. El único bypass documentado es el Hard Pivot desde W7, y está explícitamente condicionado a que `hard_pivot_triggered: true` esté presente en el output.

T5 (W7→W3) no es un reinicio, es una transición informada. Los 5 field mappings de esa transición transforman el output de W7 en inputs estructurados para el próximo W3: los winners se convierten en evidencia HIGH CONFIDENCE automática, los ángulos agotados entran al Icebox con tag DO_NOT_REPEAT_YET, y las personas confirmadas tienen prioridad de first sprint.

**Los 3 niveles de severidad**

`HARD_BLOCK` detiene la ejecución completamente y no tiene bypass. Se usa solo en T3 porque es la regla que pediste explícitamente: sin análisis no hay iteración.

`BLOCK` también detiene la ejecución pero las condiciones son más específicas y en teoría resolubles en el momento. Se usa cuando falta un campo que el usuario puede proveer ahí mismo.

`WARN` continúa con un flag `validation_incomplete: true` en el output. Se usa cuando el campo faltante degrada la calidad del análisis pero no lo invalida por completo, como personas sin citas de reviews o Feedback Loop incompleto.

**El Hard Pivot Rule como objeto separado**

> *[line redacted — references an out-of-scope venture]*
