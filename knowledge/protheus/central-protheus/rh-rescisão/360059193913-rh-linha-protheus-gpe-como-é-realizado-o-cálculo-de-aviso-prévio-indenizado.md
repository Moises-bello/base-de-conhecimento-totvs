---
article_id: 360059193913
category: RH - Rescisão
content_hash: d5c64206f31e361b885cb68c9456e8747e092ae3c25e3289b74916bfcc647d34
fetched_at: '2026-06-28T22:43:52.060083+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como é realizado o cálculo de Aviso Prévio Indenizado?
type: support-article
updated_at: '2025-06-16T17:51:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059193913-RH-Linha-Protheus-GPE-Como-%C3%A9-realizado-o-c%C3%A1lculo-de-Aviso-Pr%C3%A9vio-Indenizado
---

**Dúvida**Como o Sistema calcula o Aviso Prévio Indenizado na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**O sistema considera para o cálculo do Aviso Prévio indenizado o salário base do funcionário e caso não tenha uma verba relacionada ao ID 0250-Média Aviso Prévio Rescisão, o valor da média será calculado na verba de Aviso Prévio Indenizado (ID 0111), abaixo exemplo de cálculo:  
  
Salário base 2000,00  
Dias de aviso prévio indenizado 33  
  
Cálculo realizado pelo sistema: salário base / 30 \* dias total aviso  
2000,00 / 30 \* 33 = 2200,00  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097212954/mceclip0.png)  
  
Cálculo com médias de aviso, mas sem verba relacionada a verba de média de aviso (ID 0250), desta forma o sistema calcula as médias na verba de Aviso Prévio Indenizado (ID 0111):  
Demonstrativo de médias:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099518313/mceclip1.png)  
  
Salário base 2000,00  
Média aviso prévio 17,40  
Dias de aviso prévio indenizado 33  
  
Cálculo realizado pelo sistema: (salário base + médias aviso) / 30 \* dias total aviso  
(2000,00 + 17,40) / 30 \* 33 = 2219,14  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099518613/mceclip2.png)
