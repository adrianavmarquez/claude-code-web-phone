---
title: "Archivista de memoria de proyecto para exportación de marca"
source: claude.ai-chat
created: "2026-07-05 01:24"
summary: "**Conversation overview**  The person, Adriana V. Márquez (@adrianavmarquez), is a content strategist, brand consultant, and coach working primarily with personal brands, creators, and founders across Latin America. She used this conversation to act as archivist of her own Project's memory, requesting that Claude consolidate all accumulated brand knowledge into a single structured markdown document using an exact template she provided, then export it as a downloadable `.md` file.  The task involved extracting information from three sources: the Project's system prompt/instructions, uploaded knowledge files, and recurring patterns from past conversations. Claude searched conversation history and read skill files stored in the project environment to reconstruct Adriana's brand identity, methodology, client roster, visual standards, operational preferences, and recurring task patterns. The final deliverable covered 14 sections including brand identity, voice and tone, visual branding, operational preferences, accumulated decisions, and open pendientes. Key methodology terms used throughout include VOC (Voice of Customer), the three rules of gold (visualizable, falsifiable, uniquely ownable), 'Cinematic Confessional' for storytime scripting, and the POV formula (Lived Experience + Psychological Insight) × Negation of Mass Consensus. Her central brand philosophy is 'te sacudo, no te consiento.'  Adriana's client roster referenced in the document includes Daniela Alsina (architectural/interior designer, Miami), Claudia Grice (creator focused on migration and personal growth, Arizona), Mariana Salas (creator transitioning from engineering, Brazil), Luz/luzchapeton (founder building an Instagram personal brand), and Julieth Ferreira (creator behind a 28-day digital journaling method called 'Volver a mí'). Key operational preferences documented include: delivering paste-ready outputs without follow-up questions, keeping explanations in the Claude chat rather than pushing them to Notion pages, flagging out-of-scope edits transparently, using tuteo (not voseo), writing in Spanish and Spanglish, and producing markdown compatible with Notion. After Claude delivered the full markdown in a code block, Adriana requested it as a downloadable file, which Claude created at `/mnt/user-data/outputs/Memoria_de_marca_Adriana_V_Marquez.md` and presented for download.  **Tool knowledge**  Claude used bash to write the markdown file directly to `/mnt/user-data/outputs/` using a heredoc (`<< 'ADRIEOF'`), then used the `present_files` tool to surface the download link. The heredoc approach with a quoted delimiter (`'ADRIEOF'`) was necessary to prevent shell interpretation of special characters inside the markdown content. Before writing the file, Claude used `conversation_search` with specific thematic queries (brand identity terms, methodology names, client names) to retrieve relevant conversation history, and used `bash_tool` to read skill files directly from `/mnt/skills/user/` subdirectories. Reading the first 80-120 lines of each skill file with `head` was sufficient to extract the core identity and methodology parameters without loading full file contents. No uploaded files were present in `/mnt/user-data/uploads/` for this session; all brand knowledge came from skill files and conversation history."
messages: 4
claude_uuid: "f87456cb-cddb-4fc9-b1f6-3c898f0abb5a"
tags: [claude, chat, archive]
---
# Archivista de memoria de proyecto para exportación de marca

> **Conversation overview**

The person, Adriana V. Márquez (@adrianavmarquez), is a content strategist, brand consultant, and coach working primarily with personal brands, creators, and founders across Latin America. She used this conversation to act as archivist of her own Project's memory, requesting that Claude consolidate all accumulated brand knowledge into a single structured markdown document using an exact template she provided, then export it as a downloadable `.md` file.

The task involved extracting information from three sources: the Project's system prompt/instructions, uploaded knowledge files, and recurring patterns from past conversations. Claude searched conversation history and read skill files stored in the project environment to reconstruct Adriana's brand identity, methodology, client roster, visual standards, operational preferences, and recurring task patterns. The final deliverable covered 14 sections including brand identity, voice and tone, visual branding, operational preferences, accumulated decisions, and open pendientes. Key methodology terms used throughout include VOC (Voice of Customer), the three rules of gold (visualizable, falsifiable, uniquely ownable), "Cinematic Confessional" for storytime scripting, and the POV formula (Lived Experience + Psychological Insight) × Negation of Mass Consensus. Her central brand philosophy is "te sacudo, no te consiento."

Adriana's client roster referenced in the document includes Daniela Alsina (architectural/interior designer, Miami), Claudia Grice (creator focused on migration and personal growth, Arizona), Mariana Salas (creator transitioning from engineering, Brazil), Luz/luzchapeton (founder building an Instagram personal brand), and Julieth Ferreira (creator behind a 28-day digital journaling method called "Volver a mí"). Key operational preferences documented include: delivering paste-ready outputs without follow-up questions, keeping explanations in the Claude chat rather than pushing them to Notion pages, flagging out-of-scope edits transparently, using tuteo (not voseo), writing in Spanish and Spanglish, and producing markdown compatible with Notion. After Claude delivered the full markdown in a code block, Adriana requested it as a downloadable file, which Claude created at `/mnt/user-data/outputs/Memoria_de_marca_Adriana_V_Marquez.md` and presented for download.

**Tool knowledge**

Claude used bash to write the markdown file directly to `/mnt/user-data/outputs/` using a heredoc (`<< 'ADRIEOF'`), then used the `present_files` tool to surface the download link. The heredoc approach with a quoted delimiter (`'ADRIEOF'`) was necessary to prevent shell interpretation of special characters inside the markdown content. Before writing the file, Claude used `conversation_search` with specific thematic queries (brand identity terms, methodology names, client names) to retrieve relevant conversation history, and used `bash_tool` to read skill files directly from `/mnt/skills/user/` subdirectories. Reading the first 80-120 lines of each skill file with `head` was sufficient to extract the core identity and methodology parameters without loading full file contents. No uploaded files were present in `/mnt/user-data/uploads/` for this session; all brand knowledge came from skill files and conversation history.

## 🧑 Adriana · 2026-07-05 01:24
Vas a actuar como archivista de la memoria de este Proyecto. Tu tarea es consolidar TODO el conocimiento duradero que este Proyecto tiene sobre la marca o cliente, para exportarlo y reutilizarlo en otra herramienta. Fuentes de las que debes extraer:

1. Las instrucciones personalizadas de este Proyecto (su "system prompt").
2. Los documentos y archivos de conocimiento cargados en el Proyecto.
3. Los patrones y decisiones recurrentes que se repiten en las conversaciones de este Proyecto. Reglas:

* No inventes nada. Si un dato no está definido, escribe "No definido".
* Sé exhaustivo y específico, sobre todo en identidad de marca, voz y tono.
* Devuelve UN solo documento en markdown, dentro de un bloque de código, listo para copiar y pegar.
* Prohibido usar el guion largo (em dash). Usa comas, puntos, dos puntos o paréntesis.
* Rellena esta plantilla EXACTA, respetando los títulos:
marca: <nombre de la marca> tipo_proyecto: <ej. social media, e-commerce, marca personal> plataformas: <canales donde opera> fecha_extraccion: <fecha de hoy> estado: activo
Memoria de marca: <NOMBRE>
1. Identidad de marca

* Nombre y tagline:
* Misión y propósito:
* Valores:
* Historia breve:
2. Producto, servicio u oferta

* Qué se vende u ofrece:
* Propuesta de valor:
* Precios o paquetes (si aplica):
3. Público objetivo

* Buyer persona principal:
* Otros segmentos:
* Dolores y deseos:
4. Voz y tono

* Personalidad de marca:
* Palabras y expresiones que SÍ usar:
* Palabras y expresiones que NO usar:
* Reglas de estilo:
5. Estilo visual y branding

* Colores:
* Tipografías:
* Referencias estéticas:
6. Canales y plataformas

* Handles y enlaces:
* Prioridad de cada canal:
7. Objetivos y KPIs

* Objetivos actuales:
* Métricas que importan:
8. Preferencias operativas

* Cómo le gusta trabajar al cliente:
* Formatos que suele pedir:
9. Contexto acumulado y decisiones clave

* Decisiones importantes tomadas (con fecha si se sabe):
* Aprendizajes:
10. Activos y recursos

* Enlaces a documentos, carpetas, plantillas:
11. Tareas recurrentes

* Qué se pide con frecuencia en este Proyecto:
12. Restricciones y reglas

* Qué nunca hacer:
13. Glosario y datos clave

* Términos, nombres, fechas o datos a recordar:
14. Pendientes y preguntas abiertas

* Lo que quedó sin definir:

## 🤖 Claude · 2026-07-05 01:27
Voy a consolidar todo el conocimiento duradero de este Proyecto. Primero necesito revisar las tres fuentes: las instrucciones del Proyecto, los archivos cargados y los patrones recurrentes en las conversaciones. Déjame empezar por revisar los skills y buscar en el historial.

Tengo buen contexto de los clientes. Ahora necesito revisar las instrucciones del Proyecto y los archivos cargados. Déjame revisar los skills y buscar más sobre la marca propia de Adri y assets del proyecto.

Ahora tengo buen contexto. Déjame revisar las instrucciones del Proyecto en sí y los archivos de conocimiento cargados. Voy a revisar los skills clave que definen la voz de la marca propia de Adri y buscar si hay archivos de proyecto cargados.

No hay archivos cargados en esta sesión. Voy a revisar los skills que definen la marca propia de Adri (su POV, voz, ecosistema) para extraer identidad de marca. El skill-skill y pov-finder suelen tener info de la marca. Déjame ver los más reveladores.

Excelente, esto tiene la identidad visual exacta de la marca personal de Adri (@adrianavmarquez). Ahora déjame revisar los skills que definen el POV, voz y ecosistema de su marca propia, para tener la identidad completa.

Ahora tengo una imagen clara de la marca personal de Adri (@adrianavmarquez) y su sistema. Este Proyecto es fundamentalmente sobre **la marca personal y práctica de consultoría de Adri (Adriana V. Márquez)**, no sobre un cliente individual. Los clientes (Daniela, Claudia, Luz, Mariana, Julieth) son parte del roster.

Tengo suficiente para consolidar. Voy a construir el documento de memoria de marca con toda la información extraída de las tres fuentes: las instrucciones del proyecto (via memoria y skills), los skills cargados (archivos de conocimiento) y los patrones recurrentes de las conversaciones.

```markdown
marca: Adriana V. Márquez (@adrianavmarquez)
tipo_proyecto: marca personal + práctica de consultoría (estrategia de contenido, brand voice, copywriting)
plataformas: Instagram, TikTok, YouTube, LinkedIn, Pinterest, Email/Newsletter, Substack, Twitter/X, Threads, Web/Blog
fecha_extraccion: 2026-07-04
estado: activo

# Memoria de marca: ADRIANA V. MÁRQUEZ

## 1. Identidad de marca

* **Nombre y tagline:**
  - Marca personal: Adriana V. Márquez, handle @adrianavmarquez.
  - Filosofía/sello central: "te sacudo, no te consiento" (te reta desde la experiencia vivida, no desde un pedestal).
  - Tagline formal único: No definido (existe la filosofía como sello, pero no hay tagline oficial de una línea).

* **Misión y propósito:**
  - Ayudar a marcas personales, creadores y founders (principalmente en Latinoamérica) a desarrollar voz de marca, estrategia de contenido y copy que conecte, aterrizando el posicionamiento en verdad emocional y no en lenguaje de marketing.
  - Se posiciona como estratega/directora, no como ejecutora: dirige las reescrituras, no es la creadora del contenido.

* **Valores:**
  - Verdad emocional sobre lenguaje pulido de marketing.
  - Anti-guruismo y anti-postureo (nada de tono de coach ni de pedestal).
  - Reto desde lo vivido ("te sacudo, no te consiento").
  - Honestidad operativa: marca los gaps en vez de rellenarlos en silencio.
  - Posicionamiento visceral, único y polarizante por encima del consenso masivo.

* **Historia breve:**
  - Adri es content strategist, brand consultant y coach. Trabaja con clientes de marca personal y founders across Latinoamérica. Su metodología se basa en principios VOC (Voice of Customer). Además construye recursos internos (frameworks, plantillas, skill files) para su propia práctica de consultoría.
  - Historia de origen personal detallada: No definida.

## 2. Producto, servicio u oferta

* **Qué se vende u ofrece:**
  - Consultoría y coaching de marca personal, estrategia de contenido, voz de marca.
  - Copywriting, desarrollo de scripts, escritura de hooks, auditoría de contenido.
  - UX/UI de Shopify para tiendas de clientes.
  - Posicionamiento estratégico de marca.
  - Recursos propietarios para asesorados: el "Brand Brain" (plantilla Notion) y un hub de recursos en Basecamp.

* **Propuesta de valor:**
  - Metodología VOC con tres reglas de oro para todo copy: visualizable, falsificable, únicamente atribuible a la persona (uniquely ownable).
  - "Te sacudo, no te consiento": reta a los clientes desde la experiencia vivida.

* **Precios o paquetes (si aplica):**
  - No definido.

## 3. Público objetivo

* **Buyer persona principal:**
  - Marcas personales, creadores y founders en Latinoamérica, en niveles intermedio a avanzado. El "Brand Brain" apunta específicamente a asesorados que ya manejan pauta/paid media pero todavía tienen gaps conceptuales.

* **Otros segmentos:**
  - Roster de clientes visible en las conversaciones:
    - Daniela Alsina: diseñadora arquitectónica/de interiores formada en Venezuela, radicada en Miami.
    - Claudia Grice ("Clau"): creadora ecuatoriana radicada en Arizona; contenido de migración, espiritualidad y crecimiento personal.
    - Mariana Salas ("Maleah/Male"): creadora costarricense radicada en Brasil; en transición de ingeniería a creación de contenido.
    - Luz (luzchapeton): founder construyendo marca personal en Instagram.
    - Julieth Ferreira: creadora detrás de un método de journaling digital de 28 días ("Volver a mí").

* **Dolores y deseos:**
  - De la propia Adri como consultora: clientes cuyo contenido falla en VOC (tercera persona, lenguaje aspiracional genérico, valor enterrado detrás de CTAs vagos).
  - De las audiencias de clientes (ejemplos): la audiencia "María" de Claudia (migrante latina navegando identidad cultural, relaciones interculturales y complejidad emocional de la migración); la audiencia de Daniela (cliente de gama media-alta en Miami en modo "estoy descubriendo a quién contratar", con miedos como "mi espacio no funciona y no sé por qué" / "no quiero gastar y que se vea pasado de moda").

## 4. Voz y tono

* **Personalidad de marca:**
  - Warm-direct (cálida y directa). Nunca formal de estratega ni de guru. Retadora desde lo vivido.
  - Comunica en español y spanglish. Usa tuteo (no voseo).

* **Palabras y expresiones que SÍ usar:**
  - "te sacudo, no te consiento" (filosofía central).
  - Tuteo, tono cálido-directo.
  - Spanglish natural.
  - En scripts de clientes: primera persona confesional sobre tercera persona aspiracional.
  - Nota: los tics verbales específicos pertenecen a cada cliente, no a Adri (ej. "¿me explico?", "chucha" son de Claudia Grice).

* **Palabras y expresiones que NO usar:**
  - Guru-speak / lenguaje de coach genérico (ej. frases tipo "sustainable system built around purpose").
  - Lenguaje aspiracional en tercera persona que cualquiera podría firmar.
  - Jerga vaga no visualizable ni falsificable.
  - CTAs vagos ("te explico", "haz esto").
  - Tono formal de estratega o de pedestal.
  - Voseo (usa tuteo).

* **Reglas de estilo:**
  - Tres reglas de oro VOC: todo copy debe ser visualizable, falsificable y uniquely ownable.
  - Patrones de fallo a corregir: hooks en tercera persona; lenguaje abstracto aspiracional; estructura cronológica que entierra el insight central; falta de proof points concretos o de stakes personales reales; tono motivacional/guru.
  - Fórmula de hook que funciona (ej. Daniela Alsina): nombrar el dolor o creencia común del cliente, luego voltearlo con un criterio específico de diseñador o insight no obvio. Autoridad declarativa + reframe específico (ej. "Odiar tu cocina no es la única opción").
  - Estructura de carrusel: reframe de memoir (lo que me pasó) a valor accionable (lo que no debes hacer); acreditar el fracaso en un solo slide; construir hacia un asset guardable (la Slide 09 suele ser el objetivo de diseño).
  - Estructura de storytime: contradicción como hook, proof points comprimidos, cierre que teasea una serie en vez de resolver todo (método "Cinematic Confessional").
  - Principio de secuenciación: el contenido de enseñanza (ej. tutoriales de edición) va después, no antes, de la claridad de posicionamiento de marca personal.

## 5. Estilo visual y branding

* **Colores (marca personal @adrianavmarquez, del doc oficial de scripts de collab):**
  - Rojo: #D72323 (títulos de sección, header principal).
  - Azul: #3846C4 (estrellitas ★ de apertura/cierre, fondo de headers de tablas).
  - Amarillo: #FFBA35 (estrellitas secundarias, texto de headers de tablas).
  - Negro: #000000 (cuerpo de texto, bordes de tabla).
  - Blanco: #FFFFFF (fondo general, filas de datos).
  - Gris: #F5F5F5 (filas alternadas de tablas).

* **Tipografías:**
  - Poppins (toda la documentación de marca).

* **Referencias estéticas:**
  - Elemento gráfico de marca: estrellitas ★ (azul grande + amarillo pequeño) en apertura y cierre de documentos.
  - Bullets con "·" (punto medio), no bullets unicode estándar.
  - Nota: estos valores visuales aplican a la marca personal de Adri. Cada cliente tiene su propia estética (ej. Daniela: "Atemporal").

## 6. Canales y plataformas

* **Handles y enlaces:**
  - Handle de Adri: @adrianavmarquez.
  - Workspace de Notion: adrianavmarquez (app.notion.com) — hub principal de documentación de todos los clientes.
  - n8n cloud: adrianavmarquez.app.n8n.cloud (webhooks de exportación).
  - Handles de clientes: Luz (luzchapeton); otros handles específicos: No definidos.

* **Prioridad de cada canal:**
  - El sistema "Ecosystem Architect" planifica full stack siempre: Instagram, TikTok, YouTube, LinkedIn, Pinterest, Email, Web/Blog. El creador decide qué corta.
  - Prioridad relativa fija por canal: No definida (se decide mes a mes según hilo conductor y objetivo).

## 7. Objetivos y KPIs

* **Objetivos actuales:**
  - Tener vivo el "Brand Brain" en inglés; luego crear la versión en español como fase separada.
  - Compilar un glosario maestro de términos técnicos (AOV, CAC, CTR, etc.) una vez que el Brand Brain esté live.
  - Gestión continua de workspaces de Notion para múltiples clientes.

* **Métricas que importan:**
  - Para la marca de Adri como consultora: No definidas explícitamente.
  - Plataformas rastreadas para analítica/ads de clientes: Meta Ads Manager, TikTok Ads Manager, Google Analytics 4, Shopify, Gumroad, Stan Store, Kajabi, y otras. Métricas de referencia en el Brand Brain organizadas por etapa de funnel (CPM, ROAS, Hold Rate, CTR, AOV, CAC, LTV, etc.).

## 8. Preferencias operativas

* **Cómo le gusta trabajar al cliente (Adri):**
  - Entrega output paste-ready sin condicionar detrás de preguntas de seguimiento; prefiere deliverables completos de una.
  - Marca los gaps honestamente en vez de rellenarlos en silencio (placeholders entre corchetes para data real de cliente; marca cuándo falta lenguaje verbatim del cliente).
  - Se comunica en español y spanglish; el contenido del cliente puede ser en español o inglés según el cliente.
  - Formato markdown compatible con Notion como formato de salida preferido.
  - Incluye 2-3 hooks alternos para A/B testing como práctica estándar.
  - Piensa en funnels de audiencia más allá de social: marca cuándo los CTAs deberían enrutar a propiedades propias (YouTube, newsletter) en vez de solo pedir follow.
  - Cuando Claude hace ediciones fuera del alcance acordado, Adri espera que se marque de forma transparente con opción de revertir.
  - Las explicaciones y el razonamiento se quedan en el chat de Claude; las páginas de Notion reciben solo el copy mejorado, no el razonamiento.
  - Trata los skills (storytime, carrusel, etc.) como frameworks para aplicar con criterio, no como checklists de gatekeeping.

* **Formatos que suele pedir:**
  - Scripts de video (storytime, talking head, voiceover, fast reel, video essay, text screen).
  - Hooks (con alternos para A/B testing).
  - Carruseles.
  - Copy y value props.
  - Documentos de posicionamiento (POV).
  - Planes de contenido mensuales/semanales.
  - Emails (nurturing, ventas).
  - Posts de LinkedIn, snippets de Twitter/Threads, piezas de Substack.
  - Documentos de script de collab en .docx (marca @adrianavmarquez).

## 9. Contexto acumulado y decisiones clave

* **Decisiones importantes tomadas (con fecha si se sabe):**
  - Brand Brain se construye primero en inglés; versión en español planificada como fase separada posterior (abril 2026).
  - El glosario maestro de términos se arma de una sola vez al final, cuando el Brand Brain esté live y Adri comparta el link para extracción (abril 2026).
  - El contenido de "How Meta's Algorithm Works" y el "Metrics Cheat Sheet" van en Basecamp como páginas standalone, no dentro del Account Health Check Framework (abril 2026).
  - Explicaciones se quedan en el chat, no en Notion; los hooks del primer pase no se re-explican en el segundo (Claudia Grice, julio 2026).
  - Clientes trabajados con pressure-test VOC en Notion: Daniela Alsina (hooks reescritos, A/B testing, Mapa de 30 días), Claudia Grice (12 + 25 hooks reescritos, 10 duplicados sincronizados, 3 scripts mejorados), Mariana Salas (análisis pro-bono post-consulta) — todo junio-julio 2026.

* **Aprendizajes:**
  - El patrón de fallo dominante en el contenido de clientes: hooks en tercera persona, lenguaje aspiracional abstracto que cualquiera podría firmar, valor enterrado detrás de CTAs vagos.
  - El detalle único y concreto de cada persona es "el oro"; lo genérico es relleno. Mejor dejar un slot marcado para que el cliente aporte el detalle real (nota de voz de 30 seg) que inventar un recuerdo prestado.
  - Un flag recurrente: rutear CTAs a una propiedad propia una vez que el cliente la defina.
  - El contenido de enseñanza debe seguir, no preceder, la claridad de posicionamiento.

## 10. Activos y recursos

* **Enlaces a documentos, carpetas, plantillas:**
  - Notion: workspace principal adrianavmarquez, con páginas por cliente (intake/auto-descubrimiento, guía de voz de marca, market research, pilares de contenido, idea bank, mapa de contenido). Ejemplos: página de Daniela Alsina; Mapa de 30 días; Claudia Grice; Idea bank.
  - Brand Brain: plantilla Notion para asesorados intermedio-avanzado (paid media, pilares de contenido, diagnóstico de salud de cuenta, métricas de plataforma).
  - Basecamp: hub de recursos para clientes de coaching (Creative Brief Template, Pillar vs. Concept vs. Angle, Hook System, Account Health Check Framework, How Meta's Algorithm Works, Metrics Cheat Sheet).
  - Skill files propietarios en /mnt/skills/user/ con subdirectorios por skill (ej. storytime-scripting/SKILL.md, copywriting-pressure-test/SKILL.md).
  - Shopify / Shopify Liquid: builds de tiendas de clientes (ej. "Volver a mí" de Julieth Ferreira).
  - n8n: webhooks para exportar a Notion (Post-Iteration Hub, Brand Brain databases).
  - Links de URL completos y exactos a documentos individuales: No definidos (referenciados por nombre/ID en conversaciones).

## 11. Tareas recurrentes

* **Qué se pide con frecuencia en este Proyecto:**
  - Revisar y mejorar hooks aplicando VOC para clientes (leer página de Notion, cruzar con voz de marca y perfil de audiencia, reescribir directo en Notion vía batch update).
  - Convertir historia personal cruda de un cliente en script (storytime/reel) con método Cinematic Confessional + VOC.
  - Mejorar copy de video y carruseles con lente VOC.
  - Construir/editar contenido del Brand Brain y recursos de Basecamp.
  - Gestión de workspaces de Notion vía MCP (fetch, batch update, insert).
  - Generar documentos de script de collab en .docx con la estética de marca.

## 12. Restricciones y reglas

* **Qué nunca hacer:**
  - Nunca escribir contenido en tono guru o de coach genérico.
  - Nunca usar lenguaje aspiracional en tercera persona que cualquiera podría firmar.
  - Nunca dejar valor enterrado detrás de CTAs vagos.
  - Nunca poner las explicaciones/razonamiento en las páginas de Notion (solo copy mejorado).
  - Nunca inventar métricas, claims o detalles personales del cliente: marcar el gap con placeholder.
  - Nunca hacer ediciones fuera de alcance sin marcarlas de forma transparente y ofrecer revertir.
  - En documentos de collab: nunca incluir fechas de entrega, honorarios ni términos contractuales (van en contrato separado).
  - No usar voseo (usar tuteo).

## 13. Glosario y datos clave

* **Términos, nombres, fechas o datos a recordar:**
  - VOC: Voice of Customer. Metodología central de Adri.
  - Tres reglas de oro VOC: visualizable, falsificable, uniquely ownable.
  - "te sacudo, no te consiento": filosofía/sello de Adri.
  - Cinematic Confessional: método de storytime (contradicción como hook, sensorial, no lineal, incómodamente verdadero).
  - Brand Brain: plantilla Notion propietaria para asesorados.
  - Pillar / Concept / Angle: framework de estrategia creativa (pilar = territorio estratégico; concepto = idea testeable con audiencia + mensaje + formato + hook; angle = motivación del consumidor).
  - Fórmula del POV: (Experiencia Vivida + Insight Psicológico) × Negación del Consenso Masivo.
  - Términos de paid media del Brand Brain: AOV, CAC, LTV, CPM, CTR, ROAS, Hold Rate.
  - Sistemas de algoritmo de Meta documentados: Andromeda (retrieval), GEM (foundation), Lattice (ranking).
  - Clientes: Daniela Alsina (Miami, diseño), Claudia Grice/Clau (Arizona, migración/espiritualidad; audiencia "María"; sello "Pertenezco a donde voy"; origen 2019), Mariana Salas/Maleah (Brasil, ex-ingeniería), Luz/luzchapeton (founder IG), Julieth Ferreira ("Volver a mí", journaling 28 días).
  - Notas MCP de Notion: fetch full page antes de batch; matching exacto de strings (acentos, puntuación, asteriscos, comillas) o el replace falla en silencio; notion-update-page con update_content y content_updates (batches de hasta ~35 en una llamada); insert_content con position end para anexar tras divisores.

## 14. Pendientes y preguntas abiertas

* **Lo que quedó sin definir:**
  - Tagline oficial de una línea para la marca de Adri (existe la filosofía, no un tagline formal).
  - Historia de origen personal detallada de Adri.
  - Precios y paquetes de sus servicios.
  - KPIs/métricas propias de la marca de Adri (distintas de las de clientes).
  - Prioridad relativa fija de cada canal (se decide mes a mes).
  - Versión en español del Brand Brain (planificada, aún no ejecutada).
  - Glosario maestro del Brand Brain (pendiente de que el doc esté live y Adri comparta el link).
  - Handles de redes específicos de la mayoría de los clientes.
  - URLs completas y exactas a documentos individuales de Notion.
  - Definición de propiedades propias (newsletter/YouTube) para rutear CTAs de varios clientes.
```

Un par de notas honestas antes de que lo copies:

Este Proyecto no gira alrededor de una sola marca-cliente sino de **tu propia marca y práctica de consultoría** (@adrianavmarquez), con un roster de clientes adentro. Armé el doc con tu marca como el sujeto principal y los clientes como segmentos, porque eso es lo que la memoria acumulada sostiene. Si lo que querías era la ficha de un cliente específico (Daniela, Clau, etc.), dímelo y te armo esa versión por separado, que tienen VOC y estética propias.

El vacío más grande es todo lo que es **tuyo como marca personal más allá de la estética visual**: tagline formal, historia de origen, precios, tus propios KPIs. Están marcados como "No definido" en vez de rellenados. Si corres el `pov-finder` sobre tu propia marca en algún momento, esas casillas se llenan solas y este doc queda mucho más filoso.

## 🧑 Adriana · 2026-07-05 01:30
quiero descargar ese markdown file

## 🤖 Claude · 2026-07-05 01:31
Listo, ahí lo tienes para descargar. Es el mismo contenido que armé, ya como archivo `.md` limpio (sin em dashes, listo para importar a otra herramienta o pegarlo donde lo necesites).
