---
article_id: 4405269792023
category: Comércio Exterior - Easy - Financing
content_hash: b161fb506476fb5655d029c1d85453cfbc3a8e7785c0943778fc027169c08c0e
fetched_at: '2026-06-28T22:39:52.961218+00:00'
product: protheus
section_id: 1500001538101
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEFF - Botão Estorna
  liquidação não é exibido ao liquidar o contrato
type: support-article
updated_at: '2021-07-29T20:47:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405269792023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEFF-Bot%C3%A3o-Estorna-liquida%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-exibido-ao-liquidar-o-contrato
---

**Dúvida**Notamos que o botão de estornar liquidação desaparece após a liquidação do contrato na rotina Manutenção de Contrato de Exportação (EFFEX400).

A) Antes de liquidar o campo de estorno esta na tela.

![estorno_liquida__o_menu.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405265888279/estorno_liquida__o_menu.PNG)

B)Depois de efetuar a liquidação do contrato .

![menu_apos_a_liquida__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405266069399/menu_apos_a_liquida__o.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Financing* – Todas versões.  
  
**Solução**O botão estorna liquidação fica somente disponível para estorno de outros eventos na manutenção de contrato. Sendo assim, quando é liquidado o contrato, o botão de estorno da liquidação fica indisponível. Quando é liquidado o contrato o sistema preenche a data de encerramento que é o campo Dt. Encerra (EF1\_DT\_ENC) , com isso para estornar a liquidação do contrato é só limpar o campo Dt. Encerra (EF1\_DT\_ENC) para que o estorno seja efetuado.
