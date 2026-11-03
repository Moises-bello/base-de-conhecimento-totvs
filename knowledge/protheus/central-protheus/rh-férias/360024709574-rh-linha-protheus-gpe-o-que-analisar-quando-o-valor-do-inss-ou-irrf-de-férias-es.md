---
article_id: 360024709574
category: RH - Férias
content_hash: 2b55a020711c9bad0fba0a90a5e57b4cf5ac49bd2b38ca3e762c5a7bb4937017
fetched_at: '2026-06-28T22:43:59.373282+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - O que analisar quando o Valor do INSS ou IRRF de
  Férias estão Incorretos
type: support-article
updated_at: '2025-06-03T19:46:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024709574-RH-Linha-Protheus-GPE-O-que-analisar-quando-o-Valor-do-INSS-ou-IRRF-de-F%C3%A9rias-est%C3%A3o-Incorretos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30048204456471) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**O que analisar quando o Valor do INSS ou IRRF de Férias estão Incorretos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução  
1.** Confira se as tabelas **S001 - INSS e S002 - IR**, estão cadastradas corretamente:   
[- Tabela S001 - INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043059473-RH-Linha-Protheus-GPE-Como-cadastrar-ou-atualizar-a-tabela-de-INSS)  
[- Tabela S002 - IR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21864295842327-RH-Linha-Protheus-GPE-Como-cadastrar-ou-alterar-a-tabela-S002-Tabela-Imposto-de-Renda)

**2.** Verifique se as verbas de férias que irão incidir INSS então com o campo **INSS Férias*(*RV\_INSSFER*) =* Sim  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32560370468887)**Caso a verba esteja com o campo destacado acima preenchido com Não, o valor não será considerado para a Base do Desconto de INSS.

**3.** Verifique se as verbas de férias que irão incidir IR estão com o campo **IR (RV\_IR) = Sim  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32560433731351)**

Caso a verba esteja com o campo destacado acima preenchido com Não, o valor não será considerado para a Base do Desconto de Imposto de Renda. 

**4.** Para o cálculo do IR, verifique a incidência de IR das verbas de **id 0065 e 0168**, **apenas uma das verbas** devem ficar com **IR = Sim,** para que o sistema realize a dedução do valor do INSS no modelo completo, caso seja o mais benéfico.  **5.** Ainda para o cálculo do IR, verifique se o funcionário possui dependentes para dedução de IR e caso tenha, verifique se a verba de **id 0060** está com **IR = Sim,** para que o sistema realize a dedução do valor no modelo completo, caso seja o mais benéfico.

**Observação:**As incidências das verbas devem ser definidas mediante interpretação do cliente junto ao seu Jurídico/Contador.

**Saiba Mais:**[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhEGKfSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBj2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjQ1MTY1Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1kby1wYXIlQzMlQTJtZXRyby1NVi1ESU5TU0ZNBjsIVDoOc2VhcmNoX2lkSSIpMmQ4NmI1YzMtNjE0OS00ZmYyLTlkZjYtY2IyZTQyNzMzMDVlBjsIRjoJcmFua2kOOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIaSU5TUyBmw6lyaWFzIHBhcnRpZGFzBjsIVDoScmVzdWx0c19jb3VudGkCCgE%3D--edd9daa020477a61f855af771b65ce927894db27)  
[RH - Linha Protheus - GPE - Como configurar verbas de férias mês seguinte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgzaVbTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNzk0MTE3MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLXZlcmJhcy1kZS1mJUMzJUE5cmlhcy1tJUMzJUFBcy1zZWd1aW50ZQY7CFQ6DnNlYXJjaF9pZEkiKTI0Y2YyZTE5LTAzZTEtNGUyNy05OGM1LTY0OTJiMWJiYmZiMwY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiKHZlcmJhcyBkZSBmZXJpYXMgbWVzIGUgbWVzIHNlZ3VpbnRlBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--1b746a7b7ba9f728cae65102b707dd49676be4dd)  
[RH - Linha Protheus - GPE - Sistema não gera valor de dedução de dependente de IR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11283264869271-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-gera-valor-de-dedu%C3%A7%C3%A3o-de-dependente-de-IR)  
[RH - Linha Protheus - GPE - Como gerar relatório com todo o cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgUPlLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMDg5MDc3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci1yZWxhdCVDMyVCM3Jpby1jb20tdG9kby1vLWNhZGFzdHJvLWRlLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKTMyMTNlNTI0LWQ4ZmYtNDllNS1iN2VjLTUzYjY2M2I3YTExNgY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiUFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGNvbmZpZ3VyYXIgdmVyYmFzIGRlIGbDqXJpYXMgbcOqcyBzZWd1aW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--e18d84f2d6b6dbe1deaf4119fdf252cb80bda918)   
[RH - Linha Protheus - GPE - Verbas de férias não estão sendo integradas na folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgnX%2FDRUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNDQ3NjcxMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVmVyYmFzLWRlLWYlQzMlQTlyaWFzLW4lQzMlQTNvLWVzdCVDMyVBM28tc2VuZG8taW50ZWdyYWRhcy1uYS1mb2xoYS1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikyNGNmMmUxOS0wM2UxLTRlMjctOThjNS02NDkyYjFiYmJmYjMGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIih2ZXJiYXMgZGUgZmVyaWFzIG1lcyBlIG1lcyBzZWd1aW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--359b77115915e1e48eca01f59d103a98c063f853)
