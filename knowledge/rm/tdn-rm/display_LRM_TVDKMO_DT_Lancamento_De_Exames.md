---
content_hash: 5c345d1dcc03789619e8e0e429a60f30793a74c36cc0e923dd70dd557bc537d2
fetched_at: '2026-06-29T00:08:11.574762+00:00'
page_id: '243013067'
product: rm
source: tdn-rm
title: TVDKMO_DT_Lancamento_De_Exames
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDKMO_DT_Lancamento_De_Exames
version: 110
---

# LANÇAMENTO DE EXAMES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Lançamento de Exames |
| **Situação/Requisito:** | Além do cliente ter a opção de determinar o número de dias em que o exame poderá ser realizado, o sistema deverá emitir uma mensagem, caso o dia em que o exame for realizado seja maior que a data informada no parâmetro. Isso por que, caso a mensagem não seja apresentada, a impressão que fica é que o processo foi realizado com sucesso e na verdade não foi, pois o exame foi lançado com uma data superior ao parametrizado e permanecerá na agenda de exames. |
| **Solução/Implementação:** | Realizada pequena melhoria no processo de lançamento de exames através da agenda de exames de forma que o sistema exiba uma mensagem de confirmação caso a data de lançamento do exame seja superior ou inferior a data de agendamento levando em consideração a margem de dias que é parametrizável ("Margem de dias a considerar no lançamento de resultados pela agenda de exames"). |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVDKMO, TVE508 |
| **Requisito (ISSUE):** |  |

divs
