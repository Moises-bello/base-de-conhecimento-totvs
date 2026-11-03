---
article_id: 24418917639319
category: TAF - REINF
content_hash: df9dc3b4efc05e27a3cdbef7b6eba04087513fd9d68bd28bdb16da87b3c352a4
fetched_at: '2026-06-28T22:41:34.847820+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1484
type: support-article
updated_at: '2024-06-26T13:03:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24418917639319-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1484
---

**Ocorrência**No módulo TOTVS automação fiscal(TAF) ao transmitir um evento periódico é retornada a rejeição MS1484.

**![MS1484.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24418906891287)**

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões.  
  
**Causa**O erro retornado pela receita ocorre porque o evento R-4099 não deve ser transmitido caso não tenha envio de eventos periódicos do bloco 40.

**Solução**

 Na falta de movimento periódicos não deve ser transmitido o evento R-4099, conforme o manual de orientação da RFB.

![MS1484manual.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24418917621399)

 Exclua a apuração inconsistente para adequação do ambiente.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente?source=search)

Referência: <http://sped.rfb.gov.br/arquivo/show/7261>
