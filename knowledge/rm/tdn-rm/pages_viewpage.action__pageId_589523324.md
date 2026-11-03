---
content_hash: e57024c093b38e357247412467ca88b10c4e31e43e22c7205fd21260d56e887c
fetched_at: '2026-06-29T00:10:53.896064+00:00'
page_id: '589523324'
product: rm
source: tdn-rm
title: Calendário 2021
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589523324
version: 6
---

* Alterado a Rotina da DIRF para que passe a considerar Lançamentos Fiscais com CFOP do tipo fiscal e com o Tributo “IRRFPJ” ou “CSRF”, e CFOP's específicos de Transporte.

  Ex.: 1.350, 1.351, 1.352, 1.353, 1.354, 1.355, 1.356, 1.360, 2.351, 2.352, 2.353, 2.354, 2.355, 2.356

* Realizado ajuste no mês de geração dos valores na rotina DIRF, onde se tratando do tributo COSIRF o mesmo será gerado no mês da **"Data previsão de baixa",** caso esteja com o campo preenchido, senão, será considerada a DATALF conforme comportamento anterior.

* Realizada alteração no layout da DIRF para se adequar aos novos registros criados **RIDAC** e **RIBMR**.
* Criação dos registros RIDAC e RIBMR no Gerador de Saídas.
* Com a alteração realizada, os valores que antes eram agrupados no registro RIO passam a ser gerados em registros diferentes de acordo com o motivo do Indicador de Isenção (DIRF) selecionado no Lançamento Financeiro.
  + **Se Motivo Isenção for igual a** "**Não se Aplica**"
    - Valor do lançamento deve ir para o registro **RIO**
  + **Se Motivo Isenção for igual a** "**Diária e Ajuda de Custo**"
    - Valor do lançamento deve ir para o registro **RIDAC** no seu respectivo mês
  + **Se Motivo Isenção for igual a** "**Bolsa de Estudo Recebida por Médico Residente**"
    - Valor do lançamento deve ir para o registro **RIBMR** no seu respectivo mês
