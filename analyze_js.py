import re
import json
import os

def analyze_minified_js(filepath):
    """Analiza el JavaScript minificado para extraer información útil"""
    print("Analizando JavaScript minificado...\n")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    analysis = {
        'api_endpoints': [],
        'component_names': [],
        'route_paths': [],
        'storage_keys': [],
        'environment_variables': [],
        'websocket_urls': []
    }

    # Buscar endpoints API (patrones comunes)
    api_patterns = [
        r'"(/api/[^"]+)"',
        r"'(/api/[^']+)'",
        r'`(/api/[^`]+)`',
        r'"(https?://[^"]+/api/[^"]+)"',
    ]

    for pattern in api_patterns:
        matches = re.findall(pattern, content)
        analysis['api_endpoints'].extend(matches)

    # Buscar rutas de React Router
    route_patterns = [
        r'path:"([^"]+)"',
        r"path:'([^']+)'",
        r'to:"([^"]+)"',
        r"to:'([^']+)'",
    ]

    for pattern in route_patterns:
        matches = re.findall(pattern, content)
        analysis['route_paths'].extend(matches)

    # Buscar nombres de componentes (capitalizados)
    component_pattern = r'function\s+([A-Z][a-zA-Z0-9]+)\s*\('
    components = re.findall(component_pattern, content)
    analysis['component_names'] = list(set(components))[:50]  # Limitar a 50

    # Buscar localStorage/sessionStorage keys
    storage_patterns = [
        r'localStorage\.(?:get|set)Item\("([^"]+)"',
        r"localStorage\.(?:get|set)Item\('([^']+)'",
        r'sessionStorage\.(?:get|set)Item\("([^"]+)"',
        r"sessionStorage\.(?:get|set)Item\('([^']+)'",
    ]

    for pattern in storage_patterns:
        matches = re.findall(pattern, content)
        analysis['storage_keys'].extend(matches)

    # Buscar WebSocket URLs
    ws_patterns = [
        r'"(wss?://[^"]+)"',
        r"'(wss?://[^']+)'",
    ]

    for pattern in ws_patterns:
        matches = re.findall(pattern, content)
        analysis['websocket_urls'].extend(matches)

    # Buscar variables de entorno o configuración
    env_patterns = [
        r'process\.env\.([A-Z_]+)',
        r'REACT_APP_([A-Z_]+)',
    ]

    for pattern in env_patterns:
        matches = re.findall(pattern, content)
        analysis['environment_variables'].extend(matches)

    # Remover duplicados
    for key in analysis:
        if isinstance(analysis[key], list):
            analysis[key] = sorted(list(set(analysis[key])))

    return analysis

def print_analysis(analysis):
    """Imprime el análisis de forma legible"""
    print("=" * 60)
    print("ANALISIS DEL JAVASCRIPT")
    print("=" * 60)

    print(f"\n[API ENDPOINTS] ({len(analysis['api_endpoints'])} encontrados)")
    for endpoint in analysis['api_endpoints'][:20]:  # Mostrar primeros 20
        print(f"  - {endpoint}")
    if len(analysis['api_endpoints']) > 20:
        print(f"  ... y {len(analysis['api_endpoints']) - 20} más")

    print(f"\n[RUTAS DE LA APP] ({len(analysis['route_paths'])} encontradas)")
    for route in analysis['route_paths'][:30]:
        print(f"  - {route}")
    if len(analysis['route_paths']) > 30:
        print(f"  ... y {len(analysis['route_paths']) - 30} más")

    print(f"\n[COMPONENTES REACT] ({len(analysis['component_names'])} encontrados)")
    for comp in analysis['component_names'][:30]:
        print(f"  - {comp}")
    if len(analysis['component_names']) > 30:
        print(f"  ... y {len(analysis['component_names']) - 30} más")

    print(f"\n[STORAGE KEYS] ({len(analysis['storage_keys'])} encontradas)")
    for key in analysis['storage_keys']:
        print(f"  - {key}")

    print(f"\n[WEBSOCKET URLs] ({len(analysis['websocket_urls'])} encontradas)")
    for ws in analysis['websocket_urls']:
        print(f"  - {ws}")

    print(f"\n[VARIABLES DE ENTORNO] ({len(analysis['environment_variables'])} encontradas)")
    for env in analysis['environment_variables']:
        print(f"  - {env}")

    print("\n" + "=" * 60)

def save_analysis(analysis, output_file='scraped_data/js_analysis.json'):
    """Guarda el análisis en un archivo JSON"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    print(f"\n[OK] Analisis guardado en: {output_file}")

if __name__ == "__main__":
    js_file = 'scraped_data/assets/js/main.js'

    if not os.path.exists(js_file):
        print(f"[ERROR] No se encontro el archivo: {js_file}")
        exit(1)

    print(f"Analizando: {js_file}")
    print(f"Tamaño: {os.path.getsize(js_file) / 1024 / 1024:.2f} MB\n")

    analysis = analyze_minified_js(js_file)
    print_analysis(analysis)
    save_analysis(analysis)
