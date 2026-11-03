---
article_id: 360017714792
category: ADVPL - Rotina Automática
content_hash: 6765ccb09a6a82d0461f0379cf45203a4a2b14e29c74ab08dfd685dbae4231f5
fetched_at: '2026-06-28T22:40:23.989674+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Erro  Execauto MATA410
  pedido de venda de complemento '
type: support-article
updated_at: '2021-12-29T14:04:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017714792-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Erro-Execauto-MATA410-pedido-de-venda-de-complemento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Sistema exibe a mensagem de erro abaixo, ao gerar uma nota fiscal complementar de despesas, com produto cadastrado corretamente.

```
HELP: A410COMPRQ  
  
  
Tabela SC6   
Erro no Item 1  
--------------------------------------------------------------------------------  
Num. Pedido - C6_NUM := 000001  
Item - C6_ITEM := 01  
Produto - C6_PRODUTO := 000001 < – Invalido
```

**Ambiente**Protheus – ADVPL – A partir da versão 12  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

Foi efetuado um ajuste no sistema, adicionando o campo **C5\_TPCOMPL** nas informações a serem enviadas na **MsExecAuto** de inclusão do pedido de venda complementar. Este campo irá levar o conteúdo **"1"** que refere-se a informação de que o pedido a ser gerado será um Complemento de Preço.

**Saiba Mais:**

[**Falha ao gerar Nota Fiscal Complementar de Despesas**](http://tdn.totvs.com/display/PROT/970434+MTRADE-1141+DT+Falha+ao+gerar+Nota+Fiscal+Complementar+de+Despesas)
