---
article_id: 360050786394
category: RH - Relatórios Cadastros/Funcionários
content_hash: 6fa7e569d5b15b332d6ae9fcb67791786a44a6b6f9c7a3e34082757c651c9f59
fetched_at: '2026-06-28T22:43:18.375018+00:00'
product: protheus
section_id: 360010843654
source: central-protheus
title: RH - Linha Protheus - GPE - Como emitir um relatório por verba
type: support-article
updated_at: '2025-07-24T17:27:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050786394-RH-Linha-Protheus-GPE-Como-emitir-um-relat%C3%B3rio-por-verba
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16610481255447) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como emitir um relatório por verba?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Após a **rotina GPER100** (Relatório da Folha por Verba) **ter sido descontinuada na versão 12**, temos as seguintes opções de geração de relatório por verba: 

1. Buscar as verbas na tabela SRC (lançamentos após calculo da folha) e SRD (período fechado):  
  
**GPER102** **-** Relatório Por Período Vertical  
[RH - Linha Protheus - GPE - Como emitir o Relatório de Lançamentos Por Período Vertical - GPER102](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi2Ys3TUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzNTczODI5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lbWl0aXItby1SZWxhdCVDMyVCM3Jpby1kZS1MYW4lQzMlQTdhbWVudG9zLVBvci1QZXIlQzMlQURvZG8tVmVydGljYWwtR1BFUjEwMgY7CFQ6DnNlYXJjaF9pZEkiKWFlMTJkNjY4LTYxZjMtNDljMC04MDdmLWVkMWNjZWNjNTFmNQY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDEdQRVIxMDIGOwhUOhJyZXN1bHRzX2NvdW50aQHf--3b9b408a066507df83310a1ef91bbcc5f52bb8bd)  
  
**GPER103 -** Relatório Por Período Horizontal  
[RH - Linha Protheus - GPE - Relatório Valores por Verba no Período horizontal (GPER103) em planilha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgaEtLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjgyMjU1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tVmFsb3Jlcy1wb3ItVmVyYmEtbm8tUGVyJUMzJUFEb2RvLWhvcml6b250YWwtR1BFUjEwMy1lbS1wbGFuaWxoYS0GOwhUOg5zZWFyY2hfaWRJIiliMGY5MWIwOC0zZDU4LTQ3NDEtODFhYS0yYzQwZjViODlhZWMGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVSMTAzBjsIVDoScmVzdWx0c19jb3VudGkB7A%3D%3D--936c501a8771f4fe3a5e1c8e6ec5a47fb446f828)  
2. Busca tabela RGB (lançamentos por funcionário -  pode ser utilizado antes do cálculo da folha):  
  
**GPER104 -** Relatório Lançamentos Vertical  
[RH - Linha Protheus - GPE - Relatório lançamentos vertical GPER104](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgeGNLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjgyNDA5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tbGFuJUMzJUE3YW1lbnRvcy12ZXJ0aWNhbC1HUEVSMTA0BjsIVDoOc2VhcmNoX2lkSSIpM2RlNmVlMzItYzc3MC00MDNjLTg5YjctNDliYjhlNTJjYzdiBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjEwNAY7CFQ6EnJlc3VsdHNfY291bnRpAdM%3D--032a04cfb09714211dbc409c92ae078142bfd2d5)  
  
**GPER105 -** Relatório Lançamento Horizontal   
[Lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=451272539) [Horizontal (GPER105 - SIGAGPE - V12)](https://tdn.totvs.com/pages/viewpage.action?pageId=451272539)

**Saiba Mais:**[RH - Linha Protheus - GPE - Quais relatórios de férias são gerados em planilha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiZEdrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzM0NjcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtcmVsYXQlQzMlQjNyaW9zLWRlLWYlQzMlQTlyaWFzLXMlQzMlQTNvLWdlcmFkb3MtZW0tcGxhbmlsaGEGOwhUOg5zZWFyY2hfaWRJIik3Y2IzNGNhNi05OGE5LTRjNTAtOTVjZC1kNjNhYzVhNGM3MzUGOwhGOglyYW5raQo6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxHUEVSMTA1BjsIVDoScmVzdWx0c19jb3VudGkBxQ%3D%3D--7e3ad3d336db76822a43154538a187e280e7a7a6)  
[RH - Linha Protheus - GPE - Quais relatórios de Lançamentos são gerados em formato planilha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjdHNvUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzQxNTEzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtcmVsYXQlQzMlQjNyaW9zLWRlLUxhbiVDMyVBN2FtZW50b3MtcyVDMyVBM28tZ2VyYWRvcy1lbS1mb3JtYXRvLXBsYW5pbGhhBjsIVDoOc2VhcmNoX2lkSSIpN2NiMzRjYTYtOThhOS00YzUwLTk1Y2QtZDYzYWM1YTRjNzM1BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMR1BFUjEwNQY7CFQ6EnJlc3VsdHNfY291bnRpAcU%3D--7182c31cbcf91055370da8ab31d52409bd9392e0)  
[RH - Linha Protheus - GPE - Quais relatórios demonstram os valores da folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXlpiMLQk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwMDkxMjM2OTg4NTY3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1yZWxhdCVDMyVCM3Jpb3MtZGVtb25zdHJhbS1vcy12YWxvcmVzLWRhLWZvbGhhLWRlLXBhZ2FtZW50bwY7CFQ6DnNlYXJjaF9pZEkiKTdjYjM0Y2E2LTk4YTktNGM1MC05NWNkLWQ2M2FjNWE0YzczNQY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDEdQRVIxMDUGOwhUOhJyZXN1bHRzX2NvdW50aQHF--d6dcaf6ca6fef82ad1df8add75c7577aff15b33e)  
[RH - Linha Protheus - GPE - Padronização e conversão de Rdmakes para fonte padrão a partir da versão 12.1.33](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXf1oG7Qg6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzk4MTQxMDY4NjU0MzEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVBhZHJvbml6YSVDMyVBNyVDMyVBM28tZS1jb252ZXJzJUMzJUEzby1kZS1SZG1ha2VzLXBhcmEtZm9udGUtcGFkciVDMyVBM28tYS1wYXJ0aXItZGEtdmVycyVDMyVBM28tMTItMS0zMwY7CFQ6DnNlYXJjaF9pZEkiKTdjYjM0Y2E2LTk4YTktNGM1MC05NWNkLWQ2M2FjNWE0YzczNQY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDEdQRVIxMDUGOwhUOhJyZXN1bHRzX2NvdW50aQHF--40f976bd206bb760363b061e4f1a4f685ae991eb)
