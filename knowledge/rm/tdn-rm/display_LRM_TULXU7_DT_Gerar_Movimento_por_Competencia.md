---
content_hash: bee01efee3afe382f1f0f60c156a3e3fc5a17936295bc9b7eaea142546238af1
fetched_at: '2026-06-29T00:06:29.345922+00:00'
page_id: '234606735'
product: rm
source: tdn-rm
title: TULXU7_DT_Gerar_Movimento_por_Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TULXU7_DT_Gerar_Movimento_por_Competencia
version: 117
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Gerar movimento por competência* |
| **Situação/Requisito:** | Quando o sistema estava com o parâmetro JOBSERVER3CAMADAS configurado para true a validação relacionada as abas do processo falhavam, pois neste cenário a LIB inclui uma nova aba para agendamento do processo. Como as validações estavam sendo realizadas pelos índices a inclusão desta nova aba trazia problema quando o processo era chamado da visão do contrato, neste contexto a aba de contratos era excluída e com a inclusão da de agendamento a validação de contratos era realizada incorretamente para aba de agendamento. |
| **Solução/Implementação:** | Ajuste na validação para considerar o nome da aba e não mais o índice. |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | NA |

divs
