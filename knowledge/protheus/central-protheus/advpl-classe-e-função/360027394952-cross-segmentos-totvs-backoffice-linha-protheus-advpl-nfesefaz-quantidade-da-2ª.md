---
article_id: 360027394952
category: ADVPL - Classe e Função
content_hash: aa535d2978d45a36bb407b5ddab8f51e012bd5b062f022506f03cd091787db1e
fetched_at: '2026-06-28T22:40:20.538934+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Nfesefaz quantidade
  da 2ª unidade de medida
type: support-article
updated_at: '2022-06-01T18:17:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027394952-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Nfesefaz-quantidade-da-2%C2%AA-unidade-de-medida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Na minha SC6 - SC9 e SD2 a quantidade na segunda unidade de medida está saindo no valor inteiro, porém quando gero a nota pelo nfesefaz.prw essa quantidade sai com um valor quebrado (4 casas decimais).  
Como eu faço para que ele gere a D2 um valor inteiro?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**No fonte NFESEFAZ.prw a quantidade da 2a. Unidade de Medida é tratada na função **retQtd2UM** verifique a variável **nCONVDIP** que é o fator de conversão:

```
Static Function retQtd2UM( lNoImp2UM, cCFOPExp, cCFOP, nCONVDIP, nQUANT)
```

Obs: Como o fonte esta disponível é necessário o Debug e as alterações são responsabilidades do cliente.
