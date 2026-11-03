---
article_id: 360018124312
category: ADVPL - Ponto de Entrada
content_hash: ae2087a7254c65dd6bcedd5b3c6804cf1358900f86ce81cd972ca817f6a96144
fetched_at: '2026-06-28T22:40:11.762578+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - MT140LOK Valida
  informações no pré-documento de entrada
type: support-article
updated_at: '2021-12-29T14:37:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018124312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MT140LOK-Valida-informa%C3%A7%C3%B5es-no-pr%C3%A9-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual ponto de entrada posso utilizar para validar pré-documento de entrada?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Este ponto de entrada tem o objetivo de validar as informações preenchidas no **aCols** de cada item do pré-documento de entrada.  
Exemplo, possibilita realizar um tratamento para os valores preenchidos, validações específicas de acordo com a necessidade existente.

```
User Function MT140LOK  
  
Local lRet:= ParamIXB[1]  
  
Local aTotais:= ParamIXB[2]  
  
Local aDesp:= ParamIXB[3]  
  
// Validações específicas a serem realizadas  
  
Return lRet
```

**Saiba Mais**[MT140LOK - Valida informações no pré-documento de entrada](http://tdn.totvs.com/pages/releaseview.action?pageId=6085509)
