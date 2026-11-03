---
article_id: 24417068171927
category: TAF - REINF
content_hash: 076f93618db1d2b1964ad956667ab0f7b6fb5ca4b4783082fae0edc06a57b917
fetched_at: '2026-06-28T22:41:34.850538+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1556
type: support-article
updated_at: '2024-06-26T20:47:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24417068171927-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1556
---

**Ocorrência**

No módulo TOTVS automação fiscal(TAF) ao transmitir um evento periódico é  retornada a rejeição MS1556.

![MS1556.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24417068144407)  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões.

**Causa**

  O código MS1556 é apresentado quando o período está encerrado no E-cac, aberto no TAF e enviado uma nova transmissão de um eventos periódico,

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. O Período tem que estar aberto(em andamento) no site da RFB.

2. Exclua a apuração inconsistente.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente?source=search)

3. Após o período ter sido reaberto e excluído a apuração inconsistente, apure e transmite o evento novamente.

IMPORTANTE: As ações realizadas diretamente no E-cac, seja o encerramento ou a reabertura é de responsabilidade da empresa local, a Totvs não orienta qualquer ação diretamente no e-Cac por perder o vinculo dos dados entre Software e Governo.
