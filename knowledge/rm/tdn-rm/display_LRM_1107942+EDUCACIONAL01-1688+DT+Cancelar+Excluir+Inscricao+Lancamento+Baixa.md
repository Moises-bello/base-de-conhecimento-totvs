---
content_hash: 9bf4985ac7a2ac8a87781b1373a6f6fbb541e2d43cc5856c6e56c96fccdf81d3
fetched_at: '2026-06-29T00:08:38.403752+00:00'
page_id: '285652894'
product: rm
source: tdn-rm
title: 1107942 EDUCACIONAL01-1688 DT Cancelar Excluir Inscricao Lancamento Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/1107942+EDUCACIONAL01-1688+DT+Cancelar+Excluir+Inscricao+Lancamento+Baixa
version: 102
---

# CANCELAR E EXCLUIR INSCRIÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cancelar / Excluir Inscrição com Lançamento baixado* |
| **Situação/Requisito:** | *Foi identificado que ao cancelar uma inscrição que possua lançamento baixado o sistema não permite cancelar a inscrição, assim como na exclusão também o sistema não permite alertando sobre o lançamento baixado.* |
| **Solução/Implementação:** | *Foi feito um ajuste no processo de cancelar inscrição, foi incluído um novo parâmetro para que o usuário opte ou não por cancelar uma inscrição mantendo o lançamento baixado em aberto. No processo de exclusão, não será possível realizar nenhuma alteração quando o lançamento estiver com baixa, assim caso o usuário deseje excluir uma inscrição, o mesmo terá que efetuar o cancelamento da baixa diretamente pelo gestão financeira e seus processo. Estas alterações são para garantir que um lançamento baixado não seja cancelado ou excluído diretamente pelo processo seletivo, assim garantindo que os processos do financeiro sejam executados (baixa, cancelamento, estorno, exclusão).* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
