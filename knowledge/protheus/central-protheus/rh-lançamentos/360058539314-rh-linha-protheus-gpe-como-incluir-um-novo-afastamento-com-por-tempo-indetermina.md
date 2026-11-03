---
article_id: 360058539314
category: RH - Lançamentos
content_hash: abf5593ef9b8d621260e9e53e500d5d534b1a8258c17b58efdb31461e5051646
fetched_at: '2026-06-28T22:43:31.204733+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir um novo afastamento com por tempo
  indeterminado  para funcionário que já teve um afastamento com  15 dias, considerando
  que será pago pelo INSS
type: support-article
updated_at: '2025-04-25T20:45:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058539314-RH-Linha-Protheus-GPE-Como-incluir-um-novo-afastamento-com-por-tempo-indeterminado-para-funcion%C3%A1rio-que-j%C3%A1-teve-um-afastamento-com-15-dias-considerando-que-ser%C3%A1-pago-pelo-INSS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671008888215) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como incluir um novo afastamento com por tempo indeterminado para funcionário que já teve um afastamento com 15 dias, considerando que será pago pelo INSS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para lançamento de ausência que contém o mesmo CID e sem data de retorno previsto por conta do afastamento do INSS, deve-se informar campo **Nr. Sequencia**com referência a continuação da ausência lançada anteriormente e informar**999**no campo **Num. Dias** (este preenchimento deixará a**data fim de afastamento em branco**, já que não há previsão de fim deste).

Siga os seguintes passos:

**1.** Acesse no menu **Atualizações > Lançamentos > Ausências;  
2.** Selecione o funcionário e clique em **Manutenção**;  
**3.** Inclua uma nova linha com o mesmo código de afastamento anterior, preencha o campo **Num. Dias** com **999** e informe no campo **Nr. Sequencia** o código correspondente ao primeiro afastamento.

**Exemplo**  
Veja que o campo **Nr. Sequencia**possui preenchimento **001**,. pois refere-se a continuação do afastamento lançado com sequência 001.

No campo **Nr. Dias** temos **999**, para que o campo **Dt. Fim Afast**. fique em branco.

Como a segunda linha é continuação da sequência 001 e este funcionário já teve 15 dias pagos, a segunda linha contém **0 dias** a serem pagos, apresentada no campo **Dias Empresa**.  
  
![](https://p23.zdusercontent.com/attachment/888110/cEiMZ9nhbmqSj1RpPWCymw0kj?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..XWWKFk8YLV96egl-HDenGQ.rsONDid7-IVkKQcRRBMADQsxUXRUgj8vLCWkPloAx7XGAN7cFI96VRAllaX474pEqeZAuN8mLANofvO4q1RCTAu3YKxLoxW6X-iJMV8QJO2D3NIH8lfJG5iODIN5KuvOY5murNYSqWLK5JQWFJBul4eeGPlLF9j-i3K6URuBxEYmrQPGD_tMKjmxD_f4PpdP4q9SPDWe_3hVIu3L4ouHMwbH-sox2u58zrjr-OkuO5BHnelsbO4fsPFnQddz6IFgP0TF1gZOgln4_Kf_VSAsIwIlFdscbONkPDf5SqU5UEA.gZ-BnHjXthgW_9RUKKLA1A)

Desta forma, ficará em aberto a **data de retorno** do funcionário e não serão mais calculados dias à este funcionário, já que este será pago pelo INSS.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como informar data fim de afastamentos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhNa1o%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBg2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDY0NzY2MjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8taW5mb3JtYXItZGF0YS1maW0tZGUtYWZhc3RhbWVudG9zBjsIVDoOc2VhcmNoX2lkSSIpZTU4OWZhMzEtMTA4OS00NjE1LThkMTYtNzllNmExYWNlMWY1BjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIvQXR1YWxpemHDp8O1ZXMgPiBMYW7Dp2FtZW50b3MgPiBBdXPDqm5jaWFzBjsIVDoScmVzdWx0c19jb3VudGkCswE%3D--8b055d825d48e462333840ef42d04b3b37decaa9)  
[RH - Linha Protheus - GPE - Como alterar tipo de afastamento quando solicitado pelo INSS](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiQnHLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMzAxMjExMi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1hbHRlcmFyLXRpcG8tZGUtYWZhc3RhbWVudG8tcXVhbmRvLXNvbGljaXRhZG8tcGVsby1JTlNTBjsIVDoOc2VhcmNoX2lkSSIpZTU4OWZhMzEtMTA4OS00NjE1LThkMTYtNzllNmExYWNlMWY1BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIvQXR1YWxpemHDp8O1ZXMgPiBMYW7Dp2FtZW50b3MgPiBBdXPDqm5jaWFzBjsIVDoScmVzdWx0c19jb3VudGkCswE%3D--26cadd4a7ae730fc4f0c90fa6ea31723c6031993)  
[RH - Linha Protheus - GPE - Como informar para o sistema que o novo afastamento é sequencia do anterior](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhizaHUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0OTY1OTIzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1pbmZvcm1hci1wYXJhLW8tc2lzdGVtYS1xdWUtby1ub3ZvLWFmYXN0YW1lbnRvLSVDMyVBOS1zZXF1ZW5jaWEtZG8tYW50ZXJpb3IGOwhUOg5zZWFyY2hfaWRJIillNTg5ZmEzMS0xMDg5LTQ2MTUtOGQxNi03OWU2YTFhY2UxZjUGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIi9BdHVhbGl6YcOnw7VlcyA%2BIExhbsOnYW1lbnRvcyA%2BIEF1c8OqbmNpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQKzAQ%3D%3D--ff9872af52c96a8f3b9b2f94b728384bbf07f10f)  
[RH - Linha Protheus - GPE - Lançamento de ausência, gera mensagem Limite de lançamentos do mesmo tipo para um mesmo período alcançado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhuXQbUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB3mh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAzOTQ3MjQ5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTGFuJUMzJUE3YW1lbnRvLWRlLWF1cyVDMyVBQW5jaWEtZ2VyYS1tZW5zYWdlbS1MaW1pdGUtZGUtbGFuJUMzJUE3YW1lbnRvcy1kby1tZXNtby10aXBvLXBhcmEtdW0tbWVzbW8tcGVyJUMzJUFEb2RvLWFsY2FuJUMzJUE3YWRvLQY7CFQ6DnNlYXJjaF9pZEkiKWU1ODlmYTMxLTEwODktNDYxNS04ZDE2LTc5ZTZhMWFjZTFmNQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiL0F0dWFsaXphw6fDtWVzID4gTGFuw6dhbWVudG9zID4gQXVzw6puY2lhcwY7CFQ6EnJlc3VsdHNfY291bnRpArMB--af088ce6a4dfe4dbdb1779ebafda4ad1e48aa47a)
