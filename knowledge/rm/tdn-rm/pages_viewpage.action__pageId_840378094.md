---
content_hash: 1f9497b2492fbff46c4950500895fffc3f97ce768d3d51946ef8c186d7866a07
fetched_at: '2026-06-29T00:11:50.300897+00:00'
page_id: '840378094'
product: rm
source: tdn-rm
title: FISCAL01-22339 - PIS e COFINS - Geração de Guia Automaticamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840378094
version: 7
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Obrigações Principais =>Período de Apuração => Processos => Geração de Guias Automaticamente |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-22339 |

## **02. SITUAÇÃO/REQUISITO**

Alteração para sistema recuperar valores cumulativos e não cumulativos para geração das guias DARF do PIS e COFINS

## **03. SOLUÇÃO**

Sistema recupera os valores cumulativos e não cumulativos do PIS e COFINS e utiliza esses valores para gerar as guias para pagamento.

O campo código da obrigação da aba Outros Dados passa a ser preenchido de acordo com o Tipo de Regime.  
Para regime cumulativo o campo deverá ser preenchido automaticamente com valor 08  
Para regime não cumulativo o campo deverá ser preenchido automaticamente com valor 12

OBS: A guia será gerada apenas quando os valores cumulativos e/ou não cumulativos forem maiores que zero.

Disponível à partir da biblioteca 12.1.2406
