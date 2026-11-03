---
article_id: 4412890512023
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 62b556c0c36bda85dfc1f8b24e69d544f40f2e3e1494baea215aedc93548c281
fetched_at: '2026-06-28T22:39:41.202523+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  para incluir campos das entidades contabeis
type: support-article
updated_at: '2022-05-30T14:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890512023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-para-incluir-campos-das-entidades-contabeis
---

**Dúvida**Preciso levar para o Pedido de Compras (MATA121) os campos das seguintes entidades: classe valor, centro de custo e item conta. Temos algum ponto de entrada? Preciso inserir no pedido de compras e na nota de entrada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Para o envio dos valores na fase do Pedido, utilize a função **EICPO400**, parâmetro **PO400GRAVAPC\_ITEM**, permite gravar informações do item do pedido de compras na tabela **SC7**modificando a variável **aItensPo**.  
Para o envio dos valores na fase da nota, utilize a função **EICDI154**, parâmetro **GRAVACAO\_SF1**, modificando a variável **aItens**.  
  
**Saiba Mais**[PE EICPO400 - Manutenção do Purchase Order](https://tdn.totvs.com/pages/releaseview.action?pageId=224102887)  
[PE EICDI154 - Recebimento de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=574364993)
