import requests
import os
import json

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

def main():
    # Leer la estructura
    with open('scraped_data/structure.json', 'r', encoding='utf-8') as f:
        structure = json.load(f)

    output_dir = 'scraped_data/assets'

    print("Descargando assets de La Brute...\n")

    # Descargar CSS
    print("--- CSS ---")
    for i, css_url in enumerate(structure['stylesheets']):
        download_file(css_url, output_dir, f'css/main.css')

    # Descargar JavaScript
    print("\n--- JavaScript ---")
    for i, js_url in enumerate(structure['scripts']):
        download_file(js_url, output_dir, f'js/main.js')

    # Descargar imágenes si hay
    if structure['images']:
        print("\n--- Imágenes ---")
        for i, img in enumerate(structure['images']):
            img_url = img['src']
            filename = f"images/img_{i}_{os.path.basename(img_url)}"
            download_file(img_url, output_dir, filename)

    # Intentar descargar los favicons e iconos
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

    print(f"\n[OK] Todos los assets descargados en: {output_dir}/")

if __name__ == "__main__":
    main()
