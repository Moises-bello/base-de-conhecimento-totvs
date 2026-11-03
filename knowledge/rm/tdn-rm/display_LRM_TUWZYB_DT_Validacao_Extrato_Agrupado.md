---
content_hash: 4277d4f2a5d94b42b4b28df5096bd0297cb6205356aeb030614db79e9ee58645
fetched_at: '2026-06-29T00:08:07.917296+00:00'
page_id: '237397667'
product: rm
source: tdn-rm
title: TUWZYB_DT_Validacao_Extrato_Agrupado
type: documentation
url: https://tdn.totvs.com/display/LRM/TUWZYB_DT_Validacao_Extrato_Agrupado
version: 117
---

# Validação de extrato agrupado ao incluir / excluir bolsa retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Inclusão/Exclusão de bolsa retroativa* |
| **Situação/Requisito:** | *Ao conceder bolsa retroativa para uma parcela que foi baixada juntamente com outra parcela via Cheque o sistema está cancelando a baixa da parcela que não recebeu a bolsa retroativa* |
| **Solução/Implementação:** | Sistema passou a bloquear a inclusão / exclusão de bolsa retroativa para parcelas cuja baixa pertença a um extrato agrupado a fim de se evitar inconsistência.  Para que seja possível prosseguir com o processo a baixa da parcela deverá ser cancelada manualmente. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A* |

divs
