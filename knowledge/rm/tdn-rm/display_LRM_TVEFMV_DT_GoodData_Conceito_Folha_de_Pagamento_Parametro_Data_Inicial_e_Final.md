---
content_hash: d70686fe960f90cb5f470e326398e2c7f3252921ad39fa095051b039f65850fb
fetched_at: '2026-06-29T00:08:12.216734+00:00'
page_id: '243640391'
product: rm
source: tdn-rm
title: TVEFMV_DT_GoodData_Conceito_Folha_de_Pagamento_Parametro_Data_Inicial_e_Final
type: documentation
url: https://tdn.totvs.com/display/LRM/TVEFMV_DT_GoodData_Conceito_Folha_de_Pagamento_Parametro_Data_Inicial_e_Final
version: 116
---

# EXTRATOR GOODDATA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Extrator GoodData - Conceito Folha de Pagamento* |
| **Situação/Requisito:** | *O conceito de Folha de Pagamento não é construído na estrutura de DataServer como os demais. O novo módulo de Plano de Execução do GoodData repassa os parâmetros de Data Inicial e Final através de ownerData enviado para cada DataServer, que não é suportado pela execução de DLL, como é construído este conceito.* |
| **Solução/Implementação:** | *Foi implementado um contorno para a configuração para que as datas iniciais e finais fossem consideradas normalmente na extração* |
| **Chamados relacionados:** | *TVEFMV* |

divs
