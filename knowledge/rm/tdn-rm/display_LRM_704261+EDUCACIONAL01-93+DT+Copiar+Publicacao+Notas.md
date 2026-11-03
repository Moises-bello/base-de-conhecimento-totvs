---
content_hash: 8d0fd16b5fc67cd2648508a9b9c1f8b6438c4daf0a43d03cd86d1d3043c59016
fetched_at: '2026-06-29T00:08:32.409078+00:00'
page_id: '273985264'
product: rm
source: tdn-rm
title: 704261 EDUCACIONAL01-93 DT Copiar Publicacao Notas
type: documentation
url: https://tdn.totvs.com/display/LRM/704261+EDUCACIONAL01-93+DT+Copiar+Publicacao+Notas
version: 105
---

# COPIAR PUBLICAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentação* |
| **Situação/Requisito:** | *No TOTVS Gestão Bibliotecária foi identificado um problema na cópia de publicação.* |
| **Solução/Implementação:** | *Foi identificado que o problema ocorre na publicação de origem quando algum dos campos que compõem as notas já tiveram valores e foram apagados. Os campos de notas são armazenados em outra tabela (LMEMO), quando o conteúdo na publicação é apagado, a publicação ainda faz referência ao registro desta tabela, por que ele não é excluído da tabela LMEMO, porém o conteúdo é salvo como nulo, no momento da cópia o conteúdo nulo gera um erro, sendo assim foi feito uma alteração no processo de cópia para ignorar o campo quando o valor do conteúdo é nulo mesmo que exista a referência na publicação de origem, sendo assim o valor só é de fato copiado quando existir conteúdo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
