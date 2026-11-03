---
content_hash: e220d20b57c3537fd944f9b0472f3426826b11b93066fba1a9b365b7962068b8
fetched_at: '2026-06-29T00:10:47.621411+00:00'
page_id: '559502013'
product: rm
source: tdn-rm
title: 'DT- Criação do Encargo ''S - Base: incidência de INSS de 13o. salário Dissídio''.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=559502013
version: 2
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Encargo - Base: incidência de INSS de 13o. salário Dissídio |
| **Situação/Requisito:** | Não havia um encargo para a geração da base de INSS de 13° salário por dissídio. |
| **Solução/Implementação:** | Realizada a criação do tipo de encargo 'S - Base: incidência de INSS de 13o. salário Dissídio'. Este encargo irá considerar o valor do evento com código de cálculo 416. Este evento é lançado na tabela PFVERBASDIS quando é calculada uma diferença de 13° salário por dissídio.  Pode ser visualizado na aba de 'Verbas Geradas por Diferença’ da ficha financeira no mês/ano correspondente a diferença. |
| **Conversores e Parâmetros:** | Atualizador da Release 12.1.29. |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-8111](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-8111) |
| **Documento de Referência:** | [Encargos](https://tdn.totvs.com/display/LRM/Encargos+-+Folha+de+Pagamento)  [Código de cálculo 416](https://tdn.totvs.com.br/pages/viewpage.action?pageId=490325134) |
| **Pacote:** | N/A |
