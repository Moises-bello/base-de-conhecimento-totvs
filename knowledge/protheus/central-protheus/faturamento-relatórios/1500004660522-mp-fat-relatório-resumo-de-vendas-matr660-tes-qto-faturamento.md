---
article_id: 1500004660522
category: FATURAMENTO - RELATÓRIOS
content_hash: a7aa2204760a937eca5d54b487fcd46dde58e21048a0b94149932bc10cd1fd3c
fetched_at: '2026-06-28T22:38:23.016082+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: MP - FAT - Relatório Resumo de Vendas (MATR660) - TES Qto Faturamento
type: support-article
updated_at: '2021-04-28T15:15:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004660522-MP-FAT-Relat%C3%B3rio-Resumo-de-Vendas-MATR660-TES-Qto-Faturamento
---

**Dúvida**Como funciona o parâmetro "TES Qto Faturamento" no relatório Resumo de Vendas (MATR660)?  
  
**Ambiente**Microsiga Protheus - Faturamento - A partir da versão 11.80  
  
**Solução**O relatório de Resumo de Vendas (MATR660) possui a pergunta "TES Qto Faturamento" onde é possível definir:

* Gera Financeiro: Sistema deve filtrar as vendas que possuem um TES que contem o campo "Gera Dupl." (F4\_DUPLIC) como "Sim";
* Não Gera: Sistema deve filtrar as vendas que possuem um TES que contem o campo "Gera Dupl." (F4\_DUPLIC) como "Não";
* Considera Ambas: Sistema não realiza filtros baseados no campo "Gera Dupl." (F4\_DUPLIC)

O relatório Resumo de Vendas (MATR660) possui duas colunas, a "Faturamento" e a "Outros Valores":

![01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006139941/01.png)

Ao configurar o filtro do sistema pelo parâmetro "TES Qto Faturamento", os valores que estiverem dentro da condição inserida serão demonstrados na coluna "Faturamento".

Os demais valores, que não estão dentro do filtro, serão demonstrados na coluna "Outros Valores".

Exemplo:

Caso o parâmetro "TES Qto Faturamento" do relatório esteja como "Gera Financeiro", todos os valores das notas em que o TES possuir o campo "Gera Dupl." (F4\_DUPLIC) como "Sim" serão demonstrados na coluna "Faturamento", as notas em que o TES possuir o campo "Gera Dupl." (F4\_DUPLIC) como "Não" serão apresentadas na coluna "Outros Valores".
