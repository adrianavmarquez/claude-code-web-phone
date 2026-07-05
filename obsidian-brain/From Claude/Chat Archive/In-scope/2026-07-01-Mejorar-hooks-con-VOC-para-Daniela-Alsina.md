---
title: "Mejorar hooks con VOC para Daniela Alsina"
source: claude.ai-chat
created: "2026-07-01 20:41"
summary: "**Conversation overview**  Adri (adrianavmarquez) worked with Claude to revise and improve the content hooks for a client named Daniela Alsina, an interior designer based in Miami. The work centered on the 'Mapa de 30 días' Notion page, which contains hooks organized into four weekly themes: kitchens, bathrooms, fireplaces, and patios. The goal was to replace generic hooks with scroll-stopping first lines grounded in VOC (Voice of Customer) principles — hooks that make someone planning a home renovation immediately recognize their own doubt or desire and feel compelled to watch the video.  The conversation involved significant creative iteration. Claude initially proposed hooks framed as direct client quotes (first-person confessions with contradictions), which Adri redirected, clarifying the preferred format: declarative statements with authority and a specific reframe, exemplified by lines like 'Odiar tu cocina no es la única opción' and 'Hay 5 distribuciones posibles en este espacio de 100 metros.' The winning formula became: name the client's pain point or common belief, then flip it with a designer's specific criterion or non-obvious insight. Adri also flagged the need for storytelling energy, not just problem-solution structure, and corrected Claude when hooks felt too uniform in approach. Final deliverables included 16 hooks replacing the originals on the Notion page and a '🧪 Para testear' section added at the bottom with A/B alternatives organized by week and slot. Placeholders with brackets were preserved intentionally for real data (specific square meters, number of decisions, show title) to keep hooks falsifiable.  **Tool knowledge**  Claude used the Notion MCP integration throughout. The `notion-fetch` tool was used with full Notion page URLs (in the format `https://app.notion.com/p/[workspace]/[page-slug]-[page-id]`) to retrieve multiple pages: Daniela's profile, the Mapa de 30 días, Market Research, brand voice, intake form, and post insights. The `notion-update-page` tool with `update_content` command accepted an array of `old_str`/`new_str` pairs to replace all 16 hooks in a single call — this batch replacement approach worked reliably for swapping exact strings. For adding the testing section, `insert_content` with `position: {type: 'end'}` successfully appended content after a horizontal rule divider at the bottom of the page. One important constraint to note: `old_str` values must match the page content exactly, including curved quotation marks and emoji — mismatches will silently fail. Claude fetched several sub-pages using their standalone page IDs (e.g., `3829c084f04181c5af8bc82163f40c8d`) rather than full URLs, and both formats worked interchangeably."
messages: 14
claude_uuid: "db49c00d-221e-46f0-b593-9c1ede41f5ac"
tags: [claude, chat, archive]
---
# Mejorar hooks con VOC para Daniela Alsina

> **Conversation overview**

Adri (adrianavmarquez) worked with Claude to revise and improve the content hooks for a client named Daniela Alsina, an interior designer based in Miami. The work centered on the "Mapa de 30 días" Notion page, which contains hooks organized into four weekly themes: kitchens, bathrooms, fireplaces, and patios. The goal was to replace generic hooks with scroll-stopping first lines grounded in VOC (Voice of Customer) principles — hooks that make someone planning a home renovation immediately recognize their own doubt or desire and feel compelled to watch the video.

The conversation involved significant creative iteration. Claude initially proposed hooks framed as direct client quotes (first-person confessions with contradictions), which Adri redirected, clarifying the preferred format: declarative statements with authority and a specific reframe, exemplified by lines like "Odiar tu cocina no es la única opción" and "Hay 5 distribuciones posibles en este espacio de 100 metros." The winning formula became: name the client's pain point or common belief, then flip it with a designer's specific criterion or non-obvious insight. Adri also flagged the need for storytelling energy, not just problem-solution structure, and corrected Claude when hooks felt too uniform in approach. Final deliverables included 16 hooks replacing the originals on the Notion page and a "🧪 Para testear" section added at the bottom with A/B alternatives organized by week and slot. Placeholders with brackets were preserved intentionally for real data (specific square meters, number of decisions, show title) to keep hooks falsifiable.

**Tool knowledge**

Claude used the Notion MCP integration throughout. The `notion-fetch` tool was used with full Notion page URLs (in the format `https://app.notion.com/p/[workspace]/[page-slug]-[page-id]`) to retrieve multiple pages: Daniela's profile, the Mapa de 30 días, Market Research, brand voice, intake form, and post insights. The `notion-update-page` tool with `update_content` command accepted an array of `old_str`/`new_str` pairs to replace all 16 hooks in a single call — this batch replacement approach worked reliably for swapping exact strings. For adding the testing section, `insert_content` with `position: {type: 'end'}` successfully appended content after a horizontal rule divider at the bottom of the page. One important constraint to note: `old_str` values must match the page content exactly, including curved quotation marks and emoji — mismatches will silently fail. Claude fetched several sub-pages using their standalone page IDs (e.g., `3829c084f04181c5af8bc82163f40c8d`) rather than full URLs, and both formats worked interchangeably.

## 🧑 Adriana · 2026-07-01 20:41
revis ay mejora los hooks con el VOC para daniela alsina: [📋 Daniela Alsina](https://app.notion.com/p/adrianavmarquez/Daniela-Alsina-3829c084f0418157b3b5dad502d29640?source=copy_link)

su pagina de hooks e ideas:

[⭐ Mapa de 30 días](https://app.notion.com/p/adrianavmarquez/Mapa-de-30-d-as-3829c084f041815cb3d2c0f7adb9bbca?source=copy_link)

## 🤖 Claude · 2026-07-01 20:44
Voy a leer las dos páginas para entender el contexto de Daniela y los hooks actuales.

Ahora leo la página principal de Daniela para el contexto y la VOC.

Necesito la VOC real y el tono de marca antes de tocar los hooks. Leo Market Research, Voz de marca e Insights.

Leo los Insights de posts para anclar los hooks en lo que ya funciona.

Ya revisé todo el ecosistema de Daniela (intake, market research, voz de marca, insights y el Mapa de 30 días). Antes de los hooks, un flag honesto y el criterio que apliqué.

**El gap de VOC:** no tengo lenguaje verbatim de la audiencia de Daniela (comentarios, DMs, reviews de clientes reales). Sus insights de posts miden retención/apoyo social, no dolores de cliente. Así que la "voz de cliente" que usé la reconstruí del avatar del intake + los patrones del research: cliente de gama media-alta en Miami, con visión moderna, presupuesto claro, en modo *"estoy descubriendo a quién contratar"*. Los hooks ahora reflejan lo que esa persona **piensa y teme por dentro** (mi espacio no funciona y no sé por qué / no quiero gastar y que se vea pasado de moda / no quiero romper todo / quiero que se vea caro sin gastar de más). Cuando tengas DMs o comentarios reales, esto se afila todavía más y te lo digo abajo dónde.

> *[line redacted — references an out-of-scope venture]*

---

## 🪝 Hooks revisados (VOC aplicada)

**Semana 1 · Cocinas**

1. 🏡 **"Tenían la cocina más linda de la casa y comían parados en el mesón. Este fue el cambio."**
 · Test: "El error que hacía que nadie usara esta cocina (y no era el tamaño)."
 · Test: "Esta familia comía en el sofá teniendo comedor. Mira qué estaba mal."

2. 🎯 **"90 cm. Es la diferencia entre una cocina donde chocas con todos y una donde caben 8 sin estorbarse."**
 · Test: "Si en tu cocina siempre hay alguien en el medio, es por estos 90 cm."

3. 💬 **"En esta obra el cliente quería una isla gigante. Lo convencí de lo contrario, y aquí está el por qué."**
 · Test: "Acabo de tomar una decisión en esta cocina que al cliente le dio miedo. Tenía razón."

4. 🎯 **"Esta cocina tiene [40 mil] likes en Pinterest y un error que la haría imposible de vivir. Así la arreglo."**
 · Test: "Todos guardan esta cocina de Pinterest. Nadie ve el problema que tiene."

**Semana 2 · Baños**

1. 🏡 **"Esto era un render en mi laptop hace 3 meses. Hoy es el baño de alguien."**
 · Test: "Le prometí a esta clienta que su baño se vería igual al render. Mira."

2. 🎯 **"5 formas de que tu baño se vea nuevo sin romper una sola pared (ni pedir permiso al edificio)."**
> *[line redacted — references an out-of-scope venture]*

3. 💬 **"Nunca elijo un material de baño sin tocarlo primero. Esta es la razón, y la aprendí a los golpes."**
 · Test: "La foto miente. Por eso toco cada material antes de ponerlo en tu baño."

4. 🎯 **"Tu baño no es muy pequeño. Está mal distribuido. Diferencia total."**
 · Test: "Un baño pequeño no es el problema. Diseñarlo como si fuera grande, sí."

**Semana 3 · Chimeneas**

1. 🏡 **"Este fireplace parece de [20 mil]. Costó una fracción, y todo está en un solo material."**
 · Test: "Lo que hace que un fireplace se vea caro no es el precio. Es esto."

2. 🎯 **"La paleta que hace que una sala con chimenea se vea bien hoy y en 15 años. Guárdala."**
 · Test: "Esta paleta para sala con chimenea no va a pasar de moda. Te explico por qué."

3. 💬 **"Todos me piden una sala 'acogedora'. Casi ninguno necesita lo que cree que la hace acogedora."**
 · Test: "El 90% me pide lo mismo para su sala. Y casi nunca es lo que le hace falta."

4. 🎯 **"Todos dirían que esta sala está terminada. Yo veo el espacio vacío donde va el fireplace."**
 · Test: "Esta sala se ve completa. Le falta lo único que la haría inolvidable, aquí."

**Semana 4 · Patios**

1. 🏡 **"Este patio era donde se acumulaba lo que nadie usaba. Hoy es donde pasan las tardes."**
 · Test: "De bodega al aire libre a su lugar favorito de la casa. Mismo patio."
 *(Cambié la fórmula "nadie salía/usaba" para que no se repita con el hook 1 de cocinas dentro del mismo ciclo.)*

2. 🎯 **"Lo que vas a ver en todos los patios en 2026, y lo que ya se ve viejo (aunque lo pusiste hace un año)."**
 · Test: "Esto se va a ver en todos los patios en 2026. Y esto ya envejeció."

3. 💬 **"Montar un patio en el orden equivocado te cuesta el doble. Así lo hago yo, pieza por pieza."**
 · Test: "Nadie te muestra el desastre antes de que un patio se vea así. Yo sí."

4. 🎯 **"Ustedes viendo [la serie del momento]. Yo obsesionada con la casa donde la grabaron."**
 · Test: "Todos hablando del final de [serie]. Yo solo pensando en quién diseñó esa casa."

---

**Placeholders que solo tú puedes rellenar (no los inventé a propósito):** los likes reales de Pinterest, el precio/rango real del fireplace, la decisión real de la obra de la cocina, y la serie del momento. Son los datos que hacen el hook falsificable; con un número inventado el hook se cae.

**Dónde una VOC real dispararía esto:** si me pasas 10-15 comentarios o DMs típicos de su audiencia (o los de @betziletrivas, que es su norte exacto), puedo reemplazar mis suposiciones por frases textuales de cliente y los hooks 2 y 4 de cada semana se vuelven quirúrgicos.

¿Quieres que te los deje escritos directo en la sección "🪝 Hooks exactos" del Mapa de 30 días, o los dejamos aquí para que los pegues tú?

## 🧑 Adriana · 2026-07-01 22:23
La 1 no sirve, tiene que ser algo cómo que tenían la cocina con mayor potencial y no les gustaba ni entrar o algo así

## 🤖 Claude · 2026-07-01 22:23
Entendido, la contradicción va por el lado de "el espacio tenía todo para ser el mejor y aun así lo evitaban":

1. 🏡 **"Esta era la cocina con más potencial de la casa. Y no les provocaba ni entrar."**
 · Test: "Tenían la mejor cocina en papel y la evitaban todos los días. Este era el problema."
 · Test: "Una cocina así de linda y nadie quería estar ahí. Mira qué la estaba matando."

Si quieres afinar más el remate, dime hacia dónde: dejarlo abierto en curiosidad (como arriba) o cerrar nombrando el culpable ("...y todo era por la distribución / por la luz / por el flujo"). ¿Te sirve alguna o la seguimos moviendo?

## 🧑 Adriana · 2026-07-01 22:28
> *[line redacted — references an out-of-scope venture]*

## 🤖 Claude · 2026-07-01 22:29
> *[line redacted — references an out-of-scope venture]*

**Duda concreta que da miedo equivocarse (el "oh, eso me pasa a mí"):**
- "Antes de mover el fregadero de tu cocina, mira lo que le pasó a esta."
> *[line redacted — references an out-of-scope venture]*

**La solución no-obvia (el "oh, qué buena idea, no lo había pensado"):**
- "Lo que hizo esta cocina el doble de funcional no fue tumbar una pared."
- "No era el tamaño. Era una sola cosa lo que hacía sentir chiquita esta cocina."
- "Cambiamos algo que no se ve, y ahora la cocina se siente el doble de grande."

**Dónde poner el dinero (el "eso justo me lo estoy preguntando"):**
- "Si tu presupuesto de cocina no alcanza para todo, gasta aquí primero."
- "Ahorramos en lo que nadie nota para gastar en lo único que sí se ve. Mira dónde."

**La duda literal puesta en cámara (mirror directo):**
- "¿Tumbar la pared de la cocina o no? Esta clienta lo dudó un mes. Mira cómo quedó."

> *[line redacted — references an out-of-scope venture]*
> *[line redacted — references an out-of-scope venture]*

> *[line redacted — references an out-of-scope venture]*

Una nota: varias de estas dejan de ser puro "antes y después" y se vuelven "insight con reveal". Eso está bien y hasta rinde mejor, pero el video tiene que **cumplir** lo que promete el hook (regla de promesa = recompensa de sus insights). Si el clip es solo el reveal sin mostrar la decisión, se cae.

¿Cuál dirección te late para que la afinemos, o quieres que arme el resto de hooks de Resultado (baños, patios) con esta misma lógica de "resuelve la duda"?

## 🧑 Adriana · 2026-07-01 22:36
No pero no todas así. Cuenta una historia!!!! VOC remember

## 🤖 Claude · 2026-07-01 22:37
> *[line redacted — references an out-of-scope venture]*

1. 🏡 **"'Odio mi cocina y no sé por qué.' Me dijo eso teniendo la mejor cocina del edificio."**
 · Test: "La clienta me escribió: 'es linda pero no la siento mía'. Así empezó todo."
 · Test: "'No me provoca ni cocinar ahí.' Y era la cocina con más potencial que había visto ese año."
> *[line redacted — references an out-of-scope venture]*

Todas arrancan en un momento real con tensión (tiene la mejor cocina *y aun así* la evita), y la contradicción es la que engancha. La cita textual es el VOC: le estás poniendo en la boca al video lo que el que scrollea siente pero no ha sabido nombrar.

Si te late esta lógica, sigo con los demás hooks de Resultado (baño, patio, fireplace) abriendo cada uno con una frase real de cliente. ¿Te consigo esas citas de tu lado o las propongo yo y tú las ajustas a algo que de verdad te hayan dicho?

## 🧑 Adriana · 2026-07-03 17:15
No por ejemplo:

1. Odiar tu cocina no es la unica opcion. 
2. Hay 5 distribuciones posibles en este espacio de 100 metros.

y asi cosas que inviten que suenen unicas

## 🤖 Claude · 2026-07-03 17:16
Ahí está el ángulo: afirmación con criterio que reencuadra el problema, no cita entre comillas. Nombras el dolor y en la misma línea lo giras con autoridad de diseñadora. Suena único porque solo alguien que sabe distribuir un espacio lo diría.

Cocinas, en esa vena:

1. **"Odiar tu cocina no es la única opción."**
2. **"Hay 5 distribuciones posibles en este espacio de 100 metros. Elegimos la que nadie ve venir."**
3. **"Tu cocina no es fea. Está mal distribuida. No es lo mismo."**
4. **"Ninguna cocina es demasiado pequeña. Está mal aprovechada."**
5. **"Hay una razón por la que nadie se queda en tu cocina. Y no es el tamaño."**
6. **"Mover el fregadero 40 cm le cambió la vida a esta cocina."**
7. **"El 80% de las cocinas que entro tienen el mismo error de flujo."**
8. **"Una isla no siempre es la respuesta. Aquí sí, y por una razón puntual."**
9. **"En una cocina abierta, el error más caro es no cerrar nada."**
10. **"Esta cocina completa cabía en 12 metros. Y sobra espacio."**

Las más fuertes son las que dan número o reencuadran de golpe (1, 2, 5, 7) porque abren el gap solas: *"¿cuáles 5?", "¿cuál es la razón?", "¿mi cocina tiene ese error?"* — y obligan a ver para saber.

Nota: la 2, 6, 7 y 10 llevan dato tuyo (los metros reales, los cm reales, el % que de verdad ves). Con el número real pega; genérico se cae.

¿Sigo con Resultado de baño, fireplace y patio con esta misma fórmula (dolor + reencuadre con criterio), o quieres exprimir más cocinas primero?

## 🧑 Adriana · 2026-07-03 21:00
perfecto, combina todas las opciones y substituye los hooks de es pagina de notion

## 🤖 Claude · 2026-07-03 21:03
Me encanta la fórmula. Voy a llevar las mejores a la página (una por slot, limpio para copiar) y aplicar la misma lógica —dolor + reencuadre con criterio, único— a baños, chimeneas y patios. Primero cargo la herramienta de edición.

Todo cargado. Sustituyo los 16 hooks de la página con las versiones ganadoras (fórmula: creencia común + reencuadre con criterio), respetando el pilar de cada día.

Listo, sustituidos los 16 en la página. Así quedó la sección **🪝 Hooks exactos** del Mapa de 30 días:

**Semana 1 · Cocinas**
1. 🏡 "Odiar tu cocina no es la única opción."
2. 🎯 "Hay 5 distribuciones posibles en este espacio de [100] metros. Te muestro la que nadie ve venir."
3. 💬 "Todos entran a una cocina y ven gabinetes. Yo veo por dónde va a caminar la gente."
4. 🎯 "Ninguna cocina es demasiado pequeña. Está mal aprovechada."

**Semana 2 · Baños**
1. 🏡 "Este baño no necesitaba ser más grande. Necesitaba [3] decisiones."
2. 🎯 "5 maneras de que tu baño se sienta nuevo sin romper una pared ni pedir permiso al edificio."
3. 💬 "Nunca elijo un material de baño por cómo se ve. Lo elijo por cómo envejece."
4. 🎯 "Tu baño no es muy pequeño. Está mal distribuido. No es lo mismo."

**Semana 3 · Chimeneas**
1. 🏡 "No es el fireplace lo que hace cara esta sala. Es dónde lo pusimos."
2. 🎯 "La paleta para una sala con chimenea que se ve bien hoy y en 15 años. Guárdala."
3. 💬 "Todos me piden una sala 'acogedora'. Casi ninguno necesita lo que cree que la hace acogedora."
4. 🎯 "Esta sala se ve terminada. Yo veo el lugar exacto donde le falta un fireplace."

**Semana 4 · Patios**
1. 🏡 "Un patio no es espacio que sobra. Es el cuarto que no estás usando."
2. 🎯 "Lo que vas a ver en todos los patios en 2026, y lo que ya se ve viejo aunque lo pusiste hace un año."
3. 💬 "Montar un patio en el orden equivocado te cuesta el doble. Así lo hago yo, pieza por pieza."
4. 🎯 "Ustedes viendo [la serie del momento]. Yo obsesionada con la casa donde la grabaron."

Dos cosas para que quede redonda:

**Placeholders a rellenar con dato real** (los dejé entre corchetes a propósito, un número inventado mata lo falsificable): los `[100]` metros del espacio real, las `[3]` decisiones del baño, y `[la serie del momento]`.

**Banco de tests para A/B** (no los metí a la página para no ensuciarla, pero son los que sobraron y sirven para testear contra el principal de cada slot):
- Cocina slot 2: "El 80% de las cocinas que entro tienen el mismo error de flujo."
- Cocina slot 4: "Mover el fregadero 40 cm le cambió la vida a esta cocina."
- Baño slot 3: "El material más lindo de tu baño puede ser el peor. Así lo decido yo."
- Fireplace slot 1: "Un fireplace no calienta una sala. La ordena."
- Patio slot 3: "Nadie te muestra el desastre antes de que un patio se vea así. Yo sí."

¿Te armo estos tests como segunda columna dentro de la misma tabla de cada semana, o los dejo aquí como banco aparte?

## 🧑 Adriana · 2026-07-04 04:14
Agrégalo como una sección abajo que diga para testesr

## 🤖 Claude · 2026-07-04 04:15
Hecho. Agregué al final del Mapa de 30 días una sección **🧪 Para testear (alterna contra el principal)**, separada con un divider, con los hooks alternativos organizados por semana y marcando contra qué slot corre cada uno. Queda claro que son la segunda opción para A/B, no reemplazos.

Cuando tengas comentarios o DMs reales de la audiencia de Daniela (o de @betziletrivas), me los pasas y convierto los slots de criterio en frases textuales de cliente para que peguen todavía más duro.
