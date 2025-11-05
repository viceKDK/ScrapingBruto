import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin, urlparse
import sys

class BrutoScraper:
    def __init__(self, output_folder="scraped_data"):
        self.base_url = "https://brute.eternaltwin.org/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.output_folder = output_folder

    def login(self, username, password):
        """Intenta hacer login"""
        print(f"Intentando login como {username}...")

        # Primero obtener la página principal para ver el formulario
        try:
            response = self.session.get(self.base_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Buscar el formulario de login o endpoint de API
            # La Brute usa API, así que intentamos autenticar por API
            login_url = urljoin(self.base_url, '/api/user/authenticate')

            login_data = {
                'username': username,
                'password': password
            }

            # Intentar login
            response = self.session.post(login_url, json=login_data)
            print(f"Status de login: {response.status_code}")

            if response.status_code == 200:
                print("Login exitoso!")
                return True
            else:
                print(f"Login fallido, pero continuando... (Status: {response.status_code})")
                # Continuar de todas formas, puede que no sea necesario login para ver
                return True

        except Exception as e:
            print(f"Error en login: {e}")
            print("Continuando sin login...")
            return True

    def fetch_page(self, url=None):
        """Obtiene el contenido HTML de la página"""
        if url is None:
            url = self.base_url

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener la página: {e}")
            return None

    def analyze_structure(self, html, page_url):
        """Analiza la estructura HTML de la página"""
        soup = BeautifulSoup(html, 'html.parser')

        structure = {
            'url': page_url,
            'title': soup.title.string if soup.title else 'No title',
            'scripts': [],
            'stylesheets': [],
            'images': [],
            'links': [],
            'meta_tags': [],
            'main_content': None
        }

        # Scripts
        for script in soup.find_all('script'):
            src = script.get('src')
            if src:
                structure['scripts'].append(urljoin(self.base_url, src))

        # Stylesheets
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                structure['stylesheets'].append(urljoin(self.base_url, href))

        # Images
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                structure['images'].append({
                    'src': urljoin(self.base_url, src),
                    'alt': img.get('alt', ''),
                    'class': img.get('class', [])
                })

        # Links
        for a in soup.find_all('a'):
            href = a.get('href')
            if href:
                structure['links'].append({
                    'href': urljoin(self.base_url, href),
                    'text': a.get_text(strip=True)
                })

        # Meta tags
        for meta in soup.find_all('meta'):
            structure['meta_tags'].append({
                'name': meta.get('name', ''),
                'content': meta.get('content', ''),
                'property': meta.get('property', '')
            })

        # Contenido principal (body)
        if soup.body:
            structure['main_content'] = str(soup.body.prettify())

        return structure

    def save_html(self, html, filename='page.html'):
        """Guarda el HTML en un archivo"""
        os.makedirs(self.output_folder, exist_ok=True)
        filepath = os.path.join(self.output_folder, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"HTML guardado en: {filepath}")

    def save_structure(self, structure, filename='structure.json'):
        """Guarda la estructura en JSON"""
        os.makedirs(self.output_folder, exist_ok=True)
        filepath = os.path.join(self.output_folder, filename)

        # Crear una copia sin el main_content para JSON legible
        structure_copy = structure.copy()
        if 'main_content' in structure_copy:
            # Guardar main_content por separado
            with open(os.path.join(self.output_folder, 'main_content.html'), 'w', encoding='utf-8') as f:
                f.write(structure_copy['main_content'])
            structure_copy['main_content'] = 'Saved in main_content.html'

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(structure_copy, f, indent=2, ensure_ascii=False)
        print(f"Estructura guardada en: {filepath}")

    def run(self, url, username=None, password=None):
        """Ejecuta el scraping completo"""
        print(f"\n{'='*60}")
        print(f"Iniciando scraping de: {url}")
        print(f"Carpeta de salida: {self.output_folder}")
        print(f"{'='*60}\n")

        # Intentar login si se proporcionan credenciales
        if username and password:
            self.login(username, password)

        # Obtener página
        print(f"Obteniendo página: {url}...")
        html = self.fetch_page(url)

        if not html:
            print("No se pudo obtener la página")
            return False

        # Guardar HTML
        self.save_html(html)

        # Analizar estructura
        print("Analizando estructura...")
        structure = self.analyze_structure(html, url)

        # Guardar estructura
        self.save_structure(structure)

        print("\n=== RESUMEN ===")
        print(f"URL: {structure['url']}")
        print(f"Título: {structure['title']}")
        print(f"Scripts encontrados: {len(structure['scripts'])}")
        print(f"Stylesheets encontrados: {len(structure['stylesheets'])}")
        print(f"Imágenes encontradas: {len(structure['images'])}")
        print(f"Links encontrados: {len(structure['links'])}")
        print(f"\nArchivos guardados en la carpeta '{self.output_folder}/'")
        return True

def main():
    # Leer credenciales
    username = "vicente1222"
    password = "vice1222"

    # Páginas a scrapear
    pages = [
        {
            'name': 'inicial',
            'url': 'https://brute.eternaltwin.org/',
            'needs_login': False
        },
        {
            'name': 'celda',
            'url': 'https://brute.eternaltwin.org/diosItachi/cell',
            'needs_login': True
        }
    ]

    for page in pages:
        print(f"\n\n{'#'*60}")
        print(f"# SCRAPEANDO PÁGINA: {page['name'].upper()}")
        print(f"{'#'*60}\n")

        output_folder = os.path.join('scraped_data', page['name'])
        scraper = BrutoScraper(output_folder=output_folder)

        if page['needs_login']:
            scraper.run(page['url'], username=username, password=password)
        else:
            scraper.run(page['url'])

    print(f"\n\n{'='*60}")
    print("SCRAPING COMPLETADO PARA TODAS LAS PÁGINAS")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
