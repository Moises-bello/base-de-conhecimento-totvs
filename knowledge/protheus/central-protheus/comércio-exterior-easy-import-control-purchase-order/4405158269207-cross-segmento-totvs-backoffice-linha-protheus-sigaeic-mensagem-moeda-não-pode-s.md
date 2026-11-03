---
article_id: 4405158269207
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 6960a61b2e196f66f1de660dd11b99d31a81529bc65face97b701886774286ba
fetched_at: '2026-06-28T22:39:41.187579+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem moeda
  não pode ser alterada
type: support-article
updated_at: '2021-07-28T17:35:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405158269207-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-moeda-n%C3%A3o-pode-ser-alterada
---

**Dúvida**

Como faço para alterar a moeda informada na rotina do Purchase Order (EICPO400)  uma vez que o sistema exibe esta mensagem **"AVG0000358 - Moeda não pode ser alterada - P.O. possui L.I".***?*

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403964621079/mceclip0.png)*

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**A mensagem exibida no produto*"***Moeda não pode ser alterada - P.O. possui LI***"* não é possível efetuar alteração da moeda pois este Purchase Order possui LI cadastrada. Como solução para o problema será necessário estornar a LI primeiro para depois alterar a moeda no *Purchase Order*. Se houver embarque criado será necessário estonar o embarque também.  
Para descobrir qual a LI que precisa ser estornada é só acessar a tabela SW5 (itens preparação LI) no SQL ou via APSDU e filtrar o campo **W5\_PO\_NUM** com o numero do pedido e verificar qual o conteúdo do campo **W5\_PGI\_NUM**. O conteúdo deste campo **W5\_PGI\_NUM** será o número do processo da *Licença de importação* que será necessário efetuar o estorno para que depois seja alterada a moeda na PO.
