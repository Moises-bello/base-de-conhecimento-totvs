---
article_id: 360053131954
category: ADVPL - Ponto de Entrada
content_hash: 881fa2878bd9918d6b3b7d05ef13d580ce96dbd14886859a11c886c9edc7c9e4
fetched_at: '2026-06-28T22:40:11.647367+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Aprovação de Documento:
  Não passa no ponto de entrada ECMStart '
type: support-article
updated_at: '2022-06-21T17:58:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053131954-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Aprova%C3%A7%C3%A3o-de-Documento-N%C3%A3o-passa-no-ponto-de-entrada-ECMStart
---

**Dúvida**A rotina Aprovação de Documento não chama o ponto de entrada ECMStart, qual o motivo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**O Ponto de Entrada **ECMStart**, é acionado somente no momento que a aprovação é enviada para o **Fluig**, ou seja, quando a alçada está com **Status: "*****Pendente"***no Protheus, quando a mesma estiver com **Status: "Aguardando níveis anteriores"**, não será enviada para o **Fluig** nesse momento, somente será enviada quando todo nível for liberado e deixar o próximo Nível como "**Pendente"**é que o Envio ocorrerá**.**
