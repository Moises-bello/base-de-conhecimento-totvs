---
content_hash: 0ddddab0a1bfd1b7adfad50f122a56f7fa688ee57f56232626869f1539a10585
fetched_at: '2026-06-29T00:08:10.750994+00:00'
page_id: '240979884'
product: rm
source: tdn-rm
title: TVBZ76_DT_DataInicial_Prova_Ranking_Diferente_Data_Periodo
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBZ76_DT_DataInicial_Prova_Ranking_Diferente_Data_Periodo
version: 118
---

# PROVAS - PERÍODOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Provas com períodos* |
| **Situação/Requisito:** | *Quando uma avaliação possui um período atribuído, o sistema salva a data de início e fim da execução da prova como sendo a data do período, e não de fato a data executada pelo candidato.* |
| **Solução/Implementação:** | *Foi feito uma modificação na execução das provas para que ao iniciar armazene a data de início e ao salvar ou finalizar envie junto com a prova a data de inicio e fim da real execução do candidato, não a data do período, que só é utilizada para garantir que a prova não seja executada fora da data válida do período* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVGIXO* |
| **Requisito (ISSUE):** | *N/A* |

divs
