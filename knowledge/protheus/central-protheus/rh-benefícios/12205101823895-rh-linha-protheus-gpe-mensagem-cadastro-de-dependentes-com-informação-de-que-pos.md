---
article_id: 12205101823895
category: RH - Benefícios
content_hash: 1463a075ccf4d8f1fba042be0aa3d3e92bef172bafcd067bc95cdbc9529225f2
fetched_at: '2026-06-28T22:44:04.698898+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Mensagem "Cadastro de dependentes com informação
  de que possui plano de saúde, porém não existe plano ativo" ao calcular roteiro
  PLA
type: support-article
updated_at: '2025-09-25T11:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12205101823895-RH-Linha-Protheus-GPE-Mensagem-Cadastro-de-dependentes-com-informa%C3%A7%C3%A3o-de-que-possui-plano-de-sa%C3%BAde-por%C3%A9m-n%C3%A3o-existe-plano-ativo-ao-calcular-roteiro-PLA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32987129031063) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Mensagem "Cadastro de dependentes com informação de que possui plano de saúde, porém não existe plano ativo" ao calcular roteiro PLA.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12204724571799)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**O dependente **não está vinculado** a um plano de saúde/odontológico e no cadastro de dependente está com **Sim** para plano de saúde.   
  
**Solução**  
Verifique no cadastro de dependente como está o campo RB\_PLSAUDE e na rotina de Planos Ativos se o dependente possui plano de saúde.

-Cadastro de Dependente:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12204753161111)  
  
  
-Planos Ativos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32987123726999)  
  
A mensagem aparece apenas para **informar** que o dependente não está vinculado a um plano de saúde, portanto **não interfere** no cálculo dos que estão cadastrados na rotina de planos ativos.   
  
Caso o dependente realmente não possua plano de saúde, o ideal é deixar o campo RB\_PLSAUDE com **Não,** ou se faltou cadastrar o dependente no planos ativos, é só realizar o cadastro e prosseguir com um novo cálculo.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Quais as tabelas S relacionadas ao roteiro PLA - Plano de Saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXO27DSAo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBoGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMzA3NjMyNzA0NDA3LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy10YWJlbGFzLVMtcmVsYWNpb25hZGFzLWFvLXJvdGVpcm8tUExBLVBsYW5vLWRlLVNhJUMzJUJBZGUGOwhUOg5zZWFyY2hfaWRJIilmZGY2MDNkYy0zZDllLTQzMDgtYWRlNi0zNjNhMDc3N2M0ZTYGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxncGVtMDE2BjsIVDoScmVzdWx0c19jb3VudGkC6AM%3D--b8c3144dd672a9d832fdb85f9f2e55837a3e90e1)  
[RH - Linha Protheus - GPE - Pontos de Entrada na rotina Cálculo de Plano de Saúde - GPEM016](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjOQzzVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBo2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1OTc4MjA5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUG9udG9zLWRlLUVudHJhZGEtbmEtcm90aW5hLUMlQzMlQTFsY3Vsby1kZS1QbGFuby1kZS1TYSVDMyVCQWRlLUdQRU0wMTYGOwhUOg5zZWFyY2hfaWRJIilmZGY2MDNkYy0zZDllLTQzMDgtYWRlNi0zNjNhMDc3N2M0ZTYGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxncGVtMDE2BjsIVDoScmVzdWx0c19jb3VudGkC6AM%3D--6ad6ab5c7e28742752e46116944956b125a174e5)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXEfwyNQo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjIzNjA0OTI0Njk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tZGUtc2ElQzMlQkFkZQY7CFQ6DnNlYXJjaF9pZEkiKWZkZjYwM2RjLTNkOWUtNDMwOC1hZGU2LTM2M2EwNzc3YzRlNgY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDGdwZW0wMTYGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--c6750b9782e79640685908939b6e767ff13a5517)  
[RH - Linha Protheus - GPE - Quais as documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXoi9HOgo6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExMjQ1NDE4Njg0OTUxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYS1yb3RpbmEtZGUtcGxhbm8tb2RvbnRvbCVDMyVCM2dpY28GOwhUOg5zZWFyY2hfaWRJIilmZGY2MDNkYy0zZDllLTQzMDgtYWRlNi0zNjNhMDc3N2M0ZTYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxncGVtMDE2BjsIVDoScmVzdWx0c19jb3VudGkC6AM%3D--c99064c533f9fbf9111dd5649c524f3090a2ec5c)  
[RH - Linha Protheus - GPE - Não é realizado o cálculo do plano de saúde para alguns dependentes quando o plano do titular é diferente dos dependentes](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXonLEAAs6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB8Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEyMDk3OTIzNzUyNDcxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1OJUMzJUEzby0lQzMlQTktcmVhbGl6YWRvLW8tYyVDMyVBMWxjdWxvLWRvLXBsYW5vLWRlLXNhJUMzJUJBZGUtcGFyYS1hbGd1bnMtZGVwZW5kZW50ZXMtcXVhbmRvLW8tcGxhbm8tZG8tdGl0dWxhci0lQzMlQTktZGlmZXJlbnRlLWRvcy1kZXBlbmRlbnRlcwY7CFQ6DnNlYXJjaF9pZEkiKWZkZjYwM2RjLTNkOWUtNDMwOC1hZGU2LTM2M2EwNzc3YzRlNgY7CEY6CXJhbmtpDjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDGdwZW0wMTYGOwhUOhJyZXN1bHRzX2NvdW50aQLoAw%3D%3D--fc07a5eb34ca1d805c677667385f7cdcc1917262)
