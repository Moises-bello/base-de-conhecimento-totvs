---
content_hash: 4af8853f129c58a798d1d1e7090c9d467bf7740ee97ffbd58796cd0645775a17
fetched_at: '2026-06-29T00:12:01.433028+00:00'
page_id: '895592350'
product: rm
source: tdn-rm
title: DT - S-1210 - Múltiplos vínculos de Funcionário e Autônomo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=895592350
version: 6
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1210 - Múltiplos Vínculos de Funcionário e Autônomo |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-7394](https://jiraproducao.totvs.com.br/browse/DRHROTRM-7394) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.254
* 12.1.2406.199
* 12.1.2410.130 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratar a geração do XML do evento S-1210 no mês de admissão de funcionários que atuam sob o regime de caixa e possuem outro vínculo como autônomo registrado no Totvs Gestão Financeira. Atualmente, nessa situação, o sistema não gera o XML do evento S-1210 referente ao pagamento do vínculo como autônomo registrado no Totvs Gestão Financeira no mês da admissão do funcionário.

## **04. SOLUÇÃO**

Foi ajustada a geração do XML do evento S-1210 para que o lançamento do autônomo seja considerado corretamente, nos casos em que o regime de caixa é aplicado no mês de admissão do funcionário.

## **05. DEMAIS INFORMAÇÕES**
