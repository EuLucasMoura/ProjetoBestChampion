# 📊 Projeto: **Best Champion** – Análise Estatística dos Campeões de LoL

## 🧠 Introdução

Este projeto tem como objetivo realizar um **estudo estatístico para identificar os campeões mais eficientes do jogo *League of Legends* (LoL)**. A proposta é avaliar o desempenho dos campeões ao longo de diferentes versões, funções e regiões, com base em dados objetivos como **taxa de vitória** e **frequência de escolha**.

> 📅 Atualmente, estão sendo analisados os patches **15.08, 15.09 e 15.10**.

---

## 🛠️ Metodologia

O foco inicial está na **construção de uma base de dados robusta e confiável**, por meio de *web scraping* em sites especializados. A coleta é voltada para informações estatísticas relevantes, como:

- Nome do campeão  
- Taxa de vitória (*win rate*)  
- Frequência de escolha (*pick rate*)  
- Dados segmentados por **região**, **elo**, **patch**, **tipo de fila** e **função (lane)**  

### 🧪 Garantia de qualidade dos dados

- Coleta estruturada com base em tags HTML (`<tbody>`, `<tr>`, `<td>`) para evitar ruídos como anúncios ou componentes visuais irrelevantes.
- Tratamento de exceções para elementos dinâmicos da página, incluindo:
  - `StaleElementReferenceException`
  - `ElementClickInterceptedException`
- Salvamento incremental por região: garante persistência mesmo em caso de falhas durante a execução.
- Exportação final em formato `.xlsx` com `pandas`.

---

## 📈 Estado Atual do Projeto

- ✅ Extração bem-sucedida de dados tabulares usando Selenium.  
- ✅ Automação da navegação por patch, elo, tipo de fila e lane.  
- ✅ Scroll dinâmico implementado para carregar todos os registros da página.  
- ✅ Tratamento de elementos dinâmicos com tentativas repetidas e esperas inteligentes.  
- ✅ Salvamento automático dos dados por **região**, criando múltiplos arquivos `.xlsx`.  
- ✅ Código modular e replicável para diferentes combinações de filtros.  

---

## 🧰 Tecnologias e Ferramentas Utilizadas

### ✅ Linguagem

- **Python 3.12.10**

### ✅ Bibliotecas

| Biblioteca       | Status | Descrição                                                                 |
|------------------|--------|--------------------------------------------------------------------------|
| `pandas`         | ✅      | Manipulação, organização e exportação dos dados                          |
| `selenium`       | ✅      | Automação de navegação e scraping de conteúdo dinâmico                   |
| `openpyxl`       | ✅      | Escrita e manipulação de arquivos `.xlsx`                                |
| `beautifulsoup4` | ❌      | Avaliada, mas descartada por não oferecer suporte completo a JS dinâmico |

### ✅ Ferramentas Complementares

- **VSCode** – Ambiente de desenvolvimento e testes  
- **Google Chrome** – Análise do DOM e depuração com DevTools  
- **Microsoft Excel** – Visualização e análise manual dos dados coletados
