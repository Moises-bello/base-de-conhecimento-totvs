---
content_hash: 4bcaab8e0372e4d7beed15fd4243dea4c824c5b52c0d0cc4cd85c2dcb0471d87
fetched_at: '2026-06-29T00:12:07.314629+00:00'
page_id: '923183489'
product: rm
source: tdn-rm
title: FISCAL01-25334 - Sped Fiscal - Erro durante carregamento dos dados do lançamento.
  Identificador da situação tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=923183489
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Sped Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25334 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o Sped Fiscal do período Janeiro de 2025 o log de geração retorna a seguinte inconsistência: "não foi possível gerar o arquivo do SPED Fiscal".   
Motivo: Erro durante carregamento dos dados do lançamento. Identificador da situação tributária 36435621  
Erro: Object reference not set to an instance of object

## **03. SOLUÇÃO**

 Ajuste no código para realizar tratamento para referencia nula, para lançamentos que possuam CFOP com o seguinte parâmetro marcado: Soma ICMS por dentro do valor contábil e não possuam nenhum tributo cadastrado.

Disponível a partir da biblioteca 12.1.2406
