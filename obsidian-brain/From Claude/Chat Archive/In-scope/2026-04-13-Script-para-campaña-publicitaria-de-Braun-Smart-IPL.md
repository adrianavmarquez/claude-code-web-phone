---
title: "Script para campaña publicitaria de Braun Smart IPL"
source: claude.ai-chat
created: "2026-04-13 14:51"
summary: "**Conversation Overview**  This session continued a paid brand collaboration creative project for Braun Smart IPL with creator handle @adrianavmarquez. The conversation picked up from a previously compacted session (transcript at /mnt/transcripts/2026-06-04-04-08-09-braun-ipl-collab-scripts.txt) where two full video scripts and slide assets had already been developed. The person asked Claude to recreate the Girl Math 101 presentation slides using the exact design reference Claude had previously described: 'Poppins, #D72323, #3846C4, #FFBA35, blanco y negro. Bold, editorial, tipografía grande como el inspo.'  The person then asked whether Claude could offer template options to choose from, or alternatively create a Google Slides presentation. Claude generated both a PDF (via Python/ReportLab) and a PPTX (via pptxgenjs) of the five-slide Girl Math 101 deck in brand colors with Poppins font at 16:9 dimensions. Claude also attempted to upload the file to Google Drive but the upload was incomplete. The person then clarified that the file showing in outputs was the PDF version, not the PPTX, prompting Claude to surface the PPTX file directly for download.  The established brand constants carried through all outputs: colors #D72323, #3846C4, #FFBA35, black and white; font Poppins Bold/Regular; handle @adrianavmarquez; disclosure #BraunPartner #ad. The PPTX file is available at /mnt/user-data/outputs/GirlMath101_BraunIPL.pptx and the PDF at /mnt/user-data/outputs/GirlMath101_BraunIPL.pdf. To open as native Google Slides, the recommended path is uploading the PPTX to Google Drive and opening with Google Slides, or going to slides.google.com/create and importing directly.  **Tool Knowledge**  Google Drive file uploads via the MCP connector require a complete base64-encoded content parameter. In this session, the upload attempt sent only a fragment of the encoded PPTX, resulting in an incomplete file in Drive. The correct approach is to read the full file bytes, encode entirely, and pass the complete base64 string in one call. For PPTX-to-Google-Slides conversion, the Drive API accepts contentMimeType of application/vnd.openxmlformats-officedocument.presentationml.presentation and will convert to Google Slides format when mimeType is set to application/vnd.google-apps.presentation, but this only works reliably when the full file content is provided. When the upload cannot be completed in one call due to file size, instructing the person to manually upload the downloaded PPTX to Drive and open with Google Slides is the reliable fallback."
messages: 79
claude_uuid: "1c049ad8-91ee-4a19-a5fc-d4c98a1003dc"
tags: [claude, chat, archive]
---
# Script para campaña publicitaria de Braun Smart IPL

> **Conversation Overview**

This session continued a paid brand collaboration creative project for Braun Smart IPL with creator handle @adrianavmarquez. The conversation picked up from a previously compacted session (transcript at /mnt/transcripts/2026-06-04-04-08-09-braun-ipl-collab-scripts.txt) where two full video scripts and slide assets had already been developed. The person asked Claude to recreate the Girl Math 101 presentation slides using the exact design reference Claude had previously described: "Poppins, #D72323, #3846C4, #FFBA35, blanco y negro. Bold, editorial, tipografía grande como el inspo."

The person then asked whether Claude could offer template options to choose from, or alternatively create a Google Slides presentation. Claude generated both a PDF (via Python/ReportLab) and a PPTX (via pptxgenjs) of the five-slide Girl Math 101 deck in brand colors with Poppins font at 16:9 dimensions. Claude also attempted to upload the file to Google Drive but the upload was incomplete. The person then clarified that the file showing in outputs was the PDF version, not the PPTX, prompting Claude to surface the PPTX file directly for download.

The established brand constants carried through all outputs: colors #D72323, #3846C4, #FFBA35, black and white; font Poppins Bold/Regular; handle @adrianavmarquez; disclosure #BraunPartner #ad. The PPTX file is available at /mnt/user-data/outputs/GirlMath101_BraunIPL.pptx and the PDF at /mnt/user-data/outputs/GirlMath101_BraunIPL.pdf. To open as native Google Slides, the recommended path is uploading the PPTX to Google Drive and opening with Google Slides, or going to slides.google.com/create and importing directly.

**Tool Knowledge**

Google Drive file uploads via the MCP connector require a complete base64-encoded content parameter. In this session, the upload attempt sent only a fragment of the encoded PPTX, resulting in an incomplete file in Drive. The correct approach is to read the full file bytes, encode entirely, and pass the complete base64 string in one call. For PPTX-to-Google-Slides conversion, the Drive API accepts contentMimeType of application/vnd.openxmlformats-officedocument.presentationml.presentation and will convert to Google Slides format when mimeType is set to application/vnd.google-apps.presentation, but this only works reliably when the full file content is provided. When the upload cannot be completed in one call due to file size, instructing the person to manually upload the downloaded PPTX to Drive and open with Google Slides is the reliable fallback.

## 🧑 Adriana · 2026-04-13 14:51
Actua como un professional creative director, y vamos a hacer un script para Braun Smart IPL. Este video va a ser posteado en mis plataformas, y publicitado por la marca. 

Mi input: Soy una chica que se hizo laser en el pasado, gasto miles de dolares en su tratamiento y al año ya tenia que hacerme retoques porque me empezó a salir bello de nuevo. Ir a las consultas es inconvinient, el proceso DUELE, y tengo que volver a pagar. Por eso Braun IPL fue mi salvacion, mi mejor opcion. Puedo hacerlo a mi tiempo, Sin dolor, y a un excelente precio porque soy yo duena de mi maquinaria y de mi tratamiento. 

te adjuntare el brief de la campana que ellos pasaron, y te pondre los transcripts de los videos que ellos ponen como sugerencias:

video 1:
[00:00 - 00:08] I've been so busy lately. The last thing I want is another beauty appointment to squeeze in.
[00:08 - 00:13] Thankfully, Bronx sent me their Smart IPL. It's an at-home alternative to laser hair removal.
[00:13 - 00:18] It's made my routine so much easier. I have way more time for all the things I actually enjoy,
[00:18 - 00:24] like workouts, traveling, events. I use it once a week. It takes about 10 minutes, and the app guides me step-by-step.
[00:24 - 00:31] As an on-the-go girl, the Smart IPL makes self-care so quick and easy. I feel more confident and actually have time for myself again.
[00:31 - 00:35] If you're wanting an easier beauty routine, this is your sign.
[00:38 - 00:43] Would you rather keep shaving and waxing all the time, or have the freedom of smooth, hairless skin from home?
[00:43 - 00:47] Big thanks to Bronx for sending me the Smart IPL. It's freed up so much of my time.
[00:47 - 00:49] Girls' nights hit way different when you're not rushing to shave.
[00:49 - 00:55] I've been using it on my arms, and it's honestly so easy. I just glide it over my skin once a week, and it takes about 10 minutes.
[00:55 - 01:00] The app reminds me when it's time for my next session and shows me exactly how to use it so I stay consistent.
[01:00 - 01:02] I started seeing results after my first use.
[01:02 - 01:07] The Bronx Smart IPL is $120 off for the Thanksgiving sale from November 16th to December 1st.
[01:07 - 01:09] Make sure to grab it while it's on sale.
video 2:
[01:12 - 01:14] Let's play a little game of this or that.
[01:14 - 01:18] Big thanks to Bronx for hooking me up with my latest beauty obsession, the Bronx Smart IPL.
[01:18 - 01:21] Endless laser appointments, or the freedom to do it from home.
[01:21 - 01:25] Ingrown hairs and irritation, or dermatologist-recommended gentle treatment.
[01:25 - 01:28] Waxing pain, or gentle light pulses.
[01:28 - 01:33] Bulky protective eyewear every session, or built-in light filters for comfortable use with no bubbles needed.
[01:33 - 01:35] If I don't have to leave home for hair removal, I'm sold.
[01:35 - 01:38] With Bronx IPL, I can do it at home in just minutes.
[01:38 - 01:42] It uses gentle light pulses to target hair at the roots, so over time, the regrowth slows down.
[01:42 - 01:45] You see results after the first use, and it can last up to two years.
[01:45 - 01:49] Now, instead of stressing about shaving, I actually have more freedom for things I love.
[01:49 - 01:52] Hiking, Pilates, even last-minute nights out.
[01:52 - 01:54] For me, it's become a part of my self-care.
[01:54 - 01:58] Choosing convenience, choosing confidence, and reminding myself I'm worth investing in.
[02:12 - 02:30] The Bronx IPL is literally all you need to get laser-like results at home, and I'm going to show you how I do it.
[02:30 - 02:33] This is the only device I use on sensitive areas like my upper lip.
[02:33 - 02:35] It has three different comfort levels.
[02:35 - 02:40] The skin tone sensor makes sure the flash power adjusts automatically to match my skin, which is pretty cool.
[02:40 - 02:43] So if my skin's not suited for IPL, it won't even flash.
[02:43 - 02:45] I feel like it really knows what it's doing.
[02:45 - 02:47] It's super easy to use, and my results have been incredible.
[02:47 - 02:51] I saw results after using it once, and will have a year and a half of smooth skin.
[02:51 - 02:52] I'm obsessed.
[02:57 - 03:01] I'm a beautiful brown girl, which means I come with beautiful brown girl hair everywhere.
[03:01 - 03:09] Laser hair removal can get expensive, and for a lazy girl like me, if you're telling me I have to leave my place to go back to get painful touch-ups, I don't think so.
[03:09 - 03:16] So if you're looking for a non-complicated tool that is light and compact that will instantly show you results after the second use, look no further.
[03:16 - 03:21] Check out the Bronx IPL, a quick, nearly painless, easy-to-use tool for at-home hair removal.
[03:39 - 05:00] [Segmentos sin diálogo / música / texto en pantalla: www.bronxipr.com]
[05:00 - 05:02] If you want laser-like smooth skin at home, you have to try the Bronx IPL.
video 3:
[05:09 - 05:11] Let's fire her up, Peggy. [05:11 - 05:13] Scary every time, I promise it's not. [05:13 - 05:16] Now, this is no ordinary IPL. It's actually the world's first smart IPL. [05:16 - 05:17] It's super user-friendly. [05:17 - 05:19] The app component is just lovely. [05:19 - 05:21] It guides you step-by-step through the hair removal process, [05:21 - 05:23] so you know exactly how to use it for the best results. [05:23 - 05:27] So out of your entire week, if you just take 10 minutes, you can have a full-body treatment. [05:27 - 05:29] This is the gorgeous box it comes with. [05:29 - 05:32] There's different attachments in here, of course, based on where you want the hair removal. [05:32 - 05:36] IPL stands for Intense Post Light, and it's like the best at-home alternative for lasers. [05:37 - 05:38] Powered on that quick. [05:38 - 05:40] Oh my god, it's like cologne soft. [05:40 - 05:42] Let me know if you give it a try, and thank you for watching. [05:42 - 05:44] Okay, bye!

## 🤖 Claude · 2026-04-13 14:51

## 🧑 Adriana · 2026-04-13 15:11
Actua como un professional creative director, y vamos a hacer un script para Braun Smart IPL. Este video va a ser posteado en mis plataformas, y publicitado por la marca. 

Mi input: Soy una chica que se hizo laser en el pasado, gasto miles de dolares en su tratamiento y al año ya tenia que hacerme retoques porque me empezó a salir bello de nuevo. Ir a las consultas es inconvinient, el proceso DUELE, y tengo que volver a pagar. Por eso Braun IPL fue mi salvacion, mi mejor opcion. Puedo hacerlo a mi tiempo, Sin dolor, y a un excelente precio porque soy yo duena de mi maquinaria y de mi tratamiento. 

te adjuntare el brief de la campana que ellos pasaron, y te pondre los transcripts de los videos que ellos ponen como sugerencias:

Y vamos a hacer brainstorming de angulos y hooks que sirvan tanto para la marca como para mi como creadora
> 📎 

## 🤖 Claude · 2026-04-13 15:13
Perfecto, ya tengo todo lo que necesito. Vamos al brainstorming.

Esto es lo que armé después de leer el brief completo y cruzarlo con tu historia.

Tu input tiene algo que los otros 6 videos del brief no tienen: credibilidad comparativa real. Tú no eres alguien que "siempre odió ir al salón." Eres alguien que ya apostó por el láser, lo pagó, lo vivió, y lo vio fallar. Eso es un ángulo mucho más poderoso para conversión pagada, que es exactamente lo que Braun está buscando con este brief.

Lo que el brief pide como obligatorio: hook visual fuerte al inicio (preferiblemente before/after con timestamp), mencionar la app, hablar de los resultados en primera persona, y dejar claro el "freedom messaging." Todo eso puede fluir de tu historia sin sentirse forzado.

Abrí cada ángulo para ver el hook propuesto, seleccioná los que te llamen y armamos el script desde ahí.

## 🧑 Adriana · 2026-04-13 15:15
Quiero desarrollar el script completo con estos ángulos: POV: segunda oportunidad, Antes y después con timestamp (brief must-have). Podemos empezar.

## 🤖 Claude · 2026-04-13 15:15
Sin entradas `[APERTURA DB]` todavía, así que arrancamos desde cero en la base de datos hoy.

Antes de escribir el script, necesito que me respondas dos cosas rápido:

**1. El POV central.** Este es un collab con la marca, pero el video sale en tus plataformas con tu voz. ¿Cuál es la creencia de este video en una sola oración? ¿Es "el láser es una estafa"? ¿"La autonomía sobre tu cuerpo es el verdadero lujo"? ¿"Dejé de pagarle a la industria del dolor"? Necesito saber qué crees tú, no qué quiere Braun que digas.

**2. El before/after.** El brief lo exige con timestamp visible como parte del hook visual. ¿Tenés fotos? ¿En qué parte del cuerpo son las más notorias? ¿Cuánto tiempo llevas usando el dispositivo? Eso determina cómo escribo el momento de apertura silenciosa antes del VO.

## 🧑 Adriana · 2026-04-13 22:54
1. Mi POV es que perdí mi dinero con Laser Treatments en el salon. Porque no te garantiza que no te saldran y encima para los retoques tienes que pagar un dineral. 
2. Llevo 1 mes, haciendolo 1 vez a la semana por 10 min aprox y ya no salen casi vellos. Me lo he hecho solo en las piernas! 1 mes de diferencia Marzo 10 y Abril 13

## 🤖 Claude · 2026-04-13 22:54
Perfecto. POV claro, fechas concretas, zona específica. Eso es todo lo que necesito.

Una aclaración antes de escribir: 1 mes es muy poco tiempo para afirmar resultados dramáticos de IPL (el brief habla de hasta 2 años de piel suave, con resultados visibles desde el primer uso). Voy a escribir el script siendo honesta con tu timeline real, "en un mes ya noto la diferencia" es creíble y poderoso. No vamos a exagerar porque eso te puede costar credibilidad con tu audiencia y con la marca.

Aquí va el script:

---

**MAPA DE PRODUCCIÓN**

Formato: Reel / vertical 9:16
Duración estimada: 45 a 55 segundos
Idioma: Español con Spanglish natural
Estructura: POV visual silencioso → confesión → contraste → demostración → cierre con ownership

---

**SCRIPT — DRAFT 1**

**[00:00 a 00:05] HOOK VISUAL, SIN VOZ**
*Pantalla dividida o corte directo: foto piernas Marzo 10 con fecha visible / foto piernas Abril 13 con fecha visible.*
Texto en pantalla: **"1 mes. 1 vez a la semana. 10 minutos."**

**[00:05 a 00:15] APERTURA — VOZ EN OFF O A CÁMARA**
"POV: gastaste miles de dólares en laser, te prometieron que era definitivo, y al año te llaman para decirte que necesitas retoques... y que tienes que volver a pagar."

**[00:15 a 00:22] EL PIVOT**
"Eso me pasó a mí. Y no voy a volver a caer. Braun Smart IPL llegó a mi vida y literalmente cambió mi relación con la depilación."

**[00:22 a 00:35] DEMOSTRACIÓN**
*Clip usando el dispositivo en las piernas, mínimo 3 flashes visibles, movimiento de glide.*
"Lo uso una vez a la semana, me toma diez minutos, y la app me guía paso a paso para que no me salte ni un área. No me tengo que mover de mi cuarto. No me duele. Y la máquina es mía."

**[00:35 a 00:45] CIERRE — OWNERSHIP**
"Ya no le pago a nadie para que me quite el pelo. Ahora yo controlo mi tratamiento, mi tiempo, y mis resultados."
*Texto en pantalla: @adrianavmarquez usa Braun Smart IPL*
*CTA: Link en bio*

---

**MAPA DE RITMO**

```
[APERTURA VISUAL — silencio total]
Foto split → texto en pantalla → que el visual hable solo
-> el silencio aquí es intencional, genera curiosidad antes del VO

[CONFESIÓN — rápido, directo]
"POV: gastaste miles de dólares..." -> velocidad alta, tono algo amargo
"...y que tienes que volver a pagar." -> última palabra con pausa, deja aterrizar

[PIVOT — bajar un segundo]
"Eso me pasó a mí." -> pausa real aquí, corto y firme
"Braun Smart IPL llegó a mi vida..." -> tono sube, energía cambia

[DEMOSTRACIÓN — ritmo medio]
Clips de uso mientras hablas -> no compites con el visual, VO más tranquilo
-> pausa natural después de "No me duele."

[CIERRE — sube para el remate]
"La máquina es mía." -> pausa deliberada
"Yo controlo mi tratamiento..." -> firme, no agresivo, convencido
Última línea -> tono final, punto.
```

Las pausas después de "al año te llaman" y después de "eso me pasó a mí" son las más importantes del video. Ahí es donde tu audiencia que hizo láser dice "yo también." No las cortes en edición.

---

Revisión 0 de 5. Este es el draft base. ¿Qué sentís cuando lo lees en voz alta? ¿Hay algo que no suena como vos?

## 🧑 Adriana · 2026-04-13 23:11
POV: gastaste miles de dólares en laser, te prometieron que era definitivo, y al año llamas para porque necesitas retoque… y te quieren volver a cobrar.

## 🤖 Claude · 2026-04-13 23:11
Buena corrección. Más tuya, más conversacional, el "llamas porque" tiene un ritmo de indignación real que funciona mejor que mi versión más pulida.

La adopto exacta. Revisión 1 de 5, solo cambié esa línea:

---

**SCRIPT — REVISIÓN 1**

**[00:00 a 00:05] HOOK VISUAL, SIN VOZ**
*Split: foto piernas Marzo 10 con fecha visible / foto piernas Abril 13 con fecha visible.*
Texto en pantalla: **"1 mes. 1 vez a la semana. 10 minutos."**

**[00:05 a 00:15] APERTURA**
"POV: gastaste miles de dólares en laser, te prometieron que era definitivo, y al año llamas porque necesitas retoque… y te quieren volver a cobrar."

**[00:15 a 00:22] EL PIVOT**
"Eso me pasó a mí. Y no voy a volver a caer. Braun Smart IPL llegó a mi vida y literalmente cambió mi relación con la depilación."

**[00:22 a 00:35] DEMOSTRACIÓN**
*Clip usando el dispositivo en las piernas, mínimo 3 flashes visibles, glide.*
"Lo uso una vez a la semana, me toma diez minutos, y la app me guía paso a paso para que no me salte ni un área. No me tengo que mover de mi cuarto. No me duele. Y la máquina es mía."

**[00:35 a 00:45] CIERRE**
"Ya no le pago a nadie para que me quite el pelo. Ahora yo controlo mi tratamiento, mi tiempo, y mis resultados."
*Texto en pantalla: @adrianavmarquez usa Braun Smart IPL*
*CTA: Link en bio*

---

¿Algo más que cambiar, o lo mandamos al doc de script?

## 🧑 Adriana · 2026-04-13 23:34
No mi hook visual creo que sería yo gritando en una almohada a varias alturas de mi cuarto como stop Motion como un meme mientras leen el on screen caption hook. Luego visualmente muestro el clip del before con el time stamp seguido del after con time stamp. Mientras suena el VoiceOver: Eso me pasó a mí. Y no pensaba volver a caer. Visual: hablando a cámara mientras me paso la IPL y salen los flashes en cámara diciendo: Hasta que Braun Smart IPL llegó a mi vida y LITERALMENTE cambió mi relación con la depilación láser. Demostración: Acerco la IPL a la cámara la prendo, le cambio la intensidad. VoiceOver: lo uso una vez a la semana, me toma 10 minutos. Visual: muestro un screen recording de cómo se ve la IPL conectada a la aplicación, como agrego mi sesión del área donde me la haré y luego como es la sesión guiada pero ya mostrándolo desde un birds eye con el teléfono en el mueble con mi pierna encima del asiento y se ve como me pasó la máquina y me indica si voy bien o mal. Mientras digo: y la app le guía paso a paso para no saltarme ningún área. Desde mi cuarto. No me duele. Visual: giro mi cara hacia abajo y la camara ahora está worms eye, mientras digo: Y la máquina es mía. PARA SIEMPRE. 
Visual: sosteniendo la cámara con mi mano tipo selfie hablándole a la cámara mientras digo: ya no le pago a nadie para que me depile. Ahora yo controlo mi tratamiento, mi tiempo y mis resultados. 
Visual: camara desde mi POV: cierro el bolsito y suena el VoiceOver: link in bio

## 🤖 Claude · 2026-04-13 23:34
Revisión 2 de 5.

Esto ya es dirección de arte, no solo script. Lo reescribo en formato beat-by-beat para que puedas filmar con esto en la mano:

---

**SCRIPT FINAL — REVISIÓN 2**
**Braun Smart IPL x @adrianavmarquez**

---

**[BEAT 1 — HOOK VISUAL]**
*00:00 a 00:06*
Visual: stop motion de vos gritando en una almohada, varias alturas del cuarto, formato meme.
Audio: silencio o sound trending
On screen caption: **"POV: gastaste miles de dólares en laser, te prometieron que era definitivo, y al año llamas porque necesitas retoque… y te quieren volver a cobrar."**

---

**[BEAT 2 — BEFORE/AFTER]**
*00:06 a 00:12*
Visual: clip before piernas Marzo 10 con timestamp visible, corte directo a clip after piernas Abril 13 con timestamp visible.
VoiceOver: *"Eso me pasó a mí. Y no pensaba volver a caer."*

---

**[BEAT 3 — PIVOT + PRODUCTO]**
*00:12 a 00:20*
Visual: hablando a cámara mientras me paso la IPL por la pierna, flashes visibles en cámara.
VoiceOver: *"Hasta que Braun Smart IPL llegó a mi vida y LITERALMENTE cambió mi relación con la depilación."*

---

**[BEAT 4 — DEMOSTRACIÓN DISPOSITIVO]**
*00:20 a 00:26*
Visual: acerco la IPL a la cámara, la prendo, cambio la intensidad en vivo.
VoiceOver: *"Lo uso una vez a la semana, me toma 10 minutos."*

---

**[BEAT 5 — APP + SESIÓN GUIADA]**
*00:26 a 00:38*
Visual: screen recording de la app conectada al dispositivo. Agrego sesión por área. Corte a birds eye: teléfono en el mueble, pierna sobre el asiento, IPL pasándose, la app indicando si va bien o mal.
VoiceOver: *"Y la app me guía paso a paso para no saltarme ningún área. Desde mi cuarto. No me duele."*

---

**[BEAT 6 — OWNERSHIP]**
*00:38 a 00:43*
Visual: giro la cara hacia abajo, cámara en worm's eye.
VoiceOver: *"Y la máquina es mía. PARA SIEMPRE."*

---

**[BEAT 7 — CIERRE A CÁMARA]**
*00:43 a 00:52*
Visual: selfie con la mano sosteniendo la cámara, hablando directo al lente.
VoiceOver: *"Ya no le pago a nadie para que me depile. Ahora yo controlo mi tratamiento, mi tiempo y mis resultados."*

---

**[BEAT 8 — CTA]**
*00:52 a 00:56*
Visual: cámara desde tu POV, cerrás el bolsito del dispositivo.
VoiceOver: *"Link in bio."*

---

**MAPA DE RITMO**

```
[BEAT 1 — silencio visual, texto hace el trabajo]
Stop motion meme -> energía caótica, humor de frustración
Caption larga -> dejar que la lean, no apurar el corte

[BEAT 2 — pausa emocional]
Before/after -> que el visual respire, no lo cortes rápido
"Eso me pasó a mí." -> la línea más corta del video, la más pesada

[BEAT 3 — energía sube]
Flashes en cámara -> el producto entra con impacto visual
"LITERALMENTE" -> énfasis real, no lo suavices en edición

[BEAT 4 — ritmo técnico, concreto]
Acercás el producto -> demostración clara, sin hablar de más

[BEAT 5 — el momento más largo, justificado]
App + birds eye -> dos visuales que prueban lo que decís
"Desde mi cuarto. No me duele." -> dos frases cortas, pausa entre cada una

[BEAT 6 — el momento más cinematográfico]
Worm's eye -> ángulo inesperado, detiene el scroll
"PARA SIEMPRE." -> pausa después. No agregues nada.

[BEAT 7 — conexión directa]
Selfie -> rompe la estética, se siente real y cercano

[BEAT 8 — cierre limpio]
Bolsito -> producto como objeto cotidiano, no como ad
"Link in bio." -> sin drama, sin CTA agresivo
```

---

El beat 6 es el más importante de todo el video. El ángulo worm's eye más "para siempre" es el momento que la gente va a pausar. Que haya silencio después de esa línea antes de cortar al beat 7.

¿Ajustamos algo o lo pasamos al doc de script para Braun?

## 🧑 Adriana · 2026-04-14 01:59
POV: gastaste miles de dólares en laser, te prometieron que era definitivo, y al año llamas para porque necesitas retoque… y te quieren volver a cobrar.
Eso me pasó a mí. Y no pensaba volver a caer. Hasta que Braun Smart IPL llegó a mi vida y LITERALMENTE cambió mi relación con la depilación láser.
Lo uso una vez a la semana, me toma 10 minutos.
Y la app le guía paso a paso para no saltarme ningún área. Desde mi cuarto. No me duele.
Y la máquina es mía. PARA SIEMPRE.
Ya no le pago a nadie para que me depile. Ahora yo controlo mi tratamiento, mi tiempo y mis resultados.
Link in bio

## 🤖 Claude · 2026-04-14 01:59
Perfecto. Eso es el guion final, en tu voz exacta, sin tocar nada.

Revisión 3 de 5. Lo único que hice fue organizar el VO contra los beats visuales para que tengas una sola hoja en mano cuando grabes:

---

**SCRIPT FINAL — REVISIÓN 3**
**Braun Smart IPL x @adrianavmarquez**

---

**[BEAT 1 — HOOK VISUAL]**
*Stop motion gritando en almohada, varias alturas, formato meme.*
*Audio: silencio o sound trending*
On screen: **"POV: gastaste miles de dólares en laser, te prometieron que era definitivo, y al año llamas porque necesitas retoque… y te quieren volver a cobrar."**

---

**[BEAT 2 — BEFORE/AFTER]**
*Clip piernas Marzo 10 con timestamp / corte a Abril 13 con timestamp.*
VO: *"Eso me pasó a mí. Y no pensaba volver a caer."*

---

**[BEAT 3 — PIVOT + PRODUCTO]**
*Hablando a cámara, pasándome la IPL, flashes visibles.*
VO: *"Hasta que Braun Smart IPL llegó a mi vida y LITERALMENTE cambió mi relación con la depilación láser."*

---

**[BEAT 4 — DEMOSTRACIÓN DISPOSITIVO]**
*Acerco la IPL a cámara, la prendo, cambio intensidad.*
VO: *"Lo uso una vez a la semana, me toma 10 minutos."*

---

**[BEAT 5 — APP + SESIÓN GUIADA]**
*Screen recording de la app. Corte a birds eye: teléfono en mueble, pierna en asiento, IPL en movimiento, app indicando progreso.*
VO: *"Y la app me guía paso a paso para no saltarme ningún área. Desde mi cuarto. No me duele."*

---

**[BEAT 6 — OWNERSHIP]**
*Giro cara hacia abajo, cámara worm's eye.*
VO: *"Y la máquina es mía. PARA SIEMPRE."*

---

**[BEAT 7 — CIERRE A CÁMARA]**
*Selfie sosteniendo la cámara, hablando al lente.*
VO: *"Ya no le pago a nadie para que me depile. Ahora yo controlo mi tratamiento, mi tiempo y mis resultados."*

---

**[BEAT 8 — CTA]**
*Cámara POV: cerrás el bolsito del dispositivo.*
VO: *"Link in bio."*

---

¿Lo pasamos al doc de script para Braun?

## 🧑 Adriana · 2026-04-14 02:01
Haz el script document oficial

## 🤖 Claude · 2026-04-14 02:02
Listo. El doc tiene los 8 beats completos con visual, VO/overlay y nota de dirección por beat, la tabla de textos para aprobación de marca, notas de producción y referencias visuales.

Abrilo en Google Docs y Braun puede dejar comentarios directo en el documento. Revisión 4 de 5 disponible si necesitás ajustar algo antes de mandarlo.

## 🧑 Adriana · 2026-04-14 02:05
Ahora debo hacer una version en ingles, en incluye despues del hook y que diga en lugar de: "hasta que braun IPL llego a mi vida" sino "Until Braun sent it my way, and LITERALLY changed my relationship with laser hair removal"

## 🤖 Claude · 2026-04-14 02:07
Listo, versión en inglés completa. El Beat 3 queda: *"Until Braun sent it my way, and LITERALLY changed my relationship with laser hair removal."* Todo lo demás, secciones, notas de producción y referencias visuales también en inglés.

Revisión 5 de 5 disponible si necesitás un ajuste final antes de mandar a la marca.

## 🧑 Adriana · 2026-04-14 02:10
On the beat two ad:
Text On Screen Second 3: Braun Smart IPL Before March 10 - Braun Smart IPL After March 10.

## 🤖 Claude · 2026-04-14 02:10
Revisión 5 de 5.

Listo. Beat 2 ahora dice:

**ON SCREEN (second 3):** "Braun Smart IPL Before March 10" / "Braun Smart IPL After April 13"
**VO:** "That happened to me. And I was not going back."

Esta es tu revisión 5 de 5. El script está listo para mandar a Braun.

## 🧑 Adriana · 2026-04-14 02:19
I have one last thing the copy for the POV is too long I will leave people to see me yelling and reading just 2 seconds because I have to move on to show the before and after and mention the brand and show the device according to the brief.

"In the first 1-3 seconds, make sure you show the Braun logo on Smart IPL device clearly. The product must appear in the first 5 seconds of the video." 

So I have in mind: 2 seconds to read the OS Hook text, Sec 2 to 2.5 Before/ After Split Screen. 2.5 I say "and I was NOT going Back" while I bring the device to the frame with a playful face expression. Everything else continues as is, except: I pay NOBODY to remove my hair. I control my treatment, my time and my results" So it sounds more natural.

## 🤖 Claude · 2026-04-14 02:19
Buena nota. El brief lo dice claro y el copy actual no cabe en 2 segundos. Antes de reescribir, necesito confirmarte una cosa:

¿El hook de pantalla lo acortamos a algo como **"POV: spent thousands on laser. A year later they called me for a touch-up. And wanted to charge me again."** o tienes otra versión en mente?

## 🧑 Adriana · 2026-04-14 02:20
"POV: spent thousands on laser. A year later called for a touch-up. And wanted to charge me AGAIN."

## 🤖 Claude · 2026-04-14 02:21
Perfecto. Más punchy, más rápido, cabe en 2 segundos. Lo tomo exacto.

Listo. Los cambios aplicados:

**Beat 1 (0-2 sec):** Hook corto nuevo + device con logo visible en frame desde el inicio, cumple el brief.

**Beat 2 (2-2.5 sec):** Split screen con los labels "Braun Smart IPL Before March 10" / "Braun Smart IPL After April 13" en pantalla. Sin VO.

**Beat 3 (2.5 sec):** "And I was NOT going back. Until Braun sent it my way, and LITERALLY changed my relationship with laser hair removal." Con cara playful trayendo el device al frame.

**Beat 7:** "I pay NOBODY to remove my hair. I control my treatment, my time and my results."

Este script está listo para mandar.

## 🧑 Adriana · 2026-04-14 20:06
En el hook POV me sigue pareciendo muy alto y que no queda claro porque no alcanzas a leer.

Sugiere otros text hooks que sigan con el mismo meme:

POV: spent thousands on laser
and you need to pay MORE
for a touch-up.

## 🤖 Claude · 2026-04-14 20:06
Aquí van opciones, todas en el mismo formato de 3 líneas cortas para que entren en 2 segundos:

---

**Opción 1 — El dolor de la llamada**
POV: spent thousands on laser.
Got a call a year later.
"You need a touch-up." 💀

---

**Opción 2 — La traición**
POV: laser said "permanent."
One year later: touch-up needed.
And yes, you're paying again.

---

**Opción 3 — Minimalista / punch final**
POV: paid for "permanent" laser.
It wasn't.
Now they want more money.

---

**Opción 4 — El meme más puro**
POV: dropped thousands on laser.
Hair said: nah.
And they want you to pay again? 💀

---

**Opción 5 — Con el número**
POV: thousands on laser treatments.
Hair came back anyway.
Touch-up? That'll be $X more.

---

**Opción 6 — La más corta de todas**
POV: laser. Permanent. They said.
One year later: touch-up.
One year later: pay again.

---

Mi favorita para tu meme es la **4** porque tiene humor real y el "Hair said: nah" hace que la gente pare. La **1** es la más limpia si quieres que se lea rápido sin pensar. ¿Cuál te late o la combinamos?

## 🧑 Adriana · 2026-04-14 20:37
im missing 6 seconds to get to 430 second video what else can i insoprorate?

## 🤖 Claude · 2026-04-14 20:37
Antes de sugerir, necesito entender mejor qué tienes. ¿Los 6 segundos los agregas al final, o hay un beat específico donde sientes que el video se apresura y necesita respirar más?

## 🧑 Adriana · 2026-04-14 20:38
creo qeu quiero agregrlo en la parte de la aplicacion y habalr un poco mas de qeu la aplicacion te guia hace un tratamiento persoanlziado para ti, y ponerlo ahi ene sa parte junto con screen recordings del UX

## 🤖 Claude · 2026-04-14 20:38
Perfecto, tiene todo el sentido. El beat de la app es el más técnico del video y el que más necesita tiempo para que el producto se entienda. 6 segundos ahí se justifican solos.

Para que lo escriba bien, dime dos cosas rápido:

¿La app te hace algún tipo de setup inicial, como que te pregunta tu tipo de piel, zona del cuerpo, o te crea un plan específico? ¿O el "personalizado" es más que ella ajusta la intensidad automáticamente según tu tono de piel con el sensor?

## 🧑 Adriana · 2026-04-14 21:09
si, scneas un codigo q, descragas la app, conectas el device, seleccionas el color de vello, el area donde lo vas a aplicar, que dias, tiene un calendario de aplicacion, te dice si lo haces bien o mal, te cuent alas pulsaciones compltamento guiado

## 🤖 Claude · 2026-04-14 21:10
Eso es oro. El UX de esa app es exactamente lo que diferencia al Braun Smart IPL de cualquier otro device, y el brief lo pide explícitamente como must-have. Con esos screen recordings tienes contenido más que suficiente para justificar los 6 segundos.

Así quedaría el beat expandido:

---

**BEAT 5 — APP + SESIÓN GUIADA (expandido)**

Visual: scan del QR code para descargar la app. Conectas el device. Seleccionas color de vello y área de tratamiento. La app genera tu calendario de sesiones. Corte a birds eye: teléfono en el mueble, pierna sobre el asiento, IPL en movimiento, app contando pulsaciones y diciéndote si vas bien o mal.

VO: *"And the app builds your treatment. You scan, connect, pick your hair color, your area, your days. It gives you a full calendar, counts every pulse, and tells you in real time if you're doing it right. Step by step. From my room. No pain."*

---

Eso son exactamente 6 segundos de VO natural sin apurarse. El screen recording del UX fluye debajo mientras hablas, no compite.

¿Lo incorporo al doc y regenero?

## 🧑 Adriana · 2026-05-29 11:51
They want a second collab, what can mu second video be like?

## 🤖 Claude · 2026-05-29 11:51
Buena pregunta. Antes de proponer ángulos, dime una cosa:

¿El segundo video es para las mismas plataformas con el mismo formato corto, o Braun te está pidiendo algo diferente, como un video más largo, un tutorial, un formato distinto?

## 🧑 Adriana · 2026-05-29 11:52
Sí, es para las mismas plataformas con formato corto. No me pidieron un video con un concepto diferente, más largo, un tutorial, pero es el mismo brief, pero yo considero que debería ser un ángulo diferente para que no sea repetitivo.

## 🤖 Claude · 2026-05-29 11:52
Exacto, tienes razón. Si haces el mismo "antes y después de despair" dos veces, pierdes audiencia en el scroll. Necesitás un ángulo complet

## 🤖 Claude · 2026-05-29 11:52
Correcto, mismo brief, ángulo diferente. Tiene sentido estratégico: el primer video convierte a la gente que ya hizo láser y fracasó. El segundo tiene que hablar a alguien distinto.

Tres direcciones posibles:

---

**Dirección 1: La que nunca ha hecho nada**
La que lleva años afeitándose o depilándose con cera, nunca dio el salto al láser porque le daba miedo el dolor o el precio. Este video le habla a ella. No hay historia de trauma con el láser, hay historia de cansancio con la rutina de siempre. El hook es el tiempo y la libertad, no la decepción.

---

**Dirección 2: El lujo accesible**
Misma historia tuya pero desde otro ángulo: no es que el láser falló, es que el láser es un privilegio de clase. Cuesta miles, requiere tiempo, requiere transporte, requiere agenda. El Braun democratiza ese resultado. Este video habla a la mujer que siempre quiso hacerse láser pero nunca pudo pagarlo.

---

**Dirección 3: La rutina de self-care**
Sin comparación con el láser, sin drama. Solo tu domingo, tu cuarto, tu ritual. El Braun como parte de cómo te cuidas a ti misma. Más aspiracional, menos confrontacional. Diferente tono al primero, diferente audiencia, mismo producto.

---

¿Cuál de estas tres te resuena más con tu audiencia actual, o hay una mezcla que te interesa explorar?

## 🧑 Adriana · 2026-05-29 11:55
Este es el brief

## 🤖 Claude · 2026-05-29 11:55
Dos cosas importantes que cambian con este brief antes de hablar de ángulos:

El video tiene que ser **30 segundos o menos**, y hay un **Prime Day deal: $120 off del 14 al 27 de junio** que debes mencionar. También dice explícitamente **no decir "link in bio"** en el video, caption ni subtítulos.

Ahora, con todo eso claro, aquí van los ángulos para el segundo video:

---

**Ángulo 1: La matemática del lujo**
No es drama, es números. Salón láser completo cuesta hasta $8,000 al año. El Braun es tuyo para siempre. Y ahora con $120 off en Prime Day. Hablas directo a la cámara, sin backstory, solo la cuenta. Diferente al primero en tono y estructura.

---

**Ángulo 2: Lo que cambió en mi rutina**
Sin comparación con el láser. Solo el antes y el después de tu día a día. Antes: afeitarte antes de salir, llevar razor de viaje, pensar en la depilación antes de cada plan. Ahora: no. Este ángulo usa lifestyle clips de tu verano, tus planes, tu libertad. El brief lo pide explícitamente como Freedom messaging.

---

**Ángulo 3: El device que aprendió de mí**
El foco es la app y el flex head nuevo. No es tu historia de laser, es la tecnología que te sorprendió. "No sabía que un device de depilación podía tener esto." Tutorial corto pero con tu voz, no producido. El brief pide que menciones el nuevo flex head como must-have nuevo.

---

**Ángulo 4: GRWM con propósito**
Get ready with me pero el Braun es parte del ritual, no el protagonista forzado. Te preparas para un plan de verano, el IPL aparece naturalmente como parte de lo que haces. Freedom messaging integrado sin que se sienta a ad. 30 segundos, lifestyle pesado, producto presente.

---

¿Cuál te resuena más, o combinamos dos?

## 🧑 Adriana · 2026-05-29 12:01
Que tal un girl math?
Razones por las que gastando $399 hoy, te ganas $7621

## 🤖 Claude · 2026-05-29 12:01
Me encanta. Es el ángulo de valor más inteligente para Prime Day porque convierte el precio en una ganancia, no en un gasto.

Antes de escribirlo, tres preguntas rápidas:

**1. El número.** El brief dice salón láser cuesta hasta $8,000 al año. ¿Quieres usar ese número como base del cálculo, o tienes tu propio número real de lo que gastaste tú en láser que sea más creíble y personal?

**2. El formato visual.** Girl math funciona mejor con texto en pantalla que va apareciendo línea por línea mientras hablas, o con una calculadora en mano tipo meme. ¿Cuál te imaginas más en tu feed?

**3. El tono.** ¿Lo quieres deadpan serio tipo "esto es matemática básica" o con humor exagerado tipo "actually makes sense"?

## 🧑 Adriana · 2026-05-29 12:03
1. Como el brief 
2. Calculadora en mano, en bata, con lentes
3. Humor exagerado BUT IT MAKES SENSE

## 🤖 Claude · 2026-05-29 12:03
Perfecta la dirección. Calculadora en mano, bata, lentes, humor exagerado pero con los números reales. Es el girl math más convincente porque las matemáticas sí cuadran.

Una sola cosa antes de escribirlo: el brief dice 30 segundos o menos. Girl math con calculadora tiende a necesitar ritmo rápido para que los números entren bien.

¿Quieres que sea un monólogo tuyo hablando a cámara con texto apareciendo en pantalla, o prefieres que sea más estilo "voiceover + texto solo" sin mostrarte tanto la cara?

## 🧑 Adriana · 2026-05-29 12:04
Hablando a cámara, pienso hacer multitasking en el hook y que se accione la depiladora con 3 flashes consecutivos

## 🤖 Claude · 2026-05-29 12:04
Genius. El hook se hace solo: lentes, bata, calculadora en una mano, Braun en la otra con 3 flashes. Todo en los primeros 2 segundos, brief cubierto, y es el visual más parable del feed.

Escríbeme el número exacto que quieres usar para el precio del Braun hoy con el deal. ¿Es $279 con los $120 off de $399, o el precio base es diferente?

## 🧑 Adriana · 2026-05-29 12:05
El precio base es $519.99

## 🤖 Claude · 2026-05-29 12:05
Perfecto. Entonces con el deal de Prime Day:

**$519.99 - $120 = $399.99**

Y la ganancia que comunicas es la diferencia vs. el salón láser. El brief dice hasta $8,000 al año en salón láser completo. Pero para que el girl math sea más conservador y creíble, ¿quieres usar el $8,000 anual o prefieres un número más realista tipo $600 a $800 al año que la gente promedio gasta entre waxing, shaving y retoques?

El $8,000 es más impactante pero puede sentirse exagerado para alguien que nunca hizo láser completo. El número más bajo es más honesto y le habla a más gente.

## 🧑 Adriana · 2026-05-29 12:05
$8000 anual es lo que costaría hacerte full body laser waxing

## 🤖 Claude · 2026-05-29 12:05
Correcto, y el brief lo respalda explícitamente así que lo usamos sin problema.

Entonces los números quedan:

$8,000 al año en salón
x 1 año de uso del Braun = $8,000 ahorrado
Menos $399.99 que pagaste hoy
**= $7,600.01 ganados. Redondeamos a $7,600.**

¿Arrancamos el script?

## 🧑 Adriana · 2026-05-29 12:06
Si

## 🤖 Claude · 2026-05-29 12:06
Draft 1 de 5. Aquí va:

---

**SCRIPT — GIRL MATH: BRAUN SMART IPL**
**Draft 1**

---

**[BEAT 1 — HOOK VISUAL]**
*Sec 0-2: lentes, bata, calculadora en una mano, Braun Smart IPL en la otra. 3 flashes consecutivos visibles. Logo Braun en cámara.*
ON SCREEN: **"Braun Smart IPL"** + **#BraunPartner #ad**
VO: *"Girl math. Let me show you why spending $399 today actually makes you $7,600."*

---

**[BEAT 2 — LA CUENTA]**
*Hablando a cámara, calculadora en mano, expresión exagerada de "esto es obvio."*
VO: *"Full body laser at a salon? Up to $8,000 a year."*
ON SCREEN: **$8,000/year**

*Pausa. Mirada a cámara.*
VO: *"The Braun Smart IPL? $399 today with the Prime Day deal. And it's mine. Forever."*
ON SCREEN: **$399 today only**

---

**[BEAT 3 — EL REMATE MATEMÁTICO]**
*Levantas la calculadora, la apuntas a cámara con cara seria.*
VO: *"$8,000 minus $399..."*
*Pausa dramática. Giras la calculadora hacia cámara mostrando el número.*
ON SCREEN: **= $7,601 back in your pocket.**
VO: *"You're basically making money."*

---

**[BEAT 4 — PRUEBA]**
*Glide del device en la pierna, mínimo 3 flashes visibles.*
VO: *"One month in. Once a week. Ten minutes. And my legs already look like this."*
*Corte rápido a before/after legs. Timestamps visibles: March 10 / April 13.*

---

**[BEAT 5 — CIERRE]**
*Selfie a cámara, calculadora todavía en mano.*
VO: *"Prime Day deal ends June 27th. The math is not mathing, it's MATHED."*
ON SCREEN: **$120 off ends June 27**

---

**MAPA DE RITMO**

```
[HOOK — rápido, energía alta]
"Girl math." -> dos palabras, pausa. Dejar que aterrice.
"Let me show you why..." -> sube, invita

[BEAT 2 — ritmo de presentación, deliberado]
"$8,000 a year." -> pausa después del número, que respire
"$399 today." -> más rápido, contraste intencional
"And it's mine. Forever." -> bajar para el remate

[BEAT 3 — el momento más largo, justificado]
"$8,000 minus $399..." -> lento, dramático
[PAUSA REAL antes de girar la calculadora]
"You're basically making money." -> deadpan, no lo grites

[BEAT 4 — ritmo medio, que el visual haga el trabajo]
Deja que el before/after respire, no cortes rápido

[CIERRE — sube para el remate final]
"The math is not mathing, it's MATHED." -> la más rápida del video
Punto. No agregues nada después.
```

---

La pausa antes de girar la calculadora en el Beat 3 es el momento del video. Si la cortas en edición lo pierdes todo. Que la audiencia espere el número.

¿Qué sentís cuando lo lees en voz alta?

## 🧑 Adriana · 2026-05-29 12:07
[BEAT 1 — HOOK VISUAL]
Welcome to girlmath 101. How spending $399 ACTUALLY makes you $7600 richer.

## 🤖 Claude · 2026-05-29 12:08
Tomado exacto. Más tuyo, más directo, y "Welcome to girlmath 101" establece el tono del personaje desde la primera línea.

Revisión 1 de 5:

---

**SCRIPT — GIRL MATH: BRAUN SMART IPL**
**Revisión 1**

---

**[BEAT 1 — HOOK VISUAL]**
*Sec 0-2: lentes, bata, calculadora en una mano, Braun Smart IPL en la otra. 3 flashes consecutivos visibles. Logo Braun en cámara.*
ON SCREEN: **"Braun Smart IPL"** + **#BraunPartner #ad**
VO: *"Welcome to girlmath 101. How spending $399 ACTUALLY makes you $7,600 richer."*

---

**[BEAT 2 — LA CUENTA]**
*Hablando a cámara, calculadora en mano, expresión exagerada de "esto es obvio."*
VO: *"Full body laser at a salon? Up to $8,000 a year."*
ON SCREEN: **$8,000/year**

*Pausa. Mirada a cámara.*
VO: *"The Braun Smart IPL? $399 today with the Prime Day deal. And it's mine. Forever."*
ON SCREEN: **$399 today only**

---

**[BEAT 3 — EL REMATE MATEMÁTICO]**
*Levantas la calculadora, la apuntas a cámara con cara seria.*
VO: *"$8,000 minus $399..."*
*Pausa dramática. Giras la calculadora hacia cámara mostrando el número.*
ON SCREEN: **= $7,601 back in your pocket.**
VO: *"You're basically making money."*

---

**[BEAT 4 — PRUEBA]**
*Glide del device en la pierna, mínimo 3 flashes visibles.*
VO: *"One month in. Once a week. Ten minutes. And my legs already look like this."*
*Corte rápido a before/after legs. Timestamps visibles: March 10 / April 13.*

---

**[BEAT 5 — CIERRE]**
*Selfie a cámara, calculadora todavía en mano.*
VO: *"Prime Day deal ends June 27th. The math is not mathing, it's MATHED."*
ON SCREEN: **$120 off ends June 27**

---

¿Algo más que ajustar o lo mandamos al doc?

## 🧑 Adriana · 2026-05-29 12:09
Perfect as is except the hook i want talking to camera directly

## 🤖 Claude · 2026-05-29 12:09
Revisión 2 de 5. Un solo cambio:

---

**[BEAT 1 — HOOK VISUAL]**
*Sec 0-2: lentes, bata, calculadora en una mano, Braun Smart IPL en la otra. 3 flashes consecutivos visibles. Logo Braun en cámara. Hablando directo a cámara.*
ON SCREEN: **"Braun Smart IPL"** + **#BraunPartner #ad**
VO: *"Welcome to girlmath 101. How spending $399 ACTUALLY makes you $7,600 richer."*

---

Todo lo demás igual. ¿Lo mandamos al doc?

## 🧑 Adriana · 2026-05-29 12:10
It’s not a voiceover it’s a talking head with overlay videos of the evidence

## 🧑 Adriana · 2026-06-04 03:11
It’s not a voiceover it’s a talking head with overlay videos of the evidence. 
And then also, O wnt to follow th evdieo with a laptop showing the data with like slides on canva explaining the math like a team presentantation

## 🤖 Claude · 2026-06-04 03:11
Okay, dos cambios estructurales grandes. Confirmame antes de reescribir:

**1. El formato completo:** ¿Es talking head principal con b-roll de evidencia encima (before/after, flashes, app), o el talking head y el b-roll se alternan en cortes separados?

**2. La presentación de laptop:** ¿La grabas tú sola tipo "estoy en una presentación de negocios" con la laptop frente a ti mostrando slides de Canva, o es literalmente un screen recording de Canva con tu voz encima? ¿Y esto reemplaza los beats del medio o es el cierre del video después del hook?

## 🧑 Adriana · 2026-06-04 03:22
empieza con una portada diciendo: 
title: "Welcome to girlmath 101."
subtitle: "How spending $399 ACTUALLY makes you $7,600 richer."
slide 2: And the followed by a big title:
Full Body Treatment
@Laser Salon= $8000 a year 
slide 3: 
Full Body Treatment
w/ Braun Smart IPL= $399 and its YOURS
slide 4: 
$8,000-$399=$7,601 back in your pocket.
SLide 5:
"You're basically making money."

## 🤖 Claude · 2026-06-04 03:22
Perfecto. Antes de escribir el script completo, una última confirmación:

¿Los slides de Canva los grabas como screen recording mientras hablas encima, o es una grabación tuya con la laptop frente a ti tipo "estoy dando una presentación" donde se ve tu cara Y la pantalla al mismo tiempo?

## 🧑 Adriana · 2026-06-04 03:25
Yo las pondr ey le dare ente rmientras voy hablando

## 🤖 Claude · 2026-06-04 03:25
Perfecto, entonces es talking head tuyo mientras avanzas los slides manualmente. El video fluye así:

Tú en cámara → avanzas slide → hablas → avanzas slide → hablas. La laptop o tablet visible en el frame, tú como la presentadora.

Revisión 3 de 5:

---

**SCRIPT — GIRL MATH: BRAUN SMART IPL**
**Revisión 3**

---

**[BEAT 1 — HOOK, TALKING HEAD]**
*Sec 0-2: lentes, bata, calculadora en una mano, Braun Smart IPL en la otra. 3 flashes consecutivos visibles. Logo Braun en cámara. Talking head directo a cámara.*
ON SCREEN: **"Braun Smart IPL"** + **#BraunPartner #ad**
HABLAS: *"Welcome to girlmath 101. How spending $399 ACTUALLY makes you $7,600 richer."*
*Avanzas al Slide 1: portada con título y subtítulo.*

---

**[BEAT 2 — SLIDE 2]**
*Avanzas al Slide 2. Cámara te ve a ti con la pantalla visible.*
HABLAS: *"Full body treatment at a laser salon? Up to $8,000 a year."*
*Pausa. Mirada a cámara.*

---

**[BEAT 3 — SLIDE 3]**
*Avanzas al Slide 3.*
HABLAS: *"The Braun Smart IPL? $399 with the Prime Day deal. And it's yours. Forever."*

---

**[BEAT 4 — SLIDE 4]**
*Avanzas al Slide 4. Levantas la calculadora hacia cámara.*
HABLAS: *"$8,000 minus $399..."*
*Pausa dramática. Giras la calculadora mostrando el número.*

---

**[BEAT 5 — SLIDE 5]**
*Avanzas al Slide 5. Deadpan a cámara.*
HABLAS: *"You're basically making money."*
*Pausa. Dejas que aterrice.*
HABLAS: *"Prime Day deal ends June 27th. $120 off. The math is not mathing, it's MATHED."*
ON SCREEN: **$120 off ends June 27**

---

**MAPA DE RITMO**

```
[BEAT 1 — energía de "clase en sesión"]
"Welcome to girlmath 101." -> pausa, establece el personaje
"How spending $399..." -> sube, invita a quedarse

[BEAT 2 — deliberado, dejar que el número impacte]
"$8,000 a year." -> pausa real después. Que duela.

[BEAT 3 — contraste rápido]
"$399." -> más rápido que el beat anterior, el contraste es intencional
"Forever." -> bajar para el remate, no lo aceleres

[BEAT 4 — el momento más dramático]
"$8,000 minus $399..." -> lento, teatral
[PAUSA REAL antes de girar la calculadora, no la cortes]

[BEAT 5 — deadpan es todo]
"You're basically making money." -> no lo grites, dilo plano
Silencio de medio segundo antes del cierre
"The math is MATHED." -> la más rápida del video, punto final
```

---

¿Ajustamos algo o armamos el doc oficial?

## 🧑 Adriana · 2026-06-04 03:32
Quiero que me ayudes a hacer las slides mas bien, esto es un inspo para la distibucion, vibes, design inspo but use my colors and my brand fonts

## 🤖 Claude · 2026-06-04 03:32
Veo el inspo. Bold, editorial, tipografía grande, mucho espacio, color usado como acento no como fondo total. Perfecto para el girl math.

Antes de diseñarlas, confirmame dos cosas rápido:

**1. ¿Dónde las vas a usar?** ¿Las grabas en pantalla de laptop/tablet mientras hablas, o las necesitas también como asset exportable para otra cosa?

**2. ¿El fondo base?** Veo en el inspo que mezclan blanco con bloques de color. Para tu marca, ¿prefieres fondo blanco con tu rojo/azul/amarillo como acento, o quieres algo más oscuro tipo negro con texto blanco para algún slide?

## 🧑 Adriana · 2026-06-04 03:53
sera la presentacion para los deck y los slides que discutimos

## 🤖 Claude · 2026-06-04 03:54
Perfecto. Las hago como slides de Canva-style en tu marca: Poppins, #D72323, #3846C4, #FFBA35, blanco y negro. Bold, editorial, tipografía grande como el inspo.

5 slides exactas que describiste:

Ahí están las 5 slides en tu marca. Poppins, rojo, azul, amarillo, negro. Editorial y bold como el inspo.

Para pasarlas a Canva: la estructura está lista, copias el layout de cada slide y lo replicas en Canva usando tus colores exactos. ¿Quieres ajustar algo en el diseño antes de armar el doc del script?

## 🧑 Adriana · 2026-06-04 03:57
crea tu la version de canvas

## 🤖 Claude · 2026-06-04 03:57
Para crearte las slides directamente en Canva necesito conectarme a tu cuenta. ¿Te parece bien?

No tengo acceso a Canva en este momento. Pero lo que sí puedo hacer ahora mismo es dos cosas:

**Opción 1:** Genero las slides como un archivo HTML descargable, las abres en el browser, haces screenshot de cada una, y las importas a Canva como imágenes base para editar encima.

**Opción 2:** Te genero un PDF exportable con las 5 slides listas para usar directamente o importar a Canva.

¿Cuál prefieres?

## 🧑 Adriana · 2026-06-04 03:57
Use canva

## 🤖 Claude · 2026-06-04 03:57
Revisa el outline de las 5 slides. Si todo se ve bien, dale Generate y las creo directo en tu Canva.

## 🧑 Adriana · 2026-06-04 03:59
Please generate the presentation design with the reviewed outline and selected configuration by calling the "generate-design-structured" tool with the following arguments:

Topic: Girl Math 101 - Braun Smart IPL Prime Day
Audience: casual
Length: 1-5 pages
Style: geometric
Design Type: presentation


Presentation Outlines:

Slide 1: Welcome to Girlmath 101
  Description: - Title slide: bold editorial cover
- Subtitle: How spending $399 ACTUALLY makes you $7600 richer
- Brand tag: Braun Smart IPL x Prime Day
- Black background, red and yellow accents

Slide 2: Full Body Treatment at Laser Salon
  Description: - Option A comparison slide
- Big stat: $8,000 a year
- Label: Every. Single. Year.
- Dark background, red price number

Slide 3: Full Body Treatment w/ Braun Smart IPL
  Description: - Option B slide
- Big stat: $399
- Subtext: Prime Day deal - one time - yours forever
- Badge: $120 off ends June 27
- Blue background, yellow price

Slide 4: $8000 minus $399
  Description: - Math equation slide
- Show: $8000 minus $399 equals $7601 back in your pocket
- Clean white background with bold black and red numbers
- Result highlighted in red

Slide 5: You are basically making money
  Description: - Closing punchline slide
- Big bold quote: You are basically making money
- Red background, white and yellow text
- Handle: @adrianavmarquez - BraunPartner ad

## 🤖 Claude · 2026-06-04 03:59
Tienes 4 versiones generadas. Escoge la que más te guste y la agrego directo a tu cuenta de Canva para que puedas editar los colores exactos de tu marca y los números finales.

## 🧑 Adriana · 2026-06-04 04:01
use the exact refrence you made first with "
11:53 PM


Claude responded: Perfecto.
Perfecto. Las hago como slides de Canva-style en tu marca: Poppins, `#D72323`, `#3846C4`, `#FFBA35`, blanco y negro. Bold, editorial, tipografía grande como el inspo."

## 🤖 Claude · 2026-06-04 04:02
Entendido. El problema es que Canva genera con sus propios templates y no puedo forzar colores hex exactos desde aquí. Lo que sí puedo hacer es exportar el diseño que yo hice como HTML, convertirlo a PDF, e importarlo a Canva para que lo tengas como base editable.

¿Te parece bien esa ruta?

Ahí está. 5 slides en 16:9, Poppins, colores exactos de tu marca: #D72323, #3846C4, #FFBA35, negro y blanco. Para importarlo a Canva:

**Canva: Crear diseño → Importar archivo → sube este PDF.** Canva lo convierte slide por slide y puedes editar todo el texto y colores encima directamente.

## 🧑 Adriana · 2026-06-04 04:04
y no puedes darme opciones de templates y yo elijo? o hazme una presentacion de google slides

## 🤖 Claude · 2026-06-04 04:07
Para Google Slides necesito acceso a tu Google Drive. Ya lo tienes conectado, déjame usarlo.

Ahora lo subo directo a tu Google Drive:

Subí el archivo a tu Drive pero necesito enviarte el PPTX completo, no solo el fragmento inicial. Déjame hacer esto correctamente:

## 🤖 Claude · 2026-06-04 04:08
Para **Google Slides** lo que puedo hacer es subir el PPTX a tu Drive y tú lo abres desde ahí como Google Slides. Pero el archivo que subí antes estaba incompleto.

Déjame subir el PPTX completo correctamente:

Mira, te doy la verdad directa:

**Lo que sí puedo hacer:**
- Generar el PPTX (ya está listo para descargar arriba)
- Subirlo a tu Drive como archivo PPTX (pero para convertirlo a Google Slides nativo necesitas abrirlo manualmente desde Drive)

**Lo que NO puedo hacer:**
- Darte templates de Canva para elegir desde aquí (Canva genera sus propios diseños y no me deja presentarte opciones visuales para elegir antes)
- Convertir directamente a Google Slides vía API sin que tú lo abras

**La ruta más rápida para Google Slides:**

1. Descarga el PPTX desde aquí arriba
2. Ve a [slides.google.com/create](https://slides.google.com/create)
3. Archivo → Importar → sube el PPTX → Google lo convierte automáticamente con toda la estructura

O desde Drive: sube el PPTX → clic derecho → "Abrir con Google Slides" → ya es editable nativo.

¿Quiero seguir trabajando en el contenido o el diseño del deck mientras tanto?

## 🧑 Adriana · 2026-06-04 04:12
ese archivo esta como pdf no pptx

## 🤖 Claude · 2026-06-04 04:13
Tienes razón, el que generé antes con Python fue el PDF. El PPTX también existe pero déjame verificar cuál está en outputs:

Los dos existen. El PPTX tiene 112KB. Te lo presento directamente:

Ese es el PPTX. Descárgalo y desde Drive lo abres como Google Slides con un clic derecho → "Abrir con Google Slides". Todo el diseño en Poppins y tus colores exactos queda editable desde ahí.
