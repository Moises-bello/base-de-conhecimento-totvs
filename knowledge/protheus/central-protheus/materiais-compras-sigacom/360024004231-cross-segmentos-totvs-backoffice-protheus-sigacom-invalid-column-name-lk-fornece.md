---
article_id: 360024004231
category: Materiais - Compras (SIGACOM)
content_hash: e88ea58956b0cd3ded4612d6f40834b2f0cbd5849ce8543571ac342c24a5acdd
fetched_at: '2026-06-28T22:41:08.984206+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Invalid column name
  'LK_FORNECE' ao excluir/alterar fornecedor
type: support-article
updated_at: '2022-05-12T21:25:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024004231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Invalid-column-name-LK-FORNECE-ao-excluir-alterar-fornecedor
---

**Ocorrência**Invalid column name 'LK\_FORNECE' ao excluir/alterar fornecedor

**Ambiente**Protheus – Compras – A partir da versão 12.1.17  
  
**Causa**Ao excluir o cadastro do fornecedor o sistema exibe o error.log Invalid column name 'LK\_FORNECE'  
  
**Solução**Para solucionar essa ocorrência, deve-se criar dois campos no sistema.

Criar os campos LK\_FORNECE e LK\_LOJA.

LK\_FORNECE  =    Caracter = 6   
LK\_LOJA         =    Caracter = 2
