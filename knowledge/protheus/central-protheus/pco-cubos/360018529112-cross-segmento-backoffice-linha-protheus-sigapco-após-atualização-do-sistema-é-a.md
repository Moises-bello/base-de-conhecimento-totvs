---
article_id: 360018529112
category: PCO - Cubos
content_hash: 7e0c2f9b0a3b9505d144bb22a411eb99e1c447ec8756f3015440c28f60645448
fetched_at: '2026-06-28T22:37:11.506436+00:00'
product: protheus
section_id: 1500001550862
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Após atualização do
  sistema é apresentada mensagem O Cubo deverá ser Reprocessado.
type: support-article
updated_at: '2023-11-21T13:06:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018529112-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Ap%C3%B3s-atualiza%C3%A7%C3%A3o-do-sistema-%C3%A9-apresentada-mensagem-O-Cubo-dever%C3%A1-ser-Reprocessado
---

**Dúvida**Após atualização do sistema é apresentada mensagem O Cubo deverá ser Reprocessado.

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

Após incluir um processo de integração relacionado ao módulo PCO, a mensagem os Saldos do Cubo deverão ser Reprocessados em diferentes origem das integrações.

* Para que esse Help não seja mais apresentado se faz necessária a Instalação das Stored Procedures atualizadas, Relacionadas aos módulo PCO, são as Procedures 12.SPS e 13.SPS.   
  Ambas estão disponíveis para Download através do Portal do Cliente.

**Importante**

Caso já possua as Stored Procedures instaladas, se faz necessário, desinstalar as Stored Procedures 12 e 13, e instalar as mesmas atualizadas conforme Portal, através do módulo Configurado.

Para Maiores informações de como instalar as Stored Procedures consulte o link :

[Cross Segmento - Backoffice Linha Protheus - SIGACTB/SIGAATF/SIGPCO - Atualização de procedure com status Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX4b%2BB1RA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE4NTA5MTkwOTE0NDU1LUNyb3NzLVNlZ21lbnRvLUJhY2tvZmZpY2UtTGluaGEtUHJvdGhldXMtU0lHQUNUQi1TSUdBQVRGLVNJR1BDTy1BdHVhbGl6YSVDMyVBNyVDMyVBM28tZGUtcHJvY2VkdXJlLWNvbS1zdGF0dXMtSW5jb21wYXQlQzMlQUR2ZWwtBjsIVDoOc2VhcmNoX2lkSSIpMWY0YjhjNmUtNmZjNS00YzMyLTk1ZTUtMGQ3NjQzMWE4OTBlBjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPUHJvY2VkdXJlIAY7CFQ6EnJlc3VsdHNfY291bnRpAr0C--44abba5fc5da648c02c05d40667ecc689cf44630)
