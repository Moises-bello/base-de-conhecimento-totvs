---
content_hash: 45c09969f7cbf15ac4e9e75965e86d84ae24c170f054446092b0c91febfc79c8
fetched_at: '2026-06-29T00:06:26.387330+00:00'
page_id: '225262523'
product: rm
source: tdn-rm
title: TUFCLW_DT_Contabilização_Indevida_Aumentos_E_Cancelamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225262523
version: 120
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | *Ao gerar contabilização por competência utilizando o novo modelo, pode ocorrer de não ter havido cancelamento ou aumento no valor total de serviços, porém um erro acumulado de arredondamento, pode fazer com que uma diferença de 1 centavo, possa ser entendida como cancelamento ou aumento, gerando contabilização dessa diferença indevidamente.* |
| **Solução/Implementação:** | *Foi realizado ajuste no sistema para validar a alteração no valor total de serviços, a partir do valores de contrato, antes de calcular se houve diferença, pois a soma das parcelas mensais já contabilizadas pode acumular um erro de arredondamento.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *TUHLH0* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
