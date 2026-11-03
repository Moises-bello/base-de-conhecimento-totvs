---
content_hash: f34495d948bcced520b300496d6616550975edff0d5cc3a1bf2b9b2f167f169f
fetched_at: '2026-06-29T00:08:51.565470+00:00'
page_id: '337349387'
product: rm
source: tdn-rm
title: 1937364 DEDUINTEGRACOES-1484 DT Imprimir Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/1937364+DEDUINTEGRACOES-1484+DT+Imprimir+Boleto
version: 90
---

# IMPRIMIR BOLETO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Imprimir Boleto* |
| **Situação/Requisito:** | *Ao emitir o boleto, através do processo imprimir boleto, selecionando um relatório do reports o filtro da consulta SQL não é respeitado, estamos utilizando a fonte de dados através de consulta Sql.* |
| **Solução/Implementação:** | *Foi incluída uma validação no educacional para informar o cliente que os relatórios de boletos devem ter como fonte de dados principal uma tabela da base e esta tabela deve ser a tabela de boletos(FBOLETOS).*  *Caso o relatório não esteja configurado dessa forma o sistema irá apresentar a seguinte mensagem:* *A fonte de dados principal do relatório deverá ser do tipo Tabela da Base e o valor selecionado para essa fonte tem que ser a tabela de boletos (FBOLETO).* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
