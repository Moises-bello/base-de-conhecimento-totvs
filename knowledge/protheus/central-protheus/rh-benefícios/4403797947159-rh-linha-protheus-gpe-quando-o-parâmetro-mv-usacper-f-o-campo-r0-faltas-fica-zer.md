---
article_id: 4403797947159
category: RH - Benefícios
content_hash: d41746dd8ec022243a8ba40b1c2b5473aa1bff5dc85baf786293d2fe67e8e003
fetched_at: '2026-06-28T22:44:04.756480+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Quando o parâmetro MV_USACPER = .F. o campo R0_FALTAS
  fica zerado
type: support-article
updated_at: '2025-09-04T19:05:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403797947159-RH-Linha-Protheus-GPE-Quando-o-par%C3%A2metro-MV-USACPER-F-o-campo-R0-FALTAS-fica-zerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15508567579543) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Por que quando o parâmetro MV\_USACPER = .F. o campo R0\_FALTAS fica zerado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O Sistema faz a verificação em locais diferentes, dependendo do conteúdo do parâmetro **MV\_USACPER**.  
  
Quando o parâmetro está com **MV\_USACPER = .F.** a verificação é feita no módulo **SIGAPON** e não na Folha - **SIGAGPE**, logo o campo R0\_FALTA na rotina Atualização (GPEA133), **não apresenta conteúdo com as faltas.**  
  
Quando o parâmetro está com **MV\_USACPER = .T.** o sistema olha o cadastro de calendário do **SIGAGPE**, inserido na rotina Períodos (**GPEA400**), e apresenta as faltas no campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15508070915607)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como abater as Faltas no cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhoRV%2FTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODUyMTgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1hYmF0ZXItYXMtRmFsdGFzLW5vLWMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MtBjsIVDoOc2VhcmNoX2lkSSIpZjA1OTgyMDctOTI1Yi00MGI0LWIzYzMtZDdlODE4NzhjNzU0BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPTVZfVVNBQ1BFUgY7CFQ6EnJlc3VsdHNfY291bnRpAmME--f44145d64afa878a7be900ff3aa8a2d202a162f6)  
[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_USACPER para o calculo dos benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgOJxnVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzQ4MDk3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1kby1wYXIlQzMlQTJtZXRyby1NVi1VU0FDUEVSLXBhcmEtby1jYWxjdWxvLWRvcy1iZW5lZiVDMyVBRGNpb3MGOwhUOg5zZWFyY2hfaWRJIilmMDU5ODIwNy05MjViLTQwYjQtYjNjMy1kN2U4MTg3OGM3NTQGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg9NVl9VU0FDUEVSBjsIVDoScmVzdWx0c19jb3VudGkCYwQ%3D--4d581201171d9504fb5cd1e01fbf29a2db29fcef)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKWYwNTk4MjA3LTkyNWItNDBiNC1iM2MzLWQ3ZTgxODc4Yzc1NAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX1VTQUNQRVIGOwhUOhJyZXN1bHRzX2NvdW50aQJjBA%3D%3D--d27c6fcb527325af7a5099de4c4d49866b80057d)
