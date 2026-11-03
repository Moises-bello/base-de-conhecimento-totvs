---
article_id: 39572991159063
category: Financeiro - Faturas a Pagar
content_hash: 9ca20ebd98d13b8807c9a52314b7422a2c863d8bca81c0988419af7bea7993f5
fetched_at: '2026-06-28T22:37:34.280513+00:00'
product: protheus
section_id: 35057532916375
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Qual a diferença
  entre liquidação e faturas no contas a pagar
type: support-article
updated_at: '2026-04-08T10:49:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39572991159063-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Qual-a-diferen%C3%A7a-entre-liquida%C3%A7%C3%A3o-e-faturas-no-contas-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39572991147927) Tempo aproximado para leitura: **00:05:00 min**  
  
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
