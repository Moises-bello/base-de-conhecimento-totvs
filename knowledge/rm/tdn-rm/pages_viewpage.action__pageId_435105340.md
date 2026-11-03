---
content_hash: e205fb17c782a4279c64b806b4674cedf0c38bdbe9eddc994d3ea898321ed9d7
fetched_at: '2026-06-29T00:09:49.653866+00:00'
page_id: '435105340'
product: rm
source: tdn-rm
title: Utilitários - Conversores - Conversor de parcelas importadas de outros sistemas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105340
version: 3
---

Este processo valida se existem vendas:

* com parcelas quitadas ou canceladas sem lançamento financeiro baixado ou cancelado correspondente;
* em preparação com plano de financiamento gerado;
* efetivadas com plano de financiamento não integrado;
* efetivadas com parcelas quitadas e não integradas;

A partir da versão 12.1.15 está disponível o processo que corrige a falta de integridade de dados gerados pela importação de dados de sistemas terceiros (legados). Esta importação geralmente ocorre durante o processo de implantação do sistema.

Toda parcela TIN deve ter um lançamento financeiro correspondente, nos casos onde a importação criou parcelas apenas no TIN sem um lançamento financeiro correspondente, será necessário o ajuste.

A ferramenta fará a geração de lançamentos financeiros correspondentes as parcelas quitadas ou canceladas no TIN , que não possuam lançamentos financeiros baixados ou cancelados correspondentes no TOTVS Gestão Financeira. Este processo a partir da versão 12.1.15 faz parte dos Pré-requisitos para a versão de revitalização do TOTVS Incorporação.
