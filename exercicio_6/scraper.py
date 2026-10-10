import sys
import requests
from bs4 import BeautifulSoup

# Garante compatibilidade de saída UTF-8 no terminal Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

URL = "http://127.0.0.1:8000/exercicio_6/index.html"


def raspar_agenda_eventos(url: str = URL):
    """Extrai informações de eventos, links de inscrição e identifica múltiplos palestrantes."""
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
    evento_cards = soup.find_all("article", class_="evento-card")

    eventos = []
    for card in evento_cards:
        nome_elem = card.find(class_="evento-nome")
        data_elem = card.find(class_="evento-data")
        horario_elem = card.find(class_="evento-horario")
        local_elem = card.find(class_="evento-local")

        # Extrair palestrantes como elementos individuais (separados)
        palestrantes_tags = card.find_all(class_="palestrante-tag")
        palestrantes = [p.get_text(strip=True) for p in palestrantes_tags]

        # Extrair link de inscrição (texto e href)
        link_elem = card.find("a", class_="link-inscricao")
        link_texto = link_elem.get_text(strip=True) if link_elem else "Nenhum link"
        link_href = link_elem.get("href", "Nenhum href") if link_elem else ""

        evento = {
            "nome": nome_elem.get_text(strip=True) if nome_elem else "Sem nome",
            "data": data_elem.get_text(strip=True) if data_elem else "N/A",
            "horario": horario_elem.get_text(strip=True) if horario_elem else "N/A",
            "local": local_elem.get_text(strip=True) if local_elem else "N/A",
            "palestrantes": palestrantes,
            "qtd_palestrantes": len(palestrantes),
            "tem_multiplos_palestrantes": len(palestrantes) > 1,
            "link_texto": link_texto,
            "link_href": link_href,
        }
        eventos.append(evento)

    # Exibição de todos os eventos
    print("=" * 75)
    print("                 TECHSUMMIT 2026 - AGENDA DE EVENTOS")
    print("=" * 75)
    print(f"Total de eventos encontrados: {len(eventos)}\n")

    for i, ev in enumerate(eventos, start=1):
        print(f"[{i}] {ev['nome']}")
        print(f"    Data & Horário : {ev['data']} às {ev['horario']}")
        print(f"    Local          : {ev['local']}")
        print(f"    Palestrante(s) ({ev['qtd_palestrantes']}):")
        for p in ev["palestrantes"]:
            print(f"      • {p}")

        print("    Inscrição:")
        print(f"      - Texto do link : \"{ev['link_texto']}\"")
        print(f"      - URL (href)    : {ev['link_href']}")

        # Indicação programática de múltiplos palestrantes
        if ev["tem_multiplos_palestrantes"]:
            print(
                f"    ★ DESTAQUE: Evento com MÚLTIPLOS PALESTRANTES ({ev['qtd_palestrantes']} palestrantes)"
            )
        else:
            print("    ℹ Palestrante individual")

        print("-" * 75)

    # Seção de resumo com os eventos que possuem mais de um palestrante
    multiplos = [e for e in eventos if e["tem_multiplos_palestrantes"]]
    print("\n" + "=" * 75)
    print("    EVENTOS IDENTIFICADOS COM MAIS DE UM PALESTRANTE (RESUMO)")
    print("=" * 75)
    print(f"Total de eventos com múltiplos palestrantes: {len(multiplos)}\n")

    for i, ev in enumerate(multiplos, start=1):
        print(f"{i}. {ev['nome']}")
        print(f"   Total de palestrantes: {ev['qtd_palestrantes']}")
        print(f"   Nomes: {', '.join(ev['palestrantes'])}")
        print(f"   Inscrição: {ev['link_href']}")
        print("   " + "─" * 60)


if __name__ == "__main__":
    raspar_agenda_eventos()
