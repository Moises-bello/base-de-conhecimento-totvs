---
article_id: 15919499252247
category: Call Center - Televendas
content_hash: 8611d9fa5a8346f1584a41e58e54e2308a5f5ea5b5e39af2e6dcb9745c2a0757
fetched_at: '2026-06-28T22:41:30.375686+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Ponto de Entrada
  TMKVFIM
type: support-article
updated_at: '2023-07-10T18:41:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15919499252247-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-Entrada-TMKVFIM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15919478512151) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **TMKVFIM - Pós-gravação do pedido de vendas**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Ponto de Entrada executado **após a gravação do pedido de vendas** no fechamento de um atendimento de Televendas.

**Obs.:** Ponto de entrada executado mesmo quando Tipo de Operação for diferente de Faturamento.  
  
**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
  
User Function TMKVFIM(cNumAtend, cNumPedido)  
  
    Alert('Passou pelo ponto de entrada TMKVFIM')  
  
Return
```

**Saiba Mais**

**[TMKVFIM - Pós-gravação do pedido de vendas](https://tdn.totvs.com/x/z5Jn)**
