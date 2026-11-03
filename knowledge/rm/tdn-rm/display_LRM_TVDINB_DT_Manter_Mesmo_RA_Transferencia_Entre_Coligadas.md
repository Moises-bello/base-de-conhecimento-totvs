---
content_hash: 69e4d751a5ec218695fd6891db1aa693b3fb2e346dea11abd6e5d63cb0d90e41
fetched_at: '2026-06-29T00:08:15.474721+00:00'
page_id: '244740295'
product: rm
source: tdn-rm
title: TVDINB_DT_Manter_Mesmo_RA_Transferencia_Entre_Coligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDINB_DT_Manter_Mesmo_RA_Transferencia_Entre_Coligadas
version: 114
---

# TRANSFERÊNCIA INTERNA ENTRE COLIGADAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Processo de transferência interna entre coligadas* |
| **Situação/Requisito:** | *O processo de transferência de alunos entre coligadas sempre gerava um novo RA para o aluno.* |
| **Solução/Implementação:** | *Inclusão de um parâmetro na etapa de informações de destino a fim de permitir a parametrização para o aproveitamento do RA de origem ou a geração de um novo.*  *O aproveitamento de RA é condicionado a utilização da parametrização de RA Global nas coligadas de Origem e Destino e, também, a não existência do código de RA*  *na coligada de destino.*  *Parâmetros necessários na coligada de origem e destino:*  ***Educacional | Configurações | Parâmetros***  ***15.01 - Secretaria | Geral 1/4 | "RA Global"***  *Parâmetro necessário no processo de transferência entre coligadas:*  ***Educacional | Atividades acadêmicas | Transferência interna entre coligadas***  ***Informações de dados de destino:***  ***"Manter o RA de origem, quando o destino não existir. (Utilização de RAGlobal na origem e no destino)"*** |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
