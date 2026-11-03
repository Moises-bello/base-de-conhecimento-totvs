---
article_id: 6953211823383
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 3bef609465e0e1970b9aace6539a2934366bd33af591a5add9715d3b2f3bd1eb
fetched_at: '2026-06-28T22:42:10.307856+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar
  a coluna 06 da DAPIMG para operações de Entrada? '
type: support-article
updated_at: '2022-08-17T19:38:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6953211823383-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-coluna-06-da-DAPIMG-para-opera%C3%A7%C3%B5es-de-Entrada
---

**Dúvida**Como gerar a **coluna 06** da **DAPIMG** para operações de Entrada?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12

**Solução**

Configure a **TES (Tabela SF4)**, através dos campos:

**Sit.Trib.ICM (F4\_SITTRIB)** = 41 - Outras

**Livro Fiscal ICMS (F4\_LFICM)** = "O" - Outras

O Valor considerado é o valor gravado no campo **Vlr Out ICMS (FT\_OUTRICM)** da **Tabela SFT.**
