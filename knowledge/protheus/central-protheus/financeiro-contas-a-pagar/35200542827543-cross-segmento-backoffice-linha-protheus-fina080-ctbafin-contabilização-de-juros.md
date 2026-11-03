---
article_id: 35200542827543
category: Financeiro - Contas a Pagar
content_hash: 7f927068c6d35156766c1a8631048088bc097b31293801d799d7d4a477256986
fetched_at: '2026-06-28T22:38:06.916234+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA080 / CTBAFIN - Contabilização
  de Juros, Multa e Desconto
type: support-article
updated_at: '2025-09-25T19:56:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35200542827543-Cross-Segmento-Backoffice-Linha-Protheus-FINA080-CTBAFIN-Contabiliza%C3%A7%C3%A3o-de-Juros-Multa-e-Desconto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35200582378775) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar a contabilização de juros, multa e desconto em baixas realizadas de pagamentos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões.  
  
**Solução**  
A contabilização é realizada conforme o **LP 530**. Nesse processo, a contabilização ocorrerá na **linha que gerou movimentação bancária**, ou seja, onde consta o valor da baixa.

As demais linhas, que não geram movimentação bancária, são apresentadas apenas para facilitar a leitura dos movimentos. Importante destacar que **nem todos os movimentos que geram registros na SE5 atualizam movimentações bancárias na SE8**.

Para este cenário específico, será necessário considerar os seguintes campos da SE5 para contabilização separada na rotina de **Lançamento Padrão (CTBA080) - Campo CT5\_VLR01**

* **SE5->E5\_VLMULTA** – Valor de Multa
* **SE5->****E5\_VLJUROS** – Valor de Juros
* **SE5->****E5\_VLDESCO** – Valor de Desconto

Em resumo: a contabilização sempre se baseia nas movimentações que **atualizam os saldos bancários**.

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Descrições dos tipos de movimentações do campo E5\_TIPODOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022538171-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Descri%C3%A7%C3%B5es-dos-tipos-de-movimenta%C3%A7%C3%B5es-do-campo-E5-TIPODOC)
