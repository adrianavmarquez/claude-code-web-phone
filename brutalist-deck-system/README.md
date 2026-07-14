# Sistema de Decks Brutalista v2 · Creatividad²

El **deck madre hecho código**: un sistema de diseño de presentaciones vivo,
interactivo y didáctico para @adrianavmarquez. Pensado para pasárselo a Claude y
que salgan decks con criterio, no con plantilla genérica.

## Qué hay aquí

- **[`index.html`](index.html)** — el sistema completo en un solo archivo
  self-contained (fuentes reales incrustadas, sin dependencias externas). Ábrelo
  en cualquier navegador o publícalo como Artifact de Claude. Contiene:
  - **A · El motor** — un deck real de ejemplo ("Anti-Strategy 101", 14 slides)
    renderizado con las reglas del sistema. Navega con flechas / botones / swipe.
    - **Modo QA** superpone la caja de seguridad y los márgenes.
    - Panel didáctico que explica cada slide en vivo (familia, regla, fuente de
      color, checklist de QA).
    - Movimiento nativo: contador que sube en los datos, scribbles que se dibujan,
      barras que crecen, dona que se rellena, estrella firma.
  - **B · Las 24 familias** — el catálogo. Las marcadas *EN VIVO* saltan al motor.
  - **C · Tokens** — 9 colores (click para copiar hex), la escala tipográfica
    violenta a tamaño real, los roles fijos del kit de assets, la estrella de marca
    y las dos trampas (papeles que no son blancos, PNG sin proporción compartida).
  - **D · Movimiento + interacción** — la capa que le faltaba a la v2 estática.
    Seis patrones de motion brutalista con demos en vivo.
  - **E · QA por slide** — el checklist interactivo previo a exportar.
  - **F · El prompt para Claude** — el sistema entero destilado en instrucciones,
    copiable con un botón.

- **[`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)** — ese mismo prompt como archivo, más los
  tokens en CSS y el SVG de la estrella listos para pegar.

## Cómo se usa con Claude

1. Copia el contenido de `SYSTEM-PROMPT.md` (o el bloque del panel F) en un Project
   de Claude, o al inicio de una conversación.
2. Pídele el deck: *"Hazme un deck de 8 slides sobre [tema], módulo [N]."*
3. Claude devuelve HTML self-contained navegable, siguiendo la regla madre, la escala
   y las familias. Revisa contra el checklist de QA antes de exportar.

## Notas de implementación

- Tipografía dimensionada en **container query units (cqw)** para que escale con el
  escenario sin desbordar. El alto de un 16:9 es 56.25cqw.
- Fuentes open-source (OFL) incrustadas como data URIs: Archivo Black, Poppins,
  Caveat, Playfair Display. Nada se carga de un CDN.
- Tema único comprometido (sin dark mode): el deck trae su propia lógica de fondo
  papel/negro. Respeta `prefers-reduced-motion`.
- La estrella de marca es el placeholder SVG autorizado hasta la versión iPad.
