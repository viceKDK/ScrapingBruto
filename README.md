# ScrapingBruto

Análisis y scraping del juego web "La Brute" para recrear una versión propia inspirada en el juego original.

## Descripción

Este proyecto contiene scripts de análisis y documentación técnica del juego web La Brute (https://brute.eternaltwin.org/). El objetivo es entender la estructura, características y arquitectura del juego para poder crear una versión propia con modificaciones y mejoras.

**IMPORTANTE**: Este proyecto es solo para propósitos educativos y de aprendizaje. No se deben copiar directamente assets, código o contenido protegido por derechos de autor del juego original.

## Estructura del Proyecto

```
ScrapingBruto/
├── scraped_data/           # Datos scrapeados (no incluidos en git)
│   ├── page.html          # HTML de la página principal
│   ├── structure.json     # Estructura analizada
│   ├── js_analysis.json   # Análisis del JavaScript
│   └── assets/            # CSS, JS, iconos descargados
├── scraper.py             # Script principal de scraping
├── download_assets.py     # Script para descargar assets
├── analyze_js.py          # Script para analizar JavaScript
├── ANALISIS_BRUTO.md      # Documento de análisis general
├── REFERENCIA_TECNICA.md  # Referencia técnica detallada
├── requirements.txt       # Dependencias de Python
└── README.md             # Este archivo
```

## Instalación

### Requisitos
- Python 3.8+
- pip

### Pasos

1. Clonar el repositorio:
```bash
git clone https://github.com/viceKDK/ScrapingBruto.git
cd ScrapingBruto
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### 1. Scrapear la página principal

```bash
python scraper.py
```

Este script:
- Obtiene el HTML de la página principal
- Analiza la estructura (scripts, CSS, imágenes, etc.)
- Guarda los resultados en `scraped_data/`

### 2. Descargar assets (CSS, JS, iconos)

```bash
python download_assets.py
```

Este script descarga:
- Archivos CSS
- Archivos JavaScript
- Iconos y favicons
- Manifest.json

### 3. Analizar el JavaScript

```bash
python analyze_js.py
```

Este script extrae:
- Endpoints de la API
- Rutas de la aplicación
- Nombres de componentes React
- LocalStorage keys
- WebSocket URLs (si los hay)

## Documentación

### Documentos Principales

1. **ANALISIS_BRUTO.md**
   - Información general del juego
   - Arquitectura técnica
   - Fuentes personalizadas
   - Recomendaciones para recrear el juego

2. **REFERENCIA_TECNICA.md**
   - Características detalladas del juego
   - Todos los endpoints de la API documentados
   - Rutas de la aplicación
   - LocalStorage keys
   - Stack tecnológico recomendado
   - Plan de desarrollo por fases

## Características Detectadas del Juego

### Sistema de Juego
- ✓ Sistema de personajes (Brutes)
- ✓ Combate 1v1 y torneos
- ✓ Sistema de clanes y guerras
- ✓ Logros y rankings
- ✓ Sistema de eventos
- ✓ Inventario de items

### Características Técnicas
- ✓ SPA con React
- ✓ API RESTful
- ✓ Sistema de autenticación
- ✓ Multi-idioma
- ✓ PWA (Progressive Web App)
- ✓ Sistema de notificaciones

## API Endpoints Descubiertos

Se han identificado 56+ endpoints de la API, incluyendo:

- `/api/user/*` - Gestión de usuarios
- `/api/brute/*` - Gestión de personajes
- `/api/fight/*` - Sistema de combate
- `/api/clan/*` - Sistema de clanes
- `/api/tournament/*` - Torneos
- `/api/achievements/*` - Logros
- Y muchos más...

Ver `REFERENCIA_TECNICA.md` para la lista completa.

## Stack Tecnológico Recomendado

Para recrear el juego, se recomienda:

### Frontend
- React + TypeScript
- React Router
- TanStack Query
- Material-UI o Chakra UI
- Framer Motion

### Backend
- Node.js + Express/Fastify
- PostgreSQL + Prisma
- JWT Authentication
- Socket.io (para tiempo real)
- Redis (cache)

### Infraestructura
- Docker
- Nginx
- PM2

## Plan de Desarrollo

### Fase 1 - MVP
- [ ] Sistema de registro/login
- [ ] Creación de personaje
- [ ] Combate básico
- [ ] Sistema de niveles

### Fase 2 - Core
- [ ] Sistema de inventario
- [ ] Combate mejorado
- [ ] Rankings
- [ ] Perfil de usuario

### Fase 3 - Social
- [ ] Sistema de clanes
- [ ] Torneos
- [ ] Feed de actividades
- [ ] Logros

Ver `REFERENCIA_TECNICA.md` para el plan completo.

## Consideraciones Legales

⚠️ **IMPORTANTE**:

- Este proyecto es solo para propósitos educativos
- NO copiar directamente código o assets del juego original
- Crear contenido propio inspirado, no copias exactas
- Respetar la propiedad intelectual del juego original
- Si vas a crear tu propia versión, hazla única con tus propias ideas

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add some amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo una licencia educativa. El código de análisis es de uso libre, pero recuerda que el juego original "La Brute" tiene sus propios derechos de autor.

## Autor

**Vicente** ([@viceKDK](https://github.com/viceKDK))

## Agradecimientos

- Al equipo de desarrollo original de La Brute por crear un juego interesante para analizar
- A la comunidad de desarrollo web por las herramientas open source utilizadas

---

**Nota**: Este proyecto no está afiliado, asociado, autorizado, respaldado por, o de ninguna manera oficialmente conectado con el juego original "La Brute" o sus desarrolladores.
