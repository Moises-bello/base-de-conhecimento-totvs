---
content_hash: adff5ab43b36ba5048cf381c29f1218390c2cc94fb0407ce4795989461e63294
fetched_at: '2026-06-29T00:08:23.396677+00:00'
page_id: '270084461'
product: rm
source: tdn-rm
title: MRH-3478_DT_Lookup_Chapas_SelFunc_Recalculo
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3478_DT_Lookup_Chapas_SelFunc_Recalculo
version: 109
---

# ERRO NO LOOKUP DE CHAPAS DA SELEÇÃO DE FUNCIONÁRIOS DO RECÁLCULO DA FOLHA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Recálculo da Folha* |
| **Situação/Requisito:** | *Na seleção de funcionários do módulo Folha Mensal/Lançamentos/Executa recálculo, está retornando erro no lookup de chapas, quando é selecionado um funcionário que possui o campo RESCISAOCALCULADA nulo na PFUNC.*  *No filtro do lookup está tratando para aceitar somente RESCISAOCALCULADA igual a zero.* |
| **Solução/Implementação:** | *Tratar na consistência do filtro do lookup de chapas da Seleção de Funcionários para aceitar RESCISAOCALCULADA igual a zero ou RESCISAOCALCULADA igual a nulo.* |
| **Chamados relacionados:** | MRH-3478 |
| **Requisito (ISSUE):** | MRH-3478 |

divs
