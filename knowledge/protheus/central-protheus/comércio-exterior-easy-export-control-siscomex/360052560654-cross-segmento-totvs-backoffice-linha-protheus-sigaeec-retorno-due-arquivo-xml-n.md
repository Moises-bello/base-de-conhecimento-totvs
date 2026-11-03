---
article_id: 360052560654
category: Comércio Exterior - Easy Export Control - Siscomex
content_hash: 962ced5103ce18c6c5c6ea045f949e19c16ec08738033dcba93a0a7f5e9d036b
fetched_at: '2026-06-28T22:37:00.545492+00:00'
product: protheus
section_id: 1500001538121
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Retorno DUE:
  Arquivo XML não atende as especificações definidas no XSD: CurrencyExchange'
type: support-article
updated_at: '2022-08-04T20:45:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052560654-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Retorno-DUE-Arquivo-XML-n%C3%A3o-atende-as-especifica%C3%A7%C3%B5es-definidas-no-XSD-CurrencyExchange
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Retorno DUE: Arquivo XML não atende as especificações definidas no XSD. cvc-complex-type.2.4.b: The content of element 'CurrencyExchange' is not complete. One of '{"urn:wco:datamodel:WCO:GoodsDeclaration:1":CurrencyTypeCode}' is expected., como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – A partir da versão 12.1.17  
  
**Solução**A Tag **CurrencyTypeCode** somente aceita código ISO da moeda, exemplo USD.

![](https://totvssuporte.zendesk.com/attachments/token/XEGAYV11oUGOqoMJPyEeWB4Iz/?name=inline823291799.png)

Por gentileza, verifique a moeda informada no Embarque campo EEC\_MOEDA e acesse o cadastro de Moedas em Atualizações \ Tabelas\ Moedas (EECAT135);  
1. Posicione na moeda utilizada no processo e selecione alterar;  
2.  Informe o campo Cod.ISO (YF\_ISO):  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085504334/mceclip0.png)

Após modificação, efetue a transmissão novamente da DUE.
