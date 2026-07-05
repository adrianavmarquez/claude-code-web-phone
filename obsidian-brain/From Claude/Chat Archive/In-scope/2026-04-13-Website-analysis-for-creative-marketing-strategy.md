---
title: "Website analysis for creative marketing strategy"
source: claude.ai-chat
created: "2026-04-13 00:36"
summary: "**Conversation Overview**  The person conducted an extensive series of website audits across seven sites, requesting analysis from two distinct professional perspectives for each: first as a creative marketing strategist, then as a professional UX/UI designer. The sites analyzed spanned multiple business models and markets: three Hispanic creator education brands (creativemilkshake.com, andreabadillo.com, danischulzinc.com), one English-language AI video course landing page (ohneis652.com/landing), two digital product stores (filmkid.com, andrewsbodega.com/creatorblueprint), with the session ending mid-series on the Creator Blueprint UX audit.  Throughout the conversation, Claude used a custom visualization tool to render structured audit reports with scored scorecards, section-by-section breakdowns, color-coded issue flags, comparison tables, funnel maps, and priority fix lists. After completing the first three site pairs, the person requested that Claude synthesize all learnings into a reusable framework covering what to do and what not to do from both the marketing strategist and UX/UI designer perspectives. Claude created this as a saved skill file at `/mnt/skills/user/website-framework/SKILL.md` and saved key audit findings to memory. The framework covered: defining whether a site should convince vs. confirm based on traffic temperature, building visible value ladders, proof hierarchy, tone coherence, and email capture strategy on the marketing side; and HTML-first content, pricing visibility, accordion patterns, sticky CTAs, WCAG compliance (2.2.2, 1.1.1, 1.3.1, 2.5.5), platform-specific limitations, and image format optimization on the UX/UI side.  Key domain terminology used throughout: LUT, PowerGrade, SFX pack, DaVinci Resolve, value ladder, low-ticket, high-ticket, DOM duplication, aria-hidden, aria-expanded, prefers-reduced-motion, LCP, Core Web Vitals, WCAG AA, srcset, AVIF/WebP, focus trap, accordion pattern, sticky CTA, before/after slider, proof social, email capture, lead magnet, preselling, and platform comparisons across Kajabi, Wix, Framer, Shopify, and custom code builds. The person demonstrated consistent interest in comparing sites against each other and against the compiled framework, escalating from individual audits to cross-site pattern recognition. A recurring finding across all sites was that none had pricing in real HTML — identified as the single most universal and correctable UX gap. The person showed particular interest in the Hispanic creator education market (Andy Badillo, Dani Schulz) as well as English-language digital product creators (Ohneis, Filmkid, Andrew's Bodega), suggesting professional work or client involvement in the creator economy space across both language markets."
messages: 28
claude_uuid: "bfdd5abd-3f07-4adf-8c38-a08527dd4617"
tags: [claude, chat, archive]
---
# Website analysis for creative marketing strategy

> **Conversation Overview**

The person conducted an extensive series of website audits across seven sites, requesting analysis from two distinct professional perspectives for each: first as a creative marketing strategist, then as a professional UX/UI designer. The sites analyzed spanned multiple business models and markets: three Hispanic creator education brands (creativemilkshake.com, andreabadillo.com, danischulzinc.com), one English-language AI video course landing page (ohneis652.com/landing), two digital product stores (filmkid.com, andrewsbodega.com/creatorblueprint), with the session ending mid-series on the Creator Blueprint UX audit.

Throughout the conversation, Claude used a custom visualization tool to render structured audit reports with scored scorecards, section-by-section breakdowns, color-coded issue flags, comparison tables, funnel maps, and priority fix lists. After completing the first three site pairs, the person requested that Claude synthesize all learnings into a reusable framework covering what to do and what not to do from both the marketing strategist and UX/UI designer perspectives. Claude created this as a saved skill file at `/mnt/skills/user/website-framework/SKILL.md` and saved key audit findings to memory. The framework covered: defining whether a site should convince vs. confirm based on traffic temperature, building visible value ladders, proof hierarchy, tone coherence, and email capture strategy on the marketing side; and HTML-first content, pricing visibility, accordion patterns, sticky CTAs, WCAG compliance (2.2.2, 1.1.1, 1.3.1, 2.5.5), platform-specific limitations, and image format optimization on the UX/UI side.

Key domain terminology used throughout: LUT, PowerGrade, SFX pack, DaVinci Resolve, value ladder, low-ticket, high-ticket, DOM duplication, aria-hidden, aria-expanded, prefers-reduced-motion, LCP, Core Web Vitals, WCAG AA, srcset, AVIF/WebP, focus trap, accordion pattern, sticky CTA, before/after slider, proof social, email capture, lead magnet, preselling, and platform comparisons across Kajabi, Wix, Framer, Shopify, and custom code builds. The person demonstrated consistent interest in comparing sites against each other and against the compiled framework, escalating from individual audits to cross-site pattern recognition. A recurring finding across all sites was that none had pricing in real HTML — identified as the single most universal and correctable UX gap. The person showed particular interest in the Hispanic creator education market (Andy Badillo, Dani Schulz) as well as English-language digital product creators (Ohneis, Filmkid, Andrew's Bodega), suggesting professional work or client involvement in the creator economy space across both language markets.

## 🧑 Adriana · 2026-04-13 00:36
i need you to analize this whle website and extract its sections components, and why it works from a creative marketing stategist: https://www.creativemilkshake.com/

## 🤖 Claude · 2026-04-13 00:39
Now I have everything I need. Let me build a thorough creative marketing analysis.

There's the full breakdown. Here's the TL;DR on what to take away from it strategically:

The strongest moves on this site are things you can steal for your own positioning work with clients:

**The "system" reframe.** They don't sell ads, they sell a Growth Creative System. Whatever you're building for clients or for yourself, naming it as a system vs. a service changes the perceived value instantly.

**Metric vocabulary as audience filter.** CPA, CVR, CAC in the headline tells the right buyer "you're home" and tells the wrong buyer "exit here." It's not trying to be legible to everyone, which is exactly right for B2B.

**The verifiable handle move.** Putting @handles on testimonials instead of generic names is something almost nobody does and it costs nothing. It turns social proof from "claim" to "fact."

**Metric-first case study headlines.** "65% lower cost per mobile registration" before the brand name. The number earns the read. This is the same structure as a strong direct response hook: lead with the transformation, not the actor.

The biggest gap is the one that's most ironic: an agency that sells creative produced one of the least creative websites in their category. Technically solid, emotionally flat. If you ever build a positioning page for your own work, that's the white space to attack.

## 🧑 Adriana · 2026-04-13 00:41
now i need you to analize it from a expert UX/UI designer.

## 🤖 Claude · 2026-04-13 00:43
The contrast between both audits is telling. From the marketing lens, this site is doing real strategic work. From the UX lens, it has a broken credibility metric on the hero, an auto-scroll carousel that violates accessibility standards, and a core section that likely collapses on mobile.

The most ironic finding: the stats counter showing "1+ ads delivered monthly" and "1% CPA drop" is the single worst element on the page, and it sits above the fold on the section that's supposed to be the most persuasive. An agency selling performance creative cannot afford a broken performance metric in its first visual impression.

The Framer build is also the underlying culprit behind several issues at once: the duplicate DOM sections (which screen readers encounter 2-3 times), the responsive breakpoints baked into HTML rather than CSS, and the general constraint that the system diagram is probably a static image that can't adapt gracefully to smaller viewports.

If you ever use this as a reference or competitive analysis for a client conversation, the lesson is clean: great information architecture and great UX are not the same thing. You can have a smart conversion strategy and still have a technically broken site.

## 🧑 Adriana · 2026-04-14 01:22
i need you to analize this whle website and extract its sections components, and why it works from a creative marketing stategist:
https://www.andreabadillo.com/

## 🤖 Claude · 2026-04-14 01:25
Tengo todo lo que necesito. Voy al análisis completo.

El contraste con Creative Milkshake es la cosa más interesante de este análisis.

Creative Milkshake tiene que convencer desde cero: el tráfico llega frío, sin contexto, y el sitio hace todo el trabajo de autoridad y prueba. andreabadillo.com opera en el escenario opuesto: quien llega ya la sigue, ya la conoce, ya le tiene confianza. El sitio solo tiene que no romper esa confianza y facilitar la compra.

El movimiento más inteligente que hace el sitio de Andy es el orden emocional antes de credencial. Dice "amante de las redes sociales" antes de decir "2M de seguidores." Para otro tipo de marca, eso sería un error. Para una marca personal dirigida a creadores que quieren ser como ella, es exactamente el orden correcto: primero te conectas con la identidad, luego la credencial la refuerza, no al revés.

Lo que más me llama la atención como gap: no hay captura de email en el flujo principal. Hay una pop-up de "Free Challenge" en el código del sitio pero no parece estar activa de forma prominente. Para quien llega y todavía no está listo para comprar, el sitio básicamente los pierde. Esa es la fuga más costosa considerando el volumen de tráfico que probablemente genera su audiencia de 2M.

## 🧑 Adriana · 2026-04-14 02:20
now i need you to analize it from a expert UX/UI designer.

## 🤖 Claude · 2026-04-14 02:23
El hallazgo más interesante de este audit es que el problema central de accesibilidad y performance tiene una sola causa raíz: la decisión de diseñar en Canva y exportar secciones enteras como PNG.

Esa decisión tiene una lógica real: garantiza que lo que ves en el sitio sea exactamente lo que diseñaste, sin que Kajabi o el navegador rompan nada. Es una solución de control visual. Pero el precio es alto: el contenido más importante del sitio (la bio, los nombres de cursos, los testimonios, el headline del hero) es auditivamente invisible, no indexable por Google, no escalable por accesibilidad, y más lento de cargar que texto HTML puro.

El fix más impactante con menor esfuerzo es el que mencioné en P1: reexportar todos los PNGs a WebP. No cambia nada del diseño visual, no requiere tocar Kajabi en profundidad, y el impacto en velocidad de carga mobile puede ser inmediato y directo sobre conversión.

El segundo fix que yo priorizaría, más allá del scorecard, es convertir el alt text de las imágenes a texto real descriptivo. No "ABCO_HEADER.png." Sino el contenido que transmite esa imagen. Es una tarde de trabajo en Kajabi y convierte el sitio de invisible a funcional para un porcentaje de la audiencia que hoy literalmente no puede usar el sitio.

## 🧑 Adriana · 2026-04-14 02:31
i need you to analize this whle website and extract its sections components, and why it works from a creative marketing stategist:
https://www.danischulzinc.com/

## 🤖 Claude · 2026-04-14 02:34
Perfecto, tengo todo lo que necesito. La página de TCF especialmente es un texto estratégicamente denso que vale mucho analizar.

La diferencia entre este y los dos anteriores es de madurez de negocio, no de marca personal.

Andrea Badillo tiene el sitio de una creadora con audiencia enorme que construyó una tienda de productos. Dani Schulz tiene el sitio de un negocio educativo que usa una marca personal como motor de adquisición. La distinción importa porque las decisiones de diseño son completamente distintas en cada caso.

El elemento que más me llamó la atención estratégicamente es la lista de los 50+ nichos en la landing de TCF. Es la eliminación de objeción de nicho más completa que he visto en un sitio latinoamericano de educación digital. "Venta de bombas de agua" y "ASMR" en la misma lista. Lo que eso comunica es: no hay excusa para que tu industria sea demasiado específica. Esa lista es más persuasiva que cualquier testimonial porque opera en el nivel de "no hay razón para que esto no funcione para mí."

Lo que falta, y es la misma brecha que tiene Andrea Badillo aunque por razones diferentes, es orientación para tráfico frío. Ambos sites asumen que quien llega ya conoce a la creadora. Cuando eso deja de ser cierto a escala, o cuando quieren hacer paid media serio, esa ausencia de contexto inicial empieza a costar.

## 🧑 Adriana · 2026-04-14 02:35
now i need you to analize it from a expert UX/UI designer.

## 🤖 Claude · 2026-04-14 02:38
Lo más interesante de este audit comparado con los dos anteriores es que aquí el problema no es falta de contenido ni falta de estructura: es demasiado contenido sin diseño de consumo.

andreabadillo.com tiene el problema opuesto: poco contenido HTML real, casi todo en imágenes. danischulzinc.com tiene el texto correcto, en HTML real, pero desplegado sin arquitectura de lectura. La landing de TCF es extraordinariamente completa desde el marketing, y esa misma completitud la hace pesada desde el UX.

El fix que yo priorizaría sobre todos los demás, antes que cualquier cosa de accesibilidad o de plataforma, es el accordion en el currículum semana a semana. Ese bloque solo separa el CTA de compra por decenas de pantallas de scroll en mobile. Es el activo más persuasivo de la landing convertido en barrera. Con accordion y semana 1 abierta por defecto, el visitante que quiere explorar lo hace, y el que ya decidió baja directo al precio sin fricción.

Y la nota sobre AVIF es real: Wix hace automáticamente algo que los equipos de Kajabi y Framer tienen que hacer a mano. Es una ventaja de plataforma silenciosa que pocos notan.

## 🧑 Adriana · 2026-04-14 02:47
Ok quiero que hagas un framework de lo aprendido de estas webs, que NO hacer, que SI hacer. primero como estratega digital, y luego como UX/UI designer

## 🤖 Claude · 2026-04-14 02:50
Hay una cosa que me parece que vale la pena nombrar fuera del framework porque no cabe en ninguna tarjeta de regla.

Los tres sitios, vistos juntos, ilustran tres niveles de madurez de negocio que se corresponden directamente con qué tan deliberado es el diseño del sitio. Creative Milkshake ya llegó al nivel donde el sitio tiene que hacer trabajo real de ventas con tráfico frío, y lo construyeron como argumento. Andy Badillo está en el nivel donde la audiencia ya existe y el sitio es una extensión natural, pero sin la arquitectura para crecer más allá de ese tráfico. Dani Schulz tiene el sistema más completo de los tres, pero el nivel de densidad que implica haber construido tanto contenido de producto comienza a pesar sobre la experiencia.

La conclusión que más me sirve personalmente, si tuviera que quedarme con una sola cosa del framework: el error más caro que cometen los tres sitios, sin excepción, es que ninguno tiene el precio en HTML real. Es el elemento que más directamente impacta la decisión de compra, y los tres lo tienen en imagen o escondido detrás de un clic. Eso me parece el gap más universalmente ignorado en sitios de educación digital hispanohablante, y el más fácil de corregir.

## 🧑 Adriana · 2026-04-14 03:21
Crea un skill con toda esta informacion del framework y adicionalmente guarda lo que analizaste de los 3 sites a la tu memoria.

## 🤖 Claude · 2026-04-14 03:23
Voy a hacer las dos cosas en paralelo: crear el skill y guardar en memoria. Empiezo por la memoria para que quede registrado mientras construyo el skill.

Memoria guardada. Ahora creo el skill.

Todo listo. Esto es lo que quedó guardado:

**Skill creado:** `/mnt/skills/user/website-framework/SKILL.md` con 240 líneas que incluyen las dos partes del framework completo (estrategia + UX/UI), la tabla comparativa de los tres sitios, la checklist de publicación, las notas de plataforma, y los dos mantras. Se activará automáticamente cuando pidas auditar o dar feedback sobre sitios web, marcas personales o negocios de creadores.

**Memoria guardada:** Dos entradas nuevas en tu memoria con los hallazgos clave de los tres audits y la referencia al skill, para que si en cualquier conversación futura mencionas alguno de los tres sitios, ya tenga el contexto completo.

El único error que ninguno de los tres sitios resolvió bien, que quedó como la conclusión más importante del framework: el precio siempre en imagen, nunca en HTML. Es el gap más universalmente ignorado en educación digital hispanohablante y el más fácil de corregir.

## 🧑 Adriana · 2026-04-15 01:44
analiza esta landing page como un professional creative marketing strategist: https://www.ohneis652.com/landing

## 🤖 Claude · 2026-04-15 01:47
Tengo todo. El contenido de la landing y el framework para aplicarlo. Voy al análisis.

La conclusión que más vale la pena nombrar fuera del reporte: esta landing tiene la paradoja más interesante de los cuatro sitios analizados.

Su mecanismo diferenciador, el job board de overflow clients, es simultáneamente lo más persuasivo y lo más frágil de toda la landing. Si el buyer llega creyendo que esos proyectos son reales, la decisión de compra es casi automática: un trabajo de $1,500 paga el curso. Pero si el buyer activa su pensamiento crítico y se pregunta "¿cómo es que Ohneis tiene overflow de proyectos de wedding videography, gaming content, brewery tours y architecture tours todos al mismo tiempo?", la lista entera colapsa.

Comparado con los tres sitios hispanohablantes que analizamos antes, este es el que tiene el copywriting más sofisticado pero el foundation de credibilidad más delgado. Dani Schulz tiene "+20,000 clientes en 5 años" — eso es difícil de fabricar. Ohneis tiene una lista de proyectos sin nombre de cliente, sin fecha, sin descripción real. El gap entre la ambición del mecanismo y la prueba que lo sostiene es el problema central a resolver antes de escalar esta landing con paid traffic.

## 🧑 Adriana · 2026-04-16 03:57
ahora como un ux/ui designer profesional

## 🤖 Claude · 2026-04-16 04:00
La cosa más importante de señalar después del scorecard: esta es la primera landing de las cuatro que parece construida con código real en lugar de sobre una plataforma de arrastrar y soltar. Eso se nota directamente en los scores, especialmente en interacción (8.5) y arquitectura (8). La libertad técnica produce mejores decisiones de UX cuando la persona que diseña sabe lo que está haciendo.

El sticky CTA con el precio incluido ("Get Access Now - $999" siempre visible) es el patrón más correcto de los cuatro sitios y el fix que más veces recomendé en los audits anteriores. Aquí está implementado por defecto. Eso solo ya justifica que esta landing convierta mejor que las tres anteriores en términos de fricción de compra.

Pero el job board sin filtros es la paradoja más costosa desde UX: el activo más persuasivo de la landing es también el componente que más cansa al usuario antes de llegar al precio. 60 filas de datos que no puedes explorar activamente señalan que fueron puestas para verse bien, no para usarse de verdad. Un filtro de tres categorías y un rango de precio en mobile no es un rediseño: es una tarde de trabajo que convierte el board de decoración a herramienta de decisión real.

## 🧑 Adriana · 2026-04-16 04:04
ahora te mostrare dos de productos digitales low ticket no servicios:
i need you to analize this whle website and extract its sections components, and why it works from a creative marketing stategist:
https://filmkid.com/?srsltid=AfmBOopcV3PlxomOPrsxYqLz-0JPbb_asUNUvtY0XKOzHex1qNsVH2tu

## 🤖 Claude · 2026-04-16 04:07
Tengo todo lo que necesito del site completo. Ahora el análisis.

La lección más importante de Filmkid que aplica a cualquier otro sitio del análisis: **el producto que se demuestra a sí mismo no necesita que nadie lo defienda.**

Los samples de audio reproducibles antes del precio, y el before/after slider que el usuario controla, hacen algo que ninguno de los otros cinco sitios puede hacer: eliminan la objeción de calidad antes de que el visitante siquiera la formule. No hay copy en el mundo que reemplace escuchar el producto o ver la transformación en tiempo real.

La otra cosa que vale nombrar: este sitio resuelve correctamente el problema de la audiencia preexistente. Los cinco sitios anteriores construyen argumentos de por qué el creador merece confianza (credenciales, números, testimonios de autoridad). Filmkid no necesita ese argumento porque el tráfico llega después de ver el efecto en un reel de Instagram. La venta ya empezó ahí. El sitio solo tiene que confirmarla y facilitarla en el menor número de clics posible. El homepage de cuatro banners hace exactamente eso.

El gap de email capture es el más urgente de los tres. Para un modelo de $29-$89 por transacción, la lista de email es el único activo que permite anunciar un nuevo pack de SFX a 10,000 compradores anteriores y hacer $50,000 en un día sin pagar un peso en ads.

## 🧑 Adriana · 2026-04-16 04:37
now like an professional ux/ui designer:

## 🤖 Claude · 2026-04-16 04:41
Lo más importante de señalar aquí, comparando con todos los sitios anteriores: Filmkid es el primero del análisis donde la plataforma trabaja a favor del diseño en lugar de en contra.

Shopify hace tres cosas automáticamente que ninguno de los otros cinco builders hacía sin intervención manual: sirve el tamaño de imagen correcto por viewport (srcset), entrega un checkout nativo accesible y testeado en millones de transacciones, y genera HTML semántico real sin DOM duplicado. Esas tres ventajas de plataforma son el equivalente a empezar el partido 3-0.

El problema más irónico del sitio es Scribble. Es el producto de suscripción del catálogo (el de mayor LTV potencial porque genera ingreso recurrente a $15/mes o $119/año), y es la única página del sitio donde el HTML inicial está completamente vacío de contenido. Google ve una página en blanco. Un lector de pantalla ve "a a a a a". El producto de mayor valor estratégico es el más invisible técnicamente. Eso es lo primero que yo arregaría, antes que cualquier cosa de accesibilidad en los players.

## 🧑 Adriana · 2026-04-16 04:51
i need you to analize this whle website and extract its sections components, and why it works from a creative marketing stategist:
https://www.andrewsbodega.com/creatorblueprint/home

## 🤖 Claude · 2026-04-16 04:55
El patrón más interesante que sale de comparar estos dos productos digitales low-ticket entre sí: Filmkid y Andrew's Blueprint resuelven el problema de credibilidad de formas opuestas.

Filmkid deja que el producto se demuestre solo: el buyer escucha el sample antes de ver el precio y la pregunta de credibilidad desaparece. Andrew pone la credibilidad en el diseño del sitio mismo (que es visualmente impecable) pero la deja sin verificación en texto. El resultado es que Filmkid convierte con fricción de credibilidad casi cero, y Andrew depende de que el visitante ya confíe en él desde antes de llegar.

La afirmación de $30k/mes es el elemento más polarizante de los siete sitios. Para el visitante que ya sigue a Andrew y sabe que es real, esa frase es el punto de cierre de la decisión. Para cualquier visitante que llega nuevo, sin foto de Andrew, sin número de audiencia, sin handle de YouTube, esa frase suena exactamente como todas las afirmaciones de ingresos de cursos de internet que el buyer ya ha aprendido a ignorar.

El fix más de alto impacto con menos esfuerzo: una sección de 3 líneas con foto de Andrew, el número de sus suscriptores de YouTube, y una marca con la que colaboró. Con eso, el $30k/mes pasa de afirmación a contexto.

## 🧑 Adriana · 2026-04-16 13:44
now like an professional ux/ui designer:

## 🤖 Claude · 2026-04-16 13:47
La conclusión más importante después de siete sitios analizados en Framer, Kajabi, Wix, custom code y Shopify: el gap entre calidad visual y calidad técnica más grande del análisis está aquí, en el Creator Blueprint. Es la landing que más impresiona visualmente y la que tiene el score de accesibilidad más bajo junto a Creative Milkshake.

Eso no es una coincidencia. Framer como plataforma está diseñado para maximizar el control visual y las animaciones sofisticadas. El DOM triplicado por breakpoints es la consecuencia directa de esa filosofía: Framer renderiza tu diseño de desktop, tablet y mobile en el mismo HTML y decide cuál mostrar por CSS. Es una solución que funciona perfectamente para ojos que ven, y es un desastre para lectores de pantalla que procesan texto.

El fix más urgente y más impactante sigue siendo el mismo que recomendé en Creative Milkshake y que aplica a cualquier sitio Framer: `aria-hidden="true"` en las variantes de breakpoint inactivas. Una tarde de trabajo en el custom code de Framer. Sin ese fix, cualquier usuario de VoiceOver lee el titular del curso tres veces antes de llegar a la descripción, y la experiencia auditiva es básicamente inusable.

Y la nota de Outseta vs. Stripe merece quedarse en el radar: para una audiencia de creators anglohablantes que ya están habituados a ver el logo de Stripe en cada checkout que han completado, un modal de `andrew-paul.outseta.com` es un momento de fricción que Stripe no genera. No es un error grave, pero en un precio de $299 donde el visitante ya está evaluando si confiar lo suficiente para dejar su tarjeta, cada señal de confianza cuenta.
