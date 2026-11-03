---
article_id: 1500005088861
category: RH - Tipos de Ausências
content_hash: e0d73aa3e2ab421e55d417dd8d0697c5de3c5b12b71000801f50a9e855020ccd
fetched_at: '2026-06-28T22:43:20.941493+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Campo Verba Sup - RCM_PDSUP bloqueado para edição
type: support-article
updated_at: '2025-07-11T14:29:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005088861-RH-Linha-Protheus-GPE-Campo-Verba-Sup-RCM-PDSUP-bloqueado-para-edi%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Por que o campo **Verba Sup - RCM\_PDSUP** fica bloqueado para edição?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para que seja possível editar o campo **Verba Sup - RCM\_PDSUP** (em amarelo), a verba atrelada no campo anterior **Cód. Verba - RCM\_PD** (em verde), deve ter incidência **Sim** para INSS - RV\_INSS e **Código 11** no campo Cd. Inc. CP - RV\_INCCP na aba E-social, caso algum destes campos esteja com conteúdo diferente, o campo ficará bloqueado.

**Cadastro de Tipo de Ausência:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11653236598295)

**Cadastro Verba:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11654057299095)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11654099171607)

Além disso, o campo deve estar configurado como **Alterar** no configurador:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11654198652951)

**Saiba mais:**[RH - Linha Protheus - GPE - Cadastro tipos de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2FO2nTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBe2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyOTE3NDU5MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tdGlwb3MtZGUtYXVzJUMzJUFBbmNpYQY7CFQ6DnNlYXJjaF9pZEkiKTRmZDk3YmI4LTE1ZWYtNGQ3Yi05MDllLWMwYTdlMWZjNmE3NQY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFXRpcG8gZGUgYXVzZW5jaWEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--a6c65468fe6cb642f1d33f6fb995a310f2ac337b)  
[RH - Linha Protheus - GPE - Como configurar o sistema para afastamento superior a 15 dias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgu8T8%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDQ3NDE0MjItUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY29uZmlndXJhci1vLXNpc3RlbWEtcGFyYS1hZmFzdGFtZW50by1zdXBlcmlvci1hLTE1LWRpYXMGOwhUOg5zZWFyY2hfaWRJIillZjIzN2U0NC1iMDVhLTQ5YjQtOGJkYi1iMzY5NDY1MGIwYjQGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg52ZXJiYSBzdXAGOwhUOhJyZXN1bHRzX2NvdW50aQIyBQ%3D%3D--23e6b4ccf26fa8bec07f6d67f5e5063b5b8d36d2)  
[RH - Linha Protheus - GPE - Campos no cadastro de Tipos de Ausência desabilitados/bloqueados](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXwvXzAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDY0MzQ0NDgwMjMtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNhbXBvcy1uby1jYWRhc3Ryby1kZS1UaXBvcy1kZS1BdXMlQzMlQUFuY2lhLWRlc2FiaWxpdGFkb3MtYmxvcXVlYWRvcwY7CFQ6DnNlYXJjaF9pZEkiKTRmZDk3YmI4LTE1ZWYtNGQ3Yi05MDllLWMwYTdlMWZjNmE3NQY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFXRpcG8gZGUgYXVzZW5jaWEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--a5f564f0de92b3194e5005a989255db59eeee4dd)  
[RH - Linha Protheus - GPE - Como deve ser preenchido o novo campo RCM\_PDSUP (Verba Susp.) no cadastro do tipo de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhC%2BWk%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDc0OTYwMDItUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZGV2ZS1zZXItcHJlZW5jaGlkby1vLW5vdm8tY2FtcG8tUkNNLVBEU1VQLVZlcmJhLVN1c3Atbm8tY2FkYXN0cm8tZG8tdGlwby1kZS1hdXMlQzMlQUFuY2lhBjsIVDoOc2VhcmNoX2lkSSIpN2IwMWUwMDYtNmQxYS00ZjU3LTg3NjAtZmNhMTAzY2IxMTUyBjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVdGlwbyBkZSBhdXNlbmNpYQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--b7dc148b191310327a9733531d41ed86286ad6df)
