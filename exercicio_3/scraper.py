import sys
import requests
from bs4 import BeautifulSoup

# Garante compatibilidade de saída UTF-8 no terminal Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

URL = "http://127.0.0.1:8000/exercicio_3/index.html"
CATEGORIA_ALVO = "Tecnologia"


def raspar_portal_noticias(url: str = URL, categoria_alvo: str = CATEGORIA_ALVO):
    """Extrai notícias de portal e filtra títulos por categoria específica."""
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
    artigos = soup.find_all("article", class_="noticia-item")

    noticias = []
    for artigo in artigos:
        cat_elem = artigo.find(class_="noticia-categoria")
        tit_elem = artigo.find(class_="noticia-titulo")
        data_elem = artigo.find(class_="noticia-data")
        autor_elem = artigo.find(class_="noticia-autor")
        resumo_elem = artigo.find(class_="noticia-resumo")

        noticia = {
            "categoria": cat_elem.get_text(strip=True) if cat_elem else "Geral",
            "titulo": tit_elem.get_text(strip=True) if tit_elem else "Sem Título",
            "data": data_elem.get_text(strip=True) if data_elem else "Data não informada",
            "autor": autor_elem.get_text(strip=True) if autor_elem else "Redação",
            "resumo": resumo_elem.get_text(strip=True) if resumo_elem else "",
        }
        noticias.append(noticia)

    # Exibição organizada de cada notícia em blocos
    print("=" * 70)
    print("                 PORTAL NOTÍCIAS DO DIA")
    print("=" * 70)
    print(f"Total de notícias encontradas: {len(noticias)}\n")

    for i, notic in enumerate(noticias, start=1):
        print(f"┌── [Notícia #{i}] ───────────────────────────────────────────────────")
        print(f"│ Categoria : {notic['categoria']}")
        print(f"│ Título    : {notic['titulo']}")
        print(f"│ Data      : {notic['data']} | Autor: {notic['autor']}")
        print(f"│ Resumo    : {notic['resumo']}")
        print("└" + "─" * 69 + "\n")

    # Filtrar e exibir apenas títulos da categoria escolhida
    noticias_filtradas = [
        n for n in noticias if n["categoria"].strip().lower() == categoria_alvo.lower()
    ]

    print("=" * 70)
    print(f"    FILTRO POR CATEGORIA: '{categoria_alvo.upper()}' (Apenas Títulos)")
    print("=" * 70)
    print(f"Total na categoria: {len(noticias_filtradas)}\n")

    for i, n in enumerate(noticias_filtradas, start=1):
        print(f"  {i}. {n['titulo']}")
    print("=" * 70)


if __name__ == "__main__":
    raspar_portal_noticias()
