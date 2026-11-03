---
content_hash: 7a864f11f2417bfb75c606f6f46add989902611cd01639ae74111dc40251166b
fetched_at: '2026-06-29T00:08:17.257117+00:00'
page_id: '255754804'
product: rm
source: tdn-rm
title: TVRQSJ_DT_Log_Alterado_Manualmente_Vale_Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRQSJ_DT_Log_Alterado_Manualmente_Vale_Transporte
version: 115
---

# LOG DE CÁLCULO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Log de Cálculo* |
| **Situação/Requisito:** | Ao executar o recálculo do envelope de pagamento, no Log de Cálculo o evento de código de cálculo 32 automaticamente perde seu cálculo e é substituído pelo texto Valor lançado manualmente, sendo que o evento não foi lançado com valor manualmente.   Deveria continuar com o cálculo comum do sistema igual quando lança o evento ou então aparecer uma mensagem como por exemplo, Valor após recálculo. |
| **Solução/Implementação:** | Alterado a mensagem para 'Valor não recalculado:' para os CC 32 e 104. |
| **Chamados relacionados:** | *TVRQSJ* |

divs
