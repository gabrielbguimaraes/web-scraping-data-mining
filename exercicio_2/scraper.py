import sys
import requests
from bs4 import BeautifulSoup

# Garante compatibilidade de saída UTF-8 no terminal Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

URL = "http://127.0.0.1:8000/exercicio_2/index.html"


def raspar_loja_informatica(url: str = URL):
    """Extrai catálogo de produtos de informática e filtra itens disponíveis."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        response.encoding = "utf-8"
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao acessar {url}.")
        print("Inicie o servidor HTTP na raiz do projeto com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        print(f"Detalhes: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("article", class_="produto-card")

    produtos = []
    for card in cards:
        nome_elem = card.find(class_="produto-nome")
        fab_elem = card.find(class_="produto-fabricante")
        cat_elem = card.find(class_="produto-categoria")
        preco_elem = card.find(class_="produto-preco")
        estoque_elem = card.find(class_="produto-estoque")

        produto = {
            "nome": nome_elem.get_text(strip=True) if nome_elem else "N/A",
            "fabricante": fab_elem.get_text(strip=True) if fab_elem else "N/A",
            "categoria": cat_elem.get_text(strip=True) if cat_elem else "N/A",
            "preco": preco_elem.get_text(strip=True) if preco_elem else "N/A",
            "situacao": estoque_elem.get_text(strip=True) if estoque_elem else "N/A",
        }
        produtos.append(produto)

    # Exibição de todos os produtos
    print("=" * 65)
    print("        TECHSTORE INFORMÁTICA - TODOS OS PRODUTOS")
    print("=" * 65)
    print(f"Total de produtos cadastrados: {len(produtos)}\n")

    for i, prod in enumerate(produtos, start=1):
        print(f"[{i}] {prod['nome']}")
        print(f"    Fabricante: {prod['fabricante']}")
        print(f"    Categoria : {prod['categoria']}")
        print(f"    Preço     : {prod['preco']}")
        print(f"    Situação  : {prod['situacao']}")
        print("-" * 65)

    # Filtragem separada: apenas produtos com situação 'Disponível'
    disponiveis = [p for p in produtos if p["situacao"].strip().lower() == "disponível"]

    print("\n" + "=" * 65)
    print("        PRODUTOS COM STATUS 'DISPONÍVEL' (FILTRO)")
    print("=" * 65)
    print(f"Total de produtos disponíveis: {len(disponiveis)}\n")

    for i, prod in enumerate(disponiveis, start=1):
        print(f"[{i}] {prod['nome']}")
        print(f"    Fabricante: {prod['fabricante']} | Preço: {prod['preco']}")
        print(f"    Categoria : {prod['categoria']} | Situação: {prod['situacao']}")
        print("-" * 65)


if __name__ == "__main__":
    raspar_loja_informatica()
