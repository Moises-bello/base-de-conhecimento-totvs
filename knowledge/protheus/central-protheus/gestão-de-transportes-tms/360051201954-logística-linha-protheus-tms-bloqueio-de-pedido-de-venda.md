---
article_id: 360051201954
category: Gestão de Transportes (TMS)
content_hash: d7441124f379b4b40513fc97d47f451618556638ffbf755fd8d2a451a27f9377
fetched_at: '2026-06-28T22:45:27.283532+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Bloqueio de Pedido de Venda
type: support-article
updated_at: '2021-09-10T13:54:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051201954-Log%C3%ADstica-Linha-Protheus-TMS-Bloqueio-de-Pedido-de-Venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Como funciona o bloqueio de pedido de venda no **TOTVS Logística TMS**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões

**Solução**O bloqueio de pedido de venda ocorre quando:

* No cadastro do **Cliente - MATA030,** na aba **Vendas**, o campo **Risco - A1\_RISCO = Risco E - Liberação manual**. Quando definido dessa forma, é necessário realizar a liberação de crédito na rotina **Lib. Credito - MATA450**;
* O cliente possui um bloqueio de cliente na rotina **Bloqueio Cliente - TMSA630.**O bloqueio pode ser definido como **Comercial** ou **Operacional**. Quando definido desta forma, é necessário realizar a liberação de crédito na rotina **Lib. Credito - MATA450**e a liberação de transporte na rotina **Lib. Transporte - TMSA640**.

No **TOTVS Logística TMS**, o pedido de venda é bloqueado no momento do cálculo do documento. Por isso, após efetuar a liberação do pedido de venda, é necessário efetuar o **recálculo do documento**.
