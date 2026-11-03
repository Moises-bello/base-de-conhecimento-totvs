---
content_hash: 684fc12a9da8c343adacfb487815c26fbec1abb7eb0f1dc0d38cabc3b4260538
fetched_at: '2026-06-29T00:09:53.571720+00:00'
page_id: '440845538'
product: rm
source: tdn-rm
title: Gerar Matriz de Impacto e Probabilidade de Riscos
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Matriz+de+Impacto+e+Probabilidade+de+Riscos
version: 1
---

---

Este processo irá gerar a matriz de impacto e probabilidade de todos os riscos do projeto, considerando os valores mais atuais de impacto e probabilidade sobre cada objetivo.  
A matriz será apresentada de acordo com Tipo da matriz e Objetivo do Projeto.

* Tipo da matriz - os tipos possíveis são Ameaça ou Oportunidade.
* Objetivos do Projeto - os objetivos possíveis serão previamente cadastrados no grupo de objetivos parametrizado no projeto.

**Observações:**  
Se a escolha da visualização da matriz seja Ameaça, serão apresentados todos os riscos do projeto do tipo ameaça. Caso o tipo da matriz seja Oportunidade serão apresentados todos os riscos do projeto do tipo oportunidade.  
Só serão apresentados na matriz os riscos que tiverem valor de impacto e probabilidade definidos para o objetivo escolhido.  
O processo é constituído pelo seguinte passo:

1. Obteção de todos os riscos do projeto considerando os valores mais atuais de impacto e probabilidade para cada objetivo.
2. Para cada valor de impacto e probabilidade é verificado na escala parametrizada no projeto sobre qual quadrante da matriz o risco será posicionado.

**Atenção:**

* O sistema considera como valor mais atual, aquele definido em reunião com data de abertura mais recente.

**Observações:**

* O dimensionamento da matriz poderá ser feito através da opção "Tamanho da Matriz";
* As cores da matriz serão definidas a partir do grupo de áreas de prioridade parametrizado no projeto;
* Os riscos exibidos na matriz serão identificados pelo código.

É necessário que o projeto esteja parametrizado com a escala, grupo de objetivos do projeto e grupo de área de prioridades pra que a matriz seja exibida.
