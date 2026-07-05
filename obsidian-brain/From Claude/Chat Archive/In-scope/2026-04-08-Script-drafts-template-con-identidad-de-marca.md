---
title: "Script drafts template con identidad de marca"
source: claude.ai-chat
created: "2026-04-08 13:32"
summary: "**Conversation overview**  Adri (@adrianavmarquez) is a content creator who works on brand collabs and sponsorships. She came to this conversation wanting to build a reusable skill for generating official brand collaboration script documents to share with partner brands via Google Docs. She shared an existing script she had created for a Pippit AI collab as the reference example for her desired format and aesthetic.  The conversation was focused on understanding her exact workflow and production system before building anything. Key clarifications established: the document structure is always fixed in the same order (header, beat-by-beat script table, overlays for brand approval, production notes, visual references); the 'overlays' section is for brand-approval of on-screen texts, claims, CTAs, and handles — not a prompt template; visual references are optional and help brands understand the visual tone; and contractual details like dates, fees, and deliverables are intentionally excluded from scripts and handled separately in contracts and emails.  Claude built a `.docx` generator in Node.js using her exact brand aesthetic: Poppins font, red #D72323 for section titles and script table headers, dark #1A1A1A background for the overlays approval table with yellow #FFBA35 and white text, ★ stars in blue #3846C4 and yellow at document open and close, alternating gray rows in the beats table, and middle-dot `·` bullets. The subtitle was updated from 'Script + Prompt Template' to 'Script + Overlays + Producción + Ref Visuales' per her correction. The skill was named `script-skill`, packaged as a `.skill` file, and is designed to activate automatically when she says things like 'hazme el script para [marca]' — no slash command needed."
messages: 18
claude_uuid: "1956999a-b4e2-4887-9eda-a5ccb1c6c626"
tags: [claude, chat, archive]
---
# Script drafts template con identidad de marca

> **Conversation overview**

Adri (@adrianavmarquez) is a content creator who works on brand collabs and sponsorships. She came to this conversation wanting to build a reusable skill for generating official brand collaboration script documents to share with partner brands via Google Docs. She shared an existing script she had created for a Pippit AI collab as the reference example for her desired format and aesthetic.

The conversation was focused on understanding her exact workflow and production system before building anything. Key clarifications established: the document structure is always fixed in the same order (header, beat-by-beat script table, overlays for brand approval, production notes, visual references); the "overlays" section is for brand-approval of on-screen texts, claims, CTAs, and handles — not a prompt template; visual references are optional and help brands understand the visual tone; and contractual details like dates, fees, and deliverables are intentionally excluded from scripts and handled separately in contracts and emails.

Claude built a `.docx` generator in Node.js using her exact brand aesthetic: Poppins font, red #D72323 for section titles and script table headers, dark #1A1A1A background for the overlays approval table with yellow #FFBA35 and white text, ★ stars in blue #3846C4 and yellow at document open and close, alternating gray rows in the beats table, and middle-dot `·` bullets. The subtitle was updated from "Script + Prompt Template" to "Script + Overlays + Producción + Ref Visuales" per her correction. The skill was named `script-skill`, packaged as a `.skill` file, and is designed to activate automatically when she says things like "hazme el script para [marca]" — no slash command needed.

## 🧑 Adriana · 2026-04-08 13:32
quiero hacer un skill bien especifico de  mis colores, mis instrucciones para hacer scripts drafts para compartir con las marcas. primero te mostrare uno que ya hice.

RECUERDA MI FONTS Y MIS COLORES, PERO MIRA LA FORMA SUBLIME EN LA QUE USO LOS COLORES, LAS ESTRELLITAS DE MI BRAND.

Primero queiro asegurarme que entiendes mis peticiones que me ensenes un template y liuego cuandoe ste conforme t edigo que lo vuelvas un skill

## 🤖 Claude · 2026-04-08 13:32
Perfecto. Leí el PDF completo, lo entendí al detalle.

Antes de construir el template, déjame confirmarte lo que capturé de tu sistema de producción para asegurarme que el skill lo refleje exactamente:

**Lo que vi en el doc de Pippit:**

Tu formato de script doc tiene estas secciones:
1. Header con título del collab + subtítulo + handle
2. "Script Beat by Beat" como tabla de 3 columnas: Visual / Script+Texto en pantalla / Notas de dirección
3. "Prompt Template — Haz Screenshot" (bloque oscuro, copy-paste ready)
4. "Notas de Producción" en lista de bullets
5. "Referencias Visuales" con imágenes

**Estética que noté:**
- Tu rojo (#D72323) en títulos y headers de columna
- Texto negro sobre blanco limpio
- La estrellita azul ★ como elemento de marca (aparece en esquinas, pie de página)
- Tipografía bold, Poppins
- Bordes en tablas, todo muy estructurado pero respirado
- Subtítulos en itálica
- El bloque de prompt en fondo oscuro / negro (contraste total)

Lo que necesito que me confirmes antes de hacer el template:

1. El orden de las secciones: ¿siempre es el mismo o cambia según el tipo de collab?
2. ¿El "Prompt Template" es específico de Pippit o lo incluyes en todos los scripts de marca?
3. ¿Las referencias visuales siempre van al final o a veces abren el doc?
4. ¿Hay alguna sección que yo no vi en el PDF que normalmente incluyes, como deliverables, fechas, o redes destino?

Con eso te armo el template y te lo muestro antes de convertirlo en skill.

## 🧑 Adriana · 2026-04-08 13:35
el "Prompt Template — Haz Screenshot" (bloque oscuro, copy-paste ready)
es util solo para este script pero la idea es que en esta seccion agregue informacion importante que agregare como overlay al video apra que la marca lo apruebe

## 🤖 Claude · 2026-04-08 13:35
Ah, perfecto. Entonces esa sección no es el prompt de Pippit específicamente, es el espacio donde vas a poner **los overlays clave que necesitan aprobación de la marca** antes de grabar. Tipo:

- Textos que van en pantalla
- Claims o frases que mencionan el producto
- CTAs que vas a decir o mostrar
- Links o handles que aparecen en video

¿Lo entendí bien?

Y las otras preguntas que te hice, ¿me las puedes confirmar rápido?

1. **Orden de secciones**: ¿siempre el mismo o varía?
2. **Referencias visuales**: ¿siempre al final?
3. **¿Hay secciones que faltan?** Deliverables, fechas de entrega, plataforma destino (IG Reels, TikTok, YouTube Shorts), número de versión del script...

Porque quiero que el template sea tu sistema real, no uno genérico que luego tienes que adaptar cada vez.

## 🧑 Adriana · 2026-04-08 13:39
1. si el ordene sta bien. 
1. las ref visuales es para que la marca entienda lo que me imagino si hiciese falta. 
2. no no incluyo esas cosas en el script, suelen estar en el correo que va con el script y en el contrato que se firma antes de incluso empezar

## 🤖 Claude · 2026-04-08 13:39
Perfecto, crystal clear. Entonces el template queda así:

**5 secciones, siempre en ese orden:**

1. Header (título collab + handle)
2. Script Beat by Beat (tabla 3 col)
3. Textos para aprobación de marca (overlays, claims, CTAs, handles que aparecen en video)
4. Notas de producción
5. Referencias visuales (solo si aplica)

Ahora, una última cosa antes de hacer el template visual: el PDF que me compartiste lo hiciste tú directamente, ¿en qué herramienta? ¿Canva, Google Docs, Word, Notion?

Porque necesito saber si el skill debe generar el PDF desde aquí con tu estética exacta, o si es un template que llevas a tu herramienta de preferencia.

## 🧑 Adriana · 2026-04-08 13:41
Google Docs para poder compartiselo a las marcas facilmente y que dejen comments

## 🤖 Claude · 2026-04-08 13:41
Perfecto. Entonces el skill tiene que generar un **Google Doc** con tu estética, pero aquí hay un detalle técnico importante que quiero ser honesta contigo:

Google Docs no soporta fuentes custom (Poppins) ni elementos de diseño complejos directamente desde código. Las opciones reales son:

**Opción A: Google Doc funcional** con tu estructura, colores en títulos/headers usando los colores hex que tienes, tabla de 3 columnas, todo organizado. Las marcas pueden comentar fácil. Poppins no va a estar pero el doc se ve profesional y limpio. Lo genero desde aquí y te doy el link directo.

**Opción B: PDF como el que me mostraste** con tu estética completa, estrellitas, Poppins, todo exacto. Pero las marcas no pueden dejar comments directamente, tendrían que hacerlo por email o en una herramienta aparte.

**Opción C: Canva Doc** que sí soporta Poppins, tus colores exactos, las estrellitas, y permite comentarios cuando compartes el link. Es el punto medio entre diseño y colaboración.

¿Cuál de las tres te funciona mejor para tu flujo real con las marcas?

## 🧑 Adriana · 2026-04-08 13:41
obvioq eu lo soporta si ya lo hice, solo crealo en docx normal y yo lo abro en google doc

## 🤖 Claude · 2026-04-08 13:43
Jajaja tienes razón, perdón. Si ya lo hiciste así, obvio funciona.

Déjame leer el skill de docx primero para hacerlo bien.

Listo, ya leí el skill. Ahora voy a construir el template con tu estética exacta, basándome en el PDF que me mostraste.

Ahí está. Ábrelo en Google Docs y dime qué ajustar.

Lo que construí tiene exactamente las 5 secciones en orden, con tu estética: rojo en títulos, la tabla de beats con header en rojo, el bloque oscuro de aprobación de marca en negro con texto amarillo y blanco (como tu prompt template), bullets con "·" en notas y referencias, y las estrellitas ★ en azul y amarillo al inicio y al final del doc.

Dime qué no te gusta, qué falta o qué cambiar, y cuando estés conforme lo convertimos en skill.

## 🧑 Adriana · 2026-04-08 13:44
habria que cambiar Script + Prompt Template por: Script + Overlays + Producción + Ref Visuales

## 🤖 Claude · 2026-04-08 13:44
Hecho.

¿Qué más?

## 🧑 Adriana · 2026-04-08 13:45
ok para leer el skill draft

## 🤖 Claude · 2026-04-08 13:46
Perfecto, ya leí todo. Voy a escribir el draft del skill ahora.

Lo que va a hacer este skill: cuando le pidas un script de collab para una marca, generar automáticamente el `.docx` con tu estructura exacta, tus colores, tus estrellitas, listo para abrir en Google Docs y compartir.

Listo. Aquí está el draft del skill para que lo leas antes de aprobar:

**Lo que hace:** cuando le pidas "hazme el script para [marca]" o cualquier variación, sabe exactamente qué estructura generar, en qué orden, con qué estética, y qué preguntar si le falta información.

**Las reglas que grabé en el skill:**
- Subtítulo siempre: `Script + Overlays + Producción + Ref Visuales`
- Colores, fuente y estrellitas exactos, no negociables
- Nunca inventar claims o nombres de producto sin preguntarte
- Nunca meter fechas, honorarios ni términos contractuales (eso va en el contrato)
- Bullets con `·`, no bullets estándar

¿Hay algo que cambiar, agregar o que no refleja cómo trabajas realmente? Cuando estés conforme lo empaqueto como `.skill` y lo instalas.

## 🧑 Adriana · 2026-04-08 13:49
ok llamemozlo script-skill y que codigo uso para darle run? /script ??

## 🤖 Claude · 2026-04-08 13:49
Dos cosas rápido:

**Nombre:** cambiado a `script-skill`.

**Sobre el código para activarlo:** no necesitas ningún comando. Los skills no se activan con slash commands, se activan solos cuando Claude detecta que aplican por el contexto de lo que pides.

O sea, simplemente le dices algo como:

- *"hazme el script para la collab con [marca]"*
- *"prepara el doc de collab para [marca]"*
- *"arma el script para [marca]"*

Y el skill se dispara solo, te pregunta lo que falta y genera el `.docx`.

¿Lo empaqueto ahora como `.skill` para que lo puedas instalar?

## 🧑 Adriana · 2026-04-08 14:00
sip

## 🤖 Claude · 2026-04-08 14:01
El problema es que la descripción tiene dos puntos `:` en medio y el YAML se confunde. Lo arreglo rápido.

Listo. Para instalarlo:

1. Descarga el archivo `script-skill.skill`
2. Ve a claude.ai → Settings → Skills
3. Arrastra el archivo ahí

Y ya. La próxima vez que le digas "hazme el script para [marca]" lo detecta solo y genera el `.docx` con toda tu estética.
