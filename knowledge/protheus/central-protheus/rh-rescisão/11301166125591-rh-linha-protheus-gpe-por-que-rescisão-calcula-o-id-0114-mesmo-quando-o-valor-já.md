---
article_id: 11301166125591
category: RH - Rescisão
content_hash: f907bf2d23ac2baeda65929d38272a07f2436899d43af7c75dd7e61badc319f6
fetched_at: '2026-06-28T22:43:48.408301+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Por que rescisão calcula o id 0114 mesmo quando
  o valor já é todo calculado em roteiros 131 e 132 (roteiros cálculo 13º salário)
type: support-article
updated_at: '2025-09-09T14:11:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11301166125591-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-calcula-o-id-0114-mesmo-quando-o-valor-j%C3%A1-%C3%A9-todo-calculado-em-roteiros-131-e-132-roteiros-c%C3%A1lculo-13%C2%BA-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34807989604375) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que a rescisão calcula o id 0114 (13º Salário na Indenização Rescisão) mesmo quando o valor já é todo calculado em roteiros 131 e 132 (roteiros cálculo 13º salário)?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de pessoal - Todas as versões  
  
**Solução**A rescisão calcula o id 0114 mesmo quando o valor foi todo calculado em roteiros 131 e 132, devido este valor se tratar de uma verba indenizatória (obrigatória devido configuração tabela S043). Deste modo o valor do 13º salário em rescisão é calculado no id 0114 e como houve pagamento nos roteiros 131 e 132, o calculo de rescisão desconta esses valores nos ids 0183 e 0247 assim o valor é liquidado (entra em proventos e sai em descontos).

**Saiba mais**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[MP - GPE - Configuração de verbas de desconto de 13º salário na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059185253-MP-GPE-Configura%C3%A7%C3%A3o-de-verbas-de-desconto-de-13%C2%BA-sal%C3%A1rio-na-rescis%C3%A3o?source=search)  
[MP - GPE - Cálculo indevido de INSS 13º na rescisão após pagamento da 2ª parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgY9vTSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMTU1NDcxMi1NUC1HUEUtQyVDMyVBMWxjdWxvLWluZGV2aWRvLWRlLUlOU1MtMTMlQzIlQkEtbmEtcmVzY2lzJUMzJUEzby1hcCVDMyVCM3MtcGFnYW1lbnRvLWRhLTIlQzIlQUEtcGFyY2VsYS1kby0xMyVDMiVCQS1TYWwlQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIilkN2JmYTliNC0wZGEwLTQ3NWEtYjk5NC1jMDYxYWVkZjM2OWUGOwhGOglyYW5raQs6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhNyZXNjaXPDo28gMTPCugY7CFQ6EnJlc3VsdHNfY291bnRpAqwE--62dc1a469764f1d71f8743601a111685b497c4d8)  
[RH - Linha Protheus - GPE - Por que rescisão desconta duas vezes valor desconto adiantamento 13 salário calculado em roteiro 132](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX8AtWHAo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMTE2ODE4OTg0OTgzLVJILUxpbmhhLVByb3RoZXVzLUdQRS1Qb3ItcXVlLXJlc2NpcyVDMyVBM28tZGVzY29udGEtZHVhcy12ZXplcy12YWxvci1kZXNjb250by1hZGlhbnRhbWVudG8tMTMtc2FsJUMzJUExcmlvLWNhbGN1bGFkby1lbS1yb3RlaXJvLTEzMgY7CFQ6DnNlYXJjaF9pZEkiKWJiYWZhZjdhLTM3MTEtNGQyOC1iY2NjLTFmOWJlNmQ4MDE2NQY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiUk1QIC0gR1BFIC0gQ29uZmlndXJhw6fDo28gZGUgdmVyYmFzIGRlIGRlc2NvbnRvIGRlIDEzwrogc2Fsw6FyaW8gbmEgcmVzY2lzw6NvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--d0ea7e6239a96c2f1d0a15f94f30253478da692c)  
[RH - Linha Protheus - GPE - Por que rescisão gera id 1672 indevidamente quando a data de demissão contabiliza 12/12 avos de 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXxIHFDwo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB3Wh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMDYyODU0NDAzMDk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Qb3ItcXVlLXJlc2NpcyVDMyVBM28tZ2VyYS1pZC0xNjcyLWluZGV2aWRhbWVudGUtcXVhbmRvLWEtZGF0YS1kZS1kZW1pc3MlQzMlQTNvLWNvbnRhYmlsaXphLTEyLTEyLWF2b3MtZGUtMTMlQzIlQkEtc2FsJUMzJUExcmlvBjsIVDoOc2VhcmNoX2lkSSIpYmJhZmFmN2EtMzcxMS00ZDI4LWJjY2MtMWY5YmU2ZDgwMTY1BjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJSTVAgLSBHUEUgLSBDb25maWd1cmHDp8OjbyBkZSB2ZXJiYXMgZGUgZGVzY29udG8gZGUgMTPCuiBzYWzDoXJpbyBuYSByZXNjaXPDo28GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--13a5c728bf698675414b03e4d36ff4b21f0d6cb2)  
[RH - Linha Protheus - GPE - eSocial - S-5001 - Divergências na base de INSS de 13º Salário para Trabalhadores que receberam 13º Salário e foram demitidos no mesmo mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041152014-RH-Linha-Protheus-GPE-eSocial-S-5001-Diverg%C3%AAncias-na-base-de-INSS-de-13%C2%BA-Sal%C3%A1rio-para-Trabalhadores-que-receberam-13%C2%BA-Sal%C3%A1rio-e-foram-demitidos-no-mesmo-m%C3%AAs?source=search)
