# Biblioteca de memoria por marca

Este directorio guarda la memoria persistente de cada proyecto o marca.
Sirve para que, al iniciar una sesión, se pueda cargar el contexto de una
marca sin empezar de cero.

## Estructura

- `_plantilla-marca.md`: plantilla base. Toda marca nueva se copia de aquí.
- `marcas/`: un archivo `.md` por marca (ej. `marcas/mi-marca.md`).
- `indice.md`: lista de todas las marcas registradas y su estado.

## Flujo de trabajo

1. Abre cada Proyecto en Claude web y ejecuta el prompt de extracción.
2. Pega el resultado en el chat de Claude Code.
3. Se crea o actualiza `marcas/<marca>.md` con ese contenido.
4. Para trabajar en una marca, di "trabajemos en <marca>" y se lee su archivo.
