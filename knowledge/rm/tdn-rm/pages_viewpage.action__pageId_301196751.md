---
content_hash: 4d51ba1a9583f746d6293e8acc3cafdef3d4cbe3544ecfc566faf405236ff21b
fetched_at: '2026-06-29T00:08:43.171147+00:00'
page_id: '301196751'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-560 DT Regeração de lançamento com boleto cancelado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301196751
version: 96
---

# Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Regeração de Lançamento Financeiro |
| **Situação/Requisito:** | O TOTVS Gestão Financeira permite que o boleto de um lançamento originado do educacional seja cancelado ou excluído, ficando o lançamento sem nenhum boleto.  E, caso o lançamento seja regerado no TOTVS Educacional, o sistema não incluía o boleto novamente. |
| **Solução/Implementação:** | Realizamos uma evolução para que na regeração de um lançamento através do TOTVS Educacional, se o mesmo não tiver nenhum boleto ou todos os boletos estiverem cancelados o sistema automaticamente incluirá um boleto para o lançamento que está sendo regerado.  Observação: Quando este cenário ocorrer e na regeração o sistema tiver que incluir um novo boleto, não serão aplicadas as regras de agrupamento, sendo incluído um boleto para cada lançamento. Se desejar que as regras de agrupamento sejam aplicadas os lançamentos deverão ser cancelados e incluídos novamente |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
