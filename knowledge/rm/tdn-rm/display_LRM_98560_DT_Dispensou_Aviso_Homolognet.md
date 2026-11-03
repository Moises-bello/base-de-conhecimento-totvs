---
content_hash: 1d481148afcaac45db66f1b72599ed7cb4ebc6b2d6e4f3613f6e298b42bd737e
fetched_at: '2026-06-29T00:08:21.691302+00:00'
page_id: '269068590'
product: rm
source: tdn-rm
title: 98560_DT_Dispensou_Aviso_Homolognet
type: documentation
url: https://tdn.totvs.com/display/LRM/98560_DT_Dispensou_Aviso_Homolognet
version: 98
---

# HOMOLOGNET

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Geração do Homolognet* |
| **Situação/Requisito:** | *Ao realizar a geração do Homolognet o sistema estava sempre preenchendo a TAG TPEmpregadoDispensadoAvisoPrevio, porém de acordo com o manual do homolognet esta TAG deve ser preenchida somente quando a rescisão for iniciativa do empregado.* |
| **Solução/Implementação:** | *Foi Ajustado o sistema para preencher a TAG *TPEmpregadoDispensadoAvisoPrevio somente quando o tipo de rescisão for 3 - Iniciativa do Empregado com Justa Causa e 4 - Iniciativa do Empregado sem Justa Causa, para as demais rescisões TAG não deve ser enviada para o arquivo.** |
| **Chamados relacionados:** | 98560 |

divs
