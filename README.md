# Web Scraping & Data Mining — Resolução da Lista de Exercícios

Este repositório contém a implementação prática e completa da lista de exercícios de **HTML, DOM e Beautiful Soup**, desenvolvida com **Python**, **Requests** e **BeautifulSoup4**.

---

## 📁 Estrutura do Projeto

```text
web-scraping-data-mining/
├── .gitignore
├── README.md
├── requirements.txt
├── exercicio_1/
│   ├── index.html        # Catálogo de cursos com lista de tópicos estudados
│   └── scraper.py         # Extração de cursos, carga horária e tópicos
├── exercicio_2/
│   ├── index.html        # Loja de informática com situações de estoque variadas
│   └── scraper.py         # Extração de produtos e filtragem de itens "Disponível"
├── exercicio_3/
│   ├── index.html        # Portal de notícias com elementos semânticos
│   └── scraper.py         # Extração de artigos e filtro por categoria ("Tecnologia")
├── exercicio_4/
│   ├── index.html        # Acervo de biblioteca com livros e palavras-chave
│   └── scraper.py         # Extração de livros, tags e filtro de status "Disponível"
├── exercicio_5/
│   ├── index.html        # Cardápio dividido em Pratos, Bebidas e Sobremesas
│   └── scraper.py         # Busca hierárquica por seção e listagem dos itens filhos
└── exercicio_6/
    ├── index.html        # Agenda com palestrantes e links de inscrição
    └── scraper.py         # Extração geral e destaque para múltiplos palestrantes
```

---

## 🚀 Como Executar

### 1. Pré-requisitos e Instalação

Clone o repositório e configure o ambiente Python:

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# No Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# No Linux/macOS:
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Iniciar o Servidor HTTP Local

Todos os scripts consom as páginas simuladas servidas na raiz do projeto através da porta `8000`:

```bash
python -m http.server --bind 127.0.0.1 8000
```

> **Nota:** Mantenha este terminal aberto enquanto executa os scripts de raspagem.

### 3. Executando os Scrapers

Em um segundo terminal (com o ambiente virtual ativado), execute o script de qualquer exercício desejado:

```bash
# Exercício 1 — Catálogo de Cursos
python exercicio_1/scraper.py

# Exercício 2 — Loja de Informática
python exercicio_2/scraper.py

# Exercício 3 — Portal de Notícias
python exercicio_3/scraper.py

# Exercício 4 — Biblioteca Universitária
python exercicio_4/scraper.py

# Exercício 5 — Cardápio por Categorias
python exercicio_5/scraper.py

# Exercício 6 — Agenda de Eventos
python exercicio_6/scraper.py
```

---

## 📋 Resumo dos Exercícios

1. **Exercício 1 (Catálogo de Cursos):**
   - Página com 4 cursos, cada um contendo nome, área, carga horária e lista `<ul>` com assuntos estudados.
   - Script extrai os dados e percorre os tópicos de forma formatada.

2. **Exercício 2 (Loja de Informática):**
   - Página com produtos contendo nome, fabricante, categoria, preço e situação de estoque (`Disponível`, `Estoque baixo`, `Indisponível`).
   - Script extrai todos os produtos e aplica filtragem para listar separadamente apenas os itens disponíveis.

3. **Exercício 3 (Portal de Notícias):**
   - Página com artigos jornalísticos estruturados com tags semânticas (`<article>`, `<h2>`, `<time>`, `<p>`).
   - Script exibe os blocos formatados e filtra os títulos de uma categoria pré-determinada (`Tecnologia`).

4. **Exercício 4 (Biblioteca):**
   - Catálogo de livros com título, autor, ano, gênero, situação de empréstimo e lista de palavras-chave.
   - Script extrai os metadados, itera nas tags de palavras-chave e filtra os livros disponíveis.

5. **Exercício 5 (Cardápio por Categorias):**
   - Cardápio organizado em 3 seções semânticas: *Pratos*, *Bebidas* e *Sobremesas*.
   - Script localiza primeiro cada seção e depois itera exclusivamente pelos seus itens filhos, preservando a hierarquia visual.

6. **Exercício 6 (Agenda de Eventos):**
   - Agenda com datas, horários, locais, palestrantes e botões com links `<a>` de inscrição.
   - Script extrai dados, texto visível e atributo `href` do link, identificando programaticamente e destacando eventos com múltiplos palestrantes.