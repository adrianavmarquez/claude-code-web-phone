---
title: "Agregar dominio a Netlify"
source: claude.ai-chat
created: "2026-04-01 18:27"
summary: "**Conversation Overview**  The person asked how to add a custom domain to Netlify. Claude provided a step-by-step guide covering two main phases: adding the domain within the Netlify dashboard and configuring DNS settings. Claude explained two DNS configuration options — using Netlify DNS (recommended, where nameservers are transferred to Netlify) or maintaining an external DNS provider (using an A record for the root domain and a CNAME record for the www subdomain). Claude also noted that HTTPS is handled automatically by Netlify after setup and that DNS propagation can take up to 48 hours. The conversation ended with Claude asking which domain registrar the person uses in order to provide more specific instructions."
messages: 2
claude_uuid: "3f58072a-ff45-414f-9090-16f45741a6ab"
tags: [claude, chat, archive]
---
# Agregar dominio a Netlify

> **Conversation Overview**

The person asked how to add a custom domain to Netlify. Claude provided a step-by-step guide covering two main phases: adding the domain within the Netlify dashboard and configuring DNS settings. Claude explained two DNS configuration options — using Netlify DNS (recommended, where nameservers are transferred to Netlify) or maintaining an external DNS provider (using an A record for the root domain and a CNAME record for the www subdomain). Claude also noted that HTTPS is handled automatically by Netlify after setup and that DNS propagation can take up to 48 hours. The conversation ended with Claude asking which domain registrar the person uses in order to provide more specific instructions.

## 🧑 Adriana · 2026-04-01 18:30
como agrego mi dominio a netlify ?

## 🤖 Claude · 2026-04-01 18:30
Aquí va el paso a paso:

**Dentro de Netlify:**

1. Ve a tu proyecto en el dashboard de Netlify.
2. En el menú lateral izquierdo, selecciona **Domain management** (o "Domain settings" en versiones anteriores).
3. Haz clic en **Add custom domain**, escribe tu dominio y confírmalo. Aunque Netlify diga que ya está registrado, selecciona **Add Domain** de todas formas.

**Tienes dos opciones para el DNS:**

**Opción A: Usar Netlify DNS (recomendado, todo en un lugar)**

En la configuración del dominio, busca el dominio sin el subdominio "www" y haz clic en **Check DNS configuration**. Ahí selecciona **Setup Netlify DNS**. Netlify te dará una lista de nameservers. Luego ve a tu proveedor de dominio (GoDaddy, Namecheap, etc.), entra a la configuración de DNS y reemplaza los nameservers actuales por los que te dio Netlify.

**Opción B: Mantener tu DNS externo (más control)**

Para dominio raíz (ejemplo.com), agrega un registro **A** apuntando a la IP de Netlify. Para el subdominio "www", agrega un registro **CNAME** que apunte al dominio que Netlify te asignó automáticamente (ej. algo-random.netlify.app).

**Después de configurar el DNS:**

Una vez hecho todo, Netlify agrega automáticamente HTTPS a tu sitio, no hay que preocuparse por eso. El proceso de propagación DNS puede tomar desde unos minutos hasta 48 horas dependiendo del proveedor.

¿Con qué proveedor compraste tu dominio? (GoDaddy, Namecheap, Squarespace, etc.) Te puedo dar los pasos más específicos para ese panel.
