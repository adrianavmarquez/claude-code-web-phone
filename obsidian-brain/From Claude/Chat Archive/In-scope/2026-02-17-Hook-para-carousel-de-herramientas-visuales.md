---
title: "Hook para carousel de herramientas visuales"
source: claude.ai-chat
created: "2026-02-17 02:43"
summary: "**Conversation Overview**  The person is a content creator working on a carousel format for social media, where each slide recommends a visual reference tool, accompanied by b-roll style videos of themselves. They came to Claude specifically for help with copy, not technical implementation — they redirected Claude early on when Claude initially built a full React hook, clarifying they only needed copywriting assistance.  The carousel covers five visual reference platforms as alternatives to Pinterest: Shotdeck, Frameset, Eyecannndy, Flim, and Cosmos. The person's target audience is content creators, brand owners, and entrepreneurs with personal brands. The creative direction they landed on frames Pinterest as the reason their audience's visual content looks generic or repetitive compared to competitors.  The person provided their own directional copy as a starting point — 'Pinterest arruinó las referencias visuales tuyas y de 5000 personas más' — and Claude iterated from there with multiple headline options. The conversation was conducted in Spanish. The person has not yet selected a final option, but the preferred creative territory is a direct, slightly provocative tone that calls out Pinterest as the cause of looking 'basic' or blending in with competitors."
messages: 8
claude_uuid: "9212337f-d302-4de6-b654-e5f03bbed3b9"
tags: [claude, chat, archive]
---
# Hook para carousel de herramientas visuales

> **Conversation Overview**

The person is a content creator working on a carousel format for social media, where each slide recommends a visual reference tool, accompanied by b-roll style videos of themselves. They came to Claude specifically for help with copy, not technical implementation — they redirected Claude early on when Claude initially built a full React hook, clarifying they only needed copywriting assistance.

The carousel covers five visual reference platforms as alternatives to Pinterest: Shotdeck, Frameset, Eyecannndy, Flim, and Cosmos. The person's target audience is content creators, brand owners, and entrepreneurs with personal brands. The creative direction they landed on frames Pinterest as the reason their audience's visual content looks generic or repetitive compared to competitors.

The person provided their own directional copy as a starting point — "Pinterest arruinó las referencias visuales tuyas y de 5000 personas más" — and Claude iterated from there with multiple headline options. The conversation was conducted in Spanish. The person has not yet selected a final option, but the preferred creative territory is a direct, slightly provocative tone that calls out Pinterest as the cause of looking "basic" or blending in with competitors.

## 🧑 Adriana · 2026-02-17 02:43
ayudame a hacer un hook para un carousel en donde en cada pagina quiero recomendar una herramienta nueva. estara acompanado de videos de fondo estilo broll de mi.

5 páginas para referencias visuales (que no son Pinterest)
1. Shotdeck - Metadata completa: lentes, colorización, equipo usado
2. Frameset - Comerciales y videos musicales, no solo cine
3. Eyecannndy - Busca por transiciones, iluminación, movimientos específicos
4. Flim - Buscador por hex codes y temperatura de luz
5. Cosmos - Curación artística, cero aesthetic genérico

## 🤖 Claude · 2026-02-17 02:44
```javascript
import { useState, useCallback, useRef, useEffect } from 'react';

const useCarousel = (totalPages = 5) => {
  const [currentPage, setCurrentPage] = useState(0);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const touchStartX = useRef(0);
  const touchEndX = useRef(0);
  const videoRefs = useRef([]);

  // Configuración de las herramientas
  const tools = [
    {
      id: 1,
      name: "Shotdeck",
      description: "Metadata completa: lentes, colorización, equipo usado",
      color: "#FF6B6B",
      videoSrc: "/videos/shotdeck-broll.mp4"
    },
    {
      id: 2,
      name: "Frameset",
      description: "Comerciales y videos musicales, no solo cine",
      color: "#4ECDC4",
      videoSrc: "/videos/frameset-broll.mp4"
    },
    {
      id: 3,
      name: "Eyecannndy",
      description: "Busca por transiciones, iluminación, movimientos específicos",
      color: "#FFE66D",
      videoSrc: "/videos/eyecannndy-broll.mp4"
    },
    {
      id: 4,
      name: "Flim",
      description: "Buscador por hex codes y temperatura de luz",
      color: "#A8DADC",
      videoSrc: "/videos/flim-broll.mp4"
    },
    {
      id: 5,
      name: "Cosmos",
      description: "Curación artística, cero aesthetic genérico",
      color: "#F1FAEE",
      videoSrc: "/videos/cosmos-broll.mp4"
    }
  ];

  // Navegar a página específica
  const goToPage = useCallback((pageIndex) => {
    if (pageIndex >= 0 && pageIndex < totalPages && !isTransitioning) {
      setIsTransitioning(true);
      setCurrentPage(pageIndex);
      
      // Resetear transición después de la animación
      setTimeout(() => setIsTransitioning(false), 600);
    }
  }, [totalPages, isTransitioning]);

  // Navegación
  const nextPage = useCallback(() => {
    if (currentPage < totalPages - 1) {
      goToPage(currentPage + 1);
    }
  }, [currentPage, totalPages, goToPage]);

  const prevPage = useCallback(() => {
    if (currentPage > 0) {
      goToPage(currentPage - 1);
    }
  }, [currentPage, goToPage]);

  // Gestos táctiles
  const handleTouchStart = useCallback((e) => {
    touchStartX.current = e.touches[0].clientX;
  }, []);

  const handleTouchMove = useCallback((e) => {
    touchEndX.current = e.touches[0].clientX;
  }, []);

  const handleTouchEnd = useCallback(() => {
    const swipeThreshold = 50;
    const diff = touchStartX.current - touchEndX.current;

    if (Math.abs(diff) > swipeThreshold) {
      if (diff > 0) {
        nextPage(); // Swipe left
      } else {
        prevPage(); // Swipe right
      }
    }
  }, [nextPage, prevPage]);

  // Manejo de videos
  const handleVideoRef = useCallback((index, ref) => {
    videoRefs.current[index] = ref;
  }, []);

  // Pausar/reproducir videos según página activa
  useEffect(() => {
    videoRefs.current.forEach((video, index) => {
      if (video) {
        if (index === currentPage) {
          video.play().catch(err => console.log('Video play error:', err));
        } else {
          video.pause();
        }
      }
    });
  }, [currentPage]);

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'ArrowRight') nextPage();
      if (e.key === 'ArrowLeft') prevPage();
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [nextPage, prevPage]);

  return {
    // Estado
    currentPage,
    isTransitioning,
    totalPages,
    tools,
    
    // Navegación
    goToPage,
    nextPage,
    prevPage,
    
    // Touch handlers
    handleTouchStart,
    handleTouchMove,
    handleTouchEnd,
    
    // Video refs
    handleVideoRef,
    
    // Utilidades
    isFirstPage: currentPage === 0,
    isLastPage: currentPage === totalPages - 1,
    progress: ((currentPage + 1) / totalPages) * 100
  };
};

export default useCarousel;
```

Este hook te da todo lo que necesitas para tu carousel:

**Características principales:**
- ✅ Navegación por swipe (móvil)
- ✅ Navegación por flechas del teclado
- ✅ Control automático de reproducción de videos
- ✅ Prevención de clicks múltiples durante transiciones
- ✅ Indicador de progreso
- ✅ Data de las 5 herramientas incluida

**Uso en tu componente:**

```javascript
import useCarousel from './hooks/useCarousel';

function Carousel() {
  const {
    currentPage,
    tools,
    nextPage,
    prevPage,
    handleTouchStart,
    handleTouchMove,
    handleTouchEnd,
    handleVideoRef,
    isFirstPage,
    isLastPage,
    progress
  } = useCarousel(5);

  return (
    <div 
      className="carousel-container"
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
    >
      {/* Video background */}
      <video
        ref={(ref) => handleVideoRef(currentPage, ref)}
        src={tools[currentPage].videoSrc}
        muted
        loop
        playsInline
      />
      
      {/* Contenido */}
      <h2>{tools[currentPage].name}</h2>
      <p>{tools[currentPage].description}</p>
      
      {/* Navegación */}
      {!isFirstPage && <button onClick={prevPage}>←</button>}
      {!isLastPage && <button onClick={nextPage}>→</button>}
      
      {/* Progress bar */}
      <div style={{ width: `${progress}%` }} />
    </div>
  );
}
```

¿Quieres que agregue alguna funcionalidad adicional como autoplay o animaciones específicas?

## 🧑 Adriana · 2026-02-17 02:55
no no solo quiero ayuda con el cop;y

## 🤖 Claude · 2026-02-17 02:55
¡Ah perfecto! Aquí va el copy para cada página:

## 1. Shotdeck
**Headline:** "Deja de adivinar qué lente usaron"
**Body:** Shotdeck te da metadata completa de cada frame: lente exacto, LUT, cámara, hasta el grip que trabajó ese día. Es como tener el desglose técnico de tu película favorita.

## 2. Frameset
**Headline:** "El cine no es la única referencia"
**Body:** Frameset cataloga comerciales, videos musicales y branded content. Porque a veces la estética que buscas está en un anuncio de Nike, no en Blade Runner.

## 3. Eyecannndy
**Headline:** "Busca por lo que realmente importa"
**Body:** ¿Necesitas referencias de transiciones suaves? ¿Iluminación de contraluz? ¿Movimientos de cámara específicos? Eyecannndy busca por técnica, no por película.

## 4. Flim
**Headline:** "Tu paleta de color tiene un código"
**Body:** Flim te deja buscar por hex codes y temperatura de luz. Encontraste el tono perfecto en un frame? Ahora puedes buscar más escenas con esa misma paleta.

## 5. Cosmos
**Headline:** "Curación real, cero algoritmo genérico"
**Body:** Cosmos es curado por humanos que saben de cine. Aquí no hay "aesthetic" de TikTok, solo referencias con criterio artístico real.

---

**Alternativas más cortas/punchy:**

**Shotdeck:** "Para de googlear 'what lens was used in...'"

**Frameset:** "Las mejores referencias no están en el cine"

**Eyecannndy:** "Busca por técnica, no por título"

**Flim:** "#FF5733 = tu nueva forma de buscar referencias"

**Cosmos:** "Aesthetic real > Aesthetic de algoritmo"

¿Quieres que ajuste el tono? ¿Más casual, más técnico, más storytelling?

## 🧑 Adriana · 2026-02-17 02:55
no, quiero que sea la portada con el hook o headline: 5 páginas para referencias visuales (que no son Pinterest)

## 🤖 Claude · 2026-02-17 02:56
¡Ahhhh ya entendí! Quieres el copy para la **página de portada** que introduce el carousel completo. Aquí van opciones:

---

## Opción 1 - Directo al punto
**Headline:** "5 páginas para referencias visuales (que no son Pinterest)"
**Subheadline:** Herramientas que realmente usan los directores de fotografía

---

## Opción 2 - Problema/Solución
**Headline:** "Pinterest arruinó las referencias visuales"
**Subheadline:** 5 herramientas que usan los DP's de verdad (y por qué no son Pinterest)

---

## Opción 3 - Más narrativo
**Headline:** "Si sigues buscando referencias en Pinterest, estamos en problemas"
**Subheadline:** 5 bases de datos que cambiaron cómo armo mis moodboards

---

## Opción 4 - Provocador
**Headline:** "Pinterest es para bodas, no para cinematografía"
**Subheadline:** 5 herramientas profesionales que deberías estar usando

---

## Opción 5 - Simple y educativo
**Headline:** "5 páginas para referencias visuales (que no son Pinterest)"
**Subheadline:** Metadata real, búsquedas técnicas, curación profesional

---

## Opción 6 - Personal (mi favorita)
**Headline:** "Dejé Pinterest hace 2 años"
**Subheadline:** Estas 5 herramientas son lo que uso ahora para encontrar referencias

---

¿Cuál va más con tu vibe? ¿O quieres que ajuste alguna?

## 🧑 Adriana · 2026-02-17 02:57
si mi audienci son creadores de contenido, duenos de marca o emprendedores con marcas personales. 

pienso que deberia abordarlo algo como:

Pinterest es lo que esta haciendo que te veas basic, o repetido o algo asi. 
Pinterest arruinó las referencias visuales tuyas y de 5000 personas mas.Subheadline: 5 herramientas que usan los DP's de verdad (y por qué no son Pinterest)

## 🤖 Claude · 2026-02-17 02:57
¡PERFECTO! Esa dirección es mucho mejor para tu audiencia. Aquí van opciones refinadas:

---

## Opción 1 - Golpe directo
**Headline:** "Pinterest es por eso que tu marca se ve igual a las otras 5,000"
**Subheadline:** 5 herramientas que separan contenido profesional de contenido repetido

---

## Opción 2 - Problema claro
**Headline:** "Pinterest arruinó tus referencias visuales (y las de todos los demás)"
**Subheadline:** 5 páginas que usan los creadores que NO se ven basic

---

## Opción 3 - Más aspiracional
**Headline:** "Tu competencia usa Pinterest. Tú no deberías."
**Subheadline:** 5 herramientas de referencia visual que te sacan del montón

---

## Opción 4 - Call out fuerte
**Headline:** "Si tus referencias vienen de Pinterest, ya perdiste"
**Subheadline:** 5 bases de datos que usan marcas que SÍ destacan visualmente

---

## Opción 5 - Más educativo pero directo (mi favorita para tu audience)
**Headline:** "Pinterest te está haciendo ver básico"
**Subheadline:** 5 herramientas de referencias visuales que tu competencia no conoce

---

## Opción 6 - Exclusividad
**Headline:** "Mientras todos buscan en Pinterest, yo busco aquí"
**Subheadline:** 5 páginas para referencias visuales que elevan tu marca

---

¿Cuál resuena más con el tono que quieres dar? ¿O hacemos un mix?
