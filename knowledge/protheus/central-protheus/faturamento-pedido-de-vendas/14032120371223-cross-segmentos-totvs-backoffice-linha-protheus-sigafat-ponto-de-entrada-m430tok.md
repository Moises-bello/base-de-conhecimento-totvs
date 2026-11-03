---
article_id: 14032120371223
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a665cb13c17d27cf692a5c14bc67d85d162a55ee4117e684707da92eb3e937b2
fetched_at: '2026-06-28T22:38:41.319119+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: ' Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de
  Entrada M430TOK'
type: support-article
updated_at: '2023-04-20T13:09:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14032120371223--Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M430TOK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M430TOK - Validação de inclusão ou alteração de reservas**.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada M430TOK é utilizado para validar a inclusão ou alteração de reservas.  
  
**Exemplo**

```
#INCLUDE "Protheus.ch"  
  
User Function M430TOK()  
  
    Local lRet := .F.  
  
    Alert("Passou pelo ponto de entrada M430TOK")  
    lRet := .T.  
  
Return lRet
```

**Saiba Mais**

**[M430TOK - Validação de inclusão ou alteração de reservas](https://tdn.totvs.com/x/AIZn)**
