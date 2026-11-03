---
content_hash: 7ca62f33891c170763ca1dc82480becf4fb55dde76d0a82a141da1da383f773e
fetched_at: '2026-06-29T00:06:29.602310+00:00'
page_id: '234614094'
product: rm
source: tdn-rm
title: TULQMJ_DT_Parametros_emissao_recibos
type: documentation
url: https://tdn.totvs.com/display/LRM/TULQMJ_DT_Parametros_emissao_recibos
version: 118
---

# PARÂMETROS PARA EMISSÃO DE RECIBOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Parâmetros para Emissão de Recibos* |
| **Situação/Requisito:** | Sistema não emitia mensagem exigindo que o usuário informasse o relatório padrão para emissão de recibo caso o mesmo tivesse marcado a opção de emitir recibos. O problema acontecia para recibos de empréstimo, renovação, devolução e multa. |
| **Solução/Implementação:** | Foi criada crítica no parametrizador para tratar a situação, emitindo mensagem ao usuário quando o relatório padrão não estiver preenchido e um dos parâmetros de emitir recibo estiver. |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | NA |

divs
