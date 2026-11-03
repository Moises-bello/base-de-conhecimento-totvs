---
article_id: 8990594273303
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 027c1b46c7a3a8bbde42126654f3c9fa4b247859d2088800ec1f1ba98ad077c0
fetched_at: '2026-06-28T22:38:42.442838+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MT440VLD
type: support-article
updated_at: '2022-09-19T20:15:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8990594273303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MT440VLD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MT440VLD - Inibir liberação automática de pedido de venda.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Ponto de entrada para validação da execução da rotina de processamento da liberação automática de pedido de venda.

O ponto de entrada inibe a execução da rotina.  
  
**Exemplo**

```
User Function MT440VLD()  
  
    Local lRet  := .T.  
  
    If MV_PAR08 == 2  
        Alert("Nao e permitido informar a (Pergunta 08: Liberar?) como (Credito). Seleciona a (Pergunta 08: Liberar?) como (Credito/Estoque)")  
        lRet:= .F.  
    EndIf  
  
Return lRet
```

**Saiba Mais**

**[MT440VLD - Inibir liberação automática de pedido de venda](https://tdn.totvs.com/x/boVn)**
