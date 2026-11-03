---
article_id: 25143292599831
category: Financeiro - Contabilização
content_hash: 2171c6ecc28881581c614fb588fdf9280e2aeb9f3a2b326d57eb59ecfd85d1be
fetched_at: '2026-06-28T22:38:05.306074+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Contabilização Online com variável
  VALOR aglutina
type: support-article
updated_at: '2024-07-25T11:09:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25143292599831-Cross-Segmentos-Backoffice-Linha-Protheus-Contabiliza%C3%A7%C3%A3o-Online-com-vari%C3%A1vel-VALOR-aglutina
---

Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**  
O que fazer quando não consigo realizar a contabilização online de forma individual?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**  
Para algumas LPs, a variável VALOR é utilizada para a contabilização, mas seu comportamento difere da contabilização offline.

**Solução**

Na contabilização online, quando o lançamento padrão está configurado com o campo **CT5\_VLR01** usando a variável "**VALOR**", um lançamento contábil será gerado contendo o total compensado para a NF.

Esse comportamento não está relacionado ao parâmetro **"Aglutina Lançamentos?"** a rotina, mas é um comportamento padrão da contabilização online.

Por outro lado, exemplo, caso esteja contabilizando a tabela SE5 se o campo **CT5\_VLR01** estiver configurado com o conteúdo **SE5->E5\_VALOR**, será gerado um lançamento contábil para cada NF relacionada.

Deverá informar na CT5\_VLR01 a tabela que pretende utilizar para a contabilização.

**Saiba mais**  
[Contabilização da alteração da situação de cobrança](https://tdn.totvs.com/pages/releaseview.action?pageId=555857451)

[Contabilização Offline - CTBAFIN](https://tdn.totvs.com.br/pages/releaseview.action?pageId=497932563)
