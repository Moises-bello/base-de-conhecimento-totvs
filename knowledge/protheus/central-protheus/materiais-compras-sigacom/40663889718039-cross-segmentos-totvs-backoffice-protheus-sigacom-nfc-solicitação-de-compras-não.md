---
article_id: 40663889718039
category: Materiais - Compras (SIGACOM)
content_hash: 0a3cb7a7696f2728c99d0d44402b75defe6b2bc7929192105182840f63ec9054
fetched_at: '2026-06-28T22:41:10.061113+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Solicitação de
  compras não aparece na Necessidade de Compras.
type: support-article
updated_at: '2026-05-22T14:09:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40663889718039-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Solicita%C3%A7%C3%A3o-de-compras-n%C3%A3o-aparece-na-Necessidade-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40663889707799) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Solicitação de compras não aparece na Necessidade de Compras.  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - a partir da Release 12.1.2210  
  
**Solução**  
Para solucionar o cenário, é necessário desativar o parâmetro MV\_RESTCOM, deixando com a configuração abaixo:

**MV\_RESTCOM = N**

Com o parâmetro ativo, somente as solicitações que estão configuradas para o Grupo de Compras do solicitante são demonstradas para utilizar no NFC.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível utilizar Grupo de Compras na Rotina de Análise de Cotação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32408591021975-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-utilizar-Grupo-de-Compras-na-Rotina-de-An%C3%A1lise-de-Cota%C3%A7%C3%A3o)

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
