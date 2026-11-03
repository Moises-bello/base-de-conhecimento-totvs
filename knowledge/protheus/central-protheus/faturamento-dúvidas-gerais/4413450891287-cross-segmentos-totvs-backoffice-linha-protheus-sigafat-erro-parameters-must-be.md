---
article_id: 4413450891287
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 0766aad62fe528ca3b7cb6979b742e3850e53b6d230bce1a0b8ca07a45d68032
fetched_at: '2026-06-28T22:38:29.963324+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro: Parameters
  must be of number or date type on MVULMES(SIGACUS.PRW)'
type: support-article
updated_at: '2021-11-17T19:01:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413450891287-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-Parameters-must-be-of-number-or-date-type-on-MVULMES-SIGACUS-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar a Análise de Crédito de Cliente (MATA450A), o sistema gera o erro Parameters must be of number or date type on MVULMES(SIGACUS.PRW).  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 12  
  
**Causa**O erro pode ocorrer quando:

1. Possuir mais de uma filial e uma das filiais não possui o parâmetro **MV\_ULMES**de forma exclusiva;

2. Não existe o parâmetro de forma Default, ou seja, sem atribuição de filial ao mesmo, o tornando comum para todas as filiais.

**Solução**

Para corrigir o problema, é necessário que cada filial possua um parâmetro MV\_ULMES.
