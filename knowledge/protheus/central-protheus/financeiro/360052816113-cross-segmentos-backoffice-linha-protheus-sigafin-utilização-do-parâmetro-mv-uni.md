---
article_id: 360052816113
category: Financeiro
content_hash: 920f1e881317d9d1dde41268b2a6079e7a80e96bcbe2719d6bd976eb5809ca1d
fetched_at: '2026-06-28T22:38:01.010346+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Utilização do parâmetro
  MV_UNIAO
type: support-article
updated_at: '2025-09-12T20:12:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052816113-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-UNIAO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34904352042775)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**É possível definir a loja do fornecedor definido no parâmetro MV\_UNIAO para geração do título de imposto?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**Não é possível definir o código da loja para o fornecedor definido no parâmetro **MV\_UNIAO**. A loja, por padrão, é fixa em "**00**", conforme o tamanho do campo loja. Portanto, ao gerar título de imposto federal no contas a pagar, o fornecedor utilizado para este será o conteúdo do parâmetro **MV\_UNIAO**+ Loja 00.
