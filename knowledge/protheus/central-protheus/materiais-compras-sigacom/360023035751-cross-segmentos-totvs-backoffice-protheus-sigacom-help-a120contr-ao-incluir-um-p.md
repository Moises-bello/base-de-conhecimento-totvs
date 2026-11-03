---
article_id: 360023035751
category: Materiais - Compras (SIGACOM)
content_hash: 4dc25efc8e318dcc45e2b74afb93c8eced2648ddd2e5bef93a05dcd7cab74adf
fetched_at: '2026-06-28T22:41:08.916783+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A120CONTR ao incluir
  um pedido de compra
type: support-article
updated_at: '2022-05-12T21:20:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023035751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A120CONTR-ao-incluir-um-pedido-de-compra
---

**Ocorrência**Help **A120CONTR** ao incluir um pedido de compra

**Ambiente**Protheus - Compras – A partir da versão 11.80  
  
**Causa**

No módulo Compras, ao confirmar a inclusão do pedido de compra é apresentado o assistente **A120CONTR.**

Esse incidente ocorre pois o produto está configurado para ser utilizado somente com contrato de parceria.  
  
**Solução**Para solucionar essa ocorrência é necessário alterar o campo **B1\_CONTRAT** para Não ou Ambos no Cadastro do Produto (MATA010) ou habilitar o parâmetro **MV\_PRODCTR**
