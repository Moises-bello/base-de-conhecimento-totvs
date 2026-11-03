---
article_id: 360017451292
category: RH - Definições de Cálculo
content_hash: 581109b3e59fe26334a712c3bc7795a067fdbf046252ce8da7ceb72e64acb680
fetched_at: '2026-06-28T22:43:22.348511+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o compartilhamento das tabelas
  do Cadastro de Períodos
type: support-article
updated_at: '2025-11-14T11:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017451292-RH-Linha-Protheus-GPE-Como-configurar-o-compartilhamento-das-tabelas-do-Cadastro-de-Per%C3%ADodos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31646496088471)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como configurar o compartilhamento das tabelas do Cadastro de Períodos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o período de cálculo do Gestão de Pessoal seja cadastrado de forma consistente, evitando erros nas rotinas do módulo, é necessário que o **modo de compartilhamento das tabelas que o compõe, esteja idêntico,** por exemplo: totalmente compartilhadas ou exclusivas, compartilhadas apenas por Filial, etc.Para conferência, siga os passos abaixo:  
**1 -** Acessar o **Configurador >** **Base de Dados > Dicionários** e filtrar as tabelas **RCJ, RFQ, RCH, RCG, RCF e RG3**  
**2 -** Confirmar se o **modo de compartilhamento está idêntico para todas**  
**3 -** Se for necessário ajustar o modo de compartilhamento das tabelas, faça *backup* do dicionário e dos dados  
**4 -** Ajustar o modo de compartilhamento e atualizar o dicionário  
  
Abaixo, um exemplo correto de compartilhamento entre as tabelas:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36332940982551)

**Saiba Mais:**[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj9hsnUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjI2MjY1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW8tY2FkYXN0cm8tZGUtcGVyJUMzJUFEb2RvBjsIVDoOc2VhcmNoX2lkSSIpYjQ5NzM5YzEtNzg0ZC00N2EwLWIzZTMtYTllYTkzOGUzMWU4BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIYY2FkYXN0cm8gZGUgcGVyaW9zbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--7f5b206a807af426e92e83bd05dc1f6c52829b7f)  
[RH - Linha Protheus - GPE - Funcionalidade do campo RHC\_STATUS no cadastro de períodos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXPH4hogk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwNTkxOTUxMjczMTExLVJILUxpbmhhLVByb3RoZXVzLUdQRS1GdW5jaW9uYWxpZGFkZS1kby1jYW1wby1SSEMtU1RBVFVTLW5vLWNhZGFzdHJvLWRlLXBlciVDMyVBRG9kb3MGOwhUOg5zZWFyY2hfaWRJIik2MDVjMmI2ZC0yYmVhLTQ3Y2ItYmZlNS1hYjhkOGI3MDg5ZDkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhjYWRhc3RybyBkZSBwZXJpb2RvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--c21b9591b369a86dcd8eca7bd42ae93f42f87af9)  
[RH - Linha Protheus - GPE - Parâmetros utilizados para o cadastro de período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX6TKcqQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzg0MjUwNTE0NDk3NTEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVBhciVDMyVBMm1ldHJvcy11dGlsaXphZG9zLXBhcmEtby1jYWRhc3Ryby1kZS1wZXIlQzMlQURvZG8tR1BFQTQwMAY7CFQ6DnNlYXJjaF9pZEkiKWI0NDg1MDk4LWYzN2EtNDAzYi05NDlhLTMwOGVmNTg0ZmNiNQY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGGNhZGFzdHJvIGRlIHBlcmlvZG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--678dd5afc1d79d8660a806a5be5197b48e9326d0)
