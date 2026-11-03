---
content_hash: f49d1920e2ca52b3ac3058b8ab90a5323cd3a4bbf6ccc9044a5ff6fa66c43f3a
fetched_at: '2026-06-29T00:11:25.607275+00:00'
page_id: '714212756'
product: rm
source: tdn-rm
title: FISCAL01-18380 - DT BlocoK Simplificado/Registro K010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=714212756
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18380 |

## **02. SITUAÇÃO/REQUISITO**

Implementação do Modelo Simplificado de geração do BlocoK

## **03. SOLUÇÃO**

Foi incluída uma nova opção para a Geração do BlocoK - "Simplificado"

Ao gerar o Sped Fiscal com esta opção selecionada os registros K210 e K260 não serão gerados, para as outras opções o comportamento se mantem o mesmo.

Implementada a geração do Registro K010 para ano referência maior que 2023.

Este registro informa qual foi a forma de geração escolhida.

Indicador de tipo de leiaute adotado:   
0 – Leiaute Simplificado   
1 - Leiaute Todos os Registros - Completo   
2 – Leiaute Restrito aos Saldos de Estoque - K200; K280

Disponível a partir da biblioteca 12.1.34
