---
content_hash: 1bebb8b3aeee67bc8f060ea97b52bea49163592ef3024540987b9a5e55e72a6c
fetched_at: '2026-06-29T00:08:24.233788+00:00'
page_id: '270895586'
product: rm
source: tdn-rm
title: MRH-3881_DT_Cancelamento_Movimento_HistoricoRRA
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3881_DT_Cancelamento_Movimento_HistoricoRRA
version: 110
---

# CANCELAMENTO DE MOVIMENTO DEVE EXCLUIR HISTÓRICO DE RRA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cancelamento de Movimento* |
| **Situação/Requisito:** | *O módulo de cancelamento de movimento deverá verificar se está sendo cancelado movimentação de RRA e deletar o registro da tabela PFHSTRRA, bem como deletar os registros da tabela PFDEPMOV, referente ao RRA.* |
| **Solução/Implementação:** | *Tratamento no Cancelamento de Movimento para excluir o registro da tabela PFHSTRRA, quando cancelar eventos de um envelope com diferença de RRA.* |
| **Chamados relacionados:** | MRH-3881 |
| **Requisito (ISSUE):** | MRH-3881 |

divs
