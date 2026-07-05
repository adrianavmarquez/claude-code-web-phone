---
title: "Generar foto realista con fondo personalizado"
source: claude.ai-chat
created: "2026-07-02 00:52"
summary: "**Conversation Overview**  This conversation centered on a complex, multi-phase content creation project involving two interconnected goals: generating photorealistic AI-composed images of a woman creator at different camera angles with nature backgrounds, and recreating a viral-style social media video where her community grows from her alone to surrounded by thousands of people. The session moved fluidly between photo compositing strategy, video format analysis, tool selection, and prompt engineering, with significant iteration and course-correction throughout.  On the photo side, Claude analyzed four background images and six subject photos, identifying that camera angle matching is the non-negotiable constraint for believable composites. The creator had planned a frontal, side, top-down, and eagle-view sequence, but Claude diagnosed that her subject photos only provide two camera families (eye-level frontal and slightly elevated), making a true side and cenital impossible with existing assets. The recommended pairing was her elevated full-body shot with the high-angle grass background, and a frontal shot with the pine/meadow background. Higgsfield AI was identified as the compositing tool, with the upload widget opened multiple times.  On the video side, the creator wants to recreate a format where the camera pulls back to reveal a growing crowd, with a spoken hook ('Cuando pienses que tu comunidad es demasiado pequeña para hacer la diferencia, mira esto') replacing the text-based hook from the reference. Claude transcribed the hook using Whisper, analyzed both reference and source video files via ffprobe and frame extraction, and detected that the reference (0701.mp4) is a single unbroken 11.7-second handheld take with no cuts, making continuity the core mechanic rather than editing. The creator has four recorded angles: a close-up talking head (the hook), eye-level frontal, slightly elevated frontal, and a side angle. The elevated frontal was identified as the hero shot for the crowd reveal because it provides the most depth perception for showing crowd scale.  A substantial portion of the session involved a repeated pattern: Claude recommending compositing or matting tools for the hook shot, and the creator attempting generative AI tools (Higgsfield's generative mode, Seedance via Higgsfield Computer's auto-prompt, Google Flow) that consistently regenerated her face and altered her voice. Claude diagnosed the root cause as a categorical mismatch, generative models repaint every frame including the subject, while the task requires compositing where the subject layer is frozen. The rule established: 'generation creates what doesn't exist; compositing preserves what does.' CapCut's Remove Background and DaVinci Resolve's Magic Mask were recommended as the correct tools for the hook. The creator noted that CapCut results look fake, which Claude attributed to three missing signals: contact shadow, overly sharp cutout edges needing feathering, and mismatched color temperature and defocus between subject and background layers, with a rimlight trick to sell placement.  Late in the session, the creator shared Higgsfield's official Seedance 4K VFX blog, and Claude read the actual prompt structures used there. This revealed that the official workflow discards original audio entirely, contradicting prior prompt attempts to preserve the creator's voice via 'source dialogue only.' Claude rewrote the prompt using Higgsfield's exact block structure with SOURCE LOCK, INTEGRATION, LIGHT-MATCH, PHYSICS, and FORBIDDEN sections, anchoring to the source clip via the `<<<video_1>>>` tag rather than prose description. The audio preservation workaround identified was: generate with audio, mute the generated track, and re-layer the original audio in post, which works because video-to-video preserves mouth timing. Claude also noted that Higgsfield's own examples all involve mid or wide shots with movement, making the close-up talking-head hook the hardest possible case for this technique.  The creator communicates in Caribbean Spanglish and prefers direct, dense analysis without softening language. She pushes back decisively when advice doesn't match her constraints, and Claude adapted multiple times based on her corrections, notably when she clarified that the rule is to transform footage she already recorded rather than generate new angles. She expressed frustration with tool failures using direct language and expects Claude to investigate before advising, which led to multiple web searches, ffprobe analysis, frame extraction, audio transcription, and page fetches throughout the session."
messages: 38
claude_uuid: "ce67939b-f396-4022-8511-fc81938b60f2"
tags: [claude, chat, archive]
---
# Generar foto realista con fondo personalizado

> **Conversation Overview**

This conversation centered on a complex, multi-phase content creation project involving two interconnected goals: generating photorealistic AI-composed images of a woman creator at different camera angles with nature backgrounds, and recreating a viral-style social media video where her community grows from her alone to surrounded by thousands of people. The session moved fluidly between photo compositing strategy, video format analysis, tool selection, and prompt engineering, with significant iteration and course-correction throughout.

On the photo side, Claude analyzed four background images and six subject photos, identifying that camera angle matching is the non-negotiable constraint for believable composites. The creator had planned a frontal, side, top-down, and eagle-view sequence, but Claude diagnosed that her subject photos only provide two camera families (eye-level frontal and slightly elevated), making a true side and cenital impossible with existing assets. The recommended pairing was her elevated full-body shot with the high-angle grass background, and a frontal shot with the pine/meadow background. Higgsfield AI was identified as the compositing tool, with the upload widget opened multiple times.

On the video side, the creator wants to recreate a format where the camera pulls back to reveal a growing crowd, with a spoken hook ("Cuando pienses que tu comunidad es demasiado pequeña para hacer la diferencia, mira esto") replacing the text-based hook from the reference. Claude transcribed the hook using Whisper, analyzed both reference and source video files via ffprobe and frame extraction, and detected that the reference (0701.mp4) is a single unbroken 11.7-second handheld take with no cuts, making continuity the core mechanic rather than editing. The creator has four recorded angles: a close-up talking head (the hook), eye-level frontal, slightly elevated frontal, and a side angle. The elevated frontal was identified as the hero shot for the crowd reveal because it provides the most depth perception for showing crowd scale.

A substantial portion of the session involved a repeated pattern: Claude recommending compositing or matting tools for the hook shot, and the creator attempting generative AI tools (Higgsfield's generative mode, Seedance via Higgsfield Computer's auto-prompt, Google Flow) that consistently regenerated her face and altered her voice. Claude diagnosed the root cause as a categorical mismatch, generative models repaint every frame including the subject, while the task requires compositing where the subject layer is frozen. The rule established: "generation creates what doesn't exist; compositing preserves what does." CapCut's Remove Background and DaVinci Resolve's Magic Mask were recommended as the correct tools for the hook. The creator noted that CapCut results look fake, which Claude attributed to three missing signals: contact shadow, overly sharp cutout edges needing feathering, and mismatched color temperature and defocus between subject and background layers, with a rimlight trick to sell placement.

Late in the session, the creator shared Higgsfield's official Seedance 4K VFX blog, and Claude read the actual prompt structures used there. This revealed that the official workflow discards original audio entirely, contradicting prior prompt attempts to preserve the creator's voice via "source dialogue only." Claude rewrote the prompt using Higgsfield's exact block structure with SOURCE LOCK, INTEGRATION, LIGHT-MATCH, PHYSICS, and FORBIDDEN sections, anchoring to the source clip via the `<<<video_1>>>` tag rather than prose description. The audio preservation workaround identified was: generate with audio, mute the generated track, and re-layer the original audio in post, which works because video-to-video preserves mouth timing. Claude also noted that Higgsfield's own examples all involve mid or wide shots with movement, making the close-up talking-head hook the hardest possible case for this technique.

The creator communicates in Caribbean Spanglish and prefers direct, dense analysis without softening language. She pushes back decisively when advice doesn't match her constraints, and Claude adapted multiple times based on her corrections, notably when she clarified that the rule is to transform footage she already recorded rather than generate new angles. She expressed frustration with tool failures using direct language and expects Claude to investigate before advising, which led to multiple web searches, ffprobe analysis, frame extraction, audio transcription, and page fetches throughout the session.

## 🧑 Adriana · 2026-07-02 00:52
me puedes ayudar a generar una foto con higgsfield ai, que se vea realista en color angulo proporcion todo, substituyengo el fondo de estas imagenes: (attached) con un fondo como:

## 🤖 Claude · 2026-07-02 00:53
Adri is asking for help generating a realistic photo with Higgsfield AI where the background gets replaced, but her message cuts off right when she's about to specify what background she wants—she started saying "with a background like:" but didn't finish. I need to ask her what kind of background she's looking for before I can help.

I'm also realizing that the images she attached to the chat won't be directly accessible to the Higgsfield tools since they're local to this conversation. She'd need to upload them through Higgsfield's interface first, or I could guide her through the workflow using their background replacement features like removing the background and compositing it onto a new one, or using their image generation tools with the original as a reference.

But the real blocker is that her message cuts off at "con un fondo como:" — she never specified what background she wants. I need to ask her directly what she's envisioning before we can move forward.

Once she tells me, I can walk her through the exact workflow: upload the six images through Higgsfield's widget, then use Nano Banana Pro for a realistic background swap that preserves her lighting and perspective. The key is matching her warm interior lighting and eye-level camera angle to whatever new background she chooses, plus keeping her identity and outfit details sharp since she's creating UGC content where authenticity matters. I need to nail down the background and scope first—which images actually need the swap, and what's the background vision. The close-up with the mic probably isn't a candidate anyway. Once I know that, I'll open the upload widget for the right images and we're ready to generate.

## 🧑 Adriana · 2026-07-02 00:53
fondo como este, uno frontsl, otro side, otro top down y otro eagles view

## 🤖 Claude · 2026-07-02 00:58
Antes de quemar créditos en Higgsfield, hay una verdad de perspectiva que decide si esto se ve real o se ve pegado con Photoshop del 2009: el ángulo de cámara del sujeto tiene que ser el mismo ángulo de cámara del fondo. Eso no se negocia. Si tu cuerpo está tirado a la altura del pecho y el fondo está tomado desde un dron mirando al piso, el cerebro de quien lo ve detecta el fraude en menos de un segundo aunque no sepa explicar por qué. Es disonancia de línea de horizonte.

Te destrinco lo que tienes.

**Tus fotos (sujeto) están en dos posiciones de cámara, no en cuatro:**
- Nivel de ojo, de frente: imágenes 2 y 3.
- Ligeramente elevada, cuerpo girado: imágenes 4, 5 y 6.

**Tus fondos están en tres posiciones:**
- Nivel de ojo / frontal: fondo 2 (colina y cielo) y fondo 4 (pinos con grano de película).
- Ángulo alto en diagonal: fondo 3 (césped con sombra de árbol).
- Cenital total, recto hacia abajo: fondo 1 (el pasto puro).

**Cruzando eso con tus cuatro ángulos pedidos:**

**Frontal.** Cuadra perfecto. Imagen 3 (brazos abiertos) sobre fondo 4. Los dos a nivel de ojo, los dos de frente, y el grano del fondo 4 pega con tu estética de película. Alterna: imagen 2 sobre fondo 2 si quieres espacio negativo arriba para un hook.

**Eagle / ángulo alto.** Cuadra. Imagen 6 (girada, cámara arriba) sobre fondo 3. Los dos miran hacia abajo, la línea del piso coincide. Esta misma toma te resuelve el "side" también, porque tu cuerpo ya está de perfil ahí.

**Side limpio a nivel de ojo.** No lo tienes. Tus únicas tomas de perfil (5 y 6) están elevadas. Si quieres un side plano de verdad, son 5 segundos de reshoot: te giras de perfil, cámara a la altura del pecho, mismo outfit.

**Top down (fondo 1).** Aquí se rompe todo. Ese fondo es cenital puro, mirando recto al suelo. Para que un cuerpo se vea real ahí tú tienes que estar acostada en el piso con la cámara directamente encima. No tienes ninguna foto así. Cualquier cosa que genere la IA con tu cuerpo parado sobre ese pasto va a verse flotando. Reshoot obligatorio si lo quieres.

**Dos cosas que la IA tiene que corregir sí o sí, y que voy a forzar en el prompt:**
- Temperatura de luz. Tus fotos son tungsteno cálido de interior. Los fondos son luz de día. Hay que regradear tu piel y ropa a la luz de la escena o te vas a ver naranja sobre un campo frío.
- Sombra de contacto. Afuera proyectas sombra en el pasto según de dónde viene el sol del fondo. Sin esa sombra no tocas el piso, y ahí muere el realismo.

**Plan de ejecución.** Uso Nano Banana Pro, que aguanta referencias múltiples y regrada la luz mejor que los demás para este tipo de swap. Higgsfield no puede leer los archivos que subiste al chat, así que te abrí el widget de upload. Súbeme ahí la imagen 3, la 6 y los fondos 4 y 3 para arrancar con las dos composiciones que sí cuadran. En cuanto me confirmes las subidas, las corro.

## 🧑 Adriana · 2026-07-02 00:58
te pregunto, yo tengo los videos, pero tienen fondo, es mejor hacelro d euna vez con el vidoe o generar las imagenes apra dar como referencia al generar video por video?

## 🤖 Claude · 2026-07-02 01:00
La pregunta real no es "video o imagen". Es: en esos clips, ¿estás hablando a cámara con audio, o es puro b-roll con música encima?

Lo pregunto porque la imagen 1 tiene el mic en mano y la boca abierta. Si hay segmento hablado, generar video clip por clip queda descartado de una. Ningún modelo te va a regenerar tu delivery real y menos sincronizado al audio. Lo que salga va a ser tu cara moviéndose inventada con lip sync postizo encima. Eso no es realismo, es un deepfake tuyo mal hecho.

**Mi recomendación directa: no generes video. Reemplaza el fondo sobre el video real.** Roto/matting del sujeto y le metes el fondo nuevo detrás. Mantienes tu cara exacta, tu movimiento real, el outfit tal cual (el plaid, las cuentas rojas, la textura peluda del cardigan) y el audio intacto. Todo lo que hace que se vea como tú y no como una versión AI de ti.

El workflow que propones (generar las fotos primero como referencia y luego video por video) es lo peor de los dos mundos para tu caso:

- Paso extra de generar stills.
- El video gen igual te inventa el movimiento y no cuadra con ningún audio.
- Riesgo de identity drift en CADA clip: tu cara cambia sutil, el outfit se alucina.
- El costo se multiplica por clip.
- Inconsistencia. Cada clip generado sale un poco distinto al anterior, y eso se nota más que cualquier fondo bonito.

Cuándo SÍ valdría el camino imagen a video: si TODO el pedazo es b-roll silencioso, sin hablar, y aceptas que el movimiento sea inventado por la AI en vez de tu movimiento real. No es lo que describiste. Tú dijiste "que se vea realista en color, ángulo, proporción, todo". Realismo máximo más footage real disponible = te quedas con el footage real, siempre. Generar mete fakeness por definición.

Un detalle honesto: el reemplazo de fondo sobre video real es más movida de editor (roto + placa de fondo + relight en CapCut o After Effects) que un botón mágico. Higgsfield te da el recorte con su background removal de video, pero la parte que hace que se vea creíble pasa en la edición, no en el modelo. Lo que delata un composite falso nunca es el recorte, es esto:

1. **Luz.** La tuya es cálida y viene de un lado del cuarto. Si el fondo nuevo implica otra dirección o temperatura, tu cuerpo grita "pegado encima". Hay que regradear tu figura para que cuadre.
2. **Sombra de piso.** Ahorita proyectas sombra sobre la alfombra. Si quitas el cuarto sin recrear una sombra de contacto, quedas flotando. Ese detalle es el 80 por ciento de por qué algo se ve pegado.
3. **Bordes.** El cardigan peludo y los pelitos sueltos son justo donde el matting se rompe. Fondo muy contrastante al amarillo = halo visible.
4. **Profundidad de campo.** Tu fondo actual está suave. Si metes un fondo AI perfectamente nítido, el ojo detecta que no son del mismo lente.
5. **Altura de cámara.** Tus tomas están a cierta altura de lente. El fondo tiene que compartir la misma línea de horizonte o la proporción se parte.

Antes de comprometerte a nada, haz el diagnóstico en un frame. Agarra la imagen 4 (la más frontal, cuerpo completo, buena luz) y prueba el reemplazo de fondo en UNA sola foto con Nano Banana Pro, pasándole tu foto más la referencia de fondo. Mira dos cosas nada más: ¿sobrevivió tu cara? ¿sobrevivió el outfit? Ese test de dos minutos te dice si la generación es viable para tu cara antes de quemar créditos en seis clips.

Si el frame pasa y todo es b-roll, puedes ir a imagen y de ahí a video. Si drifta o hay segmento hablado, reemplazo de fondo sobre el video real, sin generar.

Por cierto, la referencia de fondo que ibas a adjuntar no llegó. Mándamela y te digo si ese fondo específico va a pelear con tu luz cálida o si cuadra.

## 🧑 Adriana · 2026-07-02 01:02
quiero es recrear un video asi, la diferencia es que en e mio el hook es hablado. mi video hablado es este a continuacion:

## 🤖 Claude · 2026-07-02 01:10
Antes de responder necesito ver el video de referencia. Déjame procesarlo.

Déjame intentar transcribir el audio de los dos videos, porque sin el guion hablado no puedo hacerte el análisis de retención y ritmo que necesitas.

Corrí los dos videos por debajo antes de contestarte, porque lo que encontré cambia el plan de raíz.

El de referencia (0701.mp4) no es un montaje de cortes. Es una sola toma continua, handheld, 11.7 segundos, luz cálida baja de interior, montada sobre música con voz en inglés. Nadie habla a cámara. Corrí detección de cortes a tres umbrales distintos y no aparece ni una sola transición dura. Lo que te gustó de ese video no es *qué* se ve, es que **nunca se corta**. Un solo respiro. Esa es la mecánica real, y es lo que hay que proteger.

Tu clip hablado (1-1.mp4) es el régimen opuesto: 3.9 segundos, tú a cámara en el cuarto claro, diciendo algo muy cercano a esto (confírmame la transcripción exacta, el ASR no es perfecto):

> "Cuando pienses que tu comunidad es demasiado pequeña para hacer la diferencia, mira esto."

Entonces el problema no es estético, es de arquitectura de sonido. En la referencia la música manda desde el segundo cero. En el tuyo la voz manda los primeros 4 segundos y después tiene que entregarle el mando a la música. Ese punto de entrega es donde estos videos se parten y se sienten como dos clips pegados con teip. Es la misma disonancia que te expliqué con las fotos, pero ahora en el eje del tiempo, no del espacio.

Te lo destrinco por partes.

## 1. Lo que rompe un hook hablado (y cómo se resuelve)

Hay dos regímenes chocando. El de audio (voz que lidera contra música que lidera) y el visual (talking head frontal y estático contra cámara que flota). Si pegas tu cara hablando y luego el montaje, tienes dos videos. Hay tres formas de armarlo:

- **A. Voice-over puro.** Tu línea va como VO sobre la toma continua estilo referencia. Nunca cortas a tu cara. Preserva el respiro único al 100%. El "mira esto" cae y el visual *es* el "esto".
- **B. Corte duro con swell.** Tu cara 3-4 seg, luego corte a beat con la música subiendo de golpe. Es la estructura TikTok clásica, pero es la más frágil.
- **C. Híbrido cara a VO.** Tu cara 1 a 1.5 seg (trust, reconocimiento), y tu voz *continúa* como VO mientras la imagen se disuelve al evento. La voz es el hilo, así que nunca se siente pegado.

Para contenido de comunidad y con tu marca, mi recomendación es la C. Un toque de tu cara da autoridad, y la VO sobre el footage del evento es donde vive la emoción.

## 2. El handoff (la parte que todos arruinan)

Durante el hook, la música NO está en silencio. Está sonando baja, ducked unos 15 a 18 dB debajo de tu voz. En la palabra "esto", o justo después, la música sube a nivel full y el montaje toma el control. Ese swell es el disparador emocional, no las imágenes. Y el corte al montaje va montado a un beat, no en cualquier frame. Si el swell y el corte caen juntos sobre "esto", el video se siente como una sola pieza.

Timeline concreto, calcado al largo de la referencia:

- 0.0 a 1.2s: tu cara, música ya presente pero baja. "Cuando pienses que tu comunidad es demasiado pequeña..."
- 1.2 a 4.0s: tu voz sigue como VO, la imagen ya disolvió al evento. "...para hacer la diferencia, mira esto."
- 4.0s: en "esto", corte a beat + swell a full. Sale la voz.
- 4.0 a 11s: toma continua o montaje del evento, solo música.
- 10.5 a 12s: text card con el número o resultado concreto + CTA suave.

## 3. El punto que decide si esto es posible

La referencia es UNA toma continua. Un evento de comunidad casi nunca te da una toma continua de 7 segundos que se sostenga sola. Si solo tienes fragmentos, tu payoff va a ser un montaje de cortes, que es una mecánica distinta a la referencia. No es peor, pero deja de ser "el respiro único". Necesito saber qué footage tienes de verdad antes de prometerte el mismo efecto.

## 4. Análisis del hook (concisión, retención, tono)

Son ~14 palabras, ~4 segundos. La estructura es curiosity loop ("mira esto") fusionado con creencia limitante ("tu comunidad es demasiado pequeña"), buena combinación. Dos observaciones frías:

- El loop abre tarde. "Mira esto" llega al segundo ~3.5. En feed, el loop idealmente abre en el segundo 2. El setup es un pelín largo antes de dar la razón para quedarse.
- "Hacer la diferencia" falla tus tres reglas de oro: no lo puedo visualizar, no lo puedo falsificar, y lo puede decir cualquiera. Es el registro motivacional que tú misma evitas.

Si no vas a regrabar, se compensa en edición: un dato concreto quemado en pantalla durante el hook (cuántas familias, cuánto se levantó) le mete la especificidad que a la línea hablada le falta, sin tocar el audio. Si sí regrabas, el único cambio que vale la pena es reemplazar "hacer la diferencia" por algo falsificable y adelantar el "mira esto".

## Lo que necesito de ti para armarlo

1. El footage del evento: ¿tienes alguna toma continua en movimiento que aguante sola, o son fragmentos sueltos? ¿Cuántos segundos utilizables y en qué luz?
2. ¿Quieres tu cara en el arranque (opción C) o VO puro sobre el evento (opción A)?
3. ¿Regrabas el hook o lo dejamos como está y compensamos con texto en pantalla?

Con eso te devuelvo el edit sheet beat por beat, con los puntos exactos de ducking, swell y corte.

## 🧑 Adriana · 2026-07-02 13:06
este es el frontal y para el video Top down (fondo 1) que lo imagine la ia

## 🤖 Claude · 2026-07-02 13:13
Hay un problema de continuidad que tienes que ver antes de que gastemos un solo crédito, porque de lo contrario vas a terminar con cuatro shots que no pertenecen al mismo video.

1-1.mp4 no es el frontal del reveal. Es un primer plano tuyo, grabado adentro, en tu cuarto claro, a distancia de brazo. El frontal del video de referencia es un plano entero tuyo, de cuerpo completo, en un campo, con un dron por encima mirándote a unos 40 grados. Son dos lentes, dos distancias, dos ambientes y dos alturas de cámara distintas. Si cortas de un top-down en un campo a ese primer plano indoor, el cerebro de quien lo ve registra que son dos videos, no dos ángulos del mismo. Es la misma disonancia de las fotos, pero ahora sumada al salto de ambiente: dormitorio a pradera.

Y hay un error más de fondo, más importante que ese. **El video de referencia no usa cuatro ángulos.** Usa un solo eje. El dron arranca al frente tuyo, elevado, y sube y se aleja en línea recta mientras la multitud crece. Frontal bajo, frontal medio más alto, frontal altísimo tipo eagle. Nunca hay un side. Nunca hay un cenital tuyo. La magia de ese formato es que es la MISMA toma escalando, no un carrusel de perspectivas. Si le metes un lateral y un picado cenital de tu cuerpo, rompes la ilusión de que es un solo movimiento continuo. Tu plan de "frontal, side, top down, eagle" trabaja en contra del formato que quieres copiar.

Ahora, tu instinto del top-down con fondo 1 no está del todo mal, está mal ubicado. Un cenital de ti parada muestra la coronilla y te achata el cuerpo en un borrón, y además el fondo 1 es una textura de pasto sin horizonte, no un escenario donde una persona parada tenga relación creíble con el piso. Pero ese fondo 1 sí sirve, como el ÚLTIMO beat: el plano de dios sobre la multitud gigante, donde tú ya eres un punto invisible. No es un retrato tuyo, es el clímax de la muchedumbre vista desde arriba. Ahí sí, que lo imagine la IA.

Así queda la arquitectura correcta:

- **Beat 0, hook (0 a 4s):** 1-1.mp4 tal cual, indoor, tu voz, música por debajo. Se queda adentro y no se toca. En "mira esto" hay un corte duro montado al beat. Aceptamos el salto de ambiente porque es un corte decisivo, no un pull-back. Si algún día lo quieres cinematográfico de verdad, regrabas el hook en el campo para que el plano pueda abrirse hacia la multitud sin cortar. Por ahora, corte seco.
- **Beat 1 (reveal empieza):** frontal elevado, cuerpo completo tuyo en el campo, multitud chica detrás. Fondo 4.
- **Beat 2:** mismo eje, cámara más alta, multitud más grande. Fondo 3.
- **Beat 3:** eagle, multitud hasta el horizonte. Fondo 1, cenital, tú como punto.
- **Cierre:** el número real, cuántas familias, cuánto se levantó, y el CTA.

La parte honesta que nadie te va a decir: lo difícil de este video no eres tú, es la multitud. Mantenerte idéntica a ti misma en los tres planos del campo, y que la multitud escale de forma creíble entre plano y plano, es donde esto se cae. Por eso los tres planos del campo tienen que salir de UNA sola referencia tuya de cuerpo completo, no de tres fotos distintas del cuarto con outfits distintos. Si uso la img4 para el beat 1 y la img6 para el beat 3, en pantalla eres dos personas.

Dos caminos de producción:

- **Stills + movimiento en CapCut.** Genero 3 planos fijos, cada uno con más gente, y tú les metes push-in y crossfade para fingir el pull-up del dron. Más control sobre tu cara y sobre la multitud. Se ve como secuencia con movimiento, no como pull continuo. Para tu set de herramientas, es el camino.
- **Image-to-video.** Un modelo tipo Kling hace el movimiento de dron real, pero pierde control sobre tu parecido y sobre el realismo de la multitud. Más riesgo.

Recomiendo el primero. Empezamos por el ancla, que es el beat 1, porque fija tu likeness y la lógica de compositing de la que se derivan los otros dos.

Para eso necesito UNA foto tuya de cuerpo completo, frontal, para que sea la misma tú en toda la secuencia. La img4 es la mejor candidata: cuerpo entero, de frente, ángulo ligeramente elevado que ya cuadra con un dron frontal. Súbeme esa a Higgsfield junto con el fondo 4, y corro el primer plano ancla con la multitud chica detrás. Higgsfield no puede leer lo que subes al chat, así que te abro el widget.

Se me quedó el widget sin aprobar de tu lado, así que no se abrió. Cuando lo autorices, súbeme ahí la img4 y el fondo 4, y en cuanto me confirmes las dos subidas corro el plano ancla: tú de cuerpo completo, frontal elevado, con la multitud chica detrás. Ese es el que fija tu parecido para toda la secuencia, y una vez que se vea como tú, escalamos a los beats 2 y 3 sin volver a pelear con el likeness.

## 🧑 Adriana · 2026-07-03 01:18
Tengo pensado en usar Omni Video, que esa herramienta cambie mi entorno que opinas?

Yo diria que hay que generarlo por partes.

1. Yo sola. cerca de la camara hablando
2. yo frontal sola
3. yo frontal con 10 personas atras
4. yo frontal elevado 
5. yo frontal elevado con 100 personas atras
6. yo frontal MAS elevado 
7. yo frontal elevado con 1000 personas atras
8. yo frontal MAS  MAS elevado 
9. yo frontal elevado con 10000 personas atras

## 🤖 Claude · 2026-07-03 01:21
Cambiar el entorno es la parte fácil de este video, y es justo la parte que te va a hacer creer que ya lo resolviste cuando en realidad no tocaste el problema. El swap de fondo preserva el ángulo de cámara con el que grabaste. Si te grabas a la altura de los ojos y le pides a Omni que te ponga un campo detrás, sigues siendo una persona filmada a nivel de ojo parada sobre un campo. Tu cuerpo no adquiere el picado del dron. Y el picado del dron que sube es la columna vertebral de este formato, no un adorno. Así que "que la herramienta cambie mi entorno" resuelve el backdrop y deja intactos los dos problemas reales: la escalada de ángulo de cámara y la multitud que crece.

Aclaro qué es Omni antes de opinar, porque hay dos cosas con ese nombre y cambia la respuesta. Si hablas de Gemini Omni de Google, salió en el I/O de mayo 2026 y su promesa relevante no es el fondo, es que puede cambiar un fondo o transformar todo el escenario manteniendo el sujeto y la acción consistentes, y además cambiar el ángulo de cámara conservando el personaje entre ediciones encadenadas. Si hablas de la herramienta omni-video.com, su fuerte es el control de frame inicial y final para dirigir morphs y reveals con una referencia de personaje que fija tu identidad. Para tu caso, el swap de entorno es lo de menos en ambas. Lo que necesitas de cualquiera de las dos es re-generarte en un ángulo nuevo sin que dejes de ser tú, y meter gente que no existe. Eso es harina de otro costal técnico.

Ahora tu lista de 9. El instinto está bien encaminado y mejoró respecto a lo anterior: dejaste el side y el cenital, y estás pensando en un solo eje que sube, frontal a elevado a más elevado. Eso es correcto. Tres cosas que hay que corregir antes de generar nada.

**Uno. La consistencia es todo el juego, y 9 tomas son 9 oportunidades de que dejes de parecerte a ti.** Si cada shot se genera por su cuenta, en pantalla vas a ser tres mujeres distintas con el mismo outfit aproximado. La regla es una sola: fijas UNA referencia de personaje, una foto tuya de cuerpo completo con el outfit definitivo, y UN mundo, el mismo campo. Los 9 shots se derivan de esos dos anclas. Ninguna toma inventa su propia versión de ti. Ese es el motivo por el que la referencia funciona, es una sola toma continua, la misma persona, nunca hay chance de drift.

**Dos. Los pares vacío/lleno no son shots independientes, son un morph.** En la referencia la multitud no aparece en un corte, se materializa dentro del mismo plano. Tu shot 2 (frontal vacío) y tu shot 3 (frontal con 10) tienen que ser la misma posición de cámara y la misma tú, con la única diferencia de la gente. Si los generas por separado no van a coincidir y el efecto de "aparece la multitud" se muere, se ve como dos planos pegados. La forma correcta: cada tier es una sola generación con frame inicial vacío y frame final con multitud, y ahí es donde el control de start/end frame de Omni sí te sirve de verdad. De 9 shots independientes pasas a 1 hook más 3 morphs. Menos generaciones, menos drift.

**Tres. Tus beats vacíos ya no tienen función retórica, porque el hook hablado reemplazó la pregunta.** En la referencia el "only 100 followers?" sobre el campo vacío es la pregunta, y "100 PEOPLE" es la respuesta. Tú ya haces la pregunta una vez, hablando, en "cuando pienses que tu comunidad es demasiado pequeña". Entonces no necesitas repetir el beat vacío como pregunta en cada tier. El vacío solo sobrevive como frame inicial del morph, para que la gente aparezca. No como plano suelto que respira. Eso te aprieta el video y lo vuelve una escalada continua en vez de un stop-and-go.

El consejo táctico que te ahorra medio día: **genera primero la toma peor, no la fácil.** Todo el mundo empieza por el shot 1 y 2, le queda lindo, se emociona, y descubre a las tres horas que el frontal elevado con 10.000 personas es imposible en la herramienta que eligió. Genera de una el tier más alto con la multitud más grande. Si ninguna herramienta te lo saca creíble, este formato completo se cae y pivoteas antes de invertir. La multitud de 10 y de 100 te va a salir limpia. El realismo se empieza a desmoronar en 1.000 y colapsa en 10.000, porque mantenerte nítida al frente mientras diez mil humanos distintos se van al horizonte es exactamente lo que estos modelos hacen peor. La referencia probablemente lo resolvió con duplicación de multitud en VFX, no con un solo prompt.

Mi lectura corta. Omni sirve, pero no por lo que tú le estás pidiendo. No lo uses para "cambiar el entorno", úsalo para lo difícil: re-generarte en el ángulo elevado con la referencia de personaje puesta, y hacer el morph vacío a multitud por tier. Prueba eso en el tier de 1.000 antes de tocar nada más. Si pasa esa prueba, armamos los cuatro morphs y el hook. Si no pasa, te digo de una qué formato alterno cuadra con lo que sí se puede generar hoy.

¿Cuál de los dos Omni es el que tienes a mano, el de Google o el de omni-video punto com? Con eso te doy los prompts exactos por tier, con frame inicial, frame final y densidad de multitud.

## 🧑 Adriana · 2026-07-03 01:22
No, la regla es que cambie los videos que ya yo grabe, no que los imagine. Si el video o el dron no sube tanto no importa.

## 🤖 Claude · 2026-07-03 01:25
Tu regla es la correcta, y de paso mata el único clip que me mostraste. Las dos cosas son verdad al mismo tiempo, y hay que verlas juntas antes de seguir. Editar footage real en vez de alucinarte es la decisión sensata: te mantiene siendo tú, esquiva el cuerpo uncanny que sale cuando el modelo inventa ángulos que nunca filmó, y el swap de entorno es justo lo que estas herramientas hacen con fiabilidad. Hasta ahí, bien.

El problema es lo que un swap de entorno no hace: no reencuadra. Cambia los píxeles detrás de ti, no cambia el lente, ni la distancia, ni la altura de cámara. 1-1.mp4 es un primer plano tuyo hablando. Le puedes cambiar el cuarto por un campo, pero sigue siendo un primer plano: se ve tu torso y un campo detrás, no tu cuerpo entero chiquito con la multitud llenando la pradera. El reveal de la referencia vive entero en el encuadre ancho, y el encuadre ancho no se genera con un swap, se captura en cámara. Si le metes ese primer plano al mejor tool del mundo, te devuelve un primer plano con fondo nuevo, no un reveal.

Sobre "si el dron no sube tanto no importa": de acuerdo, pero eso tiene una consecuencia que hay que asumir. Si no vas a mover la cámara, la escalada no puede venir de una cámara que sube, porque no hay cámara que suba. Tiene que venir de otro lado, y hay dos palancas que respetan tu regla al pie de la letra. Una, densidad de multitud creciente sobre el mismo plano. Dos, un zoom-out digital en post que finge el pull-back. Las dos se aplican a UN solo clip real tuyo. La cámara queda clavada, y la ilusión de que se aleja la hace el zoom sobre el 4K, no un dron.

Entonces el footage que tienes que grabar es uno solo y específico: un plano ancho, cuerpo completo, cámara fija, a la altura que quieras. Súbete a una silla si quieres un picado suave, no necesitas dron. Contra pared lisa o cuarto despejado, con aire alrededor y sobre todo detrás de ti, para que quepan el campo y la gente. Ese clip es el lienzo de todo el video. Grábalo en luz suave y neutra, no bajo tu lámpara cálida, porque si tú estás naranja y el campo y la multitud están en luz de día, no pegan. Es el mismo problema de temperatura que te marqué con las fotos, pero ahora sobre video en movimiento, donde se nota más.

Con tu regla, el build queda así:

- **Hook.** 1-1.mp4 tal cual, corte duro en "mira esto". O regrabas el hook dentro del plano ancho, hablando de cuerpo entero, para que hook y reveal sean el mismo mundo y no haya salto de ambiente. Es más trabajo pero es la versión sin costura.
- **Reveal.** Tomas el plano ancho real, Omni le cambia el entorno a campo y le agrega multitud. Generas 2 o 3 versiones del MISMO plano con más gente cada vez.
- **Edit.** Secuencias las versiones con un zoom-out lento y crossfade entre ellas. La gente crece, la cámara "se aleja", y tú siempre real y consistente porque debajo es literalmente el mismo clip.
- **Cierre.** El número real, cuántas familias, cuánto se levantó, y el CTA.

Para esta regla, Gemini Omni cuadra mejor que generar stills en Higgsfield, porque su trabajo declarado es justo ese: transformar video que ya existe cambiando el escenario y metiendo personajes nuevos sin perder al sujeto ni la dirección de la luz. Google la lanzó en mayo 2026 y una de sus capacidades es modificar un fondo o transformar el escenario completo manteniendo el sujeto y la acción consistentes. Higgsfield lo dejas para las fotos del otro proyecto, que sí eran stills.

La parte que no te va a gustar pero es honesta: sin escalada de cámara real, esto deja de ser LA referencia y pasa a ser un primo cercano. El golpe de la referencia es que el número explota tres veces, y cada explosión sube la cámara. Con una o dos revelaciones de multitud sobre un plano fijo tienes un golpe, no tres. Para tu mensaje de comunidad puede bastar de sobra, porque lo que vende no es el espectáculo del dron, es el "mira cuántos somos de verdad" que salta de tú sola a tú rodeada. Un solo reveal limpio y real puede pegar más que tres tiers falsos que se ven de IA.

Antes de darte el prompt exacto de Omni necesito una cosa: además del primer plano hablando, ¿tienes ya algún plano ancho de cuerpo completo grabado, o ese hay que salir a grabarlo? De ahí depende si te escribo el prompt del swap sobre lo que tienes o la lista de captura de lo que falta.

## 🧑 Adriana · 2026-07-03 01:31
estos son los 4 angulos que tengo para que vean

## 🤖 Claude · 2026-07-03 01:34
Estos cuatro ángulos matan el formato de la referencia, y prefiero que lo sepas ahora y no después de pelear tres horas con Omni. Los cuatro están grabados a altura de teléfono. Angle 1 es un primer plano, angle 2 es frontal a la altura de tus ojos, angle 3 es frontal con un pelín de picado, y angle 4 es un lateral apenas elevado. Ninguno tiene la altura del dron, y la altura del dron no es un lujo estético en este formato, es lo único que hace que una multitud lea como multitud.

Te explico la física, porque de aquí sale toda la decisión. Una multitud detrás de ti a la altura de los ojos se apila y se ocluye: para la tercera o cuarta fila, las personas de atrás desaparecen tapadas por las de adelante. Entonces 100 personas y 10.000 personas producen exactamente la misma imagen, un muro con las 30 caras más cercanas y nada detrás. El tapiz de gente hasta el horizonte de la referencia solo existe porque el dron está a 40 metros mirando hacia abajo, y ese picado aplana la muchedumbre en un campo legible. Tú no tienes ese picado, así que la escalada numérica está muerta. Tu plan de 10 a 100 a 1.000 a 10.000 es un texto que tus imágenes no pueden respaldar, y un número que la imagen no sostiene es justo lo que hace que un video se sienta de IA barata.

Lo que sí tienes es el corazón del formato, que no es el número, es el salto de tú sola a tú rodeada. Eso sí se puede, y estos son tus ángulos ordenados por trabajo:

- **Angle 3 es el shot estrella.** Es el único con inclinación hacia abajo, y ese picado leve es el dron del pobre: te deja ver una segunda y tercera fila de gente en vez de solo el muro de adelante. Todo tu presupuesto de multitud va aquí. Este es el plano donde ocurre el reveal.
- **Angle 1 es el hook.** Primer plano, hablando, otro trabajo. No compite con el reveal, lo prepara.
- **Angle 2 es el beat íntimo.** A tu altura, de frente, es lo peor para multitud porque es puro muro, pero es lo mejor para el momento de tú sola antes de que aparezca la gente. Úsalo vacío o con poquísima gente.
- **Angle 4 es un cutaway de textura.** Un lateral con multitud es b-roll de ritmo, medio segundo, no un reveal. No le pidas más.

El build que respeta tu regla al pie de la letra, sin imaginar nada y sin que la cámara suba:

1. **Hook.** Angle 1, tu voz, "cuando pienses que tu comunidad es demasiado pequeña para hacer la diferencia, mira esto".
2. **Reveal, un solo plano.** Angle 3. Frame inicial: tú sola en el campo, vacío. Frame final: la multitud se materializa detrás de ti. La cámara no se mueve. El crecimiento viene de la densidad de gente que aparece, no de una cámara que sube. Ahí es donde el control de frame inicial y final de Omni sí trabaja de verdad.
3. **Sabor, opcional.** Un pestañeo de angle 4 lateral con gente, o angle 2 entre la multitud, para romper la monotonía del plano fijo.
4. **Cierre.** El número real, cuántas familias, cuánto se levantó, y el CTA.

Un reveal fuerte, máximo dos tiers de densidad. No cuatro. Alone a surrounded pega más que cuatro escalones falsos que se ven pegados.

Ahora los dos asesinos técnicos que viven en estos shots específicos, porque aquí es donde se cae el realismo. El primero es el contacto con el piso. Estás parada en alfombra, con chancletas, con sombra de alfombra bajo los pies. Cuando Omni cambie el cuarto por campo, tiene que reemplazar la alfombra por grama justo debajo de tus pies y proyectar una sombra de grama, o vas a flotar. Ese parche debajo de los pies es el tell número uno de este tipo de swap. El segundo es la temperatura de luz: tu cuerpo está bañado en luz cálida de interior, y si el campo entra en luz de día fría, no pegas. Elige un campo en luz dorada o de tarde, que es lo más cercano a como estás iluminada. Es el mismo problema que te marqué con las fotos, ahora sobre video, donde se nota más porque se mueve.

El movimiento que multiplica esto sin romper tu regla: el fondo del hook (angle 1) ya está desenfocado. Cámbiaselo a un campo también desenfocado. Es de bajísimo riesgo porque el bokeh perdona todo, y logra que el hook y el reveal vivan en el mismo mundo, así el corte en "mira esto" no salta de dormitorio a pradera. Hook y reveal se sienten un solo video.

Antes de armar nada, prueba lo peor primero: mete la multitud en angle 3 y mira si Omni te saca gente creíble que cuadre con tu luz. Google la lanzó pudiendo cambiar el escenario y agregar personajes nuevos manteniendo el sujeto y la luz consistentes, pero una multitud densa realista es de lo más difícil que existe hoy. Si esa prueba pasa, armamos el reveal completo. Si Omni solo te saca cinco maniquíes tiesos, bajamos de "multitud" a "un grupo que importa", que con angle 3 y buena luz todavía cuenta la misma historia sin mentir.

¿Los cuatro ángulos los tienes en video con la cámara fija en trípode, o grabados a pulso? De eso depende si el swap se compone estable o si hay que estabilizar antes, y cambia el prompt que te escribo para el reveal de angle 3.

## 🧑 Adriana · 2026-07-03 01:38
subire la foto de fondo y el video frontal con el angulo de 1.png
que le digo a higssfield? este sera el fondo y este es en algulo, que prompt le doy?

## 🤖 Claude · 2026-07-03 01:39
Este close-up es, de todos los shots que tienes, el único donde es casi imposible perder, y por una razón mecánica: el fondo original ya está destruido por el bokeh. Nadie va a ver detalle atrás de ti, solo manchas de color desenfocadas. Eso significa que solo hay dos formas de arruinarlo. Una, que Higgsfield te renderice el campo demasiado nítido y se note el recorte. Dos, que te enfríe el color y quedes cálida sobre un campo frío. Todo el prompt está construido para forzar desenfoque y clavar la temperatura cálida. Nada más importa en esta toma.

Antes del prompt, cómo subes las dos cosas: el video hablado (1.png) va como el clip fuente, el que se va a editar. area.png va como la imagen de referencia de fondo. No al revés. Si la herramienta te deja etiquetar cuál es cuál, el video es source, la foto es background reference.

El prompt, en inglés porque estos modelos obedecen mejor en inglés, listo para copiar:

```
Replace only the background of this video. Keep the woman 100% unchanged: same face, freckles, gold wire-frame glasses, same expression, same mouth movement and speech, yellow fuzzy knit cardigan, dark red beaded necklace, the small black wireless microphone in her hand, her hand and nails, and every strand of hair including the loose flyaways at her hairline. Do not regenerate or relight the subject.

New background, based on the provided field image: an open golden-hour meadow of green rolling hills at sunset, warm amber light near the horizon, soft lavender sky above. Place her standing in the field at eye level, so the warm sky sits behind her head and the horizon sits behind her shoulders.

Keep the background heavily out of focus: creamy shallow-depth-of-field bokeh, 50mm portrait look, matching the blur of the original clip so the field reads as atmosphere, not a pasted photo. Match the color temperature to her existing warm indoor lighting, keep the warm rim light on the edges of her hair. Photoreal, no added people, no objects, no text. Vertical 9:16, preserve the original framing and her position in frame.
```

Si sale mal, no reescribas todo, mueve una sola palanca a la vez:

- Fondo se ve pegado o muy definido: agrega al final "extreme background blur, f/1.8, defocused, no sharp horizon".
- Te enfría la piel o te pone grisácea: agrega "preserve her original warm skin tone, do not cool the image".
- Te toca la cara o rompe el lip-sync: agrega "lock the face and lip motion, do not alter identity or mouth".
- Te mete luz rara encima: agrega "do not relight the subject, keep original light on her".

El path de la foto no lo vas a ver en este plano, y está bien que así sea. En un close-up ese camino se disuelve en el desenfoque, y area.png aquí solo cumple una función: darle al fondo el color y la luz dorada correctos para que este hook y el reveal vivan en el mismo mundo. El path lo reservas para cuando hagas angle 3, que es plano ancho y ahí sí se ve el piso.

Una nota honesta de herramienta, sin desviarte: un swap de fondo sobre un video hablado conservando el lip-sync es exactamente para lo que Gemini Omni está construido. Higgsfield te lo puede sacar, pero si te deforma la cara o te descuadra la boca, no pelees con el prompt, ese es el aviso de mover esta toma específica a Omni y dejar Higgsfield para las que sean image-to-video.

Y el recordatorio estratégico, porque esta toma es la fácil: cuando te salga, no cantes victoria. Este bokeh perdona todo. La prueba real del formato es angle 3 con la multitud, ahí es donde se decide si el video existe o no. Saca el hook, y de una pasamos a testear el reveal.

## 🧑 Adriana · 2026-07-03 01:43
omni flash genera en 720 px que otra opcion de mejor resolucion podria haber?

## 🤖 Claude · 2026-07-03 01:45
El 720p de Omni Flash es real y es el techo del modelo crudo de Google, sin salida nativa a 1080p ni 4K en la API. 720p es la resolución nativa de salida, sin opción de 1080p ni 4K. Pero antes de que salgas a cazar un modelo de más resolución, para el shot que estás haciendo ahorita la resolución es la pregunta equivocada, porque no deberías estar regenerando tu cara para empezar. Ese close-up con el fondo en bokeh no necesita un modelo generativo. Necesita un recorte.

Te lo desgloso por capas, de la mejor resolución a la peor.

**Capa 1. No generes, recorta y compón. Es tu resolución máxima real.**
El plano hablado es un primer plano tuyo sobre un fondo ya destruido por el desenfoque. Si en vez de pedirle a un modelo que te "re-imagine" sobre un campo, haces un matte (recortas tu silueta) y metes area.png detrás, tu cara nunca se regenera. Se queda en el 4K nativo del clip original. El fondo es una foto fija, también a resolución completa. El techo de 720p desaparece porque ningún píxel tuyo pasa por un modelo. Tienes DaVinci Resolve: Magic Mask hace ese recorte sobre video. El único punto donde esto se cae son tus pelitos sueltos en la frente, que es lo más difícil de rotoscopiar. Y justo ahí el bokeh te salva, porque un borde de pelo imperfecto se funde en el desenfoque del campo y nadie lo nota. Fondo estático, sí, pero en un close-up con ese nivel de blur, la grama no necesita moverse. Este es el camino honesto para "mejor resolución": es 4K real, tu lip-sync real, tu cara intacta, y no gastas un crédito.

**Capa 2. Si insistes en swap generativo, sube de modelo, no de wrapper.**
Ojo con la trampa: plataformas como Higgsfield o Artta te ofrecen "Omni en 1080p y 4K", pero eso es un upscale, no detalle nuevo. Genera nativo en 720p, el 1080p es un upscale gratis, y el 4K cuesta el equivalente a una generación completa. Si de verdad quieres resolución generada, estos son los que tienen 4K de verdad:

- Seedance 2.0 de ByteDance, en 4K nativo y primero en el arena de video. Seedance 2.0, ahora en 4K nativo.
- Veo 3.1, hasta 4K, pero es de generación, no de edición conversacional. Google mismo posiciona Omni para el borrador y Veo para el render final en alta. Veo maneja generación de alta calidad hasta 4K; la idea es hacer el borrador en Omni y pasar el mejor candidato a Veo.
- Kling 3.0, 1080p, y es el más fuerte con sujetos humanos y física. Kling 3.0, competidor fuerte en 1080p y clips de 15 segundos. Como tu sujeto eres tú, humana, esto importa.

El tradeoff que nadie te dice: el trabajo específico que quieres, editar el fondo de un video hablado sin romper el lip-sync, es justo el nicho de Omni, no de los modelos 4K. Veo y Seedance son más generar que editar. Entonces subir de resolución te cuesta perder la capacidad de conservar tu boca hablando. No es gratis.

**Capa 3. Genera en 720p y sube con un upscaler dedicado.**
Sacas el swap donde te preserve el lip-sync, y luego pasas el clip por un upscaler de video, Topaz, que en Higgsfield lo tienes a 1080p, 2K o 4K. El upscale recupera píxeles, no detalle: un 720p a 4K te queda suavecito pero usable. Y tienes un límite de tiempo que juega a tu favor: el lip-sync de Omni aguanta bien 6 o 7 segundos antes de desviarse. El lip sync se mantiene estable 6 a 7 segundos antes de derivar. Tu hook dura como 4, así que estás dentro del margen. Cuando tengas el clip, te corro el upscale.

**Por qué 720p es un problema aquí y no siempre.**
Para TikTok o Reels, 720p vertical pasa, las plataformas comprimen igual. El problema real no es que 720p se vea mal en abstracto, es que vas a pegar un hook de 720p al lado de un reveal en 4K, y esa mezcla de resoluciones es lo que lee como video roto. La consistencia de resolución entre shots pesa más que la nitidez absoluta de cualquiera.

**Mi recomendación, por shot:**

- Hook close-up con bokeh: matte y composición en DaVinci. 4K nativo, cero generación. Aquí la pregunta de 720p ni existe.
- Reveal ancho con multitud: ahí sí es inevitable generar, porque estás agregando gente que no existe. Usa Kling 3.0 o Seedance por el sujeto humano y la multitud, a la mayor resolución que aguante, y sube a 4K con Topaz para igualar el hook.

Antes de escribirte cualquier prompt nuevo: ¿tienes DaVinci a mano para probar el matte del hook primero? Si el recorte de pelo te sale limpio con Magic Mask, te ahorras el generativo completo en ese shot y arrancamos el reveal, que es donde sí se decide el video.

## 🧑 Adriana · 2026-07-03 01:48
higgsfield cambio todo lo que digo en lugar de dejarme a mi normal y solo cambiar el fondo 🤡

## 🤖 Claude · 2026-07-03 01:48
Ese emoji de payaso te lo estás poniendo por algo que no es tu culpa, es una restricción de diseño del modelo. Higgsfield corrió tu clip por un modelo de generación de video, no por uno de edición. Son dos categorías distintas de herramienta, y la que usaste no tiene forma de "dejarte normal", porque su trabajo es reconstruir cada frame desde cero. Cuando un modelo generativo re-renderiza el fondo, re-renderiza todo el frame en el mismo pase, tú incluida. No hay una capa que separe "sujeto" de "fondo" que él pueda respetar. Vuelve a dibujar la imagen completa guiándose por la tuya, y en ese redibujado te cambia la cara, la boca, el color, lo que sea. El prompt puede decir "no toques al sujeto" mil veces y no importa, porque a nivel de arquitectura no existe un sujeto intocable, existe un lienzo que se repinta entero.

Lo que tú querías es lo contrario: que tu grabación real quede congelada y que solo los píxeles detrás de ti se reemplacen. Eso no es generación, es composición. Y ninguna cantidad de prompt engineering convierte un modelo generativo en un compositor. Estás peleando con la herramienta equivocada, no con el prompt.

Hay tres formas de lograr lo que quieres, ordenadas de mejor a peor para tu caso específico, que es un primer plano hablando con fondo en bokeh.

**Uno. Composición por matte. Cero riesgo de que te cambien.**
Aquí tu video real es la capa de arriba y es sagrada, nunca se regenera. Recortas tu silueta, metes el campo detrás, y tú sigues siendo tú al 100% porque literalmente es tu clip original con un hueco detrás. Tu cara, tu boca, tu lip-sync, tu 4K, intactos, porque el modelo no te toca. Solo rellena lo de atrás. Tienes DaVinci Resolve: Magic Mask hace exactamente esto sobre video. También lo hace CapCut con su recorte automático, aunque más burdo. Este es el camino correcto para este shot, y de paso te resuelve el problema de resolución que tenías, porque nada tuyo pasa por un modelo de 720p.

**Dos. Un modelo de edición de video, no de generación.**
Si insistes en hacerlo con IA y no con recorte manual, la categoría que necesitas es "video-to-video edit" que preserva al sujeto, no "text-to-video" ni "image-to-video". Gemini Omni está construido específicamente para eso, cambiar un fondo conservando al sujeto y su movimiento. Pero ya viste el techo de 720p, y aún así, incluso Omni te puede desviar la cara si el clip pasa de seis o siete segundos, porque ahí el lip-sync empieza a derivar. Si vas por aquí, clip corto y una sola instrucción: cambiar fondo, nada más.

**Tres. Remove background y compón, todo dentro de Higgsfield.**
Higgsfield tiene una función de quitar fondo sobre video que te devuelve tu clip con el fondo transparente, sin tocarte a ti. Eso te deja el sujeto real recortado, y encima le pones area.png. Es la versión de la opción uno pero sin salir de la herramienta que ya estás usando. La debilidad es la misma de siempre: tus pelitos sueltos en la frente. El bokeh del campo los perdona, así que para este shot aguanta.

Lo que NO vuelvas a hacer: darle tu video a un generador de video con un prompt de "no me cambies". Ya sabes cómo termina. El generador no desobedeció, hizo justo lo único que sabe hacer.

Una nota de diagnóstico para que no pierdas más créditos: la forma de saber si una herramienta te va a respetar es preguntar qué produce. Si produce un video nuevo, te va a re-dibujar. Si produce una máscara, un recorte, o una capa transparente, te respeta. Composición te respeta. Generación te reinterpreta. Esa es toda la regla.

Dime cuál de las tres quieres y te llevo. Si vas por composición en DaVinci, te doy el paso a paso del Magic Mask con el manejo de pelo. Si vas por remove background dentro de Higgsfield, te abro la función y te digo qué subir. ¿Cuál agarras?

## 🧑 Adriana · 2026-07-03 02:09
peor noe nteidno todo el mundo hace eso ppr que no me slae a mi halgo esta shacinedo ,al, avergua

## 🤖 Claude · 2026-07-03 02:09
Todo el mundo NO está haciendo lo que tú intentaste hacer, y ahí está el malentendido que te tiene frustrada. Los videos que ves con la persona real intacta y solo el fondo cambiado casi nunca se hicieron re-generando a la persona con IA. Se hicieron con una de tres técnicas que preservan el sujeto por diseño, y ninguna es "meter mi video en un generador y pedirle que no me cambie". Lo que a ti no te sale es específicamente eso, y no te sale porque es lo único que la herramienta que usaste no puede hacer. No estás haciendo algo mal por incapacidad. Elegiste la categoría equivocada de herramienta para la tarea.

Déjame separar las dos cosas que estás mezclando, porque de ahí sale toda la confusión.

Hay dos familias de herramientas de video con IA, y se ven parecidas desde afuera pero hacen cosas opuestas por dentro:

Generación de video. Le das un prompt o una imagen, y construye un video nuevo desde cero, frame por frame. Higgsfield, en el modo que usaste, es esto. Cuando le metes tu clip y le pides cambiar el fondo, no tiene forma de "conservarte", porque su mecánica es repintar la imagen completa. Te repinta a ti también. El prompt de "déjame normal" es aire para él. No existe un botón interno que diga "esta parte no la toques".

Edición o composición de video. Aquí tu grabación real es la base y se queda congelada. La herramienta solo reemplaza los píxeles de atrás. Tu cara nunca se recalcula. Esta es la familia que usa "todo el mundo" para los videos que tú tienes en mente. No es magia de IA generativa, es recorte y capas, la misma lógica del croma de toda la vida pero automática.

Lo que pasó fue simple: mandaste tu tarea de composición a una herramienta de generación. Es como pedirle a una impresora que te escanee. La máquina no está rota, le pediste lo que no hace.

Cómo lo arreglas, de lo más fácil y seguro a lo más técnico:

Opción 1, la que yo haría con tu shot. CapCut, que ya tienes. Metes tu video, le aplicas "Remove background" o "Auto cutout", eso te recorta y te deja a ti sola sin fondo. Debajo pones la foto del campo como una capa nueva. Listo. Tú quedas exactamente como te grabaste, porque CapCut no te re-dibuja, solo te recorta y pone algo detrás. Cero riesgo de que te cambie la cara. Es literalmente imposible que te cambie, porque no te está generando.

Opción 2, más limpia de bordes. DaVinci Resolve, que también tienes. La función se llama Magic Mask. Pintas encima de ti una vez, el programa te sigue por todo el clip y te separa del fondo. Debajo va el campo. Mismo principio, mejor calidad en el pelo.

Opción 3, dentro de Higgsfield sin cambiar de app. Higgsfield tiene "Remove background" para video, que es distinto del modo generativo que usaste. Ese sí te respeta, porque te devuelve tu clip recortado con fondo transparente, sin tocarte. Encima le pones el campo. Es la opción 1 pero sin salir de donde ya estás.

La regla que te va a ahorrar créditos y frustración de ahora en adelante, y quiero que te quedes con esta más que con cualquier otra cosa: antes de mandar tu video a cualquier herramienta, pregúntate qué te va a devolver. Si te devuelve un video nuevo, te va a re-dibujar entera. Si te devuelve un recorte, una máscara o una capa con fondo transparente, te respeta. Recorte te respeta. Generación te reinterpreta. Cuando el resultado te sale "cambiada", casi siempre es que usaste generación donde necesitabas recorte.

Para arrancar ya y que veas que sí sale: abre CapCut, sube el clip del hook, busca "Remove background" en los efectos de video, y ponme abajo la foto del campo. Eso te va a dar en dos minutos lo que llevas rato peleando. ¿Lo intentas por ahí y me dices qué te sale, o prefieres que te guíe con el Magic Mask de DaVinci que te deja mejor el pelo?

## 🧑 Adriana · 2026-07-03 02:23
when i copy and paste this prompt in google flow :

"Replace only the background of this video. Keep the woman 100% unchanged: same face, freckles, gold wire-frame glasses, same expression, same mouth movement and speech, yellow fuzzy knit cardigan, dark red beaded necklace, the small black wireless microphone in her hand, her hand and nails, and every strand of hair including the loose flyaways at her hairline. Do not regenerate or relight the subject.
New background, based on the provided field image: an open golden-hour meadow of green rolling hills at sunset, warm amber light near the horizon, soft lavender sky above. Place her standing in the field at eye level, so the warm sky sits behind her head and the horizon sits behind her shoulders.
Keep the background heavily out of focus: creamy shallow-depth-of-field bokeh, 50mm portrait look, matching the blur of the original clip so the field reads as atmosphere, not a pasted photo. Match the color temperature to her existing warm indoor lighting, keep the warm rim light on the edges of her hair. Photoreal, no added people, no objects, no text. Vertical 9:16, preserve the original framing and her position in frame."


it says: "Se debe formular una peitcion"

## 🤖 Claude · 2026-07-03 02:24
Ese error no es un rechazo de contenido, es un rechazo de sintaxis. Google Flow te está diciendo, con esas mismas palabras, que lo que le pegaste no está formulado como una petición que él sepa ejecutar. Y tiene razón desde su lógica, aunque suene absurda. Tu prompt está escrito como una orden de edición dirigida a un compositor, alguien que ya tiene tu video abierto en una capa y solo va a tocar el fondo. Flow no es eso. Flow genera. Cuando le dices "reemplaza solo el fondo de este video" y "no regeneres al sujeto", le estás dando una instrucción negativa sobre una operación que él no realiza, y el modelo se queda sin una acción positiva que ejecutar. No sabe qué construir, porque tú le dijiste todo lo que NO haga y casi nada de lo que sí haga desde cero. De ahí el "se debe formular una petición". Le falta el verbo que él entiende: generar, no preservar.

Hay dos capas en tu problema, y conviene separarlas antes de tocar el texto.

La primera es que seguimos empujando la tarea equivocada a la herramienta equivocada. Flow, igual que el Higgsfield generativo que te cambió la cara, repinta el frame completo. No existe dentro de él un "solo el fondo". Si le das tu clip, te va a reinterpretar entera, y volvemos al payaso. Que el prompt no corra no es tu enemigo hoy, es tu aliado, porque te está frenando antes de gastar la generación que te iba a devolver otra versión cambiada de ti.

La segunda es más de fondo: hay una diferencia entre un prompt que edita y un prompt que genera, y tú escribiste uno de edición. Un prompt de edición dice "toma esto que ya existe y modifica esta parte". Un prompt de generación dice "construye esto que no existe, con estas características". Flow solo entiende el segundo. Un prompt de generación no lleva la palabra "reemplaza" ni "no toques", lleva una descripción afirmativa de la escena completa que quieres que nazca.

Te lo desgloso en las dos rutas reales que tienes, porque insistir en Flow con este texto no te va a llevar a ningún lado.

Ruta A, la que de verdad te da lo que quieres: no uses Flow para este shot. Este plano es un primer plano tuyo hablando con fondo desenfocado. Eso se resuelve con recorte y capa, no con generación. En CapCut subes tu clip, le das "Remove background", y debajo pones la foto del campo. Tú quedas idéntica porque no te genera, te recorta. En DaVinci es Magic Mask y el pelo te queda mejor. Es la misma conclusión de antes, y sigue siendo la respuesta correcta. Flow no debería tocar este shot.

Ruta B, si de verdad quieres o necesitas que Flow te lo haga, tienes que hablarle en su idioma, que es generación afirmativa. Eso significa aceptar un riesgo: Flow te va a re-generar, así que no esperes que sea tu grabación exacta. Va a ser una versión tuya construida, parecida pero nueva. Con esa advertencia por delante, el prompt deja de ser una orden de edición y pasa a ser una descripción de escena. Algo así:

"A realistic vertical 9:16 video of a young woman with light-brown hair in a low ponytail with loose flyaways, gold wire-frame glasses, a soft yellow fuzzy knit cardigan and a dark red beaded necklace, holding a small black wireless microphone near her chin, speaking directly to camera in a close-up portrait shot. She stands in an open golden-hour meadow of green rolling hills at sunset, warm amber light near the horizon, soft lavender sky. Shallow depth of field, creamy bokeh background, 50mm portrait look, warm rim light on her hair, photoreal, natural warm skin tones. No text, no other people."

Fíjate en la diferencia estructural, porque es la lección: no hay un solo "no cambies", no hay un "reemplaza", no hay "el sujeto original". Todo está en positivo, describiendo a una persona y una escena que Flow va a construir de cero. Por eso sí lo va a aceptar como petición. Pero de nuevo, eso te devuelve una mujer generada, no tú. Para un hook donde la gente te reconoce, eso es un downgrade, y por eso la Ruta A le gana.

La regla que te llevas de este error, y que aplica a Flow, a Higgsfield generativo y a cualquier modelo de generación que toques de aquí en adelante: si tu prompt contiene las palabras "solo", "reemplaza", "no cambies" o "el original", estás escribiendo una instrucción de edición, y un generador la va a rechazar o la va a ignorar. Los generadores solo aceptan descripciones afirmativas de algo que va a nacer completo. Cuando quieras preservarte a ti, no hay prompt que valga, hay que salir de la generación y entrar en el recorte.

Mi recomendación no se movió ni un milímetro con este error, al contrario, se reforzó: cierra Flow para este shot y hazlo en CapCut o DaVinci. Flow resérvalo para lo que sí es generación pura, que en tu proyecto es el reveal con la multitud, donde de todos modos vas a construir gente que no existe y ahí la generación es la herramienta correcta.

¿Quieres que te dé el paso a paso exacto del "Remove background" en CapCut para que salgas de esto en dos minutos, o prefieres el de Magic Mask en DaVinci que te deja mejor los pelitos?

## 🧑 Adriana · 2026-07-03 02:56
higgsfield computer me geenro este prompt:

"@source: Original selfie-style clip — a young adult woman with brown hair, gold-rimmed glasses, a yellow sweater and a red beaded necklace, holding a small microphone, speaking directly to camera with a serious, earnest expression. Preserve her identity, face, wardrobe, hairstyle, microphone, performance, close-up wide-angle framing and stationary eye-level camera exactly; replace only the environment behind her — remove the indoor white wall and doorway and place her in the open golden-hour meadow of rolling green hills. @environment:  — open golden-hour meadow of rolling green hills at sunset, warm amber light near the horizon, soft lavender sky above. Environment and light reference only; she stands in the field at eye level so the warm horizon sits behind her shoulders and the lavender sky behind her head.  Photoreal. 9:16. 4s. Warm golden-hour cinematic grade. SFX and source dialogue only.  Locked close-up, same wide-angle lens and framing as the source, camera stationary at eye level. She continues speaking directly to camera with the same serious performance and mic-in-hand gesture, saying "Cuando pienses que tu comunidad es demasiado pequeña para hacer la diferencia... mira esto." The indoor wall and doorway are fully replaced by the open meadow: rolling green hills recede into a soft lavender sky, the horizon glowing amber directly behind her shoulders. Relight the whole frame to match the scene — warm, low, directional sunset key light from screen-right catching her hair and glasses rim, soft warm bounce filling her face, a faint golden haze softening the hills behind her, natural depth of field keeping her sharp against a gently defocused horizon. Face, identity, wardrobe and performance unchanged; only the environment and light around her are new.  SFX and source dialogue only: a light breeze rustling distant grass, faint ambient birdsong far off, her own voice delivering the line clearly with no added music."

esto garantiza que no cambiaran mi voz? usando el /seedance-footage-vfx

## 🤖 Claude · 2026-07-03 02:57
Voy a verificar cómo maneja el audio Seedance 2.0 antes de responderte, porque tu pregunta es sobre garantías y no quiero darte una suposición.

Ya con los datos en la mano, la respuesta corta es no. Ese prompt no garantiza nada sobre tu voz, y de hecho está construido sobre una contradicción que casi asegura que te la toquen. Te explico exactamente por qué, porque aquí hay dos errores encadenados y conviene verlos separados.

El primero es de categoría, el mismo de siempre. Seedance 2.0 es un modelo de generación, no de composición. Genera audio y video juntos en un solo pase, con una arquitectura que produce diálogo, ambiente y música sincronizados desde el inicio. Eso significa que el audio no es tu pista original respetada, es audio nuevo que el modelo fabrica mientras construye la imagen. Cuando pones en el prompt "source dialogue only", no le estás dando una garantía, le estás dando una preferencia que el modelo puede honrar o no. Su forma de "usar tu diálogo" es leer las palabras que escribiste entre comillas y sintetizar una voz que las diga, infiriendo el timbre a partir de la descripción del personaje. No es tu grabación pasando intacta. Es una voz reconstruida a partir de "young adult woman". Puede sonar parecida, puede sonar como otra persona, y a través de generaciones separadas se le va el acento. Nada de eso lo fija una línea de prompt.

El segundo error vive dentro del propio prompt, y es una orden imposible. El texto dice dos cosas que no pueden coexistir. Dice "preserva su cara, identidad y performance exactamente", y en el mismo párrafo dice "relight the whole frame", reiluminar todo el cuadro con luz de atardecer desde la derecha. No puedes reiluminar una cara sin re-renderizar esa cara. La luz sobre tu piel son píxeles, y para cambiarlos hay que generarlos de nuevo. Entonces el modelo recibe "no la toques" y "cámbiale la luz de la cara" al mismo tiempo, y resuelve la contradicción de la única forma que sabe: te regenera. Ese es el mecanismo exacto por el que Higgsfield ya te cambió una vez. Este prompt, por más detallado y bonito que se vea, le está pidiendo lo mismo con más palabras.

Hay un matiz que sí importa a tu favor, y es la única puerta real que te queda dentro de Seedance. Se puede apagar el audio nativo. El flujo documentado es: generas el video en silencio, muteas el diálogo de IA, y encima le pones tu voz grabada. Varias fuentes lo describen como el patrón correcto cuando la identidad de voz es un activo fijo, que es justo tu caso: tu voz es tu marca, no un accesorio intercambiable. Si generas con el audio apagado, tu voz no corre ningún riesgo porque el modelo nunca la genera. Pero fíjate en lo que ganas y lo que pierdes. Ganas tu voz intacta, porque la pegas tú después. Pierdes la sincronía, porque el modelo te va a regenerar la cara y la boca, y esa boca generada no va a cuadrar con tu audio real. Terminas con tu voz verdadera encima de una boca falsa que no le coincide. Cambiaste el problema de "me cambian la voz" por el problema de "mi boca no cuadra con mi voz".

Te ordeno las rutas por lo que realmente garantizan, que es la pregunta que hiciste.

**Garantía total de voz y cara: no generes. Composición.** Tu clip real es la capa de arriba, congelada, con su audio original pegado al pixel. Recortas tu silueta, metes el campo detrás. Tu voz no se toca porque nadie la procesa, es literalmente tu archivo. Tu boca cuadra porque es tu boca real. CapCut con remove background, o DaVinci con Magic Mask. Esto es lo único en toda la conversación que te da la palabra "garantiza" con honestidad. Ninguna otra opción lo hace.

**Garantía de voz pero no de sincronía: Seedance con audio apagado más tu voz en post.** Sirve si el shot necesita algo que la composición no puede dar, movimiento en el fondo, integración de luz. Para tu close-up con bokeh no lo necesita, así que aquí es un downgrade.

**Cero garantía: Seedance con audio nativo encendido, que es lo que ese prompt hace.** Te sintetiza una voz, te reilumina la cara, te regenera. Es la ruta que te trajo hasta acá quejándote.

La regla que quiero que te lleves de este intento fallido, porque es la que te va a filtrar cualquier prompt que te genere una IA de aquí en adelante: si el prompt contiene la palabra "relight", ya perdiste la cara, sin importar cuántas veces diga "preserve identity" en la misma frase. Reiluminar es regenerar. Y si el modelo genera audio en el mismo pase, tu voz es una preferencia, no una garantía, sin importar que escribas "source dialogue only". Las garantías no viven en el prompt. Viven en la arquitectura de la herramienta. Composición te garantiza. Generación te promete y a veces cumple.

Mi recomendación no se movió, se endureció con cada intento: este shot específico, el hook hablado con fondo desenfocado, no toca un modelo generativo. Sale en CapCut o DaVinci en dos minutos, con tu voz y tu cara intactas por diseño, no por suerte. Guarda Seedance y el skill de VFX para el reveal con la multitud, que es donde de verdad vas a generar gente que no existe y ahí la generación es la herramienta correcta, no la equivocada.

¿Te doy el paso a paso de CapCut para cerrar el hook hoy, o quieres que montemos el prompt de Seedance bien hecho para el reveal, que es el único lugar de tu proyecto donde ese skill tiene sentido?

## 🧑 Adriana · 2026-07-03 03:10
regenera el prompt entonces, se dice que el skill cumple con:
"Seedance Footage VFX
Write, improve, or rewrite Seedance 2.0 prompts that TRANSFORM footage the user already has (video-to-video), rather than building a scene from scratch. Use whenever a real clip is the starting point and they want a Seedance prompt to: add a VFX element (set a head or hair on fire, transform a hand, make a limb invisible), swap the environment around a preserved subject (clouds, lava, a neon city), drop a giant photoreal creature onto a landmark, relight or regrade so the subject and added elements look like one shot, sync a crash zoom or push-in to a spoken line or timecode, or generate a matching transformed start frame to animate from. Also use when they paste such a prompt and ask to change its lighting, timing, creature, or runtime. Trigger even if they just say "make a Seedance prompt for this video" with a clip attached. This is the video-to-video specialization; for a brand-new scene from image references with no source clip to preserve, the video-generation skill applies instead."

## 🤖 Claude · 2026-07-03 03:12
Tienes razón en un punto y me toca recalibrar: este es exactamente el caso de uso del skill, y la distinción que importa es una que yo estaba aplanando. Video-to-video no es lo mismo que el prompt que te dio Higgsfield Computer. Ese prompt, aunque decía "preserve identity", estaba escrito como descripción de escena, más cerca de text-to-video, y encima traía la instrucción que el propio skill marca como la de mayor riesgo: "relight the whole frame". El skill es explícito. Reiluminar todo el cuadro, sujeto incluido, es el fork de alto riesgo para la cara, y ofrece el otro fork como el de menor riesgo de identidad: preservar la luz del sujeto y graduar solo los elementos nuevos. O sea, mi advertencia sobre el relight no estaba equivocada, estaba incompleta, porque el skill sí resuelve el env-swap con sujeto preservado, siempre que uses el fork correcto. El prompt anterior usaba el malo.

Y tienes un golpe de suerte que hace todo esto viable. El skill dice que los mundos de luz de día cálida y direccional son más seguros para la identidad que la noche o el neón, porque esos obligan a un relight completo. Tu target es golden hour, cálido. Tu grabación es tungsteno de interior, también cálido. Las dos temperaturas ya están cerca, así que no necesitas reiluminarte para pegar en el campo. Puedes conservar tu luz y solo integrarte con un rebote sutil. Si tu fondo fuera azul frío o neón, no tendrías esta salida. La escogencia del atardecer, que veníamos arrastrando desde el tema de la temperatura, es justo lo que te habilita el fork seguro.

Antes del prompt, el punto honesto sobre tu voz, que es lo que preguntaste. El skill usa "SFX and source dialogue only" como el mecanismo para que sobreviva tu pista hablada, y así lo dejé en el prompt. Pero a nivel del modelo, Seedance genera audio en el mismo pase que el video, así que "source dialogue only" es una preferencia hacia la que sintetiza, no un passthrough garantizado de tu archivo de voz. La red de seguridad es simple y no depende del prompt: si la voz que te devuelve suena distinta aunque sea un poco, muteas el audio generado y le pegas encima el audio de tu clip original. Como es video-to-video, el modelo preserva el timing de tu boca, así que tu voz real vuelve a sincronizar. Eso sí te garantiza la voz, con o sin la cooperación del modelo.

El prompt, regenerado con el skill, fork de luz preservada, en inglés y en texto plano para copiar tal cual:

Hook · env-swap · golden-hour meadow, subject light preserved

@source: Original selfie-style vertical clip, ~4s. A young woman in a soft yellow knit cardigan and a dark red beaded necklace, gold wire-frame glasses, hair in a loose low style with flyaways at the hairline, holding a small black wireless microphone near her chin, speaking directly to camera in a locked eye-level close-up under warm indoor light. Preserve her identity, face, freckles, glasses, wardrobe, necklace, the microphone and her hand and nails, hairstyle including the loose flyaways, performance and lip motion, framing, lens and the stationary camera exactly; replace only the indoor white wall and doorway behind her with an open golden-hour meadow.

Photoreal. 9:16. 4s. Warm golden-hour grade on the new environment only, subject's own light preserved. SFX and source dialogue only.

Continuous locked shot, same close-up framing, same lens and stationary eye-level camera as the source. She keeps her exact performance and mouth motion, microphone in hand near her chin, lips matching the source exactly, saying clearly: "Cuando pienses que tu comunidad es demasiado pequeña para hacer la diferencia... mira esto." Behind her the indoor wall and doorway are fully replaced by an open golden-hour meadow of green rolling hills receding into a soft lavender sky, warm amber light glowing low on the horizon behind her shoulders; the field sits heavily out of focus, creamy shallow depth of field matching the source blur, a faint golden haze softening the hills, gentle grass sway and a slow drift of warm light the only motion back there. Preserve her original soft warm key light and do not relight or repaint her face; integrate her into the scene only with a subtle warm sun bounce from screen-right, a light golden rim on the edge of her hair and glasses, matched atmospheric haze, depth of field, focus falloff and film grain, so she occupies the same space with no hard cut-out edges or halos. Lock-down: face, identity, freckles, expression, glasses, wardrobe, necklace, microphone, hands, hair and flyaways, lip motion and framing unchanged and identical to the source; only the environment behind her and its light integration are new.

SFX and source dialogue only: her own voice delivering the line clearly with no added music, a light breeze rustling distant grass, faint far-off birdsong, soft open-field air.

Cómo lo lees cuando vuelva, en orden de lo que se rompe primero. Primero la cara: si te reconoces, seguiste siendo tú, el fork de luz preservada funcionó. Segundo el borde: busca halo o recorte duro alrededor del pelo y los hombros, que es el "looks pasted in" que el skill advierte, y si aparece es que integró por color pero no por luz. Tercero la voz: si suena rara, no toques el prompt, aplica la red de seguridad y re-pegas tu audio. Cuarto el fondo: que el bokeh cuadre con el del clip, no más nítido.

Y la disciplina de iteración que trae el skill, porque es la que te ahorra créditos: cambia una sola cosa por re-roll. Si el borde del pelo falla, solo endureces esa cláusula. Si te aclara la piel, solo agregas preservación de skin tone. No reescribas el prompt completo cuando algo esté cerca, porque pierdes lo que ya sirvió. Y si después de dos re-rolls la cara sigue derivando, ese es el aviso de que este shot específico se hace mejor por composición, y el skill queda para el reveal con multitud, que es donde generar de verdad tiene sentido.

Súbelo con el clip como @source real, no como referencia de estilo, y déjame saber qué te devuelve en esos cuatro puntos. Con eso ajustamos una sola palanca y no el prompt entero.

## 🧑 Adriana · 2026-07-03 03:28
regenera el prompt

## 🤖 Claude · 2026-07-03 03:29
El defecto que arrastra este prompt no es la redacción, es que le pides al modelo una operación que se contradice consigo misma en la misma frase. Preservar tu cara exacta y reiluminar el cuadro son vectores opuestos: la luz sobre tu piel son píxeles, y no hay forma de reescribir esos píxeles sin regenerar la cara que los sostiene. El skill lo dice sin ambigüedad, preservar la luz del sujeto y graduar solo lo nuevo es el fork de menor riesgo de identidad, y reiluminar todo es el de mayor. La versión que te generó Higgsfield Computer eligió el fork malo y encima lo escribió con gramática de descripción de escena, más cerca de generar desde cero que de transformar una toma. Por eso te cambió. No desobedeció, obedeció la instrucción equivocada.

Lo que cambia en esta reescritura, y por qué cada cosa:

Uno. Fork de luz preservada, no relight-all. Tu clip es tungsteno cálido, tu target es golden hour cálido. Las temperaturas ya están cerca, así que no necesitas reiluminarte para pegar en el campo. Conservas tu key y te integras solo con un rebote sutil. Esto solo es posible porque escogiste un mundo cálido. Con neón o azul frío estarías forzada al fork de riesgo.

Dos. La cláusula de lock se repite al final. El skill insiste en repetir el guardarraíl más frágil, cara e identidad, al cierre de la acción, porque el modelo pesa más lo último que lee.

Tres. Audio como preferencia, no como garantía. Dejo "SFX and source dialogue only" porque es el mecanismo del skill, pero Seedance sintetiza audio en el mismo pase, así que si la voz vuelve distinta, muteas y repegas tu audio original, que sincroniza porque video-to-video conserva el timing de tu boca. La garantía vive en ese paso de post, no en el prompt.

El prompt, en inglés y texto plano para copiar tal cual:

Hook · env-swap · golden-hour meadow, subject light preserved

@source: Original selfie-style vertical clip, ~4s. A young woman in a soft yellow knit cardigan and a dark red beaded necklace, gold wire-frame glasses, hair in a loose low style with flyaways at the hairline, holding a small black wireless microphone near her chin, speaking directly to camera in a locked eye-level close-up under warm indoor light. Preserve her identity, face, freckles, glasses, wardrobe, necklace, the microphone and her hand and nails, hairstyle including the loose flyaways, performance and lip motion, framing, lens and the stationary camera exactly; replace only the indoor white wall and doorway behind her with an open golden-hour meadow.

Photoreal. 9:16. 4s. Warm golden-hour grade on the new environment only, subject's own light preserved. SFX and source dialogue only.

Continuous locked shot, same close-up framing, same lens and stationary eye-level camera as the source. She keeps her exact performance and mouth motion, microphone in hand near her chin, lips matching the source exactly, saying clearly: "Cuando pienses que tu comunidad es demasiado pequeña para hacer la diferencia... mira esto." Behind her the indoor wall and doorway are fully replaced by an open golden-hour meadow of green rolling hills receding into a soft lavender sky, warm amber light glowing low on the horizon behind her shoulders; the field sits heavily out of focus, creamy shallow depth of field matching the source blur, a faint golden haze softening the hills, gentle grass sway and a slow drift of warm light the only motion back there. Preserve her original soft warm key light and do not relight or repaint her face; integrate her into the scene only with a subtle warm sun bounce from screen-right, a light golden rim on the edge of her hair and glasses, matched atmospheric haze, depth of field, focus falloff and film grain, so she occupies the same space with no hard cut-out edges or halos. Lock-down: face, identity, freckles, expression, glasses, wardrobe, necklace, microphone, hands, hair and flyaways, lip motion and framing unchanged and identical to the source; only the environment behind her and its light integration are new.

SFX and source dialogue only: her own voice delivering the line clearly with no added music, a light breeze rustling distant grass, faint far-off birdsong, soft open-field air.

Cómo lo lees cuando vuelva, en orden de lo que falla primero. La cara: si te reconoces, el fork sirvió. El borde del pelo y los hombros: si hay halo o recorte duro, integró por color pero no por luz. La voz: si suena rara, red de seguridad, no tocas el prompt. El fondo: que el bokeh cuadre con el del clip, ni más nítido ni más sucio.

Y la regla de iteración del skill, que es la que te ahorra créditos: una sola palanca por re-roll. Si falla el borde, endureces solo esa línea. Si te aclara la piel, agregas solo preservación de skin tone. No reescribas todo cuando algo esté cerca, porque pierdes lo que ya funcionó. Si después de dos intentos la cara sigue derivando, ese es el techo del generativo para este plano, y ahí composición en DaVinci te lo cierra sin discusión. Súbelo con el clip como @source, no como referencia de estilo, y dime cuál de los cuatro puntos falló para mover esa sola palanca.

## 🧑 Adriana · 2026-07-03 03:30
its useless it changes everything

## 🤖 Claude · 2026-07-03 03:30
Es inútil porque le estás pidiendo peras al olmo, y quiero ser claro en dónde exactamente está el olmo, porque llevas seis intentos peleando con la herramienta en vez de con el problema. Ningún prompt, por bien construido que esté, convierte un modelo generativo en uno que te respete. Seedance reconstruye cada frame desde cero guiándose por el tuyo. "Preserve identity" no es un candado, es una sugerencia que el modelo pondera contra todo lo demás que le pediste, y cuando hay tensión, pierde tu cara. No hay redacción que arregle eso, porque el defecto no está en las palabras, está en la categoría de la máquina. Te lo dije hace varios turnos y los intentos posteriores solo lo confirmaron: generación te reinterpreta, siempre, aunque le supliques que no.

Voy a dejar de darte prompts de generación para este shot, porque seguir haciéndolo sería hacerte perder créditos en un callejón sin salida. El plano del hook, tú hablando de cerca con el fondo desenfocado, no se resuelve generando. Se resuelve recortando. Y el recorte no tiene forma de cambiarte, porque tu video queda congelado como capa de arriba y solo se reemplaza lo de atrás. Es la diferencia entre repintar un cuadro y ponerle un fondo nuevo detrás de un vidrio: en el segundo caso el cuadro es intocable por diseño.

Te lo dejo en pasos exactos para que lo cierres hoy, sin IA generativa, en la herramienta que ya tienes.

CapCut, ruta rápida:

1. Abre CapCut, proyecto nuevo, sube tu clip del hook.
2. Selecciona el clip en la línea de tiempo. En el panel derecho busca "Remove background" o "Recorte automático", dentro de Video, sección "Cutout". Actívalo. CapCut te separa a ti del fondo. No te regenera, te recorta, así que tu cara, tu voz y tu boca quedan exactamente como grabaste.
3. Baja tu clip recortado a una pista superior. En la pista de abajo, sube la foto del campo golden hour. Ajústala a 9:16 para que llene el cuadro.
4. Revisa los bordes del pelo. Si ves un halo, usa el ajuste de "Refinar borde" o baja un pelín el "Feather" para suavizar. El bokeh del campo perdona casi todo aquí.
5. Toque final para que no se vea pegada: al clip del campo ponle un desenfoque leve, "Blur", para que iguale el desenfoque de tu fondo original, y baja un punto la exposición si el campo entra más brillante que tu cara. Exporta a la máxima resolución.

Tu voz nunca corrió peligro en esta ruta, porque el audio de tu clip viaja pegado al recorte. No hay nada que sintetizar, es tu pista original.

Si el pelo te queda sucio en CapCut, esa es la señal de subir a DaVinci Resolve, donde el Magic Mask maneja mejor los pelitos sueltos. Mismo principio, tú arriba intocable, campo abajo, pero con un recorte más limpio. Te guío por ahí si CapCut no te da el borde.

Y quiero que te lleves esto por encima de cualquier prompt, porque es lo que te va a sacar del ciclo: cuando el objetivo es que TÚ no cambies, la herramienta correcta nunca es la que genera un video nuevo, es la que produce un recorte o una máscara. Generación para crear lo que no existe, como la multitud del reveal. Recorte para preservar lo que ya grabaste, como este hook. Confundir las dos es lo que te tiene dando vueltas.

Dime una cosa nada más para no adivinar: cuando abres CapCut y seleccionas tu clip, ¿te aparece la opción de "Remove background" o "Cutout", sí o no? Si te aparece, en cinco minutos cierras el hook. Si no te aparece, es tema de versión de la app y te doy la ruta de DaVinci directo.

## 🧑 Adriana · 2026-07-03 03:31
pero se ve falso haciendolo asi en capcut

## 🤖 Claude · 2026-07-03 03:31
Se ve falso, y no es porque CapCut sea inferior a la IA. Se ve falso por una razón física concreta que ningún método arregla solo con la técnica de recorte: te falta la sombra de contacto y te sobra un borde limpio donde deberías tener transición de luz. Cuando recortas un sujeto grabado en un cuarto y lo pones sobre un campo, el cerebro de quien mira no busca la calidad del recorte, busca tres señales de que perteneces a ese espacio, y las tres están ausentes por defecto. Ninguna herramienta las pone por ti. Hay que construirlas a mano.

Te desgloso las tres, en orden del impacto que tienen sobre la sensación de "pegado".

La primera y la más grave es la sombra de contacto, aunque en tu caso puntual pesa menos. En un plano entero, si no proyectas sombra sobre la grama, flotas, y ahí muere todo. Pero tu hook es un primer plano de pecho hacia arriba, no se te ven los pies ni el punto donde tocas el piso, así que esta señal casi no aplica aquí. Guárdala para el reveal, donde sí estás de cuerpo entero y será el asesino número uno.

La segunda es la que de verdad te está delatando en este close-up: el borde. Un recorte de CapCut te deja un contorno demasiado nítido y demasiado uniforme alrededor del pelo y el hombro, un filo que en la vida real no existe. Los objetos reales, contra un fondo desenfocado, tienen el borde ligeramente suave y a veces contaminado por la luz del entorno. Tu recorte tiene un borde de bisturí. Eso, más que cualquier otra cosa, es lo que grita "capa pegada". Se arregla con dos ajustes que CapCut sí tiene: baja el "feather" o suavizado del borde apenas uno o dos puntos para matar el filo, y si el pelo te quedó con halo claro, reduce el grosor del contorno o usa "refinar borde". No lo exageres, porque pasarte de feather te come los pelitos y se ve peor.

La tercera es la coherencia de luz y foco, y es donde se gana o se pierde el realismo de verdad. Tú estás iluminada con luz cálida y plana de interior. El campo, aunque sea golden hour, tiene su propia dirección y su propio desenfoque. Si dejas tu clip tal cual sobre el campo tal cual, son dos fotografías distintas apiladas. Hay que forzar que conversen. Tres movimientos concretos en CapCut:

Igualar el desenfoque. Tu fondo original de dormitorio ya estaba fuera de foco. Si pones la foto del campo nítida detrás de ti, el contraste de nitidez te delata, porque tu cara tiene el nivel de foco de un fondo borroso, no de un paisaje definido. Ponle "Blur" a la capa del campo hasta que su nivel de desenfoque se parezca al que tenías en el cuarto. El campo debe leerse como atmósfera, no como postal.

Igualar la temperatura y la exposición. Aunque ambos son cálidos, el campo probablemente entra más brillante o más saturado que tu cara. Baja un punto la exposición de la capa del campo y acércale la temperatura a la tuya con el ajuste de "Color" o "Temperatura". El objetivo es que la luz detrás de ti se sienta como la misma luz que te toca a ti.

Sembrar un rebote de luz sobre ti. Este es el truco que casi nadie hace y es el que vende el compuesto. En la vida real, un campo dorado detrás de ti te tira un poco de su luz sobre el pelo y el hombro. Duplica tu clip, al de arriba ponle una máscara suave solo en el borde del pelo del lado de donde viene el sol, súbele un toque de calidez o exposición, y bájale la opacidad. Ese rimlight falso, sutil, es lo que hace que parezca que el sol del campo te está tocando. Sin él, siempre vas a verte iluminada por una lámpara que ese campo no tiene.

Ahora, una verdad estratégica que va por encima de la técnica, porque llevas siete turnos peleando por realismo fotográfico en un formato que no lo exige. Los videos de "followers vs personas" que te inspiraron nunca se vieron perfectamente reales, y no les hizo falta. El formato vive de la idea, del salto de tú sola a tú rodeada, no de que el compuesto engañe a un supervisor de VFX. Un fondo con desenfoque, buena temperatura y un rimlight sutil es más que suficiente para que la audiencia compre el concepto. Estás persiguiendo un estándar de fotorrealismo que ni la referencia cumplía, y esa persecución es lo que te tiene trancada. Lo que hace creíble tu video no es el borde perfecto de tu pelo, es que el mensaje de comunidad aterrice.

Y la pregunta honesta que hay que ponerte sobre la mesa: si después de igualar desenfoque, exposición y rimlight todavía te chirría, el problema puede no ser el compuesto, puede ser que un primer plano cálido de interior simplemente no quiere vivir en un campo, y ninguna cantidad de ajuste lo va a forzar. En ese caso la salida más limpia no es más edición, es regrabar el hook en luz neutra cerca de una ventana, o aceptar que el hook se queda en interior y el campo entra en el corte del reveal, con el salto de ambiente montado a la palabra "esto". A veces el compuesto correcto es el que no se hace.

Dime qué de las tres señales es la que más te está molestando cuando lo ves, el borde, la diferencia de foco, o la luz que no cuadra. Con eso te doy los números exactos de cada slider en CapCut en vez de la explicación general.

## 🧑 Adriana · 2026-07-03 03:33
siguiendo de lo que dice aca: https://higgsfield.ai/blog/VFX-with-Seedance-4k

lee los ejemplos de prompts

## 🤖 Claude · 2026-07-03 03:34
No puedo leer esa página todavía, tengo que buscarla porque el enlace directo no me abre sin haberlo recuperado primero. Déjame traerla.

Ya leí los cinco prompts, y hay un patrón que confirma exactamente por qué a ti te ha estado cambiando todo y a ellos no. La diferencia no es que ellos escriban mejor. Es que ellos nunca le piden al modelo lo que tú le has estado pidiendo. Mira lo que TODOS estos ejemplos cambian, sin excepción: el mundo, la ropa, criaturas nuevas, el clima. Y mira lo que NINGUNO cambia: el ambiente sobre la cara del sujeto en un primer plano hablando. En cada caso el sujeto está en plano medio o entero, con movimiento de cuerpo o de cámara, y el efecto ocurre detrás y alrededor, no encima de sus facciones. Estás usando la técnica correcta, pero sobre el tipo de plano donde esa técnica es más frágil.

Te destrinco lo que estos prompts hacen bien y que a ti te faltaba, porque de aquí sale tu versión corregida.

Primero, el ancla del source es una etiqueta, no una descripción. Todos abren con `<<<video_1>>>` y ordenan seguir ese video con precisión 1 a 1, misma cámara, misma actuación, mismo timing. Tú venías describiendo la escena en prosa, que empuja hacia generar de cero. La etiqueta amarra el clip real como base. Ese es el cambio técnico más grande.

Segundo, y esto contradice de frente lo que decía tu prompt anterior: ninguno de estos preserva el audio original. Todos dicen lo contrario, "remove and discard all original audio", y generan SFX nuevo. Ahí está tu respuesta sobre la voz, cruda. El workflow oficial de Higgsfield asume que la voz de origen se descarta. Si tú quieres conservar TU voz, estás yendo contra el flujo que ellos diseñaron. Por eso te la cambiaba. Su patrón no protege voz, la reemplaza.

Tercero, la estructura de bloques con MAYÚSCULAS y una sección FORBIDDEN. Los prompts largos separan SOURCE LOCK, INTEGRATION, PHYSICS, y cierran con una lista de lo prohibido. Esa lista negativa es la que caza los errores concretos, "warped face", "different color temp", "pasted-on". Tu prompt no tenía esa red.

Cuarto, y decisivo para ti: la sección de light-match es idéntica a lo que te vengo diciendo hace turnos. "Never pasted, never crisper than the plate, never a different color temp." El prompt de los sauropodos lo pone como TOP PRIORITY. Todos matan el borde y fuerzan que el elemento nuevo comparta grado, exposición, grano y niebla con el plano. Eso es lo que evita el look pegado.

Ahora la verdad incómoda que estos ejemplos dejan clarísima. Todos meten un elemento nuevo, dragón, dinosaurio, manada, sobre un plano CON movimiento. El movimiento y la distancia esconden las imperfecciones de la cara. Tu hook es lo contrario: primer plano, cara enorme, quieta, hablando. Es el escenario más despiadado para video-to-video, porque cualquier micro-deriva en tus facciones se ve gigante y el lip-sync tiene que aguantar palabra por palabra. Estos prompts no resuelven tu caso, lo esquivan, porque nadie en su sano juicio hace VFX generativo sobre un talking-head en primer plano si puede evitarlo.

Dicho eso, si quieres ir con su método al pie de la letra, aquí está tu prompt reescrito con su estructura exacta, etiqueta de source, bloques, light-match y FORBIDDEN. En inglés, texto plano, listo para pegar sobre tu clip subido como `<<<video_1>>>`:

=== COMMUNITY HOOK — V2V on <<<video_1>>> (~4s) — BACKGROUND SWAP ===

SOURCE LOCK — READ FIRST
Build on <<<video_1>>>. KEEP 1:1: the woman's identity, FACE, freckles, gold wire-frame glasses, her EXACT performance, mouth movement and lip motion and timing; wardrobe (soft yellow knit cardigan, dark red beaded necklace); the small black wireless microphone in her hand, her hand and nails; hairstyle including the loose flyaways at the hairline; and the exact CAMERA, a locked eye-level close-up, same framing, same lens, stationary. Do NOT re-frame, re-time, re-angle, or move the camera. Only the wall behind her changes.

ENVIRONMENT SWAP
Replace the indoor white wall and doorway behind her with an open golden-hour meadow of green rolling hills receding into a soft lavender sky, warm amber light low on the horizon behind her shoulders. The field sits heavily out of focus, creamy shallow depth of field matching the source background blur, faint golden haze, gentle grass sway the only motion back there. It reads as soft atmosphere behind a close-up, not a sharp postcard.

INTEGRATION / LIGHT-MATCH (top priority)
Preserve her original soft warm indoor key on her face, do NOT relight or repaint her face. Integrate her into the meadow only with a subtle warm sun bounce from screen-right, a light golden rim on the edges of her hair and glasses, matched atmospheric haze, matched depth of field and focus falloff, matched film grain. Her warm indoor light and the golden-hour field already share a warm temperature, so no full relight is needed. Never pasted, never crisper than the background, never a different color temp, no hard cut-out edge or halo around her hair.

PHYSICS
Only gentle background motion: grass sway, a slow drift of warm light, faint haze. She and the camera stay exactly as the source.

FORBIDDEN: changing her face, expression, freckles, glasses, wardrobe, necklace, mic, hands, hair or flyaways; altering her lip motion or de-syncing her speech; relighting or repainting her face; moving, re-framing or re-timing the camera; a sharp or in-focus field; hard cut-out edges or halo on the hair; a cool or different color temp on her; warped face; on-screen text or watermark.

~4s. 9:16 (match <<<video_1>>>). SFX and source dialogue only: keep her original spoken line, a light breeze in distant grass, faint far-off birdsong. No music. No on-screen text.

Fíjate en la única desviación que hice de su plantilla, y es a propósito: ellos ponen "remove all original audio", yo puse "SFX and source dialogue only" para intentar salvar tu voz. Pero ya viste que su flujo asume descarte de voz, así que trátalo como no garantizado. Si vuelve con tu voz alterada, el plan no cambia: generas, muteas el audio del render, y repegas el audio de tu clip original en CapCut, que sincroniza porque el video-to-video conserva el timing de tu boca.

Mi lectura estratégica, sin rodeos, después de leer sus propios ejemplos: su método brilla justo donde tu hook no está, en planos con movimiento y elementos nuevos alrededor de un sujeto que no es el foco milimétrico. Para el reveal con la multitud, este método es perfecto, es literalmente el caso "man alone on a plain, a herd charges in from behind, one continuous shot", cámbialo por "mujer sola en un campo, una multitud aparece detrás". Ese prompt de los sauropodos es tu plantilla exacta para el reveal. Para el hook en primer plano, sigue siendo terreno hostil, y el recorte en CapCut te da garantía donde el generativo te da lotería.

Dos caminos y decides tú. Corres este prompt en Seedance 4K a ver si tu cara aguanta el primer plano, sabiendo que es el escenario difícil, y si deriva te pasas a recorte. O aceptas desde ya que el hook va por recorte y guardas toda tu energía de Seedance para el reveal, donde su método rinde de verdad. ¿Cuál agarras, y te armo el prompt del reveal con la plantilla de la manada aplicada a tu multitud?
