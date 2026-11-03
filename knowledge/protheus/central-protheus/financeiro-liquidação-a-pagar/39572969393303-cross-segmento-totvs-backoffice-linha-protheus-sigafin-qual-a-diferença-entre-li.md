---
article_id: 39572969393303
category: 'Financeiro - Liquidação a Pagar '
content_hash: 98678374a76fb6fc9896f99f588a18772c68a3c5d5572c37f0f86e44f166626e
fetched_at: '2026-06-28T22:37:32.454329+00:00'
product: protheus
section_id: 35057594361879
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Qual a diferença
  entre liquidação e faturas no contas a pagar
type: support-article
updated_at: '2026-04-08T10:49:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39572969393303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Qual-a-diferen%C3%A7a-entre-liquida%C3%A7%C3%A3o-e-faturas-no-contas-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39572969383447) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Qual a diferença entre as rotinas de Fatura e Liquidação de títulos no módulo Contas a Pagar?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

A diferença entre **Fatura (FINA290)** e **Liquidação (FINA565)** está principalmente na finalidade de uso e na flexibilidade dentro do processo financeiro.

A rotina de **Fatura (FINA290)** é utilizada para **consolidar vários títulos em um ou mais novos títulos (parcelas)**, normalmente com o objetivo de organizar pagamentos, unificar vencimentos ou até mesmo reestruturar débitos existentes.  
Um ponto importante é que, após um título ser gerado por faturamento, **ele não poderá passar novamente pelo processo de faturamento**.

Já a **Liquidação (FINA565)** tem como objetivo a **quitação de títulos**, agrupando-os e gerando um novo título que representa esse pagamento.  
A principal diferença aqui é a flexibilidade: o título gerado na liquidação **pode ser utilizado em novas liquidações**, permitindo o reprocessamento (ou “re-liquidação”), se necessário.

---

**Resumo prático**

* **Fatura:** organização e consolidação de débitos (sem possibilidade de refaturamento)
* **Liquidação:** quitação de títulos, com possibilidade de reprocessamento futuro
