---
article_id: 4415767203863
category: RH - 13º salário
content_hash: 75ed634969b03e65542a356cded0a3a967467ab1f28a2c6854866acad9190512
fetched_at: '2026-06-28T22:44:00.857862+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Não está pagando o avo de 13° referente ao mês
  de Fevereiro
type: support-article
updated_at: '2025-08-15T18:00:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415767203863-RH-Linha-Protheus-GPE-N%C3%A3o-est%C3%A1-pagando-o-avo-de-13-referente-ao-m%C3%AAs-de-Fevereiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18696932936855) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**O que analisar quando no cálculo do 13º salário não está sendo considerado o avo de Fevereiro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o funcionário tenha direito ao avo do mês, é necessário que o funcionário tenha no mínimo 15 dias trabalhados no mês.  
É necessário verificar a data de admissão do funcionário e considerando a admissão, faça a contagem até o último dia do mês de fevereiro (28 ou 29 dias conforme o ano), e se der menos de 15 dias, está correto o comportamento do Protheus pois o funcionário perde direito à este avo de 13º salário.  
  
Utilizando como exemplo um funcionário admitido em 15/02 para um mês de Fevereiro que contém 28 dias, contando do dia 15 ao dia 28/02, tem 14 dias de trabalho, logo, não tem direito a este avo realmente.   
A mesma validação deverá ser realizada para os funcionários que ficaram afastados na competência de fevereiro. Se houver menos de 15 dias trabalhados, o funcionário também perderá direito ao avo de 13º salário.

**Importante:** Há um tratamento para que em Fevereiro, seja considerado 30 dias para pagamento de Folha (Roteiro FOL), através do mnemônico P\_PGSALFEV , porém os roteiros 131 e 132 são  tratados de forma diferente, pois deve-se contar realmente os dias trabalhados de forma efetiva, assim, como explicado acima, só será pago se tiver 15 dias trabalhados, considerando 28/29 dias no mês de Fevereiro.

**Saiba Mais:**

Consultoria:<https://tdn.totvs.com/pages/viewpage.action?pageId=631324291>  
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)   
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>**  
[RH - Linha Protheus - GPE - 13º Parcela Única](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiisxbVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ8aHR0cHM6Ly9jZW50cmFsZGVhdGVuZGltZW50by50b3R2cy5jb20vaGMvcHQtYnIvYXJ0aWNsZXMvMzYwMDU3MzIwMzU0LVJILUxpbmhhLVByb3RoZXVzLUdQRS0xMyVDMiVCQS1QYXJjZWxhLSVDMyU5QW5pY2EGOwhUOg5zZWFyY2hfaWRJIik0MTY0OWQ0Zi03ZjA1LTRmYTEtYjIwYy0zZTA5NWM4NTY3ZTEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIjRSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gMTPCuiBQYXJjZWxhIMOabmljYQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--d1c352893e9be27529a7ea0abf0a213cdbe14132)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXpNm%2FAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4NTUxNTczOTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZGEtMSVDMiVBQS1wYXJjZWxhLWRvLTEzLVNhbCVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKTZjNDI4YTE5LWNhM2QtNDg4OC04OWM2LWZlNTA3NzUxMDMzYwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkid1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFpcyBzw6NvIGFzIGRvY3VtZW50YcOnw7VlcyByZWxhY2lvbmFkYXMgYW8gY8OhbGN1bG8gZGEgMcKqIHBhcmNlbGEgZG8gMTPCsCBTYWzDoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAhcH--532e20772fa9c16de008dcfe8d0c7d1f2d76b212)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do Décimo Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmUm%2BAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4Mjg5NDAwNTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRvcy1hby1jJUMzJUExbGN1bG8tZGEtMiVDMiVBQS1wYXJjZWxhLWRvLUQlQzMlQTljaW1vLVRlcmNlaXJvBjsIVDoOc2VhcmNoX2lkSSIpY2ExNTdjMWYtZDQwYS00MGQ5LWI1NjEtMzEyZTk3MjZkNmFmBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ6UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFF1YWlzIHPDo28gYXMgZG9jdW1lbnRhw6fDtWVzIHJlbGFjaW9uYWRvcyBhbyBjw6FsY3VsbyBkYSAywqogcGFyY2VsYSBkbyBEw6ljaW1vIFRlcmNlaXJvBjsIVDoScmVzdWx0c19jb3VudGkC%2BwY%3D--283eb1da5f7aa76dfea0802755a4f43d8c1c3c2c)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIik1OTIwNjVlMS1hMzNhLTQxNWQtYTk0ZS1mYTZhODkyN2E0MjAGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--e3ca5735775b2e9f7be27040613da71911582897)
