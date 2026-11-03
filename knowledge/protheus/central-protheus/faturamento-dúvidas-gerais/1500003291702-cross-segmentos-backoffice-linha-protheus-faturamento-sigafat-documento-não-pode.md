---
article_id: 1500003291702
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 874be1f9cda7be577a4a36cbe9de1b2cac196a370599fe32cba4317a45252acb
fetched_at: '2026-06-28T22:38:32.984444+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) -  Documento
  não pode ser excluído, pois esta associado a um pedido de compra
type: support-article
updated_at: '2022-09-20T16:34:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003291702-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Documento-n%C3%A3o-pode-ser-exclu%C3%ADdo-pois-esta-associado-a-um-pedido-de-compra
---

**Dúvida**Ao excluir nota de saída esta apresentando a mensagem: Documento não pode ser Excluído, pois esta associado a um Pedido de Compra.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) – A partir da versão 11.80  
  
**Solução**

A nota de entrada referenciada ao beneficiamento deve ser excluída (Nota de Entrada), para depois excluir a nota de saída.

A mensagem é apresenta pelo motivo do campo **C7\_QUJE** ter conteúdo maior que zero, essa validação esta no MATA521.  
O campo **C7\_QUJE** é preenchido por exemplo, quando é realizado o retomo de beneficiamento.
