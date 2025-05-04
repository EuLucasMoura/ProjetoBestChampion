# 📊 Projeto: **Best Champion** – Análise Estatística dos Campeões de LoL

## 🧠 Introdução

Este projeto tem como objetivo realizar um **estudo estatístico para identificar os campeões mais eficientes do jogo League of Legends (LoL)**. A ideia é avaliar o desempenho dos campeões ao longo de diferentes períodos, versões e funções dentro do jogo.

> ⚠️ *O escopo temporal (patches ou temporadas analisadas) ainda está em definição.*

---

## 🛠️ Metodologia

Neste momento, o foco está em levantar **bases de dados confiáveis** através de técnicas de **web scraping**, buscando fontes que ofereçam dados estatísticos como:

- Taxa de vitória (win rate)
- Frequência de escolha (pick rate)
- Frequência de banimento (ban rate)
- Funções mais desempenhadas (lane/role)
- Eficiência por elo (ranked tiers)

---

## 📈 Estado Atual do Projeto

- Estudando **web scraping** em sites que listam builds e estatísticas dos campeões.
- Avaliando quais páginas retornam conteúdo **estático** (HTML direto) e quais usam **JavaScript dinâmico** (necessitando renderização).
- Testando diferentes abordagens e bibliotecas para scraping eficiente e completo.

---

## 🧰 Tecnologias e Ferramentas Usadas

### ✅ Linguagem:
- **Python 3.12.10**

### ✅ Bibliotecas:
| Biblioteca     | Status | Descrição                                                                 |
|----------------|--------|--------------------------------------------------------------------------|
| `BeautifulSoup4` | ❌ | Útil para páginas estáticas, mas limitada quando o conteúdo é carregado via JS |
| `Selenium`       | ✅ | Permite simular navegador e lidar com carregamento dinâmico e infinite scroll |

### ✅ Ferramentas:
- **VSCode** – Desenvolvimento
- **Google Chrome** – Testes e depuração do DOM com DevTools

---

