---
article_id: 360034657374
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 22388cb2af867a6dc287b36781cf3c163933bcbbf80e9512c2f288080cfee9b5
fetched_at: '2026-06-28T22:38:38.635033+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso da TES Inteligente
  no Pedido de Venda
type: support-article
updated_at: '2024-02-09T12:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034657374-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-da-TES-Inteligente-no-Pedido-de-Venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16778900582295) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**

Cadastrado o **TES** **inteligente** (**MATA089**) no sistema, porém, ao informar o produto (**MATA010**) no pedido de venda (**MATA410**),  não esta sugerindo o **TES** (**MATA080**)conforme parametrização.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

O uso do TES inteligente está condicionado a inserção do tipo de operação no item do pedido, campo **C6\_OPER**, sem a inclusão do tipo de operação, o sistema não fará a sugestão do TES automaticamente.

O sistema somente fará sugestão de TES automático no pedido com a inclusão do produto, se o TES em questão estiver no cadastro do produto sugerido, campo **B1\_TS**, entretanto, se for efetuar o uso do TES associado ao produto, não se faz necessário trabalhar com TES inteligente.
