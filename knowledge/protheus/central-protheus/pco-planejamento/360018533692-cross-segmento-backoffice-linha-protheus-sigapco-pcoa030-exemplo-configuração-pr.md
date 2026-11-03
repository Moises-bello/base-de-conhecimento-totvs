---
article_id: 360018533692
category: PCO - Planejamento
content_hash: 36c4b066651c1c1796624cddbaf0898fb539317c326020478e8597cfdda3368f
fetched_at: '2026-06-28T22:37:07.612045+00:00'
product: protheus
section_id: 1500001551002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA030 - Exemplo configuração
  processo 000052 item 08 Rateio por Centro de Custo?
type: support-article
updated_at: '2023-11-21T13:41:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018533692-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA030-Exemplo-configura%C3%A7%C3%A3o-processo-000052-item-08-Rateio-por-Centro-de-Custo
---

**Dúvida**Exemplo configuração processo 000052 item 08 Rateio por Centro de Custo?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

Para que seja possível configurar o processo 000052-Pedido de Compras Item 08 - Rateio por CC

Utilize como exemplo a seguinte configuração no campo (Vlr.Lanto) :

*Posicione("SC7",1,SCH->CH\_FILIAL+SCH->CH\_PEDIDO+SCH->CH\_ITEMPD,"C7\_TOTAL") \* SCH->CH\_PERC/100*

**Importante**

Essa configuração poderá ser alterada mediante a necessidade do cliente. Este link trata-se apenas de um possível exemplo de utilização/configuração deste item/processo.
