---
content_hash: 9747dedcf08785b5363aa709ca5c55e8050e330bc0bc504aa9e33603da03f808
fetched_at: '2026-06-29T00:06:21.605577+00:00'
page_id: '223173262'
product: rm
source: tdn-rm
title: TTPZEA_DT_DataHoraInicioFim_Avaliacao_Incorreta
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPZEA_DT_DataHoraInicioFim_Avaliacao_Incorreta
version: 2
---

# EXECUÇÃO DE PROVA - WEB

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Execução de provas pelo executor web* |
| **Situação/Requisito:** | *Foi identificado que ao executar uma prova pelo portal a mesma não está armazenando corretamente na tabela 'BHISTORICO' a hora de início e fim da avaliação.* |
| **Solução/Implementação:** | *Foi identificado que o sistema estava fixando a data e hora de início e fim, sendo a final sempre com uma hora a mais, foi feito o ajuste para armazenar a data no momento do carregamento da avaliação e ao salvar ou finalizar salvar a data atual, assim salvando corretamente as datas de início e fim.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
