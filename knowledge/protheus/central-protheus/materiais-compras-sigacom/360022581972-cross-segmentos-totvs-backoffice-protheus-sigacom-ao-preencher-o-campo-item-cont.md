---
article_id: 360022581972
category: Materiais - Compras (SIGACOM)
content_hash: 9ca96938387aced6921a7c8bdd0ccea9dd897567bf07bfe1653d76a8e1dc30f4
fetched_at: '2026-06-28T22:41:07.447211+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao preencher o campo
  Item Conta (D1_ITEMCTA) no Documento de Entrada (MATA103) deve preencher campo N3_SUBCTA
  ou N3_SUBCCON ?
type: support-article
updated_at: '2022-05-16T22:08:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022581972-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-preencher-o-campo-Item-Conta-D1-ITEMCTA-no-Documento-de-Entrada-MATA103-deve-preencher-campo-N3-SUBCTA-ou-N3-SUBCCON
---

**Dúvida**Ao preencher o campo Item Conta (**D1\_ITEMCTA**) no Documento de Entrada (MATA103) deve preencher campo **N3\_SUBCTA** ou **N3\_SUBCCON** ?  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**Por padrão o campo correto a ser alimentado é o **N3\_SUBCCON** quando o campo **D1\_ITEMCTA** é alimentado via Documento de Entrada e realizada contabilização integrada ao Ativo Fixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019988211/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020128812/mceclip3.png)

Caso necessário preencher o campo **N3\_SUBCTA** é possível através da rotina ATFA240.
