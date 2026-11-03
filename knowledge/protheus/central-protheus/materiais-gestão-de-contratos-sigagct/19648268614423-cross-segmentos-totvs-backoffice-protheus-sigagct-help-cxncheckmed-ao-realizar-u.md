---
article_id: 19648268614423
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 216eb9282a04a8e8c2773e96a28441f86373c0b63dd6717e605dc903ad5bef17
fetched_at: '2026-06-28T22:37:22.940146+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CXNCHECKMED ao
  realizar uma medição.
type: support-article
updated_at: '2024-07-05T14:32:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19648268614423-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CXNCHECKMED-ao-realizar-uma-medi%C3%A7%C3%A3o
---

**Dúvida**

Help CXNCHECKMED ao realizar mais de uma medição parcial para a mesma competência em planilha de serviços.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19648247493911)

**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 12.1.33  
  
**Solução**

Para planilha de serviços somente **é possível realizar uma medição por competência**, independente do valor medido, ou seja, se medir parcialmente, o saldo restante não poderá ser medido novamente.

Caso isto ocorra, deverá ser realizada uma revisão de **Aditivo**, **Realinhamento** ou **Renovação** para redistribuição do saldo restante da(s) parcelas.

**Obs:**

Caso possua 2 parcelas na mesma competência e no mesmo mês conforme print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24672785390871)

Verifique se uma das parcelas foi medido parcialmente (No exemplo acima a parcela 16 foi medida parcialmente).

Ao Incluir a Medição (CNTA121) para competência 02/2025  trouxe a parcela 16 novamente para medir e nesse caso ocorreu o help 'CXNCHEKMED', pois, a parcela 16  já havia sido medida parcialmente.

Para que o erro não ocorra no exemplo acima, é necessário editar manualmente o campo parcela (CXN\_PARCEL) para para a infomração "17" que é a parcela que se deseja medir, pois como a parcela 17 ainda não foi medida , dessa forma não ocorre mais o erro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24672785397783)

***Saiba Mais:***

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os tipos de revisões disponíveis no Gestão de Contratos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-tipos-de-Revis%C3%A3o-dispon%C3%ADveis-no-Gest%C3%A3o-de-Contratos-)
