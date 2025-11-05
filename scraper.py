import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin, urlparse
import time

class BrutoScraper:
    def __init__(self):
        self.base_url = "https://brute.eternaltwin.org/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

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

    def login(self, username, password):
        """Intenta hacer login si es necesario"""
        # Primero obtenemos la página principal para ver si hay un formulario de login
        html = self.fetch_page()
        if not html:
            return False

        soup = BeautifulSoup(html, 'html.parser')

        # Buscar formulario de login
        login_form = soup.find('form')
        if login_form:
            # Obtener la URL de acción del formulario
            action = login_form.get('action', '')
            login_url = urljoin(self.base_url, action)

            # Preparar datos de login
            login_data = {
                'username': username,
                'password': password
            }

            # Buscar nombres de campos en el formulario
            inputs = login_form.find_all('input')
            for inp in inputs:
                name = inp.get('name', '')
                if 'user' in name.lower() or 'email' in name.lower():
                    login_data[name] = username
                elif 'pass' in name.lower():
                    login_data[name] = password

            try:
                response = self.session.post(login_url, data=login_data)
                print(f"Login attempt status: {response.status_code}")
                return response.status_code == 200
            except Exception as e:
                print(f"Error en login: {e}")
                return False

        return True  # No hay formulario de login

    def analyze_structure(self, html):
        """Analiza la estructura HTML de la página"""
        soup = BeautifulSoup(html, 'html.parser')

        structure = {
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
        os.makedirs('scraped_data', exist_ok=True)
        filepath = os.path.join('scraped_data', filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"HTML guardado en: {filepath}")

    def save_structure(self, structure, filename='structure.json'):
        """Guarda la estructura en JSON"""
        os.makedirs('scraped_data', exist_ok=True)
        filepath = os.path.join('scraped_data', filename)

        # Crear una copia sin el main_content para JSON legible
        structure_copy = structure.copy()
        if 'main_content' in structure_copy:
            # Guardar main_content por separado
            with open(os.path.join('scraped_data', 'main_content.html'), 'w', encoding='utf-8') as f:
                f.write(structure_copy['main_content'])
            structure_copy['main_content'] = 'Saved in main_content.html'

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(structure_copy, f, indent=2, ensure_ascii=False)
        print(f"Estructura guardada en: {filepath}")

    def run(self, username=None, password=None):
        """Ejecuta el scraping completo"""
        print("Iniciando scraping de Bruto...")

        # Intentar login si se proporcionan credenciales
        if username and password:
            print(f"Intentando login como {username}...")
            self.login(username, password)

        # Obtener página principal
        print("Obteniendo página principal...")
        html = self.fetch_page()

        if not html:
            print("No se pudo obtener la página")
            return

        # Guardar HTML
        self.save_html(html)

        # Analizar estructura
        print("Analizando estructura...")
        structure = self.analyze_structure(html)

        # Guardar estructura
        self.save_structure(structure)

        print("\n=== RESUMEN ===")
        print(f"Título: {structure['title']}")
        print(f"Scripts encontrados: {len(structure['scripts'])}")
        print(f"Stylesheets encontrados: {len(structure['stylesheets'])}")
        print(f"Imágenes encontradas: {len(structure['images'])}")
        print(f"Links encontrados: {len(structure['links'])}")
        print("\nArchivos guardados en la carpeta 'scraped_data/'")

if __name__ == "__main__":
    scraper = BrutoScraper()

    # Leer credenciales (puedes modificar esto)
    scraper.run(username="vicente1222", password="vice1222")
