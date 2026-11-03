---
content_hash: a4407de0524b149df8110ae7f7ea19e7de64dca086a9ced0ee43c0dc7dda082d
fetched_at: '2026-06-29T00:08:18.689886+00:00'
page_id: '266966042'
product: rm
source: tdn-rm
title: TVRTXW_DT_Transferencia_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRTXW_DT_Transferencia_Funcionario
version: 111
---

# TRANSFERÊNCIA FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Transferência de Funcionário* |
| **Situação/Requisito:** | *Quando um funcionário possuía a flag Estava Recebendo seguro desemprego na admissão marcado, e era transferido para outra filial, o sistema copiava o parâmetro para a nova chapa, fazendo com que a nova chapa não fosse levada no CAGED mensal, devido a flag estar marcada.* |
| **Solução/Implementação:** | *Foi Ajustado o sistema para que ao transferir um funcionário que possua a flag marcada o sistema não copie este parâmetro, para que o novo funcionário possa ser levado normalmente no CAGED mensal.* |
| **Chamados relacionados:** | TVRTXW |

divs
