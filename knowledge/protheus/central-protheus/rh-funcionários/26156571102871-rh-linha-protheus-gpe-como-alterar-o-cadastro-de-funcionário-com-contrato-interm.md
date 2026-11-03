---
article_id: 26156571102871
category: RH - Funcionários
content_hash: 497d78a7f8932573f275a5f639798c86901d841bfb31536a4fa8e418fe401725
fetched_at: '2026-06-28T22:43:27.256982+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE -  Como alterar o cadastro de Funcionário com contrato
  Intermitente para Indeterminado
type: support-article
updated_at: '2025-05-08T21:03:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26156571102871-RH-Linha-Protheus-GPE-Como-alterar-o-cadastro-de-Funcion%C3%A1rio-com-contrato-Intermitente-para-Indeterminado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26156562533271) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como alterar o cadastro de Funcionário com **contrato Intermitente para Indeterminado?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Os seguintes campos devem ser ajustados no Cadastro de Funcionário para alterar o contrato para tipo Indeterminado:  
**> Categoria do Funcionário (RA\_CATFUNC)** = deve ficar como M (Mensalista)  
**> Salário (RA\_SALARIO)** = deve ser preenchido  
**> Tipo de Contrato (RA\_TPCONTR**) = deve ficar como Indeterminado  
**> Tipo de Pagamento (RA\_TIPOPGT)** = deve ficar como M (Mensal)  
**> Categoria e-Social (RA\_CATEFD)** = deve ficar como 101

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26156562534295)

**Saiba Mais:**[RH - Linha Protheus - GPE - Calculo de 13º intermitente X indeterminado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX7OetAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk1NTQxMDMzMTktUkgtTGluaGEtUHJvdGhldXMtR1BFLUNhbGN1bG8tZGUtMTMlQzIlQkEtaW50ZXJtaXRlbnRlLVgtaW5kZXRlcm1pbmFkbwY7CFQ6DnNlYXJjaF9pZEkiKTNlMmMwMWE0LWVhYTQtNDkwZi05OTc4LWUzYTZhNTMzYTQwYwY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEWludGVybWl0ZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAaA%3D--a6a1f7de5dd0f79efd0916ff6a0f703bdb1e4f6d)  
[RH - Linha Protheus - GPE - Cálculo de Férias intermitente X indeterminado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX1uHW7Q46D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE2NDE0Njc1MTYyNzc1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1DJUMzJUExbGN1bG8tZGUtRiVDMyVBOXJpYXMtaW50ZXJtaXRlbnRlLVgtaW5kZXRlcm1pbmFkbwY7CFQ6DnNlYXJjaF9pZEkiKTNlMmMwMWE0LWVhYTQtNDkwZi05OTc4LWUzYTZhNTMzYTQwYwY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEWludGVybWl0ZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAaA%3D--0a5ef231bfea74cfd65806d5298ce9d75034da42)  
[RH - Linha Protheus - GPE - Como deve ser realizado o cadastro de um funcionário com contrato intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhuNT7TUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNjM1NTA1NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1kZXZlLXNlci1yZWFsaXphZG8tby1jYWRhc3Ryby1kZS11bS1mdW5jaW9uJUMzJUExcmlvLWNvbS1jb250cmF0by1pbnRlcm1pdGVudGUGOwhUOg5zZWFyY2hfaWRJIikwMDBjZWRhZS0zMDBhLTQ3MWYtODAwZC00ZDNhMGQxZmViNzUGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJInBSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBkZXZlIHNlciByZWFsaXphZG8gbyBjYWRhc3RybyBkZSB1bSBmdW5jaW9uw6FyaW8gY29tIGNvbnRyYXRvIGludGVybWl0ZW50ZQY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--715cb46a73defcc9e3b2059b32771aa6c64a5b5e)
