---
article_id: 360008266192
category: ADVPL - Classe e Função
content_hash: 56854367b392006e4025b798f3ce18b6b07b708987fff4653b6565da08341785
fetched_at: '2026-06-28T22:40:14.373464+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - APAPI64 e APAPI
type: support-article
updated_at: '2022-01-11T22:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008266192-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-APAPI64-e-APAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Na Integração com o Excel ocorre o seguinte erro.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015216592/mceclip0.png)**![](https://totvssuporte.zendesk.com/attachments/token/g4dfLeqksv3JAJ83GaImastK6/?name=erro+na+integracao+com+Excel.JPG)  
Outros erros   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012758711/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**O Erro APAPI ocorre no Office 365 , conforme documentação não suporta os componentes de integração.

[Microsoft Office 365](http://tdn.totvs.com/display/teces/Office+365)

```
Suite office não suportada pela falta dos componentes utilizados na integração direta com o executável.
```

O Erro APAPI64 ocorre devido a utilização do Office 2016 64 bits e o appserver de 32 bits ou seja são arquiteturas diferentes   
  
**Solução**A versão homologada do Pacote Office conforme documentação publicada no TDN no link abaixo, é o Office Professional 2016 32-bit.  
  
**Saiba mais**[Office homologado para uso em integrações](http://tdn.totvs.com/display/tec/SmartClient+-+Office)
