---
content_hash: f3aaaed1ae214c0bc9112e132b9200b9611c801e11f456c1fe2d0081f4387282
fetched_at: '2026-06-29T00:12:01.280714+00:00'
page_id: '892136422'
product: rm
source: tdn-rm
title: FISCAL01-24525 - Problema na integração do REINF C/ e-CAC - Alimentação automática
  de Rendimento Isento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=892136422
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24525 |

## **02. SITUAÇÃO/REQUISITO**

A tag VlrRendBruto não é gerado quando o valor da base de cálculo é igual ao valor original do lançamento, natureza de rendimento sem IR e Dados fiscais igual a Ajuda de custo.

Não gera as tags rendIsento

## **03. SOLUÇÃO**

1)O valor Bruto estava sendo gerado com o valor do campo Base de Cálculo para lançamentos de Rendimento Isento Nao Tributavel.   
A correção foi remover a lógica onde havia uma verificação na qual lançamentos de Rendimento Isento Não Tributável recebiam o valor da base de cálculo.

2) Inclusão de regra que verifica se o valor da base de cálculo é igual ao valor original do lançamento, verifica também se o Indicador de Isenção do lançament está preenchido e é diferente de Não se aplica.  
Dentro desse cenário o vlrIsento passa a ser preenchido com o valor original da nota. Dessa forma a tag tpIsencao passa a ser gerada.

Disponível à partir da biblioteca 12.1.2402
