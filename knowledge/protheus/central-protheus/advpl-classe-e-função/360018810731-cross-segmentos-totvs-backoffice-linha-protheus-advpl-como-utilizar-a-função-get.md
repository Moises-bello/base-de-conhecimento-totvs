---
article_id: 360018810731
category: ADVPL - Classe e Função
content_hash: 932bca76a718a0cad4195c7649a6ee4303bae93d6a3af4c2edfd3ca00df0be39
fetched_at: '2026-06-28T22:40:19.389048+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Como utilizar a
  função GetSXENum
type: support-article
updated_at: '2022-08-17T15:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810731-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-a-fun%C3%A7%C3%A3o-GetSXENum
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como utilizar a função GetSXENum?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Para que, por exemplo, o cadastro de clientes, traga na inclusão automaticamente o próximo número disponível, utiliza-se a seguinte sintaxe no **inicializador** padrão do campo **A1\_COD**:

```
GetSxeNum("SA1","A1_COD")
```

**Saiba mais**[GetSXENum - Último sequencial do campo da tabela](http://tdn.totvs.com/pages/releaseview.action?pageId=6814925)

[GETSXENUM()](http://tdn.totvs.com/pages/viewpage.action?pageId=24346933)
