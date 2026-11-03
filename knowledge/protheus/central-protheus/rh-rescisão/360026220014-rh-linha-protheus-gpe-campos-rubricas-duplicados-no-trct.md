---
article_id: 360026220014
category: RH - Rescisão
content_hash: 2611c2d0e2737ec6edfb5d7d7c229bba737e0bf99f1b7b207f58e0452ff26749
fetched_at: '2026-06-28T22:43:51.954838+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Campos (rubricas) duplicados no TRCT
type: support-article
updated_at: '2025-06-16T17:52:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026220014-RH-Linha-Protheus-GPE-Campos-rubricas-duplicados-no-TRCT
---

**Dúvida**Ao imprimir o TRCT, os valores de algumas verbas estão saindo duplicados em campos errados  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Este problema pode ocorrer por dois motivos: quando em uma verba que tem ID de cálculo o campo V.Homolognet esta preenchido indevidamente no cadastro da mesma, e quando uma verba esta parametrizada como DSR indevidamente, abaixo exemplos:  
  
1. Verbas com ID com o campo **V.Homolognet** preenchido **indevidamente**, esse campo deve ficar em **branco** para as verbas que tem **ID** de cálculo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040858594/mceclip0.png)  
  
2. Verbas configuradas **indevidamente** como sendo uma **verba de DSR** de outra verba, neste caso deverá ser listado TODO o cadastro de verbas e filtrar pela coluna **VERBA DRS (RV\_CODDSR),** onde a verba em questão se não for uma verba de DSR não pode estar neste campo de forma alguma:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040859014/mceclip1.png)  
  
Saiba mais:   
[RH - Linha Protheus - GPE - Como gerar relatório com todo o cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgUPlLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBk2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMDg5MDc3Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1nZXJhci1yZWxhdCVDMyVCM3Jpby1jb20tdG9kby1vLWNhZGFzdHJvLWRlLXZlcmJhcwY7CFQ6DnNlYXJjaF9pZEkiKTY3MTM5ZDdjLTRiYTItNGE0Zi1hODkyLWRlZTc3YzI5MTI0ZgY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiVFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIGdlcmFyIHJlbGF0w7NyaW8gY29tIHRvZG8gbyBjYWRhc3RybyBkZSB2ZXJiYXMGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--35441b49a5b1eed6f4cb4b7dcdf016d3c84aec8a)
