---
content_hash: 1a5a37228a189f210686715b9c1243ab6633982bd81486c247d8f2dd0a2652d1
fetched_at: '2026-06-29T00:08:03.959279+00:00'
page_id: '235330865'
product: rm
source: tdn-rm
title: TUPLCK_DT_FopRescisaoData
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPLCK_DT_FopRescisaoData
version: 112
---

# DATASERVER FOPRESCISAODATA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | SaveRecord FopRescisaoData |
| **Situação/Requisito:** | Ao realizar o cadastro de uma rescisão através do SaveRecord do dataserver FopRescisaoData, é apresentado mensagem informando que a coluna TEMLICENCARHU não pertence à tabela PFUNC. |
| **Solução/Implementação:** | Adicionado validação que verifica a existência da coluna da tabela. Caso não exista, a mesma será adicionada. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUPLCK; TUPVNY |

divs
