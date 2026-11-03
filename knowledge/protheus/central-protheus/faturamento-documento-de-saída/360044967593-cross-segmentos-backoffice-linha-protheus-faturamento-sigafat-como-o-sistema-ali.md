---
article_id: 360044967593
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: cd13850e3bdbb2497a747029957f2d0e4d0f282ea9a7b5efe4af5d7a746502d0
fetched_at: '2026-06-28T22:38:43.963482+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Como
  o sistema alimenta os campos D2_CUSTO no faturamento da nota (MATA461)
type: support-article
updated_at: '2022-09-16T11:52:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044967593-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Como-o-sistema-alimenta-os-campos-D2-CUSTO-no-faturamento-da-nota-MATA461
---

**Dúvida**

Como o sistema alimenta o campo **D2\_CUSTO1/2/3/4/5** no faturamento da nota **(MATA461)**?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Solução**

O campo **D2\_CUSTO**(**1/2/3/4/5**) é o resultado  do campo **D2\_QUANT \* B2\_CM** (**1/2/3/4/5)** - que é o custo médio do produto).O **B2\_CM** (**1 a 5**) é atualizado sempre que feita uma entrada do produto, e corresponde a divisão do **B2\_VATU** pelo **B2\_QATU**.
