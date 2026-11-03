---
article_id: 360022717792
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: da95f12b398b1341c0f2dbaefa3254f6b6b019434921edc3f5b977a380fd8a20
fetched_at: '2026-06-28T22:42:11.821446+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - O registro 5020
  do arquivo da FCI não está sendo gerado
type: support-article
updated_at: '2025-10-28T11:33:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022717792-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-O-registro-5020-do-arquivo-da-FCI-n%C3%A3o-est%C3%A1-sendo-gerado
---

**Dúvida**O registro **5020** do arquivo da FCI não está sendo gerado.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para geração do registro 5020 no arquivo da FCI é necessário o produto constar gravado na CFD com os campos:  
**CFD\_FCICOD** = em branco  
**CFD\_ORIGEM** = 3, 5 ou 8  
**CFD\_PERVEN** = mês de geração do arquivo
