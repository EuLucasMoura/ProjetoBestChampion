# 📊 Projeto: **Best Champion** – Análise Estatística dos Campeões de LoL

## 🧠 Introdução

Este projeto tem como objetivo realizar um **estudo estatístico para identificar os campeões mais eficientes do jogo *League of Legends* (LoL)**. A proposta é avaliar o desempenho dos campeões ao longo de diferentes versões, funções e regiões, com base em dados objetivos como **taxa de vitória** e **frequência de escolha**.

> ⚠️ *O escopo temporal (patches ou temporadas analisadas) ainda está em definição.*

---

## 🛠️ Metodologia

O foco inicial está na **construção de uma base de dados robusta e confiável**, por meio de *web scraping* em sites especializados. A coleta é voltada para informações estatísticas relevantes, como:

- Nome do campeão
- Taxa de vitória (*win rate*)
- Frequência de escolha (*pick rate*)

### 🧪 Garantia de qualidade dos dados

- Coleta estruturada com base em tags HTML: `<tbody>`, `<tr>`, `<td>`, evitando anúncios e elementos não relacionados à tabela.
- Validação da consistência: apenas linhas com o número correto de colunas são consideradas.
- Exportação final em formato `.xlsx`, utilizando a biblioteca `pandas`.

---

## 📈 Estado Atual do Projeto

- ✅ Extração bem-sucedida de dados tabulares usando Selenium.
- ✅ Filtragem automática de entradas incompletas ou inconsistentes.
- ✅ Exportação funcional para Excel.
- ✅ Código limpo, replicável e com scraping estável.
- ✅ Extração por lanes e por região 100% mapeada.

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
