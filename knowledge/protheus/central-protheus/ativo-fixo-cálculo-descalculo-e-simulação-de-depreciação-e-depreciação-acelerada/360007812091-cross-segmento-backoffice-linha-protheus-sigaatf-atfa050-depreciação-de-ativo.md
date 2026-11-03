---
article_id: 360007812091
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: d9e394ac46b0cde6e567054e18a4b02f65335075f183a6bcaffd74ea17525d6b
fetched_at: '2026-06-28T22:41:43.210991+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF ATFA050 - Depreciação
  de Ativo
type: support-article
updated_at: '2023-05-10T18:01:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007812091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Deprecia%C3%A7%C3%A3o-de-Ativo
---

**Dúvida**

Como funciona a rotina de depreciação ativo fixo?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Ativo Fixo  – A partir da versão 12.

**Solução**

A rotina de Calculo Mensal(ATFA050) só permite que a depreciação seja realizada no último dia do mês, ou seja, não é possível efetuar duas ou mais depreciações no mesmo mês.

Documentação:

[Cálculo (ATFA050 - SIGAATF)](https://tdn.totvs.com/pages/releaseview.action?pageId=312159943)

**Observação**: Para fins de baixas parciais, deve ser utilizado a rotina de Baixa(ATFA036) com o parâmetro MV\_TIPDEPR.

• MV\_ATFDPDI

• MV\_ATFMCCM

• MV\_ATFMDMX

• MV\_ATFMOED

• MV\_TIPDEPR

• MV\_ULTDEPR

• MV\_VALCORR

• MV\_ATFRSLD

**Saiba Mais:**

[Help :Métodos de Depreciação Gerencial](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigaatf_metodos_deprec_gerencial_bra.htm)

[TDN :Métodos de Depreciação Gerencial](http://tdn.totvs.com/pages/releaseview.action?pageId=6067556)

[Cálculo de Depreciação](http://tdn.totvs.com/pages/releaseview.action?pageId=6067612)

[Depreciação na Gestão Patrimonial](http://tdn.totvs.com/pages/releaseview.action?pageId=6067627)

[Porque o sistema não calcularia a depreciação de um bem?](http://tdn.totvs.com/pages/viewpage.action?pageId=6067622)
