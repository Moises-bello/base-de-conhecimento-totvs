---
article_id: 1500008100982
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: a5b74ad031e8cc335ad5d092494b3ef1a281d5eddfeebbaa51ebb5d48c5a9afe
fetched_at: '2026-06-28T22:39:36.808386+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Alíquotas Diferenciadas
  de PIS e COFINS Apuração (MV_APURPIS e MV_APURCOF)
type: support-article
updated_at: '2022-05-04T14:26:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008100982-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Al%C3%ADquotas-Diferenciadas-de-PIS-e-COFINS-Apura%C3%A7%C3%A3o-MV-APURPIS-e-MV-APURCOF
---

**Dúvida:**  
Como devo utilizar as alíquotas diferenciadas do PIS e COFINS apuração?  
  
**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões.  
  
**Solução:**

Por padrão, as alíquotas diferenciadas de PIS e COFINS são destacadas conforme o regime tributário (lucro real ou presumido), sendo configuradas via SX6 (MV\_TXPIS e MV\_TXCOFIN).

Além das alíquotas conforme o regime de tributação, é possível que o sistema faça a validação respeitando prioritariamente as alíquotas configuradas em:

Exceção Fiscal (SF7) ->Cadastro de Produto (SB1)->Parâmetros (SX6)

Caso o usuário tenha alíquotas diferenciadas, é importante que além da inclusão na exceção ou no produto, os parâmetros abaixo estejam como .F., para que seja aceito uma condição diferente da SX6:

**MV\_APURPIS**

Define se a alíquota de PIS deve permanecer o padrão ou utilizar o conteúdo do parâmetro MV\_TXPIS para Apuração.

**MV\_APURCOF**

Define se a alíquota de PIS deve permanecer o padrão ou utilizar o conteúdo do parâmetro MV\_TXCOFIN para Apuração.
