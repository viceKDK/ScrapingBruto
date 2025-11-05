# Resumen del Scraping - La Brute

## Fecha de Scraping
Fecha: 2025-11-05

## Páginas Scrapeadas

### 1. Página Inicial
- **URL**: https://brute.eternaltwin.org/
- **Carpeta**: `scraped_data/inicial/`
- **Login requerido**: No

### 2. Página de Celda
- **URL**: https://brute.eternaltwin.org/diosItachi/cell
- **Carpeta**: `scraped_data/celda/`
- **Login requerido**: Sí (intentado con usuario vicente1222)

## Estructura de Archivos

```
scraped_data/
├── inicial/                    # Página inicial
│   ├── page.html              # HTML completo
│   ├── main_content.html      # Contenido del body
│   ├── structure.json         # Estructura analizada
│   ├── js_analysis.json       # Análisis del JavaScript
│   └── assets/
│       ├── css/
│       │   └── main_0.css     # Estilos (10.65 MB minificado)
│       ├── js/
│       │   └── main_0.js      # App React completa (10.65 MB)
│       └── icons/
│           ├── apple-touch-icon.png
│           ├── favicon-32x32.png
│           ├── favicon-16x16.png
│           ├── favicon.ico
│           ├── manifest.json
│           └── safari-pinned-tab.svg
│
└── celda/                      # Página de celda
    ├── page.html              # HTML completo
    ├── main_content.html      # Contenido del body
    ├── structure.json         # Estructura analizada
    ├── js_analysis.json       # Análisis del JavaScript
    └── assets/
        ├── css/
        │   └── main_0.css     # Estilos (mismo que inicial)
        └── js/
            └── main_0.js      # App React completa (mismo que inicial)
```

## Observaciones Importantes

### Single Page Application (SPA)
Ambas páginas usan los **mismos archivos JavaScript y CSS** porque La Brute es una SPA construida con React:
- El HTML base es minimalista
- Todo el contenido se renderiza dinámicamente con JavaScript
- React Router maneja la navegación sin recargar la página
- El estado de la aplicación se gestiona en el cliente

### Archivos Iguales
Los siguientes archivos son **idénticos** en ambas páginas:
- `main_0.js` (10.65 MB) - App React completa
- `main_0.css` - Todos los estilos
- Estructura HTML base

### Diferencias
La **única diferencia** entre las páginas es:
- La URL que carga React Router
- El contenido renderizado dinámicamente por React
- El estado de la aplicación (si estás logueado o no)

### Login
- El intento de login devolvió status 403 (Forbidden)
- Probablemente requiere CSRF token o cookies de sesión válidas
- El HTML se pudo scrapear de todas formas (React renderiza igual)

## Datos Extraídos

### API Endpoints Detectados
**56 endpoints** encontrados, incluyendo:
- `/api/user/authenticate` - Login
- `/api/brute/` - Gestión de personajes
- `/api/fight/` - Sistema de combate
- `/api/clan/` - Sistema de clanes
- `/api/tournament/` - Torneos
- Y muchos más...

### Rutas de la Aplicación
**84 rutas** encontradas, incluyendo:
- `/` - Inicio
- `/brute/:bruteName` - Perfil del brute
- `/diosItachi/cell` - Celda del personaje diosItachi
- `/fight/:fightId` - Ver pelea
- `/clan/:clanId` - Página de clan
- Y muchas más...

### LocalStorage Keys
**7 keys** detectadas:
- `csrfToken` - Token de seguridad
- `language` - Idioma
- `fightSpeed` - Velocidad de combate
- `fightBackgroundMusic` - Música de fondo
- `mode` - Modo de juego
- `marqueePaused` - Estado del marquee
- `clanWar-*` - Estado de guerras

### Componentes React
**50+ componentes** detectados (nombres minificados)

## Scripts Utilizados

### 1. scraper_multi.py
Scrapea ambas páginas y guarda:
- HTML completo
- Estructura JSON
- Contenido del body separado

### 2. download_assets_multi.py
Descarga:
- Archivos CSS
- Archivos JavaScript
- Imágenes (si las hay)
- Iconos y favicons

### 3. analyze_js_multi.py
Analiza el JavaScript para extraer:
- API endpoints
- Rutas de la aplicación
- Componentes React
- LocalStorage keys
- WebSocket URLs
- Variables de entorno

## Cómo Usar los Scripts

```bash
# 1. Scrapear ambas páginas
python scraper_multi.py

# 2. Descargar todos los assets
python download_assets_multi.py

# 3. Analizar el JavaScript
python analyze_js_multi.py
```

## Próximos Pasos Recomendados

### Para Entender Mejor el Juego

1. **Inspeccionar con DevTools del Navegador**
   - Abre https://brute.eternaltwin.org/ en Chrome/Firefox
   - Presiona F12 para abrir DevTools
   - Instala React DevTools extension
   - Inspecciona componentes React en vivo
   - Observa el Network tab para ver llamadas a la API

2. **Jugar el Juego**
   - Crea una cuenta y juega
   - Observa todas las características
   - Toma notas de las mecánicas de juego
   - Haz screenshots de las pantallas importantes

3. **Analizar las Llamadas a la API**
   - Usa el Network tab en DevTools
   - Observa qué endpoints se llaman
   - Analiza los payloads (request/response)
   - Documenta la estructura de datos

### Para Recrear tu Versión

1. **Diseñar tu Base de Datos**
   - Basándote en los endpoints detectados
   - Crear schema para usuarios, brutes, peleas, clanes, etc.

2. **Crear Wireframes**
   - Diseña tu propia UI
   - Inspira tu diseño pero hazlo único
   - Usa Figma, Sketch o similar

3. **Configurar Proyecto**
   - Inicializar proyecto React + TypeScript
   - Configurar backend (Node.js + Express + PostgreSQL)
   - Configurar Docker para desarrollo

4. **Desarrollar por Fases**
   - Fase 1: MVP (login, crear personaje, combate básico)
   - Fase 2: Core features
   - Fase 3: Social features
   - Fase 4: Advanced features
   - Fase 5: Polish y optimización

## Notas Técnicas

### Tecnologías Detectadas
- **Frontend**: React (SPA)
- **Build Tool**: Webpack/Create React App
- **Routing**: React Router
- **Tamaño**: ~10.65 MB de JavaScript minificado
- **PWA**: Sí (tiene manifest.json)
- **Mobile**: Responsive (meta viewport configurado)

### Seguridad
- CSRF tokens en uso
- Status 403 en login sin token válido
- Probablemente usa cookies HTTP-only
- API RESTful con autenticación

### Performance
- Todo el JS se carga de una vez (no code splitting visible)
- Archivo muy grande (10.65 MB) podría optimizarse
- Para tu versión considera:
  - Code splitting
  - Lazy loading de componentes
  - Tree shaking
  - Compresión gzip/brotli

## Consideraciones Legales

⚠️ **IMPORTANTE**:
- Este scraping es solo para análisis educativo
- NO usar el código JavaScript descargado directamente
- NO copiar assets gráficos del juego original
- Crear tu propia implementación única
- Respetar la propiedad intelectual del juego original

## Recursos Adicionales

- **Documentación Original**: Ver `ANALISIS_BRUTO.md`
- **Referencia Técnica**: Ver `REFERENCIA_TECNICA.md`
- **Credenciales de Prueba**: Ver `LOGIN_README.txt` (no subir a git)

---

**Última actualización**: 2025-11-05
