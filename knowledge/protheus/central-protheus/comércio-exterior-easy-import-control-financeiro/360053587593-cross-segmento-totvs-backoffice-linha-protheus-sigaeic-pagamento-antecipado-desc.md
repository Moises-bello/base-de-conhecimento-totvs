---
article_id: 360053587593
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: e061657350b9ed8ea39b4ea0e0e58d50e6a979734cbdb088bd4d32c57399c67c
fetched_at: '2026-06-28T22:39:44.403375+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pagamento Antecipado:
  Desconto (WB_DESCO)'
type: support-article
updated_at: '2021-12-27T12:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053587593-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pagamento-Antecipado-Desconto-WB-DESCO
---

**Dúvida**O preenchimento do campo Desconto (WB\_DESCO), não replica para o financeiro, como é tratado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Para o módulo Easy Import Control a liquidação da parcela de câmbio de adiantamento (tanto da fase Purchase Order, quanto adiantamento ao fornecedor ou do tipo crédito) representa a inclusão do título a pagar do tipo PA/ NCF. Neste cenário de inclusão do título a pagar não existe a informação do desconto.  
Na issue DTRADE-4673 foi bloqueado a edição do campo de desconto (WB\_DESCO) para os câmbios do tipo adiantamento, conforme informado no primeiro parágrafo, temos uma questão conceitual que diferencia a operação realizada através do módulo SIGAEIC quando comparada a realizada no módulo SIGAFIN.  
  
Pacote da issue DTRADE-4673:  
12.1.27:<https://r.totvs.io/p/976419> ; 12.1.25:<https://r.totvs.io/p/976418> ; 12.1.23:<https://r.totvs.io/p/976417> ; 12.1.17:<https://r.totvs.io/p/976416> ;  
Boletim técnico da liberação: [DTRADE-4855 DT Compensação automática e desconto na rotina de câmbio](https://tdn.totvs.com/pages/viewpage.action?pageId=556396237 "Follow link")
