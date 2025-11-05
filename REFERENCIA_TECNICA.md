# Referencia Técnica - La Brute

## Características del Juego Detectadas

### 1. Sistema de Personajes (Brutes)
- Creación de personajes ("brute")
- Sistema de niveles (level-up)
- Inventario de items
- Cambio de nombre
- Visuales personalizables (reset-visuals)
- Sistema de ascenso (ascend)

### 2. Sistema de Combate
- Arena de combate
- Peleas 1v1 (versus)
- Sistema de destino/fate (destiny)
- Historial de peleas (fight history)
- Velocidad de pelea ajustable

### 3. Clanes
- Creación/gestión de clanes
- Guerras entre clanes (clan wars)
  - Guerras amistosas (friendly wars)
  - Selección de luchadores
  - Aceptar guerras
- Lista de clanes

### 4. Torneos
- Torneos diarios
- Torneos globales
- Rankings por fecha
- Sistema de validación de torneos

### 5. Sistema Social
- Perfiles de usuario
- Feed de actividades
- Sistema de seguir usuarios (toggle-follow)
- Notificaciones
- Logs de usuario

### 6. Logros y Rankings
- Sistema de logros (achievements)
- Rankings por logros
- Hall of Fame

### 7. Eventos
- Eventos actuales
- Lista de eventos históricos

### 8. Foro/Comunidad
- Sistema de hilos (threads)
- Posts y edición
- Wiki del juego

### 9. Moderación y Admin
- Panel de administración
- Panel de moderador
- Sistema de reportes
- Lista de palabras baneadas
- Usuarios baneados
- Detección de cuentas múltiples

### 10. Integración Externa
- OAuth (autenticación externa)
- Recompensas de DinoRPG (juego relacionado)

## API Endpoints

### Autenticación y Usuario
```
POST /api/user/authenticate
GET  /api/user/
POST /api/user/disconnect
GET  /api/user/settings
POST /api/user/change-language
POST /api/user/change-fight-speed
POST /api/user/toggle-background-music
GET  /api/user/next-modifiers
GET  /api/user/banlist
POST /api/user/toggle-follow/:id
GET  /api/user/multiple-accounts
POST /api/user/get-dinorpg-reward
```

### Brute (Personaje)
```
GET  /api/brute
POST /api/brute/
GET  /api/brute/item
```

### Combate
```
GET  /api/fight
POST /api/fight/
```

### Clan
```
GET  /api/clan/
GET  /api/clan/list
POST /api/clan/war
GET  /api/clan/war/
POST /api/clan/war/accept
GET  /api/clan/war/fighters
POST /api/clan/war/fighters/toggle
GET  /api/clan/war/fighters/used
POST /api/clan/war/friendly
```

### Torneos
```
GET  /api/tournament/
GET  /api/tournament/daily
GET  /api/tournament/global
GET  /api/tournament/global/:id
GET  /api/tournament/is-valid/global
```

### Logros y Eventos
```
GET  /api/achievements
GET  /api/achievements/
GET  /api/achievements/rankings/all
GET  /api/event/:id
GET  /api/event/currents
GET  /api/event/list
```

### Notificaciones y Logs
```
GET  /api/notification/:id
GET  /api/notification/list
POST /api/notification/all/read
GET  /api/log/list/:id
GET  /api/log/user-feed/:id
GET  /api/user-log/list
```

### Reportes y Moderación
```
POST /api/report/:id
GET  /api/report/list/:type
POST /api/report/send/:id
GET  /api/report/banned-word/:id
```

### OAuth
```
GET  /api/oauth/redirect
POST /api/oauth/token
```

### Configuración
```
GET  /api/config
GET  /api/config/list
POST /api/config/set
POST /api/config/decrypt
```

### Sistema
```
GET  /api/csrf
GET  /api/is-ready
POST /api/run-daily-job
```

## Rutas de la Aplicación

### Principales
- `/` - Página principal
- `/hall` - Hall of Fame
- `/wiki` - Wiki del juego
- `/patch-notes` - Notas de parche

### Usuario y Brute
- `/user/:userId` - Perfil de usuario
- `/brute/:bruteName` - Perfil del brute
- `/create` - Crear nuevo brute
- `/change-name` - Cambiar nombre
- `/reset-visuals` - Resetear visuales
- `/level-up` - Subir de nivel
- `/ascend` - Ascender
- `/inventory` - Inventario

### Combate
- `/arena` - Arena de combate
- `/fight/:fightId` - Ver pelea
- `/versus/:opponentName` - Combatir contra oponente
- `/destiny` - Destino/Fate
- `/history` - Historial de peleas

### Clan
- `/clan` - Clanes
- `/clan/:clanId` - Página de clan
- `/war` - Guerras de clanes

### Torneos
- `/tournaments` - Lista de torneos
- `/tournament/:date` - Torneo por fecha
- `/tournament/global/:date` - Torneo global
- `/generating-tournaments` - Generando torneos
- `/ranking` - Rankings
- `/ranking/:rank` - Ranking específico

### Social
- `/feed` - Feed de actividades
- `/current` - Actual/actual
- `/event` - Eventos

### Logros
- `/achievements` - Logros
- `/achievements/rankings` - Rankings de logros

### Foro
- `/forum` - Foro principal
- `/thread/:tid` - Hilo de discusión
- `/post/:tid` - Ver post
- `/post/:tid/edit` - Editar post

### Administración
- `/admin-panel` - Panel de administración
- `/admin-panel/user` - Gestión de usuarios
- `/admin-panel/brute/:bruteName` - Gestión de brute
- `/admin-panel/clan/:clanId` - Gestión de clan
- `/admin-panel/config` - Configuración
- `/admin-panel/banned-users` - Usuarios baneados
- `/admin-panel/multiple-accounts` - Cuentas múltiples
- `/admin-panel/report` - Reportes
- `/admin-panel/user/logs/:userId` - Logs de usuario

### Moderación
- `/moderator-panel/report` - Panel de reportes

### OAuth
- `/oauth/callback` - Callback de OAuth

## LocalStorage Keys

El juego usa localStorage para guardar:
- `csrfToken` - Token CSRF de seguridad
- `language` - Idioma seleccionado
- `fightSpeed` - Velocidad de combate
- `fightBackgroundMusic` - Música de fondo en combates
- `mode` - Modo de juego/tema
- `marqueePaused` - Estado del marquee
- `clanWar-*` - Estado de guerras de clanes

## Stack Tecnológico Identificado

### Frontend
- **React** - Framework principal
- **React Router** - Navegación
- **Webpack/Create React App** - Empaquetado
- Fuentes personalizadas (LaBrute, Pixelized, GameFont, etc.)

### Backend (inferido)
- API RESTful
- Sistema de autenticación con CSRF tokens
- OAuth integration
- Daily jobs (cron jobs probablemente)

### Características Técnicas
- PWA (Progressive Web App)
- Mobile responsive
- Sistema de notificaciones
- Multi-idioma
- Música de fondo configurable

## Estructura de Datos Inferida

### User
- id
- username
- settings (language, fightSpeed, backgroundMusic, etc.)
- banlist
- followers/following

### Brute (Character)
- name
- level
- items/inventory
- visual customization
- stats/modifiers

### Fight
- id
- fighters (2 brutes)
- winner
- rounds
- history

### Clan
- id
- name
- members
- wars
- fighters pool

### Tournament
- date
- type (daily/global)
- participants
- rounds

### Achievement
- id
- type
- requirements
- rankings

### Event
- id
- start/end date
- type
- rewards

## Recomendaciones de Stack para Tu Versión

### Frontend
```
- React + TypeScript
- React Router v6
- TanStack Query (React Query) para caché de API
- Zustand o Redux Toolkit para estado global
- Material-UI o Chakra UI para componentes
- Framer Motion para animaciones
- Socket.io-client (si implementas tiempo real)
```

### Backend
```
- Node.js + Express o Fastify
- TypeScript
- PostgreSQL (base de datos relacional)
- Prisma (ORM)
- JWT para autenticación
- Socket.io (para combates en tiempo real)
- Redis (para cache y sesiones)
- Node-cron (para trabajos diarios)
```

### Infraestructura
```
- Docker para desarrollo
- Nginx como reverse proxy
- PM2 para gestión de procesos
- PostgreSQL para datos principales
- Redis para cache
```

## Características a Implementar por Fase

### Fase 1 - MVP
1. Sistema de registro/login
2. Creación de personaje básico
3. Combate simple (puede ser automático primero)
4. Sistema de niveles básico

### Fase 2 - Juego Core
1. Sistema de inventario
2. Combate mejorado con animaciones
3. Rankings básicos
4. Perfil de usuario

### Fase 3 - Social
1. Sistema de clanes
2. Torneos
3. Feed de actividades
4. Sistema de logros

### Fase 4 - Avanzado
1. Guerras de clanes
2. Eventos especiales
3. Foro/comunidad
4. Panel de administración

### Fase 5 - Polish
1. PWA features
2. Optimizaciones
3. Multi-idioma
4. Tutorial interactivo

## Consideraciones de Seguridad

1. **CSRF Protection**: Implementar tokens CSRF como el original
2. **Rate Limiting**: Limitar requests por usuario/IP
3. **Input Validation**: Validar todos los inputs
4. **SQL Injection Prevention**: Usar ORM/prepared statements
5. **XSS Prevention**: Sanitizar outputs
6. **Authentication**: JWT con refresh tokens
7. **Password Hashing**: bcrypt o argon2
8. **Multiple Accounts Detection**: IP tracking, fingerprinting

## Próximos Pasos

1. ✓ Scraping completado
2. ✓ Análisis de estructura completado
3. **Siguiente**: Jugar el juego para entender mecánicas
4. Diseñar el modelo de datos
5. Crear wireframes/mockups
6. Configurar proyecto base
7. Comenzar desarrollo por fases
