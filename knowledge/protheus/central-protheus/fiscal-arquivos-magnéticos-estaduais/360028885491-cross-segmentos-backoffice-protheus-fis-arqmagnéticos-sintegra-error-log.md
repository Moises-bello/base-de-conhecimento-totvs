---
article_id: 360028885491
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: f464cb3df595e44270002bae484143aea5ad202a5f11e9bb9f73924331a17cbb
fetched_at: '2026-06-28T22:42:11.863045+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sintegra Error
  log
type: support-article
updated_at: '2022-08-18T14:16:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028885491-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sintegra-Error-log
---

**Ocorrência**Ao gerar o arquivo do Sintegra, ocorre o error log abaixo:

 THREAD ERROR ([2964], fiscal, IPSWKS65)   16/07/2018 14:41:51

array out of bounds ( 0 of 1 )  on SINTEGRA(MATA940.PRX) 24/05/2018 12:04:40 line : 2790

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80

**Causa**Esse erro ocorre quando os campo D2\_CF referente a CFOP, está com o conteúdo diferente das tabelas SFT e SF3, os campos FT\_CFOP e F3\_CFO.

**Solução**Para corrigir o problema  é preciso identificar no error log a última nota fiscal processada(que é a que geralmente ocorre o erro) e verificar esses campos se estão todos IGUAIS.

Obs.: o problema também pode ocorrer para documentos de entrada e para mais de uma nota.
