import sys
import requests
from bs4 import BeautifulSoup

# Garante compatibilidade de saída UTF-8 no terminal Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

URL = "http://127.0.0.1:8000/exercicio_5/index.html"


def raspar_cardapio_por_categorias(url: str = URL):
    """Localiza cada seção do cardápio e itera pelos seus respectivos itens filhos."""
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

    # Passo 1: Localizar todas as seções de categoria do cardápio
    secoes = soup.find_all("section", class_="categoria-secao")

    print("=" * 70)
    print("                BISTRÔ SABOR & ARTE - CARDÁPIO")
    print("=" * 70)
    print(f"Total de seções encontradas: {len(secoes)}\n")

    for secao in secoes:
        # Título da Categoria
        titulo_secao_elem = secao.find(["h2", "h3"], class_="categoria-titulo")
        nome_categoria = (
            titulo_secao_elem.get_text(strip=True)
            if titulo_secao_elem
            else "Categoria Desconhecida"
        )

        print(f"▶ CATEGORIA: {nome_categoria.upper()}")
        print("  " + "─" * 60)

        # Passo 2: Percorrer apenas os itens pertencentes a esta seção
        itens = secao.find_all("article", class_="item-cardapio")

        if not itens:
            print("    (Nenhum item nesta seção)")
        else:
            for i, item in enumerate(itens, start=1):
                nome_elem = item.find(class_="item-nome")
                preco_elem = item.find(class_="item-preco")
                desc_elem = item.find(class_="item-descricao")

                nome = nome_elem.get_text(strip=True) if nome_elem else "Sem nome"
                preco = preco_elem.get_text(strip=True) if preco_elem else "Sem preço"
                descricao = desc_elem.get_text(strip=True) if desc_elem else ""

                print(f"    [{i}] {nome} — {preco}")
                if descricao:
                    print(f"        Descrição: {descricao}")
        print()


if __name__ == "__main__":
    raspar_cardapio_por_categorias()
