---
article_id: 360051924833
category: RH - Definições de Cálculo
content_hash: ecbfefad9a03b079130f78eacfbb208cc689b667c50a5352d6396c60e39f327b
fetched_at: '2026-06-28T22:43:22.534782+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Qual a função do cadastro de processos
type: support-article
updated_at: '2025-09-30T17:38:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051924833-RH-Linha-Protheus-GPE-Qual-a-fun%C3%A7%C3%A3o-do-cadastro-de-processos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Qual a função do cadastro de processos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

![](https://tdn.totvs.com/download/attachments/240299561/image2016-6-21%2014%3A7%3A58.png?version=1&modificationDate=1466525427000&api=v2)

A chave para qualquer cálculo e lançamento na versão 12 é: **Processo + Período + Número de Pagamento + Roteiro.**

**O processo** serve como agrupador de funcionários no momento dos cálculos. Os funcionários são agrupados de acordo com o tipo de cálculo que possuem, por exemplo, celetistas mensalistas são agrupados em processo diferente dos celetistas semanalistas.

**Os períodos** são o espaço de tempo que o cálculo deve abranger para o processamento. Seu código é constituído por ano e mês.

[Por exemplo, para realizar o cálculo de funcionários mensalistas no mês de janeiro/2015 é necessário cadastrar um período iniciado em 01/01/2015 a 31/01/2015. O código do período será 201501]

O número de pagamento viabiliza a divisão do período em diversos intervalos de pagamento. Utilizado, por exemplo, para pagamento de semanalistas (4 pagamentos em um mesmo mês).

**O roteiro** indica qual cálculo será realizado, exemplo: FOL, FER, PLA.

O sistema traz, por padrão, esses quatro processos já cadastrados. Porém, se desejar, é possível cadastrar qualquer processo. (Como na imagem acima existe um processo com a legenda verde, que indica a criação pelo usuário).

**Saiba mais:**[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj9hsnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjI2MjY1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW8tY2FkYXN0cm8tZGUtcGVyJUMzJUFEb2RvBjsIVDoOc2VhcmNoX2lkSSIpYjgwNDc3NmItMTY3Ny00N2VmLWJkY2QtODg4YTgxMTM4NWE0BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIhcHJvdGhldXMgY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--477e472010555c017bb3e970170455113d138888)  
[RH - Linha Protheus - GPE - Tabelas utilizadas para o Cadastro de Período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXxuXhqQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg0MjYyMjA3OTk1MTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVRhYmVsYXMtdXRpbGl6YWRhcy1wYXJhLW8tQ2FkYXN0cm8tZGUtUGVyJUMzJUFEb2RvLUdQRUE0MDAGOwhUOg5zZWFyY2hfaWRJIiliODA0Nzc2Yi0xNjc3LTQ3ZWYtYmRjZC04ODhhODExMzg1YTQGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiFwcm90aGV1cyBjYWRhc3RybyBkZSBwZXJpb2RvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--041f3e1c63c434dbb7fb1530b0027598f74a08b4)  
[RH - Linha Protheus - GPE - Como excluir um período aberto indevidamente](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjB5krVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MDc0MTMxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1leGNsdWlyLXVtLXBlciVDMyVBRG9kby1hYmVydG8taW5kZXZpZGFtZW50ZS0GOwhUOg5zZWFyY2hfaWRJIillMzFjOGIzYi03ZDBmLTQ5NzUtOWU3OS1mOTIzODY1MjRiMDgGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiFwcm90aGV1cyBjYWRhc3RybyBkZSBwZXJpb2RvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--4a2937cae48e94f57927667e9a6540a5433cc16a)  
[RH - Linha Protheus - GPE - Como transferir o trabalhador de processo de folha no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjRnWbUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NTc4MDQzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby10cmFuc2ZlcmlyLW8tdHJhYmFsaGFkb3ItZGUtcHJvY2Vzc28tZGUtZm9saGEtbm8tc2lzdGVtYQY7CFQ6DnNlYXJjaF9pZEkiKWY1OGQ4NTQzLWMzOTEtNGIxNy04MzY5LWUyYTA4ZDE5M2QwNAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiXlJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIHRyYW5zZmVyaXIgbyB0cmFiYWxoYWRvciBkZSBwcm9jZXNzbyBkZSBmb2xoYSBubyBzaXN0ZW1hBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--dd41d7cdf5c0c8bebad63081e1df247eb2ceb2fd)
