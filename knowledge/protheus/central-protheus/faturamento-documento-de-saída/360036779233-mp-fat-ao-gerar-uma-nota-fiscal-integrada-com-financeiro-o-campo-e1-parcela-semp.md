---
article_id: 360036779233
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 84dbe7293c9c514c2c42cdd59e145dae69edd188bba16c18794919d6b9f36390
fetched_at: '2026-06-28T22:38:45.138106+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Ao gerar uma Nota Fiscal integrada com financeiro o campo E1_PARCELA
  sempre será preenchido
type: support-article
updated_at: '2021-04-28T15:13:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036779233-MP-FAT-Ao-gerar-uma-Nota-Fiscal-integrada-com-financeiro-o-campo-E1-PARCELA-sempre-ser%C3%A1-preenchido
---

**Dúvida**

Ao gerar uma Nota Fiscal integrada com financeiro o campo E1\_PARCELA sempre será preenchido ?  
   
 **Ambiente**

Microsiga Protheus -  todas as versões.  
  
**Solução**

Será preenchido somente se houver mais de uma parcela no **SE1** (condição de pagamento com duas ou mais parcelas).

Verifique no Cadastro de Condição de Pagamento do Modulo Faturamento, se o campo **E4\_COND** (Atualizações - Cadastros - Condição de Pagamento no campo Cond. Pagto) possui mais de uma parcela.
