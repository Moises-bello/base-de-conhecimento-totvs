---
content_hash: 3fdead034e9b8f0d74350cef177baa44ec25ac7968077affcb87682459ea2319
fetched_at: '2026-06-29T00:09:22.726564+00:00'
page_id: '422546014'
product: rm
source: tdn-rm
title: Comportamento nas Rotinas Fiscais
type: documentation
url: https://tdn.totvs.com/display/LRM/Comportamento+nas+Rotinas+Fiscais
version: 6
---

As obrigações acessórias foram evoluídas para que busquem os dados referentes aos Lançamentos Fiscais das tabelas históricas. Rotinas que foram alteradas:

* EFD Contribuições
* SPED Fiscal
* ECF - Escrituração Contábil Fiscal
* DAPI - Declaração de apuração e informações de ICMS.
* SINTEGRA
* TAF - TOTVS Automação Fiscal

Caso seja solicitada a geração da rotina para um Período Fiscal que já esteja "Fechado", o sistema buscará os dados das tabelas históricas não tendo impacto na geração das rotinas.

***Observação***: Nas rotinas fiscais EFD Contribuições, SPED Fiscal, ECF – Escrituração Contábil\Fiscal, TAF, DAPI, SINTEGRA para não serem geradas quando suas datas de geração estiverem compreendidas dentro de um período fiscal aberto/fechado parcial.
