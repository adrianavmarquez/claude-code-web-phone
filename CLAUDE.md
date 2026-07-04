# Preferencias del proyecto

## Estilo de escritura

- PROHIBIDO usar el guion largo (em dash) en cualquier texto que escribas: respuestas de chat, contenido generado, comentarios de código, mensajes de commit, descripciones, etc. Nunca uses el carácter guion largo.
- En su lugar, reescribe la frase: usa punto y seguido, coma, dos puntos, paréntesis o "y"/"pero" según corresponda.

## Protocolo de memoria de marcas

- La memoria persistente de cada marca vive en `memoria/marcas/<marca>.md`.
- Cuando el usuario diga "trabajemos en <marca>" o mencione una marca registrada, lee su archivo en `memoria/marcas/` antes de responder.
- Consulta `memoria/indice.md` para saber qué marcas existen.
- Cuando el usuario pegue la memoria extraída de un Proyecto de Claude web, crea o actualiza `memoria/marcas/<marca>.md` usando `memoria/_plantilla-marca.md` como estructura, y añade la marca a `memoria/indice.md`.
- Cuando se tome una decisión o preferencia importante de una marca, regístrala en su archivo de memoria.
