---
article_id: 360037912214
category: RH - Folha de Pagamento
content_hash: 801866215a2db6da807d712fa0fd2c07fd7907df7fcb833605ca3676eb07449d
fetched_at: '2026-06-28T22:44:14.809785+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o parâmetro MV_SALMGRP
type: support-article
updated_at: '2025-04-22T21:10:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037912214-RH-Linha-Protheus-GPE-Como-utilizar-o-par%C3%A2metro-MV-SALMGRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17501501578007) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Como utilizar o parâmetro MV\_SALMGRP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Existe no sistema um parâmetro chamado **MV\_SALMGRP**, este parâmetro é responsável por apresentar a verba de **id 0670** no calculo da folha ou no calculo de 13º salário. Para ajustar o mnemônico conforme a necessidade acesse o **Configurador SIGACFG** em **Ambiente > Cadastros > Parâmetros (CFGX017)** e pesquise pelo parâmetro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594546895383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594577711255)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594546897559)  
  
O correto é levar esta informação sempre no calculo de 13º salário, portanto o parâmetro deverá sempre ficar desabilitado. Caso tenha uma rescisão, a informação será apresentada na mesma.  
  
A configuração com **S** foi desenvolvida para empresas que ganharam **Liminar na Justiça para tal dedução mensal**, sem a liminar não cabe a empresa optar por essa dedução, visto que por lei sempre será deduzido no próprio cálculo do 13º salário da funcionária.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31594577712919)  
  
A **SEFIP** também não tem tratamento para dedução mensal, em seu leiaute a informação deve ser prestada nas seguintes situações:   
- na competência 13, referente ao valor pago durante o ano.   
- na competência da rescisão do contrato de trabalho (exceto rescisão por justa causa), aposentadoria sem continuidade de vínculo ou falecimento )   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050692833)

**Saiba Mais:**[RH - Linha Protheus - GPE - Parâmetros utilizados para geração da SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgX2rgtfQc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBl2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzgyMzQyMTkzOTU2MDctUkgtTGluaGEtUHJvdGhldXMtR1BFLVBhciVDMyVBMm1ldHJvcy11dGlsaXphZG9zLXBhcmEtZ2VyYSVDMyVBNyVDMyVBM28tZGEtU0VGSVAGOwhUOg5zZWFyY2hfaWRJIiliN2U1MjdjNS1jODAwLTQ1NGEtYWEwZC0wZjYxYjM3N2ZjNWUGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg9NVl9TQUxNR1JQBjsIVDoScmVzdWx0c19jb3VudGkCGAU%3D--172b1ff0fae35d8ea0f51897dee9dd8343faadd2)  
[RH - Linha Protheus - GPE - Limite de dedução do Salário Maternidade para a GPS](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjrnbrSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzczMTA1MS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTGltaXRlLWRlLWRlZHUlQzMlQTclQzMlQTNvLWRvLVNhbCVDMyVBMXJpby1NYXRlcm5pZGFkZS1wYXJhLWEtR1BTLQY7CFQ6DnNlYXJjaF9pZEkiKWI3ZTUyN2M1LWM4MDAtNDU0YS1hYTBkLTBmNjFiMzc3ZmM1ZQY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX1NBTE1HUlAGOwhUOhJyZXN1bHRzX2NvdW50aQIYBQ%3D%3D--dd04f640b816d22c2cffd8a2b09dd38b4cd5f126)  
[RH - Linha Protheus - GPE - O sistema está lançando a dedução de 1/12 avos de 13° salário no cálculo da licença maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhDWbvSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB3Wh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzc3OTAxMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTy1zaXN0ZW1hLWVzdCVDMyVBMS1sYW4lQzMlQTdhbmRvLWEtZGVkdSVDMyVBNyVDMyVBM28tZGUtMS0xMi1hdm9zLWRlLTEzLXNhbCVDMyVBMXJpby1uby1jJUMzJUExbGN1bG8tZGEtbGljZW4lQzMlQTdhLW1hdGVybmlkYWRlBjsIVDoOc2VhcmNoX2lkSSIpYjdlNTI3YzUtYzgwMC00NTRhLWFhMGQtMGY2MWIzNzdmYzVlBjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPTVZfU0FMTUdSUAY7CFQ6EnJlc3VsdHNfY291bnRpAhgF--a83d70e6a83634e9e5ea23aa222ca6f7214ca0ae)   
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do 13º quando há Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXgw1NSQk6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB2Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEwMjEwNDI5OTkzODc5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFpcy1zJUMzJUEzby1hcy1kb2N1bWVudGElQzMlQTclQzMlQjVlcy1yZWxhY2lvbmFkYXMtYW8tYyVDMyVBMWxjdWxvLWRvLTEzJUMyJUJBLXF1YW5kby1oJUMzJUExLUxpY2VuJUMzJUE3YS1NYXRlcm5pZGFkZQY7CFQ6DnNlYXJjaF9pZEkiKWNkMTY1MzgxLWNmNDktNDc4Yy1hZTdiLWQyNTYwYTY0ZThmZQY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiFTEzwrogbWF0ZXJuaWRhZGUGOwhUOhJyZXN1bHRzX2NvdW50aQIyBA%3D%3D--ed04fb952471f631ec960a67484ac94f696c5731)
