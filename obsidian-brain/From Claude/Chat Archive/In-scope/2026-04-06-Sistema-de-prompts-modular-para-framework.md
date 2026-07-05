---
title: "Sistema de prompts modular para framework"
source: claude.ai-chat
created: "2026-04-06 17:36"
summary: "**Conversation Overview**  The person, who appears to work in creative strategy and content production (likely at an agency or as a consultant serving clients), asked Claude to help build a Modular Prompt System based on their existing Market Research Framework hosted in Notion. The framework is structured around 8 layers and 23+ steps, focused on writing short-form video hooks using a three-component system (Visual Action + Caption + Voiceover) across funnel levels (TOF, MOF, BOF). The work session involved multiple iterative rounds of building, correcting, and expanding a functional prompt system.  Claude first read the Notion framework, then built an interactive HTML widget app with tabbed navigation across all 8 layers, copy-to-clipboard functionality for each prompt, variable documentation, and execution tips per step. The person then requested the full pipeline printed in order, which Claude delivered. A key correction followed: the person specified that Layer 6 (Execution) needed Evaluation and Iteration steps inserted between each funnel level's generation step, not just at the end — resulting in a 9-step L6 structure (Generate → Evaluate → Iterate for TOF, MOF, and BOF sequentially). The person also requested all content be translated to English throughout. Claude rebuilt the interactive app with these corrections applied, added color-coded step-type badges (Generate, Evaluate, Iterate, etc.), and re-delivered the full corrected pipeline in English. Finally, the person requested a node map visualization of the entire system, first rendered as an SVG inside the widget, then re-requested specifically as a clean HTML version with colored nodes, layer pills, directional arrows, funnel columns for L6, and a legend — which Claude delivered. The session ended with the person requesting the Step 23 Master Table prompt displayed on its own, then asking for it rendered as HTML.  The domain-specific terminology used throughout includes: hook framework, micropersona, scroll-stopping, oddly specific, TOF/MOF/BOF (top/middle/bottom of funnel), visual action, voiceover, caption, motivator, benefit angle, persona pivot, creative pivot, hook type combinations, and master table. The person works with a modular prompt chaining approach where each Claude session loads frameworks first, then runs steps sequentially in the same chat window."
messages: 16
claude_uuid: "fe0b11d1-1f92-47d9-8927-2c450a222946"
tags: [claude, chat, archive]
---
# Sistema de prompts modular para framework

> **Conversation Overview**

The person, who appears to work in creative strategy and content production (likely at an agency or as a consultant serving clients), asked Claude to help build a Modular Prompt System based on their existing Market Research Framework hosted in Notion. The framework is structured around 8 layers and 23+ steps, focused on writing short-form video hooks using a three-component system (Visual Action + Caption + Voiceover) across funnel levels (TOF, MOF, BOF). The work session involved multiple iterative rounds of building, correcting, and expanding a functional prompt system.

Claude first read the Notion framework, then built an interactive HTML widget app with tabbed navigation across all 8 layers, copy-to-clipboard functionality for each prompt, variable documentation, and execution tips per step. The person then requested the full pipeline printed in order, which Claude delivered. A key correction followed: the person specified that Layer 6 (Execution) needed Evaluation and Iteration steps inserted between each funnel level's generation step, not just at the end — resulting in a 9-step L6 structure (Generate → Evaluate → Iterate for TOF, MOF, and BOF sequentially). The person also requested all content be translated to English throughout. Claude rebuilt the interactive app with these corrections applied, added color-coded step-type badges (Generate, Evaluate, Iterate, etc.), and re-delivered the full corrected pipeline in English. Finally, the person requested a node map visualization of the entire system, first rendered as an SVG inside the widget, then re-requested specifically as a clean HTML version with colored nodes, layer pills, directional arrows, funnel columns for L6, and a legend — which Claude delivered. The session ended with the person requesting the Step 23 Master Table prompt displayed on its own, then asking for it rendered as HTML.

The domain-specific terminology used throughout includes: hook framework, micropersona, scroll-stopping, oddly specific, TOF/MOF/BOF (top/middle/bottom of funnel), visual action, voiceover, caption, motivator, benefit angle, persona pivot, creative pivot, hook type combinations, and master table. The person works with a modular prompt chaining approach where each Claude session loads frameworks first, then runs steps sequentially in the same chat window.

## 🧑 Adriana · 2026-04-06 17:36
ayudame a crear un modular prompt system para este framwork: https://www.notion.so/adrianavmarquez/Market-Research-Framework-3309c084f04180d089a1f1fedc7db5bb?source=copy_link

## 🤖 Claude · 2026-04-06 17:40
Perfecto, leí todo el framework. Es un sistema sólido de 8 capas y 23 pasos. Ahora voy a construirte el Modular Prompt System, que va a permitir activar cada paso de forma independiente o encadenada, sin tener que copiar bloques enormes cada vez.

Ahora construyo el Modular Prompt System como una app interactiva, limpia y editorial, con tus colores de marca.

Aquí tienes el **Modular Prompt System** completo para tu Market Research Framework. Esto es lo que construí:

**8 layers navegables**, cada uno con sus pasos desglosados en 3 pestañas:
- **Prompt** — listo para copiar con un click
- **Variables** — todas las variables en rojo explicadas
- **Tip** — notas de ejecución para no cometer errores comunes

**Lo que resuelve este sistema:**

Antes tenías que ir al Notion, buscar el step correcto, copiar el bloque enorme y acordarte de qué variables llenar. Ahora cada prompt vive de forma independiente, modular y con contexto.

**Cómo usarlo:**

Puedes correr los layers en orden (sesión completa), o saltar directamente al que necesitas. Por ejemplo: si ya tienes el scraping listo, abre Layer 2 y copia Step 4 directo. Si ya tienes la persona y solo necesitas hooks, ve a Layer 6.

**Próximos pasos posibles:**
- Exportarlo como `.md` o página de Notion para que viva junto al framework
- Agregarle un modo de "sesión rápida" que encadena Steps 0 a 4 en un solo bloque
- Crear versiones del system para diferentes clientes con sus variables pre-llenadas

¿Quieres que también lo suba directamente a tu Notion como subpágina del framework?

## 🧑 Adriana · 2026-04-06 19:18
Dame el pipeline completo del Market Research Framework en orden, comenzando por Layer 1 Step 0

## 🤖 Claude · 2026-04-06 19:19
Aquí está el pipeline completo en orden, listo para copiar y pegar en una sola sesión de Claude:

---

## LAYER 1 — SETUP

**STEP 0: AI Initialization**

```
Antes de comenzar, necesito que internalices los frameworks que voy a cargar.

Vas a recibir:
- Hook Database (categorías de visual, caption, voiceover)
- Brand data del cliente
- Cualquier contexto adicional de producto

Define en tu memoria:
1. Las reglas del sistema de 3 componentes (Visual + Caption + Voiceover)
2. Los estándares de calidad que aplican a TODO output
3. Tu rol: eres un creative strategist especializado en short-form conversion content

Cuando hayas procesado todo, confirma:
✓ Frameworks cargados
✓ Sistema de 3 componentes entendido
✓ Estándares de calidad claros
✓ Listo para ejecutar
```

---

**STEP 1: System Initialization**

```
Vamos a correr una sesión de hook writing.

SYSTEM OVERVIEW — 3 componentes obligatorios en cada hook:
1. Visual Action — qué pasa en pantalla en los primeros 1-2 segundos
2. Caption — texto en pantalla que funciona en mute
3. Voiceover — primeras palabras habladas

PRIORITY ORDER:
1. Caption hook (highest priority)
2. Visual action hook (highest priority)
3. Voiceover hook (high priority)

CORE RULES:
- Hooks deben ser oddly specific (números reales, timeframes reales, lenguaje real)
- Caption y voiceover se complementan — NO se repiten entre sí
- Si caption tiene el número → VO expresa emoción o contexto
- Si caption tiene la emoción → VO tiene el número
- Primera palabra del VO es crítica (nunca empezar con filler words)
- Los hooks deben sentirse mid-conversation, no scripted

FRAMEWORK:
- 12 categorías de Visual Action
- 16 categorías de Caption Hook
- 18 categorías de Voiceover Hook

Cada hook generado debe seleccionar intencionalmente de estas categorías.

QUALITY STANDARD:
- Sin lenguaje vago
- Sin frases genéricas
- Debe sonar como una persona real en una situación real
- Debe detener el scroll en los primeros 2 segundos

Confirma antes de continuar:
1. Has procesado todos los archivos del hook framework
2. Entiendes el sistema de 3 componentes
3. Estás listo para aplicarlo estrictamente
```

---

**STEP 2: Strategy Input**

```
Input de estrategia para esta sesión:

Persona: [NOMBRE_MICROPERSONA]
Formato(s): [FORMATO — ej: Street Interview, Talking Head, Podcast]
Awareness level: [TOF / MOF / BOF]
Producto: [NOMBRE_PRODUCTO]
Contexto: [CONTEXTO ADICIONAL RELEVANTE]
```

---

**STEP 3: Controlled Generation**

```
Genera 5 hooks de ejemplo para demostrar tu comprensión del hook framework.

REQUIREMENTS:
- Cada hook debe incluir: visual + caption + voiceover
- Varía los tipos de hook en el set
- Usa diferentes categorías intencionalmente
- Captions bajo 10 palabras
- Mantén especificidad y realismo

IMPORTANTE:
- Estos NO son hooks finales
- NO intentes optimizar para una persona específica
- NO uses claims reales de producto
- Enfócate únicamente en aplicar correctamente:
  → estructura visual + caption + voiceover
  → especificidad
  → no-repetición entre componentes

El objetivo es confirmar que entiendes el sistema antes de pasar a estrategia real.
```

---

## LAYER 2 — RESEARCH

**STEP 4: Data Scraping & Insights**

```
Este dataset representa contenido orgánico real que está deteniendo el scroll de usuarios.

Tu rol es analizar esta data y extraer patrones de comportamiento — no solo resumir contenido.

Extrae lo siguiente:

1. TOP RECURRING PROBLEMS & PAIN POINTS
- ¿Qué frustraciones se expresan repetidamente?
- ¿Qué se siente injusto, confuso o costoso?
- Incluye frases específicas cuando sea posible

2. MOST COMMON DESIRED OUTCOMES
- ¿Qué quiere la gente en cambio?
- ¿Cómo se ve el "éxito" para ellos?

3. VISUAL HOOK PATTERNS (FIRST 1-2 SECONDS)
- ¿Qué pasa en pantalla al inicio de los videos de alto rendimiento?
- ¿Qué setups visuales aparecen repetidamente?

4. LANGUAGE, PHRASES & NUMERIC PATTERNS
- ¿Qué frases exactas y tono aparece repetidamente?
- ¿Qué números, timeframes o stats se usan?
- Prioriza lenguaje real sobre paráfrasis

5. EMOTIONAL DRIVERS
- ¿Qué emociones están más presentes?
- ¿Qué contrastes emocionales (antes vs después, frustración vs alivio) son visibles?

OUTPUT FINAL:
Resumen claro de los patrones que explican POR QUÉ este contenido funciona — no solo QUÉ contiene. Insights específicos, accionables y anclados en señales repetidas del data.
```

---

## LAYER 3 — PSYCHOLOGY

**STEP 5: Micropersona Extraction**

```
Vamos a escribir hooks para [MARCA/PRODUCTO].

MICROPERSONA: [NOMBRE]

Ya tienes acceso a:
- El hook framework (sistema visual + caption + voiceover)
- Los insights de comportamiento extraídos del contenido viral en este nicho

Analiza esta micropersona y extrae:

1. CORE PAIN POINTS
- Pain Point:
- Description:
- Example phrasing (cómo lo dirían):

2. PRIMARY MOTIVATORS
- Motivator:
- Description:
- Why it matters:

3. EMOTIONAL TRIGGERS
Solo nombra los más relevantes (no los definas):
Anger / Outrage / Financial stress / Desperation / Shock / Disbelief / Frustration / Betrayal / Distrust / Fear / Anxiety / Regret / Embarrassment / Validation / Relief / Curiosity / Comparison / Envy / Urgency / Control / Confusion / Vindication

4. LANGUAGE
- Palabras que usa (NO términos de industria)
- Palabras que CONFÍA
- Palabras que RECHAZA

5. REAL PHRASES
- Phrase:
- Context:
- Why it resonates:

6. CORE DECISION DRIVER
- Fear: ¿Qué les preocupa que pase?
- Frustration: ¿De qué están cansados?
- Desire: ¿Qué quieren realmente?

7. HOOK DIRECTION
- Top emotional angles para liderar
- Top 3 hook types que van a funcionar mejor
- Mejor tono
- Qué evitar

Profundidad sobre brevedad. Escribe como si describieras a una persona real, no un segmento de audiencia.
```

---

**STEP 6: Core Motivator Extraction**

```
Basado en todo lo que analizaste sobre esta micropersona, identifica el motivador único y más fuerte que está manejando su comportamiento.

IMPORTANTE:
- Elige ÚNICAMENTE UN motivador
- Emocionalmente anclado, no genérico
- Que refleje cómo esta persona REALMENTE se siente
- Que suene como un pensamiento interno real

Evita: frases genéricas, múltiples ideas, lenguaje de marketing

FORMAT:
Motivador: [Una sola frase]
```

---

## LAYER 4 — PRODUCT

**STEP 7: Product Context**

```
Voy a subir información de producto para [MARCA].

Desde esta información, identifica:

1. CORE MECHANISM
- Cómo funciona realmente (en términos simples)

2. REAL DIFFERENTIATORS
- Qué hace diferente a este producto de las alternativas

3. STRONGEST PROOF POINTS
- Números específicos, resultados, comparaciones

4. LOW-FRICTION ELEMENTS
- Qué lo hace fácil, rápido o accesible

5. POTENTIAL OBJECTIONS
- Qué podría hacer que alguien dude o no confíe

NO conviertas esto en lenguaje de marketing. Extrae lo que realmente importa para la persuasión.
```

---

## LAYER 5 — STRATEGY

**STEP 8 ó 9: Hook Type Selection**

*Si es un solo formato, usa esto:*

```
Quiero escribir hooks para esta persona y benefit angle.

FORMATO: [FORMATO]
AWARENESS LEVEL: [TOF / MOF / BOF]

Usando el hook database, determina qué tipos de hook son más fuertes para este setup.

Identifica:

1. VISUAL HOOK CATEGORIES (TOP 2-4)
- Visual Category + por qué funciona para este formato

2. CAPTION HOOK TYPES (TOP 2-4)
- Caption Type + por qué funciona en este awareness level

3. VOICEOVER HOOK TYPES (TOP 3-5)
- VO Type + por qué encaja con esta persona y setup

4. STRATEGIC ALIGNMENT
- Cómo deben trabajar juntos los 3 componentes
- Qué hace cada componente de forma diferente
- Qué debe pasar en los primeros 2 segundos

Sé selectivo. Prioriza ejecución sobre teoría.
```

*Si son múltiples formatos, agrega la lista y solicita el breakdown por formato con combinaciones (Visual + Caption + VO + por qué funciona).*

---

## LAYER 6 — EXECUTION

**STEP 10: Hook Generation — TOF**

```
Escribe hooks para esta micropersona.

MICROPERSONA: [NOMBRE]
FORMATOS: [FORMATO 1] / [FORMATO 2] / [FORMATO 3]
AWARENESS LEVEL: TOF / problem unaware
TOTAL: 2 hooks por formato

Cada hook incluye:
- Visual action (primeros 1-2 segundos)
- Voiceover (primeras palabras habladas)
- Caption (texto en pantalla, funciona en mute)

STRICT RULES:
- Oddly specific (números, timeframes, situaciones reales)
- Lenguaje real del dataset — NO lo limpies
- Caption bajo 10 palabras, idealmente bajo 7
- VO NO repite el caption
- Empieza el VO mid-thought (no "Hey", "So", "Hoy")
- Varía los hook types — sin estructuras repetidas
- TOF: persona + emoción + lenguaje de mercado primero, producto ligeramente

FORMAT:
[FORMATO]
Hook 1: Visual / Voiceover / Caption
Hook 2: Visual / Voiceover / Caption

Sin comentarios. Sin explicaciones. Solo los hooks.
```

---

**STEP 11: Evaluation**

```
Evalúa cada hook:
- ¿Específico o genérico?
- ¿Detiene el scroll visualmente?
- ¿Caption y VO se complementan?
- ¿Match claro con la persona?

Puntúa cada hook del 1 al 10.
```

---

**STEP 12: Iteration**

```
Reescribe los 2 hooks más débiles. Mejora especificidad, claridad y scroll-stopping power. Muestra original y versión mejorada lado a lado.
```

---

**Repite Steps 10-12 para MOF y BOF**, ajustando el objetivo:
- **MOF:** persona + mecanismo de producto + comparación + prueba
- **BOF:** persona + prueba de producto + reducción de fricción + acción

---

## LAYER 7 — EXPANSION

**STEP 19: Creative Pivots — TOF**

```
Exploramos variación de dos formas con la misma micropersona [NOMBRE]:

FIRST PIVOT — MISMO MOTIVADOR, 3 BENEFIT ANGLES DIFERENTES
1 hook por angle, formato más apropiado para cada uno.

SECOND PIVOT — 3 MOTIVADORES DIFERENTES
Misma persona, motivadores nuevos (no reutilizar el original).
1 hook por motivador, formato más apropiado.

Todos los hooks: Visual + Voiceover + Caption.
Reglas: oddly specific, lenguaje real, caption bajo 10 palabras, VO no repite caption.
Sin comentarios. Solo output.
```

---

**STEP 20: Persona Pivot**

```
Cambiamos a nueva micropersona: [NOMBRE_NUEVA_PERSONA]

FORMATOS: [FORMATO 1] / [FORMATO 2] / [FORMATO 3]
AWARENESS LEVEL: [TOF / MOF / BOF]
TOTAL: 2 hooks por formato

La psicología, urgencia, lenguaje y tensión emocional deben cambiar claramente respecto a la persona anterior. Este es un persona pivot, no solo un cambio de palabras.

Mismas reglas de ejecución. Sin comentarios. Solo los hooks.
```

---

## LAYER 8 — STRUCTURE

**STEP 23: Master Table**

```
Compila todo lo generado en esta sesión en una sola master table.

COLUMNAS:
Persona | Awareness Level | Motivador | Beneficio | Formato | Visual Action | Voiceover | Caption

INSTRUCCIONES:
- Cada hook = una fila
- No omitas nada
- No resumas ni mezcles hooks
- No reescribas el lenguaje — mantén los hooks exactamente como fueron escritos

ORDEN:
1. [Persona 1] — TOF (todos los formatos)
2. [Persona 1] — BOF (todos los formatos)
3. [Persona 1] — pivots
4. [Persona 2] — TOF (todos los formatos)

Solo la tabla. Sin comentarios.
```

---

Este es el pipeline completo, de Step 0 a Step 23. Cada bloque está pensado para pegarse secuencialmente en el mismo chat. ¿Quieres que lo suba a Notion como subpágina del framework original?

## 🧑 Adriana · 2026-04-06 19:20
En el Layer 6, 
tienes qeu agregar Evaluation and Iteration in between hook generations for TOF, MOF y BOF

## 🤖 Claude · 2026-04-06 19:21
Hecho. Aquí está el **Layer 6 corregido** con Evaluation e Iteration entre cada generación de funnel:

---

## LAYER 6 — EXECUTION

**STEP 10: Hook Generation — TOF**

```
Escribe hooks para esta micropersona.

MICROPERSONA: [NOMBRE]
FORMATOS: [FORMATO 1] / [FORMATO 2] / [FORMATO 3]
AWARENESS LEVEL: TOF / problem unaware
TOTAL: 2 hooks por formato

Cada hook incluye:
- Visual action (primeros 1-2 segundos)
- Voiceover (primeras palabras habladas)
- Caption (texto en pantalla, funciona en mute)

STRICT RULES:
- Oddly specific (números, timeframes, situaciones reales)
- Lenguaje real del dataset — NO lo limpies
- Caption bajo 10 palabras, idealmente bajo 7
- VO NO repite el caption
- Empieza el VO mid-thought (no "Hey", "So", "Hoy")
- Varía los hook types — sin estructuras repetidas
- TOF: persona + emoción + lenguaje de mercado primero, producto ligeramente

FORMAT:
[FORMATO]
Hook 1: Visual / Voiceover / Caption
Hook 2: Visual / Voiceover / Caption

Sin comentarios. Sin explicaciones. Solo los hooks.
```

---

**STEP 11: Evaluation — TOF**

```
Evalúa cada hook de TOF generado.

Para cada hook:
- ¿Específico o genérico?
- ¿Detiene el scroll visualmente?
- ¿Caption y VO se complementan (no se repiten)?
- ¿Match claro con la persona?

Puntúa cada hook del 1 al 10.

Formato:
Hook [N] — [FORMATO]:
- Puntuación: X/10
- Específico vs genérico: [evaluación]
- Scroll-stopping visual: [sí/no + razón]
- Complemento caption-VO: [evaluación]
- Match con persona: [evaluación]
- Nota general: [una línea]
```

---

**STEP 12: Iteration — TOF**

```
Reescribe los 2 hooks más débiles de TOF.

Para cada uno, mejora:
- Especificidad
- Claridad del componente más débil
- Scroll-stopping power en los primeros 2 segundos

Muestra original y versión mejorada lado a lado.

ORIGINAL:
- Visual:
- Voiceover:
- Caption:

MEJORADO:
- Visual:
- Voiceover:
- Caption:
- Qué cambió y por qué:
```

---

**STEP 13: Hook Generation — MOF**

```
Ahora escribe hooks para esta micropersona.

MICROPERSONA: [NOMBRE]
FORMATOS: [FORMATO 1] / [FORMATO 2] / [FORMATO 3]
AWARENESS LEVEL: MOF / exploration & evaluation
TOTAL: 2 hooks por formato

Cada hook incluye:
- Visual action (primeros 1-2 segundos)
- Voiceover (primeras palabras habladas)
- Caption (texto en pantalla, funciona en mute)

MOF OBJECTIVE:
Ayudar al viewer a entender cómo funciona, evaluar si vale la pena, compararlo con su situación actual, y construir confianza a través de claridad y prueba.

STRICT RULES:
- Cada hook incluye un elemento concreto del producto (mecanismo, comparación o prueba)
- Prioriza claridad sobre curiosidad (sin hooks vagos o de "misterio")
- Lenguaje real del dataset — NO lo limpies
- Caption señala valor o evaluación (comparación, resultado o proceso)
- VO explica, compara o valida — NO repite el caption
> *[line redacted — references an out-of-scope venture]*
- Enfócate en: escenarios reales, números específicos, diferencias lado a lado, qué cambia realmente
- Varía hook types — sin estructuras repetidas
- MOF: persona + mecanismo de producto + comparación + prueba

FORMAT:
[FORMATO]
Hook 1: Visual / Voiceover / Caption
Hook 2: Visual / Voiceover / Caption

Sin comentarios. Sin explicaciones. Solo los hooks.
```

---

**STEP 14: Evaluation — MOF**

```
Evalúa cada hook de MOF generado.

Para cada hook:
- ¿Específico o genérico?
- ¿Detiene el scroll visualmente?
- ¿Caption y VO se complementan (no se repiten)?
- ¿El hook comunica valor o prueba claramente?
- ¿Match claro con la persona en etapa de evaluación?

Puntúa cada hook del 1 al 10.

Formato:
Hook [N] — [FORMATO]:
- Puntuación: X/10
- Específico vs genérico: [evaluación]
- Scroll-stopping visual: [sí/no + razón]
- Complemento caption-VO: [evaluación]
- Claridad de valor/prueba: [evaluación]
- Match con persona: [evaluación]
- Nota general: [una línea]
```

---

**STEP 15: Iteration — MOF**

```
Reescribe los 2 hooks más débiles de MOF.

Para cada uno, mejora:
- Especificidad
- Claridad del componente más débil
- Fuerza del elemento de prueba o comparación

Muestra original y versión mejorada lado a lado.

ORIGINAL:
- Visual:
- Voiceover:
- Caption:

MEJORADO:
- Visual:
- Voiceover:
- Caption:
- Qué cambió y por qué:
```

---

**STEP 16: Hook Generation — BOF**

```
Ahora escribe hooks para esta micropersona.

MICROPERSONA: [NOMBRE]
FORMATOS: [FORMATO 1] / [FORMATO 2] / [FORMATO 3]
AWARENESS LEVEL: BOF / decision-ready
TOTAL: 2 hooks por formato

Cada hook incluye:
- Visual action (primeros 1-2 segundos)
- Voiceover (primeras palabras habladas)
- Caption (texto en pantalla, funciona en mute)

BOF PRIORITY:
Reforzar la creencia (esto funciona), reducir la fricción (esto es fácil), proveer prueba (números reales, resultados reales), empujar a la acción (por qué ahora).

STRICT RULES:
- Cada hook incluye prueba (números específicos, ahorros reales, escenarios reales)
- Prioriza claridad sobre curiosidad (sin hooks vagos o abstractos)
- Lenguaje real del dataset — NO lo limpies
- Caption comunica valor inmediatamente (resultado, prueba o acción)
- VO agrega contexto o credibilidad — NO repite el caption
- Sin hooks de "misterio" (el viewer ya sabe cuál es el problema)
- Enfócate en: resultados, velocidad, facilidad, outcomes reales
- Varía hook types — sin estructuras repetidas
- BOF: persona + prueba de producto + reducción de fricción + acción

FORMAT:
[FORMATO]
Hook 1: Visual / Voiceover / Caption
Hook 2: Visual / Voiceover / Caption

Sin comentarios. Sin explicaciones. Solo los hooks.
```

---

**STEP 17: Evaluation — BOF**

```
Evalúa cada hook de BOF generado.

Para cada hook:
- ¿Específico o genérico?
- ¿Detiene el scroll visualmente?
- ¿Caption y VO se complementan (no se repiten)?
- ¿El hook incluye prueba o resultado concreto?
- ¿Reduce fricción o empuja a acción claramente?
- ¿Match claro con la persona en etapa de decisión?

Puntúa cada hook del 1 al 10.

Formato:
Hook [N] — [FORMATO]:
- Puntuación: X/10
- Específico vs genérico: [evaluación]
- Scroll-stopping visual: [sí/no + razón]
- Complemento caption-VO: [evaluación]
- Prueba/resultado concreto: [sí/no + evaluación]
- Reducción de fricción / llamada a acción: [evaluación]
- Match con persona: [evaluación]
- Nota general: [una línea]
```

---

**STEP 18: Iteration — BOF**

```
Reescribe los 2 hooks más débiles de BOF.

Para cada uno, mejora:
- Especificidad
- Fuerza de la prueba o el resultado
- Claridad de la llamada a acción o reducción de fricción

Muestra original y versión mejorada lado a lado.

ORIGINAL:
- Visual:
- Voiceover:
- Caption:

MEJORADO:
- Visual:
- Voiceover:
- Caption:
- Qué cambió y por qué:
```

---

El Layer 6 ahora tiene 9 steps en total: generación, evaluación e iteración para cada nivel de funnel, en orden. ¿Quieres que actualice también el widget interactivo y lo suba a Notion como subpágina del framework?

## 🧑 Adriana · 2026-04-06 19:22
agregalo a mi app interactiva, pero todo debe ser en ingles, y luego me das el el pipeline completo del Market Research Framework en orden, comenzando por Layer 1 Step 0 corregido y en ingles

## 🤖 Claude · 2026-04-06 19:34
Doing both at the same time — updating the app and creating the Notion page in parallel.

Now the Notion page — uploading the full corrected pipeline in English:

The Notion upload hit a permissions error — it needs access approval on your end. You can connect it from the connectors menu and I'll retry.

Here's the full corrected pipeline in English in the meantime:

---

## LAYER 1 — SETUP

**STEP 0: AI Initialization**
```
Before we begin, I need you to fully internalize the frameworks I'm about to upload.

You will receive:
- Hook Database (visual, caption, voiceover categories)
- Client brand data
- Any additional product context

Lock in:
1. The rules of the 3-component system (Visual + Caption + Voiceover)
2. The quality standards that apply to ALL output
3. Your role: you are a performance-driven creative strategist specialized in short-form conversion content

When you've processed everything, confirm:
✓ Frameworks loaded
✓ 3-component system understood
✓ Quality standards clear
✓ Ready to execute
```

---

**STEP 1: System Initialization**
```
We are about to run a live hook writing session.

SYSTEM OVERVIEW — 3 mandatory components in every hook:
1. Visual Action — what happens on screen in the first 1–2 seconds
2. Caption — on-screen text that works on mute
3. Voiceover — first spoken words

PRIORITY ORDER:
1. Caption hook (highest priority)
2. Visual action hook (highest priority)
3. Voiceover hook (high priority)

CORE RULES:
- Hooks must be oddly specific (real numbers, real timeframes, real language)
- Caption and voiceover complement each other — they do NOT repeat
- If caption contains the number → VO expresses emotion or context
- If caption contains emotion → VO contains the number
- First word of VO is critical (never start with filler words)
- Hooks must feel mid-conversation, not scripted

FRAMEWORK STRUCTURE:
- 12 Visual Action categories
- 16 Caption Hook categories
- 18 Voiceover Hook categories

Every hook generated must intentionally select from these categories.

QUALITY STANDARD:
- No vague language
- No generic phrasing
- Must sound like a real person in a real situation
- Must stop the scroll within the first 2 seconds

Confirm before proceeding:
1. You have processed all uploaded hook framework files
2. You understand the 3-component hook system
3. You are ready to apply it strictly in all outputs
```

---

**STEP 2: Strategy Input**
```
Strategy input for this session:

Persona: [PERSONA_NAME]
Format(s): [FORMAT — e.g. Street Interview, Talking Head, Podcast]
Awareness level: [TOF / MOF / BOF]
Product: [PRODUCT_NAME]
Context: [ANY ADDITIONAL RELEVANT CONTEXT]
```

---

**STEP 3: Controlled Generation**
```
Generate 5 example hooks to demonstrate your understanding of the hook framework.

Requirements:
- Each hook must include: visual + caption + voiceover
- Vary hook types across the set
- Use different categories intentionally
- Keep captions under 10 words
- Maintain specificity and realism

IMPORTANT:
- These are NOT final hooks
- Do NOT optimize for a specific persona
- Do NOT use real product claims
- Focus only on correctly applying:
  → visual + caption + voiceover structure
  → specificity
  → non-repetition between components

The goal is to confirm you understand the system before we move into real strategy.
```

---

## LAYER 2 — RESEARCH

**STEP 4: Data Scraping & Insights**
```
This dataset represents real, organic content that is successfully stopping users mid-scroll.

Your role is to analyze this data and extract behavioral patterns — not just summarize content.

Extract the following:

1. TOP RECURRING PROBLEMS & PAIN POINTS
- What frustrations are repeatedly expressed?
- What feels unfair, confusing, or costly?
- Include specific phrasing examples when possible

2. MOST COMMON DESIRED OUTCOMES
- What do people want instead?
- What does "success" look like for them?

3. VISUAL HOOK PATTERNS (FIRST 1–2 SECONDS)
- What is happening on screen at the start of high-performing videos?
- What visual setups appear repeatedly?

4. LANGUAGE, PHRASES & NUMERIC PATTERNS
- What exact phrases, wording, or tone keeps appearing?
- What numbers, timeframes, or stats are commonly used?
- Prioritize real language over paraphrasing

5. EMOTIONAL DRIVERS
- What emotions are most present?
- What emotional contrasts (before vs after, frustration vs relief) are visible?

FINAL OUTPUT:
A clear, structured summary of patterns explaining WHY this content performs — not just WHAT it contains. Specific, actionable, grounded in repeated signals from the data.
```

---

## LAYER 3 — PSYCHOLOGY

**STEP 5: Micropersona Extraction**
```
We are about to write hooks for [BRAND / PRODUCT].

MICROPERSONA: [NAME]

Analyze this micropersona and extract:

1. CORE PAIN POINTS
- Pain Point:
- Description:
- Example phrasing (how they would say it):

2. PRIMARY MOTIVATORS
- Motivator:
- Description:
- Why it matters:

3. EMOTIONAL TRIGGERS
Only name the most relevant ones (do NOT define them):
Anger / Outrage / Financial stress / Desperation / Shock / Disbelief / Frustration / Betrayal / Distrust / Fear / Anxiety / Regret / Embarrassment / Validation / Relief / Curiosity / Comparison / Envy / Urgency / Control / Confusion / Vindication

4. LANGUAGE
- Words this persona uses (NOT industry terms)
- Words this persona TRUSTS
- Words this persona REJECTS

5. REAL PHRASES
- Phrase / Context / Why it resonates

6. CORE DECISION DRIVER
- Fear: What are they worried will happen?
- Frustration: What are they tired of dealing with?
- Desire: What do they actually want instead?

7. HOOK DIRECTION
- Top emotional angles to lead with
- Top 3 hook types that will perform best
- Best tone / What to avoid

Depth over brevity. Write like you are describing a real person, not summarizing an audience segment.
```

---

**STEP 6: Core Motivator Extraction**
```
Based on everything you just analyzed about this micropersona, identify the single strongest motivator driving their behavior.

IMPORTANT:
- ONLY ONE motivator
- Emotionally grounded, not generic
- Feels like a real internal thought or belief
- Avoid generic phrases, multiple ideas, marketing language

FORMAT:
Motivator: [One sentence only]
```

---

## LAYER 4 — PRODUCT

**STEP 7: Product Context**
```
I'm uploading product information for [BRAND].

Identify:

1. CORE MECHANISM — How this actually works (in simple terms)
2. REAL DIFFERENTIATORS — What makes this different from alternatives
3. STRONGEST PROOF POINTS — Specific numbers, results, comparisons
4. LOW-FRICTION ELEMENTS — What makes this easy, fast, or accessible
5. POTENTIAL OBJECTIONS — What might make someone hesitate or doubt

Do NOT turn this into marketing language. Extract what actually matters for persuasion.
```

---

## LAYER 5 — STRATEGY

**STEP 8 or 9: Hook Type Selection**

*Single format:*
```
FORMAT: [FORMAT]
AWARENESS LEVEL: [TOF / MOF / BOF]

Using the hook database, identify:

1. VISUAL HOOK CATEGORIES (TOP 2–4)
- Category + why it works for this format

2. CAPTION HOOK TYPES (TOP 2–4)
- Type + why it works at this awareness level

3. VOICEOVER HOOK TYPES (TOP 3–5)
- Type + why it fits this persona and setup

4. STRATEGIC ALIGNMENT
- How all 3 components should work together
- What each does differently (no repetition)
- What stops the scroll in the first 2 seconds

Be selective. Prioritize execution over theory.
```

*Multiple formats: request a breakdown per format with TOP combinations (Visual + Caption + VO + why it works).*

---

## LAYER 6 — EXECUTION

**STEP 10: Hook Generation — TOF**
```
Now write hooks for this micropersona.

MICROPERSONA: [NAME]
FORMATS: [FORMAT 1] / [FORMAT 2] / [FORMAT 3]
AWARENESS LEVEL: TOF / problem unaware
TOTAL: 2 hooks per format ([X] hooks total)

Each hook: Visual action / Voiceover / Caption

STRICT RULES:
- Oddly specific (real numbers, real timeframes, real situations)
- Real language from the dataset — do NOT clean it up
- Caption under 10 words, ideally under 7
- VO does NOT repeat the caption
- Start VO mid-thought (avoid "Hey", "So", "Today")
- Vary hook types — no repeated structures
- TOF: persona + emotion + market language first, product lightly

No commentary. No explanations. Only the hooks.
```

---

**STEP 11: Evaluation — TOF**
```
Evaluate each TOF hook generated.

For each hook:
- Specific or generic?
- Stops the scroll visually?
- Caption and VO complement (not repeat)?
- Matches the persona clearly?

Score each hook 1–10.

Hook [N] — [FORMAT]:
- Score: X/10
- Specific vs generic: [assessment]
- Scroll-stopping visual: [yes/no + reason]
- Caption-VO complement: [assessment]
- Persona match: [assessment]
- Overall note: [one line]
```

---

**STEP 12: Iteration — TOF**
```
Rewrite the 2 weakest TOF hooks.

Improve: specificity / clarity of the weakest component / scroll-stopping power in the first 2 seconds.

Show original and improved side by side.

ORIGINAL: Visual / Voiceover / Caption
IMPROVED: Visual / Voiceover / Caption / What changed and why
```

---

**STEP 13: Hook Generation — MOF**
```
Now write hooks for this micropersona.

MICROPERSONA: [NAME]
FORMATS: [FORMAT 1] / [FORMAT 2] / [FORMAT 3]
AWARENESS LEVEL: MOF / exploration & evaluation
TOTAL: 2 hooks per format ([X] hooks total)

MOF OBJECTIVE: Help the viewer understand how this works, evaluate if it's worth it, compare it to their current situation, build trust through clarity and proof.

STRICT RULES:
- Every hook includes a concrete product element (mechanism, comparison, or proof)
- Clarity over curiosity (no mystery hooks)
- Real language from the dataset — do NOT clean it
- Caption signals value or evaluation
- VO explains, compares, or validates — NOT repeats caption
- Avoid: exaggerated claims, "secret"/"hack" framing, generic benefits
- MOF: persona + product mechanism + comparison + proof

No commentary. No explanations. Only the hooks.
```

---

**STEP 14: Evaluation — MOF**
```
Evaluate each MOF hook generated.

For each hook:
- Specific or generic?
- Stops the scroll visually?
- Caption and VO complement (not repeat)?
- Communicates value or proof clearly?
- Matches the persona in evaluation mode?

Score each hook 1–10.

Hook [N] — [FORMAT]:
- Score: X/10
- Specific vs generic: [assessment]
- Scroll-stopping visual: [yes/no + reason]
- Caption-VO complement: [assessment]
- Value/proof clarity: [assessment]
- Persona match: [assessment]
- Overall note: [one line]
```

---

**STEP 15: Iteration — MOF**
```
Rewrite the 2 weakest MOF hooks.

Improve: specificity / clarity of the weakest component / strength of the proof or comparison element.

Show original and improved side by side.

ORIGINAL: Visual / Voiceover / Caption
IMPROVED: Visual / Voiceover / Caption / What changed and why
```

---

**STEP 16: Hook Generation — BOF**
```
Now write hooks for the following micropersona.

MICROPERSONA: [NAME]
FORMATS: [FORMAT 1] / [FORMAT 2] / [FORMAT 3]
AWARENESS LEVEL: BOF / decision-ready
TOTAL: 2 hooks per format ([X] hooks total)

BOF PRIORITY: Reinforce belief / Reduce friction / Provide proof / Push action.

STRICT RULES:
- Every hook includes proof (specific numbers, real savings, real scenarios)
- Clarity over curiosity (no vague or abstract hooks)
- Real language from the dataset — do NOT clean it
- Caption communicates value immediately (result, proof, or action)
- VO adds context or credibility — NOT repeats caption
- No mystery hooks (the viewer already knows the problem)
- BOF: persona + product proof + friction reduction + action

No commentary. No explanations. Only the hooks.
```

---

**STEP 17: Evaluation — BOF**
```
Evaluate each BOF hook generated.

For each hook:
- Specific or generic?
- Stops the scroll visually?
- Caption and VO complement (not repeat)?
- Includes concrete proof or a real result?
- Reduces friction or pushes to action clearly?
- Matches the persona in decision mode?

Score each hook 1–10.

Hook [N] — [FORMAT]:
- Score: X/10
- Specific vs generic: [assessment]
- Scroll-stopping visual: [yes/no + reason]
- Caption-VO complement: [assessment]
- Proof / concrete result: [yes/no + assessment]
- Friction reduction / call to action: [assessment]
- Persona match: [assessment]
- Overall note: [one line]
```

---

**STEP 18: Iteration — BOF**
```
Rewrite the 2 weakest BOF hooks.

Improve: specificity / strength of the proof or real outcome / clarity of the call to action or friction reduction.

Show original and improved side by side.

ORIGINAL: Visual / Voiceover / Caption
IMPROVED: Visual / Voiceover / Caption / What changed and why
```

---

## LAYER 7 — EXPANSION

**STEP 19: Creative Pivots — TOF**
```
Back to TOF. Same micropersona: [NAME]
FORMATS: [FORMAT 1] / [FORMAT 2] / [FORMAT 3]

FIRST PIVOT — SAME MOTIVATOR, 3 DIFFERENT BENEFIT ANGLES
1 hook per angle. Most appropriate format for each.

SECOND PIVOT — 3 DIFFERENT MOTIVATORS
Same persona, new motivators (do NOT reuse the original).
1 hook per motivator. Most appropriate format.

Every hook: Visual + Voiceover + Caption.
Oddly specific. Real language. Caption under 10 words. VO does not repeat caption. Vary hook types.

No commentary. Only output.
```

---

**STEP 20: Persona Pivot**
```
Final Pivot — New Persona: [NEW_PERSONA_NAME]
FORMATS: [FORMAT 1] / [FORMAT 2] / [FORMAT 3]
AWARENESS LEVEL: [TOF / MOF / BOF]
TOTAL: 2 hooks per format ([X] hooks total)

This is a persona pivot, not just a wording change. The psychology, urgency, language, and emotional tension must clearly shift from the previous persona.

STRICT RULES:
- Specific to THIS persona's situation, language, and emotional reality
- Do NOT reuse the previous persona's framing, phrasing, or tensions
- Reflect THIS persona's specific emotional triggers
- Oddly specific. Caption under 10 words. VO does not repeat caption. Vary hook types.

No commentary. Only the hooks.
```

---

## LAYER 8 — STRUCTURE

**STEP 23: Master Table**
```
Compile everything generated in this session into a single master table.

COLUMNS:
Persona | Awareness Level | Motivator | Benefit | Format | Visual Action | Voiceover | Caption

INSTRUCTIONS:
- Every hook = its own row
- Nothing left out
- No summarizing or merging
- No rewriting — keep language exactly as written

ORDER:
1. [Persona 1] — TOF hooks (all formats)
2. [Persona 1] — BOF hooks (all formats)
3. [Persona 1] — pivot hooks
4. [Persona 2] — TOF hooks (all formats)

Only the table. No commentary.
```

---

The app is updated with all 9 Layer 6 steps (Generate + Evaluate + Iterate for TOF, MOF, and BOF), everything in English, with color-coded badges for each step type. For the Notion upload, reconnect the integration from your connectors and I can push it straight into the framework page.

## 🧑 Adriana · 2026-04-06 19:46
generate an image of how the modular prompt system would look with nodes

## 🤖 Claude · 2026-04-06 19:47
Every node is clickable — tap any step and it'll pull up that prompt directly in chat.

A few things worth noticing in the map: the dashed spine down the center is the main flow axis. L6 is intentionally the heaviest section, with the three Generate → Evaluate → Iterate loops stacked vertically for TOF, MOF, and BOF. The dashed feedback arrows looping back from Iterate to Generate show that iteration can cycle before you advance to the next funnel level. L5 is the only branching point — S8 or S9 depending on whether you have one format or multiple.

## 🧑 Adriana · 2026-04-06 21:05
Show me Step 23: Master Table prompt

## 🤖 Claude · 2026-04-06 21:05
Here's **Step 23: Master Table** — the final prompt of the full pipeline:

---

**STEP 23: Master Table**

```
We've now written hooks across multiple personas, awareness levels, motivators, benefits, and formats.

Your task is to compile everything generated in this session into a single master table.

TABLE COLUMNS:
Persona | Awareness Level | Motivator | Benefit | Format | Visual Action | Voiceover | Caption

INSTRUCTIONS:
- Every hook written in this session must appear as its own row
- Do NOT leave anything out
- Do NOT summarize or merge hooks
- Do NOT rewrite or clean the language
- Keep all hooks exactly as originally written

ORGANIZE THE TABLE IN THIS ORDER:
1. [Persona 1] — TOF hooks (all formats)
2. [Persona 1] — BOF hooks (all formats)
3. [Persona 1] — Motivator / Benefit pivot hooks
4. [Persona 2] — TOF hooks (all formats)

FORMAT REQUIREMENTS:
- Output as a clean, structured table
- Each hook = one row
- Maintain consistent formatting across all rows
- Keep wording raw and unchanged

IMPORTANT:
- Do NOT add commentary
- Do NOT explain anything
- Do NOT modify the hooks
- Only output the table

OUTPUT:
A complete master table containing all hooks generated in this session, properly categorized and ordered.
```

---

This is the closing node of the entire pipeline — it compiles every single hook from the session into one structured table, organized by persona and funnel level, ready to hand off to a client or production team. Copy it at the very end of your session and paste it into the same chat where all the hooks were generated.

## 🧑 Adriana · 2026-04-06 21:06
make it a html

## 🤖 Claude · 2026-04-06 21:07

## 🧑 Adriana · 2026-04-06 21:08
no, just make the generated image of how the modular prompt system would look with nodes as an html

## 🤖 Claude · 2026-04-06 21:09
Clean node map in HTML. Each layer is color-coded to match the app, the three funnel columns in L6 show the Generate → Evaluate → Iterate loop clearly, and the branching at L5 (S8 or S9) reads as a decision point. The legend ties the color logic together at the bottom.
