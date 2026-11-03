---
article_id: 20198207485847
category: Financeiro - Comissão
content_hash: 5a1b22aefeb57ca2f8de4ba2000ed077a4b2bca6bf2b7b7d07cd1ccdf07a6859
fetched_at: '2026-06-28T22:37:50.715855+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA440 - Recálculo
  da comissão em moeda estrangeria na compensação.
type: support-article
updated_at: '2025-07-30T20:25:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20198207485847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA440-Rec%C3%A1lculo-da-comiss%C3%A3o-em-moeda-estrangeria-na-compensa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20198232824983) Tempo aproximado para leitura: **00:00:30 min****Dúvida**Quando realizar o recalculo da comissão em moeda estrangeira, o valor da comissão é alterado.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA440 - disponível a partir do release 12.1.2210

**Solução**

Foi criado o parâmetro **MV\_COMTXMO**, cuja finalidade é definir qual **moeda** será utilizada como base para o **cálculo da comissão**. O recálculo poderá considerar:

* **1** – A comissão será calculada com base na **Taxa da Moeda cadastrada (SM2)**.
* **2** – A comissão será calculada com base na **Taxa da Moeda do movimento de baixa**.

**Saiba mais**

[Utilização do parâmetro MV\_COMTXMO](https://tdn.totvs.com/pages/releaseview.action?pageId=806774400)
