---
article_id: 360050241553
category: RH - Lançamentos
content_hash: 9c23eed630161a6c7e8e12ebc330756b26ba32f22af31ddf5c354c63456a38b3
fetched_at: '2026-06-28T22:43:31.324449+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Lançamentos Fixos - Campo Proporcional
type: support-article
updated_at: '2025-07-23T18:11:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050241553-RH-Linha-Protheus-GPE-Lan%C3%A7amentos-Fixos-Campo-Proporcional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26079914744599) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao realizar um lançamento fixo com o campo proporcional = SIM, o sistema não proporciona de acordo com a data inicial informada.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Isso ocorre porque o campo **proporcional** quando está com **SIM** proporcionaliza **de acordo com a quantidade de dias trabalhados no mês.**

Os campos **Data de inicio** e **Data fim** tem como objetivo **informar** quando **inicia** e quando **termina** este lançamento fixo, mas o calculo **não será proporcionalizado** olhando esses campos.

**Exemplos**  
Funcionário possui **15** dias **trabalhados** e 15 dias de férias. Com campo proporcional = **SIM** o sistema calcula 15 dias da verba lançada em lançamentos fixos. Caso esteja com o campo proporcional = **NÃO,** o sistema calcula **30** dias da verba lançada em lançamentos fixos.

**1**. Calculo com o campo Proporcional = **NÃO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434917434775)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434917438743)

**2**. Calculo com o campo Proporcional = **SIM** 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434917439767)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434917441175)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Qual é a rotina para Lançamentos de Verbas para o cálculo da folha?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXbVVv4Qs6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzMDYyODYzNDE2NTk5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFsLSVDMyVBOS1hLXJvdGluYS1wYXJhLUxhbiVDMyVBN2FtZW50b3MtZGUtVmVyYmFzLXBhcmEtby1jJUMzJUExbGN1bG8tZGEtZm9saGEtBjsIVDoOc2VhcmNoX2lkSSIpZTUxNWI0YjEtYjZlNi00YTdiLWI5YmMtYjUzNGQ0NWRlYzhiBjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMZ3BlYTU4MAY7CFQ6EnJlc3VsdHNfY291bnRpAg0D--2a7ec57589c2bd529d798b5503190b3d745d0955)  
[RH - Linha Protheus - GPE - Como parametrizar o Lançamento Fixo de uma verba](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwggqmXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODk0MDgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1wYXJhbWV0cml6YXItby1MYW4lQzMlQTdhbWVudG8tRml4by1kZS11bWEtdmVyYmEGOwhUOg5zZWFyY2hfaWRJIiljNWM2N2I0Yy1jMDMwLTRhZWUtOTYwMS04YTk4OWJhNzRmZjIGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVsYW7Dp2FtZW50byBmaXhvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--09b2cbb22237cf5d86fd47622e923663520af876)  
[RH - Linha Protheus - GPE - Como efetuar os lançamentos Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwivfhbSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNjk3NTE1MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW9zLWxhbiVDMyVBN2FtZW50b3MtRnV0dXJvcwY7CFQ6DnNlYXJjaF9pZEkiKTg2ZmVjOGFjLTEyY2MtNGIxOS1hNWU1LTUzM2UwYzAwY2NkZAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiI2xhbsOnYW1lbnRvIGRlIHZhbG9yZXMgZnV0dXJvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--cd246846d6f95d5c379ce04f6e6eedc638418a38)  
[RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiQShDSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNjU2ODU5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb250cm9sYXItYXMtbW92aW1lbnRhJUMzJUE3JUMzJUI1ZXMtZGUtTGFuJUMzJUE3YW1lbnRvcy1WYWxvcmVzLUZ1dHVyb3MGOwhUOg5zZWFyY2hfaWRJIik4NmZlYzhhYy0xMmNjLTRiMTktYTVlNS01MzNlMGMwMGNjZGQGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiNsYW7Dp2FtZW50byBkZSB2YWxvcmVzIGZ1dHVyb3MGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--87195cf590f1ac7c1f65b4b800d8aaa6d3cc5ea0)  
[RH - Linha Protheus - GPE - Como realizar lançamentos na rotina Lançamentos por Verba](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXnh8dxwc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg1NTE3Njg0OTc4MTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tcmVhbGl6YXItbGFuJUMzJUE3YW1lbnRvcy1uYS1yb3RpbmEtTGFuJUMzJUE3YW1lbnRvcy1wb3ItVmVyYmEGOwhUOg5zZWFyY2hfaWRJIiliMzFjMDMxYi0wMzg0LTRlMDMtOWQ5OC03MmU3NTc3ZDYxMjcGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlxSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyByZWFsaXphciBsYW7Dp2FtZW50b3MgbmEgcm90aW5hIExhbsOnYW1lbnRvcyBwb3IgVmVyYmEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--f995fbb59e201ff0fd66c811f42e696ca46aa5b4)
