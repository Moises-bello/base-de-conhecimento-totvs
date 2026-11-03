---
article_id: 360057480974
category: RH - Benefícios
content_hash: 0848d04b5f2f53dc80e54f06390525d1349bbb6c02de52a2d79f9c946bc60fd0
fetched_at: '2026-06-28T22:44:03.881604+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração do parâmetro MV_USACPER para o calculo
  dos benefícios
type: support-article
updated_at: '2025-09-03T19:39:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057480974-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-USACPER-para-o-calculo-dos-benef%C3%ADcios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15469449054103) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como realizar a configuração do parâmetro **MV\_USACPER** para o calculo dos benefícios?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**Acesse o módulo Configurador em **Base de Dados/ Dicionário/ Base de Dados**, selecionar a opção **Parâmetros** e procure por **MV\_USACPER:****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099749173)**

O parâmetro indicará se para o cálculo dos benefícios utilizará o calendário do **Períodos (SIGAGPE)** ou a **Escala do ponto (SIGAPON)**. Para a configuração deve ser preenchido o parâmetro com uma das duas opções:

* Quando preenchido com **.T.**: o sistema utilizará com busca o **Período da folha**;
* Quando preenchido com **.F.**: o sistema usa a **Escala do funcionário.**

**Importante:** Se o MV\_USACPER for configurado com .F. será verificado a escala de horário **a partir do primeiro dia do mês do cálculo até o último dia do mês.** Por exemplo, no cálculo de Março 2022, será verificado a escala de horário do Ponto no SIGAPON do dia 01/03/2022 até o dia 31/03/2022. **Não será calculado conforme o período de Ponto.** Caso o funcionário não possua escala de horário, será utilizado o calendário do período do mês de cálculo.

**Saiba mais:**[Verificação da escala de ponto para o cálculo de benefícios](https://tdn.totvs.com/pages/viewpage.action?pageId=221554360)  
[RH - Linha Protheus - GPE - Como abater as Faltas no cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhoRV%2FTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODUyMTgzMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1hYmF0ZXItYXMtRmFsdGFzLW5vLWMlQzMlQTFsY3Vsby1kZS1CZW5lZiVDMyVBRGNpb3MtBjsIVDoOc2VhcmNoX2lkSSIpZGFjYzg2MTYtYWNmZi00NmQ0LWJmNGMtM2MwOGI0ZGIyYjEyBjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPTVZfVVNBQ1BFUgY7CFQ6EnJlc3VsdHNfY291bnRpAmIE--596e4424d01493200ed56199d661838a52f61ea3)  
[RH - Linha Protheus - GPE - Rotinas envolvidas nos cálculos de Benefícios - VR/VA/VT](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjp%2B67UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDUyMzExMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUm90aW5hcy1lbnZvbHZpZGFzLW5vcy1jJUMzJUExbGN1bG9zLWRlLUJlbmVmJUMzJUFEY2lvcy1WUi1WQS1WVAY7CFQ6DnNlYXJjaF9pZEkiKWRhY2M4NjE2LWFjZmYtNDZkNC1iZjRjLTNjMDhiNGRiMmIxMgY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX1VTQUNQRVIGOwhUOhJyZXN1bHRzX2NvdW50aQJiBA%3D%3D--3137c10ce725b9ba76ef866555b181c5d4ee2f5c)  
[RH - Linha Protheus - GPE - Quando o parâmetro MV\_USACPER = .F. o campo R0\_FALTAS fica zerado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX889WAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDM3OTc5NDcxNTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YW5kby1vLXBhciVDMyVBMm1ldHJvLU1WLVVTQUNQRVItRi1vLWNhbXBvLVIwLUZBTFRBUy1maWNhLXplcmFkbwY7CFQ6DnNlYXJjaF9pZEkiKWRhY2M4NjE2LWFjZmYtNDZkNC1iZjRjLTNjMDhiNGRiMmIxMgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX1VTQUNQRVIGOwhUOhJyZXN1bHRzX2NvdW50aQJiBA%3D%3D--df155478dd21692364fe7519d36bf20f40236f16)
