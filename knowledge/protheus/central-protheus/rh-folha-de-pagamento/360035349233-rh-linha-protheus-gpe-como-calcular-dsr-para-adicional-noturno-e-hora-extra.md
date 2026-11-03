---
article_id: 360035349233
category: RH - Folha de Pagamento
content_hash: e6272cdff5dbbb16a1da70cfca3351f178d00fdd0dfe0d296e607c73c389bed3
fetched_at: '2026-06-28T22:44:12.245485+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular DSR para Adicional Noturno e Hora
  Extra
type: support-article
updated_at: '2025-04-23T12:12:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035349233-RH-Linha-Protheus-GPE-Como-calcular-DSR-para-Adicional-Noturno-e-Hora-Extra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23978977389719) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como calcular DSR para Adicional Noturno e Hora Extra?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para cálculo de DSR sobre Adicional Noturno ou Hora Extra, as verbas de Adicional Noturno e Hora Extra devem estar parametrizadas para isso. Com as verbas parametrizadas, o sistema fará o cálculo do DSR de acordo com o cadastro de Períodos do mês de cálculo.  
  
Para que o sistema calcule o DSR sobre uma hora extra ou sobre um adicional noturno, a verba de adicional noturno e/ou hora extra deve estar com os campos selecionados abaixo conforme print, assim o DSR sobre essas verbas serão calculados no ID 0035 que é o ID padrão para cálculo de DSR hora extra:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046182833)  
  
Caso queira que os sistema calcule o DSR do adicional noturno em uma verba diferente do ID 0035, o campo Verba DSR da verba de Adicional Noturno deve ser preenchido com a outra verba de DSR Adicional Noturno, abaixo exemplo:  
  
Verba DSR adicional Noturno criada sem ID:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046183193)  
  
Na verba de Adicional Noturno, os campos abaixo devem estar conforme print, onde no campo Verba DSR deve estar preenchido com a verba DSR Adicional Noturno criada:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045326814)  
  
A mesma configuração acima serve para caso queira calcular o DSR Hora Extra em uma verba diferente do ID 0035.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_TPCALEN](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhDkiLHGgA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExNTAxMDA4MTM0Ny1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25maWd1cmFyLW8tcGFyJUMzJUEybWV0cm8tTVYtVFBDQUxFTi0GOwhUOg5zZWFyY2hfaWRJIikwODdhNGVjMi0yODZmLTRkMTAtODNkMy1jNjY2MzI3ZDUyN2QGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIkhSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBjb25maWd1cmFyIG8gcGFyw6JtZXRybyBNVl9UUENBTEVOBjsIVDoScmVzdWx0c19jb3VudGkC6AM%3D--c1b2d8ef96c2c15c66d5f307f57f35e125c6fb09)  
[RH - Linha Protheus - GPE - Como o sistema calcula a quantidade de horas/referência do DSR sobre as Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhlOBnVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBtWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NzQ4NTQxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1vLXNpc3RlbWEtY2FsY3VsYS1hLXF1YW50aWRhZGUtZGUtaG9yYXMtcmVmZXIlQzMlQUFuY2lhLWRvLURTUi1zb2JyZS1hcy1Ib3Jhcy1FeHRyYXMGOwhUOg5zZWFyY2hfaWRJIilmOWNlMmQ0ZC02ZWQxLTRmNGMtYmNlYi03ZjM3MWYwNmQ1YWEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJInZSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ29tbyBvIHNpc3RlbWEgY2FsY3VsYSBhIHF1YW50aWRhZGUgZGUgaG9yYXMvcmVmZXLDqm5jaWEgZG8gRFNSIHNvYnJlIGFzIEhvcmFzIEV4dHJhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--89019a1e3825266739002b19353601620fcfa147)  
[RH - Linha Protheus - GPE - Sistema calcula automaticamente desconto de DSR falta quando lançada verba de ID 0054-Falta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050719274-RH-Linha-Protheus-GPE-Sistema-calcula-automaticamente-desconto-de-DSR-falta-quando-lan%C3%A7ada-verba-de-ID-0054-Falta?source=search)  
[RH - Linha Protheus - GPE - De onde o sistema busca os dias para cálculo de DSR de hora extra, adicional noturno e outros DSRs](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2BKofUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBwmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NzkxMzUzNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRGUtb25kZS1vLXNpc3RlbWEtYnVzY2Etb3MtZGlhcy1wYXJhLWMlQzMlQTFsY3Vsby1kZS1EU1ItZGUtaG9yYS1leHRyYS1hZGljaW9uYWwtbm90dXJuby1lLW91dHJvcy1EU1JzBjsIVDoOc2VhcmNoX2lkSSIpN2MxOGZlZTItODUxMi00ZDQ2LTkwMzctOTMyOTdmMTJkMzU3BjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSITZHNyIGhvcmEgZXh0cmEGOwhUOhJyZXN1bHRzX2NvdW50aQKjAg%3D%3D--b5e02de9cf7af2dfdd8965b9b0c9037f9c394dde)
