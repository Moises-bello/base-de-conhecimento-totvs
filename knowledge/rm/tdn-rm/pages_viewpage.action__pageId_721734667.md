---
content_hash: c7894fdc17f86ec68ce4c75cfd1e7c54aaeb4f21549df8e54a8c2dfa55719a66
fetched_at: '2026-06-29T00:11:27.276309+00:00'
page_id: '721734667'
product: rm
source: tdn-rm
title: FISCAL01-18451 - DT - R-1000 - Data da transformação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721734667
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Federais - REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18893 |

## **02. SITUAÇÃO/REQUISITO**

Conforme a nova versão da EFD-Reinf, o Evento R-1000 deve gerar o campo **<****dtTransfFinsLucr****>** - Data da transformação de entidade beneficente de assistência social isenta de contribuições sociais em sociedade com fins lucrativos - Art. 13 - Lei 11096/2005.

## **03. SOLUÇÃO**

Através dos dados Fiscais da Filial, campo Classificação tributária, ao modificar a classificação de "Entidade Beneficiente/Isenta" para "PJ em Geral", é gravado um log de alteração da Filial, o campo será gerado com esta data de alteração.

Regra: Gerar somente se no histórico estiver o código referente a classificação "Entidade Beneficiente/Isenta" e no cadastro atual estiver a classificação "PJ em Geral"

Disponível a partir da biblioteca 12.1.2205
