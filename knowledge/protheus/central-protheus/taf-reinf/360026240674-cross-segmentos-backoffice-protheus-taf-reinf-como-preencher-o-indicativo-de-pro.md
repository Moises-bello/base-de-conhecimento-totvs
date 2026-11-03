---
article_id: 360026240674
category: TAF - REINF
content_hash: cb30116e67644d051719263ebbbe5de82248f8fc03cdb8aa4eea4e9f798a8619
fetched_at: '2026-06-28T22:41:33.764155+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como preencher o Indicativo
  de Produtor Rural sobre a Folha de Pagamento para transmissão do R-2055
type: support-article
updated_at: '2023-03-31T17:03:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026240674-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-preencher-o-Indicativo-de-Produtor-Rural-sobre-a-Folha-de-Pagamento-para-transmiss%C3%A3o-do-R-2055
---

**Dúvida**  
Como preencher o Indicativo de Produtor Rural sobre a Folha de Pagamento para transmissão do R-2055 no TAF?  
  
**Ambiente**  
Microsiga Protheus – TAF – A partir da versão 12.1.17  
  
**Solução**

É necessário preencher no cadastro de fornecedor o campo A2\_INDCP com a opção 2 e executar o Extrator fiscal.

![Slide1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360041717173/Slide1.JPG)

Com o sistema alimenta a tabela de Participantes "C1H" no TAF, ao efetuar a apuração do evento será considerada essa opção na transmissão do R-2055.
