---
title: "Higgs field prompt builder"
source: claude.ai-chat
created: "2026-07-02 00:03"
summary: "**Conversation Overview**  The person, who goes by Adri (@adrianavmarquez), is a content creator and brand owner with a detailed brand identity system already on file. Her brand uses a black-and-white dominant palette with accent colors (red, yellow, blue, lavender), specific font stack (Poppins Bold, Scholar, Heading Now, Glenda Sans, Plunct), and a mixed-media visual language incorporating hand-painted elements, pixel art, stickers, brand characters (El Perro, Clones, Emociones), and gold textures. Claude has her full brand spec pre-loaded and confirmed it as context for all design work.  The conversation covered two distinct tasks. First, Claude ran a structured intake form for a Higgsfield AI image/video prompt builder, presenting 18 questions across five sections (the piece, the message, visuals, style/energy, and technical specs) designed to generate a complete JSON prompt. Claude noted it would tailor the output to specific Higgsfield models (Soul, Nano Banana Pro, or Marketing Studio) once Adri answered. The intake form was presented but not yet completed by Adri in this session. Second, Adri attempted to run `npx skillfish add tenequm/claude-plugins skill` in the chat, which Claude identified as having two issues: the command was pasted into the chat sandbox rather than her terminal, and the repo had been renamed to `tenequm/skills` with an invalid skill name argument. Claude enumerated all 32 available skills from that repo via the GitHub API and provided corrected installation syntax.  Adri then uploaded `finding-skills-1_0_0_tar.gz` and asked Claude to install it. Claude extracted, reviewed, and security-audited the package (a Claude Code skill that queries a local JSON database and the SkillsMP API to recommend other skills), confirmed it was clean (GET-only network calls, no subprocess/eval/exec/file writes), ran a smoke test, repackaged it as `finding-skills.zip` with correct folder structure, and delivered it as a downloadable file with installation instructions for both `~/.claude/skills/` (global) and project-local paths. Claude flagged that the SKILL.md is written entirely in Korean and offered to rewrite it in Adri's Spanglish register. Claude consistently communicated in Caribbean Spanglish with English industry terms, matching Adri's register throughout.  **Tool Knowledge**  Claude used `bash_tool` and `web_search` extensively in this session. For GitHub repo enumeration, the pattern `curl -sL https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1` with `-L` to follow redirects reliably returns full file trees; without `-L`, renamed repos return a 301 and the tree call fails silently. Filtering that tree for paths ending in `skill.md` (case-insensitive) is the correct way to enumerate skills in any skillfish-compatible repo. The `skillfish add --list` flag does not exist in the current CLI version; interactive skill selection or `--all` are the supported install modes. For npm operations in this sandbox, the `.npmrc` prefix setting conflicts with global installs and must be overridden via `export npm_config_prefix=/home/claude/.npm-global` before running `npx` commands. The `finding-skills` skill's search script accepts positional query string, `--limit`, and `--format text` flags and successfully returns live results from `skillsmp.com/api/skills`."
messages: 6
claude_uuid: "1c599d7d-37a3-4788-8c9f-172121ac2843"
tags: [claude, chat, archive]
---
# Higgs field prompt builder

> **Conversation Overview**

The person, who goes by Adri (@adrianavmarquez), is a content creator and brand owner with a detailed brand identity system already on file. Her brand uses a black-and-white dominant palette with accent colors (red, yellow, blue, lavender), specific font stack (Poppins Bold, Scholar, Heading Now, Glenda Sans, Plunct), and a mixed-media visual language incorporating hand-painted elements, pixel art, stickers, brand characters (El Perro, Clones, Emociones), and gold textures. Claude has her full brand spec pre-loaded and confirmed it as context for all design work.

The conversation covered two distinct tasks. First, Claude ran a structured intake form for a Higgsfield AI image/video prompt builder, presenting 18 questions across five sections (the piece, the message, visuals, style/energy, and technical specs) designed to generate a complete JSON prompt. Claude noted it would tailor the output to specific Higgsfield models (Soul, Nano Banana Pro, or Marketing Studio) once Adri answered. The intake form was presented but not yet completed by Adri in this session. Second, Adri attempted to run `npx skillfish add tenequm/claude-plugins skill` in the chat, which Claude identified as having two issues: the command was pasted into the chat sandbox rather than her terminal, and the repo had been renamed to `tenequm/skills` with an invalid skill name argument. Claude enumerated all 32 available skills from that repo via the GitHub API and provided corrected installation syntax.

Adri then uploaded `finding-skills-1_0_0_tar.gz` and asked Claude to install it. Claude extracted, reviewed, and security-audited the package (a Claude Code skill that queries a local JSON database and the SkillsMP API to recommend other skills), confirmed it was clean (GET-only network calls, no subprocess/eval/exec/file writes), ran a smoke test, repackaged it as `finding-skills.zip` with correct folder structure, and delivered it as a downloadable file with installation instructions for both `~/.claude/skills/` (global) and project-local paths. Claude flagged that the SKILL.md is written entirely in Korean and offered to rewrite it in Adri's Spanglish register. Claude consistently communicated in Caribbean Spanglish with English industry terms, matching Adri's register throughout.

**Tool Knowledge**

Claude used `bash_tool` and `web_search` extensively in this session. For GitHub repo enumeration, the pattern `curl -sL https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1` with `-L` to follow redirects reliably returns full file trees; without `-L`, renamed repos return a 301 and the tree call fails silently. Filtering that tree for paths ending in `skill.md` (case-insensitive) is the correct way to enumerate skills in any skillfish-compatible repo. The `skillfish add --list` flag does not exist in the current CLI version; interactive skill selection or `--all` are the supported install modes. For npm operations in this sandbox, the `.npmrc` prefix setting conflicts with global installs and must be overridden via `export npm_config_prefix=/home/claude/.npm-global` before running `npx` commands. The `finding-skills` skill's search script accepts positional query string, `--limit`, and `--format text` flags and successfully returns live results from `skillsmp.com/api/skills`.

## 🧑 Adriana · 2026-07-02 00:03
/higgsfield-prompt-builder

## 🤖 Claude · 2026-07-02 00:04
Listo. Ya cargué tu brand context desde el manual que subiste, así que no tienes que re explicar nada de la identidad visual. Lo que tengo pre cargado como default:

- **Marca:** Adriana V. Márquez / @adrianavmarquez
- **Colores:** dominantes negro #000000 y blanco #FFFFFF. Relleno solo para acento: rojo #D72323, amarillo #FFBA35, azul #3846C4, lavender #F2E9FF
- **Fuentes:** Poppins Bold (títulos), Scholar (subtítulos), Heading Now (cuerpo), Glenda Sans (captions), Plunct handwritten (personalidad)
- **Logo:** estrella roja pintada + wordmark "adrianavmarquez" handwritten amarillo. Monogram AM cuadrado
- **Elementos:** stickers, estrellas, sparkles, pixel 8 bit, memes, personajes (Adri, El Perro, Clones, Emociones). Energía mixed media: pintado a mano, fieltro, oro, pixel art

Ahora contéstame solo lo que es específico de esta pieza. Lo que no aplique, escribe "skip" o déjalo en blanco.

---

## PROMPT BUILDER. Intake Form

**SECCIÓN 1. LA PIEZA**

1. ¿Qué estamos haciendo? (ej: post de Instagram, static ad, email header, slide de deck, mockup de producto, ilustración, logo lockup, carrusel, story, banner)
2. ¿Cuál es el objetivo de este diseño? (ej: generar clicks, anunciar un launch, construir deseo, explicar un feature, crecer followers)
3. ¿A quién le habla? (Describe a la persona que lo ve. Edad, mindset, en qué momento está)

---

**SECCIÓN 2. EL MENSAJE**

4. ¿Cuál es el headline o mensaje principal? (Lo único más importante que dice este diseño)
5. ¿Hay subheading o mensaje secundario? (Opcional. Tiene que sumar algo nuevo, no repetir el headline)
6. ¿Hay body copy? (Opcional. Texto de apoyo corto, 1 a 3 oraciones máximo)
7. ¿Hay CTA? (Opcional. Qué acción quieres. Ej: "DM us", "Link en bio", "Descarga gratis")

---

**SECCIÓN 3. LO VISUAL**

8. ¿Cuál es el visual hero? (Dónde cae el ojo primero. Ej: producto, persona, statement tipográfico, escena, ilustración)
9. ¿Qué elementos quieres incluir? (Lista específica: foto tuya, El Perro, estrella pintada, textura, pixel art, badge, etc.)
10. ¿Cómo se siente la composición? (Ej: centrada y minimal, editorial con tensión, full bleed lifestyle, flat lay, crop cerrado, ángulo dinámico)
11. ¿Cuál es el fondo? (Ej: negro sólido, blanco, lavender, textura, escena lifestyle, gradiente, transparente)
12. ¿Qué luz o mood? (Ej: luz natural suave, studio limpio, golden hour, moody y dramático, bright y airy)

---

**SECCIÓN 4. ESTILO Y ENERGÍA**

13. ¿Qué estilo de diseño gráfico? (Ej: editorial, minimal, maximalista, brutalist, orgánico, luxury, playful, clean commercial, handcrafted)
14. ¿Cuál es el sentiment o tono emocional? (Ej: confident, urgente, cálido, aspiracional, rebelde, joyful)
15. ¿Hay variation vectors? (Opcional. Qué quieres que explore en versiones distintas. Ej: dos opciones de color, headline en dos posiciones, versión con foto vs versión solo tipográfica)

---

**SECCIÓN 5. TÉCNICO**

16. ¿Aspect ratio o formato? (Ej: 1:1 square, 4:5 portrait, 9:16 story, 16:9 landscape, custom)
17. ¿Para qué plataforma u output? (Ej: feed de Instagram, Meta ads, Pinterest, email, print, deck)
18. ¿Algo que evitar o que quede off limits? (Palabras, visuales, colores, estilos o referencias que se sentirían mal)

---

Un par de cosas antes de que llenes:

Como esto va para **Higgsfield**, cuando me devuelvas las respuestas te armo el JSON completo y el `full_image_generation_prompt` afinado para el modelo que uses (Soul si es contigo en cámara, Nano Banana Pro si es 4K con texto renderizado, Marketing Studio si es ad de producto). Si ya sabes cuál modelo, dímelo en la respuesta y calibro el prompt a ese motor. Si no, te lo dejo genérico y decidimos después.

Contéstame por número y arrancamos.

## 🧑 Adriana · 2026-07-02 00:07
npx skillfish add tenequm/claude-plugins skill

## 🤖 Claude · 2026-07-02 00:09
Ojo con dos cosas antes de que corras eso.

Primero déjame ver qué trae ese repo, porque lo puedo listar sin instalar nada.

Ese `--list` no existe en la versión actual. Déjame mirar el repo directo en GitHub para ver qué skills trae y cómo se llaman de verdad.

Ya lo desmenucé. Dos cosas antes de correr eso, más un dato que cambia el comando entero.

**1. Este chat no es tu terminal.** El sandbox de esta conversación es efímero y no está conectado a tu Claude Code real (`~/.claude`) ni a tus skills de claude.ai. Si corres `npx skillfish` aquí, instala en un contenedor que se borra y no sincroniza con tu setup. Este comando va en tu máquina, no aquí.

**2. El repo se renombró y tu comando falla como está escrito.** `tenequm/claude-plugins` ahora es **`tenequm/skills`** (GitHub redirige, pero el nombre canónico cambió). Y el `skill` al final no es un placeholder: en skillfish la sintaxis es `add <repo> [skill-name]`, así que estarías pidiendo instalar un skill que se llama literalmente "skill". Ese no existe en el repo, así que te va a tirar "not found".

**Lo que el repo sí tiene: 32 skills**, todas dev y web3 (descripción oficial: "Agent skills for building, shipping, and growing software products"):

- **Lenguajes/frameworks:** typescript-dev, python-dev, go-dev, rust-dev, effect-ts, tanstack, swift-macos, chrome-extension-wxt, cloudflare-workers, foundry-solidity, grafana-foundation-sdk, lance-format
- **Web3/crypto:** solana-development, privy-integration, x402, erc-8004, web3-protocol-gtm
- **Tooling/meta:** gh-cli, command-skill-creator, skills-best-practices, update-skill, mcp-best-practices, review-github-pr, reset-context-contamination, standard-readme, audio-quality-check, download-webpage-as-pdf
- **Writing/founder:** impactful-writing, polish, deep-research-glim, founder-playbook, mpp

De todo eso, lo único que roza tu mundo (no el de tu dev) sería `impactful-writing`, `polish`, `deep-research-glim`, `command-skill-creator` o `skills-best-practices`. El resto es puro código y cadena.

**Comandos correctos, para correr en tu terminal:**

```bash
# un skill específico por nombre exacto
npx skillfish add tenequm/skills impactful-writing --global

# elegir de una lista interactiva
npx skillfish add tenequm/skills --global

# todo el repo (no lo recomiendo, es casi todo dev)
npx skillfish add tenequm/skills --all --global
```

`--global` lo manda a `~/.claude` (visible en todos tus proyectos). Cambia a `--project` si lo quieres solo en la carpeta actual.

Un apunte de seguridad que el propio skillfish da: no verifica skills de terceros, así que revisa el SKILL.md antes de instalar. Si quieres, te leo el contenido de cualquiera de esos 32 aquí mismo para que decidas antes de bajarlo. ¿Cuál te abro?

## 🧑 Adriana · 2026-07-02 00:11
install this

## 🤖 Claude · 2026-07-02 00:13
Revisé el paquete completo antes de tocarlo. Está limpio. Déjame validar el resto y armártelo listo para instalar.

Hecho. No lo puedo instalar en tu entorno real desde este chat (el sandbox de aquí es efímero y no toca tu `~/.claude` ni tus skills de claude.ai), así que hice lo siguiente: lo abrí, lo revisé de seguridad, lo probé funcionando, y te lo empaqueté limpio y listo para soltar. Arriba te dejé el zip.

**Qué es:** un skill de Claude Code llamado `finding-skills`. Recomienda otros skills/plugins de Claude Code cruzando una base local (`external-skills-database.json`, actualizada 2026-01-04, con skills oficiales + comunidad) y una búsqueda en vivo contra la API de **SkillsMP** vía un script Python. Se activa cuando pides "búscame un skill para PDF / Git / code review", etc.

**Revisión de seguridad, veredicto limpio:**
- El script solo hace un GET a `skillsmp.com/api/skills`, parsea el JSON e imprime. Timeout de 10s.
- Cero `subprocess`, `eval`, `exec`, escritura de archivos, lectura de env vars o exfiltración. Nada raro.
- Lo corrí en prueba y responde bien (me trajo resultados reales de "pdf").

**Un flag importante:** todo el SKILL.md está escrito en coreano. Funciona igual, pero cuando se dispare te va a responder en coreano salvo que lo edites. Si quieres te lo reescribo en tu Spanglish y de paso lo adapto a tu voz, es rápido.

**Cómo instalarlo de verdad, en tu terminal.** Usa el zip que te di (ya viene envuelto en la carpeta `finding-skills/` con el nombre correcto):

```bash
# global, disponible en todos tus proyectos
unzip finding-skills.zip -d ~/.claude/skills/

# o solo en el proyecto actual
unzip finding-skills.zip -d ./.claude/skills/
```

Reinicia la sesión de Claude Code y debería aparecer. Si prefieres el tar original en vez del zip:

```bash
mkdir -p ~/.claude/skills/finding-skills
tar -xzf finding-skills-1_0_0_tar.gz -C ~/.claude/skills/finding-skills
```

Si lo que querías era subirlo como skill de **claude.ai** (para usarlo en la app web como tus otros user skills, no en Claude Code), eso va por la sección de Skills en settings subiendo el zip. No te doy los pasos exactos de memoria porque el flujo cambia seguido. Dime si esa es la ruta y te confirmo el proceso actual desde los docs de Anthropic.

¿Te lo dejo en coreano tal cual o te lo traduzco a tu Spanglish antes de que lo instales?
