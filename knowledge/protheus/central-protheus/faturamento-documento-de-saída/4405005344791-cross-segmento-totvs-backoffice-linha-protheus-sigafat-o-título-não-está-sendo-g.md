---
article_id: 4405005344791
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7409fe0d69f2220fbc865b5a6a3d3d8f63847e372cf940f97109099efe94120d
fetched_at: '2026-06-28T22:38:43.947033+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- O título não
  está sendo gerado no faturamento da nota de saída no módulo de Faturamento
type: support-article
updated_at: '2024-04-11T17:01:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405005344791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-O-t%C3%ADtulo-n%C3%A3o-est%C3%A1-sendo-gerado-no-faturamento-da-nota-de-sa%C3%ADda-no-m%C3%B3dulo-de-Faturamento
---

**Dúvida**O título não está sendo gerado no faturamento da nota de saída no módulo de Faturamento.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Todas as versões.  
  
**Solução**

O que define se uma Nota de saída(**MATA461**) será gerada e integrada ao módulo do Financeiro é o **TES (MATA080)**.  
  
Desta forma, verifique se o TES utilizado na movimentação gera financeiro, se não controla Poder de Terceiros e se está com o Campo Agrega Valor igual a Sim.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405005096727/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405005081111/mceclip0.png)​  
  
Além disto, o Tipo de Pedido de Vendas (**MATA410**)não pode ser do tipo **B (Beneficiamento),** pois o pedido do tipo B, tem como finalidade tratar guarda/conserto/beneficiamento, utilizando controle de poder de terceiros de produto, seja remessa ou devolução. Não se trata de ***VENDA*** e sim, ***Movimentação** **de Estoque***, com isso, ***não gera Financeiro***.  
  
Não há  dentro do Faturamento, rotina de reprocessamento para gerar o Titulo após a inclusão da Nota Fiscal. Caso seja necessário incluir um titulo depois da geração da Nota Fiscal de Saída, somente será possível incluindo de forma manual na rotina de Contas a Receber no modulo Financeiro.
