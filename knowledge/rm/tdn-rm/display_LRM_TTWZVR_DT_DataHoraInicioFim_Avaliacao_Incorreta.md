---
content_hash: 21c83727129d25d43a4f2fce32c885d7ff072067d39dc2356a237df1235ee827
fetched_at: '2026-06-29T00:06:21.610521+00:00'
page_id: '223173277'
product: rm
source: tdn-rm
title: TTWZVR_DT_DataHoraInicioFim_Avaliacao_Incorreta
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWZVR_DT_DataHoraInicioFim_Avaliacao_Incorreta
version: 1
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
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
