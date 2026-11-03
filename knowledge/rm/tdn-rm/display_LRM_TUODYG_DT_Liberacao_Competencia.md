---
content_hash: 4d6823edd619ae9ddce439c06a5f23f261aeef450dc65031bbdd0eafb124ffdb
fetched_at: '2026-06-29T00:06:30.203072+00:00'
page_id: '235316821'
product: rm
source: tdn-rm
title: TUODYG_DT_Liberacao_Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TUODYG_DT_Liberacao_Competencia
version: 115
---

# LIBERAÇÃO DE COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Contrução e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Liberação de competência* |
| **Situação/Requisito:** | Caso for liberado a competência e for apresentado erro no processo, não está sendo efetuado o Rollback     Exemplo:     Competência atual 03/2016, ao Liberar a competência apresentou erro de histórico de funcionários, porém a competência atual virou para 04/2016 e o mês caixa continuou em 03/2016, só é possível efetuar o reparo da situação excluindo o Broker e reiniciando o serviço, corrigindo a competência atual para 03/2016. |
| **Solução/Implementação:** | *Otimizada liberação de competência, de forma que a rotina limpe o cache de parâmetros em caso de erro, evitando que o sistema mantenha a competência errada para os processos.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUODYG* |
| **Requisito (ISSUE):** |  |

divs
