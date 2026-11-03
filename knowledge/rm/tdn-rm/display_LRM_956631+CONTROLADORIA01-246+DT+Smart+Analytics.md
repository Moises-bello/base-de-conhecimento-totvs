---
content_hash: 17dd7d4d1f8474c3ac33e70c4c6893828e85eee443105e99842c581319155288
fetched_at: '2026-06-29T00:08:35.552435+00:00'
page_id: '281981712'
product: rm
source: tdn-rm
title: 956631 CONTROLADORIA01-246 DT Smart Analytics
type: documentation
url: https://tdn.totvs.com/display/LRM/956631+CONTROLADORIA01-246+DT+Smart+Analytics
version: 105
---

# Alterar as dimensões e os fatos para considerar apenas as coligadas ativas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | GooData |
| **Função:** | Smart Analytics |
| **Situação/Requisito:** | Algumas das informações de fatos (tabelas de valores), como por exemplo, Contabilidade (HL9 e HLC), mandam os dados com valores de coligadas “INATIVAS”. Nesse caso precisaria ser feito uma alteração no extrator para desconsiderar as informações relacionadas com as coligadas inativas. |
| **Solução/Implementação:** | Foram realizadas as seguintes alterações:  1 - As dimensões e os fatos do módulo contábil foram alterados para considerar apenas as coligadas ativas. 2 - A instancia, parametrizada no Totvs Business Analytics, passou a ser retornada pelos fatos e dimensões. 3 - Os conceitos do módulo contábil passaram a buscar a instância parametrizada pelo usuário. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
