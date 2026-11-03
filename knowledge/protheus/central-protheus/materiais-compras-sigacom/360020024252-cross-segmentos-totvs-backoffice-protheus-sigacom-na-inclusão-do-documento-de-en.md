---
article_id: 360020024252
category: Materiais - Compras (SIGACOM)
content_hash: 67530e7cb899c2d67c18f1b05c51d3f085ab7a55249daa7724b05ee9b2e83f7d
fetched_at: '2026-06-28T22:41:09.043787+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Na inclusão do documento
  de entrada o sistema apresenta o Help A100QDEV
type: support-article
updated_at: '2022-05-13T11:40:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020024252-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Na-inclus%C3%A3o-do-documento-de-entrada-o-sistema-apresenta-o-Help-A100QDEV
---

**Dúvida**No Documento de Entrada (MATA103) ao preencher o cabeçalho e o número de série da nota, é apresentada a mensagem informando que o saldo do produto foi totalmente devolvido.

![1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016057692/1.JPG)

**Ambiente**Protheus – Compras – A partir da versão 12  
  
  
**Solução**Consultar na tabela SD2 (Itens de Venda da NF) se o campo D2\_QTDEDEV consta com o mesmo valor do campo D2\_QUANT.

Caso esteja igual, o sistema entende que já houve a devolução e por isso apresenta o alerta.  
Revisar também se há alguma diferença no tamanho dos campos.

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM)
