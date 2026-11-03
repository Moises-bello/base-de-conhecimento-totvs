---
article_id: 360036071533
category: RH - Rescisão
content_hash: aae0e290e0a15f7d901769e6b049c3b6b090817071a0a7781338670f4da7a545
fetched_at: '2026-06-28T22:43:50.892138+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema está considerando as faltas para abatimento
  de avos mesmo alterando a quantidade na rotina de Controle de Dias de Direito
type: support-article
updated_at: '2025-10-24T14:06:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036071533-RH-Linha-Protheus-GPE-Sistema-est%C3%A1-considerando-as-faltas-para-abatimento-de-avos-mesmo-alterando-a-quantidade-na-rotina-de-Controle-de-Dias-de-Direito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16838652128919) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Por que o sistema está considerando as faltas para abatimento de avos mesmo alterando a quantidade na rotina de Controle de Dias de Direito?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O módulo SIGAGPE não utiliza os campos da rotina de Controle de Dias de Direito como base para compor as faltas que irão abater os avos de férias. O módulo realiza a busca diretamente no acumulado do funcionário. Desta forma, existindo a verba de faltas nos acumulados e se esta verba estiver com S no campo médias férias, será executado o abatimento dos avos de férias de acordo com a quantidade de dias de faltas.

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Como conferir faltas do funcionário apresentadas no cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjND9XUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzAxODU3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25mZXJpci1mYWx0YXMtZG8tZnVuY2lvbiVDMyVBMXJpby1hcHJlc2VudGFkYXMtbm8tYyVDMyVBMWxjdWxvLWRlLWYlQzMlQTlyaWFzBjsIVDoOc2VhcmNoX2lkSSIpNWNiM2I4M2ItNTAzYS00MGI0LTk0ZTgtNWZmZjcxMGMxYmEwBjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIbcmVlbWJvbHNvIGZhbHRhIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpZQ%3D%3D--f756a8023567cc8f9b833e8595909da35b581f21)  
[RH - Linha Protheus - GPE - Funcionamento do parâmetro MV\_SEGFALT nas faltas no Controle Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgayLLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDc3MTk5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRnVuY2lvbmFtZW50by1kby1wYXIlQzMlQTJtZXRyby1NVi1TRUdGQUxULW5hcy1mYWx0YXMtbm8tQ29udHJvbGUtRGlhcy1kZS1EaXJlaXRvBjsIVDoOc2VhcmNoX2lkSSIpOTk1NGM3YWQtZDE5NC00NWYxLTgzZGEtNjc1NjgyZTNmYWQ3BjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIgY29udHJvbGUgZGUgZGlhcyBkZSBkaXJlaXRvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--03b4fae0db55956cabc3bf608a992124cd9c41de)  
[RH - Linha Protheus - GPE - Como efetuar manutenção do Controle de Dias de Direito após o fechamento do período](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjle0vVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBw2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MDc3OTQ5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW1hbnV0ZW4lQzMlQTclQzMlQTNvLWRvLUNvbnRyb2xlLWRlLURpYXMtZGUtRGlyZWl0by1hcCVDMyVCM3Mtby1mZWNoYW1lbnRvLWRvLXBlciVDMyVBRG9kbwY7CFQ6DnNlYXJjaF9pZEkiKTk5NTRjN2FkLWQxOTQtNDVmMS04M2RhLTY3NTY4MmUzZmFkNwY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiIGNvbnRyb2xlIGRlIGRpYXMgZGUgZGlyZWl0bwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--7bb446bdfeb1350561489427db87a9871b32b82e)  
[RH - Linha Protheus - GPE - No cálculo da rescisão, o sistema verifica a quantidade de faltas da rotina de Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwieMa3TUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBz2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzMzYyODU3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTm8tYyVDMyVBMWxjdWxvLWRhLXJlc2NpcyVDMyVBM28tby1zaXN0ZW1hLXZlcmlmaWNhLWEtcXVhbnRpZGFkZS1kZS1mYWx0YXMtZGEtcm90aW5hLWRlLUNvbnRyb2xlLWRlLURpYXMtZGUtRGlyZWl0bwY7CFQ6DnNlYXJjaF9pZEkiKTk5NTRjN2FkLWQxOTQtNDVmMS04M2RhLTY3NTY4MmUzZmFkNwY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiIGNvbnRyb2xlIGRlIGRpYXMgZGUgZGlyZWl0bwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--ef838f7b4833ec0ed27e5f75c01e40f051292166)
