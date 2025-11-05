import requests
import os
import json
import sys

def download_file(url, output_dir, filename):
    """Descarga un archivo desde una URL"""
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()

        filepath = os.path.join(output_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Guardar el contenido
        mode = 'wb' if isinstance(response.content, bytes) else 'w'
        with open(filepath, mode) as f:
            f.write(response.content)

        print(f"[OK] Descargado: {filename}")
        return True
    except Exception as e:
        print(f"[ERROR] Error descargando {url}: {e}")
        return False

def process_page(page_folder):
    """Procesa una página específica"""
    structure_file = os.path.join(page_folder, 'structure.json')

    if not os.path.exists(structure_file):
        print(f"[ERROR] No se encontro structure.json en {page_folder}")
        return False

    # Leer la estructura
    with open(structure_file, 'r', encoding='utf-8') as f:
        structure = json.load(f)

    output_dir = os.path.join(page_folder, 'assets')

    print(f"\n{'='*60}")
    print(f"Descargando assets de: {page_folder}")
    print(f"{'='*60}\n")

    # Descargar CSS
    print("--- CSS ---")
    for i, css_url in enumerate(structure['stylesheets']):
        download_file(css_url, output_dir, f'css/main_{i}.css')

    # Descargar JavaScript
    print("\n--- JavaScript ---")
    for i, js_url in enumerate(structure['scripts']):
        download_file(js_url, output_dir, f'js/main_{i}.js')

    # Descargar imágenes si hay
    if structure['images']:
        print("\n--- Imagenes ---")
        for i, img in enumerate(structure['images']):
            img_url = img['src']
            ext = os.path.splitext(img_url)[1] or '.png'
            filename = f"images/img_{i}{ext}"
            download_file(img_url, output_dir, filename)

    # Intentar descargar los favicons e iconos (solo para página inicial)
    if 'inicial' in page_folder:
        print("\n--- Iconos y Favicons ---")
        base_url = "https://brute.eternaltwin.org"
        icons = [
            '/apple-touch-icon.png',
            '/favicon-32x32.png',
            '/favicon-16x16.png',
            '/favicon.ico',
            '/manifest.json',
            '/safari-pinned-tab.svg'
        ]

        for icon_path in icons:
            url = base_url + icon_path
            filename = f"icons/{os.path.basename(icon_path)}"
            download_file(url, output_dir, filename)

    print(f"\n[OK] Assets descargados en: {output_dir}/")
    return True

def main():
    # Carpetas a procesar
    page_folders = [
        'scraped_data/inicial',
        'scraped_data/celda'
    ]

    print(f"\n{'#'*60}")
    print("# DESCARGANDO ASSETS DE TODAS LAS PÁGINAS")
    print(f"{'#'*60}\n")

    for folder in page_folders:
        if os.path.exists(folder):
            process_page(folder)
        else:
            print(f"[WARNING] Carpeta no encontrada: {folder}")

    print(f"\n\n{'='*60}")
    print("DESCARGA COMPLETADA PARA TODAS LAS PÁGINAS")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
