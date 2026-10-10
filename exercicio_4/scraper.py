import sys
import requests
from bs4 import BeautifulSoup

# Garante compatibilidade de saída UTF-8 no terminal Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

URL = "http://127.0.0.1:8000/exercicio_4/index.html"


def raspar_biblioteca(url: str = URL):
    """Extrai livros, metadados, palavras-chave e filtra os livros disponíveis."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao acessar {url}.")
        print("Inicie o servidor HTTP com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        print(f"Detalhes: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")
    livro_elements = soup.find_all("article", class_="livro-card")

    livros = []
    for elem in livro_elements:
        titulo_el = elem.find(class_="livro-titulo")
        autor_el = elem.find(class_="livro-autor")
        ano_el = elem.find(class_="livro-ano")
        genero_el = elem.find(class_="livro-genero")
        situacao_el = elem.find(class_="livro-situacao")

        palavras_chave = []
        lista_tags = elem.find("ul", class_="palavras-chave")
        if lista_tags:
            for item in lista_tags.find_all("li"):
                palavras_chave.append(item.get_text(strip=True))

        livro = {
            "titulo": titulo_el.get_text(strip=True) if titulo_el else "N/A",
            "autor": autor_el.get_text(strip=True) if autor_el else "N/A",
            "ano": ano_el.get_text(strip=True) if ano_el else "N/A",
            "genero": genero_el.get_text(strip=True) if genero_el else "N/A",
            "situacao": situacao_el.get_text(strip=True) if situacao_el else "N/A",
            "palavras_chave": palavras_chave,
        }
        livros.append(livro)

    # Exibição completa de todos os livros
    print("=" * 70)
    print("           BIBLIOTECA CENTRAL - ACERVO COMPLETO")
    print("=" * 70)
    print(f"Total de livros cadastrados: {len(livros)}\n")

    for i, livro in enumerate(livros, start=1):
        print(f"[{i}] Título   : {livro['titulo']}")
        print(f"    Autor    : {livro['autor']}")
        print(f"    Ano      : {livro['ano']} | Gênero: {livro['genero']}")
        print(f"    Situação : {livro['situacao']}")
        print("    Palavras-chave:")
        for tag in livro["palavras_chave"]:
            print(f"      - {tag}")
        print("-" * 70)

    # Apresentar separadamente apenas os livros disponíveis
    disponiveis = [l for l in livros if l["situacao"].strip().lower() == "disponível"]

    print("\n" + "=" * 70)
    print("           LIVROS COM STATUS 'DISPONÍVEL' PARA EMPRÉSTIMO")
    print("=" * 70)
    print(f"Total disponíveis: {len(disponiveis)}\n")

    for i, livro in enumerate(disponiveis, start=1):
        print(f"[{i}] {livro['titulo']} ({livro['ano']})")
        print(f"    Autor   : {livro['autor']}")
        print(f"    Gênero  : {livro['genero']}")
        print(f"    Tags    : {', '.join(livro['palavras_chave'])}")
        print("-" * 70)


if __name__ == "__main__":
    raspar_biblioteca()
