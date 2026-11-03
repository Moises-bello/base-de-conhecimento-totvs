---
article_id: 115005142808
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a2e76fc404ecf2bfa340aeef89ce11bd1fb6762c8daaeda89aa3116e10f3ade5
fetched_at: '2026-06-28T22:37:20.054702+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help A120NDEL apresentado
  ao Estornar a Medição
type: support-article
updated_at: '2026-02-24T11:07:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115005142808-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-A120NDEL-apresentado-ao-Estornar-a-Medi%C3%A7%C3%A3o
---

**Dúvida**

Ao tentar estornar uma medição ocorre o help:

AJUDA:A120NDEL  
Pedido de compra não poderá ser excluído pois já foi movimentado no Protheus.

**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 12

**Solução**

Este Help normalmente é apresentado durante estorno da medição com integração do pedido de compra.

Acesse a  documentação do help "***A120NDEL***" exibido no estorno da medição de contratos do link abaixo no TDN:

[GCT0004\_Assistente\_A120NDEL\_no\_estorno\_da\_medição](http://tdn.totvs.com/pages/releaseview.action?pageId=229769998)

***Obs1:***

Um ponto que pode ser analisado na base/ambiente em questão, é a verificação nos registros das tabelas **CXJ** (**CXJ\_NUMPED**, **CXJ\_ITEMPE**) e **CNE** (**CNE\_PEDIDO**) vinculados a medição em questão, verificando o número do pedido e item exatos que estão vinculado a medição **(podendo ser um ou mais pedidos de possíveis planilhas diferentes associadas a uma medição nesses registros)**, e assim identificando o Pedido e Item para a checagem e assim verificando o pedido correto que esteja de fato já movimentado.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
