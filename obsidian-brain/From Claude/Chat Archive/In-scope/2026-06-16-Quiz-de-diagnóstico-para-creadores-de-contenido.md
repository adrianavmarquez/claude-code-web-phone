---
title: "Quiz de diagnóstico para creadores de contenido"
source: claude.ai-chat
created: "2026-06-16 15:41"
summary: "**Conversation Overview**  Adri (adrianavmarquez.com) is building a free diagnostic quiz called 'Video Diagnóstico' under her Creatividad² brand, targeted at content creators and business owners. The project is explicitly separated from a founder-led product called Emergent (V3), and maintaining that distinction was a recurring constraint throughout the conversation. The quiz identifies which of six content creation stages (Estrategia, Pre-producción, Producción, Edición, Distribución, Análisis post-publicación) represents a user's biggest bottleneck, serving dual purposes: giving users an actionable diagnosis while generating aggregate research data to inform Adri's course development.  The conversation progressed through full product development across several layers. First, the quiz architecture was established: a routing question splits users into two tracks (creators/personal brands versus business owners), followed by 12 scored questions per track. Each question uses 4-5 shuffled answer options with hidden scoring (0-3), a 'conchita de mango' trap option that sounds sophisticated but reveals a misunderstanding, and behavioral micromomentos rather than self-diagnosis prompts. The scoring model accumulates friction by stage, with the highest-scoring stage becoming the bottleneck and the next two as improvement areas. Both complete question sets were built, reviewed, and approved through iterative feedback, including Adri pushing back twice on question length (compressed to one-liners), answer order (shuffled so the correct answer never appears first), and answer obviousness (redesigned so the zero-point option doesn't glow). The full funnel UX was then designed across five screens: landing page, quiz experience with two personality break screens, results page with pill-format bucket scores and a social proof distribution curve, email capture page, and a thank-you page with a referral mechanic granting both parties priority access to Creatividad² plus a free planning guide for the sharer.  Adri's working style is block-by-block approval before scaling, moving sequentially through decisions. She thinks in Spanglish and uses Venezuelan slang ('conchitas de mango,' 'deja tu vaina,' 'ladillarse'). She explicitly flagged that her brand voice includes tonal whiplash between serious diagnostic content and irreverent humor, referencing her own neurodivergent energy as a feature of the brand rather than something to manage. She pushed back firmly when Claude suggested softening humor for the business track, establishing that polarizing humor is an intentional audience filter. Key brand assets referenced include emotion blob characters, a Kronos meme, a peach-crossing-finish-line meme labeled 'RECTO FINAL,' brand colors (#D72323 red, #FFBA35 yellow, #3846C4 blue, #F2E9FF lavender), and Poppins Bold typography. Implementation notes flagged include a cold-start problem for the distribution curve (hide percentage until sufficient submissions accumulate), n8n automation for referral tagging and agenda delivery, and Mailerlite auto-segmentation by diagnosed bucket via form tagging. The conversation ended with both question tracks complete and UX fully specced, with the next deliverable identified as the six per-bucket five-minute plan emails."
messages: 38
claude_uuid: "0c323276-64a2-4f30-ba9c-0ef7ed665155"
tags: [claude, chat, archive]
---
# Quiz de diagnóstico para creadores de contenido

> **Conversation Overview**

Adri (adrianavmarquez.com) is building a free diagnostic quiz called "Video Diagnóstico" under her Creatividad² brand, targeted at content creators and business owners. The project is explicitly separated from a founder-led product called Emergent (V3), and maintaining that distinction was a recurring constraint throughout the conversation. The quiz identifies which of six content creation stages (Estrategia, Pre-producción, Producción, Edición, Distribución, Análisis post-publicación) represents a user's biggest bottleneck, serving dual purposes: giving users an actionable diagnosis while generating aggregate research data to inform Adri's course development.

The conversation progressed through full product development across several layers. First, the quiz architecture was established: a routing question splits users into two tracks (creators/personal brands versus business owners), followed by 12 scored questions per track. Each question uses 4-5 shuffled answer options with hidden scoring (0-3), a "conchita de mango" trap option that sounds sophisticated but reveals a misunderstanding, and behavioral micromomentos rather than self-diagnosis prompts. The scoring model accumulates friction by stage, with the highest-scoring stage becoming the bottleneck and the next two as improvement areas. Both complete question sets were built, reviewed, and approved through iterative feedback, including Adri pushing back twice on question length (compressed to one-liners), answer order (shuffled so the correct answer never appears first), and answer obviousness (redesigned so the zero-point option doesn't glow). The full funnel UX was then designed across five screens: landing page, quiz experience with two personality break screens, results page with pill-format bucket scores and a social proof distribution curve, email capture page, and a thank-you page with a referral mechanic granting both parties priority access to Creatividad² plus a free planning guide for the sharer.

Adri's working style is block-by-block approval before scaling, moving sequentially through decisions. She thinks in Spanglish and uses Venezuelan slang ("conchitas de mango," "deja tu vaina," "ladillarse"). She explicitly flagged that her brand voice includes tonal whiplash between serious diagnostic content and irreverent humor, referencing her own neurodivergent energy as a feature of the brand rather than something to manage. She pushed back firmly when Claude suggested softening humor for the business track, establishing that polarizing humor is an intentional audience filter. Key brand assets referenced include emotion blob characters, a Kronos meme, a peach-crossing-finish-line meme labeled "RECTO FINAL," brand colors (#D72323 red, #FFBA35 yellow, #3846C4 blue, #F2E9FF lavender), and Poppins Bold typography. Implementation notes flagged include a cold-start problem for the distribution curve (hide percentage until sufficient submissions accumulate), n8n automation for referral tagging and agenda delivery, and Mailerlite auto-segmentation by diagnosed bucket via form tagging. The conversation ended with both question tracks complete and UX fully specced, with the next deliverable identified as the six per-bucket five-minute plan emails.

## 🧑 Adriana · 2026-06-16 15:41
VIDEO DIAGNÓSTICO · Creator / Business Separado del V3 Emergent (founder-led). No mezclar el norte de los dos. Este le habla directo al dolor del creador.
IDEA Un quiz gratuito que funciona como identificador automático de problemas: le dice a cualquier creador, marca personal o negocio en cuál de las 6 etapas de su creación de contenido se está cayendo. El usuario sale sabiendo su cuello de botella y el primer paso para arreglarlo. Adri sale sabiendo, en agregado, cuál es la mayor necesidad de su audiencia. Las 6 etapas: Estrategia, Pre-producción, Producción, Edición, Distribución, Análisis post-publicación.
PITCH Un quiz gratis que le dice a cualquier creador en cuál de las 6 etapas de su contenido se está cayendo. A él le resuelve dónde enfocar. A Adri le dice exactamente qué enseñar.
OBJETIVO (el flywheel)

1. Para el usuario: diagnóstico gratis + primer paso accionable. Razón concreta para completarlo.
2. Para Adri (research): cada submission registra la etapa diagnosticada. En agregado, ve el cuello de botella #1 de su audiencia. Eso dicta qué módulos desarrollar MÁS en el curso Creatividad² y qué videos de tips hacer MÁS.
3. Lead gen + retroalimentación: los videos de tips (con open loop "comenta qué se te dificulta y te ayudo") mandan gente al quiz, el quiz genera más submissions y más data, y el ciclo se alimenta solo.
DATA Stat de validación (originada en la investigación del V3, sirve de fundamento): construir sin validar tiene ~30-45% de probabilidad de fracaso; validar la necesidad antes lo baja a ~10-15%. Caveats: la gente dice que compraría pero al pagar cambia; preguntas mal formuladas dan falsa seguridad por sesgo de confirmación; lo que más valida es un MVP con interacciones reales, no solo la encuesta. Pendiente: sourcear un dato propio de contenido (ej. % de creadores que no sabe en qué etapa falla) con fuente creíble.
DESARROLLO DEL QUIZ Las 6 etapas, qué diagnostica cada una y señales de fallo:

1. Estrategia: POV, pilares, claridad de mensaje, conocer a la audiencia. Falla: contenido sin dirección, no sabe para quién habla, copia tendencias sin criterio.
2. Pre-producción: ideación, guión, hook, planificación. Falla: improvisa, no guioniza, hooks débiles.
3. Producción: grabación, luz, audio, encuadre, b-roll. Falla: mala luz o audio, una sola toma, sin b-roll.
4. Edición: ritmo, cortes, subtítulos, retención. Falla: edición sin ritmo, sin subtítulos, no entiende retención.
5. Distribución: formato por plataforma, caption, timing, SEO semántico. Falla: postea igual en todas, caption flojo, no adapta ni usa SEO.
6. Análisis post-publicación: leer métricas (saves, watch time, shares), iterar. Falla: no mira data, mide likes en vez de saves y retención, no itera.
Mecánica:

* 10 a 15 preguntas, cada una pesa hacia una o más etapas.
* Scoring: se acumula por etapa. La etapa con mayor fricción es el cuello de botella.
* Resultado: "Tu cuello de botella está en [etapa]. Esto es lo que pasa y este es tu primer paso."
* Ruteo: cada resultado manda al contenido u oferta de Creatividad² de esa etapa, invita a la serie de tips de esa etapa, y captura el correo con un incentivo.
* Captura de data: cada submission loguea la etapa diagnosticada para el agregado de research.
HOOK (punto de partida, sin pulir) Carril beneficio: "Si tu contenido no despega, el problema está en una de seis etapas. Este quiz te dice en cuál."
PENDIENTES / DECISIONES ABIERTAS

* ¿El quiz del diagnóstico es el MISMO que se construye en Emergent en V3, o uno distinto? Probablemente el mismo, dos ángulos. Confirmar.
* Pulir el hook (carril beneficio).
* Sourcear un dato propio de contenido con fuente creíble.
* Definir el incentivo de captura (descuento, recurso, etc.).
* Registro Creator/Business-led, NO founder-led.

## 🤖 Claude · 2026-06-16 15:43
El quiz tiene un agujero de diseño que se come tu research antes de recogerlo. Si las preguntas miden lo que el creador CREE que falla en vez de lo que su contenido demuestra, terminas con un agregado de percepciones, no de cuellos de botella reales. Y esas dos cosas casi nunca coinciden.

Ese desfase es el activo más grande del proyecto. El creador que fracasa culpa a lo visible y comprable: la cámara, la luz, la edición sin ritmo. El problema real suele estar más arriba, en Estrategia, donde no hay gear que comprar ni atajo de CapCut. Si diseñas las preguntas con señales de comportamiento ("¿tu último video tenía subtítulos?", "¿escribiste el hook antes de grabar o improvisaste?") en lugar de autoevaluación ("¿crees que editas bien?"), capturas dos cosas a la vez: la etapa que SIENTEN rota, que te dice qué vender, y la etapa que ESTÁ rota, que te dice qué enseñar. Cuando el agregado muestre que la gente culpa a Producción y Edición mientras se cae en Estrategia, ahí tienes una pieza de contenido que nadie más puede publicar porque la data es tuya.

Sobre tus pendientes:

**Mismo quiz que V3 o distinto.** Mismo motor, dos carrocerías, dos bases de datos separadas. Las 6 etapas son universales, un founder y un creador pasan por el mismo flujo de producción, así que la lógica de diagnóstico se comparte sin problema. Lo que no se puede compartir es el pool de submissions. Si founders y creadores caen en la misma tabla, tu agregado para decidir qué módulos de Creatividad² desarrollar queda contaminado con una población que no es tu cliente. Ahí se te mezcla el norte, no en el copy sino en la capa de data, que es peor porque no se ve. Taggea cada submission por fuente de entrada, mantén instancias separadas, y rutea distinto: founder a Emergent, creador a Creatividad².

**Incentivo de captura.** No inventes un soborno aparte. El incentivo es el resultado mismo. En pantalla le das el nombre de su etapa, el diagnóstico crudo. La profundidad (el porqué, el primer paso, el mini recurso de esa etapa) llega por correo. El email se vuelve el canal de entrega del resultado que ya quería, y eso convierte mejor que cualquier descarga genérica porque no se siente como peaje. Bonus estructural: cada correo entra ya segmentado por etapa, lo que te arma la lista de Mailerlite por cuello de botella sin trabajo extra. Un descuento de Creatividad² en este punto es prematuro y huele a venta antes de tiempo.

**El dato propio.** El stat exacto que quieres ("% de creadores que no sabe en qué etapa falla") no existe limpio en investigación creíble. Si lo busco, lo más probable es que salga de un blog de marketing reciclado, justo la fuente que no te sirve. La jugada es fabricarlo, no pedirlo prestado. Después de X submissions publicas "El 41% de los creadores que tomó el quiz se cae en [etapa]" contigo como fuente. Más creíble y más tuyo que cualquier número ajeno, y nadie más puede decirlo. Arrancas usando el dato de validación que ya tienes (construir sin validar, 30-45% vs 10-15%) como el fundamento de por qué el quiz existe, y dejas que la herramienta genere el titular con el tiempo. Si aun así quieres un número de relleno para el lanzamiento, te busco adyacentes creíbles, pero te recomiendo no anclar tu autoridad ahí.

**El hook.** El que tienes funciona, pero "no despega" lo afloja. Conviene un pase enfocado en lugar de tirarte una versión a medias aquí. Como dirección: el carril beneficio gana cuando prometes que en dos minutos sabes exactamente dónde se rompe tu contenido, en vez de en cuál de seis casillas genéricas caes.

¿Por dónde entramos primero, el diseño de las 10-15 preguntas, que es lo que decide la calidad de toda tu data, o el pase de hook?

## 🧑 Adriana · 2026-06-19 01:00
aca quiero desarollar primero el quiz, despues pensamos en el video para promovomerlo

## 🤖 Claude · 2026-06-19 01:02
Antes de escribir una sola pregunta hay que cerrar el modelo de scoring, porque eso es lo que separa un diagnóstico que mueve la aguja de un quiz de Buzzfeed que reparte etiquetas bonitas. La pregunta de fondo: cuando alguien tiene fricción en varias etapas a la vez, y casi todos la van a tener, ¿cuál le declaras como su cuello de botella?

Mi recomendación: el cuello de botella es la etapa más temprana que se rompe, no la que acumula más fricción.

Las 6 etapas son secuenciales y dependientes, una falla arriba envenena todo lo de abajo. Editar con ritmo perfecto un video que no sabe para quién es no arregla nada. Entonces el modelo apunta al primer eslabón roto de la cadena, ahí está el verdadero punto de palanca. Para tu research es perfecto: el agregado te dice dónde arranca la cascada para la mayoría de tu audiencia, que es exactamente lo primero que tienes que enseñar.

Ejemplo concreto: alguien marca las dos señales rotas en Estrategia (no sabe para quién habla, copia tendencias sin criterio) y también dos en Edición. Un modelo que suma fricción te tira un empate o una moneda al aire. El modelo en cascada le dice Estrategia sin dudar, porque ese es el arreglo que desbloquea todo lo de abajo.

Cómo queda el esqueleto:

**Una pregunta de gut al inicio.** Antes de mostrar el framework, le preguntas qué parte de hacer contenido se le hace más cuesta arriba, en lenguaje normal, sin nombrar las 6 etapas. Esa respuesta sin contaminar es tu medición de la etapa que SIENTEN rota. El gap entre eso y el diagnóstico real es el oro, vas a poder publicar "el creador jura que su problema es la edición, casi siempre es el POV".

**12 preguntas de comportamiento, dos por etapa.** Nunca nombran la etapa ni usan lenguaje clínico. Miden lo que el creador HACE, no lo que cree. Ejemplo: "¿tu último reel tenía subtítulos?" en vez de "¿editas bien?". Una sola señal por etapa es ruido, dos te dejan triangular.

**Scoring.** Cada pregunta puntúa 0, 1 o 2 hacia su etapa (sólido, a medias, roto). Cada etapa llega máximo a 4. Una etapa se rompe en 3 o más. El cuello de botella es la etapa más temprana que cruza ese umbral. Si ninguna lo cruza, gana la de mayor puntaje.

**El reveal cierra el loop.** Le das el nombre de su etapa, el porqué en una línea, el primer paso accionable, lo ruteas al contenido u oferta de esa etapa, y capturas el correo para mandarle la profundidad. Cada submission loguea tres cosas: respuesta de gut, diagnóstico real, y el puntaje por etapa. Esa es tu tabla de research.

El único fork que cambia cómo escribo cada pregunta es el modelo de scoring. Si le das luz verde a la cascada con umbral, el próximo bloque son las 12 preguntas con su mapeo y sus tres respuestas cada una. ¿Vamos con eso?

## 🧑 Adriana · 2026-06-19 01:16
la idea no es que el mismo usuario diga: esto es mi fallo es Estrategia: POV, pilares, claridad de mensaje, conocer a la audiencia. Falla: contenido sin dirección, no sabe para quién habla, copia tendencias sin criterio.

1. Pre-producción: ideación, guión, hook, planificación. Falla: improvisa, no guioniza, hooks débiles.
2. Producción: grabación, luz, audio, encuadre, b-roll. Falla: mala luz o audio, una sola toma, sin b-roll.
3. Edición: ritmo, cortes, subtítulos, retención. Falla: edición sin ritmo, sin subtítulos, no entiende retención.
4. Distribución: formato por plataforma, caption, timing, SEO semántico. Falla: postea igual en todas, caption flojo, no adapta ni usa SEO.
5. Análisis post-publicación: leer métricas (saves, watch time, shares), iterar. Falla: no mira data, mide likes en vez de saves y retención, no itera. 

La idea es que ideemos uan serie de pregutnas con micromomentos que los van categorizando y van acumulando puntos para el scoring Scoring: se acumula por etapa. La etapa con mayor fricción es el cuello de botella.

Seria ideal poner el cuello de botella y 2 areas de mejora.

## 🤖 Claude · 2026-06-19 01:18
Claro, el usuario nunca ve las 6 etapas ni se pone una etiqueta. Las preguntas hacen el trabajo sucio por debajo y él solo vive el micromomento. Corto la pregunta de gut que te propuse antes, esa te obligaba a que se autodiagnosticara, justo lo que no quieres.

Sobre el scoring, voy con tu modelo: acumulación por etapa, la de mayor fricción es el cuello de botella, y le mostramos ese cuello más las 2 etapas que le siguen en puntaje como áreas de mejora. Lo único que le agrego es una regla para los empates, porque con acumulación van a pasar seguido: si dos etapas quedan iguales, gana la más temprana en la cadena. Arreglar Estrategia antes que Edición siempre es el consejo correcto.

La arquitectura de cada pregunta:

Cada pregunta es un micromomento concreto, una escena que el creador reconoce al instante. Tres respuestas, una por nivel: sólido (0 puntos), a medias (1), roto (2). Cada pregunta mide una sola etapa, y van dos preguntas por etapa para triangular. Doce preguntas en total, estirables a quince si alguna etapa necesita una tercera señal.

El truco que hace que el quiz se sienta inteligente está en la opción de en medio: la que suena bien pero delata que no entiende. El que contesta "me enfoco en que la edición se vea bonita, transiciones, color" cree que va bien, y ahí mismo te dice que prioriza estética por encima de retención.

Tres ejemplos para que sientas el tono, uno del inicio de la cadena, uno del medio y uno del final:

**Estrategia.** Alguien que te acaba de conocer te pregunta de qué va tu cuenta. Respondes:
- En una frase digo exacto para quién es y qué se llevan. (0)
- Doy una explicación larga que cambia según el día. (1)
- Algo como "subo de varias cosas, lifestyle, tips, lo que me inspire". (2)

**Edición.** Terminaste de grabar. En la edición se te va más el tiempo en:
- Cortar para que no haya un segundo muerto y enganche hasta el final. (0)
- Que se vea bonito: transiciones, color, que quede estético. (1)
- Junto los clips, les pongo música y subo. (2)

**Análisis.** Pasaron 48 horas desde que publicaste. Lo que haces:
- Reviso saves, watch time y shares, y saco la conclusión para el próximo. (0)
- Veo cuántos likes y comentarios juntó. (1)
- Ya ando en el siguiente, no reviso mucho. (2)

Si te cuadra el formato (micromomento más tres niveles, dos preguntas por etapa), te armo las 12 completas con su mapeo y dejo señalada la opción de en medio de cada una para que veas qué trampa esconde. ¿Le seguimos así?

## 🧑 Adriana · 2026-06-19 01:31
primera pregunta debe ser si son un negocio o una marca personal eso cambia por completo laspreguntas

## 🤖 Claude · 2026-06-19 01:32
De acuerdo. Esa pregunta es un router, no entra al scoring: va antes de las 12 y no suma puntos, solo decide por cuál set de micromomentos pasa la persona. Las 6 etapas y la lógica de acumulación son idénticas en los dos caminos, lo único que se reescribe es la escena de cada pregunta. Una marca personal piensa "yo grabo, yo edito". Un negocio piensa "quién me produce esto, mi equipo, mi agencia". El mismo cuello de botella se ve distinto según quién mueve las manos.

Lo que ganas con esto va más allá de preguntas afinadas: tu research se vuelve bidimensional. Antes ibas a ver la etapa donde se cae tu audiencia. Ahora la ves cortada por creador y por negocio. Eso mapea directo a tus dos tipos de cliente, el creador early-stage y la marca ya montada que necesita estructura. El agregado te dice qué enseñar y a quién, que es justo la decisión pendiente con los módulos de Creatividad².

Un detalle de la pregunta router. "Negocio o marca personal" tiene un medio borroso, porque casi toda marca personal también es un negocio, tú misma eres el ejemplo. Si los haces elegir en seco, dudan. La forma limpia los ordena por quién es la cara del contenido:

Para empezar, ¿qué estás creciendo con tu contenido?
- Mi marca personal. Yo soy la cara, la gente me sigue a mí.
- Un negocio o producto. La marca no soy yo, aunque yo la maneje.

Así alguien como tú cae en marca personal sin pensarlo, y una cuenta de marca cae del otro lado. Esto vive dentro del quiz creator/business y no toca el norte founder-led del V3, esos siguen separados.

Para el build: dos tracks de 12, mismo motor. Arranco por el de marca personal, que es el grueso de tu audiencia y tu Cliente A, lo dejamos cerrado, y después lo espejeo al track de negocio reescribiendo solo las escenas. ¿Le doy a las 12 de marca personal con esta pregunta router arriba?

## 🧑 Adriana · 2026-06-19 01:34
ok perfecto. 
las preguntas diria yo que tienen un difurcacion a aprtir de esto hay 12 preguntas para cliente a y 12 preguntas para el cliente b

## 🤖 Claude · 2026-06-19 01:36
Listo, aquí están las 12 del track de marca personal. Van agrupadas por etapa para que veas el mapeo, pero en el quiz vivo se barajan para que el usuario no detecte el patrón ni intente gamear el resultado. La opción de en medio siempre es la trampa, la que suena razonable y delata el malentendido.

**ESTRATEGIA**

1. Alguien que te acaba de conocer te pregunta de qué va tu cuenta. Respondes:
- En una frase digo exacto para quién es y qué se llevan. (0)
- Doy una explicación larga que cambia según el día. (1) (cree que ser detallado es tener claridad, la inconsistencia delata que no hay POV fijo)
- Algo como "subo de varias cosas, lifestyle, tips, lo que me inspire". (2)

2. Sale un trend que está reventando. Tu primer instinto:
- Veo si encaja con mi mensaje, y si no, lo dejo pasar aunque esté pegando. (0)
- Lo adapto rápido para no quedarme afuera y después veo si pegó con mi gente. (1) (adaptar trends suena ágil, pero el instinto sigue siendo perseguir, no filtrar)
- Lo hago igual que todos, si funciona algo hará. (2)

**PRE-PRODUCCIÓN**

3. Vas a grabar ahorita. Antes de prender la cámara tienes:
- El hook escrito y la estructura, sé cómo abre y cómo cierra. (0)
- Una idea clara en la cabeza, lo resuelvo mientras grabo. (1) (tener la idea clara se siente preparado, sin hook escrito las aperturas salen débiles)
- Prendo y veo qué sale, después le busco. (2)

4. Piensa en tu último video. Los primeros 3 segundos:
- Los escribí para frenar el scroll, sé con qué abre. (0)
- Abren con una intro tipo "hola, hoy les voy a hablar de...". (1) (parece una apertura normal y educada, es justo lo que mata el scroll)
- No los pensé, empieza donde empezó la grabación. (2)

**PRODUCCIÓN**

5. Grabas un talking head. Tu setup normal:
- Pienso luz y audio antes que nada. (0)
- Busco buena luz natural, el audio es el del teléfono. (1) (la buena luz da sensación de producción, ignorar el audio se la come)
- Una toma, donde esté, con lo que haya. (2)

6. Cuando grabas, ¿cuántas tomas distintas terminas teniendo?
- Varias: el talking head, planos de detalle, b-roll para que respire. (0)
- La principal y un par de cosas que grabé por si acaso. (1) ("por si acaso" se siente cubierto, no hay b-roll pensado)
- Una sola, de corrido. (2)

**EDICIÓN**

7. Terminaste de grabar. En la edición se te va más el tiempo en:
- Cortar para que no haya un segundo muerto y enganche hasta el final. (0)
- Que se vea bonito: transiciones, color, que quede estético. (1) (prioriza estética por encima de retención)
- Junto los clips, les pongo música y subo. (2)

8. Tus videos llevan subtítulos:
- Siempre, y los edito para que marquen el ritmo. (0)
- A veces, depende del video o de si tengo tiempo. (1) ("a veces" se siente flexible, la inconsistencia cuesta retención)
- Casi nunca, se entiende con el audio. (2)

**DISTRIBUCIÓN**

9. Ya tienes el video listo. Cómo lo subes a tus plataformas:
- Adapto formato y caption por plataforma, pensando en qué lo hace buscable. (0)
- El mismo video en todas, le cambio el caption a veces. (1) (cambiar el caption a ratos se siente esfuerzo, no hay adaptación real)
- Exporto una vez y subo igualito a todas, mismo caption. (2)

10. Cuando escribes el caption, lo haces para:
- Que diga algo solo y que tenga las palabras que mi gente busca. (0)
- Acompañar el video con una frase, un emoji y los hashtags. (1) (suena a "sí hago captions", es relleno sin SEO semántico)
- Pongo cualquier cosa rápido o lo dejo casi vacío. (2)

**ANÁLISIS POST-PUBLICACIÓN**

11. Pasaron 48 horas desde que publicaste. Lo que haces:
- Reviso saves, watch time y shares, y saco la conclusión para el próximo. (0)
- Veo cuántos likes y comentarios juntó. (1) (mide las métricas de vanidad, no las que predicen alcance)
- Ya ando en el siguiente, no reviso mucho. (2)

12. Un video se te fue mucho mejor que el resto. Lo que pasa después:
- Identifico qué lo hizo jalar y lo repito a propósito. (0)
- Me alegro, me da gasolina para seguir subiendo. (1) (respuesta emocional, no extrae el porqué para replicarlo)
- Pienso que fue suerte del algoritmo y sigo igual. (2)

Cada par suma de 0 a 4 por etapa. La de mayor puntaje es el cuello de botella, las dos que siguen son las áreas de mejora, y en empate gana la más temprana en la cadena.

El siguiente bloque lógico son las 6 pantallas de resultado de este track: nombre del cuello de botella, el porqué en una línea, el primer paso accionable, y a dónde lo ruteas. ¿Sigo con esas o prefieres que primero espeje las 12 al track de negocio?

## 🧑 Adriana · 2026-06-19 02:13
creo que las respuestas que categorizan a las personas en puntaje 0 e smuy obvio de que es la respuesta correcta, la idea es que no sea tan obvio que sean preguntas mas psicologicas podemos incluir 4-5 opciones por pregunta que sean como decimos en venezuela conchitas de mango

## 🤖 Claude · 2026-06-19 02:14
Tienes razón, el (0) brilla. Cualquiera que haya visto dos reels de consejos huele cuál es la respuesta de "creador que sí sabe" y la marca aunque no sea él. Eso te llena la data de gente actuando el resultado que quiere en vez del que es.

El arreglo son cuatro reglas:

1. Cinco opciones por pregunta, con puntaje escondido y orden barajado, para que ninguna se lea como la obvia.
2. La respuesta sólida se escribe en seco, sin vocabulario de best practice. En vez de "escribo el hook para frenar el scroll", dice algo plano y hasta humilde que solo le suena propio a quien de verdad lo hace.
3. Metes mínimo una conchita de mango: la opción que suena más aplicada o más lista, y que justo por eso puntúa peor. Atrapa al que consume consejos y los repite pero no los ejecuta.
4. Ninguna opción es un strawman. Las cinco son cosas que una persona real diría sin pena. La que de verdad es la persona delata su nivel sin que se sienta juzgada.

Dos preguntas reconstruidas con el modelo nuevo. Los puntajes van entre paréntesis solo para ti, el usuario no los ve:

**Estrategia.** Alguien que te acaba de conocer te pregunta de qué va tu cuenta. Lo que te sale:
- Le suelto la frase de siempre, la tengo tan repetida que ya hasta me aburre. (0)
- Le digo que hago contenido de lo mío y ya, sin mucho rollo. (1)
- Depende de quién pregunte, le acomodo la respuesta a la persona. (2)
- Le explico con contexto, en una frase no le hago justicia a todo lo que toco. (3)
- Le mando que me siga mejor, que ahí lo va a entender. (3)

La conchita: "le acomodo la respuesta a la persona" suena a inteligencia social, y delata que no hay mensaje fijo, cambia de forma según quién pregunte. La sólida es la primera, escondida detrás de un "me aburre" que solo dice quien ya tiene su POV clavado.

**Pre-producción.** Piensa en tu último video. Sus primeros segundos salieron de:
- Lo pensé un rato, sabía con qué quería abrir antes de grabar. (0)
- Grabé varias aperturas y me quedé con la que sentí más fuerte. (1)
- Una frase que se me ocurrió y me pareció que pegaba, la puse de una. (2)
- Empecé presentándome, un saludito para que sepan quién soy. (3)
- Ni me acuerdo, salió como salió. (3)

La conchita aquí es "grabé varias aperturas y me quedé con la más fuerte". Se ve diligente, casi más trabajadora que la sólida, pero es selección por vibra sin saber por qué jala, así que puntúa peor que el plano "sabía con qué abrir".

Si te cuadra este nivel de disimulo, reconstruyo las 12 enteras así, cinco opciones cada una con su conchita marcada. ¿Le doy?

## 🧑 Adriana · 2026-06-19 03:03
sip 12 para creadores de contenido/ marca personal y otras 12 para duenos de negocios/ empresas/ productos son dos personas diferentes

## 🤖 Claude · 2026-06-19 03:06
Aquí van las 24 completas con el modelo nuevo. Los (puntajes) y las marcas de conchita son solo para ti, el usuario no los ve, y en el quiz vivo las opciones van barajadas.

## TRACK A · CREADOR / MARCA PERSONAL

**ESTRATEGIA**

1. Alguien que te acaba de conocer te pregunta de qué va tu cuenta. Lo que te sale:
- Le suelto la frase de siempre, la tengo tan repetida que ya hasta me aburre. (0)
- Le digo que hago contenido de lo mío y ya, sin mucho rollo. (1)
- Depende de quién pregunte, le acomodo la respuesta a la persona. (2, conchita)
- Le explico con contexto, en una frase no le hago justicia a todo lo que toco. (3)
- Le mando que me siga mejor, que ahí lo va a entender. (3)

2. Ves a alguien de tu nicho explotar con un formato. Por dentro piensas:
- Qué bueno por esa persona, ya tengo claro lo mío y no va por ahí. (0)
- Interesante, lo anoto por si encaja con algo que yo haría. (1)
- Lo pruebo yo también rápido, si le funcionó algo tendrá. (2, conchita)
- Me da ansiedad sentir que me estoy quedando atrás. (3)
- Me pongo a estudiarlo y termino pareciéndome cada vez más. (3)

**PRE-PRODUCCIÓN**

3. Piensa en tu último video. Sus primeros segundos salieron de:
- Lo pensé un rato, sabía con qué quería abrir antes de grabar. (0)
- Grabé varias aperturas y me quedé con la que sentí más fuerte. (1, conchita)
- Una frase que se me ocurrió y me pareció que pegaba, la puse de una. (2)
- Empecé presentándome, un saludito para que sepan quién soy. (3)
- Ni me acuerdo, salió como salió. (3)

4. Te sientas a crear. Tu forma de trabajar:
- Tengo un banco de ideas y guiones a medio hacer, escojo de ahí. (0)
- Cuando me llega la inspiración grabo varias seguidas para aprovechar. (1, conchita)
- Abro la cámara y veo qué tengo ganas de decir hoy. (2)
- Espero a que se me ocurra algo bueno y ahí me muevo. (3)
- Casi siempre replico algo que vi funcionando. (3)

**PRODUCCIÓN**

5. Vas a grabar en cámara. Lo primero que resuelves:
- Dónde me da la luz y que el audio entre limpio, lo demás después. (0)
- Que el fondo se vea ordenado y estético. (1, conchita)
- Me pongo donde haya luz natural y le doy. (2)
- Donde me agarre el momento, si espero se me va la idea. (3)
- Grabo y ya, no le pienso al setup. (3)

6. Cuando grabas, lo normal es que termines con:
- La toma principal más planos de detalle y cosas para cortar encima. (0)
- Varias tomas de lo mismo hasta que me sale bien. (1, conchita)
- La toma buena y alguito más por si acaso. (2)
- Una sola, si quedó quedó. (3)
- Lo que sea, después en la edición lo arreglo. (3)

**EDICIÓN**

7. Editando, en lo que más se te va el tiempo:
- En quitar todo lo que sobra para que no haya un bajón de energía. (0)
- En que las transiciones y el color queden bien bonitos. (1, conchita)
- En ponerle música que combine con el mood. (2)
- En que no quede muy largo, le corto al ojo. (2)
- Casi no edito, junto y subo. (3)

8. Sobre los subtítulos en tus videos:
- Siempre van, y los uso para marcar el golpe de cada frase. (0)
- Les pongo los animados de moda porque se ven pro. (1, conchita)
- Los pongo cuando me acuerdo o si el video lo pide. (2)
- A veces, no siempre tengo el tiempo. (2)
- Casi nunca, se entiende escuchando. (3)

**DISTRIBUCIÓN**

9. Tienes el video listo. Lo subes así:
- Lo acomodo a cada plataforma, no se comporta igual en todas. (0)
- Lo subo a todas a la vez con una herramienta para no perder tiempo. (1, conchita)
- El mismo video en todas, le cambio el caption según la red. (2)
- Lo mismo en todas, mismo caption, copy paste. (3)
- Lo subo donde me acuerde, no siempre a todas. (3)

10. El caption de tus posts es:
- Texto que dice algo solo y usa las palabras que mi gente buscaría. (0)
- Un copy bien cuidado que acompañe la estética del feed. (1, conchita)
- Una frase con emojis y los hashtags de siempre. (2)
- Lo que se me ocurra rápido para no dejarlo vacío. (3)
- Casi siempre vacío o un par de emojis. (3)

**ANÁLISIS POST-PUBLICACIÓN**

11. Pasaron 48 horas. Lo que miras:
- Saves, watch time y shares, eso me dice si conectó de verdad. (0)
- Entro a estadísticas y reviso el panel completo. (1, conchita)
- Cuántos likes y comentarios hizo. (2)
- Si llegó a más gente que el anterior. (2)
- Casi no entro, me estreso con los números. (3)

12. Un video se te fue mucho mejor que el resto. Lo que haces:
- Saco qué lo hizo distinto y lo meto a propósito en los próximos. (0)
- Lo fijo, lo reuso y trato de exprimirlo en otros formatos. (1, conchita)
- Me motiva y subo más seguido un tiempo. (2)
- Lo celebro y sigo con lo que tenía planeado. (2)
- Pienso que fue el algoritmo y no le busco. (3)

## TRACK B · DUEÑO DE NEGOCIO / EMPRESA / PRODUCTO

**ESTRATEGIA**

1. Un cliente nuevo te pregunta por qué debería seguir la cuenta de tu marca. Lo que dirías:
- Tenemos una razón clara para estar en su feed, más allá de vender. (0)
- Subimos contenido de valor sobre nuestro rubro y novedades. (1, conchita)
- Mostramos nuestros productos y lo que la marca va haciendo. (2)
- Posteamos para mantenernos presentes y activos. (2)
- Subimos por subir, porque hay que estar. (3)

2. Cuando defines qué postear, te guías por:
- Lo que mi cliente necesita escuchar para confiar y comprar. (0)
- Un calendario armado con fechas y temas del sector. (1, conchita)
- Lo que les está funcionando a otras marcas parecidas. (2)
- Lo que el equipo o la agencia proponga esa semana. (3)
- Lo que se pueda según el producto o la promo del momento. (3)

**PRE-PRODUCCIÓN**

3. Antes de producir una pieza, lo que existe es:
- Un mensaje y un gancho definidos, sabemos qué tiene que entender la gente. (0)
- Un brief con referencias y mood board para quien graba. (1, conchita)
- Una idea general de lo que queremos mostrar. (2)
- El producto y la fecha, el resto sale en la grabación. (3)
- Improvisamos según lo que se nos ocurra ese día. (3)

4. Las primeras líneas o el primer frame de sus piezas suelen:
- Estar pensadas para frenar a alguien que ni conoce la marca. (0)
- Abrir con el logo y el nombre para reforzar marca. (1, conchita)
- Mostrar el producto de una. (2)
- Empezar con un "en [marca] creemos que...". (3)
- No las pensamos, arranca donde arranca. (3)

**PRODUCCIÓN**

5. Cuando se produce el contenido de la marca:
- Cuidamos luz y audio aunque sea con celular, eso no se transa. (0)
- Contratamos una producción cuidada para que se vea premium. (1, conchita)
- Lo graba alguien del equipo con lo que hay. (2)
- Usamos fotos del producto y banco de imágenes. (2)
- Sale como salga, lo importante es subir. (3)

6. El material visual de sus piezas es:
- Variado y propio, grabamos de más para tener con qué cortar. (0)
- Plantillas y stock que mantienen todo uniforme y prolijo. (1, conchita)
- Las fotos del producto que ya tenemos. (2)
- Una toma o un render y ya. (3)
- Lo que mande el proveedor o el fabricante. (3)

**EDICIÓN**

7. En la edición de sus piezas, la prioridad es:
- Que enganche y no pierda a nadie en los primeros segundos. (0)
- Que se vea impecable y alineado con el manual de marca. (1, conchita)
- Que el producto se vea lo mejor posible. (2)
- Que quede dentro del tiempo del formato. (2)
- Edición mínima, cortar y subir. (3)

8. Sobre subtítulos y texto en pantalla en sus videos:
- Van siempre y guían la atención a lo que importa. (0)
- Ponemos el texto con la tipografía y colores de la marca. (1, conchita)
- A veces, depende de la pieza. (2)
- Solo el claim final o el precio. (2)
- Casi nunca, el video habla solo. (3)

**DISTRIBUCIÓN**

9. Cuando publican una campaña o pieza:
- La adaptamos a cómo consume la gente en cada canal. (0)
- La mandamos a todos los canales el mismo día para coordinar el lanzamiento. (1, conchita)
- El mismo arte en todas las redes. (2)
- Donde el equipo alcance a subir. (3)
- Cuando hay algo que promocionar, si no, no. (3)

10. El texto que acompaña sus publicaciones busca:
- Decir algo que la gente buscaría y conectar con su necesidad. (0)
- Comunicar los beneficios y un llamado a la acción claro. (1, conchita)
- Describir el producto o la promo. (2)
- Frase corta con los hashtags de la marca. (2)
- Lo arma quien suba ese día. (3)

**ANÁLISIS POST-PUBLICACIÓN**

11. Para saber si el contenido funciona, miran:
- Saves, retención y shares, eso predice si va a escalar. (0)
- El reporte de alcance e impresiones del mes. (1, conchita)
- Likes, seguidores nuevos y comentarios. (2)
- Solo si se tradujo en ventas o no. (2)
- No medimos mucho el orgánico. (3)

12. Cuando una pieza funciona mucho mejor que las otras:
- Entendemos por qué y lo volvemos parte del manual de contenido. (0)
- La convertimos en pauta para escalar el alcance con presupuesto. (1, conchita)
- La repetimos tal cual varias veces. (2)
- Nos alegra el resultado y seguimos el plan. (2)
- Lo damos por suerte y seguimos igual. (3)

Las dos personas quedan bien distintas: el creador piensa en "yo hago todo", el negocio piensa en equipo, marca y producto, y las conchitas de cada track atacan el autoengaño propio de cada uno (el creador confunde estética con retención, el negocio confunde gloss y presupuesto con estrategia).

El siguiente bloque son las pantallas de resultado: cuello de botella, el porqué en una línea, primer paso y ruteo. Son 6 por persona porque el copy cambia según quién lee. ¿Las hago para el track de creador primero o te las tiro para las dos personas de una?

## 🧑 Adriana · 2026-06-19 03:39
todo muy bien pero siento que esas preguntas estan larguisimas y esas respuestas tambien cualquiera se ladillaria en leer tienen que ser un poco mas balanceadas para qeu sea rapido uno tras otro pa pa pa

## 🤖 Claude · 2026-06-19 03:40
Tienes toda la razón, así nadie llega a la 12. Apreté todo, mismo mecanismo y misma conchita, ahora se lee de un golpe. Track creador:

**ESTRATEGIA**

1. Te preguntan de qué va tu cuenta:
- La frase de siempre, ya me la sé de memoria. (0)
- Hablo de lo mío y ya. (1)
- Depende de quién pregunte. (2, conchita)
- Explico largo, en una frase no cabe. (3)
- "Síguela y vas a entender." (3)

2. Alguien de tu nicho explota con un formato:
- Bien por esa persona, lo mío no va por ahí. (0)
- Lo anoto por si encaja. (1)
- Lo pruebo rápido, algo tendrá. (2, conchita)
- Me da ansiedad quedarme atrás. (3)
- Lo estudio y termino copiándolo. (3)

**PRE-PRODUCCIÓN**

3. Los primeros segundos de tu último video:
- Sabía con qué abrir antes de grabar. (0)
- Grabé varias y elegí la que se sintió mejor. (1, conchita)
- Una frase que se me ocurrió ahí. (2)
- Me presenté, un saludito. (3)
- Ni me acuerdo. (3)

4. Cuando te sientas a crear:
- Saco del banco de ideas que tengo. (0)
- Grabo varias cuando llega la inspiración. (1, conchita)
- Abro cámara y veo qué digo hoy. (2)
- Espero a que se me ocurra algo. (3)
- Replico algo que vi funcionando. (3)

**PRODUCCIÓN**

5. Lo primero que resuelves al grabar:
- Luz y audio limpio. (0)
- Que el fondo se vea estético. (1, conchita)
- Donde haya luz natural. (2)
- Donde me agarre el momento. (3)
- Grabo y ya. (3)

6. Cuando grabas terminas con:
- Toma principal más planos para cortar. (0)
- Varias tomas de lo mismo. (1, conchita)
- La buena y algo por si acaso. (2)
- Una sola. (3)
- Lo que sea, lo arreglo editando. (3)

**EDICIÓN**

7. Editando, el tiempo se te va en:
- Quitar todo lo que sobra. (0)
- Transiciones y color bonitos. (1, conchita)
- Buscar la música del mood. (2)
- Que no quede largo. (2)
- Nada, junto y subo. (3)

8. Tus subtítulos:
- Siempre, marcan el ritmo. (0)
- Los animados de moda, se ven pro. (1, conchita)
- Cuando me acuerdo. (2)
- A veces, si hay tiempo. (2)
- Casi nunca. (3)

**DISTRIBUCIÓN**

9. Subes el video así:
- Lo acomodo a cada plataforma. (0)
- Lo lanzo a todas con una herramienta. (1, conchita)
- Mismo video, cambio el caption. (2)
- Mismo todo, copy paste. (3)
- Donde me acuerde. (3)

10. Tu caption es:
- Dice algo solo y usa palabras que la gente busca. (0)
- Copy cuidado para la estética del feed. (1, conchita)
- Frase con emojis y hashtags. (2)
- Algo rápido para no dejarlo vacío. (3)
- Vacío o dos emojis. (3)

**ANÁLISIS**

11. 48 horas después, miras:
- Saves, watch time y shares. (0)
- El panel completo, todo. (1, conchita)
- Likes y comentarios. (2)
- Si llegó a más que el anterior. (2)
- Casi no entro. (3)

12. Un video se va mucho mejor que el resto:
- Saco qué lo hizo y lo repito a propósito. (0)
- Lo reuso y lo exprimo en otros formatos. (1, conchita)
- Me motiva y subo más seguido. (2)
- Lo celebro y sigo el plan. (2)
- Fue el algoritmo, no le busco. (3)

Si este es el ritmo pa pa pa que buscas, espejeo el track de negocio igual de apretado. ¿Va?

## 🧑 Adriana · 2026-06-19 03:56
sigues dejando el puntaje 0 de primero en todos, barajea los ordenes

## 🤖 Claude · 2026-06-19 03:57
Hecho. Mismo set, órdenes barajados, el (0) cae en distinta posición en cada una:

**ESTRATEGIA**

1. Te preguntan de qué va tu cuenta:
- Hablo de lo mío y ya. (1)
- "Síguela y vas a entender." (3)
- La frase de siempre, ya me la sé de memoria. (0)
- Depende de quién pregunte. (2, conchita)
- Explico largo, en una frase no cabe. (3)

2. Alguien de tu nicho explota con un formato:
- Lo pruebo rápido, algo tendrá. (2, conchita)
- Me da ansiedad quedarme atrás. (3)
- Lo anoto por si encaja. (1)
- Bien por esa persona, lo mío no va por ahí. (0)
- Lo estudio y termino copiándolo. (3)

**PRE-PRODUCCIÓN**

3. Los primeros segundos de tu último video:
- Ni me acuerdo. (3)
- Sabía con qué abrir antes de grabar. (0)
- Me presenté, un saludito. (3)
- Grabé varias y elegí la que se sintió mejor. (1, conchita)
- Una frase que se me ocurrió ahí. (2)

4. Cuando te sientas a crear:
- Abro cámara y veo qué digo hoy. (2)
- Espero a que se me ocurra algo. (3)
- Grabo varias cuando llega la inspiración. (1, conchita)
- Replico algo que vi funcionando. (3)
- Saco del banco de ideas que tengo. (0)

**PRODUCCIÓN**

5. Lo primero que resuelves al grabar:
- Donde me agarre el momento. (3)
- Que el fondo se vea estético. (1, conchita)
- Luz y audio limpio. (0)
- Grabo y ya. (3)
- Donde haya luz natural. (2)

6. Cuando grabas terminas con:
- Una sola. (3)
- La buena y algo por si acaso. (2)
- Varias tomas de lo mismo. (1, conchita)
- Toma principal más planos para cortar. (0)
- Lo que sea, lo arreglo editando. (3)

**EDICIÓN**

7. Editando, el tiempo se te va en:
- Buscar la música del mood. (2)
- Quitar todo lo que sobra. (0)
- Transiciones y color bonitos. (1, conchita)
- Nada, junto y subo. (3)
- Que no quede largo. (2)

8. Tus subtítulos:
- Los animados de moda, se ven pro. (1, conchita)
- A veces, si hay tiempo. (2)
- Casi nunca. (3)
- Cuando me acuerdo. (2)
- Siempre, marcan el ritmo. (0)

**DISTRIBUCIÓN**

9. Subes el video así:
- Mismo video, cambio el caption. (2)
- Lo lanzo a todas con una herramienta. (1, conchita)
- Lo acomodo a cada plataforma. (0)
- Donde me acuerde. (3)
- Mismo todo, copy paste. (3)

10. Tu caption es:
- Frase con emojis y hashtags. (2)
- Vacío o dos emojis. (3)
- Copy cuidado para la estética del feed. (1, conchita)
- Dice algo solo y usa palabras que la gente busca. (0)
- Algo rápido para no dejarlo vacío. (3)

**ANÁLISIS**

11. 48 horas después, miras:
- El panel completo, todo. (1, conchita)
- Saves, watch time y shares. (0)
- Casi no entro. (3)
- Likes y comentarios. (2)
- Si llegó a más que el anterior. (2)

12. Un video se va mucho mejor que el resto:
- Lo reuso y lo exprimo en otros formatos. (1, conchita)
- Me motiva y subo más seguido. (2)
- Lo celebro y sigo el plan. (2)
- Fue el algoritmo, no le busco. (3)
- Saco qué lo hizo y lo repito a propósito. (0)

¿Espejeo el track de negocio igual de apretado y barajado?

## 🧑 Adriana · 2026-06-19 04:05
ok aceptadas las preguntas vamos con el copy y el UX/UI del resto:
 quier una pagina de inicio, por ejemplo:
diagnóstico gratis · 60 seg
¿Por qué tu contenido no convierte?
Siete preguntas. Te digo en qué etapa de tu proceso se te cae todo, y cuánta gente está en tu mismo punto.
Empezar mi diagnóstico →
creatividad² · adrianavmarquez.com

al terminar las preguntas esta la pagina con el resultado del puntaje por bucket:
Estrategia / Pre-pro/ Producción/ Edición/ Distribucion/Análisis, debajo hay un espacio para una grafica de curvas simulando el porcentaje de personas que han caido en su mismo bucket hasta el momento. Un CTA para que reciban como un plan rapido para mejorar en 5 min. dependiendo del bucket cada quien recibe su plan rapido. 

pagina de captacion preguntando a donde mando el plan, ejemplo:

adrianav✦marquezcasi listo
plan
último paso
¿A dónde te *mando* tu plan?
Recomendaciones hechas para tu etapa, directo a tu correo.
Nombre
Correo
Enviarme mi plan →
creatividad² · adrianavmarquez.com

Y luego es como un thank you page que dice que su plan va en camino y que si comparten esto ocn alguien que lo necesite ambas personas entran a mi lista d eprioridad para mi herramienta Creatividad2, con precio especial y tambien te mandare [mi agenda de crea tu 2026 gratis] paa que puedas ponerle orden a la cosa.

## 🤖 Claude · 2026-06-19 04:07
Va el funnel completo, copy apretado y UX por pantalla. Mantengo tu voz y tus tics de marca (la estrella, el asterisco para énfasis).

**1 · LANDING**

UX: fondo negro, titular en Poppins Bold blanco, la estrella roja como acento detrás del título. Eyebrow en amarillo. Un solo botón rojo #D72323, nada más que distraiga. Al tocar "Empezar" lo primero que ve es el router (negocio o marca personal), después las 12.

Copy:
diagnóstico gratis · 60 segundos
**¿Por qué tu contenido no convierte?**
12 preguntas. Te digo en qué etapa de tu proceso se te cae todo, y cuánta gente está atascada en tu mismo punto.
Empezar mi diagnóstico →
creatividad² · adrianavmarquez.com

(Tu ejemplo decía "siete preguntas". El quiz tiene 12, así que ajustamos el número o lo dejamos en "menos de un minuto". No prometas siete y entregues doce.)

**2 · RESULTADO**

UX: arriba el veredicto grande, la etapa en rojo. Una línea de qué significa, lo justo para picarlos, la profundidad va al correo. Debajo, los 6 buckets en barras con tu cuello de botella en rojo y las 2 áreas de mejora en amarillo. Más abajo, la curva: dónde caes tú contra todos los demás. CTA rojo al plan.

Copy (plantilla, ejemplo con Estrategia):
tu diagnóstico
**Se te cae en: Estrategia**
Produces bien, pero no sabes del todo para quién. Sin eso, lo demás no levanta.
[gráfico de los 6 buckets]
[curva] El 38% de los creadores se cae aquí también. No estás solo.
Quiero mi plan de 5 minutos →

Las 6 líneas de veredicto, una por bucket:
- Estrategia: produces bien, pero no sabes del todo para quién. Sin eso, lo demás no levanta.
- Pre-producción: improvisas, por eso tus primeros 3 segundos no frenan a nadie.
- Producción: el mensaje está, la ejecución te baja la percepción (luz, audio, tomas).
- Edición: grabas bien y lo pierdes en el corte, tu edición no pelea por la retención.
- Distribución: buen contenido escondido, lo subes sin adaptar y sin que se pueda encontrar.
- Análisis: publicas y no aprendes, sin leer la data correcta repites lo que no jala.

(Ojo cold start: el primer día la curva no tiene data. Hasta juntar suficientes respuestas, esconde el % o ponlo en "calculando", si no el primer usuario ve 0% y mata el social proof.)

**3 · CAPTACIÓN**

UX: pantalla limpia, dos campos y un botón. Señal de progreso "último paso". El form taggea la respuesta con el bucket diagnosticado, así tu lista de Mailerlite queda segmentada por etapa sola.

Copy:
adrianav✦marquez
casi listo · último paso
**¿A dónde te *mando* tu plan?**
Hecho para tu etapa. Directo a tu correo.
Nombre
Correo
Enviarme mi plan →
creatividad² · adrianavmarquez.com

**4 · THANK YOU**

UX: confirmación arriba, el bloque de compartir como protagonista. Botones de WhatsApp, IG y copiar link, con link de referido que taggea a las dos personas. Estrella de marca, CTA rojo.

Copy:
**Tu plan va en camino.**
Revisa tu correo en un minuto. Si no llega, mira en promociones.

¿Conoces a alguien atascado en la misma etapa?
Compártele el diagnóstico. Cuando lo tome, ustedes dos entran a mi lista de prioridad para Creatividad², con precio especial cuando abra.
Y por compartir te mando mi *Agenda Crea tu 2026* gratis, para que le pongas orden a todo esto desde ya.
Compartir mi diagnóstico →
creatividad² · adrianavmarquez.com

(El link de referido tiene que taggear a ambos para la lista de prioridad y disparar el envío de la agenda. Eso lo amarras con n8n.)

El siguiente bloque natural es el contenido del plan de 5 minutos, uno por bucket, que es el lead magnet que llega al correo. ¿Lo armo?

## 🧑 Adriana · 2026-06-19 04:14
el ux del resultado me lo imaginaba en lugar de barra algo asi:
como pills arriba con numero y bucket name y abajo el procentaje y la barra

## 🤖 Claude · 2026-06-19 04:16
Visto, ese es el patrón: pills arriba con número y nombre, el número grande y la curva abajo. Lo adapto a los 6 buckets y mantengo el copy que ya cerramos. Reescribo solo la pantalla de resultado:

**RESULTADO · layout (mobile, de arriba a abajo)**

1. Eyebrow: "tu diagnóstico"

2. Veredicto hero, Poppins Bold, la etapa en rojo:
**Se te cae en: Estrategia**
Produces bien, pero no sabes del todo para quién. Sin eso, lo demás no levanta.

3. Las pills, dos filas de tres (como las tres circulares de tu referencia, pero seis). Cada pill: ícono chico, nombre del bucket y un número de nivel, donde más alto es más sólido. El cuello de botella es el de número más bajo, en rojo #D72323. Las 2 áreas de mejora en amarillo #FFBA35. Las 3 sanas en lavender, para que el rojo cante solo.

Ejemplo de los seis:
Estrategia 32 · Pre-pro 71 · Producción 64 · Edición 80 · Distribución 55 · Análisis 90
(rojo el 32, amarillo el 55 y el 64, lavender el resto)

4. El número grande, estilo el 78% de tu screenshot, pero aquí es el social proof:
**38%**
de los creadores se cae en Estrategia, igual que tú.

5. La curva. Eje x: los 6 buckets en orden (Estrategia a Análisis). Eje y: % de gente cuyo cuello de botella es ese bucket. Un marcador tipo tooltip sobre tu etapa, como el "78%" sobre agosto en tu referencia. La persona ve de un vistazo dónde está el pico y que no está sola.

6. CTA rojo:
Quiero mi plan de 5 minutos →

El número de la pill (nivel) y el número grande (% de gente) son distintos a propósito: uno es tuyo por etapa, el otro es cuánta gente está donde tú. Pills sin signo de %, el grande con %, así nadie los confunde.

(Sigue en pie el cold start: hasta tener respuestas suficientes, el 38% y la curva van en "calculando". El nivel de las pills sí se puede mostrar desde el día uno, porque sale del score propio y no de la data agregada.)

¿Te cuadra así y sigo con el plan de 5 minutos por bucket?

## 🧑 Adriana · 2026-06-19 04:16
la distribucion de la pagina de inicio algo asi lo que tiene mas peso es la pregunta

## 🤖 Claude · 2026-06-19 04:17
Claro, la pregunta es la protagonista, ocupa medio screen y todo lo demás se le subordina. Reescribo la landing con esa distribución, sobre fondo claro como tu referencia (lavender #F2E9FF o blanco), titular negro Poppins Bold con un acento rojo:

**LANDING · layout (mobile, de arriba a abajo)**

1. Barra mínima: el monogram chiquito o una estrellita de marca. Nada pesado.

2. Personaje + badge. Un cutout tuyo o una de tus caras de marca arriba, con una estrellita roja tipo sticker que diga "diagnóstico gratis". Es tu equivalente al "ONLINE SCHOOL" de la referencia, le da cara y energía sin robarle peso a la pregunta.

3. El hero, lo más grande de toda la página, Poppins Bold negro, una palabra o el signo en rojo #D72323:
**¿Por qué tu contenido no convierte?**
Esto se come el grueso del screen, como el "ARE YOU READY LEARN?" de tu ref.

4. Subtexto chico, una línea, de bajo peso:
12 preguntas. Te digo dónde se te cae todo y cuánta gente está en tu mismo punto.

5. Botón rojo #D72323, ancho:
Empezar mi diagnóstico →

6. Línea secundaria, chiquita, donde la ref pone "Sign in". Aquí la uso para bajar fricción:
Sin registro. Solo tus respuestas.

El orden de lectura cae solo: cara, pregunta que pega, una línea que explica, botón. La pregunta es lo único que se ve de lejos.

¿Cerramos la parte de UX aquí y arranco el contenido del plan de 5 minutos por bucket, o quieres que ajuste otra pantalla con este mismo criterio?

## 🧑 Adriana · 2026-06-19 04:23
la pagina de captacion quiero que tenga como full toque de personalidad que no duden que soy cool y en damrme su info, yo haciendo una mueca most likely o un meme de kronus

## 🤖 Claude · 2026-06-19 04:24
Me cuadra. La página de captación es justo donde la gente duda antes de soltar el correo, así que ahí tu cara haciendo la mueca trabaja más que cualquier copy: pasa de "formulario frío" a "ah, es Adri, dale". Reescribo la pantalla con full personalidad, estilo tu ref de Savee:

**CAPTACIÓN · layout (mobile)**

1. Fondo de un color de marca a tope, amarillo #FFBA35 o azul #3846C4, con tus doodles regados alrededor (las estrellitas, los pluses, el pixel art). Tu "combina sin miedo".

2. Hero: tu cutout haciendo la mueca o el meme de reacción que elijas (tipo el de kronus), grande y centrado, como el personaje del MyWallet. Esto es lo que vende el "soy cool, suéltame el correo".

3. Lockup bold tipo wordmark, Poppins Black con contorno, donde la ref pone "MyWallet":
**último paso**

4. La pregunta, mediana, debajo:
**¿A dónde te *mando* tu plan?**
Hecho para tu etapa. Y tranqui, no vine a llenarte el correo de baboserías.

5. Form limpio sobre el color, inputs blancos:
Nombre
Correo

6. Botón redondeado, estilo "Get started":
Enviarme mi plan →

micro debajo del botón:
Un correo. El plan. Ya.

adrianav✦marquez · creatividad²

La personalidad la cargan la cara y el fondo, el texto se queda corto a propósito para que el meme sea el protagonista.

¿Va con este criterio y cierro UX para meterle al contenido del plan por bucket?

## 🧑 Adriana · 2026-06-19 04:26
quiero que la experiencia durante las preguntas y respuestas sean asi, preguntas espacio para un personaje ilustrado, luego descanso entre preguntas de icebreakers o memes y seguimos con preguntas

## 🤖 Claude · 2026-06-19 04:27
Buenísimo, y encaja perfecto porque esos blobs son literalmente tus EMOCIONES de marca (emocionado, confundido, dolido, etc.). Los usas de personaje por pregunta y de paso le das cara a cada momento. Te armo la experiencia sin matar el pa-pa-pa:

**EXPERIENCIA · flow**
router → 4 preguntas → break → 4 preguntas → break → 4 preguntas → resultado

Dos breaks nada más, a los tercios. Si metes uno entre cada pregunta, matas la completación. Así respiras dos veces y mantienes el ritmo.

**Pantalla de pregunta**
- Arriba, acotado, un blob de emoción que reacciona al tema. Pregunta sobre un fracaso, sale el "dolido". Pregunta de estrategia, el "confundido". El personaje cambia, el peso se lo lleva la pregunta.
- Barrita de progreso fina arriba, para que sienta que avanza.
- La pregunta corta y las 5 opciones tappables, estilo el "Qual seu objetivo?" de la ref.
- Tap en una opción y avanza solo, sin botón de siguiente. Eso es lo que sostiene el pa-pa-pa.

**Pantalla de break (2)**
Cara o meme tuyo grande, una línea en tu voz, un "seguir →". No puntúa, no pide nada, puro aire y rapport.
- Break 1, tras la 4: [tu meme] "Vas a un tercio y ya te estoy leyendo. Dale."
- Break 2, tras la 8: [tu meme] "Recta final. Aquí es donde la mayoría se raja. Tú no."

Si quieres más temperatura, el break puede ser un icebreaker bobo sin scoring, tipo [tu cara] "¿editas con música o en silencio absoluto? (no cuenta, es chisme mío)". Sube personalidad sin sumar fricción porque sigue siendo un solo tap.

Con esto ya tienes landing, experiencia, resultado, captación y thank you. ¿Cierro la capa de UX y arranco el contenido del plan de 5 minutos por bucket, que es lo único que falta?

## 🧑 Adriana · 2026-06-19 04:32
que opinas de Pantalla de break (2)
Cara o meme tuyo grande, una línea en tu voz, un "seguir →". No puntúa, no pide nada, puro aire y rapport.

* Break 1, tras la 4: [meme de kronus juzgando] "Ya estas pensando en salirte? DALEEE DEJA TU VAINA, sigue. Son solo unas preguntas, comprometete con eso al menos."
* Break 2, tras la 8: [tu meme] "Recto final. (foto de una alcancia) Sorry recta final* y le cae una banderita en la alcancia del pompi. Falta poco"

## 🤖 Claude · 2026-06-19 04:33
Break 1 me encanta, déjalo tal cual. Hace exactamente el trabajo: nombra el impulso de salirse justo cuando aparece (en la 4 es cuando la gente empieza a flojear) y los reta a comprometerse. El "kronus juzgando" le pega al tono y el "deja tu vaina" es 100% tu voz. Ese retiene.

Break 2 tiene buen chiste, pero dos riesgos de ejecución:

1. El bit del typo ("recto" → "recta final*") es gracioso, pero necesita un segundo para caer, y una pantalla de break no da ese segundo. Si no lo cachan rápido, se lee como un error de verdad y confunde en vez de causar gracia. La salida: que el chiste lo cargue la imagen, no el texto. La alcancía con la banderita cayéndole al pompi ES el remate. Si el visual hace el trabajo, el texto se queda en lo mínimo: "Recta final. (sí, casi escribo otra cosa)". Lo cachan al toque y sigues.

2. El chiste del pompi es perfecto para el track de creador, pero puede chirriar para el dueño de negocio. Ahí te conviene decidir: ¿los breaks son los mismos para los dos tracks, o track-aware? Si son compartidos, Break 2 lo bajaría a algo igual de divertido pero sin meter el pompi. Si son separados, te dejo el pompi en creador y le pongo otra cosa al negocio.

> *[line redacted — references an out-of-scope venture]*

## 🧑 Adriana · 2026-06-19 04:35
quien sea que vaya. atrabaajr onmigo tiene que entender mi sentido del humor y saber que no soy seria, que tengo adhd que un minuto estamos haciendo unas preguntas d ediagnostico que te van a cambiar el rumbo de las redes y otro te hago un chiste d edoble snetido

## 🤖 Claude · 2026-06-19 04:36
Claro. Ese choque de tono es tu filtro. El que se incomoda con que pases de "esto te cambia el rumbo de las redes" a un chiste de doble sentido en la misma pantalla no es tu cliente, y mejor que se caiga ahí y no después de pagarte. La marca polariza a propósito, así llega tu gente.

Entonces me retracto de lo de bajarle el tono al negocio. El pompi se queda en los dos tracks. El dueño de negocio que aguanta ese chiste y se queda es justo el que quieres. El de la agencia con corbata se va, y bien que se vaya.

Lo único que mantengo, y va a favor de tu humor: el contraste es lo que hace que peguen los dos lados. Preguntas filosas y creíbles, breaks desquiciados. Si los breaks fueran serios no eres tú, y si las preguntas fueran chistosas el diagnóstico pierde autoridad. El whiplash jala porque cada lado vive en su extremo, y esa velocidad de switch es tu energía, no un bug.

La nota de producción iba justo a favor del chiste: deja que la alcancía con la banderita cargue el remate y el texto corto encima, para que pegue de una sin que nadie se pierda en el camino.

Quedamos: Break 1 tal cual, Break 2 con pompi para ambos, visual cargando el remate. ¿Arranco el plan de 5 minutos por bucket?

## 🧑 Adriana · 2026-06-19 04:37
ejemplo de meme

## 🤖 Claude · 2026-06-19 04:38
Jajaja perfecto, ese meme hace TODO el trabajo solo. El "RECTO FINAL" en el banner ya es el remate, la durazno cruzando la meta lo sella, y nadie necesita que se lo expliquen, lo cachan en menos de un segundo. Justo eso: el visual carga el chiste, cero lag.

Bonus, ese rojo del banner es prácticamente tu #D72323, así que entra en paleta sin tocar nada.

Entonces el break 2 casi no necesita texto, el meme habla. Lo dejaría así:
[meme RECTO FINAL]
falta poco →

Y ya. Break 1 con kronus, break 2 con la durazno, los dos para ambos tracks.

Con esto la capa de UX queda redonda: landing, experiencia con breaks, resultado, captación y thank you. ¿Le entro al plan de 5 minutos por bucket?

## 🧑 Adriana · 2026-06-19 04:41
esto siento tiene mucho copy:
4 · THANK YOU
UX: confirmación arriba, el bloque de compartir como protagonista. Botones de WhatsApp, IG y copiar link, con link de referido que taggea a las dos personas. Estrella de marca, CTA rojo.
Copy:
Tu plan va en camino.
Revisa tu correo en un minuto. Si no llega, mira en promociones.
¿Conoces a alguien atascado en la misma etapa?
Compártele el diagnóstico. Cuando lo tome, ustedes dos entran a mi lista de prioridad para Creatividad², con precio especial cuando abra.
Y por compartir te mando mi Agenda Crea tu 2026 gratis, para que le pongas orden a todo esto desde ya.
Compartir mi diagnóstico →
creatividad² · adrianavmarquez.com
(El link de referido tiene que taggear a ambos para la lista de prioridad y disparar el envío de la agenda. Eso lo amarras con n8n.)

## 🤖 Claude · 2026-06-19 04:41
De acuerdo, eso parecía contrato. Apretado:

**4 · THANK YOU**

UX: igual. Confirmación arriba, el bloque de compartir como protagonista, botones de WhatsApp/IG/copiar link, CTA rojo.

Copy:
**Tu plan va en camino. ✦**
Revísalo en tu correo, o en promociones si se esconde.

¿Conoces a alguien atascado en la misma etapa?
Compártelo y ganan los dos: prioridad y precio especial en Creatividad², y para ti la Agenda Crea tu 2026 gratis.
Compartir mi diagnóstico →
creatividad² · adrianavmarquez.com

(Build: el link de referido taggea a ambos y dispara el envío de la agenda, lo amarras con n8n.)

Bajé el bloque de cuatro líneas a una. ¿Así sí, o lo quieres todavía más seco?

## 🧑 Adriana · 2026-06-19 04:50
espejea las preguntas de negocios, cortas barajadas, con conchitas de mango todo asi como las que hciimos para creadores:

ESTRATEGIA

1. Te preguntan de qué va tu cuenta:

* Hablo de lo mío y ya. (1)
* "Síguela y vas a entender." (3)
* La frase de siempre, ya me la sé de memoria. (0)
* Depende de quién pregunte. (2, conchita)
* Explico largo, en una frase no cabe. (3)

1. Alguien de tu nicho explota con un formato:

* Lo pruebo rápido, algo tendrá. (2, conchita)
* Me da ansiedad quedarme atrás. (3)
* Lo anoto por si encaja. (1)
* Bien por esa persona, lo mío no va por ahí. (0)
* Lo estudio y termino copiándolo. (3)
PRE-PRODUCCIÓN

1. Los primeros segundos de tu último video:

* Ni me acuerdo. (3)
* Sabía con qué abrir antes de grabar. (0)
* Me presenté, un saludito. (3)
* Grabé varias y elegí la que se sintió mejor. (1, conchita)
* Una frase que se me ocurrió ahí. (2)

1. Cuando te sientas a crear:

* Abro cámara y veo qué digo hoy. (2)
* Espero a que se me ocurra algo. (3)
* Grabo varias cuando llega la inspiración. (1, conchita)
* Replico algo que vi funcionando. (3)
* Saco del banco de ideas que tengo. (0)
PRODUCCIÓN

1. Lo primero que resuelves al grabar:

* Donde me agarre el momento. (3)
* Que el fondo se vea estético. (1, conchita)
* Luz y audio limpio. (0)
* Grabo y ya. (3)
* Donde haya luz natural. (2)

1. Cuando grabas terminas con:

* Una sola. (3)
* La buena y algo por si acaso. (2)
* Varias tomas de lo mismo. (1, conchita)
* Toma principal más planos para cortar. (0)
* Lo que sea, lo arreglo editando. (3)
EDICIÓN

1. Editando, el tiempo se te va en:

* Buscar la música del mood. (2)
* Quitar todo lo que sobra. (0)
* Transiciones y color bonitos. (1, conchita)
* Nada, junto y subo. (3)
* Que no quede largo. (2)

1. Tus subtítulos:

* Los animados de moda, se ven pro. (1, conchita)
* A veces, si hay tiempo. (2)
* Casi nunca. (3)
* Cuando me acuerdo. (2)
* Siempre, marcan el ritmo. (0)
DISTRIBUCIÓN

1. Subes el video así:

* Mismo video, cambio el caption. (2)
* Lo lanzo a todas con una herramienta. (1, conchita)
* Lo acomodo a cada plataforma. (0)
* Donde me acuerde. (3)
* Mismo todo, copy paste. (3)

1. Tu caption es:

* Frase con emojis y hashtags. (2)
* Vacío o dos emojis. (3)
* Copy cuidado para la estética del feed. (1, conchita)
* Dice algo solo y usa palabras que la gente busca. (0)
* Algo rápido para no dejarlo vacío. (3)
ANÁLISIS

1. 48 horas después, miras:

* El panel completo, todo. (1, conchita)
* Saves, watch time y shares. (0)
* Casi no entro. (3)
* Likes y comentarios. (2)
* Si llegó a más que el anterior. (2)

1. Un video se va mucho mejor que el resto:

* Lo reuso y lo exprimo en otros formatos. (1, conchita)
* Me motiva y subo más seguido. (2)
* Lo celebro y sigo el plan. (2)
* Fue el algoritmo, no le busco. (3)
* Saco qué lo hizo y lo repito a propósito. (0)

## 🤖 Claude · 2026-06-19 04:51
Espejeado: mismo formato, cortas, barajadas y con su conchita.

## TRACK B · NEGOCIO / EMPRESA / PRODUCTO

**ESTRATEGIA**

1. Te preguntan por qué seguir tu marca:
- Subimos contenido de valor del rubro. (1, conchita)
- Para mantenernos presentes. (2)
- Una razón clara, más allá de vender. (0)
- Subimos por subir. (3)
- Mostramos productos y novedades. (2)

2. Qué postear lo decides por:
- Lo que les funciona a marcas parecidas. (2)
- Un calendario con fechas y temas. (1, conchita)
- Lo que el equipo proponga. (3)
- Lo que el cliente necesita para comprar. (0)
- Lo que haya de producto o promo. (3)

**PRE-PRODUCCIÓN**

3. Antes de producir una pieza tienes:
- Improvisamos. (3)
- Mensaje y gancho definidos. (0)
- El producto y la fecha. (3)
- Brief con referencias y mood board. (1, conchita)
- Una idea general de qué mostrar. (2)

4. El primer frame de tus piezas:
- Muestra el producto de una. (2)
- "En [marca] creemos que...". (3)
- Abre con el logo y el nombre. (1, conchita)
- No lo pensamos. (3)
- Pensado para frenar a quien no te conoce. (0)

**PRODUCCIÓN**

5. Al producir contenido de la marca:
- Lo graba el equipo con lo que hay. (2)
- Contratamos producción premium. (1, conchita)
- Cuidamos luz y audio, aunque sea con celular. (0)
- Sale como salga. (3)
- Fotos de producto y banco de imágenes. (2)

6. El material visual de tus piezas:
- Una toma o un render. (3)
- Las fotos de producto que ya hay. (2)
- Plantillas y stock, todo uniforme. (1, conchita)
- Propio y variado, grabamos de más. (0)
- Lo que mande el proveedor. (3)

**EDICIÓN**

7. En la edición, la prioridad es:
- Que el producto luzca. (2)
- Que enganche y no pierda a nadie al inicio. (0)
- Impecable y alineado al manual de marca. (1, conchita)
- Cortar y subir. (3)
- Que entre en el tiempo del formato. (2)

8. Subtítulos y texto en pantalla:
- Con la tipografía y colores de marca. (1, conchita)
- A veces, depende de la pieza. (2)
- Casi nunca. (3)
- Solo el claim o el precio. (2)
- Siempre, guían la atención. (0)

**DISTRIBUCIÓN**

9. Cuando publican una pieza:
- El mismo arte en todas. (2)
- A todos el mismo día, coordinado. (1, conchita)
- La adaptamos a cada canal. (0)
- Donde el equipo alcance. (3)
- Solo si hay algo que promocionar. (3)

10. El texto de tus posts busca:
- Describir el producto o la promo. (2)
- Frase corta con hashtags de marca. (2)
- Beneficios y un CTA claro. (1, conchita)
- Decir algo que la gente busca y conectar. (0)
- Lo arma quien suba ese día. (3)

**ANÁLISIS**

11. Para saber si funciona, miran:
- El reporte de alcance e impresiones. (1, conchita)
- Saves, retención y shares. (0)
- No medimos el orgánico. (3)
- Likes, seguidores y comentarios. (2)
- Solo si se tradujo en ventas. (2)

12. Una pieza funciona mucho mejor que el resto:
- La metemos en pauta para escalar con presupuesto. (1, conchita)
- La repetimos tal cual. (2)
- Nos alegra y seguimos el plan. (2)
- Lo damos por suerte. (3)
- Entendemos por qué y lo volvemos manual. (0)

Las conchitas de negocio pegan donde el dueño se autoengaña: calendario, mood board, producción premium, manual de marca, reporte de alcance y pauta. Todo suena profesional y delata que confunde prolijidad con estrategia.

Con esto los dos tracks quedan completos. ¿Arranco el plan de 5 minutos por bucket?
