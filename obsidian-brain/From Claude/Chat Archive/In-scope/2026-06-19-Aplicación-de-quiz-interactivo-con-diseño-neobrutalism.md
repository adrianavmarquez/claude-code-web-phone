---
title: "Aplicación de quiz interactivo con diseño neobrutalism"
source: claude.ai-chat
created: "2026-06-19 02:33"
summary: "**Conversation Overview**  Adriana V. Márquez is a creative marketing strategist building an interactive quiz diagnostic tool for her educational ecosystem, Creatividad². The quiz functions as a segmentation engine disguised as a game: it identifies which stage of a creator's content process is weakest, then routes that person toward a specific Creatividad² offer for retargeting. The core strategic logic established was diagnosis free, prescription gated—users see their weakness bucket and social proof percentage without giving anything, and unlock personalized recommendations by submitting name and email only (no last name, to reduce friction).  The conversation moved through several layers: design direction debates, funnel architecture decisions, backend logic, and iterative builds. Adriana shared reference images spanning multiple aesthetic families. Claude initially pushed neobrutalism but Adriana clarified her actual preference was flat illustrative and friendly, citing one reference for its character illustrations and clear branding, another for its question/answer layout structure, and a third for its result screen showing weakness scores broken into buckets with percentage comparisons. A key social proof mechanic was established: show what percentage of quiz takers share the same weakness bucket, but gate this display until 50 real submissions are collected to avoid fake data at launch. The referral mechanic on the thank you page was reframed from a discount offer to founder access positioning, with a placeholder gift product to be defined later. Claude built two full HTML versions of the quiz with working JavaScript state machines, shared aggregate storage for bucket counts, webhook integration point for n8n/Mailerlite, and a discrete admin counter tracking progress toward the 50-submission threshold.  After the second build, Adriana pushed back on the design being too basic, referencing a maximalist editorial collage aesthetic with dramatic font size contrast, font stretch, overlapping type, ghost words behind content, and italic serif clashing with heavy bold sans-serif. The third build incorporated these typographic moves: vertical scaleY stretch on hero words, large ghost words layered behind each screen, rotated tape-strip eyebrows, SVG scribble accents, and italic DM Serif Display (as a stand-in for her brand font Scholar) colliding with Poppins 900. The quiz content is structured around six content process stages as weakness buckets: Estrategia, Pre-producción, Producción, Edición, Distribución, and Análisis, scored across seven questions where the final anchor question carries double weight and breaks ties. Adriana requested a comprehensive build prompt consolidating all context, which Claude delivered as a prose brief covering strategic logic, screen flow, design direction with explicit exclusions, brand system, content structure, scoring logic, backend architecture, and pending items including the bucket-to-offer mapping and webhook URL. The session ended with Adriana requesting stronger typographic energy in the design, which was delivered in the third iteration."
messages: 12
claude_uuid: "1b1a3ba5-7bd2-42de-90e3-5ebf508812d2"
tags: [claude, chat, archive]
---
# Aplicación de quiz interactivo con diseño neobrutalism

> **Conversation Overview**

Adriana V. Márquez is a creative marketing strategist building an interactive quiz diagnostic tool for her educational ecosystem, Creatividad². The quiz functions as a segmentation engine disguised as a game: it identifies which stage of a creator's content process is weakest, then routes that person toward a specific Creatividad² offer for retargeting. The core strategic logic established was diagnosis free, prescription gated—users see their weakness bucket and social proof percentage without giving anything, and unlock personalized recommendations by submitting name and email only (no last name, to reduce friction).

The conversation moved through several layers: design direction debates, funnel architecture decisions, backend logic, and iterative builds. Adriana shared reference images spanning multiple aesthetic families. Claude initially pushed neobrutalism but Adriana clarified her actual preference was flat illustrative and friendly, citing one reference for its character illustrations and clear branding, another for its question/answer layout structure, and a third for its result screen showing weakness scores broken into buckets with percentage comparisons. A key social proof mechanic was established: show what percentage of quiz takers share the same weakness bucket, but gate this display until 50 real submissions are collected to avoid fake data at launch. The referral mechanic on the thank you page was reframed from a discount offer to founder access positioning, with a placeholder gift product to be defined later. Claude built two full HTML versions of the quiz with working JavaScript state machines, shared aggregate storage for bucket counts, webhook integration point for n8n/Mailerlite, and a discrete admin counter tracking progress toward the 50-submission threshold.

After the second build, Adriana pushed back on the design being too basic, referencing a maximalist editorial collage aesthetic with dramatic font size contrast, font stretch, overlapping type, ghost words behind content, and italic serif clashing with heavy bold sans-serif. The third build incorporated these typographic moves: vertical scaleY stretch on hero words, large ghost words layered behind each screen, rotated tape-strip eyebrows, SVG scribble accents, and italic DM Serif Display (as a stand-in for her brand font Scholar) colliding with Poppins 900. The quiz content is structured around six content process stages as weakness buckets: Estrategia, Pre-producción, Producción, Edición, Distribución, and Análisis, scored across seven questions where the final anchor question carries double weight and breaks ties. Adriana requested a comprehensive build prompt consolidating all context, which Claude delivered as a prose brief covering strategic logic, screen flow, design direction with explicit exclusions, brand system, content structure, scoring logic, backend architecture, and pending items including the bucket-to-offer mapping and webhook URL. The session ended with Adriana requesting stronger typographic energy in the design, which was delivered in the third iteration.

## 🧑 Adriana · 2026-06-19 02:33
quiero desarollar una app de quiz interactivo, tengo unos templates de referencias de disenos como guia que opinas? esto es neobrutalism design?

## 🤖 Claude · 2026-06-19 02:34
Lo primero, separemos el término del montón, porque ahí está el problema real. De las seis referencias que subiste, solo una es neobrutalism en sentido estricto, y es justo la que viene literalmente rotulada "NEOBRUTALISM DESIGN" (imagen 4). Las otras cinco las agrupaste bajo una etiqueta que en realidad cubre tres o cuatro familias estéticas distintas. Eso no es un detalle de nerd tipográfico. Si le pasas las seis juntas a un builder, a un diseñador o a una IA como "mi referencia", vas a recibir incoherencia, porque cada imagen jala hacia un lado opuesto en bordes, sombras, ilustración y densidad.

## Qué es neobrutalism (para que deje de ser un cajón de todo)

Los marcadores duros, los que tienen que estar sí o sí:

- Sombra sólida y desplazada, sin blur. El bloque se ve "pegado" con offset, no flotando.
- Borde negro grueso rodeando los elementos.
- Rellenos planos y saturados. Cero gradiente, cero glassmorphism, cero sombra suave.
- Componentes expuestos y chunky. La UI no se disimula, se exhibe casi cruda a propósito.
- Tipografía pesada, grotesca, sin delicadeza.

Si una pantalla no tiene borde negro duro ni sombra sin blur, casi seguro no es neobrutalism. Es otra cosa que comparte actitud pero no estructura.

## Tus seis referencias, clasificadas por lo que realmente son

**Imagen 1 (app rosada de learning):** soft gamified. Tarjetas redondeadas, sombras con blur, pastel, hasta gradiente en la gráfica. Es lo contrario de neobrutalism. Es la estética friendly de fintech educativa.

**Imagen 2 (Explicai):** flat editorial ilustrativo. Bloques de color plano, display negro fuerte, blob amarillo. Tiene carácter pero le faltan los bordes y la sombra dura. Borderline, no neobrutal.

**Imagen 3 (ARE YOU READY TO LEARN):** ilustración flat con tipografía grotesca gigante y stickers de estrella. Comparte el instinto de tipo ruidoso, pero las sombras son suaves y la base es ilustrativa. No es brutalist, aunque está cerca de tu marca por las estrellas y el peso del título.

**Imagen 4 (la rotulada):** sí, neobrutalism de manual. Bordes negros, sombra offset, personajes cartoon retro rubber hose, pills chunky. Es el subgénero "mascota cartoon" del estilo.

**Imagen 5 (MyWallet):** neobrutalism ilustrativo. Outlines negros, personaje plano, bordes y botones gruesos. La ilustración es más pulida que el brutalism puro, pero la estructura califica.

**Imagen 6 (app de eventos crema):** anti-design maximalista. Blobs orgánicos, sparkles, stickers regados, italic editorial, fills rayados. Comparte tu energía mixed media, pero es una familia aparte. No es brutalist, es collage Gen-Z.

El patrón: juntaste 1.5 referencias de neobrutalism y 4.5 de otras tres corrientes. Por eso "se sienten parecidas" pero no son lo mismo.

## Lo que esto significa para tu quiz

Acá está lo que importa de verdad, y va conectado a tu marca y a la función del producto.

Tu sistema de marca ya es brutalist-adjacent. La estrella garabateada, el Plunct hand-drawn, el monogram caótico, el pixel art, los stickers meme, el "combina sin miedo". Tú no estás eligiendo neobrutalism desde cero, estás eligiendo la corriente que más se parece a lo que ya construiste. La imagen 1, la soft gamified, es la que choca con tu identidad. Si la sigues, diluyes tu marca para parecerte a cualquier app de cursos.

Y hay un argumento de función, no solo de gusto. Un quiz diagnóstico, sobre todo si es la herramienta de pre-validación de Creatividad², tiene que entregar un veredicto que la persona se tome en serio. El neobrutalism lee como confiado y opinado. El pastel suave lee como amable y dócil. Para algo que te va a decir "estás en esta etapa y te falta esto", la estructura brutalist sostiene la autoridad del resultado. El soft gamified la suaviza hasta volverla irrelevante.

Y a nivel UI puro, el quiz necesita exactamente lo que el neobrutalism hace bien. Bloques de respuesta grandes y tappables, estados claros de seleccionado y no seleccionado, una barra de progreso visible, jerarquía sin ambigüedad. Los componentes chunky con borde duro resuelven eso sin que tengas que inventar nada.

## Mi recomendación, una sola

Compromete una base neobrutalist ilustrativa, el eje de las imágenes 4 y 5, y descarta la imagen 1 como dirección. Sobre esa base, montas tu sistema de acentos propio en vez de copiar el de las referencias. La estrella pintada, el Plunct para los momentos hand-drawn, los stickers pixel, y sobre todo tus personajes de emoción del brandspec, los de la página 7. Esos doce estados emocionales son oro para un quiz, porque cada resultado o cada transición puede tener su cara. Eso es algo que ninguna de las seis referencias tiene y que es 100 por ciento tuyo.

De las imágenes 3 y 6 no copies la estructura, róbate solo dos ideas sueltas. De la 3, la escala bestial del título. De la 6, el uso de stickers y estrellas regados como acento, que ya es lenguaje de tu marca.

Si quieres, el siguiente paso lógico es que te arme la especificación de diseño del quiz con esta dirección. Bordes, sombras, estados de los bloques de respuesta, tipografía por jerarquía usando tus fuentes, y dónde entran los personajes de emoción. Dime si vamos por ahí o si primero quieres definir el contenido del quiz y las preguntas.

## 🧑 Adriana · 2026-06-19 02:42
el que MAS me gusta es el numero 3 por el tema de que incluye ilustraciones s eve divertido, un braidng claro, de la imagen 2 me gusta que en lo slayours hay espacio para preguntas respuestas, ilustraciones, y de la imagen 1 me gusta que el resulado pudiese mostrarlo asi como el score de sus fallas en buckets, y abajo el % puedo ir mostrando el % de los usuarios que han hecho el quiz han tenido el mismo bucket de debilidad que ellos. y la ultima debe ser nombre apellido y correo para enviarle recomendaciones para mejorar y poder hacerle retargeting con creatividad2. y ya en el thank you page podriamos poner que si comparten el quiz con alguien que lo necesite obtienen un % off de una herramienta (misteriosa) que voy a sacar que los puede ayudar con su probelma.

## 🤖 Claude · 2026-06-19 02:44
Lo que estás describiendo no es un quiz, es un motor de segmentación con disfraz de juego. Y eso cambia el orden en que hay que pensarlo. La parte divertida, las ilustraciones, el branding de la imagen 3, todo eso es el envoltorio. El producto real es el bucket de debilidad, porque ese bucket es exactamente lo que determina a qué oferta de Creatividad² mandas a esa persona después. Si el bucket está mal definido, tienes un quiz bonito que no vende nada. Así que antes de diseñar una sola pantalla, lo primero que hay que cerrar es cuántos buckets hay y a qué destino lleva cada uno.

Vamos pieza por pieza, porque cada cosa que elegiste tiene una decisión escondida adentro.

## El mix visual está bien, con un cuidado

Tomar las ilustraciones y el branding de la 3, el layout de preguntas de la 2, y la arquitectura de resultado de la 1 es una combinación sólida. El único cuidado es el que te dije antes. De la imagen 1 róbate la estructura de información, los buckets y el %, no el skin pastel suave. Esa estética blandita choca con tu marca y le quita autoridad al resultado. Renderiza el layout de la 1 con la piel de la 3, 4 y 5. Bordes definidos, ilustración con carácter, nada de sombras con blur. Bonus práctico: el estilo brutalist-ilustrativo es el más fácil de construir fiel en HTML sin diseñador, que es literalmente para lo que existe tu brandspec.

## El orden del funnel y qué hace cada pantalla

1. **Entrada / hook.** Energía imagen 3. Promete un diagnóstico específico y filtra. El hook tiene que hacer sus tres trabajos como siempre.
2. **Primera pregunta fácil.** Baja la energía de activación. Que la Q1 sea de un click, sin pensar, para que entren al flujo.
3. **Flujo de preguntas.** Layout imagen 2. Máximo 6 a 8 preguntas. El largo del quiz es una variable de conversión directa, cada pregunta de más es gente que abandona. Cada pregunta tiene que sentirse sobre ELLOS, no sobre el tema.
4. **Transición de cálculo.** Un beat de anticipación. Aquí entra un personaje o sticker tuyo mientras "calcula".
5. **Diagnóstico.** Bucket + % de comparación. Esta es la dopamina gratis y es lo más compartible de todo. Aquí no pidas nada todavía.
6. **El gate.** Aquí va el correo.
7. **Thank you + referral.**

## La decisión más importante: dónde va el correo

Pusiste la captura de correo después de mostrar el resultado, y tu instinto está casi bien, pero hay que afilarlo. La regla que más convierte es separar diagnóstico de prescripción. El diagnóstico va gratis, el bucket y el %, eso lo ve todo el mundo sin dar nada. La prescripción, el plan personalizado para arreglar esa debilidad, esa es la que desbloquea el correo.

Esto además te resuelve un problema de marca. Tu manifiesto es anti acaparar conocimiento. Si gateas el diagnóstico mismo, te contradices. Pero gatear el plan personalizado es legítimo y generoso al mismo tiempo. Le diste su verdad gratis, el correo le da el siguiente nivel hecho a su medida. Eso sí es consistente contigo.

Un ajuste concreto sobre los campos: pide solo nombre y correo. El apellido agrega fricción y casi nunca lo necesitas para email marketing. Cada campo extra te baja la conversión sin pagártelo. Si en algún momento necesitas el apellido para el CRM, lo pides después, no en el momento de mayor abandono.

## El % de comparación tiene un problema de arranque que hay que resolver

"X% de las personas que hicieron este quiz tienen tu misma debilidad" es el mecanismo más fuerte que mencionaste, porque es prueba social, normalización e identidad en una sola línea. El problema: el día del lanzamiento tienes cero usuarios, entonces ese % o es falso o está vacío.

No inventes data falsa, tú eres una marca anti bullshit y eso se huele. Lo que sí puedes hacer: lanza la v1 mostrando solo el bucket, sin el %. Prende el % en vivo cuando cruces un umbral creíble de quizzes completados. Mientras tanto, si quieres rellenar ese espacio, pon una lectura tuya de experta en vez de data viva, algo como tu observación de los founders que diagnosticas, dicho como tu criterio profesional, no como estadística del quiz. Honesto y direccional, sin mentir.

## El backend es donde el quiz se vuelve negocio

Mencionaste el retargeting con Creatividad² pero no conectaste el bucket con la oferta, y ahí está el corazón. Cada bucket de debilidad tiene que mapear a un destino antes de construir. El bucket es el tag, el tag dispara la secuencia, la secuencia empuja a un producto específico.

Ejemplo del principio: si el bucket es "produces contenido pero no tienes estrategia", ese tag dispara una secuencia que termina apuntando al Strategy Sprint o al curso. Si el bucket es "tienes estrategia pero no distribuyes", apunta a otra cosa. Tú ya tienes los frameworks para definir estos buckets, está el diagnóstico de seis etapas y el de Creator/Business que dejaste parqueados. Ese mapa bucket por bucket es el paso que va antes del diseño, y vale una sesión dedicada.

El plumbing lo tienes listo: el correo entra a Mailerlite o vía Resend con n8n, etiquetado por bucket, y la secuencia corre sola.

## El referral de la thank you page: reencuádralo

La idea de la herramienta misteriosa como motor de curiosidad es buena y es muy tú. El problema es el incentivo en el momento exacto del share. Estás ofreciendo un % off de una herramienta que todavía no existe. En el segundo en que comparten, no hay nada que comprar, entonces el premio es 100% diferido y abstracto, que es el tipo de incentivo más débil que hay.

Dos arreglos:

- Reencuádralo de descuento a acceso. En vez de "comparte y obtén % off", "comparte y tú y la persona que refieras entran a la lista prioritaria de la herramienta con tu precio founder bloqueado". Eso pasa de soborno a privilegio de insider, que va con tu posicionamiento de marca que selecciona en vez de rogar.
- Dale gratificación inmediata. Que el acto de compartir desbloquee algo AHORA, no solo algo futuro. Suelta uno de tus productos digitales que ya existen, el LUT pack, la agenda de Notion, el template de script, lo que aplique al bucket. Así el premio no es puro humo diferido y de paso metes tus productos en manos de leads ya calificados por debilidad.

## Mi recomendación, una sola

Construye el quiz como diagnóstico gratis y prescripción gateada, con el correo desbloqueando el plan personalizado más el acceso a la herramienta. Pero antes de tocar una pantalla, cierra el mapa de buckets a ofertas, porque ese mapa es el producto real y todo lo demás cuelga de ahí.

El siguiente paso que tiene más sentido es trabajar ese mapa: definir los buckets de debilidad y a qué destino de Creatividad² lleva cada uno. Una vez que eso esté, el contenido de las preguntas se escribe casi solo, porque cada pregunta existe para empujar a la persona hacia uno de esos buckets. ¿Arrancamos por ahí, o prefieres que primero definamos la lista de preguntas y de ahí derivamos los buckets?

## 🧑 Adriana · 2026-06-19 02:48
quiero disenarlo, que quede listo desarollado en el backend y luego de las primeras 50 submissions lo habilito.

## 🤖 Claude · 2026-06-19 02:53
Lo construí. Antes de que lo abras, tres decisiones que tomé y que tienes que saber para que el backend haga exactamente lo que pediste.

**Los buckets son tu framework de seis etapas**, no inventé un eje nuevo. Usé tu diagnóstico de contenido (estrategia, pre-producción, producción, edición, distribución, análisis) porque ya es tuyo y mapea limpio a un público creador. Todo el contenido vive en un bloque CONFIG arriba del código, editable sin tocar la lógica.

**El % se activa solo después de 50 muestras**, tal como dijiste. Hay un THRESHOLD = 50. Antes de cruzarlo, el resultado muestra una lectura tuya de experta en vez de data falsa. Cuando el contador global llega a 50, el % en vivo se prende automático. Te dejé un contador discreto "muestras: N / 50" en la pantalla de resultado para que monitorees tu fase de siembra. Lo borras antes del lanzamiento público.

**Los correos NO se guardan dentro del quiz, por privacidad.** El storage compartido que alimenta el % es visible para todos los que abran el archivo, entonces meter ahí emails sería un problema. Lo que hice: los conteos por bucket van al storage compartido sin data personal, y el correo se enruta a tu webhook de n8n. Llenas una constante WEBHOOK_URL y los leads caen directo en tu stack, que es donde deben vivir para el retargeting de todas formas.

Déjame escribir el archivo.

Ábrelo y haz el recorrido completo, intro hasta thank you. Funciona de verdad, no es mockup: las respuestas suman peso, calcula tu bucket, guarda el conteo global y avanza por las cinco pantallas.

**Lo que ya está vivo:**

- Diseño en tu marca con la dirección brutalist. Bordes negros duros, sombra offset sin blur, tus seis colores, Poppins para todo lo estructural. Las estrellas son acento de marca en SVG.
- Flujo de 7 preguntas con la última como ancla que pesa doble y desempata, sale tu etapa más débil.
- Resultado con el bucket grande, el diagnóstico en tu voz, y el % gateado a las 50 muestras. Mientras tanto sale tu lectura de experta.
- Captura de nombre y correo, solo dos campos como acordamos, sin apellido.
- Thank you con el referral ya reencuadrado a acceso founder en vez de descuento suelto.

**Lo que tú tienes que llenar (todo está en el bloque CONFIG arriba del código, marcado con [MAPEAR]):**

1. **El mapa bucket a oferta.** Cada bucket tiene un campo `destino` con una sugerencia entre corchetes. Eso es tu decisión de negocio, yo solo dejé placeholders. Es el paso que sigue pendiente desde la sesión pasada y sin él el retargeting no apunta a nada.
2. **El WEBHOOK_URL de n8n.** Vacío ahorita. Cuando lo llenes, cada lead llega como POST con nombre, correo y bucket directo a tu stack. Sin eso, el correo se captura pero no va a ningún lado, es prototipo.
3. **Los corchetes del referral.** `[HERRAMIENTA MISTERIOSA]` y `[TU PRODUCTO DIGITAL]` en la sección thankyou.

**Dos cosas honestas sobre el entorno:**

Tus fuentes de marca Scholar, Heading Now, Glenda y Plunct no cargan por web en este preview, entonces usé Poppins para la estructura y Permanent Marker como stand-in del Plunct hand-drawn. Cuando portes esto a Emergent con tus archivos de fuente embebidos, se ve exacto.

Y el storage compartido que alimenta el % funciona dentro del entorno de Claude. Para el público real, este archivo es tu diseño y tu lógica ya resueltos, listos para portar a Emergent, que es donde lo hosteas público y conectas el webhook. Eso calza con tu flujo de V3.

¿Quieres que ajuste las preguntas, que cambie el eje al diagnóstico Creator/Business en vez del de seis etapas, o trabajamos ya el mapa de bucket a oferta para que el backend apunte a algo concreto?

## 🧑 Adriana · 2026-06-19 02:59
Ok perfecto les regalo algo, aun no se que pero les regalo algo, quizas tenemos que desarollarlo despues. pero dejalo con ese esqueleto. 

Umm no me gusta ese diseno no se parece a los layouts que te di como referencia

## 🤖 Claude · 2026-06-19 03:03
Tienes razón, y el error es mío. En nuestra primera conversación te empujé hacia el neobrutalism, pero tú me dijiste clarísimo que lo que más te gustaba era la 3 por las ilustraciones y la 2 por el layout. Esas dos no son brutalist, son flat ilustrativo, amigable, character-driven, tipografía gigante, campos de color sólido. Yo construí bordes negros duros y sombras offset, que es justo lo que NO se parece a tus referencias. Lo reconstruyo en la dirección correcta.

Tres cosas que cambio:

Saco todo lo brutalist. Adiós bordes negros gruesos, sombras pegadas y fondo de puntos. Entra el lenguaje de Explicai y la imagen 3: cada pantalla es un campo de color sólido completo, esquinas redondeadas, un personaje grande y amigable, tipografía bold enorme.

El personaje. La imagen 2 funciona porque tiene UN personaje recurrente que carga toda la identidad. Tú ya tienes eso en tu brandspec: los doce personajes de emoción de la página 7. Esos son tu versión del blob de Explicai. Por ahora dejo un placeholder de personaje en CSS para que veas el layout correcto, y tú sueltas tus assets reales encima.

El resultado ahora sí muestra los buckets. En la versión pasada me quedé corto. Tú pediste, citando la imagen 1, ver el score de las fallas repartido en buckets. Lo agrego: un breakdown de las seis etapas con su barra, la más débil resaltada, y debajo el % de comparación.

El regalo lo dejo como esqueleto, tal cual pediste. Los corchetes `[HERRAMIENTA MISTERIOSA]` y `[TU PRODUCTO DIGITAL]` se quedan ahí esperando. Toda la lógica del backend queda intacta, solo cambio la piel.

Ábrelo de nuevo. Ahora cada pantalla es un campo de color completo que rota por tu paleta, con el personaje grande, tipografía gigante y esquinas redondeadas. Es el lenguaje de Explicai y la imagen 3, no el brutalist de antes.

Qué cambió de fondo:

- Fuera bordes negros, sombras pegadas y fondo de puntos. Entran campos de color sólido por pantalla, botones pill, sombras suaves.
- El personaje amigable aparece en intro, resultado, captura y thank you, como el blob recurrente de Explicai. Las respuestas viven en un panel crema con rows limpios, igual que las listas de la imagen 2.
- El resultado ahora muestra el breakdown de buckets que pediste citando la imagen 1. Cada etapa con su barra de color, la más débil resaltada con estrella, y debajo el % de comparación gateado a las 50.
- El regalo queda como esqueleto, intacto, con los corchetes esperando.

Dos cosas que tienes que decidir para que quede 100 por ciento tuyo:

El personaje es un placeholder en CSS. Lo construí parecido al de Explicai a propósito, pero lo ideal es soltar tus personajes de emoción de la página 7 del brandspec. Eso es lo que hace que se sienta tuyo y no genérico. ¿Quieres que dejemos un solo personaje recurrente, o que cambie de emoción según la pantalla? Por ejemplo, neutral en las preguntas y la cara que matchee el bucket en el resultado.

Y dime si esta sí va por buen camino. Si todavía sientes que se aleja de las referencias, dime exactamente qué pantalla y de cuál imagen, y lo afino. Si vamos bien, el siguiente paso real es el mapa de bucket a oferta, que sigue siendo lo único que falta para que el backend apunte a algo concreto.

## 🧑 Adriana · 2026-06-19 03:08
dame un prompt con contexto de todo lo que hemos hablado

## 🤖 Claude · 2026-06-19 03:10
Te lo armo como un prompt de build completo, no como prompt de imagen. El skill de prompts que tienes está hecho para generar una sola pieza visual, y esto es un app entero con lógica, funnel y backend, así que ese formato perdería la mitad de lo importante. Lo que sigue es autocontenido: alguien sin contexto podría construir la versión de producción solo con esto. Pégalo en Emergent o en cualquier AI o dev.

```
PROMPT DE BUILD · QUIZ DIAGNÓSTICO DE CONTENIDO · CREATIVIDAD²

CONTEXTO Y OBJETIVO
Construye un quiz diagnóstico interactivo para Adriana V. Márquez (@adrianavmarquez), estratega de marketing creativo. El quiz es una herramienta de pre-validación para su ecosistema educativo Creatividad². No es un juego suelto, es un motor de segmentación con disfraz de quiz: el resultado diagnostica en qué etapa del proceso de contenido falla el usuario, y ese diagnóstico determina a qué oferta de Creatividad² se le hace retargeting después.

PÚBLICO
Creadores de contenido y founders con marca propia que producen pero no monetizan, o que tienen marca pero les falta estructura de estrategia. Hablan español, registro casual.

LÓGICA ESTRATÉGICA (no negociable)
1. El bucket de debilidad es el producto real. Cada bucket mapea a una oferta. El diseño es el envoltorio.
2. Diagnóstico gratis, prescripción gateada. El usuario ve su bucket y el % sin dar nada. El plan personalizado para arreglarlo desbloquea el correo. Esto es consistente con su manifiesto anti acaparar conocimiento.
3. El correo segmenta. El bucket es el tag, el tag dispara la secuencia de email, la secuencia empuja a una oferta.

FLUJO DE PANTALLAS
Intro (hook + promesa) → 7 preguntas → Resultado (bucket + breakdown + %) → Captura (nombre + correo) → Thank you + referral.

DIRECCIÓN DE DISEÑO
Estética: flat ilustrativo amigable. Referencias: el lenguaje de Explicai (un personaje blob recurrente, pantallas de campo de color sólido completo, rows de lista limpios, tipografía editorial bold) y el estilo "ARE YOU READY TO LEARN" (ilustraciones grandes, tipografía gigante, campos de color brillantes, estrellas y sparkles de acento). La pantalla de resultado se inspira en dashboards de learning apps: tarjetas de stat por bucket, número de % grande, comparación.

CADA PANTALLA es un campo de color sólido completo que rota por la paleta. Esquinas muy redondeadas. Botones pill. Sombras suaves. Personaje amigable recurrente. Tipografía Poppins gigante.

QUÉ EVITAR (importante, ya se descartó esta dirección)
NO neobrutalism. Sin bordes negros gruesos, sin sombras offset duras tipo box-shadow sólido pegado, sin fondo de puntos o grid. Eso se ve techy y frío, no se parece a las referencias.

SISTEMA DE MARCA
Colores: #080808 negro, #FFFFFF blanco, #D72323 rojo, #3846C4 azul, #FFBA35 amarillo, #F2E9FF lavanda. Negro y blanco dominantes, los otros cuatro de acento.
Fuentes: Poppins Bold/Black para títulos y estructura. Scholar para subtítulos editoriales. Heading Now para cuerpo. Glenda Sans para captions y datos. Plunct para acentos hand-drawn y firma. En web cargar Poppins por Google Fonts. Las otras embeberlas al portar. Mientras tanto usar Permanent Marker como stand-in de Plunct.
Personajes: usar los 12 personajes de emoción del brandspec como mascota recurrente, al estilo del blob de Explicai. Existen también Adri (cara recortada), El Perro, Clones. En el resultado, el personaje muestra la emoción que matchee el bucket.
Elementos: estrellas pintadas a mano y sparkles como acento. Energía mixed media. Logo: firma "adrianavmarquez" con estrella roja, monogram AM.

CONTENIDO · 6 BUCKETS (framework de seis etapas del proceso de contenido)
1. Estrategia: "Tu contenido se ve bien pero no está conectado a lo que vendes. Grabas por inercia, no por intención. Lo que falta no es producir más, es que cada pieza tenga un para qué claro antes de que prendas la cámara."
2. Pre-producción: "Llegas a grabar sin plan y lo resuelves en el momento. Eso quema tiempo, energía y consistencia. Te falta el sistema que convierte una idea suelta en algo grabable en minutos, no en horas."
3. Producción: "Tienes las ideas pero se quedan en notas. Entre que la piensas y que la ejecutas se pierde casi todo. Tu cuello de botella es sentarte a grabar, no la creatividad."
4. Edición: "Grabas más de lo que publicas porque la edición te traga. Pasas horas en cosas que no mueven la retención. Te falta criterio de qué cortar para que el video respire sin que se te vaya el día."
5. Distribución: "Produces buen contenido y lo escondes. Publicas sin hook, sin pensar la plataforma, y el algoritmo no te lee. El trabajo ya está hecho, lo que falla es cómo y dónde lo sueltas."
6. Análisis: "Publicas y pasas a lo siguiente sin mirar atrás. No sabes qué funcionó ni por qué, entonces repites lo que no sirve. Sin leer tus números, estás creando a ciegas."

CONTENIDO · 7 PREGUNTAS (cada opción etiqueta una debilidad o "none")
Q1 Se te ocurre una idea buena, qué pasa: a) la anoto y se queda=produccion b) la grabo pero no sé para qué=estrategia c) la pienso tanto que se pasa=preproduccion d) la planeo grabo y publico=none
Q2 Cuando te toca grabar cómo llegas: a) improviso=preproduccion b) idea sin guión ni tomas=preproduccion c) cansada y no grabo=produccion d) con plan claro=none
Q3 Cada cuánto publicas: a) sin ritmo fijo=distribucion b) seguido sin pensar hook=distribucion c) grabo en lotes pero no publico=edicion d) calendario y lo cumplo=none
Q4 La edición es: a) lo que más tiempo me come=edicion b) videos a medias que no salen=edicion c) ni llego porque no grabo=produccion d) rápida ya tengo flujo=none
Q5 Después de publicar: a) paso a lo siguiente sin números=analisis b) veo likes pero no entiendo=analisis c) me frustro y no sé por qué=analisis d) reviso métricas y ajusto=none
Q6 Tu contenido y lo que vendes: a) caminos separados=estrategia b) no sé qué vendo=estrategia c) vendo pero el contenido no lo refleja=estrategia d) conectados con para qué=none
Q7 (ANCLA) Si arreglaras UNA cosa hoy: estrategia / preproduccion / produccion / edicion / distribucion / analisis

SCORING
Suma peso por debilidad. Peso 1 normal. Q7 es ancla, peso 2, y desempata. El bucket con más peso es el resultado. "none" no suma.

BACKEND Y LÓGICA
Agregados compartidos: guarda conteo por bucket y total global, sin data personal.
% en vivo = conteo del bucket / total, redondeado. Se muestra SOLO si total >= 50 (constante THRESHOLD). Antes de 50, mostrar una línea de lectura de experta ("De cada 10 creadores que diagnostico, la mayoría se atasca justo aquí"), nunca data falsa.
Captura: solo nombre y correo, sin apellido. Al enviar, POST a WEBHOOK_URL con {nombre, email, bucket, ts} hacia n8n, Mailerlite o Resend. NUNCA guardar correos en el storage compartido por privacidad.
Contador admin discreto "muestras: N / 50" en el resultado, removible antes del lanzamiento público.

PANTALLA DE RESULTADO (detalle)
Hero con el nombre del bucket grande y el personaje con la emoción que matchee. Breakdown de las 6 etapas, cada una con barra de color proporcional al score, la más débil resaltada con estrella. Debajo el stat del % gateado. CTA "Desbloquear mi plan".

CAPTURA Y REFERRAL
Thank you celebratorio. Referral reencuadrado a acceso, no a descuento suelto: comparte y los dos entran a la lista prioritaria de [HERRAMIENTA MISTERIOSA] con precio founder bloqueado, y desbloquea [PRODUCTO DIGITAL] ahora mismo. Esqueleto, los corchetes se llenan después. Share vía navigator.share o copiar link.

PENDIENTES POR DEFINIR
1. Mapa bucket a oferta de Creatividad² (Strategy Sprint, Apoyo Express, VIP 3 Actos, LUT pack, agenda Notion, curso, bootcamp, community).
2. El regalo del referral, todavía sin definir, dejar el esqueleto.
3. WEBHOOK_URL real de n8n.
4. Soltar los personajes de emoción reales sobre el placeholder.
5. Embeber las fuentes de marca al portar.

NOTAS TÉCNICAS Y DE VOZ
Mobile-first. Target Emergent o HTML single-file. Respetar prefers-reduced-motion, foco de teclado visible. Voz de Adri: sin em dashes, prohibido "no es X es Y" y "X no ha muerto solo lo haces mal", hooks específicos con números reales, nada de lenguaje corporativo vacío.
```

Esto refleja todo lo que decidimos, incluida la corrección de brutalist a flat ilustrativo. Si quieres, te lo dejo también en inglés para que Emergent lo procese mejor, o le agrego el mapa de bucket a oferta una vez que lo definamos, que sigue siendo el único hueco que mantiene el backend apuntando al vacío.

## 🧑 Adriana · 2026-06-19 03:19
esta bien en teoria pero mal en la practica, porque esta muy basico hay que jugar con el font size font stretch superposiciones ejemplo

## 🤖 Claude · 2026-06-19 03:23
Esa imagen es justo el nivel de tensión que le falta. Lo que tienes razón en señalar es que mi versión está tipográficamente plana: un solo tamaño de Poppins, todo alineado, todo del mismo peso. El FLAMXDESIGN funciona por contraste brutal de escala, stretch vertical, palabras fantasma repetidas detrás, italic serif chocando con el bold condensado, y cosas que se montan unas sobre otras. Eso es lo que le voy a inyectar.

Dónde meto la energía sin romper el quiz:

Los momentos hero (intro, resultado, thank you) reciben el tratamiento completo: palabra gigante estirada, fantasma repetido detrás, italic serif de acento, scribble encima, tape rotado. Las preguntas y respuestas reciben personalidad pero se mantienen legibles, porque un quiz que no se puede leer no convierte. Ahí está el balance.

Sobre las fuentes: el stretch lo hago con transform scale sobre Poppins, así juego con font size y font stretch sin romper tu regla de marca. El italic serif editorial, esas palabras inclinadas tipo "tendências" y "básicas", es el rol de tu Scholar. Lo cargo con DM Serif Display como stand-in hasta que embebas Scholar real.

Déjame reconstruirlo.

Ábrelo. Ya no está plano. Esto es lo que metí del FLAMXDESIGN:

**Contraste de escala brutal.** El nombre del bucket en el resultado entra gigante, estirado vertical, casi rompiendo la pantalla. Al lado, labels chiquitas en tape. Esa diferencia de tamaño es la tensión que pedías.

**Font stretch real.** Las palabras titán usan transform scaleY para estirarse hacia arriba, ese look comprimido y alto del SALVE y el FOD4S. Es Poppins jugando con la forma, sin salirme de tu marca.

**Italic serif chocando con bold.** Cada título tiene una palabra en italic serif minúscula peleando contra el resto en bold mayúsculas. Como "marcas" y "tendências" y "básicas" en tu referencia. Ese es el rol de tu Scholar.

**Palabras fantasma detrás.** Igual que el TUDO y el GENZ repetidos al fondo, cada pantalla tiene una palabra gigante fantasma detrás del contenido. El número de pregunta también vive ahí atrás, enorme y tenue.

**Tape rotado y scribble.** Los eyebrows ahora son strips de highlighter amarillo rotados, como "De um jeito que ninguém mais conversa". Y el título de intro tiene un scribble rojo encima, como el óvalo rosa sobre SALVE.

Lo que cuido: las preguntas y las respuestas mantienen legibilidad. El caos vive en los momentos hero, no donde la persona tiene que leer para decidir. Si meto ransom-note en las opciones, el quiz deja de funcionar.

Dos cosas para calibrar:

¿El stretch del bucket en el resultado se siente bien o lo quieres aún más agresivo, más alto y más comprimido? Puedo subirle.

Y dime si quieres que las palabras fantasma sean palabras tuyas de marca en vez de repetir la de la pantalla. Por ejemplo "creatividad²" fantasma de fondo en todas, o palabras sueltas tipo tu manifiesto. Eso lo amarraría más a tu mundo y menos a un efecto genérico.
