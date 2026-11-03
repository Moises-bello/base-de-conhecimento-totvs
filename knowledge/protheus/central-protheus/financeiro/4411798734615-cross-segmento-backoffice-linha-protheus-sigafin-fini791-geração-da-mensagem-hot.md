---
article_id: 4411798734615
category: Financeiro
content_hash: eda8a2ec0738347b43fe0ba700f30237be8651c1d424eb72e4c367283a4e6781
fetched_at: '2026-06-28T22:38:01.036614+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice linha Protheus -  SIGAFIN – FINI791 – Geração da
  mensagem HOTELINVOICE via interação CmNet
type: support-article
updated_at: '2021-10-29T19:20:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411798734615-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-FINI791-Gera%C3%A7%C3%A3o-da-mensagem-HOTELINVOICE-via-intera%C3%A7%C3%A3o-CmNet
---

**Dúvida**Ao gerar um cancelamento de fatura via xml referente a mensagem HOTELINVOICE, não deletando as tabelas XXF,FO8,FO9,FOA, com isso ao integrar a mesma fatura, podendo gerar duplicidade.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – FINI791 A partir da versão 12  
  
  
**Solução**Realmente não é deletado as tabelas, pois no desenvolvimento deste tipo de integração foi mapeado que:

“Uma fatura, uma vez incluída, não poderá ser alterada ou excluída. Apenas será possível cancelar uma fatura e incluir uma nova, que por sua vez deverá possuir um novo número de fatura”

**Segue a documentação mas essas informações:**

<https://tdn.totvs.com/display/public/CMNET/11.1.18.+Faturas+de+hotel>

**Outras documentações sobre o CmNet:**

<https://tdn.totvs.com/display/public/PROT/DSERFINR-3709+DT+Hotelaria+-+Faturas>

<https://tdn.totvs.com/pages/releaseview.action?pageId=538492453>

<https://tdn.totvs.com/pages/releaseview.action?pageId=490980696>

<https://tdn.totvs.com/display/public/PROT/Vendas+-+RetailSales>
