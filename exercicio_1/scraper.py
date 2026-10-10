import sys
import requests
from bs4 import BeautifulSoup

# Garante compatibilidade de saída UTF-8 no terminal Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

URL = "http://127.0.0.1:8000/exercicio_1/index.html"


def extrair_catalogo_cursos(url: str = URL):
    """Extrai informações dos cursos da escola fictícia."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Não foi possível acessar a página em {url}.")
        print("Certifique-se de que o servidor local está rodando:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        print(f"Detalhes do erro: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")
    cursos = soup.find_all("article", class_="curso-card")

    print("=" * 60)
    print("        INSTITUTO ALPHA - CATÁLOGO DE CURSOS")
    print("=" * 60)
    print(f"Total de cursos encontrados: {len(cursos)}\n")

    for indice, curso in enumerate(cursos, start=1):
        nome_elem = curso.find(class_="curso-nome")
        area_elem = curso.find(class_="curso-area")
        carga_elem = curso.find(class_="curso-carga")

        nome = nome_elem.get_text(strip=True) if nome_elem else "N/A"
        area = area_elem.get_text(strip=True) if area_elem else "N/A"
        carga_horaria = carga_elem.get_text(strip=True) if carga_elem else "N/A"

        print(f"[{indice}] {nome}")
        print(f"    Área: {area}")
        print(f"    Carga Horária: {carga_horaria}")

        assuntos_lista = curso.find("ul", class_="assuntos-lista")
        if assuntos_lista:
            itens_assuntos = assuntos_lista.find_all("li")
            print("    Assuntos Estudados:")
            for item in itens_assuntos:
                print(f"      • {item.get_text(strip=True)}")
        else:
            print("    Assuntos Estudados: Não informado")

        print("-" * 60)


if __name__ == "__main__":
    extrair_catalogo_cursos()
