---
article_id: 360051972233
category: ADVPL - Rotina Automática
content_hash: 10a0173ce2857de549b264beaf194e0e9781ae14670be7d630382bfa099810f5
fetched_at: '2026-06-28T22:40:23.973657+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Documento de Entrada:Informar
  data de validade de Lote via ExecAuto com Pedido de Compra
type: support-article
updated_at: '2023-06-07T20:37:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051972233-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Documento-de-Entrada-Informar-data-de-validade-de-Lote-via-ExecAuto-com-Pedido-de-Compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Por que o ExecAuto MATA103 não acata a data de vencimento do Lote passada via ExecAuto?

**Ambiente**Protheus – ADVPL – A partir da versão p12

**Solução**Detalhes do comportamento do campo **D1\_DTVALID**.

1) Ao informar uma Data de validade (**D1\_DTVALID**) com um **Lote** (**D1\_LOTECTL**) inexistente.  
1.1) Sem amarração de um Pedido de Compras, será acatado o data de validade que o usuário informou.  
1.2) Com amarração de um Pedido de Compras, será acatado **DATABASE + B1\_PRVALID**

2) Ao informar uma Data de validade (**D1\_DTVALID**) com um Lote (**D1\_LOTECTL**) existente.  
2.1) a Data de Validade (**D1\_DTVALID**) será a data de validade já cadastrada do **LOTE**.
