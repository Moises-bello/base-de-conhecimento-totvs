---
article_id: 115010081347
category: RH - Benefícios
content_hash: c1e1715251feaa5f87d571e5aeb99e788d2ed28afe32ce5c26635ba88b093529
fetched_at: '2026-06-28T22:44:04.858114+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o parâmetro MV_TPCALEN
type: support-article
updated_at: '2025-09-25T11:25:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010081347-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-TPCALEN
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32986600043927) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**  
Como configurar o parâmetro MV\_TPCALEN?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões **Solução**  
O parâmetro **MV\_TPCALEN** indica o tipo de edição para o calendário do período. O valor padrão é 1 que indica calendário analítico ou 2 calendário sintético.  
  
Quando este parâmetro está com **conteúdo 1** o sistema monta o calendário de períodos do mês (dia a dia) para que se possa efetuar ajuste do tipo do dia (trabalhado, não trabalhado, dsr) ou se determinado dia terá ou não desconto de VT/VR.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10760855865495)

Quando este parâmetro está com **conteúdo 2** o sistema não monta calendário de períodos. Existem clientes que não utilizam nossa rotina de beneficio sendo que o calendário de períodos influencia somente no calculo de benefícios.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10760574728727)  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj9hsnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjI2MjY1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW8tY2FkYXN0cm8tZGUtcGVyJUMzJUFEb2RvBjsIVDoOc2VhcmNoX2lkSSIpNjMyMzY5NGItNzRkZi00MzdjLTgwOWItZTA3MmE0M2QwMWJlBjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--817d1aed5c7a55b7f2b5ffe1650adbed0b5132c3)  
[RH - Linha Protheus - GPE - Parâmetros utilizados para o cadastro de período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX6TKcqQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg0MjUwNTE0NDk3NTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVBhciVDMyVBMm1ldHJvcy11dGlsaXphZG9zLXBhcmEtby1jYWRhc3Ryby1kZS1wZXIlQzMlQURvZG8tR1BFQTQwMAY7CFQ6DnNlYXJjaF9pZEkiKTYzMjM2OTRiLTc0ZGYtNDM3Yy04MDliLWUwNzJhNDNkMDFiZQY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGGNhZGFzdHJvIGRlIHBlcmlvZG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--7d10662f047bf9bbe09994689a070c953f61a123)  
[RH - Linha Protheus - GPE - Tabelas utilizadas para o Cadastro de Período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXxuXhqQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg0MjYyMjA3OTk1MTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVRhYmVsYXMtdXRpbGl6YWRhcy1wYXJhLW8tQ2FkYXN0cm8tZGUtUGVyJUMzJUFEb2RvLUdQRUE0MDAGOwhUOg5zZWFyY2hfaWRJIik2MzIzNjk0Yi03NGRmLTQzN2MtODA5Yi1lMDcyYTQzZDAxYmUGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjYWRhc3RybyBkZSBwZXJpb2RvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--f391000e45286dd519ae0abd12e548e49aeffe9a)  
[RH - Linha Protheus - GPE - Como configurar o compartilhamento das tabelas do Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgcWbbSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ1MTI5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLW8tY29tcGFydGlsaGFtZW50by1kYXMtdGFiZWxhcy1kby1DYWRhc3Ryby1kZS1QZXIlQzMlQURvZG9zBjsIVDoOc2VhcmNoX2lkSSIpY2RmNmJhMDctNWQ4MS00YzI0LWE3NjEtMjdkMTk4NDQwMmY4BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--4b1c22d68a2344d7e02bd2fa58853357d88c5ccd)  
[RH - Linha Protheus - GPE - Como configurar bloqueio de período na rotina GPEA400 - Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgFNdzUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzQ4Njg1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLWJsb3F1ZWlvLWRlLXBlciVDMyVBRG9kby1uYS1yb3RpbmEtR1BFQTQwMC1DYWRhc3Ryby1kZS1QZXIlQzMlQURvZG9zBjsIVDoOc2VhcmNoX2lkSSIpNjMyMzY5NGItNzRkZi00MzdjLTgwOWItZTA3MmE0M2QwMWJlBjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9kbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--63603d22698d2a8c6eab93eba5058a3fae04e722)
