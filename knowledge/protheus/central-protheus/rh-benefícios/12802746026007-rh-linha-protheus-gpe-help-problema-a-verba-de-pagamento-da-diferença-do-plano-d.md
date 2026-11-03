---
article_id: 12802746026007
category: RH - Benefícios
content_hash: a7d839e8e2fbd89305702dca7e394993f11346b1ffbe6cb739037da50f821216
fetched_at: '2026-06-28T22:44:04.885311+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: 'RH - Linha Protheus - GPE - Help: Problema: A Verba de pagamento da diferença
  do Plano de Dep./Agreg. deve ser preenchida'
type: support-article
updated_at: '2025-08-28T03:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12802746026007-RH-Linha-Protheus-GPE-Help-Problema-A-Verba-de-pagamento-da-diferen%C3%A7a-do-Plano-de-Dep-Agreg-deve-ser-preenchida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31909803692951) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**

Ao inserir a Data Final no campo **RHL\_DATFIM** para o dependente, sistema apresenta a mensagem:   
Help: Problema: A Verba de pagamento da diferença do Plano de Dep./Agreg. deve ser preenchida!

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12802027480983)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da release 12.1.17  
  
**Causa**A mensagem é apresentada quando não existe verbas de Diferença de Dependente cadastradas.   
  
**Solução**Para solucionar a ocorrência, realize o cadastro das verbas necessárias para o cálculo do dependente utilizando os IDs abaixo como **verbas de Base:**

* 1427 - Base parte Empresa Diferença Assistência Médica Dependentes e Agregados.
* 1429 - Base parte Empresa Diferença Assistência Odontológica Dependentes e Agregados.

E cadastrar as verbas para o **pagamento** da diferença, essas serão **verbas de provento** e **não terão ID de cálculo.**  
  
Veja mais sobre o Cálculo de Plano de Saúde Proporcional [aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=317295045)

**Saiba Mais**[RH - Linha Protheus - GPE - Descontar plano de saúde do cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXS1HuAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA2MzQ3NTA3NDMtUkgtTGluaGEtUHJvdGhldXMtR1BFLURlc2NvbnRhci1wbGFuby1kZS1zYSVDMyVCQWRlLWRvLWMlQzMlQTFsY3Vsby1kZS1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTczZGZjZDFjLTNjZGUtNGZiOS1iZWI2LTgxYzA4Mzk0YjlmOAY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiE3BsYW5vIGRlIHNhdWRlBjsIVDoScmVzdWx0c19jb3VudGkC6QM%3D--bab91ed1a7c20c6186592a6b1bb5c1a8e658f4d9)  
[RH - Linha Protheus - GPE - Cálculo do Plano de Saúde Proporcional a data de Aquisição](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh9VDDVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODk5OTkzMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRvLVBsYW5vLWRlLVNhJUMzJUJBZGUtUHJvcG9yY2lvbmFsLWEtZGF0YS1kZS1BcXVpc2klQzMlQTclQzMlQTNvBjsIVDoOc2VhcmNoX2lkSSIpOTg0YjRhYWItNzA4NC00NjcwLThmNzctMmEyMzFiMTgyY2QyBjsIRjoJcmFua2kIOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSITcGxhbm8gZGUgc2F1ZGUGOwhUOhJyZXN1bHRzX2NvdW50aQLpAw%3D%3D--b22128f50717c478a5e57843d16eed38c7404390)  
[RH - Linha Protheus - GPE - Cálculo do plano de saúde proporcional após encerramento do plano](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwheUyTVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODIxMzIxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRvLXBsYW5vLWRlLXNhJUMzJUJBZGUtcHJvcG9yY2lvbmFsLWFwJUMzJUIzcy1lbmNlcnJhbWVudG8tZG8tcGxhbm8GOwhUOg5zZWFyY2hfaWRJIik5ODRiNGFhYi03MDg0LTQ2NzAtOGY3Ny0yYTIzMWIxODJjZDIGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhNwbGFubyBkZSBzYXVkZQY7CFQ6EnJlc3VsdHNfY291bnRpAukD--ed5aba6f19528ebd5cc31179c015ce4d694b2bc9)
