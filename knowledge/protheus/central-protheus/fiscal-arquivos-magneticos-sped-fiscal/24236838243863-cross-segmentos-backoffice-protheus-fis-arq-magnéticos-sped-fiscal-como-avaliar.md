---
article_id: 24236838243863
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 359412d9b427684c12d861ef4cfbeeff376d0902c93c512918c21a4cf651492a
fetched_at: '2026-06-28T22:42:01.137964+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como avaliar Performance no Sped Fiscal?
type: support-article
updated_at: '2025-03-05T17:41:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24236838243863-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-avaliar-Performance-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24236810133655) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Quais os primeiros passos para avaliarmos **lentidão/performance** no processamento do **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Análise:**

Avalie se aumentando a quantidade de thread, o arquivo gera com menos tempo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=862601151>

Caso persista, para avaliarmos o incidente, encaminhar via ticket as informações abaixo:

**1 -** **LogProfiler** em modo **exclusivo** no ambiente:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar o LogProfiler](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhOH8jUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjE3MDU3NC0tQ3Jvc3MtU2VnbWVudG9zLUJhY2tvZmZpY2UtUHJvdGhldXMtRG9jLUVsZXRyJUMzJUI0bmljb3MtQ29tby1nZXJhci1vLUxvZ1Byb2ZpbGVyBjsIVDoOc2VhcmNoX2lkSSIpNTAzOTc3Y2QtMTRhMS00MzhkLWE5YjEtMTNhZjY2ZTNlNTY4BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQbG9ncHJvZmlsZXIGOwhUOhJyZXN1bHRzX2NvdW50aSE%3D--cd261141372c78c758c21f41038732ca682ef36a)

**2** - **Inspetor de Objetos**:

 [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como gerar o Inspetor de Objetos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwi521jVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBo2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MTY1NTk5My1Dcm9zcy1TZWdtZW50by1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FFU1QtQ29tby1nZXJhci1vLUluc3BldG9yLWRlLU9iamV0b3Mtbm8tUHJvdGhldXMGOwhUOg5zZWFyY2hfaWRJIilkNmE0MGRhMS1mMjZiLTQ4M2QtYjc5YS1kNmQ0NTIzZDM3MGIGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhhpbnNwZXRvciBkZSBvYmpldG9zBjsIVDoScmVzdWx0c19jb3VudGkClQI%3D--eae2afa2633c1e0d468582338ab2a137bd1afb18)

**Observação**: Efetuar a geração dos logs acima com as perguntas na geração do arquivo com

"**Gera Bloco K = Não**" e **"Processa histórico do Bloco K = Não".**
