---
title: "Yapping instructions for scripting"
source: claude.ai-chat
created: "2026-04-10 02:30"
summary: "**Conversation overview**  The person, who goes by @adrianavmarquez, worked with Claude to build a scripting methodology and workflow tool for content creation. The conversation began with a request to adapt 'yapping on camera' instructions into a scripting-focused document, resulting in a branded .docx file called 'Yapping on Script' — a five-instruction guide for writing scripts that sound conversational, based on Tom Boyd's method. The document used her brand palette (red D72323, blue 3846C4, yellow FFBA35) with Poppins font, formatted as an editorial table with a checklist question per instruction.  She then requested that this be packaged as a reusable skill file (.skill format), and further evolved the concept from a static document into a full interactive workflow. The key additions she specified were: Claude must first ask for links to five small creators (under 10K followers) before touching any script; every session must extract and save opening lines to a growing database in memory using the `[APERTURA DB]` tag format; script review must check for POV before correcting anything; the corrected script must always include a rhythm and breathing map showing where pauses go and why; and revisions are capped at exactly five rounds with no exceptions — on revision five, Claude closes the session and refuses further changes. The final skill was repackaged incorporating all of this logic as a sequenced five-step workflow with memory accumulation across sessions."
messages: 6
claude_uuid: "77147ada-3f3d-4d3a-acfa-504f01f39df9"
tags: [claude, chat, archive]
---
# Yapping instructions for scripting

> **Conversation overview**

The person, who goes by @adrianavmarquez, worked with Claude to build a scripting methodology and workflow tool for content creation. The conversation began with a request to adapt "yapping on camera" instructions into a scripting-focused document, resulting in a branded .docx file called "Yapping on Script" — a five-instruction guide for writing scripts that sound conversational, based on Tom Boyd's method. The document used her brand palette (red D72323, blue 3846C4, yellow FFBA35) with Poppins font, formatted as an editorial table with a checklist question per instruction.

She then requested that this be packaged as a reusable skill file (.skill format), and further evolved the concept from a static document into a full interactive workflow. The key additions she specified were: Claude must first ask for links to five small creators (under 10K followers) before touching any script; every session must extract and save opening lines to a growing database in memory using the `[APERTURA DB]` tag format; script review must check for POV before correcting anything; the corrected script must always include a rhythm and breathing map showing where pauses go and why; and revisions are capped at exactly five rounds with no exceptions — on revision five, Claude closes the session and refuses further changes. The final skill was repackaged incorporating all of this logic as a sequenced five-step workflow with memory accumulation across sessions.

## 🧑 Adriana · 2026-04-10 02:30
make this a yapping instructions for scripting
> 📎 Instrucciones_para_hablar_a_la_cámara_(Yapping_on_camera).docx

## 🤖 Claude · 2026-04-10 02:32
Ahora voy a crear el documento. Primero déjame entender bien qué necesitas: tomar esas 5 instrucciones de "yapping on camera" y adaptarlas para **scripting** (no para hablar en cámara, sino para escribir guiones).

Aquí lo tienes. **Yapping on Script** adaptado desde las instrucciones de Tom Boyd para el proceso de guionización, no de cámara.

Lo que cambié del original:

El enfoque pasó de "cómo te comportas frente a cámara" a "cómo construyes el guión antes de grabar." Cada instrucción ahora tiene una pregunta de cierre que funciona como checklist mientras escribes, y el lenguaje apunta al momento de escritura, no al de grabación. El marco se mantiene igual (estudia outliers, analiza aperturas, prueba el POV, estudia el ritmo, prioriza volumen) pero anclado a la página, no al set.

## 🧑 Adriana · 2026-04-10 03:31
ok make it a skill for yapping-scripting

## 🤖 Claude · 2026-04-10 03:33
Voy a crear la skill. Tengo todo el contexto de la conversación: el doc original, la adaptación al scripting, tu flujo de trabajo. Lo construyo ahora.

Ahora la empaqueto:

Lista. La skill `yapping-scripting` está empaquetada y contiene:

**Lo que hace:** Cuando le pidas "hazme las instrucciones de scripting", "arma el yapping on script" o cualquier variación, Claude lee la skill, toma el contenido canónico de las 5 instrucciones, y genera el .docx con toda la estética de marca lista para descargar.

**Lo que tiene adentro:**
- Las 5 instrucciones base en una tabla de referencia, con título, subtítulo, cuerpo y pregunta de cierre para cada una
- Las specs exactas de diseño: colores hex, tamaños, estructura de tabla, jerarquía de bloques
- Reglas de cuándo actualizar vs. regenerar (si cambias una instrucción, si agregas una nueva, si quieres PDF)
- Advertencias técnicas para evitar errores de parsing en Node.js

La próxima vez que necesites el doc, solo dime "hazme el yapping on script" y lo genera directo sin tener que explicar nada.

## 🧑 Adriana · 2026-04-10 03:48
si yo le pido hacer esto faltaria agregar que me tiene primero que pedir el link de 5 perfiles de creadores pqeuenos para que haga el paso 1, y cada vez que hagamos esta dinamica debe agregar a su database las aperturas de los best performing videos, asi las va coleccionando. luego de que corrija mi guion o mi draft de la idea basado en lo que estudio, colecciono y que se preunte, este guion itnee un punti de vista? debe indicarme donde haran pausas, donde el video respira. y no dejarme perfeccionarlo o hacerle modificaciones mas de 5 veces

## 🤖 Claude · 2026-04-10 03:50
Buenísima idea. Estás convirtiendo esto de un doc estático a un **workflow interactivo** con memoria acumulativa. Déjame actualizar la skill con toda esa lógica.

Actualizada. Esto es lo que cambió vs. la versión anterior:

**La skill ahora es un workflow, no un doc.** Cada vez que arranques una sesión de guionización, el proceso es este:

1. **Pide los 5 links primero.** No toca el guión hasta tenerlos. Analiza los best-performing de cada perfil y extrae patrones de apertura.

2. **Guarda todo en memoria.** Cada apertura nueva se agrega a `[APERTURA DB]` con handle, tipo de hook, texto, promesa y plataforma. Al inicio de cada sesión nueva, recupera la base completa y te dice cuántas aperturas tienes y qué patrones dominan.

3. **Revisa el guión en 3 capas:** primero verifica que tenga POV (si no lo hay, para y pregunta antes de corregir nada), luego compara la apertura contra la base de datos, luego corrige respetando tu voz al 100%.

4. **Siempre entrega el mapa de ritmo.** Cada guión corregido viene con el mapa de pausas, velocidades y momentos de respiración explicados.

5. **Contador de revisiones visible.** Cada cambio que pidas te dice "Revisión 2 de 5." A la quinta, cierra la sesión y no negocia.
