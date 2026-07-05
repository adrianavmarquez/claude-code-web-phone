---
title: "Sistema de 7 agentes para revisión de contenido"
source: claude.ai-chat
created: "2026-05-01 02:31"
summary: "**Conversation Overview**  The person asked for clarification about a specific instruction from Claude's previous response regarding how to use a multi-agent ad copy review system. Specifically, they did not understand the step that referenced pasting a 'Master Prompt' into a Project's instructions and providing a brief to the agent.  Claude explained the two practical options for deploying the system. The first option involves using Claude.ai's Projects feature, where the Master Prompt is loaded once into the project's custom instructions, making it automatically available in every chat within that project without needing to re-paste it each time. The second option is a chat-by-chat approach where the Master Prompt is pasted at the start of each new conversation, followed by the brief and the activation phrase. Claude also clarified what a 'brief' consists of in this context: the brand and product details, target persona, chosen strategic angle, ad format, and the copy to be reviewed.  The conversation was conducted entirely in Spanish. The person appears to be working with or building a seven-agent ad copy evaluation system, with agents covering persona fit, angle execution, emotional resonance, brand consistency, copy excellence, format compliance, and grammar editing. The system is designed to iterate on copy autonomously until all seven agents score 90 or above and the grammar agent returns a pass verdict."
messages: 4
claude_uuid: "919d5fc6-e397-4788-9933-79fa9b607714"
tags: [claude, chat, archive]
---
# Sistema de 7 agentes para revisión de contenido

> **Conversation Overview**

The person asked for clarification about a specific instruction from Claude's previous response regarding how to use a multi-agent ad copy review system. Specifically, they did not understand the step that referenced pasting a "Master Prompt" into a Project's instructions and providing a brief to the agent.

Claude explained the two practical options for deploying the system. The first option involves using Claude.ai's Projects feature, where the Master Prompt is loaded once into the project's custom instructions, making it automatically available in every chat within that project without needing to re-paste it each time. The second option is a chat-by-chat approach where the Master Prompt is pasted at the start of each new conversation, followed by the brief and the activation phrase. Claude also clarified what a "brief" consists of in this context: the brand and product details, target persona, chosen strategic angle, ad format, and the copy to be reviewed.

The conversation was conducted entirely in Spanish. The person appears to be working with or building a seven-agent ad copy evaluation system, with agents covering persona fit, angle execution, emotional resonance, brand consistency, copy excellence, format compliance, and grammar editing. The system is designed to iterate on copy autonomously until all seven agents score 90 or above and the grammar agent returns a pass verdict.

## 🧑 Adriana · 2026-05-01 02:31
> 📎 Master_Prompt_Paid_Media_Copywriting_Agents_System_Setup.md

## 🤖 Claude · 2026-05-01 02:35
Entendido, voy a construir el sistema completo. Primero genero los 7 archivos `.md`, luego los presento para descarga.

Ahora copio todo a outputs y los presento.

Los 7 agentes están listos. Aquí el resumen del sistema construido:

**Los 7 archivos generados:**

| Archivo | Agente | Rol |
|---|---|---|
| `agent-persona.md` | Persona Fit | Psicólogo del consumidor. Evalúa language match, root pain, worldview, identidad. |
| `agent-angle.md` | Angle Execution | Estratega de DR. Caza angle drift desde hook hasta CTA. |
| `agent-emotion.md` | Emotion | Especialista en resonancia. Verifica que el copy PRODUZCA emoción, no solo la nombre. |
| `agent-brand.md` | Brand Consistency | Brand guardian. Voz, valores, lenguaje prohibido, diferenciación. |
| `agent-excellence.md` | Copy Excellence | Copy chief. Elimina fluff, clichés, lenguaje genérico. Cada palabra trabaja. |
| `agent-format.md` | Format Compliance | Ad architect. Word counts, estructura, scanning speed, CTA fit. |
| `agent-grammar.md` | Copy Editor | Pass/Fail. Zero em-dashes, gramática, ortografía, consistencia. |

**Cómo activar el sistema en cualquier chat:**

Pega el contenido del Master Prompt original en las instrucciones del Proyecto, luego dale al agente un brief y di exactamente: *"Please have the agents review the copy. Please iterate on the copy until every agent gives it a 90+ / 100."*

El sistema itera autónomamente hasta que los 7 agentes pasan y el Grammar Agent da PASS.

## 🧑 Adriana · 2026-05-01 03:55
no entendi esta parte: Pega el contenido del Master Prompt original en las instrucciones del Proyecto, luego dale al agente un brief?

## 🤖 Claude · 2026-05-01 03:55
Buena pregunta. Te explico paso a paso cómo funciona todo esto en la práctica.

**El Master Prompt es el "cerebro" del sistema.** Sin él, Claude no sabe que existen los 7 agentes, no sabe cómo scorear, no sabe iterar. Es el setup que hace que todo funcione.

Tienes dos opciones para usarlo:

**Opción A: Proyecto de Claude (recomendado)**

En Claude.ai puedes crear un "Project" y meterle instrucciones personalizadas que se aplican a TODOS los chats dentro de ese proyecto. Copias todo el texto del Master Prompt en esas instrucciones, y cada vez que abras un chat dentro del proyecto, Claude ya sabe que es el sistema de agentes. No tienes que volver a explicarle nada.

Flujo: Project con Master Prompt cargado → abres un chat → pegas tu brief de copy → dices la frase de activación → el sistema corre.

**Opción B: Chat nuevo cada vez**

Si no usas Projects, simplemente abres un chat nuevo, pegas el Master Prompt completo como primer mensaje, luego en el mismo mensaje (o en el siguiente) pegas tu brief, y terminas con la frase de activación.

**Y el "brief" es simplemente la información del anuncio que quieres evaluar**, por ejemplo:

- Marca y producto
- Target persona
- Ángulo estratégico elegido
- Formato del ad (static headline, Meta feed, Story, etc.)
- El copy que escribiste y quieres que los agentes revisen

Con eso el sistema tiene todo lo que necesita para correr las 7 evaluaciones y empezar a iterar.
