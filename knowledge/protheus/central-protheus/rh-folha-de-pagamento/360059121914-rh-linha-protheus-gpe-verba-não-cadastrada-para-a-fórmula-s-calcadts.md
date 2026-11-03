---
article_id: 360059121914
category: RH - Folha de Pagamento
content_hash: 90481ce5c8a3d4a61181fc72725998df1a16cb3dad50fa0cd496dde92f374ec6
fetched_at: '2026-06-28T22:44:16.422882+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Verba não cadastrada para a fórmula S_CALCADTS
type: support-article
updated_at: '2024-09-11T18:56:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059121914-RH-Linha-Protheus-GPE-Verba-n%C3%A3o-cadastrada-para-a-f%C3%B3rmula-S-CALCADTS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26305555674519) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Ao tentar fazer algum cálculo no Gestão de Pessoal, é gerado *log* de ocorrências com a mensagem de verba não cadastrada para a fórmula S\_CALCADTS  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - À partir da versão 12.1.25

**Causa**Esse incidente ocorre pois está faltando algum identificador de cálculo no cadastro de verbas, e que são relacionados ao adicional por tempo de serviço.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Acesse Atualizações - Definições de Cálculo - Verbas;  
**2.** Verifique se os identificadores de Cálculo abaixo, estão cadastrados:  
1288 - ATS 13. Salário  
1296 - ATS Férias Mês  
1438 - ATS 13. Salário Maternidade  
1630 - ATS 13. Salário 1ª Parc.  
1641 - ATS 13. Salário Maternidade 1ª Parc.  
  
**3.** Caso não tenha algum destes cadastrado, faça o cadastro para que não ocorra mais a mensagem.  
**OBS: Caso tenha a SRV exclusiva, deve ter as verbas cadastradas para todas as filiais.**

**Exemplos para cadastro**

1288 - ATS 13. Salário

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10069360091415)  
1296 - ATS Férias Mês

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10069407212695)  
1438 - ATS 13. Salário Maternidade

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10069444056599)  
1630 - ATS 13. Salário 1ª Parc.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10069475328151)  
1641 - ATS 13. Salário Maternidade 1ª Parc.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10069477039767)

**Para saber mais**

[RH - Linha Protheus - GPE - Como parametrizar o sistema para que o cálculo do Adicional por Tempo de Serviço (ATS) seja sobre salário base mais verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwht9Pc%2BXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB5Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDAwMjM2NjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tcGFyYW1ldHJpemFyLW8tc2lzdGVtYS1wYXJhLXF1ZS1vLWMlQzMlQTFsY3Vsby1kby1BZGljaW9uYWwtcG9yLVRlbXBvLWRlLVNlcnZpJUMzJUE3by1BVFMtc2VqYS1zb2JyZS1zYWwlQzMlQTFyaW8tYmFzZS1tYWlzLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKWQ3MWFhNTc5LTY0ZWQtNDNjMy05MjliLTViODgzYjZkZmEzMAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiJlJIIC0gTElOSEEgUFJPVEhFVVMgIC0gR1BFICAtIEFUUwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--30c9051e5e93de645f0834ad90da03b8128da71a)

[RH - Linha Protheus - GPE - Como o sistema efetua o cálculo do adicional por tempo de serviço (ATS) sobre as verbas indenizatórias quando a base de cálculo é salário + verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi%2B1nk%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSICCQFodHRwczovL2NlbnRyYWxkZWF0ZW5kaW1lbnRvLnRvdHZzLmNvbS9oYy9wdC1ici9hcnRpY2xlcy8xNTAwMDA4NTM1NzQyLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLW8tc2lzdGVtYS1lZmV0dWEtby1jJUMzJUExbGN1bG8tZG8tYWRpY2lvbmFsLXBvci10ZW1wby1kZS1zZXJ2aSVDMyVBN28tQVRTLXNvYnJlLWFzLXZlcmJhcy1pbmRlbml6YXQlQzMlQjNyaWFzLXF1YW5kby1hLWJhc2UtZGUtYyVDMyVBMWxjdWxvLSVDMyVBOS1zYWwlQzMlQTFyaW8tdmVyYmFzBjsIVDoOc2VhcmNoX2lkSSIpZDcxYWE1NzktNjRlZC00M2MzLTkyOWItNWI4ODNiNmRmYTMwBjsIRjoJcmFua2kOOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSImUkggLSBMSU5IQSBQUk9USEVVUyAgLSBHUEUgIC0gQVRTBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--d1bf646ad8b21ba7f19fafcb5cbb19858d68f2d7)
