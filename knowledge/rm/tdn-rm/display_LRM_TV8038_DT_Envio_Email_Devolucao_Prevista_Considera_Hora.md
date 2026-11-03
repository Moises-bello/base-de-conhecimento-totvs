---
content_hash: 0b697c2b565c52f7ec8ff1fcbdf23c3ed86e0f060535443155e54b1af8c3ad0a
fetched_at: '2026-06-29T00:08:10.101155+00:00'
page_id: '240301394'
product: rm
source: tdn-rm
title: TV8038_DT_Envio_Email_Devolucao_Prevista_Considera_Hora
type: documentation
url: https://tdn.totvs.com/display/LRM/TV8038_DT_Envio_Email_Devolucao_Prevista_Considera_Hora
version: 111
---

# ENVIO DE E-MAILS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Leitura biométrica* |
| **Situação/Requisito:** | **No utilitário de envio de e-mails, ao utilizar o e-mail de devolução prevista, o sistema não localiza empréstimos com dava prevista de devolução com a hora superior ao acréscimo da data. Mesmo os empréstimos por dia, o sistema salva a hora prevista de devolução, porém desconsiderada na devolução, considerando somente o dia, porém no envio de e-mails de devolução prevista o sistema está considerando a hora, ou seja, se a devolução é para o dia seguinte as 18hs, o sistema faz a busca começando da data atual, acrescentando exatos 1 dia (ou mais) e mantendo a hora, por exemplo, se hoje é 22/06/2016 09:20, a busca com 1 dia irá considerar dia 23/06/2016 09:20, excluindo o empréstimos que são por dia que estão com data de devolução prevista para 23/06/2016 18:00.** |
| **Solução/Implementação:** | *Foi feito o ajuste para que a data sempre busque até o final do dia do período, assim encontrando todos os empréstimos do dia.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
