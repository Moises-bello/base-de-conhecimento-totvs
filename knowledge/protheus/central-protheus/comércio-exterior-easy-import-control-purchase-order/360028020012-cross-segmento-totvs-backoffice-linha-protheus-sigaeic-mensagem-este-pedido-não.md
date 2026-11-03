---
article_id: 360028020012
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: dddd4fc994c6649e8cd2fe80fb387de3900b6a3501e9a2b6fbe42c8d17e73232
fetched_at: '2026-06-28T22:39:41.193845+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem: Este
  pedido não pode ser alterado/excluido pelo módulo de compras, pois foi emitido pelo
  módulo Easy Import Control atraves da P.O.'
type: support-article
updated_at: '2022-02-04T17:23:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028020012-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-Este-pedido-n%C3%A3o-pode-ser-alterado-excluido-pelo-m%C3%B3dulo-de-compras-pois-foi-emitido-pelo-m%C3%B3dulo-Easy-Import-Control-atraves-da-P-O
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao alterar um pedido de compras originado do SIGAEIC, é apresentada a mensagem ORIGIMP - "Este pedido não pode ser alterado/excluído pelo módulo de compras, pois foi emitido pelo módulo Easy Import Control atraves da P.O."

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028287932/mceclip0.png)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – A partir da versão 11.80  
  
**Solução**A mensagem é apresentada pois o Pedido de Compras foi originado do Purchase Order no módulo SIGAEIC. Toda e qualquer alteração deve ser feita no módulo de origem SIGAEIC.  
  
1. Acesse o módulo SIGAEIC em Atualizações / Purchaser Order / manutenção (EICPO400), posicione sobre o processo, selecione Alterar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028286291/mceclip1.png)

Após fazer todas as alteração na Purchase Order "P.O.", salvar o P.O e as alterações serão refletidas no Pedido de Compras.
