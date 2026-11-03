---
article_id: 360029040432
category: RH - Benefícios
content_hash: a820edde392d296f13bc9cbfce7c7b565ffcd71758b4afa1c1c3c8dfea1401a7
fetched_at: '2026-06-28T22:44:04.854487+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como alterar faixa etária de assistência médica
  automaticamente
type: support-article
updated_at: '2025-09-30T11:28:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029040432-RH-Linha-Protheus-GPE-Como-alterar-faixa-et%C3%A1ria-de-assist%C3%AAncia-m%C3%A9dica-automaticamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como alterar faixa etária de assistência médica automaticamente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**O sistema verifica o cadastro nas tabelas a coluna Código, que deverá ser sempre o **mesmo código para o mesmo tipo de plano.**

* Plano de Saúde: **S009**
* Plano Odontológico: **S014**

Para que o sistema busque a próxima sequência corretamente, é necessário realizar o cadastro conforme exemplo da tabela S009:  
 **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100933133/mceclip0.png)**

Veja que o fornecedor 003 possui 1 plano apenas com 4 faixas salariais, todas com o mesmo código. O mesmo acontece para o fornecedor 002. Também existe o parâmetro **MV\_PLSBASI** quedetermina a alteração do Plano de Saúde/Odontológico por Faixa Etária, de acordo com a sua configuração.   
  
Quando configurado com **1**, a alteração do valor do Plano de Saúde será realizada no mês de aniversário do beneficiário;  
Quando configurado com **2**, a alteração do valor do Plano de Saúde será realizada no mês subsequente ao aniversário do beneficiário.  
  
Para realizar a alteração do parâmetro siga os seguintes passos:  
1. Acesse o **Configurador** / **Cadastros** / **Parâmetros;**  
2. Localize o parâmetro **MV\_PLSBASI** e selecione a opção **Alterar;**  
3. Altere o conteúdo de acordo com a demanda da empresa e Salve.  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Como cadastrar e calcular assistência médica por faixa etária](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjbHMTSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxODM1MzM3MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItZS1jYWxjdWxhci1hc3Npc3QlQzMlQUFuY2lhLW0lQzMlQTlkaWNhLXBvci1mYWl4YS1ldCVDMyVBMXJpYQY7CFQ6DnNlYXJjaF9pZEkiKWFjNmEyNDhiLTk0OWEtNGYxYi05M2QxLTI5NTMzNDUxMzdlYgY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEWZhaXhhIGV0YXJpYQY7CFQ6EnJlc3VsdHNfY291bnRpAqIE--ebfd32fe90643070d3faf5e722b41fe180366230)  
[RH - Linha Protheus - GPE - Como cadastrar e calcular assistência odontológica por faixa etária](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjs88jSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxODY3MDU3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItZS1jYWxjdWxhci1hc3Npc3QlQzMlQUFuY2lhLW9kb250b2wlQzMlQjNnaWNhLXBvci1mYWl4YS1ldCVDMyVBMXJpYQY7CFQ6DnNlYXJjaF9pZEkiKWFjNmEyNDhiLTk0OWEtNGYxYi05M2QxLTI5NTMzNDUxMzdlYgY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEWZhaXhhIGV0YXJpYQY7CFQ6EnJlc3VsdHNfY291bnRpAqIE--28594839919819fce7e50efaa68a5c2afb15e168)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXEfwyNQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjIzNjA0OTI0Njk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tZGUtc2ElQzMlQkFkZQY7CFQ6DnNlYXJjaF9pZEkiKTAwZmIyOThkLTk2ODktNGUzMC04ZGYyLTVlMzIxMmU5MTkyZgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiLFF1YWlzIGFzIGRvY3VtZW50YcOnw7VlcyByZWxhY2lvbmFkYXMgYQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--bb364b5385f2aba3d2535b211110840aefa96e6b)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXoi9HOgo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjQ1NDE4Njg0OTUxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIilkNWQ0YTE1OC1hZGQxLTQ2N2EtYWI0Zi00ZWM2NDI2ZDE5MjAGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhByb3RlaXJvIHBsYQY7CFQ6EnJlc3VsdHNfY291bnRpAlYD--755bdf4e2150308cacaa2dfacd6ac066b8b28102)  
[RH - Linha Protheus - GPE - Quais as tabelas S relacionadas ao roteiro PLA - Plano de Saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXO27DSAo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMzA3NjMyNzA0NDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy10YWJlbGFzLVMtcmVsYWNpb25hZGFzLWFvLXJvdGVpcm8tUExBLVBsYW5vLWRlLVNhJUMzJUJBZGUGOwhUOg5zZWFyY2hfaWRJIilkNWQ0YTE1OC1hZGQxLTQ2N2EtYWI0Zi00ZWM2NDI2ZDE5MjAGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhByb3RlaXJvIHBsYQY7CFQ6EnJlc3VsdHNfY291bnRpAlYD--5d9985fc35af98743b13f1e17a2b9bbfa5addb12)
