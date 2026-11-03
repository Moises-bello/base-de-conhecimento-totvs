---
content_hash: c64f9f90c6cf2e2c8482ab7719d8e8a9db6d5c880e20de65166b9a0617f3bf77
fetched_at: '2026-06-29T00:10:47.617559+00:00'
page_id: '559501986'
product: rm
source: tdn-rm
title: 'DT- Criação do Encargo ''R - Base: incidência de INSS Dissídio''.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=559501986
version: 3
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Encargo - Base: incidência de INSS Dissídio |
| **Situação/Requisito:** | Não havia um encargo para a geração da base de INSS por dissídio. |
| **Solução/Implementação:** | Realizada a criação do tipo de encargo 'R - Base: incidência de INSS Dissídio'. Este encargo irá considerar o valor do evento com código de cálculo 415. Este evento é lançado na tabela PFVERBASDIS quando é calculada uma diferença salarial por dissídio.  Pode ser visualizado na aba de 'Verbas Geradas por Diferença’ da ficha financeira no mês/ano correspondente a diferença. |
| **Conversores e Parâmetros:** | Atualizador da Release 12.1.29 |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-8111](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-8111) |
| **Documento de Referência:** | [Encargos](https://tdn.totvs.com/display/LRM/Encargos+-+Folha+de+Pagamento)  [Código de cálculo 415](https://tdn.totvs.com.br/pages/viewpage.action?pageId=488864232) |
| **Pacote:** | N/A |
