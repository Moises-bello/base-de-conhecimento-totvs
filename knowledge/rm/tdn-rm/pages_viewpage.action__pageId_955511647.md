---
content_hash: a366e155dbad6e28a6064c3f151f3f4cf7ef7fe29b500b8e4393528f5569449f
fetched_at: '2026-06-29T00:12:13.427415+00:00'
page_id: '955511647'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Tipo "24-Total Guia FGTS Digital" - Rescisão Complementar
  Tipo F na Guia Mensal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=955511647
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro - Tipo "24-Total Guia FGTS Digital" - Rescisão Complementar Tipo F na Guia Mensal |
| País: | Brasil |
| Issue: | [DRHROTRM-11604](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11604 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.257
* 12.1.2502.160
* 12.1.2506.104 e superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar o sistema para que, quando o funcionário possuir uma rescisão complementar no mesmo mês da data de demissão, o lançamento financeiro do tipo **"24-Total Guia FGTS Digital"** considere essa rescisão na modalidade MENSAL, conforme estabelecido no MOS do FGTS Digital.

## **04. SOLUÇÃO**

Foi implementada uma tratativa no produto para que, nas situações em que houver uma rescisão complementar do tipo **"F-****Verbas de natureza salarial ou não salarial devidas após o desligamento**” no mesmo mês da rescisão original, o valor correspondente seja considerado na guia Mensal do FGTS Digital, conforme previsto no MOS.

**Exemplo:**

* A rescisão do funcionário foi enviada em **15/04/2025**, por meio do evento **S-2299**.
* Posteriormente, em **30/04/2025**, foi enviada uma **rescisão complementar do tipo F**, por meio do evento **S-1200**.
* Após o envio desses eventos, o **retorno do evento S-5003** indica que os valores da rescisão complementar foram corretamente apurados na **modalidade MENSAL**, conforme demonstrado abaixo no XML.

A geração do lançamento financeiro utilizando a opção **"Gerar guia para o tipo: Rescisório"** foi realizada corretamente, contemplando todas as verbas relacionadas ao evento **S-2299**.

A geração do lançamento financeiro utilizando a opção **"Gerar guia para o tipo: Mensal"** foi realizada corretamente, contemplando as verbas relacionadas ao evento **S-1200**, conforme esperado.

## **05. DEMAIS INFORMAÇÕES**

[Lançamento Financeiro - Cadastro](https://tdn.totvs.com.br/display/public/LRM/Cadastros+Financeiros)
