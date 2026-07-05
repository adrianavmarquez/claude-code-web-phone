---
title: "Separar timeline visual y UX del portafolio"
source: claude.ai-chat
created: "2026-04-10 15:16"
summary: "**Conversation Overview**  Adriana V. Márquez, a content creator and creative marketing strategist collaborating with Emergent AI, worked with Claude across multiple sessions to organize and develop the full brief for her UGC creator portfolio website. She shared an initial idea dump covering both a video visual timeline and a portfolio UX concept, and asked Claude to separate these into two distinct documents. Claude produced a video beat-by-beat timeline table and a full UX section-by-section breakdown, pulling structure from both her written description and an uploaded script file for the video.  In a second round, Adriana flagged that several portfolio sections were missing based on industry best practices for creator portfolios that close brand deals. The missing sections included: a value proposition hero (not a bio), video demos separated cleanly by category with brand and format labeled per video, hooks that represent her style, a featured video with process walkthrough, real organic metrics framed as sales proof, a brand moodboard and visual identity section, and rates presented without apology. Claude updated the full UX document to incorporate all of these, marking sections that lacked a visual concept with a clear 'falta diseño' flag so she could return to them later.  After completing a mockup at her live URL, Adriana provided a comprehensive technical brief covering every section of the site with specific interaction details, typography rules (Poppins Bold for titles, Heading Now for body), exact brand hex codes, spacing requirements tied to custom background image exports, editable frontend fields for metrics and pricing, a typewriter-style contact form with predefined budget dropdown options, and a persistent dog-head scroll indicator. She confirmed she does not want Claude to build the HTML, only to produce a structured prompt she can paste directly into Emergent AI. Claude delivered the full brief first in Spanish prose, then Adriana requested it as a JSON file, which Claude generated and delivered as a downloadable artifact covering all 10 sections, global technical requirements, persistent elements, and card-level pricing data with editable field flags.  Her stated working preferences include keeping visual design decisions exportable and pixel-precise for background image alignment, maintaining frontend editability for live data like metrics and rates without code access, and using the exact typographic and color system consistently throughout. She explicitly corrected an early response where Claude skipped key portfolio sections, and she redirected the final deliverable format from prose to JSON for direct use in her build tool."
messages: 10
claude_uuid: "4e098090-7f1c-4e5c-8e03-946e6d87eea7"
tags: [claude, chat, archive]
---
# Separar timeline visual y UX del portafolio

> **Conversation Overview**

Adriana V. Márquez, a content creator and creative marketing strategist collaborating with Emergent AI, worked with Claude across multiple sessions to organize and develop the full brief for her UGC creator portfolio website. She shared an initial idea dump covering both a video visual timeline and a portfolio UX concept, and asked Claude to separate these into two distinct documents. Claude produced a video beat-by-beat timeline table and a full UX section-by-section breakdown, pulling structure from both her written description and an uploaded script file for the video.

In a second round, Adriana flagged that several portfolio sections were missing based on industry best practices for creator portfolios that close brand deals. The missing sections included: a value proposition hero (not a bio), video demos separated cleanly by category with brand and format labeled per video, hooks that represent her style, a featured video with process walkthrough, real organic metrics framed as sales proof, a brand moodboard and visual identity section, and rates presented without apology. Claude updated the full UX document to incorporate all of these, marking sections that lacked a visual concept with a clear "falta diseño" flag so she could return to them later.

After completing a mockup at her live URL, Adriana provided a comprehensive technical brief covering every section of the site with specific interaction details, typography rules (Poppins Bold for titles, Heading Now for body), exact brand hex codes, spacing requirements tied to custom background image exports, editable frontend fields for metrics and pricing, a typewriter-style contact form with predefined budget dropdown options, and a persistent dog-head scroll indicator. She confirmed she does not want Claude to build the HTML, only to produce a structured prompt she can paste directly into Emergent AI. Claude delivered the full brief first in Spanish prose, then Adriana requested it as a JSON file, which Claude generated and delivered as a downloadable artifact covering all 10 sections, global technical requirements, persistent elements, and card-level pricing data with editable field flags.

Her stated working preferences include keeping visual design decisions exportable and pixel-precise for background image alignment, maintaining frontend editability for live data like metrics and rates without code access, and using the exact typographic and color system consistently throughout. She explicitly corrected an early response where Claude skipped key portfolio sections, and she redirected the final deliverable format from prose to JSON for direct use in her build tool.

## 🧑 Adriana · 2026-04-10 15:16
ok, tengo una collaboracion con emergent ai, esta es mi idea para los visuales del video y la ux de la pagina que voy a crear con ellos. quiero que me separes el visual timeline del video, toda la descripcion del UX del portafolio y te adjunte el script que usare como outline para el video. 

"I bring my phone to the screen showing the animation on my phone of my head being cracked opened and my projects come out. Like an animation of ideas that generated my videos.
You scroll up and you see my intro:
I do a creative bio and description of myself ( i want the image to change somewhat similar to what I’m stating about myself so it looks like it goes with the narrative, “hi I’m Adri I’m a Venezuelan creator very goofy creative but a very big thinker. And I love goofy things i can create. This is my portfolio. (and next to it is a gif image of a lot of things that make me me. Selfie, Venezuela Picture, Personality Pic, Me working/thinking, Using a Camera, making rings, drawing, my top 3 fav photos, photo of me and Kronus, photo with pluchi, smile thumb up picture. Or meme)
I have multiple passions:
A book(education), a camera(technology), a bronzer(travel), an egg(LUV eggs but food in general), la laptop (content creation), lipgloss(makeup), sunscreen (skincare), hair clip (hair care) electrolytes (wellness), and sunglasses. (Fashion)
When you click on each it takes you to the section of my portfolio where I show my videos for this niche.
(Section for brand logos I worked with)
A wallet open in the hair that says: “my rates”
Or a very wide picture taken from the bottom of me with glasses and counting money
And whatever I add my rates.
Picture of me reaching for something or a gif of my fit getting on tippy toes like “reaching”
and I show my metrics. My reach screenshots.
(Not sure how y will show them (thinking of a picture film lab and have like the screenshots hanging from there)
Old school kind of my 90 baby video game that has a visual movement or traveling thinking of:
Dora the explorer showing the map and where she is at and where she wanted to go or Mario party seat/ spots moving.
My timeline:
Email/meeting/discussion/ scripting etc etc
Let’s talk, a gif Me as a baby doing a “call me sign”
Let’s talk CTA button
the scroll is a png image of my dogs head."

## 🤖 Claude · 2026-04-10 15:17
Perfecto, ya tengo todo. Aquí tienes los dos documentos separados:

---

## 🎬 VISUAL TIMELINE DEL VIDEO

*(basado en tu idea + el script del .docx)*

| # | BEAT | VISUAL | NOTAS DE DIRECCIÓN |
|---|------|--------|-------------------|
| 1 | **HOOK** | On-cam, talking head. Tono de confesión, casi riéndote de ti misma. | 3 segundos. Corte limpio. Sin texto encima, tu cara es el gancho. |
| 2 | **SETUP DEL PROBLEMA** | On-cam, continuación. Cambias de energía a "pero espera." | 5 seg. Tono honesto, no dramático. |
| 3 | **TRANSICIÓN VISUAL** | Corte a la laptop mostrando la animación: tu cabeza abriéndose y los proyectos saliendo. | Sin VO encima. Solo música + animación. Respirar 2-3 segundos. |
| 4 | **BEAT DE PRODUCTO** | Screen recording de Emergent, se ve el prompt que escribiste generando el portfolio en tiempo real. | VO encima del screen recording. El más corto del reel, dato de paso, no pausa de comercial. |
| 5 | **DEMO PRINCIPAL** | Scroll lento e intencional por el portfolio completo, de arriba hacia abajo. Cada sección aparece en pantalla justo cuando se nombra en VO. | ~20-25 seg. Scroll lento, que se note que hay sustancia. No tutorial, tour cinematográfico. |
| 6 | **PAUSA EMOCIONAL** | Scroll se detiene. Pausa en una sección del portfolio. Sonríes a cámara. | 1-2 segundos sin texto. Dejar respirar. |
| 7 | **CIERRE + CTA** | On-cam, directo a cámara. Misma energía del hook, como cerrando el chisme. Texto del link aparece en pantalla simultáneamente. | Tono cómplice. "emergent.sh" visible en pantalla. |

**Notas de producción generales:**
subtítulos en todo momento (audiencia scrollea en mute), tu cara en cuadro desde el hook, acento de color único por toma, cortes con intención.

---

## 🖥️ UX DEL PORTFOLIO: DESCRIPCIÓN COMPLETA

*(tu idea original, organizada sección por sección)*

---

### SECCIÓN 1 — HERO / ENTRADA
La pantalla abre con la **animación del teléfono**: tu cabeza abriéndose y tus proyectos saliendo. Este es el primer elemento visual que el usuario ve. Sin texto, sin nav. Solo el momento de impacto.

---

### SECCIÓN 2 — BIO INTERACTIVA
Scroll up revela tu **intro creativa**. El copy va cambiando en sync con la imagen que aparece al lado, narrativa visual que acompaña lo que estás diciendo de ti misma:

> "Hi, I'm Adri. Venezuelan creator. Very goofy, very creative, but a very big thinker."

El lado derecho es un **gif collage** que rota entre: selfie, foto de Venezuela, foto de personalidad, tú trabajando/pensando, usando cámara, haciendo argollas, dibujando, tus 3 fotos favoritas, foto con Kronus, foto con Pluchi, foto sonriendo con pulgar arriba (o meme).

La imagen cambia en tiempo real mientras se lee el texto, como si el copy y el visual fueran un solo elemento.

---

### SECCIÓN 3 — MIS PASIONES (Navegación por íconos)
Una fila de objetos físicos como íconos clickeables:

| Ícono | Objeto | Categoría |
|---|---|---|
| 📚 | Libro | Education |
| 📷 | Cámara | Technology |
| 🟫 | Bronzer | Travel |
| 🥚 | Huevo | Food |
| 💻 | Laptop | Content Creation |
| 💄 | Lipgloss | Makeup |
| 🧴 | Sunscreen | Skincare |
| 🪮 | Hair clip | Hair Care |
| ⚡ | Electrolytes | Wellness |
| 🕶️ | Sunglasses | Fashion |

Al hacer click en cada ícono, baja a la **sección de videos correspondiente** de ese nicho.

---

### SECCIÓN 4 — BRAND LOGOS
Franja horizontal con los logos de las marcas con las que has trabajado. Limpio, sin copy extra.

---

### SECCIÓN 5 — RATES
Dos opciones de tratamiento visual (tú eliges):

**Opción A.** Billetera abierta en el aire con la frase "my rates" visible.

**Opción B.** Foto wide shot desde el piso hacia arriba, tú con gafas contando billetes.

Debajo o al lado: tabla de rates y paquetes.

---

### SECCIÓN 6 — MÉTRICAS
Una foto o gif tuyo estirándote/alcanzando algo (o gif de tu fit de puntillas como "reaching") seguida de tus screenshots de reach y métricas reales.

**Propuesta de tratamiento visual:** estilo film lab/cuarto oscuro con los screenshots colgando como fotos en proceso de revelado. Hilo negro, pinzas de madera, luz roja de cuarto oscuro. Old school pero editorial.

---

### SECCIÓN 7 — TIMELINE DEL PROCESO
Animación o elemento interactivo estilo **retro/videojuego** mostrando el camino de colaboración. Dos referencias visuales propuestas:

**Referencia A.** Mapa de Dora la Exploradora mostrando "donde estamos" y "a dónde vamos."

**Referencia B.** Mario Party: spots moviéndose en el tablero, cada casilla = una etapa del proceso.

Las etapas del proceso: Email → Meeting → Discussion → Scripting → Filming → Editing → Delivery.

---

### SECCIÓN 8 — CTA / LET'S TALK
Gif de ti de bebé haciendo el gesto de "llámame" (🤙).

Botón grande: **"Let's talk"** con link a tu contacto.

---

### ELEMENTO PERSISTENTE — SCROLL INDICATOR
El scroll de la página es un **PNG de la cabeza de tus perros**. Aparece a lo largo de toda la página como el indicador de posición/scroll.

---

Eso es todo lo que tenías en la cabeza, separado y limpio. ¿Arrancamos a desarrollar alguna de las dos partes, o esto va directo a Emergent para la build?

## 🧑 Adriana · 2026-04-10 20:36
faltan secciones:
"Estas son las secciones que necesita
cualquier portfolio para poder
conseguir cerrar ese cliente. Un Hero,
no una bio. Una propuesta de valor.
Videos de muestra por categoria. NO
lo mezcles. Tambien nombra la marca
con la que trabajaste para cada
collab y el formato que elegiste.
Que la portada de cada video deje
claro de que se trato cada video&quot;
En la industria ellos buscan tu
contenido para generar VENTAS asi
que necesitan variacion y efectividad.
Menciona los hooks que mas te
representan.
MEtricas reales. No necesitas tener
campanas pagas para mostrar tus
numeros. Un video tuyo con 200k
views+8% de engagement+Alto save
rate. ERES lo que estan buscando. No
solo un unboxing aesthetic.
resalta un video que te represente
BIEN como creador. y nombre el paso
a paso de proceso esto hara que te
perciban como una persona que
ENTIENDE lo que ellos buscan.
moodboard/estetica de tu marca. si
tienes una identidad visual definida,
ensena tus paletas, tu set, tu
iluminacion.
rates y paquetes.
no lo escondas, que no te de miedo.
ya explicaste por que cobras lo que
cobras, tu no solo vendes un video y
ya, vendes UN SERVICIO.
No quiero que me digas lo que haces,
quiero que me dejes claro como
piensas!! Ya saben que entiendes lo
que buscan, pero cual es TU angulo."


Si alguna no tiene visual pensando en el idea dump que te pase, agregala y escribe falta disneo

## 🤖 Claude · 2026-04-10 20:37
Aquí va el UX completo actualizado con todas las secciones, incluyendo las que faltaban:

---

## 🖥️ UX DEL PORTFOLIO: DESCRIPCIÓN COMPLETA

---

### SECCIÓN 1 — HERO / ENTRADA
La pantalla abre con la **animación del teléfono**: tu cabeza abriéndose y tus proyectos saliendo. Primer elemento visual, sin texto, sin nav. Solo el impacto.

---

### SECCIÓN 2 — PROPUESTA DE VALOR
*(no una bio, un hero)*

Copy de una sola línea que deja claro quién eres y qué haces. No descripción personal, declaración de valor. Ejemplo de estructura: **[quién eres] + [qué produces] + [para qué sirve].**

Al lado o debajo, el **gif collage** con las fotos que rotan: selfie, Venezuela, personalidad, working/thinking, cámara, argollas, dibujando, top 3 fotos, Kronus, Pluchi, pulgar arriba. La imagen cambia en sync con el copy, como si fueran un solo elemento.

---

### SECCIÓN 3 — MIS PASIONES (Navegación por íconos)
Fila de objetos físicos clickeables. Cada uno baja a la sección de videos de ese nicho.

| Ícono | Objeto | Categoría |
|---|---|---|
| 📚 | Libro | Education |
| 📷 | Cámara | Technology |
| 🟫 | Bronzer | Travel |
| 🥚 | Huevo | Food |
| 💻 | Laptop | Content Creation |
| 💄 | Lipgloss | Makeup |
| 🧴 | Sunscreen | Skincare |
| 🪮 | Hair clip | Hair Care |
| ⚡ | Electrolytes | Wellness |
| 🕶️ | Sunglasses | Fashion |

---

### SECCIÓN 4 — VIDEOS POR CATEGORÍA
*(una sección por cada ícono, NO mezcladas)*

Cada categoría tiene su propio bloque con:
- Nombre de la categoría visible
- Thumbnail de cada video que deja claro de qué trató (no aesthetic genérico, contexto inmediato)
- Nombre de la marca con la que fue la collab
- Formato elegido (Reel, TikTok, UGC, etc.)

Las secciones no se mezclan. El talent scout puede navegar directo a lo que busca.

---

### SECCIÓN 5 — HOOKS QUE TE REPRESENTAN
Bloque dedicado a mostrar los hooks de apertura que más te definen como creadora. Texto en pantalla + clip de 3-5 segundos de cada uno, o solo el texto si es estático.

El objetivo: demostrar que entiendes cómo detener el scroll y que tienes variación. No un solo estilo, varios ángulos.

⚠️ *Falta diseño: no hay visual pensado para este bloque todavía.*

---

### SECCIÓN 6 — VIDEO DESTACADO
Un solo video que te representa mejor como creadora. No el más viral, el más completo. El que muestra que entiendes lo que una marca necesita.

Debajo del video: el **paso a paso de tu proceso** de producción (scripting → grabación → edición → entrega). Esto comunica que no vendes un video, vendes un servicio con criterio.

⚠️ *Falta diseño: no hay visual pensado para la presentación del proceso todavía.*

---

### SECCIÓN 7 — MÉTRICAS
Gif o foto tuya estirándote/en puntillas como "reaching," seguida de los screenshots reales de reach y engagement.

**Propuesta de tratamiento visual:** film lab/cuarto oscuro con los screenshots colgando como fotos en revelado. Hilo negro, pinzas de madera, luz roja. Old school pero editorial.

El énfasis va en los números orgánicos: views, engagement rate, save rate. No necesitas pauta para validarte.

---

### SECCIÓN 8 — MOODBOARD / ESTÉTICA DE MARCA
Tu identidad visual definida: paletas de color, set habitual, tipo de iluminación, estilo de encuadre.

Esto no es decoración, es prueba de que tienes un punto de vista visual consistente. Las marcas necesitan saber cómo se va a ver su producto en tu feed.

⚠️ *Falta diseño: no hay visual pensado para este bloque todavía.*

---

### SECCIÓN 9 — BRAND LOGOS
Franja horizontal con logos de marcas con las que has trabajado. Limpio, sin copy extra.

---

### SECCIÓN 10 — RATES Y PAQUETES
No escondidos, no al final como afterthought. Presentados con contexto: ya explicaste quién eres, lo que produces y cómo piensas. Los rates son la consecuencia lógica.

**Opción A de visual.** Billetera abierta en el aire con "my rates."

**Opción B de visual.** Foto wide desde el piso, tú con gafas contando billetes.

Tabla de paquetes debajo.

---

### SECCIÓN 11 — TU ÁNGULO
*(el cierre más importante)*

No lo que haces. Cómo piensas.

Un párrafo corto u oración que deja claro tu perspectiva única como creadora. Las marcas ya saben que entiendes lo que buscan. Esta sección responde: **¿cuál es tu ángulo?**

⚠️ *Falta diseño: no hay visual pensado para este bloque todavía.*

---

### SECCIÓN 12 — TIMELINE DEL PROCESO DE COLABORACIÓN
Animación retro/videojuego mostrando el camino de trabajo juntos.

**Referencia A.** Mapa de Dora mostrando dónde estamos y a dónde vamos.
**Referencia B.** Mario Party: casillas moviéndose en el tablero, cada una = una etapa.

Etapas: Email → Meeting → Discussion → Scripting → Filming → Editing → Delivery.

---

### SECCIÓN 13 — CTA / LET'S TALK
Gif tuyo de bebé haciendo el gesto 🤙. Botón grande: **"Let's talk."**

---

### ELEMENTO PERSISTENTE — SCROLL INDICATOR
PNG de la cabeza de tus perros a lo largo de toda la página como indicador de posición.

---

Las secciones marcadas con ⚠️ son las que necesitan que pienses el visual antes de pasarle el brief a Emergent. ¿Arrancamos con esas o revisamos el orden primero?

## 🧑 Adriana · 2026-04-11 20:04
Ok, ya termien el mockup que hice para el portfolio, elimine algunas secciones porque no tengo informcion suficiente aun para agregar, pero desarollo esas secciones despues (hooks y angulos obviados) https://adrianavmarquez.com/mockup Es importante que tomes en cuenta que: Mi fuente de titulo es Poppins, de Subitulos es Poppins, y de Body es Heading Now. Mis colores de Marca son #000000 #FIFFFFF #D72323 #F2E9FF #FFBA35 #3846C4, los espaciados, margenes, placeholding de imagenes, empieza con un menu isla que tiene "hey, work, rates, contact me" seguido de un ribbon bar con los logos de marcas con las que he trabajado, en la seccion de "hi, im adri" quiero que el texto se anime tipotypewritter, las imagenes y gif se mantienen en su sitio, toma en cuenta la distribucion espaciados y margenes aca, luego viene un slider con imagenes horizontales, que he hecho para campanas y colaboraciones, luego la seccion my work, cada objeto es clickeable y te lleva a la seccion de mi portfolio que le corresponde a esa industria, los iconos tienen efecto hover cuando le pasas por encima se mueve un poquito, en la seccion de demo de mis videos son unos sliders y cada placeholder del video tiene un texto que se mueve con ellos indicando que formato de video es "try-on","unboxing" o lo que corrresponda. en los titulos de cada industria debes tener los espacios bien calculados porque debo exportar la foto de fondo y que los emojis coincidan justo en donde estan los titulos, es uno derecha, otro izqueirda y asi sucesivamente. en my wokrflow solo habra un video gif centrado y el timeline esta sin animar, con una linea de tiempo asi tal cual como esta, en mis metricas, esta area debe ser ajustable, debo poder poner el numero correspondiente a cada grafico y que se ajuste, ya que mis metricas cambian de mes a mes, aca el tema de los espacios tambien es importante porque debo hacer la imagen de fondo como un hilo rojo que conecta el titulo de "my metrics" con "my rates" y el rollo de film con el billete de 100. en la seccion de my rates, es importante que sean dos filas de maximo 3 columans cada una, pero yo usare 3 arriba y 1 abajo, el titulo de cada tarjeta es poppins en negrita pero a escala y el texto del body es heading now, dentro de cada tarjeta debajo del titulo esta dividido en una tabla de dos columnas de una lado escribire el servicio y del lado derecho cuanto cuesta, de nuevo debe poder ser ajustable por si mis tarifas cambian, luego esta una frase centrada debajo de la tarjeta de la segunda fila. y a su lado derecho un callout phrase CTA mas grande en otro color y a su derecha un azucar y unos cubos de azucar que estan bottom alignes con la phrase de la izquierda, Y por ultimo la seccion de lets talk, este texto que vez ahi es un form submission que parece formato typewritter, conectandolo con la misma estetica con la que empezo el portfolio, las secciones en amarillo deben ser llenadas por la marca/persona interesada en mis servicios, asi que debe haber un cursor titilando que indique que hay que llenarlo, en donde dice drop down cuando le den click deben poder elegir entre las pciones de presupuesto que yo predetermine [$350 - $700, $700 - $1,200, $1,200 - $2,500, $2,500 - $5,000 $5,000+]. Considera que debo poder tene run espacio para hacer un placeholder de imagen del lado derecho, que debe quedar en el fondo y por encima en la capa superior mi correo para que me contacten y los socialmedia icons hipervinculados.

## 🤖 Claude · 2026-04-11 20:07
Perfecto, ya leí el mockup completo. Tengo todo lo que necesito: la estructura de secciones, los textos exactos, los estilos (Poppins bold para títulos, Heading Now para body), la paleta de colores, y la lógica de cada componente interactivo. Voy a leer el frontend skill primero.

Ahora tengo todo. Voy a construir el portfolio completo como un HTML artifact fiel al mockup, con todos los detalles técnicos que describiste.

## 🧑 Adriana · 2026-04-11 20:08
No quiero que me hagas el html, lo que quiero es que me hagas el prompt explicativo de punta a punta con todo eso a considerar, para yo copiarlo y pegarlo en emergent ai y construirlo con ellos

## 🤖 Claude · 2026-04-11 20:09
Ah, perfecto. Entonces necesito hacer un prompt de briefing completo para que Emergent AI construya el sitio. Aquí va:

---

# PORTFOLIO WEBSITE — FULL BUILD BRIEF
**Para:** Emergent AI
**Proyecto:** Portfolio UGC / Content Creator — @adrianavmarquez

---

## CONTEXTO GENERAL

Quiero construir mi portfolio como creadora de contenido y estratega de marketing. El sitio tiene que funcionar como herramienta de ventas hacia marcas y talent scouts. El tono visual es editorial, cinematográfico, minimalista expresivo, con personalidad latina. No quiero que se vea genérico ni que parezca un template.

---

## TIPOGRAFÍA

- **Títulos de sección:** Poppins Bold
- **Subtítulos:** Poppins
- **Body / descripciones:** Heading Now (Heading Now 61-68)

---

## PALETA DE COLORES

```
Negro:    #000000
Blanco:   #FFFFFF
Rojo:     #D72323
Azul:     #3846C4
Amarillo: #FFBA35
Lavanda:  #F2E9FF
```

---

## ESTRUCTURA COMPLETA DEL SITIO (sección por sección)

---

### 1. NAVEGACIÓN — Island Menu

Menú flotante estilo "pill" o isla, pegado al top center de la pantalla. Fondo negro, esquinas completamente redondeadas. Contiene 4 links:

```
hey   |   work   |   rates   |   contact me
```

Sticky al hacer scroll. No desaparece.

---

### 2. RIBBON BAR — Logos de marcas

Inmediatamente debajo del nav. Una barra horizontal de scroll automático (marquee/ticker) infinito, que se mueve de derecha a izquierda sin pausa. Contiene logos o nombres de marcas con las que he trabajado. Fondo lavanda (#F2E9FF) con borde superior e inferior de 1.5px negro.

Dejar espacio/placeholder para que yo pueda agregar los logos de imagen más adelante.

---

### 3. SECCIÓN "HI, I'M ADRI" — Hero

Layout de dos columnas:

**Columna izquierda (texto):**
- Título grande en Poppins Bold: "Hi, I'm Adri & this is my portfolio."
- El texto debe animarse con efecto **typewriter** (letra por letra), empezando desde "Hi, I'm Adri" y terminando en "portfolio." con cursor parpadeando al final.
- Subtítulo en Heading Now debajo del título: "content creator & creative marketing strategist"

**Columna derecha (imágenes):**
- Grid de 4 placeholders de imagen/gif que mantienen su posición mientras el texto se anima.
- Las imágenes deben poder ser reemplazadas fácilmente.
- Placeholders para: selfie, foto Venezuela, foto de personalidad, foto working/thinking, usando cámara, haciendo argollas, dibujando, top 3 fotos, foto con Kronus, foto con Pluchi, pulgar arriba, o meme.
- Las imágenes **no se mueven** con la animación del texto, están fijas en su posición.

**Espaciado y márgenes:** Respetar márgenes generosos. Alineación izquierda del texto. Las columnas deben estar bien balanceadas.

---

### 4. SLIDER HORIZONTAL — Campañas y Colaboraciones

Slider horizontal de imágenes que se puede deslizar manualmente (scroll horizontal o flechas). Fondo negro. Cada tarjeta/card del slider representa una campaña o collab y contiene:
- Placeholder de imagen grande (landscape o portrait)
- Tag de formato de video que **se mueve junto con el slider**, pegado a cada card: puede decir "try-on", "unboxing", "dupe review", "product usage", "GRWM", "cinematic", "reel", etc.
- Nombre de la marca con la que fue la collab

Los tags de formato van encima o debajo del placeholder de imagen, visibles en todo momento, y se desplazan junto con su card al hacer scroll.

---

### 5. SECCIÓN "MY WORK" — Íconos clickeables por industria

Título de sección: **[my work]** en Poppins Bold grande.

Debajo, una grid de objetos/íconos físicos, uno por industria. Cada ícono es **clickeable** y al hacer click hace scroll a la sección correspondiente de videos de esa industria (anchor link).

**Los íconos tienen efecto hover:** cuando el cursor pasa por encima, el ícono se mueve ligeramente (wiggle o bounce suave).

Lista de íconos e industrias:
```
📚 Libro          → Education
📷 Cámara         → Technology
🟫 Bronzer        → Travel
🥚 Huevo          → Food
💻 Laptop         → Content Creation
💄 Lipgloss       → Beauty/Makeup
🧴 Sunscreen      → Skincare
🪮 Hair clip      → Hair Care
⚡ Electrolytes   → Wellness
🕶️ Sunglasses    → Fashion
```

---

### 6. SECCIONES DE VIDEOS POR INDUSTRIA — Demo de contenido

Una sección por cada industria (10 en total). Cada sección contiene:

**Header de sección:**
- El emoji de la industria y el título (Poppins Bold grande, ej: "Fashion", "Skincare")
- Los títulos alternan alineación: uno a la derecha, el siguiente a la izquierda, y así sucesivamente.

**IMPORTANTE para el fondo de los títulos:** Los títulos de cada industria necesitan tener el espaciado y posición precisos porque voy a exportar la imagen de fondo de cada sección y los emojis tienen que coincidir exactamente donde están los títulos en el diseño. Diseñar con cuidado el layout para que esto sea posible.

**Slider de videos:**
- Cards de video en formato vertical (9:16 ratio), scroll horizontal por sección.
- Cada card muestra: placeholder de video/thumbnail, nombre de la marca de la collab, tag de formato (Try-On / Unboxing / Dupe Review / Product Usage / GRWM / etc.)
- Los tags de formato se mueven junto con sus cards en el slider.
- Las cards NO se mezclan entre industrias. Cada industria tiene su propio slider separado.

---

### 7. SECCIÓN "MY WORKFLOW" — Proceso de trabajo

Título: **[my workflow]** en Poppins Bold.

**Centro de la sección:** Un solo video/gif centrado (placeholder). Este será un gif animado de mi proceso. Solo hay un elemento visual central aquí.

**Timeline debajo del gif:** Una línea de tiempo horizontal estática (sin animación), que muestra las etapas del proceso de colaboración en orden:

```
Strategy → Storyboard → First Draft → Edits → Final Content
```

Descripción debajo de cada etapa (en Heading Now, itálica, pequeño):
- Strategy: *vision setting, ideas and logistics*
- Storyboard: *script and shotlist for brand approval*
- First Draft: *video for review or choose from RAWs*
- Edits: *feedback applied (CTA, text, thumbnail, etc)*
- Final Content: *content delivery and follow-up analytics*

La línea de tiempo es exactamente como está en el mockup: una línea horizontal con puntos o nodos, sin animación, tal cual.

---

### 8. SECCIÓN "MY METRICS" — Métricas ajustables

Título: **[my metrics]** en Poppins Bold.

Esta sección tiene gráficos o cards de métricas. **Cada número debe ser editable directamente en la página** (campo editable o input field visible) porque mis métricas cambian mes a mes y necesito poder actualizar los números sin tocar el código.

Métricas a mostrar (con sus plataformas):
- Followers (Instagram)
- Avg Views/Video (TikTok)
- Engagement Rate
- Monthly Reach

**Diseño de la sección:**
- El área debe tener espaciado preciso porque voy a crear una imagen de fondo que conecte visualmente con un hilo rojo que une:
  - El título "my metrics" en la parte superior
  - Con el título "my rates" en la sección siguiente
  - Y conecta también con un ícono de rollo de film y un billete de $100 en la composición
- Dejar el espacio correcto para que esa imagen de fondo encaje pixel-perfect.

---

### 9. SECCIÓN "MY RATES" — Tarifas

Título: **[my rates]** en Poppins Bold.

**Layout:** Dos filas. Primera fila tiene máximo 3 columnas. Segunda fila tiene 1 columna centrada (o hacia un lado). Yo usaré: **3 cards arriba + 1 card abajo**.

**Estructura de cada card:**
- **Título de la card:** Poppins Bold, a escala (grande). Ej: "organic UGC", "ad campaign videos", "cinematic video", "other services"
- **Debajo del título:** Una tabla de dos columnas dentro de la card:
  - Columna izquierda: nombre del servicio
  - Columna derecha: precio
- **Body text:** Heading Now
- Los precios deben ser **editables directamente en la página** (mismo criterio que las métricas) para poder actualizar tarifas sin tocar código.

Cards y contenido:
```
Card 1 — organic UGC
1 video          $350
3 videos         $976
4 videos         $1,260
5 videos         $1,540

Card 2 — ad campaign videos
tester A: 8 videos (2 set shots, 2 hooks, 2 CTA)    $990
tester B: 16 videos (2 set shots, 4 hooks, 2 CTA)   $1,165

Card 3 — cinematic video
Production Base from
Props & Styling
Model Fee (per day)
Location Fee
[precios a la derecha, editables]
Includes: Creative direction, lighting, professional editing & color grading

Card 4 (abajo) — other services
UGC photography - 5 Pack         $350
Monthly contracts                Custom Quotes
Paid usage (90 days)             30% of total
Spark Ads (30 days)              50% of total
Raw Footage                      50% of total
```

**Debajo de la última card:** Una frase centrada en texto pequeño (Heading Now):

> *error 101: sugar coat not found*

**A la derecha de esa frase:** Un callout/frase más grande en color azul (#3846C4), Poppins Bold:

> "Ready to be the next success story on my metrics bar?"

**A la derecha de ese callout (bottom-aligned):** Ilustración o emoji de un azucarero y cubos de azúcar, alineados al fondo con la frase de la izquierda.

---

### 10. SECCIÓN "LET'S TALK" — Contacto

Fondo azul (#3846C4).

**Layout:** Dos columnas.

**Columna izquierda — Formulario estilo typewriter:**

Un formulario que visualmente parece texto escrito a máquina, en Heading Now, fondo transparente sobre el azul. Las partes que la marca/cliente debe llenar están en **amarillo (#FFBA35)** y tienen un **cursor parpadeante** que indica que son campos interactivos.

El formulario dice exactamente:

```
Hi, I'm [____nombre____] and I'm with [____Brand Name____].

We are looking for: [ ] Organic UGC  [ ] Cinematic Hero  [ ] Monthly Partnership

Our budget is around: [dropdown ▾]

The vibe of the project is: [____Write a few words...____]
```

El campo de presupuesto es un **dropdown** con estas opciones predeterminadas:
```
$350 - $700
$700 - $1,200
$1,200 - $2,500
$2,500 - $5,000
$5,000+
```

Los checkboxes de "looking for" también deben ser seleccionables.

Botón al final: **[submit]**

**Columna derecha — Imagen + información de contacto:**

- Placeholder de imagen (foto mía) que va en el fondo de la columna derecha
- Por encima de la imagen (en capa superior): mi correo electrónico
- También en capa superior: íconos de redes sociales con hipervínculo a mis perfiles (Instagram, TikTok, YouTube)

---

## ELEMENTO PERSISTENTE — Scroll indicator

A lo largo de toda la página, el indicador de posición de scroll es un **PNG de la cabeza de mis perros**. Va en la barra de scroll lateral o como elemento flotante que indica dónde está el usuario en la página.

---

## NOTAS TÉCNICAS FINALES

- **Todos los placeholders de imagen** deben poder reemplazarse fácilmente sin tocar código, idealmente con un botón de "replace image" o estructura clara de imagen referenciada.
- **Métricas y precios** deben ser editables directamente en el frontend sin acceder al código fuente.
- El sitio debe ser **responsive** pero está diseñado primero para desktop.
- No usar fuentes genéricas de fallback para Heading Now — si no carga, usar Poppins como fallback.
- El color #FFFFFF en mi paleta puede aparecer escrito con una "I" mayúscula en algunas notas; el hex correcto es #FFFFFF (blanco puro).

---

Ese es el brief completo. ¿Lo quieres en inglés también para pasárselo directamente a Emergent, o con este en español está bien?

## 🧑 Adriana · 2026-04-11 20:13
damelo en json file

## 🤖 Claude · 2026-04-11 20:14
Ahí está. El JSON tiene las 10 secciones completas, todos los detalles técnicos, la paleta exacta, las notas de espaciado crítico para las imágenes de fondo, los campos editables, y la estructura de cada card de rates con los precios reales del mockup. Está listo para pegar directo en Emergent.
