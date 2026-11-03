---
article_id: 360028795492
category: Escrita Fiscal - Impostos - ICMS
content_hash: 486c3e1bcf2ced9e52e55cf434cd09ac103b77a31efcedfae91a2e8f9629a632
fetched_at: '2026-06-28T22:39:24.176312+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar para
  considerar o fornecedor do frete(MATA116) e não o fornecedor da mercadoria na aplicação
  da exceção fiscal? 
type: support-article
updated_at: '2021-07-28T03:10:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028795492-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-para-considerar-o-fornecedor-do-frete-MATA116-e-n%C3%A3o-o-fornecedor-da-mercadoria-na-aplica%C3%A7%C3%A3o-da-exce%C3%A7%C3%A3o-fiscal
---

**Dúvida**

Como configurar para considerar o fornecedor do frete(MATA116) e não o fornecedor da mercadoria na aplicação da exceção fiscal?   
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Para que a exceção fiscal o sistema valide o fornecedor do frete configure o  parâmetro MV\_M116FOR como T.

MV\_M116FOR - Descrição: Define a origem dos impostos para gerar a nota de conhecimento de frete.

**T= Fornecedor do frete**  
**F= Fornecedor da nota de origem.**
