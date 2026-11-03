---
content_hash: 0077a53b20774b7ce7382882af6c151b3794b1b9cedbc127593091481a7fcc01
fetched_at: '2026-07-02T19:24:25.156208+00:00'
page_id: '499105921'
product: protheus
source: tdn-tec
title: Correção - TGrid com registros fora de ordem após redimensionamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499105921
version: 1
---

Correção - TGrid com registros fora de ordem após redimensionamento

|  |  |
| --- | --- |
| Situação | Caso o tamanho vertical do TGrid seja aumentado durante seu uso, novas linhas poderão ser adicionadas no espaço disponível e, após isso, os registros podem ser recriados em posições incorretas durante a navegação entre as linhas utilizando mouse ou teclado. |
| Ocorrência | O comportamento pode ser observado em algumas telas de cadastro do Protheus que possuam no rodapé um label com o totalizador de registros por coluna, sendo o label exibido ou ocultado dependendo da coluna que está selecionada. |
| Correção | Foi adicionada uma proteção no componente TGrid para quando ocorrer o redimensionamento. |
| Informações adicionais | * Referente ao chamado: PP-904 * Referente à ocorrência: ITEC-430 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.9 |
