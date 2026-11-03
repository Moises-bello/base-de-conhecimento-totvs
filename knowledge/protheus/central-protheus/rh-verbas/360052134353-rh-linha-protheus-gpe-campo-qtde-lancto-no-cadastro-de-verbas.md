---
article_id: 360052134353
category: 'RH - Verbas '
content_hash: 16a08a7c4ccfecff208368f9f9ceb3f2513ed9efb8766fb4b7f1b47cbb0623bc
fetched_at: '2026-06-28T22:43:19.886222+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Campo "Qtde Lancto" no cadastro de verbas
type: support-article
updated_at: '2025-09-15T19:16:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052134353-RH-Linha-Protheus-GPE-Campo-Qtde-Lancto-no-cadastro-de-verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32737954751895) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como informar o campo "Qtde. Lancto" no cadastro de verbas? **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões **Solução**

O campo está localizado em: **Atualizações > Definições de Cálculo > Verbas**

Deverá ser informado o número de sequências que esta Verba pode ter( Mínimo 1 máximo 9).

-Caso seja informado **0** (Zero) essa verba não poderá ser Lançada no Movimento Mensal  
-Caso seja lançado **1** (Um) será somado os valores daquele evento na folha.  
-Se informado **9** (Nove) será listado a quantidade de vezes que aquele evento foi gerado pelo sistema.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10329757396759)

**Exemplo**Funcionário efetuou 3 dias de horas extras a 100%.  
Se informar **9** irá listar o evento de hora extra 100% 3 vezes e se informar **1** irá listar uma única vez a verba com o somatório dos 3 dias.

**Observação**Verba de Hora Extra: neste caso, quando o campo Lançamento Diário está como Sim, a hora extra poderá ser lançada várias vezes, uma vez para cada data de referência.

**Para saber mais:**

[RH - Linha Protheus - GPE - Funcionalidade do campo RV\_CUSTO no cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXAJVO6gU6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzY1MDM4OTg4NzQwMDctUkgtTGluaGEtUHJvdGhldXMtR1BFLUZ1bmNpb25hbGlkYWRlLWRvLWNhbXBvLVJWLUNVU1RPLW5vLWNhZGFzdHJvLWRlLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKTNjYzgyYzFhLTNlOWEtNGE3MS05OGZhLTg4Nzg3NjU3NDM4MgY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFmNhZGFzdHJvIGRlIHZlcmJhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--206988de5839393f09e7d1c8699848793494adbc)  
[RH - Linha Protheus - GPE - Campo "Percentual" no cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwixosfUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjEzODY3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FtcG8tUGVyY2VudHVhbC1uby1jYWRhc3Ryby1kZS12ZXJiYXMGOwhUOg5zZWFyY2hfaWRJIikzY2M4MmMxYS0zZTlhLTRhNzEtOThmYS04ODc4NzY1NzQzODIGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhZjYWRhc3RybyBkZSB2ZXJiYQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--6aa88e92e3e7965ff011daffe44df9533ff8040e)  
[RH - Linha Protheus - GPE - Como gerar relatório com todo o cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgUPlLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMDg5MDc3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci1yZWxhdCVDMyVCM3Jpby1jb20tdG9kby1vLWNhZGFzdHJvLWRlLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKTNjYzgyYzFhLTNlOWEtNGE3MS05OGZhLTg4Nzg3NjU3NDM4MgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFmNhZGFzdHJvIGRlIHZlcmJhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--36fdcfe9d240b891673f2d827f6f0e336fb1c6f9)  
[RH - Linha Protheus - GPE - Pontos de Entrada da rotina GPEA040 - Cadastro de Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiWlxvVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzY0MDg1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUG9udG9zLWRlLUVudHJhZGEtZGEtcm90aW5hLUdQRUEwNDAtQ2FkYXN0cm8tZGUtVmVyYmFzBjsIVDoOc2VhcmNoX2lkSSIpM2NjODJjMWEtM2U5YS00YTcxLTk4ZmEtODg3ODc2NTc0MzgyBjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIWY2FkYXN0cm8gZGUgdmVyYmEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--f00e68c73c5d23c0fa49877040dea51072f28c00)
