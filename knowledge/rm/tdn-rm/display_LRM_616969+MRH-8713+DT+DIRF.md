---
content_hash: 834e411660422d5fa7565a6febf6a2d6a2b73f672bca3997990f80db73a81c50
fetched_at: '2026-06-29T00:08:30.263996+00:00'
page_id: '272416641'
product: rm
source: tdn-rm
title: 616969 MRH-8713 DT DIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/616969+MRH-8713+DT+DIRF
version: 106
---

# Informe de Rendimentos Funcionários Transferidos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | DIRF |
| **Situação/Requisito:** | Quando um funcionário é transferido para outra filial (a demissão de uma chapa e admissão de uma nova ) e é gerado o informe de rendimentos para as mesmas, o sistema estava considerando somente a chapa demitida para buscar os valores do informe de rendimentos, desta forma não gerava o informe para a chapa que estava ativa.   Este erro acontecia somente quando o processo era executado para toda a base sem nenhum filtro, pois desta forma com a ordenação padrão do sql a chapa demitida era processada primeiro que a chapa ativa, causando assim o erro.   Quando o processo era gerado com filtros, a chapa ativa era listada primeiro e não causava o erro. |
| **Solução/Implementação:** | Foi ajustado o sistema para que ordene os funcionários, além da ordenação já realizado sobre o CPF, ordene também por data de transferência, desta forma a chapa ativa, com a última transferência realizada, será sempre a primeira a ser processada. |
| **Tickets relacionados:** | * + [616969](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22616969%22 "616969") |

divs
