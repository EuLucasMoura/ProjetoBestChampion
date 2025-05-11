# 📊 Projeto: **Best Champion** – Análise Estatística dos Campeões de LoL

## 🧠 Introdução

Este projeto tem como objetivo realizar um **estudo estatístico para identificar os campeões mais eficientes do jogo League of Legends (LoL)**. A ideia é avaliar o desempenho dos campeões ao longo de diferentes períodos, versões e funções dentro do jogo.

> ⚠️ *O escopo temporal (patches ou temporadas analisadas) ainda está em definição.*

---

## 🛠️ Metodologia

O foco atual está na criação de uma base de dados sólida e confiável a partir de **web scraping** de sites especializados, que fornecem dados estatísticos como:

- Nome do campeão (Champion)
- Taxa de vitória (win rate)
- Frequência de escolha (pick rate)

Para garantir a integridade dos dados:

- Uso estruturado de tags HTML: `<tbody>`, `<tr>`, `<td>` — evitando anúncios e elementos fora da tabela.
- Validação de consistência: apenas linhas com o número correto de colunas são mantidas.
- Exportação dos dados em formato `.xlsx` via `pandas`.

---

## 📈 Estado Atual do Projeto

- Extração bem-sucedida de dados tabulares com Selenium.
- Filtragem automática de linhas incompletas ou inválidas.
- Exportação funcional para Excel.
- Código limpo, com scraping estável e replicável.

---

## 🧰 Tecnologias e Ferramentas Usadas

### ✅ Linguagem:
- **Python 3.12.10**

### ✅ Bibliotecas:
| Biblioteca     | Status | Descrição                                                                 |
|----------------|--------|--------------------------------------------------------------------------|
| `pandas`         | ✅ | Manipulação e estruturação dos dados extraídos                             |
| `Selenium`       | ✅ | Navegação automatizada e scraping de conteúdo dinâmico via JavaScript      |
| `openpyxl`       | ✅ | Suporte à exportação de dados para arquivos `.xlsx`                        |
| `BeautifulSoup4` | ❌ | Avaliada, mas descartada por não lidar bem com páginas JS dinâmicas         |

### ✅ Ferramentas:
- **VSCode** – Ambiente de desenvolvimento
- **Google Chrome** – Testes e depuração do DOM com DevTools
- **Excel** – Análise manual e visualização dos dados exportados
