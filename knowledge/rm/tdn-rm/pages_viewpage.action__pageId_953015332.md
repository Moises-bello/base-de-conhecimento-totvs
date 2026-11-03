---
content_hash: c11d5e7b5aab36d94f397bfcaa89ae1c89891eeefd2dabfa096c3fd2ecbb6068
fetched_at: '2026-06-29T00:12:10.864942+00:00'
page_id: '953015332'
product: rm
source: tdn-rm
title: FISCAL01-25876 - Registro 0200 - Não podem ser gerados GTINs iguais para fatores
  de conversão de produtos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953015332
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25876 |

## **02. SITUAÇÃO/REQUISITO**

Ao validar o SPED Fiscal é apresentada a inconsistência abaixo, no Registro 0200, campo 4 COD\_BARRA:  
“Não podem ser gerados GTINs iguais para fatores de conversão de produto” 

A inconsistência ocorre porque foi informado o mesmo código de barras no campo 04 do Registro 0200 e no campo 04 do Registro 0220, o que infringe as validações estabelecidas pelo manual do SPED.

## **03. SOLUÇÃO**

Ajuste no cache do código de barras, antes filtrava por coligada e codProduto o ajuste incluí a unidade de medida no filtro.

Disponível à partir da biblioteca 12.1.2410
