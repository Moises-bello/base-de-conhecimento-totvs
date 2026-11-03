---
content_hash: 9b980ce8c14780b1abf4bb8a9c4e96297cd2a6b3a026331f37ac9776f11d2d6c
fetched_at: '2026-06-29T00:08:29.759453+00:00'
page_id: '272163708'
product: rm
source: tdn-rm
title: 598448 MRH-8238 TPSE DIRF Assistência Médica Dependente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272163708
version: 105
---

# DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Emissão do registo TPSE. |
| **Situação/Requisito:** | O campo de valor do registro TPSE para DIRF em arquivo estava recebendo os valores dos registros DTPSE quando para o titular o valor era zerado e tem valores para o dependente. |
| **Solução/Implementação:** | O registro TPSE para DIRF em arquivo mesmo estando zerado passa a ser emitido caso haja registros DTPSE a ele relacionado com valores moires que zero. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 598448. |
| **Requisito:** |  |

divs
