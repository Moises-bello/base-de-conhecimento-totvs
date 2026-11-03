---
content_hash: 4758430bc193daed94d16952d58cd11c8148e400d74edf873a3e9e9ed95f8e4a
fetched_at: '2026-06-29T00:08:11.256581+00:00'
page_id: '242388041'
product: rm
source: tdn-rm
title: TVCRGF_DT_Validacao_Bolsa_Sequencia_Nao_Tem_Elementos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCRGF_DT_Validacao_Bolsa_Sequencia_Nao_Tem_Elementos
version: 110
---

# VALIDAÇÃO DE INCLUSÃO DE BOLSA - SEQUÊNCIA NÃO TEM ELEMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Inclusão de bolsa no contrato* |
| **Situação/Requisito:** | Na inclusão de uma bolsa, o sistema está emitindo o erro "A sequência não contém elementos" |
| **Solução/Implementação:** | Ajuste na validação de inclusão de bolsas no mesmo período que outras bolsas já existentes para não levantar um erro na conversão de parcela para data de vencimento em parcelas já excluídas. |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | TVDMXD |
| **Requisito (ISSUE):** | *N/A.* |

divs
