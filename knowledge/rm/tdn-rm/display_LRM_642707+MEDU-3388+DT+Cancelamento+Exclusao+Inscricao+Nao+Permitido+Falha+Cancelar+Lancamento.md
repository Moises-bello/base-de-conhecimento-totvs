---
content_hash: bc76e0cfc27e09c9b00f25a0174c7c1709313979e35a195358da5faae239a594
fetched_at: '2026-06-29T00:08:30.872254+00:00'
page_id: '272699240'
product: rm
source: tdn-rm
title: 642707 MEDU-3388 DT Cancelamento Exclusao Inscricao Nao Permitido Falha Cancelar
  Lancamento
type: documentation
url: https://tdn.totvs.com/display/LRM/642707+MEDU-3388+DT+Cancelamento+Exclusao+Inscricao+Nao+Permitido+Falha+Cancelar+Lancamento
version: 110
---

# CANCELAMENTO E EXCLUSÃO DE INSCRIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cancelamento e exclusão de inscrição* |
| **Situação/Requisito:** | *Foi identificado um erro ao cancelar ou excluir uma inscrição no processo seletivo que tenha lançamento, retornando um erro genérico* |
| **Solução/Implementação:** | *Foi identificado que o erro é causado por uma inconsistência na montagem do contexto pela contabilidade, pois o parâmetro utilizado como código do usuário é passado nulo em todas as partes do processo seletivo, financeiro e contabilidade, porém o código do usuário é passado separado como referência em todos so métodos porém não é utilizado. Foi feito o ajuste do lado do processo seletivo para enviar o código do usuário na lista de lançamentos a serem cancelados, assim o financeiro monta o contexto corretamente que envia a lista de cancelamento corretamente para o contabilidade.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
