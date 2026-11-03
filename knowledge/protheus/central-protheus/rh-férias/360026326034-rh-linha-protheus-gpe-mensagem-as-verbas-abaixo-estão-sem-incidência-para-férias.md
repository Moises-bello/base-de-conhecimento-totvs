---
article_id: 360026326034
category: RH - Férias
content_hash: d340a5425b2f61d48fa8d4785f9c7f997b665bbd173d8aa8d3936152516d1297
fetched_at: '2026-06-28T22:43:59.364217+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Mensagem "As verbas abaixo estão sem incidência
  para férias (RV_REFFER)..." ao executar cálculo
type: support-article
updated_at: '2025-08-21T19:53:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026326034-RH-Linha-Protheus-GPE-Mensagem-As-verbas-abaixo-est%C3%A3o-sem-incid%C3%AAncia-para-f%C3%A9rias-RV-REFFER-ao-executar-c%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34354631631383) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**Ao executar cálculos de roteiros na rotina GPEM020, sistema apresenta um log com a seguinte mensagem: "As verbas abaixo estão sem incidência para férias (RV\_REFFER). Verifique a necessidade de alteração e recalculo da folha.":  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040986734)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Causa**Essa mensagem é apresentada quando verbas relacionadas a IDs de cálculos de férias estão com o campo Ref. a Fer (RV\_REFFER) com Não ou sem preenchimento.   
  
**Solução**As verbas que aparecerem no log devem ter o campo Ref. a Fer (RV\_REFFER) **alterado para S - SIM.**  
Acesse: **Atualizações/ Definições de Cálculo/ Verbas** e altere o campo localizado na **aba Incidências**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040986894)

**Saiba Mais**[RH - Linha Protheus - GPE - Como configurar verbas de férias mês seguinte](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgzaVbTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNzk0MTE3MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLXZlcmJhcy1kZS1mJUMzJUE5cmlhcy1tJUMzJUFBcy1zZWd1aW50ZQY7CFQ6DnNlYXJjaF9pZEkiKTc1N2M4ZTE5LTAxZjEtNDQ4ZC1iZjQxLTIxN2YxZDUwZjFiNwY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEXZlcmJhIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAvoG--c60ae7f5f8cef90c9830ddd6e20ca1099fb1c729)  
[RH - Linha Protheus - GPE - Como são demonstradas as verbas de férias na folha](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwheU6LUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0OTY5MzUzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1zJUMzJUEzby1kZW1vbnN0cmFkYXMtYXMtdmVyYmFzLWRlLWYlQzMlQTlyaWFzLW5hLWZvbGhhLQY7CFQ6DnNlYXJjaF9pZEkiKTc1N2M4ZTE5LTAxZjEtNDQ4ZC1iZjQxLTIxN2YxZDUwZjFiNwY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEXZlcmJhIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAvoG--a193d7d0906f56fa6cd26153f2215b1c24ec1b92)  
[RH - Linha Protheus - GPE - Quais são os ID's para o cadastro das verbas de férias em dobro](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhGeBzVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzY5ODM3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUXVhaXMtcyVDMyVBM28tb3MtSUQtcy1wYXJhLW8tY2FkYXN0cm8tZGFzLXZlcmJhcy1kZS1mJUMzJUE5cmlhcy1lbS1kb2JybwY7CFQ6DnNlYXJjaF9pZEkiKTc1N2M4ZTE5LTAxZjEtNDQ4ZC1iZjQxLTIxN2YxZDUwZjFiNwY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEXZlcmJhIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAvoG--ade87da04165cbca4122e71fd62686661ccde960)  
[RH - Linha Protheus - GPE - Verbas de férias não estão sendo integradas na folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgnX%2FDRUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwNDQ3NjcxMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtVmVyYmFzLWRlLWYlQzMlQTlyaWFzLW4lQzMlQTNvLWVzdCVDMyVBM28tc2VuZG8taW50ZWdyYWRhcy1uYS1mb2xoYS1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIik3NTdjOGUxOS0wMWYxLTQ0OGQtYmY0MS0yMTdmMWQ1MGYxYjcGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhF2ZXJiYSBmZXJpYXMGOwhUOhJyZXN1bHRzX2NvdW50aQL6Bg%3D%3D--7d649203563301a4c158b1e82a2f29b09df6ee03)  
[RH - Linha Protheus - GPE - Como criar e informar uma verba sem Identificador de cálculo nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi6wRo%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDIzMDQ0NDItUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY3JpYXItZS1pbmZvcm1hci11bWEtdmVyYmEtc2VtLUlkZW50aWZpY2Fkb3ItZGUtYyVDMyVBMWxjdWxvLW5hcy1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTc1N2M4ZTE5LTAxZjEtNDQ4ZC1iZjQxLTIxN2YxZDUwZjFiNwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEXZlcmJhIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAvoG--712d12fab7e3698b368faf5dd8178517b7811a8a)
