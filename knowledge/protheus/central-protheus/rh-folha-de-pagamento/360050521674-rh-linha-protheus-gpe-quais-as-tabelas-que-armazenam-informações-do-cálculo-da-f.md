---
article_id: 360050521674
category: RH - Folha de Pagamento
content_hash: a66648a7eebf14285d495dd407240328f6f48bff13e54a3dba852e6a4b19580d
fetched_at: '2026-06-28T22:44:16.207249+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Quais as tabelas que armazenam informações do Cálculo
  da Folha de pagamento
type: support-article
updated_at: '2025-04-22T17:16:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050521674-RH-Linha-Protheus-GPE-Quais-as-tabelas-que-armazenam-informa%C3%A7%C3%B5es-do-C%C3%A1lculo-da-Folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17318452690455) Tempo aproximado para leitura: 00:01:00 min  
  
  
Dúvida**Quais tabelas ficam armazenadas informações de cálculos já realizados da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**

**Verbas informadas para um período aberto** antes do cálculo da folha ficam na tabela RGB - Lançamentos Por Funcionário

**Período aberto**, após o calculo da folha ficam na tabela SRC - Valores Mensais

**Período fechado**, após o calculo e fechamento da folha ficam na tabela SRD - Valores Acumulados.

**Saiba Mais:**[RH - Linha Protheus - GPE - É possível emitir relatório de acumulados em formato planilha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXMuEMJgY6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzY3NjA0OTQ2MDkwNDctUkgtTGluaGEtUHJvdGhldXMtR1BFLSVDMyU4OS1wb3NzJUMzJUFEdmVsLWVtaXRpci1yZWxhdCVDMyVCM3Jpby1kZS1hY3VtdWxhZG9zLWVtLWZvcm1hdG8tcGxhbmlsaGEGOwhUOg5zZWFyY2hfaWRJIik0MGY1MzQ5OC00NGVhLTRmYjItYjk4Mi05MGIxNmI0NzhkNTUGOwhGOglyYW5raQ86C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg90YWJlbGEgU1JEBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--0cd63d271f4b718f810950284fec30bfc707344f)  
[RH - Linha Protheus - GPE - Como calcular a folha pela rotina Lançamentos por Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg6ErM%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMTIyODY1MjItUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY2FsY3VsYXItYS1mb2xoYS1wZWxhLXJvdGluYS1MYW4lQzMlQTdhbWVudG9zLXBvci1GdW5jaW9uJUMzJUExcmlvcwY7CFQ6DnNlYXJjaF9pZEkiKTIyNDJkYzlhLTk5OTgtNDdkMi05ODNkLWVmZWE4MzczMmVmYQY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiIGxhbsOnYW1lbnRvIHBvciBmdW5jaW9uYXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--a6940dbb63b2ce3d5af39f909019335f04a49fc5)  
[RH - Linha Protheus - GPE - Como identificar a origem das verbas no cálculo mensal do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiEpUfTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNjk3MzU3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pZGVudGlmaWNhci1hLW9yaWdlbS1kYXMtdmVyYmFzLW5vLWMlQzMlQTFsY3Vsby1tZW5zYWwtZG8tZnVuY2lvbiVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWUwMzM5NTBiLTUxMDEtNDI0Yy04ZjBhLTc5OWYwNTkyM2FkYQY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFm9yaWdlbSBkYXMgdmVyYmFzBjsIVDoScmVzdWx0c19jb3VudGkCQQU%3D--8c8222858958bd6451d281eeda2ddb55c217b131)  
[RH - Linha Protheus - GPE - Como consultar o calculo da folha do movimento aberto (SRC) ou fechado (SRD) de um trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgx3V3UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NTIwNjgzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25zdWx0YXItby1jYWxjdWxvLWRhLWZvbGhhLWRvLW1vdmltZW50by1hYmVydG8tU1JDLW91LWZlY2hhZG8tU1JELWRlLXVtLXRyYWJhbGhhZG9yBjsIVDoOc2VhcmNoX2lkSSIpZDMzZGMzZDQtMmQzNi00NTFiLWEzMTgtNWQ0M2MzNGI1NmUwBjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIIU1JEBjsIVDoScmVzdWx0c19jb3VudGkBig%3D%3D--aa9a4c7fed66efd5fbd869e1d095ea871949a2da)
