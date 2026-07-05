---
title: "Emergent x2 collaboration scripts"
source: claude.ai-chat
created: "2026-06-14 17:08"
summary: "**Conversation overview**  This was a focused build session with Adriana V. Márquez (@adrianavmarquez), a founder-content creator who builds educational tools and sponsored video content under her brand Creatividad². The session picked up mid-project from a prior transcript and had one primary goal: finalize the interactive '¿cuánto cobrar?' (rate calculator) web app as a branded HTML wizard, then generate a comprehensive Emergent AI prompt spec so the tool can be rebuilt as a fully functional app with real email capture.  The session moved through three sequential tasks. First, Adriana chose the layout configurations for two animated GIFs (a calculating cat and a smug corgi) from a set of four wireframe mockup options Claude generated per page. She selected portada C (cat GIF as a corner sticker on the start screen, slightly rotated, no border) and resultados B (corgi beside the price, side by side, flexible left column for price and right column for the GIF). Second, Claude implemented both GIF selections into the live HTML file along with an email capture card at the end of the results screen — after the number reveals, never gated — using her exact copy ('¿Te gustó la herramienta? Déjame tu correo y te sigo mandando herramientas y cosas cool para creadores, entrepreneurs y marcas'). Claude noted that tying the capture to a concrete freebie (like a rate card template) would lift opt-in rates and she can swap the subtitle copy at any time. Two iteration rounds followed: both GIFs were sped up 1.5x (frame duration reduced from 250ms to 167ms) and then their white borders were removed, preserving rounded corners and the cat's rotation. Third, the session closed with Claude generating a full Emergent AI prompt spec for copy-paste delivery alongside the HTML file.  The final Emergent prompt spec is fully self-contained and includes: the complete six-question wizard flow with exact option labels, subtexts, default selections, and all associated multiplier and rate values; the locked pricing formula (tiered follower dollar calculation across four bands at $18/$12/$8/$5 per thousand, the engagement multiplier at 0.5 + eng%/8, and the four multiplicative factors for authority/production/relevance with the $150 floor minimum); the leverage calculation (leads via seguidores × eng% × lead rate by relevance tier, times CPL by industry); the results screen element order; the email capture spec including three backend connection options (native Emergent database, MailerLite API, or webhook for Manychat/N8n); and full brand styling including hex codes, Poppins typeface, GIF placement rules, and the 600px max-width centered column layout. The prompt explicitly states that the written spec overrides the HTML if any conflict exists, protecting the formula from Emergent reinterpretation. Adriana works in Caribbean Spanglish, iterates line by line, wants single clear recommendations rather than option menus, and enforces hard voice rules: no em dashes, no 'no es X es Y' contrast structures, hooks under ten words, and no clichés. Her own rewrites are treated as authoritative. Tool files delivered: `/mnt/user-data/outputs/calculadora_tarifas_app.html` (the active self-contained branded wizard with both GIFs embedded as base64)."
messages: 136
claude_uuid: "9f0b0b13-9c1a-42e2-98a8-2e1abc004286"
tags: [claude, chat, archive]
---
# Emergent x2 collaboration scripts

> **Conversation overview**

This was a focused build session with Adriana V. Márquez (@adrianavmarquez), a founder-content creator who builds educational tools and sponsored video content under her brand Creatividad². The session picked up mid-project from a prior transcript and had one primary goal: finalize the interactive "¿cuánto cobrar?" (rate calculator) web app as a branded HTML wizard, then generate a comprehensive Emergent AI prompt spec so the tool can be rebuilt as a fully functional app with real email capture.

The session moved through three sequential tasks. First, Adriana chose the layout configurations for two animated GIFs (a calculating cat and a smug corgi) from a set of four wireframe mockup options Claude generated per page. She selected portada C (cat GIF as a corner sticker on the start screen, slightly rotated, no border) and resultados B (corgi beside the price, side by side, flexible left column for price and right column for the GIF). Second, Claude implemented both GIF selections into the live HTML file along with an email capture card at the end of the results screen — after the number reveals, never gated — using her exact copy ("¿Te gustó la herramienta? Déjame tu correo y te sigo mandando herramientas y cosas cool para creadores, entrepreneurs y marcas"). Claude noted that tying the capture to a concrete freebie (like a rate card template) would lift opt-in rates and she can swap the subtitle copy at any time. Two iteration rounds followed: both GIFs were sped up 1.5x (frame duration reduced from 250ms to 167ms) and then their white borders were removed, preserving rounded corners and the cat's rotation. Third, the session closed with Claude generating a full Emergent AI prompt spec for copy-paste delivery alongside the HTML file.

The final Emergent prompt spec is fully self-contained and includes: the complete six-question wizard flow with exact option labels, subtexts, default selections, and all associated multiplier and rate values; the locked pricing formula (tiered follower dollar calculation across four bands at $18/$12/$8/$5 per thousand, the engagement multiplier at 0.5 + eng%/8, and the four multiplicative factors for authority/production/relevance with the $150 floor minimum); the leverage calculation (leads via seguidores × eng% × lead rate by relevance tier, times CPL by industry); the results screen element order; the email capture spec including three backend connection options (native Emergent database, MailerLite API, or webhook for Manychat/N8n); and full brand styling including hex codes, Poppins typeface, GIF placement rules, and the 600px max-width centered column layout. The prompt explicitly states that the written spec overrides the HTML if any conflict exists, protecting the formula from Emergent reinterpretation. Adriana works in Caribbean Spanglish, iterates line by line, wants single clear recommendations rather than option menus, and enforces hard voice rules: no em dashes, no "no es X es Y" contrast structures, hooks under ten words, and no clichés. Her own rewrites are treated as authoritative. Tool files delivered: `/mnt/user-data/outputs/calculadora_tarifas_app.html` (the active self-contained branded wizard with both GIFs embedded as base64).

## 🧑 Adriana · 2026-06-14 17:08
its time to develop de scripts for emergent x2 collab

## 🤖 Claude · 2026-06-14 17:09
Listo, ya tengo el contexto de la primera collab cargado, así que no me repitas eso. Para que estemos en la misma página antes de tocar nada:

**Lo que ya tenemos de la collab 1 (Kritika / Emergent):**
- Concepto: construir tu portfolio real en Emergent y documentar el proceso. Hook confesional ("mi portfolio daba pena ajena").
- Reglas duras del brief: no mencionar stats de la marca (ARR, usuarios, países), CTA a link en bio, tu cara en cuadro desde el hook.
- Quedó pendiente que Kritika eligiera hook y que metiéramos el beat de tips para beginner creators.

Antes de guionizar necesito que me aterrices una cosa, porque "x2" lo puedo leer de dos formas y el guión cambia completo según cuál sea:

**¿Qué es exactamente el x2?**
1. **Segunda pieza del mismo deal** (ej. el deal era 2 reels y este es el segundo entregable), o
2. **Deal nuevo completo** con Emergent (renovación, otro brief, otro objetivo).

Y pegado a eso, lo que sí necesito sí o sí para arrancar:
- El **brief de esta pieza** (o si reusamos el mismo, dímelo). El brief manda el scripting.
- **Cuántos entregables** y en **qué plataforma** cada uno (Reel IG, TikTok, YouTube short, etc.). Porque la backbone del guión la define el destino.

**Mi recomendación estratégica mientras me confirmas:** si esto es una segunda pieza, no repitamos el ángulo "portfolio confesional". Esa ya la quemamos con Kritika. La segunda pieza debería atacar un **momento distinto del funnel**. La primera fue identidad y vulnerabilidad (TOF, "esto me pasó a mí"). La segunda gana más si es **proceso documentado con fricción real**: enseñar el prompt exacto, el momento donde algo no salió a la primera, cómo lo arreglaste. Eso es lo que retiene en 2026 y le da a Emergent una demo de producto más honesta que un before/after.

Pásame el brief y el scope y arrancamos.

## 🧑 Adriana · 2026-06-14 17:09
They asked to change the hook to “You do not need another content idea. You need a system that can actually turn your ideas into an offer, a product, or a business” adapt the video script
> 📎 COLLAB_2_Emergent_Creatividad2_Script_Final.docx

## 🤖 Claude · 2026-06-14 17:12
Antes de tocar nada, una cosa que tengo que marcarte porque es justo lo que cuidamos en tu copy:

El hook que te mandó la marca, en su forma literal ("you do not need another content idea, you need a system..."), es exactamente la estructura **"no necesitas X, necesitas Y"** que tienes vetada. Si lo traduzco tal cual, suena a caption de coach. Así que mantuve la **intención** y el **payload** que la marca quiere (el problema no es generar contenido, es no tener un sistema que convierta la idea en producto), pero lo reescribí en tu voz sin la fórmula.

Y un punto a favor: este hook **le cuadra mejor al cuerpo que el anterior.** El hook viejo prometía "una página web" y el bloque de screen recording muestra un sistema completo (landing + email + segmentación + countdown, todo conectado). Con este hook nuevo, lo que prometes y lo que enseñas por fin están al mismo nivel. La palabra **sistema** se vuelve la columna del video: la abres en el hook, la pagas en el build, la cierras en el CTA.

Lo dejé en español para que cuadre con el resto del guión. Si esta pieza va en inglés, dímelo y te la adapto.

---

**BEAT 1 nuevo (hook adaptado) · talking head ~18 seg**

> "El contenido nos sobra. Ideas, mil." [pausa]
> "Lo que casi nadie monta es el sistema que convierte esa idea en una oferta. En un producto. En un negocio que de verdad puedas vender." [pausa, cambio de tono]
> "Yo llevo años con Creatividad² en la cabeza. Este mes la monto." [pausa]
> "¿El problema?" [pausa]
> "No sé hacer una página web. Los developers son carísimos. Las plataformas prediseñadas te cobran el 15% de todo lo que generas. Y encima ni siquiera lucen como tu marca." [pausa corta]
> "De eso, ya me cansé." [pausa, mira directo a cámara]
> "Te enseño cómo seteé el sistema completo."

**Notas de dirección:** Las dos primeras líneas son la afirmación que frena el scroll. Dílas con calma y certeza, como un hecho que ya sabes. "En una oferta. En un producto. En un negocio" va en escalada, separa cada palabra y sube un punto la intención en cada una. "Yo llevo años con Creatividad²" baja a lo personal, ahí te haces el caso de estudio. "¿El problema?" es el quiebre: baja la voz, acércate a cámara. Los tres problemas van uno por uno, no los encadenes. El 15% como dato frío, no como queja. La última línea es la promesa, directa y sin sonrisa, y fíjate que "sistema" cierra el loop que abriste en la primera frase.

**Overlay del hook (texto en pantalla, aparte de los subtítulos):** "TIENES LA IDEA. TE FALTA EL SISTEMA." El audio habla en plural ("nos sobra"), el overlay te señala a ti que ves el video. Capa distinta, no repite el audio.

---

**Los 3 hilos que tengo que ajustar para que el hook no quede huérfano**

Solo el hook cambia de fondo. Pero para que "sistema" pague a lo largo del video, tres retoques chiquitos:

1. **Beat 2, primera línea:** "Mi objetivo era simple" pasa a "El sistema que quería era simple". Refuerza la palabra ancla.
2. **Beat 3, cierre del bloque screen recording:** después de "Todo conectado. Todo funcionando." agregas "Ese es el sistema completo." Ahí pagas el hook con el visual ya construido en pantalla.
3. **Beat 4, CTA de Emergent:** "Si quieres construir algo así" pasa a "Si quieres montar tu propio sistema, el link de @emergentlabs está en mi bio." Cierra el arco completo.

Todo lo demás del guión se queda igual: checklist, BTS, money shots del correo y el countdown, los dos CTAs, las notas.

---

**Una alerta de tiempo:** el hook nuevo suma unos 4 segundos sobre el original. Con la versión tight que te puse ("Este mes la monto") quedamos rozando los 90. Si la marca pide algo extra después, recortamos del Beat 2 que es el más prescindible.

¿Lo regenero ya en .docx con tu estética de marca para mandárselo a @emergentlabs, o quieres afinar el wording del hook primero?

## 🧑 Adriana · 2026-06-14 17:41
ok que alternativas a “You do not need another content idea. You need a system that can actually turn your ideas into an offer, a product, or a business”

## 🤖 Claude · 2026-06-14 17:42
Todas estas mantienen el payload que la marca quiere (el problema no es generar ideas, es no tener el sistema que las convierte en producto) y ninguna usa la estructura "no necesitas X, necesitas Y". Te las doy en español para delivery y en inglés para que Kritika apruebe sin fricción, como hicimos en la collab 1.

**A. Open loop + prueba personal**
ES: "Este mes convertí una idea que tenía guardada hace años en un producto real. Sin saber programar, sin developer. Te enseño el sistema completo."
EN: "This month I turned an idea I'd been sitting on for years into a real product. No coding, no developer. I'll show you the whole system."

**B. Relatabilidad (filtra a tu persona exacta)**
ES: "Llevas años creando contenido. Pero un producto con tu nombre, todavía no. Casi siempre se interpone lo mismo: el sistema que convierte la idea en negocio."
EN: "You've been creating content for years. But a product with your name on it? Not yet. It's almost always the same thing in the way: the system that turns an idea into a business."

**C. Afirmación contundente (la que ya está en el guión)**
ES: "El contenido nos sobra. Ideas, mil. Lo que casi nadie monta es el sistema que convierte una idea en una oferta, un producto, un negocio."
EN: "We're drowning in content. A thousand ideas. What almost nobody builds is the system that turns one into an offer, a product, a business."

**D. Confesión (tu lane de vulnerabilidad)**
ES: "Tengo una carpeta de notas llena de ideas que nunca salieron de ahí. Este año por fin saqué una. Lo que cambió fue tener un sistema para convertirla en algo que la gente pudiera comprar."
EN: "I have a notes folder full of ideas that never left the folder. This year I finally shipped one. What changed was having a system to turn it into something people could actually buy."

**E. Liderada por el dato (15%)**
ES: "Las plataformas prediseñadas te cobran el 15% de todo lo que generas y ni siquiera lucen como tu marca. Por eso monté mi propio sistema. Te enseño cómo."
EN: "Pre-built platforms take 15% of everything you make and don't even look like your brand. So I built my own. Let me show you the system."

---

**Mi pick y por qué**

Iría con **A como principal.** Hace los tres trabajos del hook de una: frena el scroll con la prueba ("convertí una idea en producto"), filtra audiencia ("sin saber programar"), y entrega curiosidad de sistema. Y lo mejor: empata directo con tu bloque de screen recording, no tienes que forzar el puente.

**C como respaldo seguro con la marca,** porque es la más fiel a lo que pidió Kritika literalmente. Mantiene la palabra "contenido/ideas" que es justo lo que ella quiso meter. Si la marca está casada con su framing, C es la que aprueban sin pelear.

**B si quieres precisión de persona máxima.** Es la que mejor le habla al creador que lleva años publicando pero nunca lanzó un producto. Filtra durísimo, retiene menos volumen pero el que se queda es exactamente tu cliente.

Cuidado con **E:** es la más específica y falsificable, pero se desvía del ángulo "ideas/contenido" que la marca pidió. Solo la usaría si Kritika está abierta a reposicionar el hook hacia el dolor del 15%.

¿Con cuál nos quedamos y regenero el .docx, o le mando a Kritika un set de 2 o 3 para que elija ella?

## 🧑 Adriana · 2026-06-14 18:08
"Crear tu producto digital NUNCA se habia hecho tan sencillo"
"Sin desarollador, Sin programador, Sin diseñador."
"Necesitas pasar lo MAS facil y rapido posible esas ideas a una oferta/producto o negocio"

## 🤖 Claude · 2026-06-14 18:09
Estás iterando con tu propia versión, así que te la leo con criterio editorial, línea por línea, no te la apruebo entera.

**Línea 1: "Crear tu producto digital NUNCA se había hecho tan sencillo"**
Esta la cortaría. "Nunca se había hecho tan sencillo" es el cliché exacto que dice toda herramienta no-code en su landing. Pásala por tu propio test: no la puedo visualizar, no la puedo falsificar, y la puede decir cualquiera. Tres no. Es la línea más débil de las tres y arrancar el hook con ella te quita el filo desde el segundo uno.

**Línea 2: "Sin desarrollador, Sin programador, Sin diseñador."**
Esta es la fuerte. El triple negativo tiene ritmo y es concreto. Único arreglo: "desarrollador" y "programador" son lo mismo en español, así que se siente relleno para llegar a tres. Cámbialo por tres cosas distintas: **"Sin developer. Sin diseñador. Sin saber código."** Mismo cadencia, sin redundancia.

**Línea 3: "Necesitas pasar lo MÁS fácil y rápido posible esas ideas a una oferta/producto o negocio"**
El payload está bien, mantiene el oferta/producto/negocio que pidió la marca. Pero la sintaxis está enredada ("pasar esas ideas a una oferta") y "Necesitas" te devuelve al tono de coach, que es justo el borde de la estructura "you need" que estamos evitando. Hay que limpiarla.

---

**Cómo lo armaría (fusionando tus tres líneas en un hook)**

**Build 1, liderado por el dato (mi pick):**
ES: "Monté mi producto digital en [X días]. Sin developer, sin diseñador, sin saber una línea de código. De una idea guardada a una oferta lista para vender."
EN: "I built my digital product in [X days]. No developer, no designer, no line of code. From an idea sitting in my notes to an offer ready to sell."

El número real es lo que mata el cliché. "Nunca tan sencillo" es humo. "En un fin de semana" o "en tres días" es falsificable y la gente se queda a ver si es verdad. Métele el tiempo real que te tomó el build, eso es el oro.

**Build 2, más pegado a tus palabras exactas:**
ES: "Crear un producto digital con tu nombre. Sin developer, sin diseñador, sin saber código. De una idea a una oferta, un producto, un negocio. Y más rápido de lo que crees."
EN: "Build a digital product with your name on it. No developer, no designer, no code. From an idea to an offer, a product, a business. And faster than you'd think."

---

**Dos cosas a tener en cuenta:**

Tus líneas se inclinan al ángulo de **facilidad** (sin skills, rápido). La marca pidió el ángulo de **sistema** (convertir ideas en producto). No pelean, los buenos hooks fusionan los dos, que es lo que hacen los builds de arriba. Pero si Kritika está casada con la palabra "system", la metemos: "el sistema que monté para pasar de idea a oferta, sin developer ni diseñador."

Y ojo: si arrancas el video con el triple negativo (sin developer, sin diseñador, sin código), el Beat 1 que ya tenemos pierde un poco de sentido porque ahí desarrollas los tres problemas (página web, developers carísimos, el 15%). O el hook adelanta esos problemas, o el Beat 1 los desarrolla, no los dos. Decime con cuál build vas y reajusto el Beat 1 completo para que no se pisen.

## 🧑 Adriana · 2026-06-14 18:12
No quiero hablarlo en primera persona YO YO YO, al menos no en el hook.

## 🤖 Claude · 2026-06-14 18:14
Claro. Saco el YO del hook y lo dejo o impersonal o hablándole al que ve. La primera persona la guardamos para el cuerpo, donde sí funciona porque ahí te haces el caso de estudio.

**A. Transformación como sujeto (impersonal, mi pick)**
ES: "De una idea guardada a una oferta lista para vender. Sin developer, sin diseñador, sin saber una línea de código."
EN: "From an idea sitting in your notes to an offer ready to sell. No developer, no designer, no line of code."

Arranca in media res con el antes y después concreto. No hay YO, no hay sermón. El triple negativo entra como prueba, no como promesa vacía.

**B. Segunda persona, observacional (no coach)**
ES: "Tienes la idea. Tienes hasta el contenido. Lo que casi nunca se monta es el producto que la convierte en negocio."
EN: "You've got the idea. You've even got the content. What almost never gets built is the product that turns it into a business."

Le habla al que ve sin darle órdenes. Y mantiene la palabra "contenido" que es justo lo que pidió la marca. Es la más segura para que Kritika apruebe.

**C. El acto de crear como sujeto**
ES: "Crear un producto digital con tu nombre dejó de necesitar developer, diseñador, y meses de presupuesto."
EN: "Building a digital product with your name on it no longer takes a developer, a designer, or months of budget."

**D. Fragmentado, liderado por números**
ES: "Una idea guardada hace años. Una semana de trabajo. Cero código. Un producto real, listo para vender."
EN: "An idea sitting around for years. One week of work. Zero code. A real product, ready to sell."

La más punzante si le metes el tiempo real del build. "Una semana", "tres días", lo que haya sido. El número es lo que hace que se queden a verificar.

---

**Una decisión que tienes que tomar y reflujo el Beat 1 según lo que elijas:**

Si el hook arranca con el triple negativo (sin developer, sin diseñador, sin código), el Beat 1 actual se pisa, porque ahí desarrollas justo esos problemas (no sé hacer página web, los developers carísimos, el 15%). No pueden vivir los dos.

Dos caminos limpios:
1. **Hook con el triple negativo** (A o C). Entonces el Beat 1 suelta el problem-stack y va directo a tu caso: "Yo llevo años con Creatividad²..." y de una al build. El 15% lo rescatamos como dato suelto dentro del screen recording.
2. **Hook sin triple negativo** (B o D, transformación pura). El Beat 1 se queda como está, con el problem-stack completo y el 15% intacto, y el triple negativo aparece como remate cuando enseñas el resultado.

¿Con cuál hook vas y por cuál camino? Decido eso y te reflujo el Beat 1 completo, sin pisarse, y regenero el .docx.

## 🧑 Adriana · 2026-06-14 18:14
Que pensarías si te digo que puedes crear tu página web SIN DEVELOPER, SIN DISENADOR Y SIN SABER NADA DE CODIGO?

Y mucho mas rapido de lo que crees.

## 🤖 Claude · 2026-06-14 18:15
Te soy honesta porque es lo que me pides: el núcleo es bueno, pero el envoltorio lo debilita. Dos cosas.

**Una: "¿Qué pensarías si te digo que...?" es un wind-up.** Gasta cuatro o cinco palabras antes de que aterrice nada. Y esa cadencia específica ("what if I told you that you could...") es justo el registro de infomercial que sonás a anuncio de Facebook de 2017. Tu propia regla de esta sesión es arrancar in media res. La pregunta hipotética es lo contrario: es un marco alrededor de la frase real, no la frase real. El triple negativo que metiste adentro es lo bueno. Sácalo del envoltorio y déjalo pegar solo.

**Dos: "página web" te encoge el scope.** Veníamos de algo más grande: un sistema que convierte una idea en producto, oferta, negocio. Eso fue lo que pidió la marca. "Crear tu página web" te devuelve al frame chiquito, que es justo la versión débil del hook viejo. Una página web la promete cualquier plantilla. Un producto con tu nombre, listo para vender, no.

Hay una tensión real ahí y la decides tú: "página web" es la palabra literal de tu cliente A (el creador early que dice "quiero una web"), y conecta por relatabilidad. Pero "producto" es la transformación más grande y la que la marca quiere. Yo me quedaría con el frame grande y dejaría que el video muestre que ese producto incluye la web.

---

**Tu misma línea, sin el wrapper y con el scope restaurado:**

**Versión directa (tus palabras, limpia):**
ES: "Puedes crear tu producto digital sin developer, sin diseñador, y sin saber nada de código. Y mucho más rápido de lo que crees."
EN: "You can build your digital product with no developer, no designer, and zero code. And way faster than you'd think."

**Versión liderada por el resultado (más fuerte, in media res):**
ES: "Tu producto digital, listo para vender. Sin developer, sin diseñador, sin saber nada de código. Más rápido de lo que crees."
EN: "Your digital product, ready to sell. No developer, no designer, zero code. Faster than you'd think."

Si estás casada con el formato pregunta, que sea específica y provocadora, no hipotética: "¿Cuánto crees que tardarías en montar tu propio producto digital sin developer, sin diseñador, sin código?" Pero mi recomendación es soltar la pregunta y afirmar.

---

**Dos remates:**

"Más rápido de lo que crees" es vago. Tu estándar pide número. Cámbialo por el tiempo real del build ("en un fin de semana", "en tres días") y el hook sube de nivel solo. El número es lo que hace que se queden a comprobar.

Y este hook arranca con el triple negativo, así que es el **camino 1** que te dije: el Beat 1 suelta el problem-stack y va directo a tu caso, y el 15% lo rescato como dato suelto dentro del screen recording. Si vas con esta, me confirmas y te reflujo el Beat 1 completo y regenero el .docx.

## 🧑 Adriana · 2026-06-14 18:16
Es que puede serviri incluso para auqellos sin producto digital, quiero ser ultra especifica pero sin dejar por fuera los creadores que no tienen un producto digitsl como tal sino otro tipo de negocio.

## 🤖 Claude · 2026-06-14 18:17
> *[line redacted — references an out-of-scope venture]*

Pero ojo con cómo resuelves la amplitud, porque ahí está la trampa: la gente compra amplitud con vaguedad. "Crea lo que quieras", "haz realidad tus ideas". Eso es la sopa de clichés. Si abres el abanico bajando la especificidad, perdiste.

**La salida: mueve la especificidad de lugar.** No la pongas en QUÉ construyes (producto digital), ponla en el HUECO y en el MECANISMO. El hueco es lo que une a todos tus segmentos: tienen la idea y la visión, pero no el equipo técnico. Es literal la línea de Creatividad² en tu propio guión. Y el mecanismo es ultra concreto: sin developer, sin diseñador, sin código, el número real del build.

Así eres ultra específica en el dolor (visión sin equipo técnico) y en la prueba (el triple negativo), y dejas el output abierto con el triángulo que ya te dio la marca: oferta, producto, negocio. Cubre a todo el mundo sin sonar genérico.

---

**Build 1 (mi pick, limpio y en media res):**
ES: "Esa idea que tienes guardada, convertida en algo que puedas vender. Una oferta, un producto, un negocio. Sin developer, sin diseñador, sin saber código."
EN: "That idea you've been sitting on, turned into something you can sell. An offer, a product, a business. No developer, no designer, no code."

**Build 2 (ancla en el hueco, y rima con el pitch de Creatividad²):**
ES: "Tienes la visión. Lo que no tienes es el equipo técnico para montarla. Una oferta, un producto, un negocio entero. Sin developer, sin diseñador, sin código."
EN: "You've got the vision. What you don't have is the technical team to build it. An offer, a product, a whole business. No developer, no designer, no code."

**Build 3 (el más explícitamente inclusivo):**
ES: "Lo que quieres vender, montado y listo. Da igual si es una oferta, un producto o un negocio entero. Sin developer, sin diseñador, sin código. Más rápido de lo que crees."
EN: "Whatever you want to sell, built and ready. An offer, a product, or a whole business. No developer, no designer, no code. Faster than you'd think."

---

Iría con **Build 2.** Mete el "tienes la visión, no el equipo técnico" que es exactamente la audiencia de Creatividad², así que el hook y el pitch del producto que viene después riman. El espectador escucha la misma frase dos veces sin que se note, y eso construye coherencia en todo el video. El triángulo oferta/producto/negocio abre la carpa sin perder filo.

Build 1 si quieres lo más limpio y rápido. Build 3 si quieres dejar la inclusión explícita, blanco y negro.

El triángulo te resuelve el problema de exclusión sin tocar la especificidad. ¿Con cuál vas? Confirmo y te reflujo el Beat 1 y regenero el doc.

## 🧑 Adriana · 2026-06-14 18:19
escuchame, estas escribiendo HORRIBLE. 
explicame como un hook de 26 palabras te parece una buena idea?

## 🤖 Claude · 2026-06-14 18:19
Tienes razón. Un hook de 26 palabras no es un hook, es un párrafo. La cagué ahí: estuve metiendo el beat de apertura completo (la transformación, el triángulo, el triple negativo, la velocidad) y llamándolo hook. Eso no es el hook. El hook es la primera línea que frena el scroll, y nada más. Todo lo demás es cuerpo y entra después.

El hook hace UN trabajo: que no sigan deslizando. Punto. Cinco a diez palabras. El resto se desenrolla en los segundos siguientes.

Hooks de verdad:

1. "Sin developer. Sin diseñador. Sin código." (6)
2. "Tienes la visión. Te falta el equipo técnico." (8)
3. "Tu idea lleva años guardada." (5)
4. "Una idea no se vuelve negocio sola." (7)
5. "Lo más caro de lanzar algo nunca fue la idea." (10)

Iría con la **1** o la **2.**

La 1 es el scroll-stopper más limpio, es tu propia línea reducida a tamaño hook, y abre el loop solo: sin esas tres cosas, ¿entonces qué? El cuerpo lo responde de una.

La 2 es la que mejor filtra a tu gente, el que tiene visión pero no equipo técnico, y rima con el pitch de Creatividad² que viene después.

El triángulo (oferta, producto, negocio) y el triple negativo no van en el hook. Van en la línea 2 y 3 del beat, ya con el espectador enganchado.

¿Con cuál vas? Y armo el Beat 1 completo, hook corto arriba y el resto desenrollándose, sin paja.

## 🧑 Adriana · 2026-06-14 18:46
Estas lista para lanzar tu negocio. Crea tu página web SIN DEVELOPER, SIN DISENADOR Y SIN SABER NADA DE CODIGO.
Lo más importante de un lanzamiento es TODO lo que haces antes. 
PASO #1: Crear tu página de PRE-LANZAMIENTO
Me ahorre un dineral con esta herramienta. 
Tienes que tomar en cuenta los componentes indispensables para que tengas una lanzamiento exitoso. 

1. Que este optimizada para CONVERTIR. 
2. Que tenga los elementos necesarios.
3. Que este conectado con tu plataforma de Email Marketing. 
4. Que se parezca a ti.
5. Que cargue rápido.

1. Para convertir necesita un mensaje claro, generar confianza, el usuario solo debe tomar 1 accion .
2. Elementos principales son tu titulo, tu subtitulo, body, servicios, formulario de correo, boton de CTA y tus botones de redes. 
3. Yo use la que me sugirio Emergent y con tu llave de acceso se conecta a cualquier plataforma de email marketing que prefieras. Asi cada persona que ingresa recibe un email de bienvenida y ya colectaste tu correo.
4. Por mas que no seas disenador debes tener una idea, un bosquejo, de como quieres que luzca. Yo AMO las estrellas y mis colores favoritos son el amarillo, el rojo y el azul. Asi que los use los 3. 
5. Para cargar rapido debes evitar exceso de imagenes pesadas, mucha información,  código pesado/ desorganizado y un hosting malo. pero NADA e esto deberia importarte porque Emergent Ai se encarga de estos detalles. 
6.

## 🤖 Claude · 2026-06-14 18:46
Te sigo. Y veo el giro: esto pasó de talking-head confesional a un tutorial estructurado, con PASO #1 = tu página de pre-lanzamiento y los 5 componentes de una landing que convierte. Buen esqueleto, mucho más accionable.

Te quedaste en el 6. Dale, termina el dump completo y ahí lo proceso de una, sin tocar nada hasta que cierres. Tengo una nota sobre el formato y otra sobre el hook, pero me las guardo hasta que sueltes todo para no cortarte el flow.

## 🧑 Adriana · 2026-06-14 18:55
del 6 a 10 ya no es enumerado solo que no supe quitar la enumeracion. continuo:

para mi toque le agregue un conteo regresivo para que entiendan cuando se lanza. 

Le Agregué mis credenciales. Todo conectado. Todo funcionando.

Si quieres construir algo así con @emergentlabs comenta PRELAUNCH y te envio el link

## 🤖 Claude · 2026-06-14 18:57
Ya cerraste, lo tengo completo. Tres cosas rápidas antes de armarlo, porque cambian la estructura.

**1. Runtime, esta es la grande.** Cinco componentes, cada uno con su sub-explicación, más el countdown, más credenciales, más CTA. Eso no es un Reel de 90 segundos, son 2 a 3 minutos. Hay que decidir antes de escribir:
- Reel/TikTok: se comprime brutal, los 5 componentes pasan a una lista rápida y el visual hace el trabajo, no narras cada sub-punto.
- YouTube/talking head: cabe todo y hasta sobra para profundizar.

> *[line redacted — references an out-of-scope venture]*

Y "un dineral" es vago. Si puedes decir cuánto te ahorraste, o lo que te cobraba un developer, eso es lo falsificable que se queda en la cabeza.

**3. Hook.** Tu mejor hook no es el de arriba, es una línea que tienes enterrada en el setup: "Lo más importante de un lanzamiento es todo lo que haces antes." Eso es contrarian, abre loop y monta el PASO #1 solo. Súbela a hook. Y "página web" ya cuadra, porque ahora el video literalmente trata de construir esa página. Ese problema se resolvió cuando cambiaste el contenido.

**CTA.** "Comenta PRELAUNCH" es tu mecánica de Manychat y va perfecto. Dos flags: se desvía del "link en bio" que Emergent ya aprobó, confírmalo con Kritika antes de grabar. Y soltaste el CTA de Creatividad², dime si fue a propósito o lo reintegramos.

Decime el formato y te armo el beat-by-beat completo.

## 🧑 Adriana · 2026-06-14 18:58
verga el primero me parecia mucho mas largo comapra:

| **VISUAL** | **SCRIPT + TEXTO EN PANTALLA** | **NOTAS DE DIRECCIÓN** | | --- | --- | --- | | Talking head — cámara ~14 seg | "Llevo tiempo queriendo lanzar algo mío." [pausa] "Un producto real. Con mi nombre." [pausa — cambio de tono] "El problema?" [pausa] "No sé cómo hacer una página web. Los developers son carísimos. Las plataformas pre diseñadas te cobran el 15% de todo lo que generas. Y encima ni siquiera luce como tu marca." [pausa corta] "De eso, ya me cansé." [pausa — mira directo a cámara] "Te enseño cómo setearlo todo." | Aspiración tranquila en las primeras dos líneas. El "El problema?" es el quiebre: baja la voz, acércate a la cámara. Los tres problemas van en escalada, uno por uno. No los encadenes. El 15% como dato frío, no como queja. "De eso, ya me cansé" suave. "Te enseño cómo setearlo todo" directo, sin sonrisa. Es una promesa. | | Talking head — cámara ~10 seg | "Mi objetivo era simple: un landing mío, conectado a mi plataforma de email marketing. El problema: ¿por dónde empiezas?" [pausa — cuenta con los dedos] "Tu checklist: crear tus cuentas de Resend y MailerLite, los permisos para conectarlas, y un bosquejo de lo que quieres." | La pregunta "¿por dónde empiezas?" va directo al espectador, míralo. El checklist se dice como quien ya lo tiene resuelto, no como quien lo está descubriendo. Esa seguridad es lo que les da confianza de que tú sí sabes a dónde vas. | | Corte a pantalla. Música entra. Screen recording de Emergent + BTS intercalado. ~45 seg Orden de pantalla: 1. Bosquejo en Canva 2. Emergent con brand spec card, colores, fuentes 3. Nombre Creatividad² en el site 4. Cuentas de Resend y MailerLite 5. Segmentación de listas 6. Countdown ticker 7. Landing completa + formulario + correo llegando | "Así fue mi proceso con Emergent AI." [Se ve el bosquejo en Canva] "Primero diseñé mi bosquejo en Canva." [Se ve Emergent con la brand spec card] "Le adjunté mis colores, mis fuentes, mi copy. Y construyó todo con mi identidad visual." [Se ve el nombre Creatividad² en el site] "Se llama Creatividad² porque es para fundadores y creativos. Los que tienen la idea y la visión, pero no el equipo técnico." [Se ven las cuentas de Resend y MailerLite] "Les di acceso a mis cuentas de Resend y MailerLite para que se comunicaran entre sí." [Se ve la segmentación de listas] "Lo más importante a nivel NERD: segmenté los correos por fecha de ingreso. Pre-launch. Announcement. Post-launch. Así mi estrategia de email marketing se adapta a cada fase desde YA." [Se ve el countdown ticker] "Le pedí un countdown ticker. Lo construyó." [Se ve el resultado final: landing, formulario, correo llegando] "Agregué mis credenciales. Todo conectado. Todo funcionando." | Voiceover encima del visual. No regresar a cámara durante este bloque. Cada línea sincronizada con lo que se ve en pantalla. "Lo más importante a nivel NERD" se dice con una sonrisa. Es el momento más tuyo del bloque. El correo llegando al inbox: 2 seg mínimo en pantalla. El countdown ticker: 2 seg mínimo en pantalla. Ambos son los money shots del video. | | Corte de regreso a cámara. Laptop cerrada o a un lado. ~15 seg | "Si quieres construir algo así, el link de @emergentlabs está en mi bio." [pausa — cambio de energía, más íntimo] "Y si Creatividad² es para ti, comenta abajo. Te mando el link directo." [pausa — sonríe] "Junto con @emergentlabs les voy a estar contando todo el BTS de la creación de Creatividad²." | Dos CTAs con tono diferente. El de Emergent: directo, informativo. El de Creatividad²: más cercano, como una conversación. La pausa entre los dos es crítica: dale al espectador un segundo para procesar cuál es el suyo. La última línea se dice como anuncio, no como CTA. "Esto apenas empieza." Que se sientan invitados a un proceso. |

## 🤖 Claude · 2026-06-14 19:00
Tienes razón, me equivoqué en el número. Lo recalculé: tu contenido nuevo son unas 265 palabras habladas, el original era ~295. O sea el nuevo es hasta más corto. Lo de "2 a 3 minutos" fue mala matemática mía.

Lo que me confundió: asumí que ibas a nombrar los 5 componentes Y después narrar cada uno como párrafo aparte. Eso sí lo infla. Pero el original no funciona así. El original mete un montón de contenido en 84 segundos porque el bloque de screen recording hace VO corto encima del visual, la pantalla carga el significado mientras tú dices líneas cortas. Si los 5 componentes los muestras en el build en vez de explicarlos hablando, cabe igual de fácil. Misma técnica.

Aquí está armado con esa lógica. ~82 segundos.

| VISUAL | SCRIPT + TEXTO EN PANTALLA | NOTAS DE DIRECCIÓN |
| --- | --- | --- |
| Talking head, cámara. ~12 seg | "Lo más importante de tu lanzamiento pasa antes de lanzar." [pausa] "Paso uno: tu página de pre-lanzamiento. Sin developer, sin diseñador, sin saber código." [pausa, directo a cámara] "Y me ahorré un dineral. Te enseño cómo la monté." | La primera línea es el hook. Dícela como un hecho, no como pregunta. Es contrarian: todos creen que el lanzamiento es el día, tú dices que es lo de antes. Pausa para que aterrice. El triple negativo en escalada, una cosa por una. "Me ahorré un dineral" con cara de complicidad. |
| Talking head + overlay checklist. ~13 seg | "Una página de pre-lanzamiento que sirve tiene cinco cosas." [aparece la lista 1 a 5 en pantalla] "Que convierta. Que tenga los elementos correctos. Que esté conectada a tu email marketing. Que se parezca a ti. Que cargue rápido." [pausa] "Te muestro cómo conseguí las cinco." | Los cinco puntos rápido mientras aparecen como checklist (Glenda Sans, brand). No expliques cada uno aquí, eso lo hace el visual en el bloque que sigue. La velocidad es a propósito: abres cinco loops que el screen recording cierra. |
| Corte a pantalla. Música entra. Screen recording Emergent + BTS. ~45 seg | [Bosquejo en Canva] "Hice un bosquejo de cómo la quería. No hay que ser diseñador, solo tener la idea." [Emergent + brand spec card] "Le pasé mis colores y mis fuentes. Yo amo las estrellas, y el amarillo, el rojo y el azul. Usó los tres." [Landing con copy] "Título, subtítulo, tus servicios, y una sola acción para el que llega: dejar su correo." [Formulario + conexión] "Con tu llave de acceso se conecta a tu plataforma de email. Cada persona que entra recibe su bienvenida, y ya colectaste el correo." [Segmentación] "A nivel nerd: segmenté los correos por fase. Pre-launch, announcement, post-launch." [Countdown ticker] "Mi toque: un conteo regresivo para que sepan cuándo se lanza. Se lo pedí, lo construyó." [Resultado: landing + correo llegando] "Credenciales adentro. Todo conectado. Todo funcionando. Y carga rápido, porque de eso se encarga Emergent." | VO encima del visual, no regreses a cámara. Cada línea sincronizada con lo que se ve. "A nivel nerd" con sonrisa, es tu momento. El correo llegando: 2 seg mínimo. El countdown: 2 seg mínimo. Son los money shots. Aquí cierras los cinco loops del beat anterior, en orden. |
| Regreso a cámara. Laptop a un lado. ~12 seg | "Si quieres montar la tuya con @emergentlabs, comenta PRELAUNCH y te mando el link." [pausa] "Esto fue el paso uno de un lanzamiento que apenas empieza." | CTA directo. "PRELAUNCH" se dice claro y aparece en pantalla, es tu keyword de Manychat. La última línea es promesa de serie, no cierre. Que se queden para los próximos pasos. |

Tres cosas pendientes:

El UX-101 genérico (mensaje claro, genera confianza) lo comprimí en "una sola acción: dejar su correo", una línea mostrada, no una clase. Si lo quieres más explícito me dices, pero ahí es donde el video se vuelve tutorial de ChatGPT.

"Me ahorré un dineral": si tienes el número real o lo que cobra un developer, mételo. Falsificable pega más.

Soltaste el CTA de Creatividad² y el "link en bio" de Emergent. Ahora hay un solo CTA (PRELAUNCH). Confírmame dos cosas: que Emergent acepta comenta-para-DM en vez de link en bio, y si Creatividad² lo dejamos afuera a propósito.

Dime y regenero el .docx con tu estética para mandárselo a Kritika.

## 🧑 Adriana · 2026-06-14 19:07
1. me ahorré dos mil dólares con esta plataforma.
2. No me cambie sel hook, que ahora no conecta, no me hagas una tabla solo copia el script con el hook original y las correcciones que propones

## 🤖 Claude · 2026-06-14 19:08
Listo. Tu hook tal cual, sin tabla, con los dos mil dólares y mis correcciones adentro.

---

[Talking head, cámara]

"Estás lista para lanzar tu negocio. Crea tu página web sin developer, sin diseñador, y sin saber nada de código."

"Lo más importante de un lanzamiento es todo lo que haces antes."

"Paso uno: tu página de pre-lanzamiento."

"Me ahorré dos mil dólares montándola con esta plataforma."

"Una página de pre-lanzamiento que sirve tiene cinco cosas."

[Aparece la lista 1 a 5 en pantalla mientras las nombras]

"Que convierta. Que tenga los elementos correctos. Que esté conectada a tu email marketing. Que se parezca a ti. Y que cargue rápido."

"Te muestro cómo conseguí las cinco."

[Corte a pantalla. Música entra. Screen recording de Emergent + BTS intercalado]

[Bosquejo en Canva] "Hice un bosquejo de cómo la quería. No hay que ser diseñador, solo tener la idea."

[Emergent con brand spec card] "Le pasé mis colores y mis fuentes. Yo amo las estrellas, y el amarillo, el rojo y el azul. Usó los tres."

[Landing con el copy] "Título, subtítulo, tus servicios, y una sola acción para el que llega: dejar su correo."

[Conexión Resend y MailerLite] "Con tu llave de acceso se conecta a tu plataforma de email. Cada persona que entra recibe su bienvenida, y ya colectaste el correo."

[Segmentación de listas] "A nivel nerd: segmenté los correos por fase. Pre-launch, announcement, post-launch."

[Countdown ticker] "Mi toque: un conteo regresivo para que sepan cuándo se lanza. Se lo pedí, lo construyó."

[Resultado: landing completa, formulario, correo llegando] "Credenciales adentro. Todo conectado. Todo funcionando. Y carga rápido, porque de eso se encarga Emergent."

[Regreso a cámara, laptop a un lado]

"Si quieres montar la tuya con @emergentlabs, comenta PRELAUNCH y te mando el link."

"Esto fue el paso uno de un lanzamiento que apenas empieza."

---

Lo que toqué: metí los dos mil dólares, los 5 componentes se muestran en el build en vez de explicarse hablando (el UX-101 genérico quedó en una sola línea), dejé segmentación y countdown como tus diferenciadores, y el cierre paga el componente 5 con "carga rápido porque Emergent se encarga".

Pendiente tu confirmación: un solo CTA (PRELAUNCH), sin el link en bio ni el de Creatividad². Si Emergent pidió link en bio en el contrato, hay que reintegrarlo. Dime y te lo paso al .docx con tu marca.

## 🧑 Adriana · 2026-06-14 19:13
hazle pressure test a esto:

[Talking head, cámara]
"Estás lista para lanzar tu negocio. Crea tu página web sin developer, sin diseñador, y sin saber nada de código."
"Lo más importante de un lanzamiento es todo lo que haces antes."
"Paso uno: tu página de pre-lanzamiento."
"Me ahorré dos mil dólares montándola con esta plataforma."
"Una página de pre-lanzamiento que sirve tiene cinco cosas."
[Aparece la lista 1 a 5 en pantalla mientras las nombras]
"Que convierta. Que tenga los elementos correctos. Que esté conectada a tu email marketing. Que se parezca a ti. Y que cargue rápido."
"Te muestro cómo conseguí las cinco."
[Corte a pantalla. Música entra. Screen recording de Emergent + BTS intercalado]
[Bosquejo en Canva] "Hice un bosquejo de cómo la quería. No hay que ser diseñador, solo tener la idea."
[Emergent con brand spec card] "Le pasé mis colores y mis fuentes. Yo amo las estrellas, y el amarillo, el rojo y el azul. Usó los tres."
[Landing con el copy] "Título, subtítulo, tus servicios, y una sola acción para el que llega: dejar su correo."
[Conexión Resend y MailerLite] "Con tu llave de acceso se conecta a tu plataforma de email. Cada persona que entra recibe su bienvenida, y ya colectaste el correo."
[Segmentación de listas] "A nivel nerd: segmenté los correos por fase. Pre-launch, announcement, post-launch."
[Countdown ticker] "Mi toque: un conteo regresivo para que sepan cuándo se lanza. Se lo pedí, lo construyó."
[Resultado: landing completa, formulario, correo llegando] "Credenciales adentro. Todo conectado. Todo funcionando. Y carga rápido, porque de eso se encarga Emergent."
[Regreso a cámara, laptop a un lado]
"Si quieres montar la tuya con @emergentlabs, comenta PRELAUNCH y te mando el link."
"Esto fue el paso uno de un lanzamiento que apenas empieza."

## 🤖 Claude · 2026-06-14 19:15
Lo corrí por tus cuatro filtros: visualizar, falsificar, que nadie más lo pueda decir, y comprensión en menos de 2 segundos. Te lo doy sin anestesia.

**El hallazgo grande, antes que nada:** tu línea más fuerte está enterrada y tu línea más débil está en el hook.

"Me ahorré dos mil dólares" pasa los tres filtros de una: es concreta, es falsificable, y solo tú la puedes decir con ese número. Es la mejor línea del script. Y está en la posición 4, llegando al segundo 12.

Mientras tanto, "crea tu página web sin developer, sin diseñador, sin código" está en el hook. Y esa es, técnicamente, la línea más genérica de todo el guión. Webflow, Wix, Framer, Durable, Squarespace, todos dicen exactamente eso. Si la firma cualquier competidor, sigue teniendo sentido. Falla durísimo el filtro de "que nadie más lo pueda decir". Es concreta y falsificable, pero no es tuya, es de la categoría entera.

No te lo cambio porque lo bloqueaste. Pero el test dice lo que dice. La movida mínima que respeta tu hook: sube "me ahorré dos mil dólares" para que caiga en los primeros 5 segundos, no en el 12. Tu hook se queda, pero el dato que sí es tuyo entra temprano. Ahí el hook deja de cargar todo el peso de la unicidad solo.

**Lo que pasa los tres filtros (no toques):**

"Yo amo las estrellas, y el amarillo, el rojo y el azul. Usó los tres." Concreta, falsificable, y es literal tu marca. Nadie más dice esto.

"A nivel nerd: segmenté los correos por fase. Pre-launch, announcement, post-launch." Tu voz, y una jugada estratégica real que casi ningún creador hace. Bespoke.

La conexión del email con la llave de acceso y el "Mi toque: un conteo regresivo". Mecanismos mostrados, específicos, tuyos.

**Lo que falla y cómo lo arreglo:**

"Que tenga los elementos correctos." Es la frase más vaga del guión. ¿Correctos según quién? No la puedo visualizar ni falsificar. O nombras los elementos ahí mismo (título, formulario, CTA) o la cortas. Como está, es relleno.

"Que convierta." Genérica sola, pero el build la rescata cuando muestras "una sola acción: dejar su correo". Vive del visual, no se sostiene hablada. Déjala como abre-loop, nada más.

"Y carga rápido, porque de eso se encarga Emergent." "Carga rápido" no es falsificable. Si tienes el load time real (carga en 1 segundo, lo que sea), mételo. Si no, es la cola más débil del cierre, baja prioridad.

**El veredicto:** el cuerpo está fuerte, está lleno de lo que solo tú puedes decir. El problema es de orden, no de contenido. Tu activo más falsificable ($2000) está tarde y tu línea más genérica (el sin-código) está primero. Reordena eso y el script sube de nivel sin reescribir casi nada.

Si quieres, hago una segunda pasada con el método completo: saco el lenguaje real de tus DMs y comentarios y traduzco el hook a las palabras exactas que usa tu gente. Eso es lo que lo volvería imposible de replicar. Pero necesito que me pases ese material crudo.

## 🧑 Adriana · 2026-06-14 19:44
comencemos por el hook, tomando en cuenta mi strong line, como lo adaptarias con el hook que tngo actualmente? Necesita dar contexto de en que me ahorre los dos mil dolares y por que se tienen que quedar a ver

## 🤖 Claude · 2026-06-14 19:45
Tu hook se queda verbatim. Le pego abajo dos cosas: el contexto del ahorro (para qué eran esos dos mil) y la razón para quedarse.

**Opción 1 (mi pick, la razón para quedarse es la promesa de las 5 cosas):**

"Estás lista para lanzar tu negocio. Crea tu página web sin developer, sin diseñador, y sin saber nada de código."
"Me ahorré dos mil dólares. Lo que me cobraba un developer por hacerla."
"Te muestro las cinco cosas que necesita para funcionar."

Por qué funciona: el "lo que me cobraba un developer" le da contexto al número y lo vuelve falsificable, ya no es "me ahorré plata", es "un developer me cobraba esto exacto y no lo pagué". Y "las cinco cosas que necesita" es la razón para quedarse: abre un loop de lista que tu cuerpo cierra justo después. La gente se queda por la lista, y la lista ya está armada en tu guión.

**Opción 2 (la razón para quedarse es curiosidad contrarian):**

"Estás lista para lanzar tu negocio. Crea tu página web sin developer, sin diseñador, y sin saber nada de código."
"Me ahorré dos mil dólares. Lo que me cobraba un developer."
"Pero la página es apenas el paso uno. Lo más importante de un lanzamiento pasa antes."

Por qué funciona: misma fuerza en el número, pero la razón para quedarse cambia. En vez de prometer una lista, abres una tensión: si crees que el lanzamiento es el día, te equivocas, lo importante pasa antes. Eso pica más fuerte pero retiene a menos gente, la que se queda es la que de verdad va a lanzar algo.

Iría con la 1 para este video, porque tu cuerpo es literalmente las 5 cosas. La promesa y la entrega cuadran perfecto, sin deuda.

Una verificación antes de cerrar: ¿los dos mil eran específicamente lo que te cobraba un developer? Si fue contra otra cosa (una agencia, las fees de una plataforma a lo largo del año), cambio esa línea de contexto para que sea verdad exacta y no se te caiga si alguien pregunta. El número es tu mejor activo, no lo quiero apoyar en un contexto que no puedas defender.

## 🧑 Adriana · 2026-06-14 19:49
"Estas lista para lanzar tu negocio: crea tu pagina web sin developer, sin diseñador, y sin saber nada de código."
"Yo me ahorre dos mil dolares, lo que me cobraba un desarrollador por hacerla."
"Pero la página en sí AHORITA es lo de menos, necesitas una pagina de lanzamiento."

## 🤖 Claude · 2026-06-14 19:50
La línea del ahorro quedó cerrada y fuerte, ahí no toco nada. Y el instinto de la tercera línea es correcto: reencuadrar de "tu web" a "tu página de lanzamiento" abre el loop y te da la razón para quedarse. Tres ajustes finos.

**1. "La página en sí es lo de menos" te juega en contra.** Estás vendiendo a Emergent, que hace páginas. Si dices que la página es lo de menos, devalúas justo el producto del sponsor. El arreglo es de alcance: no descartes "la página", acota a "la web completa". La web completa viene después, lo primero es la de pre-lanzamiento. Secuencias en vez de descartar, y el reframe se mantiene igual de fuerte.

**2. Dijiste "página de lanzamiento", tu cuerpo dice "pre-lanzamiento".** Son cosas distintas: la de pre-lanzamiento es la que colecta correos ANTES de lanzar, con el countdown. Eso es lo que muestras. Alinéalo a "pre-lanzamiento" para no tener dos términos peleando.

**3. Detalle mínimo:** el hook dice "developer", la línea 2 dice "desarrollador". Mismo rol, dos idiomas, en cinco segundos. Pega uno. Yo dejaría "developer", que ya está arriba.

Tu beat queda así:

"Estás lista para lanzar tu negocio: crea tu página web sin developer, sin diseñador, y sin saber nada de código."
"Yo me ahorré dos mil dólares, lo que me cobraba un developer por hacerla."
"Pero la web completa AHORITA es lo de menos. Lo primero que necesitas es tu página de pre-lanzamiento."

Una cosa para cuando armemos el cuerpo: ahí ya dijiste "página de pre-lanzamiento", así que el "Paso uno: tu página de pre-lanzamiento" del cuerpo se repetiría. Lo fusiono cuando lleguemos para que no suene dos veces.

¿Cerramos el hook así y seguimos con el cuerpo?

## 🧑 Adriana · 2026-06-14 19:55
"Yo me ahorré dos mil dólares, lo que me cobraban por hacerla."
"Pero la web completa AHORITA es lo de menos. Lo primero que necesitas es tu página de pre-lanzamiento."

## 🤖 Claude · 2026-06-14 19:56
Quedó. Y quitar "developer" de la línea 2 fue buena decisión: el hook ya lo nombró un segundo antes, así que "lo que me cobraban por hacerla" se entiende solo sin repetir la palabra. Más limpio.

Hook cerrado. Aquí está el script completo, con el cuerpo fusionado para que no se repita (el "paso uno" y los dos mil dólares ya viven en el hook, así que el cuerpo arranca directo en el porqué):

[Talking head, cámara]

"Estás lista para lanzar tu negocio: crea tu página web sin developer, sin diseñador, y sin saber nada de código."

"Yo me ahorré dos mil dólares, lo que me cobraban por hacerla."

"Pero la web completa AHORITA es lo de menos. Lo primero que necesitas es tu página de pre-lanzamiento."

"Porque lo más importante de un lanzamiento es todo lo que haces antes."

"Y una página de pre-lanzamiento que sirve tiene cinco cosas."

[Aparece la lista 1 a 5 en pantalla mientras las nombras]

"Que convierta. Que tenga los elementos correctos. Que esté conectada a tu email marketing. Que se parezca a ti. Y que cargue rápido."

"Te muestro cómo conseguí las cinco."

[Corte a pantalla. Música entra. Screen recording de Emergent + BTS intercalado]

[Bosquejo en Canva] "Hice un bosquejo de cómo la quería. No hay que ser diseñador, solo tener la idea."

[Emergent con brand spec card] "Le pasé mis colores y mis fuentes. Yo amo las estrellas, y el amarillo, el rojo y el azul. Usó los tres."

[Landing con el copy] "Título, subtítulo, tus servicios, y una sola acción para el que llega: dejar su correo."

[Conexión Resend y MailerLite] "Con tu llave de acceso se conecta a tu plataforma de email. Cada persona que entra recibe su bienvenida, y ya colectaste el correo."

[Segmentación de listas] "A nivel nerd: segmenté los correos por fase. Pre-launch, announcement, post-launch."

[Countdown ticker] "Mi toque: un conteo regresivo para que sepan cuándo se lanza. Se lo pedí, lo construyó."

[Resultado: landing completa, formulario, correo llegando] "Credenciales adentro. Todo conectado. Todo funcionando. Y carga rápido, porque de eso se encarga Emergent."

[Regreso a cámara, laptop a un lado]

"Si quieres montar la tuya con @emergentlabs, comenta PRELAUNCH y te mando el link."

"Esto fue el paso uno de un lanzamiento que apenas empieza."

Dos cosas siguen abiertas del pressure test, por si las quieres cerrar antes del .docx: "que tenga los elementos correctos" sigue siendo la línea vaga (o nombras los elementos o la cortas), y falta confirmar con Kritika que aceptan el CTA de comenta-PRELAUNCH en vez del link en bio que ya estaba aprobado.

¿Las cerramos o te genero el .docx con tu estética ya?

## 🧑 Adriana · 2026-06-14 19:59
no queiro repetir lo mismo aca ""Y una página de pre-lanzamiento que sirve tiene cinco cosas."" no hay otra manera de redactarlo?

## 🤖 Claude · 2026-06-14 19:59
Sí, hay varias. La idea es que la segunda vez te refieras a ella sin nombrarla, ya la nombraste dos líneas antes.

Opciones:

A. "Pero no cualquiera sirve. La que funciona tiene cinco cosas."
B. "Y para que la tuya funcione, necesita cinco cosas."
C. "Y no cualquiera convierte. La que sí, tiene cinco cosas en común."

Iría con la **A.** El "no cualquiera sirve" mete una tensión que la versión vieja no tenía: no es solo "tiene cinco cosas", es que la mayoría no funciona y solo la que cumple estas cinco sí. Eso hace que el espectador quiera ver las cinco para no quedarse con la que no sirve. Refuerza el loop en vez de solo anunciarlo.

La B es la más económica si quieres algo seco y directo. La C si quieres amarrarla al verbo "convierte", que es justo el componente número uno.

## 🧑 Adriana · 2026-06-14 20:01
ok dale B

## 🤖 Claude · 2026-06-14 20:01
Hecho. Así queda esa parte:

"Lo primero que necesitas es tu página de pre-lanzamiento."
"Porque lo más importante de un lanzamiento es todo lo que haces antes."
"Y para que la tuya funcione, necesita cinco cosas."

Fluye limpio y ya no se repite.

Con eso el hook y la transición quedaron cerrados. La única línea que el pressure test sigue marcando es "que tenga los elementos correctos", que es vaga. ¿La afinamos (nombrando los elementos, tipo título, formulario y CTA) o la dejas así y te genero el .docx con tu estética para mandárselo a Kritika?

## 🧑 Adriana · 2026-06-14 20:05
ok continua con el resto

## 🤖 Claude · 2026-06-14 20:06
Listo, cierro el resto. Afiné "elementos correctos" nombrando los elementos concretos (era lo que pedía el pressure test) y dejé todo lo demás ya cerrado. Script completo y final:

[Talking head, cámara]

"Estás lista para lanzar tu negocio: crea tu página web sin developer, sin diseñador, y sin saber nada de código."

"Yo me ahorré dos mil dólares, lo que me cobraban por hacerla."

"Pero la web completa AHORITA es lo de menos. Lo primero que necesitas es tu página de pre-lanzamiento."

"Porque lo más importante de un lanzamiento es todo lo que haces antes."

"Y para que la tuya funcione, necesita cinco cosas."

[Aparece la lista 1 a 5 en pantalla mientras las nombras]

"Que convierta. Que tenga lo esencial: título, formulario y un solo botón. Que esté conectada a tu email marketing. Que se parezca a ti. Y que cargue rápido."

"Te muestro cómo conseguí las cinco."

[Corte a pantalla. Música entra. Screen recording de Emergent + BTS intercalado]

[Bosquejo en Canva] "Hice un bosquejo de cómo la quería. No hay que ser diseñador, solo tener la idea."

[Emergent con brand spec card] "Le pasé mis colores y mis fuentes. Yo amo las estrellas, y el amarillo, el rojo y el azul. Usó los tres."

[Landing con el copy] "Título, subtítulo, tus servicios, y una sola acción para el que llega: dejar su correo."

[Conexión Resend y MailerLite] "Con tu llave de acceso se conecta a tu plataforma de email. Cada persona que entra recibe su bienvenida, y ya colectaste el correo."

[Segmentación de listas] "A nivel nerd: segmenté los correos por fase. Pre-launch, announcement, post-launch."

[Countdown ticker] "Mi toque: un conteo regresivo para que sepan cuándo se lanza. Se lo pedí, lo construyó."

[Resultado: landing completa, formulario, correo llegando] "Credenciales adentro. Todo conectado. Todo funcionando. Y carga rápido, porque de eso se encarga Emergent."

[Regreso a cámara, laptop a un lado]

"Si quieres montar la tuya con @emergentlabs, comenta PRELAUNCH y te mando el link."

"Esto fue el paso uno de un lanzamiento que apenas empieza."

Lo único que queda fuera de mis manos es confirmar con Kritika que aceptan el CTA de comenta-PRELAUNCH en lugar del link en bio. Eso lo tienes que validar tú con la marca antes de grabar.

¿Te genero el .docx con tu estética para mandárselo?

## 🧑 Adriana · 2026-06-14 20:08
lo cambiaste es: A. "Pero no cualquiera sirve. La que funciona tiene cinco cosas."

## 🤖 Claude · 2026-06-14 20:09
El script estaba con B, lo cambio a A como pides. Queda así:

"Lo primero que necesitas es tu página de pre-lanzamiento."
"Porque lo más importante de un lanzamiento es todo lo que haces antes."
"Pero no cualquiera sirve. La que funciona tiene cinco cosas."

Todo lo demás del script se queda igual. ¿Te genero el .docx con tu estética ya, o quieres revisar algo más antes?

## 🧑 Adriana · 2026-06-14 20:22
ok asi quedo

## 🤖 Claude · 2026-06-14 20:26
Cerrado. Te lo armo en el .docx con tu estética de marca.

Listo. Ábrelo en Google Docs y ya está listo para que Kritika deje comentarios.

Tiene tu estética completa: header con las estrellas, tabla beat-by-beat con headers azules y letra amarilla, tabla de overlays para aprobación, notas de producción y referencias visuales.

Dentro del doc, en la tabla de aprobación, dejé marcado en el CTA principal que tiene que confirmar el comenta-PRELAUNCH en lugar del link en bio. Eso es lo único que falta cerrar con la marca antes de grabar.

## 🧑 Adriana · 2026-06-14 20:37
formato copy paste del script only

## 🤖 Claude · 2026-06-14 20:38
Estás lista para lanzar tu negocio: crea tu página web sin developer, sin diseñador, y sin saber nada de código.

Yo me ahorré dos mil dólares, lo que me cobraban por hacerla.

Pero la web completa AHORITA es lo de menos. Lo primero que necesitas es tu página de pre-lanzamiento.

Porque lo más importante de un lanzamiento es todo lo que haces antes.

Pero no cualquiera sirve. La que funciona tiene cinco cosas.

Que convierta. Que tenga lo esencial: título, formulario y un solo botón. Que esté conectada a tu email marketing. Que se parezca a ti. Y que cargue rápido.

Te muestro cómo conseguí las cinco.

Hice un bosquejo de cómo la quería. No hay que ser diseñador, solo tener la idea.

Le pasé mis colores y mis fuentes. Yo amo las estrellas, y el amarillo, el rojo y el azul. Usó los tres.

Título, subtítulo, tus servicios, y una sola acción para el que llega: dejar su correo.

Con tu llave de acceso se conecta a tu plataforma de email. Cada persona que entra recibe su bienvenida, y ya colectaste el correo.

A nivel nerd: segmenté los correos por fase. Pre-launch, announcement, post-launch.

Mi toque: un conteo regresivo para que sepan cuándo se lanza. Se lo pedí, lo construyó.

Credenciales adentro. Todo conectado. Todo funcionando. Y carga rápido, porque de eso se encarga Emergent.

Si quieres montar la tuya con @emergentlabs, comenta PRELAUNCH y te mando el link.

Esto fue el paso uno de un lanzamiento que apenas empieza.

## 🧑 Adriana · 2026-06-16 14:46
Necesito hacer una parte dos para un tercer video, el primeor fue mi portfolio, el segundo mi landing page, y el tercero no se como abordarlo segun el brief any idea sparks?

## 🤖 Claude · 2026-06-16 14:48
La serie tiene un arco claro: V1 = quién eres (portfolio), V2 = empieza el lanzamiento (capturas la lista). El riesgo de V3 es que se vuelva "otra página que construí". Si es otra landing, la trilogía se aplana. V3 tiene que escalar: mostrar a Emergent haciendo algo que un constructor de páginas NO puede.

Cuatro sparks, de menos a más diferenciado:

**1. El momento de conversión (la página de oferta/ventas).**
El paso lógico del funnel: ya tienes la lista, ahora se convierte. Tensión: una lista no es un negocio hasta que vende. Pro: cierra el arco capturar → convertir. Contra: es otra página, formato pegado a V2. Para que no se sienta repetido, el foco va en la mecánica de persuasión en vivo (el stack de oferta, la prueba, el checkout), no en la página en sí.

**2. Una herramienta interactiva como lead magnet (mi pick).**
No otra página: una app real. Un quiz que diagnostica qué tipo de creador eres y te manda a la oferta correcta de Creatividad². O tu "Pasa el Filtro" convertido en herramienta. Hook: "construí una herramienta interactiva, no una página, y sin saber código." Por qué gana: es el mejor demo de Emergent porque muestra que hace apps, no solo landings, rompe formato con V2, y le das a Creatividad² un lead magnet real que vive solo. Cuadra con tu serie de recursos.

**3. El sistema que se mueve solo (automatización).**
Conectas Emergent + Manychat + email + segmentación y muestras todo corriendo sin ti. Tensión: la diferencia entre un creador y un negocio es lo que pasa cuando no estás. Money shot: alguien comenta PRELAUNCH en vivo, le entra el DM, el email, el tag, todo automático. Paga el keyword que sembraste en V2, buen callback de serie. Es lo más tuyo. Contra: más abstracto, hay que trabajarlo visual.

**4. El reveal de la web completa.**
En V2 dijiste "la web completa AHORITA es lo de menos". V3 la revela: el sitio que amarra portfolio, ofertas y comunidad. Cierre narrativo de la trilogía. Contra: otra vez una página.

Iría con la **2 o la 3.** La 2 si quieres el mejor demo del producto y un activo nuevo. La 3 si quieres lo más tuyo y cerrar el loop de PRELAUNCH.

Pero la decisión real depende de dos cosas: ¿el brief de V3 te asigna tema o lo dejan abierto? Y más importante, ¿qué estás construyendo de verdad para Creatividad² ahora mismo? El brief te pide documentar proceso real, así que el mejor video es el que sí vas a montar, no el que suena bonito. Dime eso y aterrizo el ángulo.

## 🧑 Adriana · 2026-06-16 15:06
Este es el que mas me gusta:

2. Una herramienta interactiva como lead magnet (mi pick).No otra página: una app real. Un quiz que diagnostica qué tipo de creador eres y te manda a la oferta correcta de Creatividad². O tu "Pasa el Filtro" convertido en herramienta. Hook: "construí una herramienta interactiva, no una página, y sin saber código." Por qué gana: es el mejor demo de Emergent porque muestra que hace apps, no solo landings, rompe formato con V2, y le das a Creatividad² un lead magnet real que vive solo. Cuadra con tu serie de recursos.

Y que empiece con: Como garantizar un lanzamiento IMPECABLE. El proceso de desarrollo tiene como funcion principal: comunicar que estas desarollando algo, ajustar tu prototipo para que tengas un mayor % de clientes satisfechos y a ti para entender mejor a tu cliente ideal. 

Como coño hacemos esto te preguntarás? Con un quiz de diagnóstico COOL e Interactivo. 
Sin saber NADA de código con Emergent. 

La estrategia de rollout te la dejo en otro video. 

Cómo desarollamos esta herramienta:

1. Preguntas estratégicas que te ayuden a mejorar tu product demo
2. Garantizale a aquellos que completen esta herramienta un descuento
3. Define tu estética de marca, color, elementos, fuentes, etc
4. Para el enfoque visual tienes dos opciones:
a: lo dibujas tu misma, escaneas y subes tus bosquejos 
b: consigue inspiraciones de frames para la app 

1. Sin importar lo que decidas anteriormente, desarolla un "Mood Board" de como quieres que se SIENTA tu app y tambien lo subes. 
Es un PLUS si desarollas un archivo .md con do's dont's de tu marca, tu identidad visual, etc para que sea un resultado mas acertado. 
Y LISTOOO!
Emergent Ai se encarga de desarollartelo todo, conectar una base de datos donde se vacian todos los submissions y LISHTO.

Comenta LISHTO y te mando el link de ingreso

## 🤖 Claude · 2026-06-16 15:07
Buena elección, y tu dump ya trae el oro adentro, solo está enterrado. Déjame marcarte lo que veo antes de armarlo.

**Lo más fuerte que escribiste (y casi lo escondes):** "el proceso de desarrollo comunica que estás construyendo algo, ajusta tu prototipo, y te enseña a entender a tu cliente ideal." Eso es el ángulo. El quiz no es un lead magnet, es un instrumento que hace tres trabajos a la vez disfrazado de quiz divertido: marketing, producto y research. Ese es el insight que ningún tutorial de "haz un lead magnet" te da. Eso va arriba, no enterrado en la línea cuatro.

**El hook.** "Cómo garantizar un lanzamiento IMPECABLE" tiene el problema que ya conoces: "impecable" es un adjetivo vacío, no lo puedo visualizar ni falsificar. Y "quiz COOL" igual, "cool" no dice nada. Mantengo tu intención (asegurar que el lanzamiento funcione) pero la aterrizo. Dos direcciones:

A. "La mayoría lanza a ciegas y reza. Antes de vender, construí una herramienta que me dice qué quiere mi cliente antes de terminar el producto. Un quiz interactivo. Sin código, con Emergent."

B. "Lo más importante de un lanzamiento es todo lo que haces antes." [callback directo a V2] "Esta vez construí un quiz que hace tres cosas a la vez: avisa que estoy creando algo, me dice cómo mejorar el producto, y me enseña a quién le estoy vendiendo."

La B amarra la trilogía porque repite tu propia línea de V2. La A pega más fuerte sola. Yo iría con la B por la coherencia de serie, pero dime tú.

**Lo que está fuerte y mantengo tal cual:**
El descuento para quien completa el quiz (razón concreta para terminarlo, eso convierte). Las dos opciones visuales (dibujar y escanear vs. buscar frames). El mood board subido. Y el archivo .md con do's y don'ts de marca, eso es oro de power-user y conecta con la brand spec card de V2. La base de datos llenándose con los submissions es tu money shot, ahí Emergent demuestra que hace una app de verdad, no una página. Y "la estrategia de rollout te la dejo en otro video" es un open loop perfecto que siembra el V4.

**Tres flags rápidos:**

"Como coño hacemos esto" es tu voz pura y me encanta, pero es video de marca. Confirma que Emergent acepta el "coño" o lo suavizamos a "¿cómo se hace esto?". Tu call.

LISHTO como keyword va perfecto y es consistente con PRELAUNCH. Mismo pendiente: confirmar con la marca el comenta-para-DM.

Esto tiene más pasos que V2. Misma solución: los pasos se muestran en el build, tú narras corto. Puede que roce los 90 o se pase un poquito, lo medimos cuando lo arme.

¿Con cuál hook vamos, A o B, y dejamos el "coño" o lo cambiamos? Con eso te armo el beat-by-beat completo.

## 🧑 Adriana · 2026-06-16 15:13
No, iteremos mas esos hooks no me dicen nada.

## 🤖 Claude · 2026-06-16 15:14
Cierto, A y B explican en vez de pegar. Suenan a estrategia, no a gancho. Te tiro ángulos distintos, más viscerales y concretos:

A. "Hice que mi audiencia hiciera mi estudio de mercado por mí. Y la pasaron bien."

B. "Esto parece un quiz divertido. En realidad me está diciendo qué producto construir y a quién vendérselo."

C. "Conseguí compradores antes de terminar el producto."

D. "Convertí a mi cliente ideal en mi consultor de producto. Gratis."

Iría con la **B.** Es la única que aprovecha que es video: muestras el quiz en pantalla, se ve inofensivo y divertido, y tú revelas lo que de verdad está haciendo por debajo. El gap entre lo que parece y lo que es, ese es el gancho. Las otras lo cuentan, la B lo enseña.

La A es la más cheeky y tu voz pura. La C es la más bold pero solo si es verdad que ya tienes interesados con el descuento, no la uses si no. La D reencuadra la relación con tu cliente, buena pero más cerebral.

¿Alguna te prende o te tiro otra tanda por otro lado?

## 🧑 Adriana · 2026-06-16 15:15
Conseguí clientes ANTES de tener mi producto?

## 🤖 Claude · 2026-06-16 15:16
Esa es la más fuerte de las cuatro, pero solo si es verdad de verdad. Y ahí tengo que frenarte un segundo antes de enamorarnos de ella.

"Clientes" implica que pagaron o se comprometieron. ¿Eso fue lo que pasó, o lo que tienes son leads e interesados que reclamaron el descuento? La diferencia lo es todo:

Si pagaron o apartaron, el hook es oro puro. Conseguir clientes antes de tener el producto es de las cosas más bold que un founder puede decir: es contraintuitivo, es falsificable, y nadie más lo puede decir. Úsalo sin miedo.

Si son leads que llenaron el quiz por el descuento, "clientes" se pasa de la raya y se te cae si alguien pregunta "¿cuántos pagaron?". Ahí lo bajamos a lo que sí es verdad y sigue siendo fuerte: "ya tengo gente esperando para comprar antes de terminar el producto" o "validé que hay demanda antes de construir nada".

Sobre el formato: tu versión es pregunta de sí/no, y esa se siente un poco blanda porque la respuesta obvia es sí, por eso estás haciendo el video. Pega más fuerte como afirmación, y dejas que el "cómo" sea el loop:

"Conseguí clientes antes de tener el producto. Te enseño cómo."

La curiosidad no está en si lo lograste, está en cómo. Eso es lo que los retiene.

Dime una cosa nada más: ¿pagaron, apartaron, o son leads? Con eso cierro el hook en la versión que puedas defender con los ojos cerrados.

## 🧑 Adriana · 2026-06-16 15:19
Bueno no son clientes clientes no apagron pero lo que quieor hacer elusion es que, 
como garantizas la satisfaccion de tu cliente antes de que siquiera hayan comprado el producto?
es TREMENDA estrategia,

## 🤖 Claude · 2026-06-16 15:20
Eso sí es defendible, y es mejor ángulo que "clientes". Porque es literal verdad: el quiz recoge lo que tu gente quiere, tú construyes el producto alrededor de esas respuestas, y por eso quedan satisfechos cuando sale. Eso sí lo puedes sostener. Buen instinto bajándote de "clientes".

Un flag chiquito: "garantizar la satisfacción" es el nuevo "clientes". Garantizar al 100% no se puede, y alguien te lo puede picar. Lo que de verdad haces es subir las probabilidades muchísimo, porque ellos lo diseñaron. Si quieres airtight, "asegurar" o "casi garantizar". Si quieres la palabra bold, deja "garantizar" pero sabiendo que atrás está el mecanismo de co-creación.

La inversión es el gancho: la satisfacción normalmente pasa DESPUÉS de comprar, tú la mueves a ANTES. Tres formas:

A. "¿Cómo logras que tu cliente quede satisfecho con tu producto antes de comprarlo?"

B. "Mis clientes van a estar satisfechos con mi producto antes de pagarlo. A propósito."

C. "Dejé que mis futuros clientes me dijeran qué construir. Antes de construirlo."

Iría con la **B.** Pone la inversión completa en la cara (satisfechos antes de pagar) y el "a propósito" deja claro que es estrategia, no suerte. Esa es tu voz. La C enseña el mecanismo y es la más concreta, buena si la quieres menos declarativa. La A mantiene tu pregunta, y aquí sí funciona porque la premisa es tan contraintuitiva que la respuesta no es obvia.

¿Cuál te prende?

## 🧑 Adriana · 2026-06-16 15:21
Como yo hago contenido para creadores, marcas personales y negocios, la idea seria comenzar a hacer videos dando tips faciles y dejar un open loop de que es lo que mas se te dificulta, comenta abajo del video y te ayudo. 

En el mismo quiz quisiera que sea como un identificador de problema automatico para las personas, saber donde estan fallando en su creacion de contenido,  si es estretagia, pre produccion, produccion, edicion, distribucion, falta de analisis POST publicacion. 

Quiero que las preguntas sean relacionadas a todo esto y asi yo entiendo tambien cual es la mayor necesidad que tienen las personas

## 🤖 Claude · 2026-06-16 15:23
Esto eleva el video completo. El quiz dejó de ser un lead magnet genérico y se volvió un diagnóstico real: le dices al creador en cuál de las seis etapas de su contenido se está cayendo. Eso es útil de verdad, por eso lo completan.

Y lo que estás armando no es un video, es un flywheel: el quiz diagnostica, tú ves en agregado dónde falla la mayoría de tu audiencia, haces tus videos de tips justo sobre esa etapa con el open loop de "comenta qué se te dificulta", y ese contenido manda más gente al quiz. Tu lead magnet y tu calendario de contenido se alimentan solos. ESA es la tremenda estrategia, más que la satisfacción del producto. Es una máquina de research que te dicta qué enseñar.

Las seis etapas ya están en secuencia lógica (estrategia es la raíz, análisis post cierra el loop). Las dejaría exactamente así, es un framework que se entiende de un vistazo.

Pero esto te mueve el hook. Veníamos del ángulo "satisfacción antes de comprar", que es sobre TI. Ahora el quiz le habla directo al dolor del que ve. Dos carriles:

Carril beneficio (al espectador): "Si tu contenido no despega, el problema está en una de seis etapas. Este quiz te dice en cuál." Le da al que ve una razón inmediata para hacer el quiz. Convierte más.

Carril estrategia (tú): el de "satisfacción antes de comprar, a propósito". Más contrarian y founder, pero menos accionable para el que ve.

Para un video cuyo trabajo es mandar gente al quiz, iría por el carril beneficio, y tu estrategia la dejas como el reveal del medio: "y de paso, esto me dice exactamente qué tengo que enseñar."

¿Te armo el framework del quiz (las seis etapas con preguntas de diagnóstico de muestra y la lógica de resultado y ruteo)? Es lo que el video muestra construyéndose, y de paso te queda el quiz real listo. Dime también qué carril de hook quieres y cierro el gancho.

## 🧑 Adriana · 2026-06-16 15:27
No cambies el norte de este video, estamos hablando de dos videos a la vez. 
Este es para publicitar Emergent Ai, como lo use para desarollar mi herramienta pero esto es Founder/ Entrepeneur Led y el otro es para Creator/ Business con problemas de estrategia de contenido, que alimentara lo que MAS debo desarollar en mi curso Creatividad2 y a su vez que videos debo hacer MAS para generar MAS clientes, MAS flywheel submissions y que se retroalimente.

En google consegui: esta data: "Hacer encuestas de necesidades no garantiza el éxito por sí solo, pero reduce el riesgo de fracaso del promedio general (del 30%-45%) a cerca de un 10%-15%. Las encuestas evitan que construyas algo que nadie quiere, validando la demanda antes de invertir. [[1](https://help.letshighlight.com/help/what-percentage-of-new-products-fail), [2](https://www.youtube.com/watch?v=EEyWXB15fpU&t=91), [3](https://easibind.com/80-percent-of-new-products-fail/), [4](https://www.clearlypayments.com/blog/how-long-businesses-survive-and-why-they-fail/), [5](https://www.adimen.es/trabajo-de-campo/)]
Las probabilidades exactas varían, pero el uso de encuestas y el posterior desarrollo basado en ellas mejoran radicalmente los resultados. Varios factores clave explican esta mejora: [[1](https://help.letshighlight.com/help/what-percentage-of-new-products-fail)]

* Lo que dicen los usuarios vs. lo que hacen: Las personas suelen decir que comprarían un producto en una encuesta, pero a la hora de pagar, el comportamiento cambia.
* El riesgo de sesgo: Las preguntas mal formuladas pueden dar una falsa sensación de seguridad (sesgo de confirmación). [[1](https://help.letshighlight.com/help/what-percentage-of-new-products-fail)]
* Validación práctica: Para mejorar aún más tus probabilidades, el siguiente paso lógico no es solo la encuesta, sino la construcción de un Producto Mínimo Viable (MVP). Esto te permite medir el interés real con ventas o interacciones tangibles. [[1](https://translate.google.com/translate?u=https://www.qualtrics.com/articles/strategy-research/minimum-viable-product/&hl=es&sl=en&tl=es&client=sge), [2](https://caroli.org/es/lean-inception-cuando-hacer/)]"
Podriamos hacer un statistic/number hook hablando de que con esta herramienta reduje mi probabilidad de fracaso un 25%.

## 🤖 Claude · 2026-06-16 15:28
Recibido, y corrijo: son dos videos distintos. El del flywheel y el diagnóstico de contenido (Creator/Business) es el OTRO, ese alimenta tu curso y tu calendario. Lo aparco para cuando lo trabajemos. Este, V3, se queda founder-led: cómo usaste Emergent para construir tu herramienta de validación. No le muevo el norte.

Y sí, un stat hook es la dirección correcta para este. Los números son tu fuerte, ya lo viste con los dos mil dólares. Pero tengo que frenarte en el "reduje MI probabilidad de fracaso un 25%", por dos razones, y son importantes para que no se te caiga:

**Uno, es el mismo error de "clientes".** Esa estadística es un promedio general de estudios, no una medición tuya. No has lanzado ni medido tu propio fracaso, así que "reduje MI probabilidad un 25%" no lo puedes probar. La versión defendible atribuye el dato a la investigación y te posiciona usando el método, no inventándote tu resultado personal.

**Dos, "25%" es difuso.** Tu propia data va de 40% a 15%. Dos números reales pegan más fuerte y son más claros que un "25%" suelto. "Del 40% al 15%" es concreto y falsificable, que es justo tu estándar.

Y un flag de marca: en un video pagado, el número va sobre el MÉTODO (validar antes de construir baja el riesgo), no sobre Emergent. Emergent es la herramienta con la que ejecutaste. Así separas el claim de la investigación del producto del sponsor, y Kritika lo aprueba sin que legal lo pique. Ten una fuente creíble lista, tus links de Google son mezcla y algunos son blogs flojos.

Ojo además con algo que tu propia data dice: la gente dice que compraría pero a la hora de pagar cambia. Por eso el número honesto es "baja el riesgo", no "garantiza el éxito".

Hooks defendibles, founder-led:

A. "Casi la mitad de los productos nuevos fracasan. Casi siempre por construir algo que nadie quería. Yo validé el mío antes de construirlo."

B. "Construir a ciegas: 40% de probabilidad de fracaso. Validar antes: 15%. Te muestro la herramienta que usé para validar el mío."

C. "El error que hace fracasar al 40% de los productos nuevos es construir antes de preguntar. Yo hice lo contrario."

Iría con la **B.** Es el stat hook más limpio: dos números reales, el contraste 40 contra 15 frena el scroll, el dato es sobre el método (defendible), y "la herramienta que usé" abre el loop directo al build en Emergent. La A es la narrativa si la quieres menos dura. La C es la de error/curiosidad.

¿Con cuál vamos y cierro el hook de V3?

## 🧑 Adriana · 2026-06-16 15:30
ok quiero dejar para otra sesion el video de diagnostico para que no se me pierda, dame un contexto completo de idea, pitch, data, objetivo, desarollo del quiz, y comenzar una conversacion separada para eso.

## 🤖 Claude · 2026-06-16 15:32
Listo. Aquí está el contexto completo del video de diagnóstico, parqueado y empaquetado. Cópialo y pégalo como primer mensaje en una conversación nueva y arrancas con todo el contexto cargado. Al final te digo qué queda abierto.

---

**VIDEO DIAGNÓSTICO · Creator / Business**
Separado del V3 Emergent (founder-led). No mezclar el norte de los dos. Este le habla directo al dolor del creador.

**IDEA**
Un quiz gratuito que funciona como identificador automático de problemas: le dice a cualquier creador, marca personal o negocio en cuál de las 6 etapas de su creación de contenido se está cayendo. El usuario sale sabiendo su cuello de botella y el primer paso para arreglarlo. Adri sale sabiendo, en agregado, cuál es la mayor necesidad de su audiencia. Las 6 etapas: Estrategia, Pre-producción, Producción, Edición, Distribución, Análisis post-publicación.

**PITCH**
Un quiz gratis que le dice a cualquier creador en cuál de las 6 etapas de su contenido se está cayendo. A él le resuelve dónde enfocar. A Adri le dice exactamente qué enseñar.

**OBJETIVO (el flywheel)**
1. Para el usuario: diagnóstico gratis + primer paso accionable. Razón concreta para completarlo.
2. Para Adri (research): cada submission registra la etapa diagnosticada. En agregado, ve el cuello de botella #1 de su audiencia. Eso dicta qué módulos desarrollar MÁS en el curso Creatividad² y qué videos de tips hacer MÁS.
3. Lead gen + retroalimentación: los videos de tips (con open loop "comenta qué se te dificulta y te ayudo") mandan gente al quiz, el quiz genera más submissions y más data, y el ciclo se alimenta solo.

**DATA**
Stat de validación (originada en la investigación del V3, sirve de fundamento): construir sin validar tiene ~30-45% de probabilidad de fracaso; validar la necesidad antes lo baja a ~10-15%. Caveats: la gente dice que compraría pero al pagar cambia; preguntas mal formuladas dan falsa seguridad por sesgo de confirmación; lo que más valida es un MVP con interacciones reales, no solo la encuesta. Pendiente: sourcear un dato propio de contenido (ej. % de creadores que no sabe en qué etapa falla) con fuente creíble.

**DESARROLLO DEL QUIZ**
Las 6 etapas, qué diagnostica cada una y señales de fallo:
1. Estrategia: POV, pilares, claridad de mensaje, conocer a la audiencia. Falla: contenido sin dirección, no sabe para quién habla, copia tendencias sin criterio.
2. Pre-producción: ideación, guión, hook, planificación. Falla: improvisa, no guioniza, hooks débiles.
3. Producción: grabación, luz, audio, encuadre, b-roll. Falla: mala luz o audio, una sola toma, sin b-roll.
4. Edición: ritmo, cortes, subtítulos, retención. Falla: edición sin ritmo, sin subtítulos, no entiende retención.
5. Distribución: formato por plataforma, caption, timing, SEO semántico. Falla: postea igual en todas, caption flojo, no adapta ni usa SEO.
6. Análisis post-publicación: leer métricas (saves, watch time, shares), iterar. Falla: no mira data, mide likes en vez de saves y retención, no itera.

Mecánica:
- 10 a 15 preguntas, cada una pesa hacia una o más etapas.
- Scoring: se acumula por etapa. La etapa con mayor fricción es el cuello de botella.
- Resultado: "Tu cuello de botella está en [etapa]. Esto es lo que pasa y este es tu primer paso."
- Ruteo: cada resultado manda al contenido u oferta de Creatividad² de esa etapa, invita a la serie de tips de esa etapa, y captura el correo con un incentivo.
- Captura de data: cada submission loguea la etapa diagnosticada para el agregado de research.

**HOOK (punto de partida, sin pulir)**
Carril beneficio: "Si tu contenido no despega, el problema está en una de seis etapas. Este quiz te dice en cuál."

**PENDIENTES / DECISIONES ABIERTAS**
- ¿El quiz del diagnóstico es el MISMO que se construye en Emergent en V3, o uno distinto? Probablemente el mismo, dos ángulos. Confirmar.
- Pulir el hook (carril beneficio).
- Sourcear un dato propio de contenido con fuente creíble.
- Definir el incentivo de captura (descuento, recurso, etc.).
- Registro Creator/Business-led, NO founder-led.

---

Si quieres que no dependa de copiar y pegar, te lo dejo también en un .docx para que lo guardes. Dime y lo genero. Y cuando quieras seguimos con el hook de V3, que ahí lo dejamos en la B.

## 🧑 Adriana · 2026-06-16 15:41
ok, volvamos al video de emergent

## 🤖 Claude · 2026-06-16 15:42
Volvemos. Estado de V3 (Emergent, founder-led): el cuerpo ya lo tienes casi completo en tu dump, los pasos del build, el archivo .md, la base de datos, el CTA de LISHTO. Lo único sin cerrar es el hook. Quedaron dos direcciones vivas:

Stat (mi recomendación): "Construir a ciegas: 40% de probabilidad de fracaso. Validar antes: 15%. Te muestro la herramienta que usé para validar el mío."

Satisfacción (la otra): "Mis clientes van a estar satisfechos con mi producto antes de pagarlo. A propósito."

Iría con la del stat. Dos números reales, el contraste frena el scroll, el dato es sobre el método así que es defendible, y "la herramienta que usé" abre el loop directo al build. La de satisfacción es más conceptual, buena pero menos falsificable.

Si quieres lo mejor de las dos, se fusionan: "El 40% de los productos nuevos fracasan por construir algo que nadie quería. Yo me aseguré de que el mío les gustara antes de venderlo. Te enseño cómo." Esa pega con el número y con la inversión humana a la vez. Es la que yo usaría.

¿Lockeo esa (la fusión) y te armo el cuerpo completo, ya con tu dump pasado por el pressure test? O sea: "impecable" y "COOL" fuera, el .md y la base de datos amplificados como money shots, y el "como coño" lo dejo o lo suavizo según me digas.

## 🧑 Adriana · 2026-06-16 16:06
Construir que? esta vago, no me explica porque a MI como audiencia me conviene ver este video? no esta a prueba de viralidad

## 🤖 Claude · 2026-06-16 16:07
Tienes razón en las tres cosas. El stat es founder-abstracto, "construir qué" es vago, y un número de fracaso no frena el scroll de nadie que no sea ya founder. El stat es para el CUERPO como prueba, no para el hook.

El hook tiene que hacer una cosa que el del stat no hacía: darle al que ve una razón inmediata y concreta para quedarse. Y tu carril más viral es la confesión vulnerable, no la estadística. Ese es el tuyo.

Tres opciones, todas concretas y viewer-first:

A. "Gasté meses construyendo productos que nadie compró. Hasta que invertí el orden: ahora sé qué quiere mi cliente antes de construir nada."

B. "Si vas a lanzar un producto, no construyas nada hasta ver esto."

C. "Dejé que mi cliente diseñara mi producto antes de que existiera. Sin código."

Iría con la **A.** Es tu lane viral: arranca con tu propio fracaso (relatable, vulnerable, la gente se queda porque le ha pasado), es concreta (meses, nadie compró), y "invertí el orden" abre un loop que el video paga. El beneficio para el que ve está implícito y se vuelve explícito en la segunda línea: tú también puedes saber antes de gastar. El stat del 40% al 15% entra justo después como la prueba de que no es solo tu anécdota.

La B es el scroll-stopper más directo si quieres algo más punchy y menos personal. La C es la del método sorprendente, concreta pero menos emocional.

¿Cuál te prende? Y si es la A, el stat lo meto de segundo beat como respaldo.

## 🧑 Adriana · 2026-06-16 16:14
El hook a esta larguiiisimo y habla de mi, no de quien ve el video

## 🤖 Claude · 2026-06-16 16:15
Cierto, todo sobre mí. Lo volteo al que ve y lo corto:

1. "No construyas tu producto antes de ver esto."

2. "Sabe si tu idea va a vender antes de construirla."

3. "Deja que tu cliente diseñe tu producto antes de hacerlo."

La **1.** Corta, te habla a ti que ves, mete el riesgo, y "esto" abre el loop que el video paga. El "yo" y el stat entran después, en el cuerpo.

## 🧑 Adriana · 2026-06-16 16:18
1. Harías un producto sabiendo que va a fracasar?
2. Hook verbal: Implementar esto CASI garantiza un cliente satisfecho. Hook textual: Reduce tu riesgo de fracasar tu lanzamiento del 40% al 15%.

## 🤖 Claude · 2026-06-16 16:19
La 2 es el camino, no la 1 sola. Partir el hook en verbal + textual es la jugada correcta: el audio y el texto se complementan en vez de repetirse. Esa es tu propia regla, y aquí la estás aplicando bien.

La 1 sola se queda corta porque la respuesta es obvia: nadie haría un producto sabiendo que va a fracasar. Pero con un ajuste mínimo se arregla y se vuelve tu hook verbal. El problema no es saber que va a fracasar, es no saber si alguien lo quiere. Cambia eso:

Verbal (hablado): "¿Harías un producto sin saber si alguien lo quiere?"
Textual (en pantalla): "Validar antes baja el riesgo de fracaso del 40% al 15%."

Ahí la pregunta ya no tiene respuesta obvia, le clava la duda al que ve, y el texto le pone el número que lo respalda. No se pisan.

Tu "implementar esto casi garantiza un cliente satisfecho" lo sacaría del hook, "implementar esto" suena corporativo y vago. Pero esa idea de satisfacción es buena, va al cuerpo cuando muestras los resultados del quiz.

Una nota de marca: el "40% al 15%" en pantalla necesita una fuente creíble o un "según estudios" pegado, porque es video pagado y un número solo en pantalla lo pica el equipo legal de Emergent.

¿Te cuadra la dupla así?

## 🧑 Adriana · 2026-06-18 23:09
ok sigamos con mas copy

## 🤖 Claude · 2026-06-18 23:11
Dale. Tomo tu dump del cuerpo y lo paso por el mismo filtro. Aquí está el copy del cuerpo, después del hook:

[Talking head, después del hook]

"Antes de construir mi producto, construí otra cosa primero: una herramienta que hace tres cosas a la vez. Avisa que estoy creando algo, me dice cómo ajustar el producto, y me enseña a quién le estoy vendiendo."

"Traducción: mi cliente va a estar satisfecho con esto antes de pagarlo. A propósito."

"¿Cómo? Un quiz interactivo. Sin saber nada de código, con Emergent."

"La estrategia de rollout te la dejo en otro video."

[Corte a pantalla. Música entra. Screen recording de Emergent + BTS]

"Así lo construí."

[Preguntas] "Las preguntas no son cualquier cosa: cada una me dice qué quiere mi cliente y qué ajustar antes de lanzar."

[Descuento] "A quien lo completa, le doy un descuento. Esa es su razón para terminarlo, y la mía para tener gente lista para comprar."

[Estética de marca] "Le pasé mi estética: mis colores, mis fuentes, mis estrellas."

[Opciones visuales] "Para el look tienes dos caminos: lo dibujas tú misma y subes tus bosquejos, o buscas frames de inspiración."

[Mood board] "Yo subí un mood board de cómo quería que se SINTIERA, no solo de cómo se viera."

[Archivo .md] "Y el detalle que lo cambia todo: un archivo con los do's y don'ts de mi marca. Mientras más claro se lo das, más se parece a ti."

[Emergent + base de datos] "El resto lo hace Emergent: lo construye y conecta una base de datos donde caen todos los submissions."

[Regreso a cámara]

"Comenta LISHTO y te mando el link de ingreso."

Lo que toqué: tu premisa la apreté a las tres funciones limpias y metí tu inversión de satisfacción como remate ("antes de pagarlo, a propósito"). Saqué "COOL" porque no dice nada. El .md y la base de datos quedaron como los money shots, que es donde Emergent demuestra que hace una app, no una página.

Dos cosas tuyas que dejé pendientes: cambié tu "¿cómo coño?" por "¿cómo?" para ir seguros con la marca, pero si quieres tu voz cruda va ahí, solo confírmame que Emergent lo acepta. Y el stat del hook necesita su fuente.

¿Reacciona, qué ajustas?

## 🧑 Adriana · 2026-06-19 04:57
¿Harías un producto sabiendo que va a fracasar?
"4 de cada 10 productos que fracasan, fracasan por una sola razón. A nadie le hacía falta.
(texto en pantalla: Análisis de +100 startups
by CB Insights)
Te tengo una solución que CASI te garantiza un cliente satisfecho.
Es un test interactivo: tu cliente responde unas preguntas, se lleva un resultado que le sirve, y tú te enteras al instante de lo que de verdad necesita, sin tener que adivinarlo.
Una vez más desarollarlo NO es complicado con Emergent Ai. 

1. Dale contexto sobre el aspecto estético de tu marca, guía de marca, stickers, memes, etc.
2. Hazle un bosquejo o subeles inspo.
3. LA PARTE MAS DIFICIL te toca A TI. Debes tener al menos una IDEA de para quien/quienes es. Y en base a cada perfil desarollar preguntas de autodescubrimiento para ellos y REVELADORAS PARA TI. 
4. Debes AJURO conectar tu pixel de facebook a esta app si vas a hacer publicidad.
5. Subscribe a las personas en un flujo en IG una vez que les mandes esto, ya sabes que los llevo a tu marca. 
6. De nuevo Emergent se encargara de enviar todos esos datos a una hoja de calculo como respaldo, enviar el correo con la confirmacion de subscripcion y ya metiste a la persona en tu embudo de ventas. 
Asi lograste ajustar tu estrategia, mejorar tu producto, y alimentar tu relación con la audiencia.
Con la mejor herramienta que puedes tener: Emergent Ai.

## 🤖 Claude · 2026-06-19 04:59
Esto subió de nivel, y el movimiento clave fue el stat. Cambiar el "40 al 15" difuso por "4 de cada 10 fracasan porque a nadie le hacía falta", con CB Insights en pantalla, es real, citable y específico. De paso rescata tu pregunta: "¿harías un producto sabiendo que va a fracasar?" ahora funciona, porque el dato la contesta de una (nadie lo haría a propósito, pero 4 de cada 10 lo hacen sin darse cuenta).

Una nota de diligencia ahí: fija el número exacto de CB Insights antes de ponerlo en pantalla. El "no market need" de ellos anda entre 35% y 42% según la edición. "4 de cada 10" es defendible, pero si citas la fuente, que el número calce clavado con la edición que linkeas.

Lo que pasa el filtro y no toco:
- La explicación del tool: "tu cliente responde, se lleva un resultado que le sirve, y tú te enteras de lo que necesita sin adivinarlo." Clara, beneficio mutuo, concreta.
- El paso 3. "Preguntas de autodescubrimiento para ellos y reveladoras para ti" es el oro del video. Eso nadie más lo dice así.
- El cierre que paga la premisa: ajustar estrategia, mejorar producto, alimentar relación.

Lo que ajustaría:

"Con la mejor herramienta que puedes tener" es la única línea que no pasa tu propio filtro. "La mejor" es superlativo genérico, lo puede decir cualquiera. Al sponsor le encanta, así que es tradeoff, pero un cierre concreto pega más que "la mejor".

El paso 5 está enredado. Limpio: "En cuanto les mandas el resultado, entran a un flujo de Manychat en IG, y ya los tienes en tu mundo."

Dos cosas que se cayeron de la versión anterior, dime si fue a propósito:
- El CTA. No hay LISHTO ni "comenta para el link". ¿Lo reintegro al final?
- El open loop "la estrategia de rollout te la dejo en otro video". Era buena siembra del próximo.

Y ojo al runtime: 6 pasos detallados más la explicación más el stat es mucho. Mientras los 6 se MUESTREN en el screen recording con VO corto, cabe. Si los hablas completos, se va a dos minutos largos.

¿Reintegro CTA y rollout, limpio el paso 5, y te armo la versión completa en copy?

## 🧑 Adriana · 2026-06-19 18:55
Agrega estas dos que lo habia olvidado:

* El CTA. No hay LISHTO ni "comenta para el link". ¿Lo reintegro al final?
* El open loop "la estrategia de rollout te la dejo en otro video". Era buena siembra del próximo.

Y en cuanto a lo que hay que ajustar:

* la mejor herramienta no es emergent ai, la mejor herramienta es lo que DESARROLLÉ con emergent ai. Es el poder de hacer un estudio de mercado.
* como explico de una forma mas clara que sucede con el cliente despues de qu obtiene su promesa y tu obtienes el resultado, porque eso no deberia quedarse asi queria decir "funnel" pero es muy marketero no entenderian

## 🤖 Claude · 2026-06-19 18:56
Resuelvo los dos ajustes y reintegro lo que faltaba.

**El cierre (tienes toda la razón, la mejor herramienta no es Emergent):**

"Y eso es lo que de verdad construiste con Emergent: tu propio estudio de mercado. El poder de saber qué quiere tu cliente antes de invertir un peso en el producto."

Así Emergent queda como el medio, y el premio es la capacidad que tú montaste. Sin "la mejor" genérico, y el sponsor igual sale bien parado porque ellos te lo hicieron posible.

**Lo que pasa con el cliente después (sin decir "funnel"):**

"Fíjate en el intercambio: la persona se lleva un resultado que le sirve, y tú te quedas sabiendo exactamente qué necesita. Pero no termina ahí. Te dejó su correo, ya sabe quién eres, y desde ahí la acompañas hasta que esté lista para comprar. Lo que parecía un quiz, te abrió una relación."

"La acompañas hasta que esté lista para comprar" es el funnel dicho en humano. Nadie necesita saber la palabra para entender la idea. Y "lo que parecía un quiz, te abrió una relación" te cierra el loop de que la herramienta hacía más de lo que aparentaba.

Y en el paso 6, donde decías "ya metiste a la persona en tu embudo de ventas", lo cambias por: "y desde ahí esa persona ya está contigo."

**Rollout loop + CTA, al final:**

"La estrategia de rollout, cómo lanzarlo y a quién, te la dejo en el próximo video."

"Comenta LISHTO y te mando el link de ingreso."

El rollout siembra el próximo video y el CTA cierra con la acción. Los dos juntos al final funcionan: primero los dejas con ganas del siguiente, después les das qué hacer ahora.

¿Te armo ya la versión completa en copy con todo esto integrado para que la veas de corrido?

## 🧑 Adriana · 2026-06-19 19:06
no entendi tus sugerencias de swap para las oraciones, cambiar:

* "Subscribe a las personas en un flujo en IG una vez que les mandes esto, ya sabes que los llevo a tu marca." por "Subscribes a las personas en un flujo que las acompaña hasta que estén listas para comprarte"
* "De nuevo Emergent se encargara de enviar todos esos datos a una hoja de calculo como respaldo, enviar el correo con la confirmacion de subscripcion y ya metiste a la persona en tu embudo de ventas. Asi lograste ajustar tu estrategia, mejorar tu producto, y alimentar tu relación con la audiencia. Con la mejor herramienta que puedes tener: Emergent Ai." por "De nuevo Emergent se encargara de enviar todos esos datos a una hoja de calculo como respaldo, enviar el correo con la confirmacion de subscripcion y ya metiste a la persona en tu mundo digital."
Y agregar apartir de ahi un nuevo ending: "Lo que parecía un quiz, te hizo un upgrade de seguidor a posible comprador y lograrás ajustar tu estrategia, mejorar tu producto, y alimentar tu relación con la audiencia. Un WIN-WIN ayudas REALMENTE a tu audiencia y haces un producto que SI valga la pena. Gracias a Emergent Ai que lo hace TODO posible"
"La estrategia de rollout, cómo lanzarlo y a quién, te la dejo en el próximo video.
Comenta LISHTO y te mando el link de ingreso."

## 🤖 Claude · 2026-06-19 19:08
Aquí está todo integrado con tus swaps y el nuevo ending, de corrido para que lo veas completo:

[Talking head, cámara]

"¿Harías un producto sabiendo que va a fracasar?"

"4 de cada 10 productos que fracasan, fracasan por una sola razón: a nadie le hacía falta."
(Texto en pantalla: Análisis de +100 startups · CB Insights)

"Te tengo una solución que casi te garantiza un cliente satisfecho."

"Es un test interactivo: tu cliente responde unas preguntas, se lleva un resultado que le sirve, y tú te enteras al instante de lo que de verdad necesita, sin adivinarlo."

"Una vez más, desarrollarlo no es complicado con Emergent AI."

[Corte a pantalla. Música entra. Screen recording de Emergent + BTS]

"Así lo construí."

1. "Dale contexto sobre la estética de tu marca: tu guía de marca, stickers, memes, todo."
2. "Hazle un bosquejo o súbele inspo."
3. "La parte más difícil te toca a ti: tienes que tener al menos una idea de para quién es. Y según cada perfil, desarrollas preguntas de autodescubrimiento para ellos y reveladoras para ti."
4. "Si vas a hacer publicidad, ajuro tienes que conectar tu pixel de Facebook a la app."
5. "Subscribes a las personas en un flujo que las acompaña hasta que estén listas para comprarte."
6. "Y de nuevo, Emergent se encarga: manda todos los datos a una hoja de cálculo como respaldo, envía el correo de confirmación de suscripción, y ya metiste a la persona en tu mundo digital."

[Regreso a cámara]

"Lo que parecía un quiz te hizo un upgrade de seguidor a posible comprador. Y lograste ajustar tu estrategia, mejorar tu producto, y alimentar tu relación con tu audiencia."

"Un win-win: ayudas de verdad a tu audiencia y haces un producto que sí vale la pena. Gracias a Emergent AI, que lo hace todo posible."

"La estrategia de rollout, cómo lanzarlo y a quién, te la dejo en el próximo video."

"Comenta LISHTO y te mando el link de ingreso."

Tres notas rápidas:

Limpié solo gramática: "que sí valga la pena" pasó a "que sí vale la pena", y apreté un par de líneas. Tu slang lo dejé intacto (ajuro, upgrade, win-win), es tu voz.

CB Insights: fija el número exacto según la edición que linkees. Su "no market need" anda entre 35% y 42%, así que "4 de cada 10" es defendible, solo que calce con la fuente en pantalla.

Dos cosas que quedaron implícitas y eran fuertes: el archivo .md con do's y don'ts de tu marca quedó folded dentro del paso 1, y el "poder de hacer tu propio estudio de mercado" quedó en el espíritu del cierre, no con esas palabras. Si quieres lucir cualquiera de los dos explícito, los saco aparte.

¿Lo dejamos así y te lo paso a .docx con tu estética, o a copy-paste limpio primero?

## 🧑 Adriana · 2026-06-19 19:12
"tu relación con tu audiencia." y "ayudas de verdad a tu audiencia"
audiencia se siente como muletilla, cual de los dos podria hacerle swap a otra palabra o sinonimo?

## 🤖 Claude · 2026-06-19 19:13
Le haría el swap a la primera, la de "relación con tu audiencia". Dos razones: rompe la repetición, y "relación con tu comunidad" suena más natural. Una relación es con una comunidad, "audiencia" se siente más de broadcast, más fría para la palabra "relación".

Quedaría:

"...y alimentar tu relación con tu comunidad."
"...ayudas de verdad a tu audiencia y haces un producto que sí vale la pena."

Si quieres algo aún más cálido que "comunidad", ahí también entra "tu gente": "alimentar tu relación con tu gente."

Y si prefieres dejar "audiencia" en la primera porque es tu triada de payoff, entonces el swap va en la segunda: "ayudas de verdad a tu gente."

Yo iría por cambiar la primera a comunidad. ¿Cuál prefieres?

## 🧑 Adriana · 2026-06-19 23:14
OK BELLO asi quedo dale

## 🤖 Claude · 2026-06-19 23:16
¡Bello! Te lo armo en el .docx con tu estética para que se lo mandes a Kritika.

Listo el V3, con tu estética completa y listo para Google Docs.

Antes de que se lo mandes a Kritika, en la tabla de aprobación dejé marcados los dos pendientes que dependen de ti o de la marca: fijar el número exacto de CB Insights contra la edición que cites, y confirmar que aceptan el comenta-LISHTO en vez del link en bio.

Con esto tienes los tres videos de la serie cerrados: portfolio, landing y la herramienta de validación. El de diagnóstico de contenido quedó parqueado en su brief para cuando lo retomes.

## 🧑 Adriana · 2026-06-19 23:23
Ok damelo formato copy y paste del script para pasarlo a noiton

## 🤖 Claude · 2026-06-19 23:23
¿Harías un producto sabiendo que va a fracasar?

4 de cada 10 productos que fracasan, fracasan por una sola razón: a nadie le hacía falta.
(en pantalla: Análisis de +100 startups · CB Insights)

Te tengo una solución que casi te garantiza un cliente satisfecho.

Es un test interactivo: tu cliente responde unas preguntas, se lleva un resultado que le sirve, y tú te enteras al instante de lo que de verdad necesita, sin adivinarlo.

Una vez más, desarrollarlo no es complicado con Emergent AI.

Así lo construí.

1. Dale contexto sobre la estética de tu marca: tu guía de marca, stickers, memes, todo.
2. Hazle un bosquejo o súbele inspo.
3. La parte más difícil te toca a ti: tienes que tener al menos una idea de para quién es. Y según cada perfil, desarrollas preguntas de autodescubrimiento para ellos y reveladoras para ti.
4. Si vas a hacer publicidad, ajuro tienes que conectar tu pixel de Facebook a la app.
5. Subscribes a las personas en un flujo que las acompaña hasta que estén listas para comprarte.
6. Y de nuevo, Emergent se encarga: manda todos los datos a una hoja de cálculo como respaldo, envía el correo de confirmación de suscripción, y ya metiste a la persona en tu mundo digital.

Lo que parecía un quiz te hizo un upgrade de seguidor a posible comprador. Y lograste ajustar tu estrategia, mejorar tu producto, y alimentar tu relación con tu comunidad.

Un win-win: ayudas de verdad a tu audiencia y haces un producto que sí vale la pena. Gracias a Emergent AI, que lo hace todo posible.

La estrategia de rollout, cómo lanzarlo y a quién, te la dejo en el próximo video.

Comenta LISHTO y te mando el link de ingreso.

## 🧑 Adriana · 2026-06-20 00:13
Ok dejare este realmente para DESPUES de que lance creatividad2 para no revelar la tactica antes de tener los resultados jejejej, se me ocurrio otra que puede servir FULL y cae un poco en el mismo que el video 1 que se fue viral

## 🤖 Claude · 2026-06-20 00:15
Jajaja sí, total. Aguantar el V3 hasta después del launch te da algo que ahorita no tienes: resultados reales que enseñar. Cuando lo sueltes ya no es "esta táctica funciona," es "miren lo que me dio." Eso lo hace más fuerte.

Dale, suéltame la idea nueva. ¿Qué es y qué la conecta con el del portfolio que explotó?

## 🧑 Adriana · 2026-06-20 00:20
Mi idea es la siguiente, en la colaboracion 1 mi video fue este:
Me cansé de que mi portafolio diera pena ajena. Siempre quise algo demasiado creativo, demasiado yo, algo que estuviese impregnado con mi esencia. Les presento Emergent AI. Emergent es una plataforma donde conviertes tus ideas en objetos reales. Literalmente te encargas de describirle lo que quieres, adjuntar referencias y listo. Ella se encarga de todo lo demás. Digo ella porque me da vibes de mujer, una mujer que resuelve, como tú y como yo. Pero como yo no quiero que des pena ajena como yo, te voy a dar los pasos para tener un portafolio que realmente convierta. Necesitas un hero que te venda, no una biografía. Un hero. Una frase que muestre tu esencia. Básicamente, ¿qué se siente trabajar contigo? Organiza los videos por categorías. Tienes que hacerle el trabajo más fácil a esta persona que quieres que te contrate. Bonus points si pones marcas con las que has trabajado y la etiquetica diciendo qué formato es ese video en específico. Porfis. Adjunta métricas reales. No te abrumes, no necesitas grandes números, necesitas buenos números. Son dos cosas completamente diferentes. Una sección en donde enseñes qué es trabajar contigo. Cómo se sentirá el paso a paso de contratarte a ti. Y tus rates. Sin esconderlos. Sin sugarcoating. Yo sí te los voy a esconder a ti, porque me da pena. Necesitamos tu identidad visual impregnada en todos lados. Tu personalidad. Qué se siente tu contenido. Cómo te sientes tú. Cómo te percibe la gente. Este portafolio es tu carta de presentación. So it better be a good one. Al final, tu trabajo es ser muy específico. Tienes que ser el director creativo de la página web que quieres construir. Yo le di el copy, las direcciones, las secciones que yo quería. Y le hice un mock-up en Canva de cómo quería que se viera. Y él hizo todo lo demás. La verdad es que yo no sé ni verga de websites. Lo único que sí sé es que Mergent me ayudó a hacer algo que yo pensaba que era imposible. Yo sola o que me iba a costar asquerosamente caro. Por eso, te dejo el link en mi biografía y espero que te sirva tanto como a mí. Nos vemos mañana.

para este que seria el video 2 y el otro pasaria a ser el video 3 los invertiria.

1. portfolio
2. herramienta para calcular CUANTO cobrar por colaboracion
3. landing de captura de emails
4. herramienta de market research

quisiera hacer una herramienta interactiva facil donde las personas rellenan sus datos, calculan su % de engagement rates, su experiencia, etc etc te paso la formula que yo uso  para que creemos la formula para la herramienta y luego hacemos el script del video jejej

## 🤖 Claude · 2026-06-20 00:21
Perfecto el reorder. Y de los cuatro, este es el que más gasolina tiene. "¿Cuánto cobro?" es LA pregunta que todo creador se hace y casi nadie contesta de verdad. Eso es save y share casi garantizado, y es puro framework regalado: mismo ADN del portfolio que explotó.

Mándame tu fórmula. Cuando me la pases, dime dos cosas para que la herramienta dé números en los que la gente confíe de verdad y no termine enseñándole a subcotizar:

1. ¿Los derechos de uso, exclusividad y whitelisting van DENTRO de la fórmula o como capa aparte? En un deal real eso se cotiza separado. Si la herramienta lo mete todo en un solo número, la gente va a regalar el usage sin darse cuenta, que es justo donde más plata se deja sobre la mesa.

2. ¿Quieres que escupa un número fijo o un rango? Un rango aguanta mejor la negociación y se siente menos como sentencia.

Con eso armo la lógica, la pruebo con números reales para ver que no escupa locuras, y de ahí saltamos al script. Dale.

## 🧑 Adriana · 2026-06-20 00:24
Solo seria lo que cobras por CREAR el video y POSTEARLO si le van a hacer publicidad eso es separado, si piden derecho a tu imagen de por vida eso es separado. guarda eso que eso es separado. la formula es:

Follower count x ‘average impact level’ x 1.5 = $BASE RATE How do you define the ‘average impact level’ or AIL? There are 4 factors: 👉 Average engagement rate (av. engagement per post x 100, divided by the number of followers) 👉 Collaboration experience (how many years of collab experience you have) 👉 Industry impact (how much of a go-to expert you are in your niche) 👉 Expertise (how much knowledge, skills, and experience you have in your field) For each factor, I want you to give a rating: 0, 1, 2, or 3. Let’s say you have 10,000 followers: 👉 You should have a decent engagement (3-4%) as a small account, so let’s rate it as 2️⃣ 👉 You probably have 1-2 years of collab experience, so the rating is 1️⃣ 👉 You’re recognizable, but not a go-to leader, so 1️⃣ 👉 Let’s say you have a degree along with a small portfolio and client work experience, 2️⃣. Your average “impact level” = [Sum of ratings/4]/100 2+1+1+2 = 6 [6/4]/100 = 0.015% AIL So your base rate per 1 reel = 10,000 x 0.015 x 1.5 = $225.


Hay un par de debilidades aca: como sbaemos que la gente se dara un rate REALISTA en su impact level score?

## 🤖 Claude · 2026-06-20 00:26
Buena pregunta, y das justo en el hueso del tool. Cualquier calculadora que dependa de que la persona se ponga sola una nota 0 a 3 se rompe por los dos lados: el ego se sobrevalora y el impostor se subvalora. Para tu audiencia el riesgo grande es el segundo, gente buenísima poniéndose 1 cuando es 3 y saliendo a cobrar miseria. Eso mata el propósito del video.

El fix es quitarle el autorating a lo que SÍ se puede medir, y anclar lo que no. Tu fórmula no cambia ni un número, cambia de dónde sale cada puntaje:

1. **Engagement, calculado, no autopuntuado.** El tool pide follower count y engagement promedio por post (números que sacan de sus stats), calcula el % con tu misma fórmula y lo convierte solo al 0 a 3. Bandas que propongo, ajústalas: menos de 1% = 0, 1 a 3% = 1, 3 a 6% = 2, 6%+ = 3. Tu ejemplo de 3 a 4% cae en 2, igualito. Aquí nadie se puede mentir.

2. **Experiencia, derivada de años.** Preguntas "¿cuántos años llevas haciendo collabs pagadas?" y el tool mapea: 0 = ninguna, 1 = hasta 2 años, 2 = 3 a 4, 3 = 5+. Tu ejemplo de 1 a 2 años da 1.

3 y 4. **Industry impact y Expertise, ancladas.** Estas dos sí son subjetivas. En vez de un slider abstracto, cada nivel es una frase concreta que la persona elige porque se reconoce en ella. Ejemplo expertise: 0 "apenas aprendiendo", 1 "tengo skills y un portafolio chiquito", 2 "formación más portafolio más clientes reales", 3 "años comprobables con resultados de peso". La gente se ubica más honesta eligiendo el escenario que se le parece que poniéndose una nota.

Con eso 2 factores quedan blindados y 2 quedan anclados. Y arriba mostramos el desglose ("tu engagement real es 2.8%, eso es un 2") para que vean de dónde salió el número.

Dos cosas más del pressure test:

- **El otro hueso:** el follower count pesa demasiado. Como es multiplicador directo y el engagement es solo 1 de 4 factores topados, una cuenta grande con engagement mediocre igual cobra alto. Es el defecto clásico de toda fórmula basada en followers y para un heurístico está bien. Si quieres le metemos un tope o le subimos peso al engagement, pero eso lo decides tú, no lo toco sin que me lo pidas.
- **Detalle técnico:** escribiste "0.015% AIL" pero en la cuenta usas 0.015 como decimal (por eso da $225 y no $2.25). En el tool da igual porque lo hace el código. Si pones la fórmula en pantalla en el video, quítale el "%" o el que la haga a mano se equivoca por 100.

Anotado lo del scope: el base rate es solo crear más postear. Publicidad y whitelisting aparte, derechos de imagen de por vida aparte. Eso va como capa de add-ons encima de la calculadora, no adentro.

Para cerrar el engagement confírmame una sola cosa: ¿qué cuenta como engagement por post, likes más comentarios más saves más shares? Con eso fijo las bandas y armo la lógica completa.

## 🧑 Adriana · 2026-06-20 00:30
lo hara el tool automaticamente, hazme lado a lado la comaprativa de un calculo con mi ejemplo usado basado en followers y al lado basado en engagement con mas peso

## 🤖 Claude · 2026-06-20 00:32
Va. Mantengo tu cuenta igualita (10k followers, experiencia 1, impact 1, expertise 2) y solo muevo el engagement, para que se vea limpio qué cambia.

Las dos lógicas:
- **Actual (followers manda):** Followers × AIL × 1.5, con AIL = (suma de los 4 ÷ 4) ÷ 100.
- **Engagement pesado:** saco el engagement del AIL y lo meto al alcance. Base = (Followers × engagement ÷ 3%) × AIL3 × 1.5, con AIL3 = (suma de los 3 restantes ÷ 3) ÷ 100. El 3% es el benchmark, ajustable.

| Misma cuenta de 10k | Actual (followers) | Engagement pesado |
|---|---|---|
| Tu ejemplo, 3.5% eng | **$225** | **$233** |
| Engagement bajo, 1% | $188 | $67 |
| Engagement alto, 8% | $263 | $533 |

Lo que dice la tabla: con tu fórmula actual, una cuenta muerta (1%) y una cuenta prendida (8%) con los mismos 10k cobran casi igual, $188 contra $263. El follower count aplana todo. Con engagement pesado, esa misma diferencia se abre a $67 contra $533. El precio empieza a seguir la influencia real y no el número de vanidad.

Mi recomendación: **engagement pesado.** Tres razones. Es más honesto. Premia justo a tu audiencia, cuentas chiquitas con engagement brutal, en lugar de la cuenta inflada. Y lo mejor, es coherente con lo que YA dijiste en el video que explotó: "no necesitas grandes números, necesitas buenos números". La calculadora estaría ejecutando tu propia tesis. Eso es oro narrativo para el script.

El único cuidado: a la cuenta grande con engagement pobre le va a dar un número más bajo y eso puede asustar. Se maneja mostrando el resultado como piso más rango, y dejando que los add-ons (publicidad, derechos) sumen encima.

Si te cuadra, fijamos el benchmark (yo arrancaría en 3% y lo subimos si tu audiencia tiende a engagement más alto) y armo la lógica completa del tool. De ahí saltamos al script.

## 🧑 Adriana · 2026-06-20 00:47
cono siento que hay que hacerlo un balance o sea que una cuenta de 10k cobre 67 usd me parece una groseria cuando lo minimo debe ser 150, pero que una cuenta con un egagamente del 6% cobre 263 esta fatal. el tema de la producion tambien es something big y el nicho porque o sea yo cobro por un video entre 700 y 1200 usd ahora y mi engagament es del 5% y tengo 65.100 seguidores

## 🤖 Claude · 2026-06-20 00:51
Coño pero qué dato más útil me diste. Déjame meter TUS números reales a las dos fórmulas, porque ahí se cae la venda. Tu cuenta: 65,100 followers, 5% engagement, y te pongo alto en experiencia, impact y expertise, porque eres eso.

| Tu cuenta real (65.1k, 5%) | Resultado |
|---|---|
| Follower-led | $2,685 |
| Engagement pesado | $4,882 |

Y tú cobras $700 a $1,200. Las dos te disparan muy por encima de lo que cobras.

Elegir entre followers o engagement es la discusión chiquita. Las dos corren calientes cuando subes de tamaño, porque escalan en línea recta y nunca frenan. Balancear dos números inflados te deja un número inflado.

El fix de verdad tiene tres piezas, y dos son tu instinto puro:

1. **Piso.** Mínimo $150, punto. Eso mata el $67 de grosería de una.
2. **Freno arriba.** Mientras más grande la cuenta, la tarifa por seguidor baja un poco, como pagan las marcas en la vida real. Eso es lo que ninguna de las dos fórmulas tiene, y es por lo que tu propia cuenta da $2,600 en papel.
3. **Producción y nicho como multiplicadores encima.** Tienes toda la razón que son big. Un video producido en un nicho con presupuesto (tech, finanzas, beauty con marcas grandes) no vale igual que un talking head rápido en un nicho sin plata, aunque tengan los mismos stats. Entran como × sobre la base.

Con piso abajo y freno arriba calibrados a TU cuenta, el extremo chiquito y el grande por fin cuadran.

Ahora la pregunta que decide todo el calibre: tu $700 a $1,200, ¿es tu número justo o te estás cobrando por debajo? Tu propia fórmula te ve como creadora de $2,000+. Eso casi siempre significa una de dos cosas: o estás dejando plata en la mesa, o tu nicho tiene techo de presupuesto y por eso cobras eso. Solo tú sabes cuál, y el número que me des es el ancla con la que calibro el freno.

Dame ese número y te devuelvo la tabla recalibrada, cuentas de 10k y la tuya, con producción y nicho ya metidos. De ahí, script.

## 🧑 Adriana · 2026-06-20 01:02
yo estoy for sure for sure, underselling me, pero o sea, en definitiva estoy cobrando poco para algunas marcas pero no soy yo el tema. 

pero una persona por ejemplo hagamos este contraste:
10k seguidores
nicho: fashion, beauty y travel
esta calculando para: seguros
engagement rate: 8%
anos en la industria: 1
nivel de produccion: basico

vs.

10k seguidores
nicho: fashion, beauty y travel
esta calculando para: seguros
engagement rate: 5%
anos en la industria: 1
nivel de produccion: elevado

10k seguidores
nicho: fashion, beauty y travel
esta calculando para: travel
engagement rate: 8%
anos en la industria: 1
nivel de produccion: basico

vs.

10k seguidores
nicho: fashion, beauty y travel
esta calculando para: travel
engagement rate: 5%
anos en la industria: 1
nivel de produccion: elevado

como variarian esos calculos?

## 🤖 Claude · 2026-06-20 01:04
Entonces dejamos tu rate fuera del cálculo y calibro a mercado sano. Así tú quedas como la que sabe y no como la vara de medir.

Y ojo, lo que metiste es fino. Aquí hay DOS nichos: el tuyo (fashion/beauty/travel) y el de la marca para la que cotizas (seguros o travel). El multiplicador lee el cruce. Seguros está fuera de tu nicho pero tiene bolsillos hondos, y las dos cosas empujan el precio hacia arriba, te pagan por alcance y por estirar tu feed a algo off-brand. Travel es tu casa, fit perfecto y presupuesto moderado, así que se queda en la base.

El modelo queda así (los multiplicadores son diales, los movemos cuando quieras):
- **Base** = followers + engagement, con piso de $150.
- **× Producción:** básico 1.0, elevado 1.35.
- **× Categoría de marca:** seguros 1.3, travel 1.0.

| Escenario (10k, 1 año) | Base (eng) | Producción | Categoría | Total |
|---|---|---|---|---|
| A · seguros · 8% · básico | $270 | ×1.0 | ×1.3 | **$351** |
| B · seguros · 5% · elevado | $203 | ×1.35 | ×1.3 | **$355** |
| C · travel · 8% · básico | $270 | ×1.0 | ×1.0 | **$270** |
| D · travel · 5% · elevado | $203 | ×1.35 | ×1.0 | **$273** |

Lo que dice la tabla:
- La categoría de la marca es la palanca más fuerte aquí. Seguros paga +30% sobre travel en todos los casos. Estés como estés de engagement o producción, cotizarle a seguros vale más.
- Engagement alto con producción básica (A y C) y engagement medio con producción elevada (B y D) salen casi iguales. En este default, subir producción compensa bajar engagement y al revés. Ese es el balance que pediste.

El dial que tienes que decidir: ¿te cuadra que producción y engagement pesen casi igual, o uno debe mandar sobre el otro? Si producción elevada debe valer más, la subo a 1.5. Si el engagement manda, le empino la curva. Dime para dónde y lo dejo fijo. De ahí, script.

## 🧑 Adriana · 2026-06-20 01:24
ves? no tiene sentido como lo calculas si mi nicho es travel y el video ES de travel hay demasiada relevancia de contenido deberia ser MAS caro aunque la industria de seguros pague mas

## 🤖 Claude · 2026-06-20 01:26
Tienes toda la razón y lo tenía al revés. Castigué la relevancia cuando la relevancia es justo lo que más vale. Un creador de travel vendiendo travel convierte muchísimo mejor para esa marca que vendiendo seguros, así que ahí el precio sube, no baja.

El arreglo es separar lo que yo había metido en un solo multiplicador. Son dos palancas distintas que a veces jalan para lados opuestos:
- **Relevancia / fit** (tu nicho vs el de la marca): es el value driver. Fit perfecto 1.4, adyacente 1.0, off-niche 0.85.
- **Presupuesto de industria** (qué tan rica es la industria de la marca): seguros alto 1.3, travel medio 1.0. Sube el número, pero no manda.

Calibré la relevancia fuerte para que GANE, que es lo que dijiste. Mira:

| Escenario (10k, 1 año) | Base × Prod | Relevancia | Industria | Total |
|---|---|---|---|---|
| A · seguros · 8% · básico | $270 | ×0.85 | ×1.3 | **$298** |
| B · seguros · 5% · elevado | $274 | ×0.85 | ×1.3 | **$303** |
| C · travel · 8% · básico | $270 | ×1.4 | ×1.0 | **$378** |
| D · travel · 5% · elevado | $274 | ×1.4 | ×1.0 | **$384** |

Travel le gana a seguros en todos los casos, ~27% más, aunque seguros sea la industria más rica. La razón en números: el deal de travel combina fit perfecto × industria media = 1.4. El de seguros combina off-niche × industria rica = 1.105. La relevancia se come la ventaja de presupuesto. Seguros igual cobra decente porque su bolsillo lo levanta, pero estar fuera de tu nicho le quita el premio.

El dial que confirmas: ¿ese ~27% de premio por fit perfecto se siente correcto, o quieres que la relevancia pegue aún más duro? Si un deal en tu nicho debe valer muy por encima de uno off-niche rico, le abro más el espacio entre 1.4 y 0.85. Dime y lo fijo.

## 🧑 Adriana · 2026-06-20 01:27
ok recalibremos pero esta cuenta tiene 60 mil seguidores

## 🤖 Claude · 2026-06-20 01:28
Recalibrado a 60k. Aquí entra el freno que te prometí. Si escalara en línea recta, 60k daría números absurdos. Acuérdate que con el método viejo tu cuenta daba $2,685. El freno hace que la tarifa por cada mil baje mientras la cuenta crece, igual que pagan las marcas en la vida real:

| Tramo de followers | $ por cada 1k |
|---|---|
| Primeros 10k | $18 |
| 10k a 50k | $12 |
| 50k a 150k | $8 |
| 150k+ | $5 |

Para 60k eso suma $740 de base por followers. Encima entra el engagement:
- 8% → base $1,110
- 5% → base $833

Y ya con los mismos diales (producción, relevancia, industria):

| Escenario (60k, 1 año) | Base × Prod | Relevancia | Industria | Total |
|---|---|---|---|---|
| A · seguros · 8% · básico | $1,110 | ×0.85 | ×1.3 | **$1,227** |
| B · seguros · 5% · elevado | $1,125 | ×0.85 | ×1.3 | **$1,243** |
| C · travel · 8% · básico | $1,110 | ×1.4 | ×1.0 | **$1,554** |
| D · travel · 5% · elevado | $1,125 | ×1.4 | ×1.0 | **$1,575** |

Lo que pasó:
- El freno funcionó. 60k no se disparó. Los números viven entre $1,227 y $1,575, rango sano y hasta conservador para esa cuenta.
- Travel le sigue ganando a seguros, ~27%, igualito que en 10k. La lógica de relevancia aguanta a cualquier tamaño.
- El salto de 10k ($298 a $384) a 60k ($1,227 a $1,575) es como 4x, no 6x. Ese es el freno trabajando. 6 veces más seguidores no te dan 6 veces el precio.

El modelo ya se porta bien en chiquito y en grande, con piso, freno y los tres multiplicadores. Si los tramos del freno te cuadran ($18 / $12 / $8 / $5 por mil), lo dejo fijo y armo la lógica completa. De ahí, script.

## 🧑 Adriana · 2026-06-20 01:34
cuando calculemos el presupuesto de la industria creo que podemos ajustar la formula, cual es el cpa average de esa industria? agreguemoslo a la relevancia, si es un value driver, calcula el numero de personas APROX que interactuan X  de cada X seguidores por el numero de CPA que tiene esa industria y eso lo evaluas. Porque yo ahorita digamos estoy empezando en el nicho de tech, tengo un a;o, aunque tenga 3 a;os de experiencia como creadora. PERO cuando me posicione con marcas que me respalden olvidate, mis numeros suben. Y ojo la relevancia de tech vino porque cambie el norte y el nicho de mi contenido en enero del a;o pasado y todo mi engagement nuevo y seguudores nuevos tienen que ver con crear contenido, editar, gear, herramientas, trucos hacks etc. y ahora que se sobre el CPA y tengo un numero que respalda la conversion de mis recomendaciones, puedo usarlo como leverage.

## 🤖 Claude · 2026-06-20 01:37
Brutal idea, y le diste al corazón. El CPA es lo más real que existe para defender un precio, porque es plata que la marca YA gasta por cliente. Ese es tu leverage de verdad.

Cómo entra el CPA a la fórmula: valor que le entregas a la marca = gente que interactúa × conversión × CPA de la industria.
- Gente que interactúa = followers × engagement.
- Conversión = la relevancia. On-niche convierte alto, off-niche convierte bajito.
- CPA = lo que vale cada cliente para esa industria.

Pero ahí está el detalle que tienes que ver, porque te voltea lo de travel. El CPA de seguros es como 20x el de travel. Mira tu cuenta de 60k a 5%, 3,000 personas que interactúan:

| Deal | Conversión (relevancia) | CPA | Valor a la marca |
|---|---|---|---|
| Travel (tu nicho) | 2% → 60 clientes | ~$25 | ~$1,500 |
| Seguros (off-niche) | 0.3% → 9 clientes | ~$500 | ~$4,500 |

Aunque conviertas 7 veces peor en seguros, le entregas 3x más valor, porque cada cliente de seguros vale un platal. Si meto el CPA como multiplicador de precio directo, seguros le gana a travel y se te cae la tesis de relevancia.

Mi recomendación para no romper tu lógica: que el CPA salga como NÚMERO DE LEVERAGE al lado del precio, sin tocar el precio.
- El precio se queda anclado a base + engagement + producción + relevancia. Ahí la relevancia sigue ganando, tu nicho sigue premium, tu stance intacto.
- Y el tool escupe aparte la línea de negociación: "tu audiencia puede generar ~9 conversiones que a un CPA de $500 valen ~$4,500 para esta marca". Esa frase es la que usas para empujar el fee, sobre todo con industrias ricas.

Así la relevancia gana el precio y el CPA gana la mesa. Que es exactamente lo que pediste: un número que respalda la conversión de tus recomendaciones, listo como leverage.

Y conecta con tu posición real: en tech eres fit perfecto, todo tu engagement nuevo es content creation, gear, edición, hacks. Tu precio sale premium por relevancia y tu línea de leverage usa el CPA de tech/SaaS, que es decente. Conforme te respalden marcas, sube tu autoridad y suben los dos números. Lo de "1 año en tech pero 3 de creadora" es buen catch, separo los dos tenures: autoridad en el nicho (1 año, alimenta relevancia) y oficio de creadora (3 años, alimenta producción y base).

Los CPA exactos por industria los saco reales cuando armemos el tool. Los de arriba son ballpark para enseñarte el mecanismo.

Una sola cosa para cerrar: ¿vas con CPA como línea de leverage al lado del precio, o lo quieres como multiplicador del precio aunque eso deje que seguros le gane a travel?

## 🧑 Adriana · 2026-06-20 01:44
Y si en vez de CPA es CPL?

## 🤖 Claude · 2026-06-20 01:45
Mejor todavía. CPL le pega más a lo que de verdad haces.

Piénsalo: lo que tu contenido mueve es el lead. El click, el email, el DM, el signup. La venta final la cierra la marca con su propio proceso, que tú no controlas. CPA te hace cobrar crédito por todo el embudo, y una marca viva te lo discute. CPL cobra crédito por lo que sí mueves y se atribuye a tu link o tu código. Un número que nadie te puede tumbar es mejor leverage que un número grande que te discuten.

Y para TI es perfecto. Todo lo que estás construyendo, la landing de captura, el quiz de validación, los flujos de Manychat, es una máquina de leads. CPL es literalmente la métrica de lo que produces. Tu línea de negociación se vuelve "te genero leads a $X cuando tu CPL pagado es $Y".

Cómo cambian los números (misma cuenta 60k a 5%, 3,000 que interactúan):

| Deal | Leads que mueves | CPL | Leverage |
|---|---|---|---|
| Travel (tu nicho) | ~150 | ~$4 | ~$600 |
| Seguros (off-niche) | ~30 | ~$25 | ~$750 |

Con CPA la brecha era $1,500 vs $4,500. Con CPL es $600 vs $750, casi pegados. El CPL comprime la diferencia entre industrias, porque el costo de un lead no se dispara como el de un cliente cerrado. Y eso te conviene, porque deja tu leverage más alineado con tu tesis de relevancia.

Mi recomendación: CPL como default para la línea de leverage. CPA lo guardas solo para deals explícitos de venta o afiliados, donde sí te toca fondo de embudo. Lo demás queda igual, el CPL va al lado del precio como leverage y no toca el precio.

Los CPL reales por industria los saco cuando armemos el tool. ¿Lo fijo así, CPL default?

## 🧑 Adriana · 2026-06-20 01:55
calcula en este ejemplo:
Cómo cambian los números (misma cuenta 60k a 5%, 3,000 que interactúan):
DealLeads que muevesCPLLeverageTravel (tu nicho)~150~$4~$600Seguros (off-niche)~30~$25~$750

pero cada una con la variable de produccion de video alta y otro bajo

## 🤖 Claude · 2026-06-20 01:57
Ojo aquí, porque producción y leverage viven en columnas distintas. La producción mueve el PRECIO, tu craft cuesta más. No mueve el leverage. El leverage es leads × CPL, y la marca recibe los mismos leads la grabes con iPhone o con crew completo. Así que dentro de cada nicho el leverage no se mueve, lo que se parte es el precio.

| Escenario (60k, 5%) | Producción | Precio | Leverage (CPL) |
|---|---|---|---|
| Travel (tu nicho) | baja | $1,166 | ~$600 |
| Travel (tu nicho) | alta | $1,574 | ~$600 |
| Seguros (off-niche) | baja | $708 | ~$750 |
| Seguros (off-niche) | alta | $956 | ~$750 |

Dos cosas que saltan:

1. El precio de seguros bajó (antes $1,243, ahora $708 a $956). Es porque sacamos el premio de industria del precio y lo mandamos al leverage. Quedó donde debe estar.

2. Aquí está el oro del modelo. Fíjate dónde el leverage le gana al precio:
- En travel, el leverage de $600 es MENOR que tu precio ($1,166+). Ese número no te ayuda, te delata. En deals de tu nicho con CPL bajito, ni lo muestres. Cobras premium por relevancia y calidad de audiencia, y por ahí justificas.
- En seguros, el leverage de $750 está pegado o por encima del precio ($708 a $956). Ahí el número es tu arma. Le dices "te entrego ~$750 en valor de leads y te cobro $956", y empujas para arriba.

O sea, el tool no solo te da un precio. Te dice con cuál de los dos números pelear según el deal. Nicho propio, peleas con relevancia. Industria rica off-niche, peleas con el CPL.

¿Te cuadra esa lógica? Si sí, el modelo ya está bastante completo y podemos pasar a definir el script del video.

## 🧑 Adriana · 2026-06-20 01:58
ah eso queria ver el precio totalll

## 🤖 Claude · 2026-06-20 01:58
Jaja sí, esa columna de Precio ES el total, con todo adentro: base, engagement, piso, freno, producción y relevancia. Ese es el número que cobras. El CPL vive aparte como leverage, solo para empujarlo en la mesa.

La lógica del modelo ya está cerrada. Lo único que queda para cuando lo armes en Emergent son los CPL reales por industria y afinar los diales finales, y eso lo sacamos en el build.

¿Le entramos al script del video?

## 🧑 Adriana · 2026-06-20 02:00
para ver la formula y la logica del video, escribemelo estilo prompt, y generame un html interactivo para ver

## 🤖 Claude · 2026-06-20 02:04
Te dejo las dos cosas. Primero el prompt para que se lo pases a Emergent, después el HTML para que juegues con los números.

Aquí va el prompt para Emergent:

---

**PROMPT — Calculadora de tarifas para creadores (Creatividad²)**

Quiero una calculadora web interactiva de una sola página. El creador mete sus datos y le sale cuánto cobrar por **crear y postear un video** (un reel/post). NO incluye publicidad/whitelisting ni derechos de imagen, eso se cotiza aparte y se menciona como nota.

**Inputs que llena el usuario:**
1. Seguidores (número)
2. Interacciones promedio por post (likes + comentarios + saves + shares). Con esto calculas el engagement solo: `(interacciones ÷ seguidores) × 100`. Así nadie se autopuntúa.
3. Autoridad: Emergente / Establecido / Autoridad respaldada por marcas
4. Producción: Básico / Intermedio / Alto
5. Relevancia (qué tanto cuadra tu nicho con el de la marca): Perfecto / Adyacente / Off-niche
6. Industria de la marca (define el CPL): cada una trae su CPL promedio, más opción manual

**Fórmula del PRECIO** (este es el número que cobra):
`PRECIO = Base × Autoridad × Producción × Relevancia`, con piso de $150.

- **Base** = dólares-por-followers × multiplicador-de-engagement
  - Dólares-por-followers (escalonado, la tarifa por mil baja mientras creces): primeros 10k a $18 c/1k · 10k-50k a $12 · 50k-150k a $8 · 150k+ a $5
  - Multiplicador-de-engagement = `0.5 + (engagement% ÷ 8)`
- **Autoridad:** Emergente 0.9 · Establecido 1.0 · Respaldada 1.2
- **Producción:** Básico 1.0 · Intermedio 1.15 · Alto 1.35
- **Relevancia:** Perfecto 1.4 · Adyacente 1.0 · Off-niche 0.85

**Línea de LEVERAGE (CPL)**, aparte, NO suma al precio:
`Leverage = leads × CPL`
- Leads = `(seguidores × engagement%) × tasa-de-lead`
- Tasa-de-lead por relevancia: Perfecto 5% · Adyacente 2.5% · Off-niche 1%
- CPL según la industria seleccionada

**Output:**
- Engagement % calculado
- PRECIO TOTAL grande y claro
- Desglose de base y multiplicadores
- Línea de leverage: "tu audiencia genera ~X leads, que a un CPL de $Y valen ~$Z para esta marca"
- Consejo dinámico: si leverage ≥ precio, "usa este número en la negociación". Si leverage < precio, "no lo muestres, justifica con relevancia y calidad de audiencia"

**Estética (mi marca):** fondo lavanda #F2E9FF, negro #000000, rojo #D72323 para el precio y acentos, amarillo #FFBA35, azul #3846C4. Títulos en Poppins Bold. Estrellas ★ como acento. Limpio, editorial, mixed media sin miedo.

---

Ahora el HTML:

Ábrela con doble click y juega con los diales. La dejé montada en tu ejemplo de 60k (60,000 seguidores, 3,000 interacciones = 5%, travel perfecto, producción alta), así que de entrada vas a ver el precio ~$1,573 y el leverage ~$600, igualito a lo que cuadramos. Mueve relevancia a off-niche y la industria a seguros para ver cómo el tip cambia de "no lo muestres" a "úsalo en la negociación".

Los CPL y las tasas de lead son ballpark para el prototipo. Cuando lo montes en Emergent, esos son los que cambias por los reales.

¿Le entramos al script del video o quieres tocar algún dial primero?

## 🧑 Adriana · 2026-06-20 02:05
Quiero que sea pregunta, siguient epegunta como una app donde no ves tood completo solo ensena abajo una barra de cuanto te falta para ver tu rate

## 🤖 Claude · 2026-06-20 02:08
Me encanta, así es mucho más app y mantiene a la persona enganchada hasta el reveal. Te la rehíce como flujo de una pregunta a la vez con la barra abajo.

Así quedó el flujo:

Pantalla de inicio con "Empezar", después una pregunta a la vez (seguidores, interacciones, autoridad, producción, relevancia, industria), y abajo fija la barra roja que se llena y te dice "Pregunta X de 6". Cerca del final cambia a "Ya casi ves tu número", y solo al responder las 6 se revela tu tarifa.

Detalles que metí pensando en la conversión:
- Las preguntas de opción única avanzan solas al tocarlas, se siente app.
- El engagement se calcula solo en la pregunta 2, nadie se autopuntúa.
- El reveal trae el precio grande, un "ver desglose" plegable, y abajo tu línea de leverage con el tip dinámico.

Pruébala y dime si el ritmo te cuadra. Si sí, esto ya es el prototipo exacto que le describes a Emergent con el prompt de arriba, y de ahí podemos pasar al script del video.

## 🧑 Adriana · 2026-06-20 02:10
deja el boton de atras siguiente all throughout

## 🤖 Claude · 2026-06-20 02:11
Hecho, te pongo Atrás y Siguiente en cada paso y le quito el auto-avance para que el flujo sea consistente.

Ahora quito el auto-avance del JS para que Siguiente sea la única forma de avanzar:

Listo. Ahora cada paso tiene Atrás y Siguiente, incluido el reveal, y elegir una opción solo la marca sin saltar sola. Las preguntas de opción ya vienen con un default seleccionado (Establecido, Alto, Perfecto, Travel), así que puedes darle Siguiente directo o cambiarla antes.

¿Te cuadra así el flujo, o seguimos afinando antes de pasar al script?

## 🧑 Adriana · 2026-06-20 02:13
y estas seleccionando la industria y el para el CPL y no esta variado deberia quizas sugerir abajo tipo mira esto es lo que ellos pagarian basado en el CPL este es tu piso si te quieren pagar menos que eso estan robandote y deja un disclaimer, esto NO incluye Usage Rights, Whitelisting, Spark Ads o Perpetuity Usage

## 🤖 Claude · 2026-06-20 02:17
Buen ojo. Lo de la industria es a propósito: el CPL mueve tu leverage, no tu rate. Tu rate habla de ti, el CPL habla de ellos. Pero tienes razón que ahorita se siente flojo, así que lo convierto en piso con actitud y le meto el disclaimer exacto.

Cambios en el reveal:

- El número grande ahora es **TU PISO**, con tu línea: "Si te ofrecen menos, te están robando".
- Abajo, la tarjeta de CPL dice "lo que vales para ellos": basado en el CPL, tu audiencia vale ~$Z para esa marca. Y el tip cambia según la industria, cuando el CPL es alto te dice "tu piso sube, pídeles hacia $X, les sales barata", cuando es bajo te dice que defiendas con relevancia.
- Disclaimer en caja punteada: **NO** incluye Usage Rights, Whitelisting, Spark Ads ni Perpetuity Usage.

Una decisión que tomé y quiero que la valides: dejé el piso anclado a tu rate, no al número del CPL. La razón es que el CPL es lo que vales para ELLOS, o sea tu techo y tu munición para pedir más. Si pones el valor completo del CPL como piso duro, en industrias ricas te puede dar un número inflado (tipo $4,500 para seguros) y te arriesgas a que te ghosteen por pedir de más. Por eso el piso es tu rate y el CPL es para empujar hacia arriba.

Si tú lo quieres literal, que el piso SEA el número del CPL, te lo cambio en un toque. ¿Lo dejo así o lo volteo?

## 🧑 Adriana · 2026-06-20 02:22
perfecto ahora si, mi logo y mi favicon, me gustaria ver que posibilidad hay de cambiar ese color de fondo, quisiera el azul o amarillo de mi marca de fondo como repropondrias se ve?

## 🤖 Claude · 2026-06-20 02:27
Buenísimo, el logo y el favicon le van a dar el toque de marca que le faltaba. Déjame primero revisar los archivos y de ahí te lo armo.

El logo es transparente, perfecto para ponerlo sobre cualquier color. Va a quedar brutal sobre el azul. Déjame ver el archivo actual y armar la versión azul.

El logo es transparente y de altísima resolución, así que lo escalo y lo embebo junto al favicon para que el archivo siga siendo uno solo, como te gusta. Mi reproposición es **azul de fondo**: tu logo (rojo + amarillo) y los acentos amarillos explotan sobre el azul, se siente premium, y las tarjetas blancas mantienen todo legible en el flujo largo. El amarillo de fondo te mataría el wordmark amarillo y los acentos, por eso voy con azul.

Quedó en azul con tu marca:

- Tu logo (estrella roja + wordmark amarillo) arriba a la izquierda, se ve brutal sobre el azul.
- Favicon puesto, así que en la pestaña del navegador sale tu estrella AM.
- Texto de las preguntas en blanco, acentos y estrellas en amarillo, el precio enorme en blanco con el `$` rojo.
- Las tarjetas blancas y la de leverage en negro flotan limpias sobre el azul, así el flujo largo sigue fácil de leer.
- Disclaimer y barra de progreso intactos.

Todo embebido en un solo archivo, como te gusta.

¿Te late el azul, o quieres que te genere la versión amarilla para comparar lado a lado antes de decidir?

## 🧑 Adriana · 2026-06-20 02:28
mi logo se ve muy pequeno, creo que no se lee muy bien

## 🤖 Claude · 2026-06-20 02:29
Tienes razón, ese wordmark a ese tamaño no se lee. El archivo original trae mucho espacio transparente alrededor, así que lo recorto al contenido y lo agrando bastante.

Listo. Recorté el espacio transparente (el logo real era 3:1) y ahora se muestra mucho más grande y responsive, entre 210 y 310px de ancho según la pantalla. Quité el textito de al lado para darle aire. Ahora sí se lee el wordmark.

Si lo quieres aún más grande, o centrado en vez de a la izquierda, dime y lo ajusto.

## 🧑 Adriana · 2026-06-20 02:31
te paasaste ahora es GIGANTE y quitaste el "¿Cuanto Cobrar?" de arruba lo pudieses poner justificado a la derecha si acaso

## 🤖 Claude · 2026-06-20 02:32
Jaja me pasé. Lo bajo a un tamaño normal y te devuelvo el "¿Cuánto cobrar?" justificado a la derecha.

Ahora sí, tamaño normal (56px de alto, ya recortado así que se lee bien) a la izquierda, y "¿Cuánto cobrar?" en amarillo justificado a la derecha.

¿Así te cuadra el header? Si quieres que el logo sea un pelín más grande o más chico, es un número y te lo muevo.

## 🧑 Adriana · 2026-06-20 02:33
bien pero el logo y el cuanto cobrar no tienen el mismo padding que el contenido de la pagina como tal

## 🤖 Claude · 2026-06-20 02:34
Buen ojo. El header iba a ancho completo y el contenido va en una columna centrada de 600px, por eso no cuadraban. Lo meto en el mismo contenedor para que alineen.

Listo. Ahora el logo a la izquierda y "¿Cuánto cobrar?" a la derecha quedan dentro de la misma columna de 600px que las preguntas, así que el borde izquierdo del logo se alinea con el texto del contenido y el "¿Cuánto cobrar?" con el borde derecho. En pantallas chicas mantienen el mismo margen de 22px que el resto.

¿Quedó cuadrado el borde ahora?

## 🧑 Adriana · 2026-06-20 02:50
me gustaria poner un gif que le da humor a la portada un sello muy yo y un gif para la pagina de resultados, antes de cambiar todo el html, proponme en imagen 4 layouts posibles para cada pagina

## 🤖 Claude · 2026-06-20 02:54
Esos gifs son perfectos: el gatico con el spinner para el momento "calculando" y el corgi engreído para el reveal, puro sello tuyo. Antes de tocar el HTML, te armo las opciones en mockup para que elijas.

Esos gifs son perfectos: el gato del spinner = humor de portada, el corgi engreído = el remate del resultado. Ojo, los colores siguen siendo tu marca (azul, rojo, amarillo); estos wireframes son solo para que veas DÓNDE cae el gif. Aquí van las 4 opciones de portada:

Las cuatro de portada en corto: **A** mete el gato arriba como sello sobre el título, **B** parte la pantalla con texto a la izquierda y gato a la derecha, **C** lo deja de sticker asomándose en la esquina, **D** lo enmarca tipo polaroid entre título y botón.

Ahora las 4 de la página de resultados (corgi):

Resultados en corto: **A** corgi arriba reaccionando al número, **B** corgi al lado del precio (timing de comedia, "aquí está tu número" + cara de engreído), **C** sticker pegado al precio como calcomanía, **D** corgi de cierre abajo junto a "calcular otra".

Mi pick si me preguntas: **portada C** (sticker asomándose, es lo más "sello tuyo") y **resultados B** (el corgi al lado del número remata perfecto). Pero tú mandas.

Dime qué combo quieres, tipo "portada C, resultados B", y de ahí sí toco el HTML.

## 🧑 Adriana · 2026-06-20 03:08
portada: c
resultado: b 

deberia agregar un form capture al final?
tipo: te gusto esta herramienta? dejame tu correo y por ahi sigo compartiendo cosas cool para creadores, entrepeneurs y marcas

## 🤖 Claude · 2026-06-20 03:10
Sí, 100% deberías, y tu instinto de ponerlo AL FINAL (después de mostrar el resultado, sin tapar el número) es el correcto. Gatear el rate detrás del correo mataría lo viral. Así regalas el valor, capturas en el punto de máxima buena onda ("ya vi mi número") y alimentas tu lista, que es justo el motor de Creatividad².

Un upgrade a tu copy: en vez de "cosas cool" genérico, amárralo a lo que acaban de recibir y, si puedes, cuelga un freebie concreto (tipo "te mando mi plantilla de rate card"). Eso sube el opt-in muchísimo más que un "te comparto cosas". Te lo dejo armado con tu copy y tú decides si le metes el freebie.

Déjame revisar los gifs y armo todo: portada C, resultados B, y el form al final.

## 🤖 Claude · 2026-06-20 03:13
Ya los revisé: ambos 1080×1080, 400 frames, ~1.9MB cada uno. Crudos no caben (el archivo quedaría en +5MB). Los reduzco a ~300px y bajo frames manteniendo la animación, y de ahí los incrusto. Déjame ver el HTML actual para no romper nada.

HTML confirmado. Armo todo en un solo paso: reduzco los gifs, monto **portada C** (gato sticker en la esquina), **resultados B** (corgi al lado del precio) y el **form de captura** al final con tu copy.

Listo. Quedó en ~890KB, self-contained, con la animación viva.

Ábrela y mira: el gatico asomándose en la esquina de la portada y el corgi al lado del número en resultados. Dos notas rápidas:

El form es prototipo, captura visual con su "¡Listo!" pero no guarda el correo todavía. En Emergent lo cableas a MailerLite o Resend (o lo metes por Manychat) para que entre a tu lista de verdad.

Si quieres exprimir el opt-in, cambia la línea por algo con freebie concreto, tipo "déjame tu correo y te mando mi plantilla de rate card". Un regalo tangible convierte mucho más que "cosas cool". Te lo dejé con tu copy original; si decides el freebie, me dices y lo ajusto en 2 segundos.

¿Seguimos con el guión del video de la calculadora? Era el siguiente paso antes de meternos con los gifs.

## 🧑 Adriana · 2026-06-20 03:15
no hay manera de hacer el gif pase 1.5X mas rapido?

## 🤖 Claude · 2026-06-20 03:15
Sí, fácil. Es solo bajar la duración de cada frame. Lo dejo a 1.5X y vuelvo a incrustar ambos gifs.

Hecho. Ambos gifs ahora corren a 1.5X (167ms por frame en vez de 250ms), mismo peso del archivo.

Ábrela y checa el ritmo. Si lo quieres aún más rápido (2X) o más lento, me dices el número y lo ajusto.

¿Arrancamos con el guión del video de la calculadora?

## 🧑 Adriana · 2026-06-20 03:16
quitales el borde a los gifs

## 🤖 Claude · 2026-06-20 03:16
Listo, les quité el borde blanco (y la sombrita que iba con él) a los dos gifs. El gato mantiene su rotacioncita de sticker y las esquinas redondeadas; el corgi queda limpio al lado del precio.

¿Te late así o quieres que también le quite las esquinas redondeadas para que queden full cuadrados? Y si todo bien, seguimos con el guión del video.

## 🧑 Adriana · 2026-06-20 03:22
ok si todo lo que hicimos lo convertimos en un prompt, para darselo a emergent ai junto con este html adjuntado, pero dame todo bien especificado, las formulas, los layouts preguntas todo todo todo

## 🤖 Claude · 2026-06-20 03:23
Buenísima movida. Para que Emergent no improvise nada, el prompt tiene que clavar los mismos números que ya están en el HTML. Déjame leer el archivo completo para transcribir las fórmulas, opciones e industrias exactas y que todo cuadre.

## 🧑 Adriana · 2026-06-20 03:29
ok si todo lo que hicimos lo convertimos en un prompt, para darselo a emergent ai junto con este html adjuntado, pero dame todo bien especificado, las formulas, los layouts preguntas todo todo todo

## 🧑 Adriana · 2026-07-04 20:59
ok si todo lo que hicimos lo convertimos en un prompt, para darselo a emergent ai junto con este html adjuntado, pero dame todo bien especificado, las formulas, los layouts preguntas todo todo todo para solo hacer copy and paste

## 🤖 Claude · 2026-07-04 21:00
Antes de tirarte el prompt, una cosa que te va a ahorrar un dolor de cabeza con Emergent: el prompt no puede depender de que Emergent "adivine" la lógica del HTML. Tiene que ser la fuente de verdad por sí solo, con el HTML como referencia visual. Si Emergent lee el HTML y reconstruye la fórmula por su cuenta, te va a cambiar un multiplicador sin avisarte y ni cuenta te das hasta que un número salga raro. Así que el prompt lleva TODA la lógica escrita, y el HTML va solo como "así se ve, respétalo".

Ya extraje los valores exactos del archivo. Aquí va todo, listo para copy paste. Adjunta `calculadora_tarifas_app.html` en el mismo mensaje.

---

```
Estoy construyendo una calculadora web interactiva de "¿cuánto cobrar?" para creadores de contenido. Te adjunto un archivo HTML (calculadora_tarifas_app.html) que ya tiene el diseño, el flujo y toda la lógica funcionando. Tu trabajo es reconstruir esta herramienta como app web real en Emergent, conectada a captura de email, RESPETANDO EXACTAMENTE la lógica, las fórmulas, los textos y el diseño que te especifico abajo. El HTML adjunto es la referencia visual y de comportamiento: cópialo, no lo reinterpretes. Si algo del HTML contradice lo que escribo abajo, gana lo que escribo abajo.

═══════════════════════════════════════
1. QUÉ ES Y CÓMO FUNCIONA
═══════════════════════════════════════

Es un wizard (asistente paso a paso) que hace 6 preguntas, una a la vez, y al final revela un número: la tarifa mínima ("piso") que el creador debe cobrar por crear y postear UN video para una marca.

Flujo de pantallas en orden:
- Pantalla de inicio (portada) con botón "Empezar"
- Pregunta 1 de 6: seguidores
- Pregunta 2 de 6: interacciones promedio por post (de aquí se calcula el engagement automáticamente)
- Pregunta 3 de 6: nivel de autoridad
- Pregunta 4 de 6: nivel de producción
- Pregunta 5 de 6: relevancia (nicho del creador vs nicho de la marca)
- Pregunta 6 de 6: industria de la marca
- Pantalla de resultados (revela el piso + un dato de leverage + captura de email)

Reglas de navegación (obligatorias):
- Solo se muestra UNA pregunta a la vez.
- En CADA paso hay dos botones: "Atrás" y "Siguiente" (excepto inicio, que solo tiene "Empezar", y resultados, que tiene "Atrás" y "Calcular otra").
- NO auto-avanzar al seleccionar una opción. El usuario elige y luego pulsa "Siguiente".
- Cada pregunta de opciones ya tiene una opción preseleccionada por defecto (te la marco abajo).
- Barra de progreso fija abajo: muestra "Pregunta X de 6", se va llenando, y al final dice "Ya casi ves tu número".

═══════════════════════════════════════
2. LAS 6 PREGUNTAS (textos y opciones exactos)
═══════════════════════════════════════

PREGUNTA 1 — Seguidores
Título: "¿Cuántos seguidores tienes?"
Input numérico. Valor por defecto: 60000. Mínimo 0.

PREGUNTA 2 — Interacciones promedio
Título: "Interacciones promedio por post"
Subtítulo: "Likes + comentarios + saves + shares. Con esto calculo tu engagement, sin que te autopuntúes."
Input numérico. Valor por defecto: 3000. Mínimo 0. Paso de 50.
Debajo del input muestra en vivo: "Engagement: X.X%"
El engagement se calcula solo así: (interacciones ÷ seguidores) × 100. Si seguidores es 0, engagement es 0.

PREGUNTA 3 — Autoridad
Título: "¿Cómo es tu autoridad?"
3 opciones (botones seleccionables, la del medio viene preseleccionada):
- "Emergente" / subtexto "nuevo, construyendo" / valor 0.9
- "Establecido" / subtexto "reconocido, portafolio sólido" / valor 1.0  ← PRESELECCIONADA
- "Autoridad" / subtexto "referente, con marcas que te respaldan" / valor 1.2

PREGUNTA 4 — Producción
Título: "Nivel de producción"
3 opciones (la tercera "Alto" viene preseleccionada):
- "Básico" / subtexto "talking head, una toma" / valor 1.0
- "Intermedio" / subtexto "varias tomas, edición" / valor 1.15
- "Alto" / subtexto "producido, b-roll, gear, música" / valor 1.35  ← PRESELECCIONADA

PREGUNTA 5 — Relevancia
Título: "Relevancia: tu nicho vs el de la marca"
3 opciones (la primera "Perfecto" viene preseleccionada). Cada una tiene DOS valores asociados, un multiplicador de relevancia y una tasa de leads:
- "Perfecto" / subtexto "mismo nicho" / multiplicador 1.4 / tasa de leads 0.05  ← PRESELECCIONADA
- "Adyacente" / subtexto "relacionado" / multiplicador 1.0 / tasa de leads 0.025
- "Off-niche" / subtexto "fuera de lo tuyo" / multiplicador 0.85 / tasa de leads 0.01

PREGUNTA 6 — Industria
Título: "Industria de la marca"
Subtítulo: "Define el CPL para tu número de leverage."
Opciones en grid (la primera "Travel" viene preseleccionada). Cada una tiene un CPL (costo por lead) en dólares:
- "Travel" / "~$4" / CPL 4  ← PRESELECCIONADA
- "Food" / "~$5" / CPL 5
- "Beauty" / "~$6" / CPL 6
- "Fashion" / "~$8" / CPL 8
- "Fitness" / "~$8" / CPL 8
- "Tech / SaaS" / "~$20" / CPL 20
- "Salud" / "~$22" / CPL 22
- "Seguros" / "~$25" / CPL 25
- "Finanzas" / "~$30" / CPL 30
- "CPL manual" / al seleccionarla aparece un input numérico (valor por defecto 15) donde el usuario escribe su propio CPL.

═══════════════════════════════════════
3. LA FÓRMULA DEL PISO (esto es lo más importante, no lo cambies)
═══════════════════════════════════════

El precio final ("piso") se calcula así:

PISO = máximo entre ($150, Base × Autoridad × Producción × Relevancia)

O sea: nunca cobra menos de $150, sin importar qué salga la fórmula.

Donde:

BASE = dólares_por_seguidores × multiplicador_engagement

3.1 — dólares_por_seguidores es POR TRAMOS (escalonado, la tarifa por cada mil seguidores baja mientras más grande eres):
- Los primeros 10,000 seguidores valen $18 por cada mil.
- De 10,001 a 50,000 valen $12 por cada mil.
- De 50,001 a 150,000 valen $8 por cada mil.
- De 150,001 en adelante valen $5 por cada mil.

Se suman los tramos. Ejemplo con 60,000 seguidores:
  primeros 10,000 → 10 × $18 = $180
  siguientes 40,000 (del 10k al 50k) → 40 × $12 = $480
  siguientes 10,000 (del 50k al 60k) → 10 × $8 = $80
  total dólares_por_seguidores = $740

Lógica exacta (en pseudocódigo, respétala):
  tramo1 = min(seguidores, 10000) / 1000 × 18
  tramo2 = max(0, min(seguidores, 50000) − 10000) / 1000 × 12
  tramo3 = max(0, min(seguidores, 150000) − 50000) / 1000 × 8
  tramo4 = max(0, seguidores − 150000) / 1000 × 5
  dólares_por_seguidores = tramo1 + tramo2 + tramo3 + tramo4

3.2 — multiplicador_engagement:
  multiplicador_engagement = 0.5 + (engagement% ÷ 8)
  (el engagement% es el que ya calculaste en la pregunta 2)
  Ejemplo: engagement 5% → 0.5 + (5 ÷ 8) = 0.5 + 0.625 = 1.125

3.3 — Los otros tres multiplicadores salen directo de las preguntas 3, 4 y 5:
  Autoridad = valor de la opción elegida en P3 (0.9, 1.0 o 1.2)
  Producción = valor de la opción elegida en P4 (1.0, 1.15 o 1.35)
  Relevancia = multiplicador de la opción elegida en P5 (1.4, 1.0 o 0.85)

Ejemplo completo (60k seguidores, 3000 interacciones = 5% eng, Establecido, Alto, Perfecto):
  Base = 740 × 1.125 = $832.5
  Piso = 832.5 × 1.0 × 1.35 × 1.4 = $1,573 (redondeado)

IMPORTANTE: el piso es SOLO por crear y postear el video. NO incluye Usage Rights, Whitelisting, Spark Ads ni Perpetuity Usage. Eso se cotiza aparte y así debe decirlo la pantalla de resultados.

═══════════════════════════════════════
4. EL NÚMERO DE LEVERAGE (dato secundario, NO cambia el precio)
═══════════════════════════════════════

En resultados también se muestra un dato de "lo que vales para ellos" vía CPL. Este número NO toca el piso, es solo para negociar. Se calcula así:

leads = (seguidores × engagement%) × tasa_de_leads
  (la tasa_de_leads viene de la opción elegida en P5: Perfecto 0.05, Adyacente 0.025, Off-niche 0.01)

leverage = leads × CPL
  (el CPL viene de la industria elegida en P6)

Se muestra como texto: "Basado en el CPL, tu audiencia vale $[leverage] para esta marca (≈ [leads] leads × CPL $[cpl])."

═══════════════════════════════════════
5. PANTALLA DE RESULTADOS (orden de elementos)
═══════════════════════════════════════

De arriba a abajo:
1. Etiqueta "Tu piso · lo mínimo que cobras"
2. El número grande del piso (ej. $1,573)
3. Si aplicó el mínimo de $150, muestra "Aplicado el mínimo de $150"
4. Nota: "Por crear y postear el video. Si te ofrecen menos, te están robando."
5. Un desplegable colapsable "Ver desglose" que muestra: Base (followers + engagement), × Autoridad, × Producción, × Relevancia.
6. Tarjeta de leverage (el texto del punto 4 de arriba).
7. Disclaimer en caja: "Esto NO incluye Usage Rights, Whitelisting, Spark Ads ni Perpetuity Usage. Todo eso se cotiza aparte."
8. TARJETA DE CAPTURA DE EMAIL (ver sección 6).
9. Botones "Atrás" y "Calcular otra".

═══════════════════════════════════════
6. CAPTURA DE EMAIL (esto sí necesito que lo conectes de verdad)
═══════════════════════════════════════

La tarjeta de captura va al final de resultados, DESPUÉS de mostrar el número (nunca antes, no quiero gatear el resultado, mata la viralidad de la herramienta).

Textos:
- Título: "¿Te gustó la herramienta?"
- Subtítulo: "Déjame tu correo y te sigo mandando herramientas y cosas cool para creadores, entrepreneurs y marcas."
- Input de email con placeholder "tu@correo.com"
- Botón "Quiero"
- Al enviar (con email válido), la tarjeta se reemplaza por: "¡Listo! Te escribo pronto."

Conexión real (esto es lo que el HTML no hace y tú sí debes hacer):
- Valida que el email tenga formato correcto antes de aceptarlo.
- Guarda el email en una base de datos o lista. Si Emergent tiene integración nativa de captura de leads o base de datos, úsala. Si no, prepáralo para conectar a MailerLite vía su API (yo pondré la API key). Como alternativa, deja lista una integración por webhook para poder mandar el email a Manychat o a una automatización de N8n.
- No borres ni cambies el número del piso al capturar el email.

═══════════════════════════════════════
7. DISEÑO (respeta la marca, todo esto ya está en el HTML)
═══════════════════════════════════════

Colores de marca:
- Fondo azul: #3846C4 (fondo principal de la app)
- Rojo: #D72323 (el número del piso, acentos)
- Amarillo: #FFBA35 (acentos, tarjeta de captura de email)
- Negro: #000000
- Blanco: #FFFFFF (tarjetas)
- Lavanda: #F2E9FF

Tipografía: Poppins.
Header arriba: logo a la izquierda, texto "¿Cuánto cobrar?" en amarillo a la derecha, centrado en una columna de máximo 600px.

Dos gifs animados (ya vienen incrustados en el HTML como base64, respétalos tal cual):
- Portada: gif del gato con spinner, va como STICKER en la esquina superior derecha del panel de inicio, ligeramente rotado, sin borde, esquinas redondeadas. El título de la portada tiene padding a la derecha para que el texto no choque con el gif.
- Resultados: gif del corgi, va AL LADO del precio (precio a la izquierda ocupando el espacio flexible, corgi a la derecha, ~140px), sin borde, esquinas redondeadas. En móvil se apila debajo.

Reglas de estilo del texto (importante para el copy dentro de la app): sin em dashes, usa puntos o comas. Tono directo, sin lenguaje corporativo.

═══════════════════════════════════════
8. RESUMEN DE LO QUE QUIERO QUE HAGAS
═══════════════════════════════════════

Recrea esta calculadora exactamente como el HTML adjunto (mismo flujo, mismos textos, misma fórmula, mismo diseño, mismos gifs), pero como app web real en Emergent, con la captura de email funcionando de verdad (base de datos o MailerLite/Manychat, con webhook de respaldo). El piso y el leverage se calculan exactamente con las fórmulas de arriba. No cambies ningún multiplicador, tramo ni texto sin preguntarme.
```

---

Un par de cosas antes de que lo pegues:

El bloque de captura es donde Emergent te va a poder aportar valor real, porque el HTML solo simula el "¡Listo!" sin guardar nada. Le dejé pedidas tres rutas (base de datos nativa, MailerLite por API, webhook para Manychat/N8n) para que Emergent elija la que le quede más fácil y tú no dependas de una sola.

Y ojo con esto: le puse explícito "si el HTML contradice lo que escribo, gana el texto". Eso es tu seguro. Sin esa línea, Emergent a veces lee el base64 de los gifs o algún estilo y empieza a improvisar. Con ella, la fórmula queda blindada.

Si en algún momento decides meterle el freebie a la captura (la plantilla de rate card que te mencioné), solo cambias el subtítulo de la sección 6 y me dices, no hay que tocar nada más del prompt.
