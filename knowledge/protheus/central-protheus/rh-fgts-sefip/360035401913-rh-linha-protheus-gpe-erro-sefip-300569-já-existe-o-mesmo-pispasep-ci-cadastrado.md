---
article_id: 360035401913
category: RH - FGTS / SEFIP
content_hash: c7f7dff4fea2c2d1760ea1203a9590ce8e64d1967c41fc290c4c45ca2742704e
fetched_at: '2026-06-28T22:43:41.290385+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro Sefip 300569 - Já existe o mesmo PIS/PASEP/
  CI cadastrado com o código de ocorrência que não permite múltiplos vínculos.
type: support-article
updated_at: '2025-08-07T13:30:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035401913-RH-Linha-Protheus-GPE-Erro-Sefip-300569-J%C3%A1-existe-o-mesmo-PIS-PASEP-CI-cadastrado-com-o-c%C3%B3digo-de-ocorr%C3%AAncia-que-n%C3%A3o-permite-m%C3%BAltiplos-v%C3%ADnculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34012618936343) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Erro SEFIP 300569- Já existe o mesmo PIS/PASEP/ CI cadastrado com o código de ocorrência que não permite múltiplos vínculos.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.

**Causa**

O erro é apresentado quando o menor aprendiz é desligado e readmitido como CLT no mesmo mês e o Validador da Caixa não aceita duas vezes o mesmo PIS sem a multiplicidade de vínculos.

**Solução**

**1**. No cadastro de funcionário, preencha o código de Múltiplos Vínculos no campo ocorrência (aba funcionais) para as duas matriculas (ativa e desligada),

**Importante:**Como trata-se de um campo em que o sistema grava histórico de alterações na tabela SR9, é necessário que no momento da alteração do campo a **data base do sistema esteja com a mesma data da competência da geração da SEFIP**, **caso contrário irá gravar uma data futura e não será considerada a ocorrência para geração**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10468573890071)

Este processo deve ser feito **somente no primeiro mês**, nos próximos meses como existirá somente um vínculo, deve retirar a informação de múltiplos vínculos de ambas as matrículas.

**2**. Para o caso em que ambas as matrículas estão com a ocorrência de Múltiplos Vínculos, verificar na rotina Histórico Manutenção Hist. Funcionário, através do caminho **Atualização / Funcionários / Manutenção Hist. Funcionário**, nas duas matriculas, a coluna Campo Alt. com o conteúdo "RA\_OCORRENCIA", coluna Descrição "05", na coluna Dt. Alteração deve estar com a data do período que está gerando a Sefip.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14229006508183)

No Exemplo acima, o menor aprendiz foi demitido e readmitido no mês 04/2023, a Descrição das duas matriculas deverão estar = 05 para o campo RA\_OCORREN, e o campo Dt. Alteração com a data da competência em que o SEFIP está sendo gerado.

Caso esteja uma data diferente da competência do SEFIP efetuar a alteração da data através desta rotina.

**OBS:** Caso não possua esta rotina no menu, efetue o procedimento conforme o link abaixo:

[RH - Linha Protheus - GPE - Como realizar manutenção no histórico de alterações do cadastro de funcionários (tabela SR9)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXB2IUwQk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB12h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwNzI0ODc1MzA2Nzc1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLXJlYWxpemFyLW1hbnV0ZW4lQzMlQTclQzMlQTNvLW5vLWhpc3QlQzMlQjNyaWNvLWRlLWFsdGVyYSVDMyVBNyVDMyVCNWVzLWRvLWNhZGFzdHJvLWRlLWZ1bmNpb24lQzMlQTFyaW9zLXRhYmVsYS1TUjktBjsIVDoOc2VhcmNoX2lkSSIpODA5YTQyMWQtYWM1My00MTNhLThhYTktMjljNDg4NjhjODBkBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBflJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIHJlYWxpemFyIG1hbnV0ZW7Dp8OjbyBubyBoaXN0w7NyaWNvIGRlIGFsdGVyYcOnw7VlcyBkbyBjYWRhc3RybyBkZSBmdW5jaW9uw6FyaW9zICh0YWJlbGEgU1I5KQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--7f22d5ee15e8e0850ed4c8d894d6b50efc3e2f74)

**Saiba Mais:**

[RH - Linha Protheus - GPE - SEFIP Múltiplos Vínculos, como configurar](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgbn2DTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODYxMDMzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtU0VGSVAtTSVDMyVCQWx0aXBsb3MtViVDMyVBRG5jdWxvcy1jb21vLWNvbmZpZ3VyYXIGOwhUOg5zZWFyY2hfaWRJIiliODczNDU5Yi02ZWI0LTRiOWUtYWZiNS1mMjM2ZmZjMGZkZDIGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg5HUEUgc2VmaXAGOwhUOhJyZXN1bHRzX2NvdW50aQI7BA%3D%3D--bfd4f39142640c20f09620015b52e47f41299315)  
[RH - Linha Protheus - GPE - Erro SEFIP 100091 - Código Outras Entidades Inválido.](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwga%2Bx%2FVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzkyODQ3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRXJyby1TRUZJUC0xMDAwOTEtQyVDMyVCM2RpZ28tT3V0cmFzLUVudGlkYWRlcy1JbnYlQzMlQTFsaWRvLQY7CFQ6DnNlYXJjaF9pZEkiKWI4NzM0NTliLTZlYjQtNGI5ZS1hZmI1LWYyMzZmZmMwZmRkMgY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDkdQRSBzZWZpcAY7CFQ6EnJlc3VsdHNfY291bnRpAjsE--275e2315463c1314ab127c43d69acbb62eaa5e51)  
[RH - Linha Protheus - GPE - SEFIP Erro 130391 Código de Identificação da Empresa na Caixa inválido](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhN%2FPDTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzODA3MTM3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtU0VGSVAtRXJyby0xMzAzOTEtQyVDMyVCM2RpZ28tZGUtSWRlbnRpZmljYSVDMyVBNyVDMyVBM28tZGEtRW1wcmVzYS1uYS1DYWl4YS1pbnYlQzMlQTFsaWRvBjsIVDoOc2VhcmNoX2lkSSIpYjg3MzQ1OWItNmViNC00YjllLWFmYjUtZjIzNmZmYzBmZGQyBjsIRjoJcmFua2kLOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIOR1BFIHNlZmlwBjsIVDoScmVzdWx0c19jb3VudGkCOwQ%3D--a906434200745a4f8a2d1a4a4dfa017a82a8e7ac)  
[RH - Linha Protheus - GPE - Erro Sefip quando funcionário tem CTPS digital - 130389 - Série CTPS Inválida](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXsy2mhgg6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzkzNzQ0MDY2NTI2OTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUVycm8tU2VmaXAtcXVhbmRvLWZ1bmNpb24lQzMlQTFyaW8tdGVtLUNUUFMtZGlnaXRhbC0xMzAzODktUyVDMyVBOXJpZS1DVFBTLUludiVDMyVBMWxpZGEGOwhUOg5zZWFyY2hfaWRJIiliODczNDU5Yi02ZWI0LTRiOWUtYWZiNS1mMjM2ZmZjMGZkZDIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg5HUEUgc2VmaXAGOwhUOhJyZXN1bHRzX2NvdW50aQI7BA%3D%3D--3c9a86ca4153c34f8362d7782aca9473b48e0750)

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
