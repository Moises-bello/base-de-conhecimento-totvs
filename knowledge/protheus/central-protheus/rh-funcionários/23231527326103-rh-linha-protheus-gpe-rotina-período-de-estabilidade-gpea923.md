---
article_id: 23231527326103
category: RH - Funcionários
content_hash: 4270e65f2aac213e96b802431c8164cc3e118bb0ee509173907131e60f92e0a9
fetched_at: '2026-06-28T22:43:28.682376+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Rotina Período de Estabilidade - GPEA923
type: support-article
updated_at: '2025-09-12T18:18:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23231527326103-RH-Linha-Protheus-GPE-Rotina-Per%C3%ADodo-de-Estabilidade-GPEA923
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23231527425943) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como funciona a rotina GPEA923 - Período de Estabilidade   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**

A rotina GPEA923 possibilita o empregador informar e consultar as datas que o funcionário esteve em período de estabilidade e por qual motivo.  
  
**1.** Acesse: **Atualizações/ Funcionários/ Período de Estabilidade****2.** Informe a data de inicio, término e o motivo, conforme tabela de Estabilidade (S053).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23231527302295)  
  
Após salvar o cadastro, o sistema alimenta o campo **Dt. Vto. Estab (RA\_DTVTEST)** automaticamente no cadastro de funcionário.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23231527303703)  
  
Esta data servirá de **alerta** no cálculo de uma rescisão para funcionário com estabilidade.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23231756414231)

A tabela utilizada para armazenamento destas informações será a RFX.

**Saiba Mais:**[RH - Linha Protheus - GPE - Cálculo de estabilidade CIPA em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwghwc%2FUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjY3MDc1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRlLWVzdGFiaWxpZGFkZS1DSVBBLWVtLXJlc2NpcyVDMyVBM28GOwhUOg5zZWFyY2hfaWRJIik1OGFhZDYwMy1kNGEwLTQ4YTYtYWM2Ny1kYjM0OGFlNWFmYjAGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhFlc3RhYmlsaWRhZGUGOwhUOhJyZXN1bHRzX2NvdW50aQGJ--20e4df539bb49befc48582234934a79c07e8bf5e)[RH - Linha Protheus - GPE - Como cadastrar estabilidade após retorno de Ausência](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwh9Y5DUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0ODUxODAxMy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jYWRhc3RyYXItZXN0YWJpbGlkYWRlLWFwJUMzJUIzcy1yZXRvcm5vLWRlLUF1cyVDMyVBQW5jaWEGOwhUOg5zZWFyY2hfaWRJIik5ZTM4YWYyNC1kNzRhLTRhZjQtYmZiZi01Y2M2MDk2OTFiZjUGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg9SQV9EVFZURVNUBjsIVDoScmVzdWx0c19jb3VudGkCuAE%3D--99ee8833eb514ea5e200915e519bde69e1e09ed0)[RH - Linha Protheus - GPE -O Sistema realiza o cálculo de estabilidade em caso de demissão após o retorno de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi6s30%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDg3ODg5MjItUkgtTGluaGEtUHJvdGhldXMtR1BFLU8tU2lzdGVtYS1yZWFsaXphLW8tYyVDMyVBMWxjdWxvLWRlLWVzdGFiaWxpZGFkZS1lbS1jYXNvLWRlLWRlbWlzcyVDMyVBM28tYXAlQzMlQjNzLW8tcmV0b3Juby1kZS1mJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTU4YWFkNjAzLWQ0YTAtNDhhNi1hYzY3LWRiMzQ4YWU1YWZiMAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEWVzdGFiaWxpZGFkZQY7CFQ6EnJlc3VsdHNfY291bnRpAYk%3D--463b249f1f35c93ba71f483daa0578967ba39d68)
