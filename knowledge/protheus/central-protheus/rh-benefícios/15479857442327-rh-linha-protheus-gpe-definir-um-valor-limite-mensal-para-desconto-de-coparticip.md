---
article_id: 15479857442327
category: RH - Benefícios
content_hash: dc044750411efd81cc492eda9f038a3472702f80dfb96c1354c34b0a4a7ad4c4
fetched_at: '2026-06-28T22:44:03.895517+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Definir um valor limite mensal para desconto de
  coparticipação
type: support-article
updated_at: '2025-08-29T18:33:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15479857442327-RH-Linha-Protheus-GPE-Definir-um-valor-limite-mensal-para-desconto-de-coparticipa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15479904700951) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como definir um valor limite mensal para desconto de coparticipação?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**É possível configurar no sistema um teto para desconto de coparticipação e armazenar o saldo restante a ser descontado no próximo período.   
  
Para informar o limite a ser descontado existem duas opções:

**Opção 1 - Cadastro de Sindicato**  
Acessar em **Atualizações> Cadastros> Sindicatos (GPEA340)**. No cadastro de Sindicato, aba **Outras Inform.** informe o limite do desconto da coparticipação por mês.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15478694505623)

**Opção 2 - Tabela S148**  
Acessar **Atualizações> Definições de Cálculos> Manutenção de tabelas (GPEA320)**. Na S148 é possível definir um teto para o desconto da coparticipação por mês, definida por faixas, de acordo com o saldo restante da coparticipação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15479181931543)

**Observação:** Não é possível validar as duas opções para um mesmo sindicato, o sistema primeiro irá verificar se existe configuração válida de teto de desconto no cadastro de sindicato do funcionário, e apenas se não houver configuração válida, irá validar se existe a configuração na tabela S148.

Na rotina de Coparticipação (GPEA003) o sistema armazena o saldo restante a ser descontado e o período de origem do lançamento. 

**Saldo -** Saldo restante a ser descontado referente ao lançamento.  
**Per. Origem -** Indica se o lançamento foi originado no período atual ou anterior  
**Remanescente -** Saldo total restante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15479800151959)

Verifique as documentações abaixo com os exemplos do cálculo do desconto da coparticipação:  
[Teto Coparticipação - Cadastro de Sindicatos](https://tdn.totvs.com/pages/viewpage.action?pageId=640196742)  
[Teto Coparticipação - Tabela S148](https://tdn.totvs.com/pages/viewpage.action?pageId=657211413)

**Saiba Mais:**[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXczJlRwo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBp2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMzAxNzU2NzYwODU1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Eb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtY29wYXJ0aWNpcGElQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpMzNmZmZmZDItNTI4MC00YWVjLTkyYWUtMDgwNDE2ZGE5MTA2BjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIVY29wYXJ0aWNpcGHDp8OjbwY7CFQ6EnJlc3VsdHNfY291bnRpTw%3D%3D--f3fed369f95a8d151ce581556945758aeec9345d)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXoi9HOgo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjQ1NDE4Njg0OTUxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIiljMTU5NzlkOS00MTEyLTRhNjktOGQ0OC03MTYzN2ZmMGNjOTIGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkdSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gRG9jdW1lbnRhw6fDtWVzIHJlbGFjaW9uYWRhcyBhIHJvdGluYSAGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--88dbbe16a9f7a7bf326a478a1057b06f7124a880)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXEfwyNQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjIzNjA0OTI0Njk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tZGUtc2ElQzMlQkFkZQY7CFQ6DnNlYXJjaF9pZEkiKWMxNTk3OWQ5LTQxMTItNGE2OS04ZDQ4LTcxNjM3ZmYwY2M5MgY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiR1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBEb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGEgcm90aW5hIAY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--6e8febbec63f4078fa505e6fc87c3a653f0da807)
