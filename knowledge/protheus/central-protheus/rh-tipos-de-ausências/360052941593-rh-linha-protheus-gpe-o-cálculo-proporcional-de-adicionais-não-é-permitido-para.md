---
article_id: 360052941593
category: RH - Tipos de Ausências
content_hash: 18e77f03e357cf052ddb142921b845228b8225e345cdb907237e919a896aba74
fetched_at: '2026-06-28T22:43:21.025127+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - O cálculo proporcional de adicionais não é permitido
  para esse tipo de ausência
type: support-article
updated_at: '2025-07-11T14:21:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052941593-RH-Linha-Protheus-GPE-O-c%C3%A1lculo-proporcional-de-adicionais-n%C3%A3o-%C3%A9-permitido-para-esse-tipo-de-aus%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29417571165335)Tempo aproximado para leitura: 00:01:00min**

**Ocorrência**No módulo Gestão de Pessoal, ao incluir um afastamento por licença maternidade na rotina de Ausências, ao salvar o registro gera mensagem: **O cálculo proporcional de adicionais não é permitido para esse tipo de ausência.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11644723269015)**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -Recursos Humanos - A partir da versão 12.1.17

**Solução**

Verifique na rotina Tipo de Ausência - GPEA430, o cadastro da ausência de código 006,  a configuração do campo **Calc. Pr. Adic** deve ficar em **branco** ou como **Não.**  
Esse cálculo é efetuado automaticamente pela verba e o ID que foi informado nela. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085146633)

**Saiba mais:**

[RH - Linha Protheus - GPE - Cadastro tipos de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2FO2nTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBe2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyOTE3NDU5MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ2FkYXN0cm8tdGlwb3MtZGUtYXVzJUMzJUFBbmNpYQY7CFQ6DnNlYXJjaF9pZEkiKTBmOWY3MTg1LTZmMzctNDg4MC05Y2Q5LTliNDdhYjlhYWY0MwY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFXRpcG8gZGUgYXVzZW5jaWEGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--e2743590f37006cfa0d61204e05e7d41f27a3c3b)  
[RH - Linha Protheus - GPE - Como lançar ausência por Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwih4NrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzM5OTcxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1sYW4lQzMlQTdhci1hdXMlQzMlQUFuY2lhLXBvci1MaWNlbiVDMyVBN2EtTWF0ZXJuaWRhZGUtBjsIVDoOc2VhcmNoX2lkSSIpZjFiNmQxMWUtMDc4OS00NmZjLTg4NzAtYjgwYzg1NzQ2N2Q5BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIZYXVzZW5jaWEgbWF0ZXJuaWRhZGUGOwhUOhJyZXN1bHRzX2NvdW50aQL%2BAg%3D%3D--b3c2e3828a01d9fc0b72a51f9425471af2371525)  
[RH - Linha Protheus - GPE - Sequência de afastamento Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiOs63UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBkmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDQzOTA1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtU2VxdSVDMyVBQW5jaWEtZGUtYWZhc3RhbWVudG8tTGljZW4lQzMlQTdhLU1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpZjFiNmQxMWUtMDc4OS00NmZjLTg4NzAtYjgwYzg1NzQ2N2Q5BjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIZYXVzZW5jaWEgbWF0ZXJuaWRhZGUGOwhUOhJyZXN1bHRzX2NvdW50aQL%2BAg%3D%3D--d0670a26d90f3385994227df663cd6bc08b80825)  
[RH - Linha Protheus - GPE - Lançamento de ausência para funcionário em férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiNvYY%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDkzODEyNjEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUxhbiVDMyVBN2FtZW50by1kZS1hdXMlQzMlQUFuY2lhLXBhcmEtZnVuY2lvbiVDMyVBMXJpby1lbS1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTMwMTQ2ODM4LWEyY2MtNDczMi04YjA2LTdmMTZmYTU1NzE5NQY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDGF1c2VuY2kGOwhUOhJyZXN1bHRzX2NvdW50aQJ3Ag%3D%3D--79ef9eb875ebd7a863b74b54d1d98c1e9457054a)  
[RH - Linha Protheus - GPE - Como cadastrar estabilidade após retorno de Ausência](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh9Y5DUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0ODUxODAxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItZXN0YWJpbGlkYWRlLWFwJUMzJUIzcy1yZXRvcm5vLWRlLUF1cyVDMyVBQW5jaWEGOwhUOg5zZWFyY2hfaWRJIikzMDE0NjgzOC1hMmNjLTQ3MzItOGIwNi03ZjE2ZmE1NTcxOTUGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxhdXNlbmNpBjsIVDoScmVzdWx0c19jb3VudGkCdwI%3D--c5180f8403646f9bed89936b4375a54cce85acb9)
