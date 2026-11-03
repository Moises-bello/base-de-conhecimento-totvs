---
content_hash: 0acc0e2886e56b1a54c8e0be2108233531bddefacaee574eedb989520233d9a2
fetched_at: '2026-06-29T00:08:39.902912+00:00'
page_id: '286024819'
product: rm
source: tdn-rm
title: 1194671 EDUCACIONAL01-1983 DT Criterios Desempate Inclusao Edicao Exclusao
type: documentation
url: https://tdn.totvs.com/display/LRM/1194671+EDUCACIONAL01-1983+DT+Criterios+Desempate+Inclusao+Edicao+Exclusao
version: 106
---

# ÁREA DE INTERESSE OFERTADA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Área de interesse ofertada* |
| **Situação/Requisito:** | *Foi identificado que ao tentar alterar uma área ofertada de um processo seletivo a alteração retorna um erro vazio e não completa a operação.* |
| **Solução/Implementação:** | ***Foi identificado que a situação é causada pois o processo seletivo já estava com data de inscrição encerrada e possui controle de vagas excedentes, ao alterar uma área ofertada para este tipo de situação o sistema tenta buscar candidatos excedentes para converter em inscritos, neste momento é feito uma validação no processo seletivo, como está fora do prazo de inscrição é gerado o erro, foi feito um ajuste para que se o processo seletivo estiver desativado ou com os prazos encerrados o sistema não efetuará a conversão de excedentes para inscritos.*** |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
