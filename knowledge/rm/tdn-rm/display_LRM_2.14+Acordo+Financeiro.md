---
content_hash: fafe1b8247681760c24c1e37d1dbd1ff761ec91d2f4d2e9f12a7c89e0b567f4f
fetched_at: '2026-06-29T00:10:42.853477+00:00'
page_id: '547861451'
product: rm
source: tdn-rm
title: 2.14 Acordo Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/2.14+Acordo+Financeiro
version: 11
---

No Módulo Financeiro são registrados os acordos financeiros firmados com alunos/clientes. Para isso, existe a funcionalidade de acordo onde são registradas as negociações e geradas as “novas” dividas a partir deste acordo. Acordo financeiro é uma modalidade de negociação, que consiste em formalizar um novo plano de pagamento para o(s) Lançamento(s) Financeiro(s). através do *template de acordo* será possível determinar descontos, acréscimos, juros, parcelamentos, prazos, entre outros. Com essas informações disponíveis o usuário poderá escolher o melhor Plano para gerar o Acordo.

Premissas para o processo Acordo**:**

* Os lançamentos devem ter a mesma Natureza (pagar/receber).
* Os lançamentos devem ter mesmo Tipo Contábil, exceto no caso de combinação entre lançamento "Contábil"  e "Baixa Contábil", que são considerados equivalentes no contexto do Acordo.
* Os lançamentos devem ter o mesmo Aplicativo de Origem.
* O lançamento deve estar com status "Em Aberto"  ou "Parcialmente Baixado".
* O lançamento não pode estar Faturado.
* O lançamento não pode ser um Vencimento de Fatura.
* O lançamento não pode estar Vinculado (Adiantamento, Nota de Crédito e Devolução).
* O lançamento não pode ter um Cheque emitido.
* O lançamento não pode estar Bloqueado (baixa e alteração).
* O lançamento não deve ser uma Baixa Pendente\* .
* O lançamento não deve ser Previsão (tipo de documento com classificação Previsão).

  Recursos Adicionais

* [Associação do Template de Acordo](https://tdn.totvs.com/pages/viewpage.action?pageId=607323048)
* [Geração do Acordo](https://tdn.totvs.com/pages/viewpage.action?pageId=551424631)
