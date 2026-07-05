---
title: "Skill para extraer messaging desde social listening"
source: claude.ai-chat
created: "2026-05-07 05:48"
summary: "**Conversation Overview**  The person is building a comprehensive brand intelligence system for marketing and creative strategy work. They operate with a 'Brand Brain' database in Notion as the central hub for brand information, and are developing a series of interconnected skills and automated workflows using Apify (for scraping), n8n (for automation), and Airtable (as a staging layer for raw scraped data). The conversation focused on designing a skill specifically for a 'Messaging and Angles' session — one component within a larger multi-stage system where scraping and Notion population happen across several distinct workflows.  The person and Claude collaboratively designed the full architecture for a skill called `language-bank-pipeline`, working through multiple iterations as the person provided increasingly detailed information about their actual Airtable schemas. A critical design insight emerged when the person shared their real schema data: Instagram Raw turned out to capture actual user comments via Meta API (making it a legitimate Voice of Customer source), not just brand captions as initially assumed. Facebook Raw captures page posts with seven granular emotional reaction types (Angry, Care, Haha, Like, Love, Sad, Wow), enabling sentiment signal extraction. The conversation established a foundational architectural distinction between Voice of Customer sources (Reddit, Twitter, Instagram comments, Reviews) and Category Context sources (Facebook posts, YouTube metadata, all seven Google tables). Claude designed a Notion Language Bank database schema with 22 properties covering source metadata, creative classification (Language Category as multi-select, Awareness Stage mapped to Schwartz's framework), quality validation (four pressure tests: Specificity, Truth, Volume, Hook), and a performance feedback loop connecting to a Concepts database.  Claude built four skill files: `SKILL.md` (four-stage pipeline: S1 Ingesta → S2 Extracción → S3 Pressure Testing → S4 Notion Write), `schemas.md` (JSON output contracts for each stage), `evals.json` (four test cases covering happy path, schema mismatch detection, connector failure fallback, and pressure test override scenarios), and `references/notion_write_protocol.md` (technical Notion connector integration with exact payload structure and Markdown fallback format). The person also had Claude generate a JSON spec of the Notion database schema to paste directly into Notion AI for automated database creation, which the person confirmed was successfully created with all 22 properties intact. The conversation ended with an important correction: the person clarified that scraping and Notion population happen across multiple other workflow stages, and this skill should be scoped exclusively to the Messaging and Angles session — not positioned as a general language pipeline. Claude acknowledged the over-scoping and asked five clarifying questions to properly rewrite the skill with correct boundaries before proceeding."
messages: 16
claude_uuid: "e2cf42e3-268a-42ee-8cd7-d0087672db12"
tags: [claude, chat, archive]
---
# Skill para extraer messaging desde social listening

> **Conversation Overview**

The person is building a comprehensive brand intelligence system for marketing and creative strategy work. They operate with a "Brand Brain" database in Notion as the central hub for brand information, and are developing a series of interconnected skills and automated workflows using Apify (for scraping), n8n (for automation), and Airtable (as a staging layer for raw scraped data). The conversation focused on designing a skill specifically for a "Messaging and Angles" session — one component within a larger multi-stage system where scraping and Notion population happen across several distinct workflows.

The person and Claude collaboratively designed the full architecture for a skill called `language-bank-pipeline`, working through multiple iterations as the person provided increasingly detailed information about their actual Airtable schemas. A critical design insight emerged when the person shared their real schema data: Instagram Raw turned out to capture actual user comments via Meta API (making it a legitimate Voice of Customer source), not just brand captions as initially assumed. Facebook Raw captures page posts with seven granular emotional reaction types (Angry, Care, Haha, Like, Love, Sad, Wow), enabling sentiment signal extraction. The conversation established a foundational architectural distinction between Voice of Customer sources (Reddit, Twitter, Instagram comments, Reviews) and Category Context sources (Facebook posts, YouTube metadata, all seven Google tables). Claude designed a Notion Language Bank database schema with 22 properties covering source metadata, creative classification (Language Category as multi-select, Awareness Stage mapped to Schwartz's framework), quality validation (four pressure tests: Specificity, Truth, Volume, Hook), and a performance feedback loop connecting to a Concepts database.

Claude built four skill files: `SKILL.md` (four-stage pipeline: S1 Ingesta → S2 Extracción → S3 Pressure Testing → S4 Notion Write), `schemas.md` (JSON output contracts for each stage), `evals.json` (four test cases covering happy path, schema mismatch detection, connector failure fallback, and pressure test override scenarios), and `references/notion_write_protocol.md` (technical Notion connector integration with exact payload structure and Markdown fallback format). The person also had Claude generate a JSON spec of the Notion database schema to paste directly into Notion AI for automated database creation, which the person confirmed was successfully created with all 22 properties intact. The conversation ended with an important correction: the person clarified that scraping and Notion population happen across multiple other workflow stages, and this skill should be scoped exclusively to the Messaging and Angles session — not positioned as a general language pipeline. Claude acknowledged the over-scoping and asked five clarifying questions to properly rewrite the skill with correct boundaries before proceeding.

## 🧑 Adriana · 2026-05-07 05:48
ayudame a crear un skill pensado para este workflow, sabiendo que yo tengo un brand brain database en notion donde se centraliza toda la informacion de la marca, esto es para desarrollar el [💌](https://www.notion.so/adrianavmarquez/Messaging-and-Angles-3399c084f041808d97def2938cf268aa?pvs=24)__[Messaging and Angles](https://www.notion.so/adrianavmarquez/Messaging-and-Angles-3399c084f041808d97def2938cf268aa?pvs=24)__ - Key language about the customer DB:

another idea: i already scrape the reviews for reviews on the reviews intelligence DB, so that is separate this is for:

So i would instead of making an automatic connection to an apify scrapping tool I most likely would have to create a Tiktok Scrapper database inside airtable that connects to apify through n8n, Instagram Scrapper database inside airtable that connects to apify through n8n, and Google Scrapper database inside airtable that connects to apify through n8n, for general brand listening. and from those database upload it into claude and iterate manually until i find the angles from uploading all sources database, and after manually iterating then I connect it to notion DB, so it uploads what i have approved. that said i would need a scrapping-data-angle-messaging-extraction skill, so it understands what i need, why, when, how and what for. and the output from this final approved iteration session needs to be compatible with my notion database so it connects and autopopulates, what do you think?

este era mi draft del skill:

YAML

```
name: scrapping-data-angle-messaging-extraction
description: Flujo de trabajo para extraer angles y messaging desde datos de social listening (Apify/Airtable) iterando manualmente con Claude, y exportando el resultado aprobado al Notion Language Bank DB.
license: Complete terms in LICENSE.txt

```

Scrapping Data & Angle Messaging Extraction
Este skill define el flujo de trabajo para procesar datos crudos de social listening (reviews, comentarios, UGC) y convertirlos en angles y messaging aprobados, listos para ser importados en el Notion Language Bank DB.
Arquitectura del Sistema
El proceso se divide en tres capas para asegurar la calidad de los datos:

1. Recolección (Automatizada): Apify extrae datos de TikTok, Instagram y Google, y los envía vía n8n a tablas específicas en Airtable.
2. Procesamiento (Manual/Iterativo): Sesión de trabajo con Claude donde se suben los datos crudos, se extraen patrones, se hace pressure testing y se aprueban frases específicas.
3. Exportación (Estructurada): Claude genera una tabla Markdown con las frases aprobadas, formateada exactamente para coincidir con las propiedades del Notion Language Bank DB.
Flujo de Trabajo: Iteración con Claude
Cuando el usuario solicite extraer angles o messaging de datos scrapeados, sigue este proceso:
1. Solicitar los Datos Crudos
Pide al usuario que proporcione los datos exportados de sus bases de datos de Airtable (TikTok Scraper, Instagram Scraper, Google Scraper). Los datos deben incluir el texto original del comentario/review y la fuente.
2. Análisis y Extracción
Analiza los datos buscando patrones recurrentes. Extrae:

* Core Product Language: Cómo describen el producto.
* Customer Language: Frases verbatim sobre su experiencia.
* Transformation Language: El cambio emocional (antes/después).
* Sensory Language: Descriptores de textura/sensación.
* Emotional Benefit: El sentimiento que da el producto.
* Trust Language: Frases que reducen escepticismo.
* Objections: Dudas o quejas comunes.
* Winning Phrases: Frases potentes que destacan.
3. Pressure Testing y Aprobación
Presenta las frases extraídas al usuario para su revisión.

* Discute por qué ciertas frases son fuertes y otras débiles.
* Refina las frases basándote en el feedback del usuario.
* REGLA CRÍTICA: Debes obtener la aprobación explícita del usuario para cada frase antes de considerarla "final".
4. Exportación al Language Bank DB
Al final de la sesión, cuando el usuario indique que ha terminado o pida exportar, utiliza el prompt de exportación definido en `references/export_prompt.md`.
Recursos

* `references/export_prompt.md`: El prompt exacto que debes usar para generar la tabla Markdown compatible con el Notion Language Bank DB.

## 🤖 Claude · 2026-05-07 05:50
Tu draft tiene la arquitectura correcta — separar recolección automatizada de iteración manual es la decisión clave aquí, y la haces bien. Pero hay seis cosas que lo van a hacer mucho más fuerte si las atacas antes de empezar a escribir el SKILL.md.

**1. Define la relación con el Reviews Intelligence DB.** Tu skill actual no lo menciona, pero es crítico. Reviews y social listening capturan cosas distintas: reviews son post-compra (transformación, satisfacción, objection-resolved), TikTok/IG/Google son pre-compra y peer-to-peer (curiosidad, comparación, objection-raised). Si tratas las dos fuentes igual, vas a duplicar trabajo y perder la señal específica de cada una. El skill debería decir explícitamente: "este flujo extrae lenguaje *de descubrimiento y consideración*, complementario al Reviews Intelligence DB que captura lenguaje *de validación post-compra*."

**2. Adopta el Resource Collection Gate del motion-creative-pipeline.** Ya tienes ese patrón establecido y funciona. Mismo formato CRÍTICO/VALIDADOR/ENRIQUECEDOR, adaptado a este flujo. No reinventes el control de calidad de inputs.

**3. El pressure testing necesita protocolo, no solo "discutir".** Sin reglas, vas a aprobar frases que suenan bien pero son débiles. Te propongo cuatro tests obligatorios por frase:
- *Specificity test*: ¿Cualquier marca de la categoría podría decir esto? Si sí, descarta.
- *Truth test*: ¿Esta frase suena a alguien escribiéndola en su teléfono o suena a copy de marca? Si suena a copy, descarta.
- *Volume test*: ¿Aparece este patrón ≥3 veces o es un outlier brillante? Outliers van a un bucket separado.
- *Hook test*: ¿Funcionaría en los primeros 3 segundos de un ad? Si la respuesta es "tendría que reescribirla", la frase no está lista.

**4. Las 8 categorías están bien pero necesitan mapear a deliverables creativos.** Si no, terminan siendo un ejercicio taxonómico. Cada categoría debería declarar para qué se usa downstream: Sensory Language → script ingredients para UGC, Trust Language → reframes para objection handling en BOF ads, Transformation Language → hooks para MOF, etc. Eso conecta este skill con el motion-creative-pipeline directamente.

**5. Atribución de fuente importa más de lo que parece.** Una frase en comentarios orgánicos de TikTok tiene peso diferente a una en comentarios de un ad pagado de IG. El export debería preservar source + context (organic vs paid, comment vs caption, video del brand vs video del usuario). Si no, todo se aplana y pierdes la señal de calidad.

**6. La estructura debería seguir el patrón motion-creative-pipeline:** SKILL.md + schemas.md + evals.json + references/export_prompt.md. Cada etapa con contrato de entrada, protocolo de razonamiento, SOP, guardrails, y JSON de salida estructurado. Eso te da consistencia con el resto de tu sistema y hace que las sesiones sean reproducibles.

---

Antes de escribir los archivos necesito una cosa que es bloqueante:

**¿Cuál es el schema exacto de tu Notion Language Bank DB?** Específicamente:
- Qué propiedades tiene (nombre exacto + tipo: text, multi-select, relation, select, etc.)
- Cómo están organizadas las categorías de lenguaje (¿una propiedad multi-select? ¿una relation a otra DB?)
- Si tiene relaciones a otras DBs del Brand Brain (ej: relation a un Brand DB, a un Persona DB)
- Si hay propiedades de metadata (source, date_extracted, approval_status, etc.)

Sin eso, el `export_prompt.md` va a ser genérico y vas a tener que reformatear manualmente cada vez. Si me das un screenshot del schema o me describes las propiedades, te dejo el export_prompt.md listo para que la tabla Markdown que genere Claude se pegue directo en Notion vía CSV import o copy/paste y autopopule sin fricción.

¿Me compartes el schema y arrancamos? Mientras tanto puedo ir armando el SKILL.md y el schemas.md con los placeholders correctos para que solo conectemos las propiedades de Notion al final.

## 🧑 Adriana · 2026-05-07 06:04
aun no esta creada, esperaba qu epudiesemos determinar el criterio y lo que es importante basado en nuestra conversacion,  un ejemplo de como lucen las airtable raw database a donde cae la data para que veas sus propiedades podria ayudarte a pensar en ello?

Adjunto links de tablas raw de airtable vacias para tu refrencia:

| Reddit Raw    | [airtable.com/appsJ4KCECe6e07fh/tblXwQC28Uu2Nk9qg](https://airtable.com/appsJ4KCECe6e07fh/tblXwQC28Uu2Nk9qg) |
| Twitter Raw   | [airtable.com/appsJ4KCECe6e07fh/tblWJryWy36dNwnqT](https://airtable.com/appsJ4KCECe6e07fh/tblWJryWy36dNwnqT) |
| Instagram Raw | [airtable.com/appsJ4KCECe6e07fh/tblYTheFc74GHOkIL](https://airtable.com/appsJ4KCECe6e07fh/tblYTheFc74GHOkIL) |
| Facebook Raw  | [airtable.com/appsJ4KCECe6e07fh/tbluqCnI46H40801m](https://airtable.com/appsJ4KCECe6e07fh/tbluqCnI46H40801m) |
| YouTube Raw   | [airtable.com/appsJ4KCECe6e07fh/tblazH7qt21CftLBG](https://airtable.com/appsJ4KCECe6e07fh/tblazH7qt21CftLBG) |

## 🤖 Claude · 2026-05-07 06:05
No puedo abrir los links de Airtable porque están detrás de auth — necesitaría screenshots o que pegues los nombres y tipos de campos de una de las tablas (con que veas una basta, asumo que las 5 tienen estructura similar). Eso me deja terminar el mapping Airtable → Claude → Notion correctamente.

Pero mientras llega eso, puedo proponerte el schema del Notion Language Bank DB basado en lo que ya definimos juntos. Si lo validas o lo ajustas, queda listo para crear y entonces el `export_prompt.md` del skill puede generar tablas Markdown que se peguen directo sin reformatear.

## Notion Language Bank DB — Schema propuesto

**Propiedades core (la frase y su origen):**

| Propiedad | Tipo | Por qué |
|---|---|---|
| Phrase | Title | La cita verbatim. El título es la frase exacta, sin parafraseo |
| Brand | Relation → Brand DB | Si manejas más de una marca, no se mezclan |
| Source Platform | Select | Reddit / Twitter / Instagram / Facebook / YouTube / TikTok / Google / Reviews. La plataforma cambia el peso de la señal |
| Source Context | Select | Organic comment / Brand caption / Paid ad comment / User video caption / Review / Forum thread / DM. Una frase en orgánico ≠ una en comentarios de un ad pagado |
| Source URL | URL | Trazabilidad cuando sea posible |
| Date Extracted | Date | Para detectar shifts de lenguaje en el tiempo |

**Propiedades de clasificación creativa (lo que conecta con motion-creative-pipeline):**

| Propiedad | Tipo | Por qué |
|---|---|---|
| Language Category | Multi-select | Core Product / Customer / Transformation / Sensory / Emotional Benefit / Trust / Objection. Multi-select porque una frase puede ser Sensory + Emotional Benefit a la vez |
| Awareness Stage | Select | Unaware / Problem-aware / Solution-aware / Product-aware / Most-aware. Mapea directo a Schwartz y a TOF/MOF/BOF en briefs |
| Persona | Relation → Persona DB | Conecta el lenguaje a la persona específica que lo usa. Sin esto el bank se aplana |
| Downstream Use | Multi-select | Hook candidate / Body script / Objection handler / Transformation moment / Trust builder / CTA frame. Esto evita que el bank sea taxonómico — cada frase declara para qué sirve |

**Propiedades de calidad (el pressure testing como dato persistente):**

| Propiedad | Tipo | Por qué |
|---|---|---|
| Pressure Tests Passed | Multi-select | Specificity / Truth / Volume / Hook. Marcas las 4 cajas que pasó. Frases con menos de 3 son débiles |
| Volume Signal | Select | Outlier (1-2) / Recurring (3-9) / High frequency (10+). Una frase brillante que aparece una vez es distinta de un patrón |
| Hero Line | Checkbox | Reemplaza "Winning Phrases" como categoría. Es un flag de calidad, no un bucket de contenido |
| Status | Select | Draft / Approved / In use / Retired. Solo Approved entra al pipeline creativo |

**Propiedades opcionales pero útiles:**

| Propiedad | Tipo | Por qué |
|---|---|---|
| Date Approved | Date | Cuándo pasaste el pressure test |
| Used In | Relation → Concepts DB | Trazabilidad cuando una frase se convierte en hook real |
| Performance | Select | If used: Won / Lost / Mixed / Pending. Cierra el loop de qué lenguaje convierte en mercado |
| Notes | Text | Contexto que no cabe en propiedades |

## Decisiones de diseño que vale la pena que confirmes

**1. Una sola DB en lugar de varias por categoría.** Más fácil de filtrar, consultar y feed a briefs. Si separas por plataforma (TikTok DB, IG DB, etc.), terminas con duplicados cuando la misma frase aparece en dos lugares.

**2. "Winning Phrases" se vuelve un flag (Hero Line), no una categoría.** Las 7 categorías restantes son sobre *contenido* del lenguaje. "Winning" es sobre *calidad*. Mezclarlos te confunde queries: "dame todo el Trust Language" vs "dame los Hero Lines" son dos preguntas distintas.

**3. Awareness Stage es el puente al motion-creative-pipeline.** Sin esa propiedad, el Language Bank y el creative pipeline viven separados. Con esa propiedad puedes hacer queries como "dame Trust Language para BOF de Persona X" y eso es input directo para un brief.

**4. Volume Signal y Pressure Tests Passed son propiedades, no comentarios.** Si los dejas como notas en texto libre, los pierdes en queries. Como propiedades estructuradas filtras "frases con 4/4 pressure tests + Volume High frequency" en un click.

**5. Performance loop (opcional pero potente).** Si una vez que usas una frase en un ad puedes marcarla como Won/Lost, el Language Bank se vuelve un sistema vivo: el próximo brief sabe qué lenguaje *convirtió en mercado*, no solo qué *suena bien*. Esto cierra el loop con W7 del motion-creative-pipeline.

## Lo que necesito de los Airtable raw

Cuando me compartas los screenshots o pegues los field names, lo crítico que necesito ver es:

- ¿Tienen ya un campo de "transcript" o "text content" con el verbatim?
- ¿Hay un campo de tipo de contenido (comment vs caption vs post)?
- ¿Hay timestamp o date scraped?
- ¿Hay author o username?
- ¿Hay engagement metrics (likes, replies)? Si sí, eso ayuda al Volume Signal automático.
- ¿Hay un campo libre de keywords o tags donde Apify tira metadata?

Con eso defino el formato exacto en el que tienes que exportar de Airtable para subir a Claude (probablemente CSV con columnas específicas), y el `export_prompt.md` del skill mapea Airtable raw fields → Notion Language Bank properties sin que tengas que mover nada a mano.

¿Te hace sentido el schema propuesto? ¿Algo que cambies, agregues o quites antes de que lo crees en Notion?

## 🧑 Adriana · 2026-05-07 06:10
1. Google resultsTotal
Resumen de resultados totales por búsqueda en Google.
Columna
Tipo
Search Query
Texto corto
Total Results
Número
AI Overview
Texto largo
Ad Count
Número
Term
Texto largo
URL
URL
Device
Texto corto
Country Code
Texto corto
Language Code
Texto corto
Date Found
Texto corto
2. Google organicResults
Resultados orgánicos de búsquedas en Google.
Columna
Tipo
Title
Texto largo
URL
URL
Displayed URL
URL
Description
Texto largo
Keywords
Texto largo
Product Info
Texto largo
Position
Número
Search Query
Texto largo
Date Found
Texto corto
3. Google peopleAlsoAsk
Preguntas del bloque "People Also Ask" de Google.
Columna
Tipo
Question
Texto corto
Title
Texto largo
Answer / Snippet
Texto largo
Source URL
URL
Keyword
Texto largo
Category
Selección única
Date Found
Texto corto
4. Google relatedQueries
Consultas relacionadas sugeridas por Google.
Columna
Tipo
Original Search
Texto corto
Title
Texto largo
URL
URL
Related Query
Texto largo
Date Found
Texto corto
5. Google paidResults
Anuncios pagados (resultados de pago) en Google.
Columna
Tipo
Ad Title
Texto corto
Description
Texto largo
Position
Número
Display URL
Texto largo
Search Query
Texto largo
Date Found
Texto corto
6. Google paidProducts
Productos pagados (Google Shopping) en resultados de búsqueda.
Columna
Tipo
Primary Field
Texto corto
Description
Texto largo
Price
Texto largo
Merchant
Texto largo
URL
URL
Position
Número
Search Query
Texto largo
Date Found
Texto corto
7. Google aiOverview
Fuentes citadas en el bloque de AI Overview de Google.
Columna
Tipo
Source Title
Texto corto
Source URL
URL
Brand Description
Texto largo
Search Query
Texto largo
Date Found
Texto corto
8. Reddit Raw
Datos crudos scrapeados de Reddit (fuente: trudax/reddit-scraper-lite).
Columna
Tipo
Title
Texto corto
Body
Texto largo
Author
Texto corto
Subreddit
Texto corto
URL
URL
Upvotes
Número
Data Type
Selección única (post / comment / community)
Flair
Texto corto
Date Created
Texto corto
Date Scraped
Texto corto
9. Twitter Raw
Datos crudos scrapeados de Twitter/X (fuente: apidojo/tweet-scraper).
Columna
Tipo
Tweet Text
Texto largo
Author Name
Texto corto
Author Username
Texto corto
URL
URL
Likes
Número
Retweets
Número
Replies
Número
Views
Número
Hashtags
Texto corto
Date Created
Texto corto
Date Scraped
Texto corto
10. Instagram Raw
Datos crudos scrapeados de Instagram (fuente: apify/instagram-scraper).
Columna
Tipo
Caption
Texto largo
Owner Username
Texto corto
URL
URL
Type
Selección única (post / reel / story / sidecar)
Likes
Número
Comments
Número
Video Views
Número
Hashtags
Texto corto
Location
Texto corto
Date Posted
Texto corto
Date Scraped
Texto corto
11. Facebook Raw
Datos crudos scrapeados de Facebook (fuente: apify/facebook-posts-scraper).
Columna
Tipo
Post Text
Texto largo
Page Name
Texto corto
URL
URL
Likes
Número
Comments
Número
Shares
Número
Date Published
Texto corto
Date Scraped
Texto corto
12. YouTube Raw
Datos crudos scrapeados de YouTube (fuente: streamers/youtube-scraper).
Columna
Tipo
Title
Texto corto
Description
Texto largo
Channel Name
Texto corto
URL
URL
Views
Número
Likes
Número
Comments
Número
Tags
Texto corto
Duration
Texto corto
Date Published
Texto corto
Date Scraped
Texto corto
Resumen: La base tiene 7 tablas de datos de Google (resultados totales, orgánicos, PAA, consultas relacionadas, anuncios pagados, productos pagados y AI Overview) y 5 tablas de raw data de redes sociales (Reddit, Twitter, Instagram, Facebook y YouTube). Todas las tablas de redes sociales siguen la misma lógica: almacenan datos crudos del scraper con métricas de engagement y fechas de creación/scraping.

## 🤖 Claude · 2026-05-07 06:12
Esto cambia la arquitectura del skill bastante. Antes de seguir, hay un patrón en los schemas que vale la pena nombrar — porque define qué tipo de extracción es posible desde cada fuente.

## Las 12 tablas no son del mismo tipo

Mirando con cuidado, tienes dos universos distintos:

**Voice of Customer (lenguaje verbatim del usuario):**
- Reddit Raw — Body completo + Data Type (post/comment) ✓
- Twitter Raw — Tweet Text completo ✓
- Reviews Intelligence DB — ya lo tienes separado ✓

**Category Context (lenguaje sobre la categoría, no del cliente directamente):**
- Instagram Raw — Caption (de la cuenta scrapeada, no comentarios)
- Facebook Raw — Post Text (de la página, no comentarios)
- YouTube Raw — Title + Description (del canal, no comentarios)
- Google peopleAlsoAsk — preguntas reales que la gente busca
- Google relatedQueries — vocabulario de categoría
- Google paidResults / paidProducts — copy de competidores
- Google organicResults — qué rankea
- Google aiOverview — cómo la AI resume la categoría

Esta separación cambia todo, porque cada universo alimenta cosas distintas en la extracción de angles.

## El gap que tienes que decidir cómo manejar

Tus tablas de Instagram, Facebook y YouTube **no capturan comentarios de usuarios** — solo el conteo (`Comments: número`). Capturan caption/post/título de la cuenta scrapeada. Eso significa que si scrapeas tu marca o competidores, tienes su *messaging side* pero no la *respuesta del cliente*. Para customer voice de IG/FB/YT necesitarías otro Apify actor (hay scrapers específicos de comments que entregan el texto, no solo el conteo).

Tres opciones, ninguna mala:

1. **Aceptar el gap.** Reddit + Twitter + Reviews son suficientes para Voice of Customer. IG/FB/YT se quedan como Category Context (qué dice la marca y los competidores). Es la opción más limpia y arrancas más rápido.

2. **Cerrar el gap.** Agregas tablas separadas — `Instagram Comments Raw`, `YouTube Comments Raw`, `Facebook Comments Raw` — con sus propios scrapers en Apify. Más completo pero más infra que mantener.

3. **Híbrido.** Aceptas el gap por ahora, pero tu skill anota explícitamente "no tenemos VoC de IG/FB/YT" en el output, así nunca asumes que tienes data que no tienes.

Mi voto: **opción 3 al inicio, migrar a 2 si la calidad del bank lo amerita después de 2-3 ciclos.** No bloquees por completitud.

## Cómo esto reforma el skill

La extracción no es uno-a-uno por fuente. Cada categoría de lenguaje tiene fuentes primarias y secundarias:

| Categoría a extraer | Fuente primaria | Fuente secundaria |
|---|---|---|
| Customer Language (verbatim) | Reddit, Twitter | Reviews |
| Transformation Language | Reviews, Reddit | Twitter |
| Sensory Language | Reviews, Reddit | — |
| Trust Language | Reddit (threads), Reviews | Twitter |
| Objections | Reddit (especialmente), Reviews | Twitter, peopleAlsoAsk |
| Emotional Benefit | Twitter, Reddit | Reviews |
| Core Product Language | Google paidResults, organicResults, aiOverview | IG/FB captions |
| Search-Intent Hooks | Google peopleAlsoAsk | relatedQueries |
| Competitive Gaps | Google paidResults vs aiOverview | IG captions |

Las preguntas de **peopleAlsoAsk** son oro que tu draft original no consideraba: son las preguntas literales que la gente teclea, listas para usarse como hooks. "¿El magnesio realmente reduce la ansiedad?" es un hook directo si tu marca puede responder con autoridad.

## Notion Language Bank — ajustes al schema

Dos propiedades nuevas que ahora tienen sentido:

| Propiedad nueva | Tipo | Por qué |
|---|---|---|
| Source Type | Select | VoC (Voice of Customer) / Category Context / Brand Messaging / Competitor Messaging. Esto te deja filtrar "dame solo VoC" cuando estás escribiendo un script UGC, vs "dame Category Context" cuando estás haciendo positioning |
| Originating Query | Text | Para frases derivadas de Google: la search query que la generó. Para frases de Reddit: el subreddit. Para Twitter: hashtag o conversación. Es metadata de contexto que ahorra trabajo después |

Y un cambio: **Source Platform** ahora tiene más opciones de las que pensé:
Reddit / Twitter / Instagram / Facebook / YouTube / Google PAA / Google Related / Google Paid / Google Organic / Google AI Overview / Reviews

Más granular, pero te permite queries del tipo "todas las objections que vinieron de Reddit" sin mezclarlas con captions de IG.

## Engagement como Volume Signal automatizable

Tus tablas tienen `Upvotes`, `Likes`, `Retweets`, `Replies`, `Views`, `Comments`, `Shares`. Eso te permite que el Volume Signal en Notion no sea un juicio del usuario sino algo derivable:

- High frequency: top 10% de engagement de su tabla origen
- Recurring: encima de la media
- Outlier: aparece pocas veces pero alto engagement

El skill puede calcular esto al exportar. Eso reduce trabajo manual de pressure testing.

---

**Lo que necesito de ti antes de escribir los archivos:**

1. ¿Cuál de las tres opciones para el comment gap eliges? (mi voto: opción 3)
2. ¿Te hace sentido el split VoC vs Category Context? Si sí, lo incorporo al SKILL.md como decisión de arquitectura
3. ¿Las dos propiedades nuevas (Source Type, Originating Query) entran al Notion DB? 

Con esos tres sí/no, puedo escribir el SKILL.md, schemas.md, evals.json y export_prompt.md completos en una sola pasada.

## 🧑 Adriana · 2026-05-07 06:41
ok reajuste despues de hacer un test, los values que extrae cada scrapping tool que aterrizza en airtable:

1. Google resultsTotal Resumen de resultados totales por búsqueda en Google. Columna Tipo Search Query Texto corto Total Results Número AI Overview Texto largo Ad Count Número Term Texto largo URL URL Device Texto corto Country Code Texto corto Language Code Texto corto Date Found Texto corto
2. Google organicResults Resultados orgánicos de búsquedas en Google. Columna Tipo Title Texto largo URL URL Displayed URL URL Description Texto largo Keywords Texto largo Product Info Texto largo Position Número Search Query Texto largo Date Found Texto corto
3. Google peopleAlsoAsk Preguntas del bloque "People Also Ask" de Google. Columna Tipo Question Texto corto Title Texto largo Answer / Snippet Texto largo Source URL URL Keyword Texto largo Category Selección única Date Found Texto corto
4. Google relatedQueries Consultas relacionadas sugeridas por Google. Columna Tipo Original Search Texto corto Title Texto largo URL URL Related Query Texto largo Date Found Texto corto
5. Google paidResults Anuncios pagados (resultados de pago) en Google. Columna Tipo Ad Title Texto corto Description Texto largo Position Número Display URL Texto largo Search Query Texto largo Date Found Texto corto
6. Google paidProducts Productos pagados (Google Shopping) en resultados de búsqueda. Columna Tipo Primary Field Texto corto Description Texto largo Price Texto largo Merchant Texto largo URL URL Position Número Search Query Texto largo Date Found Texto corto
7. Google aiOverview Fuentes citadas en el bloque de AI Overview de Google. Columna Tipo Source Title Texto corto Source URL URL Brand Description Texto largo Search Query Texto largo Date Found Texto corto
8. Reddit Raw — Raw data from Reddit Scraper Lite (oAuCIx3ItNrs2okjQ)
Columna
Tipo
Mapea a
Author Flair
Texto corto
authorFlair
Body
Texto largo
body
Username
Texto corto
username
Community Name
Texto corto
communityName
URL
URL
url
Data Type
Select
dataType
Created At
Texto corto
createdAt
Scraped At
Texto corto
scrapedAt
Category
Texto corto
category
HTML
Texto largo
html
ID
Texto corto
id
Number Of Replies
Número
numberOfReplies
Parent ID
Texto corto
parentId
Parsed ID
Texto corto
parsedId
Post ID
Texto corto
postId
Up Votes
Número
upVotes
User ID
Texto corto
userId
Twitter Raw — Raw data from Tweet Scraper V2 (61RPP7dywgiy0JPD0)
Columna
Tipo
Mapea a
Text
Texto largo
text
Twitter URL
Texto corto
twitterUrl
Tweet ID
Texto corto
id
URL
URL
url
Like Count
Número
likeCount
Retweet Count
Número
retweetCount
Reply Count
Número
replyCount
Quote Count
Número
quoteCount
Bookmark Count
Texto corto
bookmarkCount
Created At
Texto corto
createdAt
Date Scraped
Texto corto
—
Is Retweet
Checkbox
isRetweet
Is Quote
Checkbox
isQuote
Instagram Raw — Raw data from Meta API Comments (graph.facebook.com/v19)
Columna
Tipo
Mapea a
Text
Texto largo
text
Username
Texto corto
username
Comment ID
Texto corto
id
Like Count
Número
like_count
Reply Count
Número
replies.count
Media ID
Texto corto
media_id
Media Type
Select
media_type
Media Permalink
URL
media_permalink
Parent ID
Texto corto
parent_id
Timestamp
Texto corto
timestamp
Date Scraped
Texto corto
—
Facebook Raw — Raw data from Facebook Posts Scraper (KoJrdxJCTtpon81KY)
Columna
Tipo
Mapea a
Text
Texto largo
text
Page Name
Texto corto
pageName
URL
URL
url
Likes
Número
likes
Comments
Número
comments
Shares
Número
shares
Time
Texto corto
time
Date Scraped
Texto corto
—
Facebook ID
Texto corto
facebookId
Facebook URL
Texto corto
facebookUrl
Feedback ID
Texto corto
feedbackId
Input URL
Texto corto
inputUrl
Is Video
Checkbox
isVideo
Link
Texto corto
link
Page Ad Library
Texto corto
pageAdLibrary
Post ID
Texto corto
postId
Reaction Angry Count
Número
reactionAngryCount
Reaction Care Count
Número
reactionCareCount
Reaction Haha Count
Número
reactionHahaCount
Reaction Like Count
Número
reactionLikeCount
Reaction Love Count
Número
reactionLoveCount
Reaction Sad Count
Número
reactionSadCount
Reaction Wow Count
Número
reactionWowCount
Text References
Texto largo
textReferences
Timestamp
Texto corto
timestamp
Top Level URL
Texto corto
topLevelUrl
Top Reactions Count
Número
topReactionsCount
User
Texto corto
user
Views Count
Número
viewsCount
YouTube Raw — Raw data from YouTube Scraper (h7sDV53CddomktSi5)
Columna
Tipo
Mapea a
Title
Texto corto
title
Channel Name
Texto corto
channelName
Channel URL
Texto corto
—
URL
URL
url
View Count
Número
viewCount
Likes
Número
likes
Comments Count
Número
commentsCount
Type
Texto largo
type
Duration
Texto corto
duration
Published
Texto corto
date
Date Scraped
Texto corto
—

## 🤖 Claude · 2026-05-07 06:43
Esto cambia las cosas para mejor. Hay un upgrade enorme y dos hallazgos que vale la pena nombrar antes de cerrar el diseño.

## El cambio grande: Instagram ahora es Voice of Customer

Tu nuevo IG Raw scrapea desde **Meta API Comments**, no captions. Tienes `Text` con el comentario verbatim, `Username`, `Like Count`, `Reply Count`, `Parent ID` para threading. Eso lo mueve completamente del bucket "Category Context" al bucket "Voice of Customer". Ahora tienes **tres fuentes fuertes de voz del cliente**: Reddit, Twitter, Instagram. Más Reviews Intelligence DB que ya existe. Eso es robusto.

Facebook y YouTube se quedan en Category Context, pero por razones distintas:

- **Facebook** sigue siendo posts de páginas (con `Page Name` y `Text`), no comentarios — pero ahora tiene **7 tipos de reacciones desglosadas** (angry, care, haha, like, love, sad, wow). Eso convierte FB en una fuente de **señal emocional cuantificada** sobre qué resuena. Un post con alto `reactionAngryCount` te está diciendo qué frustra al mercado. Alto `reactionLoveCount` te dice qué emociona. Alto `reactionHahaCount` te dice qué tono humorístico funciona.
- **YouTube** se redujo: ya no tiene Description ni Tags, solo metadata del video. Sirve para identificar qué *temas* y *formatos* funcionan en la categoría, no para extraer lenguaje.

## Tres oportunidades que los nuevos schemas desbloquean

**1. Filtros de calidad automatizables.** Tu Twitter Raw tiene `isRetweet` e `isQuote` como checkboxes. El skill debe excluirlos por default — un retweet no es voz propia, es eco. Reddit Raw tiene `Data Type` (post/comment/community), y el skill debe tratarlos distinto:
- Posts → señal de qué *temas* iniciar
- Comments → señal de qué *lenguaje* usar
- Community → contexto de la subreddit, no contenido extraíble

**2. Volume Signal automático por percentil.** Tienes engagement quantitativo en todas las VoC sources. El skill puede calcular el Volume Signal sin que tú lo decidas:
- Reddit: `upVotes` > p75 de su tabla → High frequency
- Twitter: `likeCount + retweetCount` > p75 → High frequency
- Instagram: `like_count` > p75 → High frequency

Esto reduce trabajo manual de pressure testing — llegas con frases pre-rankeadas.

**3. Facebook reactions como sentiment layer.** Esto es nuevo y específico. Una propiedad en el Notion DB que capture el `dominant_reaction` cuando la frase viene de FB le da al brief downstream una señal directa: "esta frase salió de un post con alto Love" → buena para Emotional Benefit hooks. "Esta salió de alto Angry" → buena para Problem-aware hooks que validan frustración.

## Schema Notion final propuesto

Después de incorporar todo esto, así queda:

**Core (la frase y dónde nació):**
| Propiedad | Tipo |
|---|---|
| Phrase | Title |
| Brand | Relation → Brand DB |
| Source Platform | Select: Reddit / Twitter / Instagram / Facebook / YouTube / Google PAA / Google Related / Google Paid / Google Organic / Google AI Overview / Reviews |
| Source Type | Select: VoC (Voice of Customer) / Category Context / Brand Messaging / Competitor Messaging |
| Source Subtype | Select: Reddit Post / Reddit Comment / Tweet / IG Comment / FB Post / Search Query / PAA Question / Ad Copy / Caption |
| Source URL | URL |
| Originating Query | Text (para Google: search query; para Reddit: subreddit; para Twitter: hashtag o conversación) |
| Date Extracted | Date |

**Clasificación creativa:**
| Propiedad | Tipo |
|---|---|
| Language Category | Multi-select: Customer / Transformation / Sensory / Emotional Benefit / Trust / Objection / Core Product / Search Intent |
| Awareness Stage | Select: Unaware / Problem-aware / Solution-aware / Product-aware / Most-aware |
| Persona | Relation → Persona DB |
| Downstream Use | Multi-select: Hook candidate / Body script / Objection handler / Transformation moment / Trust builder / CTA frame / Search-intent hook |

**Calidad y validación:**
| Propiedad | Tipo |
|---|---|
| Pressure Tests Passed | Multi-select: Specificity / Truth / Volume / Hook |
| Volume Signal | Select: Outlier / Recurring / High frequency (auto-calculado por percentil de engagement) |
| Engagement Score | Number (el valor crudo de la fuente — upvotes, likes, etc.) |
| Dominant Reaction | Select (solo para Facebook): Angry / Care / Haha / Like / Love / Sad / Wow |
| Hero Line | Checkbox |
| Status | Select: Draft / Approved / In use / Retired |

**Loop con creative pipeline:**
| Propiedad | Tipo |
|---|---|
| Used In | Relation → Concepts DB |
| Performance | Select: Won / Lost / Mixed / Pending |
| Date Approved | Date |
| Notes | Text |

Total: ~20 propiedades. Suena mucho pero la mitad son Selects/Multi-selects que el skill autopopula desde la fuente. Solo Phrase, Persona, Downstream Use y Pressure Tests requieren juicio humano en la sesión.

## Cómo se estructura el skill

Con todo esto cuadrado, el SKILL.md va a tener cuatro stages:

**S1 — Resource Collection Gate + Source Classification.** El usuario sube CSVs de las tablas que quiera usar. El skill clasifica cada uno por Source Type, aplica filtros automáticos (excluir retweets, separar posts de comments en Reddit, identificar parent comments en IG), y publica un bloque de estado con conteos por fuente.

**S2 — Pattern Extraction asimétrica.** Cada Source Type extrae cosas distintas:
- VoC sources → 7 categorías de lenguaje verbatim con engagement score
- Category Context → competitive angles, search questions, AI Overview summaries
- Brand Messaging → captions/posts del brand para mapear lo que ya estás diciendo
- Competitor Messaging → posts de competidores para mapear el espacio

**S3 — Cross-Source Triangulation + Pressure Testing.** Las frases que aparecen en múltiples VoC sources con engagement alto saltan al top. El skill propone, el usuario aprueba con los 4 tests. Hero Lines se marcan explícitamente.

**S4 — Export Notion-compatible.** Tabla Markdown con las propiedades exactas, lista para CSV import o paste manual.

---

Si todo esto te cuadra (especialmente: ~20 propiedades en el Notion DB, los 4 stages, y el manejo asimétrico por Source Type), digo "ok" y arranco a escribir los cuatro archivos: `SKILL.md`, `schemas.md`, `evals.json` y `references/export_prompt.md`. Si algo te suena de más o de menos, ajustamos antes.

¿Le damos?

## 🧑 Adriana · 2026-05-07 06:49
perfecto lo unico que falta agregar es que, esa tabla markdown en su lugar quiero que se popule sola con la conexion de claude con notion app, se puede?

## 🤖 Claude · 2026-05-07 06:50
Sí, se puede. Tengo acceso al connector de Notion, así que el skill puede llamar `notion-create-pages` directamente y las frases aprobadas aparecen en tu Language Bank DB en tiempo real durante la sesión, no como Markdown para copiar/pegar.

Eso cambia tres cosas en el diseño:

**1. El DB tiene que existir primero.** El skill no puede escribir en algo que no existe. Dos caminos: o lo creas tú a mano con el schema que definimos, o el skill ejecuta `notion-create-database` en la primera corrida. Crearlo automatizado garantiza que los nombres de propiedades y las opciones de selects coincidan exactamente con lo que el skill espera escribir. Crearlo a mano te da más control sobre dónde vive (workspace, teamspace, página padre) pero introduce riesgo de mismatch — si una opción de select se llama "VoC" en Notion pero el skill escribe "Voice of Customer", el campo queda vacío.

**2. El `export_prompt.md` se reemplaza por un protocolo de escritura estructurada.** En lugar de generar tabla Markdown, el archivo se vuelve un mapping schema: "para cada frase aprobada, llama notion-create-pages con esta estructura de propiedades". Lo dejo en `references/notion_write_protocol.md`.

**3. Necesito un fallback documentado.** Si el connector falla por auth, latencia o rate limit, el skill cae al export Markdown como respaldo. No se pierde una sesión de pressure testing por un error de conexión. Eso queda declarado en los guardrails del SKILL.md.

**Mi recomendación para el DB:** lo creas tú, pero con un protocolo asistido. El skill, en su primera ejecución, hace dos cosas antes de extraer nada:

1. Te pasa un bloque copy/paste-able con cada propiedad y sus opciones exactas para que crees el DB en Notion sin ambigüedad (o usas el schema que ya generamos)
2. Te pide el database_id (lo sacas del URL del DB) y hace un `notion-fetch` de validación: lee el schema real, lo compara contra lo que el skill espera, y te avisa de cualquier mismatch antes de empezar a escribir

Eso da control + safety. Después de la primera sesión el database_id queda guardado y nunca más se valida (a menos que tú lo cambies).

¿Le damos a construir? Si dices sí, escribo en una sola pasada: `SKILL.md`, `schemas.md`, `evals.json` y `references/notion_write_protocol.md`. 4 archivos, listos para que los pruebes con datos reales.

## 🧑 Adriana · 2026-05-07 06:53
dame el schema de notion final propuesto como instrucciones en formato json, para pasarlo al ai the notion para que me lo cree con cada criterio que tu determinaste

## 🤖 Claude · 2026-05-07 06:55
Aquí va. Pegalo tal cual a Notion AI con un prompt corto del tipo *"Create this database in my workspace following this exact specification:"* y debería generarte la estructura completa.

```json
{
  "instruction": "Create a new Notion database named 'Language Bank' with the following exact specification. Each property must match the type, options, colors, and description listed. Preserve all option names exactly — they are referenced programmatically by an external system.",

  "database": {
    "name": "Language Bank",
    "icon": "💬",
    "description": "Central repository of customer voice and category language extracted from social listening sources (Reddit, Twitter, Instagram, Facebook, YouTube, Google) and reviews. Each entry is a verbatim phrase or pattern, classified by source, language category, awareness stage, and creative use. Feeds directly into ad concept briefs, hooks, and creative strategy work.",

    "properties": [
      {
        "name": "Phrase",
        "type": "Title",
        "description": "The verbatim quote or phrase exactly as it appeared in the source. Do not paraphrase — preserve original wording, punctuation, and tone."
      },
      {
        "name": "Brand",
        "type": "Relation",
        "target_database": "Brand Brain",
        "description": "Link to the brand this phrase belongs to. Required if managing multiple brands."
      },
      {
        "name": "Source Platform",
        "type": "Select",
        "description": "The platform where the phrase originated.",
        "options": [
          { "name": "Reddit", "color": "orange" },
          { "name": "Twitter", "color": "blue" },
          { "name": "Instagram", "color": "pink" },
          { "name": "Facebook", "color": "blue" },
          { "name": "YouTube", "color": "red" },
          { "name": "Google PAA", "color": "yellow" },
          { "name": "Google Related", "color": "yellow" },
          { "name": "Google Paid", "color": "yellow" },
          { "name": "Google Organic", "color": "yellow" },
          { "name": "Google AI Overview", "color": "yellow" },
          { "name": "Reviews", "color": "green" }
        ]
      },
      {
        "name": "Source Type",
        "type": "Select",
        "description": "Whether this is direct customer voice, category context, brand messaging, or competitor messaging.",
        "options": [
          { "name": "VoC", "color": "green" },
          { "name": "Category Context", "color": "blue" },
          { "name": "Brand Messaging", "color": "purple" },
          { "name": "Competitor Messaging", "color": "red" }
        ]
      },
      {
        "name": "Source Subtype",
        "type": "Select",
        "description": "More granular classification of where exactly the phrase came from.",
        "options": [
          { "name": "Reddit Post", "color": "orange" },
          { "name": "Reddit Comment", "color": "orange" },
          { "name": "Tweet", "color": "blue" },
          { "name": "IG Comment", "color": "pink" },
          { "name": "FB Post", "color": "blue" },
          { "name": "YouTube Video Title", "color": "red" },
          { "name": "Search Query", "color": "yellow" },
          { "name": "PAA Question", "color": "yellow" },
          { "name": "Ad Copy", "color": "yellow" },
          { "name": "AI Overview Source", "color": "yellow" },
          { "name": "Review", "color": "green" }
        ]
      },
      {
        "name": "Source URL",
        "type": "URL",
        "description": "Direct link to the source content for traceability."
      },
      {
        "name": "Originating Query",
        "type": "Text",
        "description": "Context that produced the phrase. For Google: the search query. For Reddit: subreddit name. For Twitter: hashtag or conversation."
      },
      {
        "name": "Date Extracted",
        "type": "Date",
        "description": "When the phrase was scraped or extracted. Used to detect language shifts over time."
      },
      {
        "name": "Language Category",
        "type": "Multi-select",
        "description": "What kind of language this phrase represents. Multi-select because a phrase can be Sensory + Emotional Benefit at the same time.",
        "options": [
          { "name": "Customer", "color": "blue" },
          { "name": "Transformation", "color": "green" },
          { "name": "Sensory", "color": "purple" },
          { "name": "Emotional Benefit", "color": "pink" },
          { "name": "Trust", "color": "yellow" },
          { "name": "Objection", "color": "red" },
          { "name": "Core Product", "color": "brown" },
          { "name": "Search Intent", "color": "orange" }
        ]
      },
      {
        "name": "Awareness Stage",
        "type": "Select",
        "description": "Schwartz awareness stage that this phrase reveals. Maps to TOF/MOF/BOF in ad briefs.",
        "options": [
          { "name": "Unaware", "color": "gray" },
          { "name": "Problem-aware", "color": "yellow" },
          { "name": "Solution-aware", "color": "orange" },
          { "name": "Product-aware", "color": "green" },
          { "name": "Most-aware", "color": "blue" }
        ]
      },
      {
        "name": "Persona",
        "type": "Relation",
        "target_database": "Personas",
        "description": "The persona segment that uses this language."
      },
      {
        "name": "Downstream Use",
        "type": "Multi-select",
        "description": "What this phrase is ready to be used for in creative work. Forces the bank to be operational, not taxonomic.",
        "options": [
          { "name": "Hook candidate", "color": "red" },
          { "name": "Body script", "color": "blue" },
          { "name": "Objection handler", "color": "yellow" },
          { "name": "Transformation moment", "color": "green" },
          { "name": "Trust builder", "color": "purple" },
          { "name": "CTA frame", "color": "pink" },
          { "name": "Search-intent hook", "color": "orange" }
        ]
      },
      {
        "name": "Pressure Tests Passed",
        "type": "Multi-select",
        "description": "Quality validation. A phrase needs at least 3 of 4 to be Approved. Specificity = could any brand say this? Truth = does it sound like a real person typing? Volume = does the pattern repeat? Hook = could it work in the first 3 seconds of an ad?",
        "options": [
          { "name": "Specificity", "color": "blue" },
          { "name": "Truth", "color": "green" },
          { "name": "Volume", "color": "yellow" },
          { "name": "Hook", "color": "red" }
        ]
      },
      {
        "name": "Volume Signal",
        "type": "Select",
        "description": "How often this pattern appeared in the source. Auto-calculated from engagement percentile when possible.",
        "options": [
          { "name": "Outlier", "color": "gray" },
          { "name": "Recurring", "color": "yellow" },
          { "name": "High frequency", "color": "green" }
        ]
      },
      {
        "name": "Engagement Score",
        "type": "Number",
        "description": "Raw engagement value from the source: upvotes for Reddit, like+retweet count for Twitter, like_count for Instagram. Used to compute Volume Signal."
      },
      {
        "name": "Dominant Reaction",
        "type": "Select",
        "description": "Only for Facebook-sourced phrases. The dominant emotional reaction on the originating post. Tells you what emotional register the phrase taps into.",
        "options": [
          { "name": "Angry", "color": "red" },
          { "name": "Care", "color": "pink" },
          { "name": "Haha", "color": "yellow" },
          { "name": "Like", "color": "blue" },
          { "name": "Love", "color": "red" },
          { "name": "Sad", "color": "purple" },
          { "name": "Wow", "color": "orange" }
        ]
      },
      {
        "name": "Hero Line",
        "type": "Checkbox",
        "description": "Flag for standout phrases that are exceptionally strong. Different from category — Hero Line is a quality marker, not a content type."
      },
      {
        "name": "Status",
        "type": "Status",
        "description": "Lifecycle of the phrase in the bank.",
        "options": [
          { "name": "Draft", "color": "gray", "group": "To-do" },
          { "name": "Approved", "color": "green", "group": "In progress" },
          { "name": "In use", "color": "blue", "group": "In progress" },
          { "name": "Retired", "color": "brown", "group": "Complete" }
        ]
      },
      {
        "name": "Used In",
        "type": "Relation",
        "target_database": "Concepts",
        "description": "Concepts or briefs where this phrase has been used. Closes the feedback loop: every approved phrase can be traced to ad outputs."
      },
      {
        "name": "Performance",
        "type": "Select",
        "description": "If used in an ad, what was the result. Feeds back into deciding which language to prioritize.",
        "options": [
          { "name": "Won", "color": "green" },
          { "name": "Lost", "color": "red" },
          { "name": "Mixed", "color": "yellow" },
          { "name": "Pending", "color": "gray" }
        ]
      },
      {
        "name": "Date Approved",
        "type": "Date",
        "description": "When the phrase passed pressure testing and moved from Draft to Approved."
      },
      {
        "name": "Notes",
        "type": "Text",
        "description": "Any additional context that doesn't fit other properties."
      }
    ],

    "default_views": [
      {
        "name": "All Phrases",
        "type": "Table",
        "shows_all_properties": true
      },
      {
        "name": "Pending Review",
        "type": "Table",
        "filter": "Status is Draft",
        "sort": "Date Extracted descending"
      },
      {
        "name": "Approved",
        "type": "Table",
        "filter": "Status is Approved",
        "sort": "Date Approved descending"
      },
      {
        "name": "Hero Lines",
        "type": "Gallery",
        "filter": "Hero Line is checked AND Status is not Retired"
      },
      {
        "name": "By Category",
        "type": "Board",
        "group_by": "Language Category"
      },
      {
        "name": "By Awareness Stage",
        "type": "Board",
        "group_by": "Awareness Stage"
      },
      {
        "name": "VoC Only",
        "type": "Table",
        "filter": "Source Type is VoC AND Status is Approved"
      }
    ]
  },

  "post_creation_notes": [
    "If 'Brand Brain', 'Personas', or 'Concepts' target databases do not exist yet, create the Relation properties anyway and link the targets later when those databases are ready.",
    "The Status property must use Notion's native Status type (not Select) to enable kanban-style workflow grouping.",
    "Dominant Reaction will be empty for non-Facebook sources — that is expected, not an error.",
    "Engagement Score should be a plain integer with no special formatting (no currency, no percentage)."
  ]
}
```

Una vez creado, mándame el `database_id` de la URL de Notion (la parte después de `notion.so/` y antes del `?`). Con eso el skill puede validar el schema en su primera corrida y empezar a escribir directo. Cuando lo tengas listo arrancamos a construir los archivos del skill.

## 🧑 Adriana · 2026-05-07 07:11
ya quedo tal cual como lo pediste con esas propiedades, todo tal cual. 
creo que ya puedes hacer `SKILL.md`, `schemas.md`, `evals.json` y `references/export_prompt.md`

## 🤖 Claude · 2026-05-07 07:19
Perfecto. Voy a leer primero la guía de skill-creator para asegurar que sigo el formato correcto, y luego construyo los cuatro archivos.

Listo. Ahora construyo los cuatro archivos siguiendo el patrón de motion-creative-pipeline.

Ahora escribo el `SKILL.md`:

Ahora creo `schemas.md` con los JSON de cada stage:

Ahora creo `evals.json` con los casos de prueba:

Por último, creo `references/notion_write_protocol.md`:

Verifico la estructura y muevo los archivos a outputs:

Listo. Estructura final:

```
language-bank-pipeline/
├── SKILL.md                          (420 líneas)
├── schemas.md                        (351 líneas)
├── evals.json                        (4 casos de prueba)
└── references/
    └── notion_write_protocol.md      (241 líneas)
```

**Decisiones de diseño que implementé y vale la pena que veas:**

Cambié el nombre de `scrapping-data-angle-messaging-extraction` a `language-bank-pipeline` para mantener la familia de naming con `motion-creative-pipeline`. Si prefieres el original solo cambia los headers — ningún archivo depende del nombre.

El skill tiene **4 stages secuenciales** (no entradas opcionales como motion-creative-pipeline) porque la lógica del pipeline es lineal: ingesta → extracción → pressure test → write. No tiene sentido entrar en S3 sin haber hecho S1.

La filosofía **VoC vs Category Context** quedó como sección dedicada al inicio del SKILL.md, no enterrada — porque es la decisión arquitectónica que separa este skill de un "extrae frases de CSVs" genérico.

El **fallback Markdown** está documentado como circuito de respaldo serio, no como afterthought. La tabla generada tiene headers exactos que coinciden 1:1 con las propiedades del Notion DB, lista para CSV import sin reformatear.

Los **4 evals** cubren el camino feliz, dos failure modes críticos (schema mismatch y connector down), y un edge case importante (cuando el usuario quiere aprobar una frase que falla pressure tests — el skill no debe bloquear pero sí dejar rastro auditable).

**Para probar el skill:** corre el caso 1 de evals.json en una sesión limpia con CSVs reales. Si pasa todas las expectations, está listo para producción. Si falla en alguna, me dices cuál y ajustamos antes de que lo subas a tu carpeta de skills.

## 🧑 Adriana · 2026-05-07 23:28
hay otros pasos en lo que tambien se hace scraping e input final en notion, esto es solo para el messaging and angle session. cuidado

## 🤖 Claude · 2026-05-07 23:28
Tienes razón, gracias por la corrección. El scraping es transversal a varios stages de tu sistema, no propiedad de este skill. Este skill solo cubre **una sesión específica** dentro de un workflow más grande: convertir scrapes ya disponibles en angles/messaging aprobados para esa sección particular del Brand Brain.

Antes de tocar los archivos, déjame entender bien para no volver a sobre-extender el alcance:

**Lo que necesito que me aclares:**

1. **¿Cuáles son los otros stages que también scrapean y escriben a Notion?** Para nombrarlos en el SKILL.md como "fuera de alcance" y evitar que el skill se active cuando alguien dispare uno de esos workflows.

2. **El nombre Messaging and Angles** que mostraste en tu mensaje original con el emoji 💌 — ¿ese es el nombre exacto de la sección/DB destino en Notion? Si sí, el skill debería referenciarlo por ese nombre, no por "Language Bank" genérico.

3. **El alcance real de esta sesión específica:** ¿es solo messaging y angles (frases que se convierten en hooks, body copy, objection handling), o también incluye lenguaje sensorial, transformacional, etc.? Pregunto porque si es estrictamente "messaging y angles" entonces algunas de las 8 Language Categories que metí (Sensory, Transformation) podrían pertenecer a otra sesión distinta.

4. **¿Los scrapes que entran a este skill ya están limpios** (otro skill o proceso anterior los procesó), o entran crudos desde Airtable como los diseñamos? Si hay un skill upstream que pre-procesa, este skill arranca más adelante en el flujo y el Resource Collection Gate cambia.

5. **¿Hay un skill orquestador** que llama a este como sub-rutina, o el usuario activa este directamente cuando está trabajando la sección de Messaging and Angles?

Con esas 5 respuestas reescribo los 4 archivos para que el skill quede correctamente acotado a su rol específico — no como "language pipeline general" sino como "sesión de Messaging and Angles dentro de un sistema más grande". El fix probablemente es:

- Renombrar el skill a algo más preciso (`messaging-angles-session` o similar)
- Acotar el `description` para que NO se active en otros contextos de scraping
- Quitar las categorías que no son de messaging/angles si pertenecen a otras sesiones
- Ajustar el Resource Collection Gate al input real que recibe esta sesión específica
- Dejar referencia explícita a los otros stages para que el usuario sepa cuándo NO usar este skill

¿Me das esos 5 contextos y lo reescribo limpio?
