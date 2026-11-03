---
article_id: 360048615034
category: Escrita Fiscal - Impostos - ICMS
content_hash: 08c6f55314e3375fdfd02b888fd77a9710af2308c2bc3788340d566ab98e58a9
fetched_at: '2026-06-28T22:39:25.656569+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Estorno de credito
  das notas fiscais de saídas destinadas a não Contribuintes - regra03
type: support-article
updated_at: '2021-07-20T13:11:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048615034-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Estorno-de-credito-das-notas-fiscais-de-sa%C3%ADdas-destinadas-a-n%C3%A3o-Contribuintes-regra03
---

**Dúvida**  
Como configurar o estorno de credito das notas fiscais de saidas destinadas a não Contribuintes ?  
   
 **Ambiente**  
Protheus - fiscal – A partir da versão 11.80  
  
**Solução**  
No regime atacadista o credito do icms st é realizado no momento da entrada da nota fiscal, porém se a venda não for para Não contribuinte deve ser realizado o estorno do credito.

Venda

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072143854/mceclip3.png)

Criar uma TES para Vendas com o tipo de cliente Revendedor / Solidário

Amarrar um código de reflexo

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073369753/mceclip4.png)

O estorno de credito será calculado sobre a nota fiscal de compras

Na TES o campo

Atualiza estoque = sim

Será demonstrado na rotina Fisa196

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073371393/mceclip5.png)
