---
content_hash: 7a21b97d5d5ca2d295a52f248a72d81a7984bc79fa81b8e0a1b421a7abe9df9a
fetched_at: '2026-06-29T00:08:04.404380+00:00'
page_id: '235569932'
product: rm
source: tdn-rm
title: TUPVS2_DT_Troca_Codigo_Secao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPVS2_DT_Troca_Codigo_Secao
version: 115
---

# TROCA DE CÓDIGO DA SEÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Troca de código da seção |
| **Situação/Requisito:** | Ao tentar realizar a troca de código da seção, o sistema está apresentando mensagem de violação de chave estrangeira. |
| **Solução/Implementação:** | Alteração na ordem em que as tabelas da base de dados são atualizadas com o novo código de seção, dessa forma, evita-se que ocorra a mensagem de violação de chave estrangeira. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUPVS2 |

divs
