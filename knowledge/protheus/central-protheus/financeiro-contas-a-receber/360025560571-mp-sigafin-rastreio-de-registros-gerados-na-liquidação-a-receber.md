---
article_id: 360025560571
category: Financeiro - Contas a Receber
content_hash: f4005e75fbfdd0cf40775f5633edfe7b0d8ccf7f8aded08a102e7806d4d79269
fetched_at: '2026-06-28T22:38:15.108056+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - Rastreio de registros gerados na liquidação a receber
type: support-article
updated_at: '2022-06-28T16:49:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025560571-MP-SIGAFIN-Rastreio-de-registros-gerados-na-liquida%C3%A7%C3%A3o-a-receber
---

**Dúvida**Como é feito o rastreio dos títulos gerados a partir da liquidação a receber?  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
   
**Solução**O rastreio é feito através do campo **E5\_DOCUMEN** (registro da baixa do título principal) que irá armazenar o numero da liquidação  nos títulos gerados **(E1\_NUMLIQ)**, e que por sua vez irá vincular na tabela **FO0**,  **FO0\_NUMLIQ**, e **FO0\_PROCESS** e este irá amarrar os demais itens das tabelas **FO1** **( FO1\_PROCESS)** (registros utilizados para gerar a liquidação) e **FO2** **(FO2\_PROCESS)** ( títulos gerados).

![image2018-2-23_9-26-26.png](http://tdn.totvs.com/download/attachments/340363674/image2018-2-23_9-26-26.png?version=1&modificationDate=1519390015000&api=v2)

**Importante**Essa nova versão da rotina FINA460, com a descontinuidade da rotina de faturas a receber, não faz uso do campo E1\_FATURA. Deste modo, caso possua customizações com este campo, deverá readequá-las.
