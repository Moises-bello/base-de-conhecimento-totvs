---
content_hash: af6e77ba581e4a2047b49948db5f53477fc52be25b6c2896d50089cc473740ca
fetched_at: '2026-06-29T00:08:05.122919+00:00'
page_id: '235584409'
product: rm
source: tdn-rm
title: TUQ379_DT_Geração_De_Lançamentos_Agrupados_Em_Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235584409
version: 118
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Geração de lançamentos* |
| **Situação/Requisito:** | *Ao gerar lançamentos em lote com agrupamento, pode ocorrer do sistema deixar de processar alguns lançamentos caso ocorra agrupamentos virtuais indevidos entre lançamentos novos e lançamentos que não tenham que ser processados. O boleto utilizado para agrupamento pode retroceder em caso de lançamentos gerados.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de geração de lançamentos, de forma que a lógica de agrupamento não faça com que alguns lançamentos não sejam gerados e não se tenha informações sobre o ocorrido no log do processo que foi executado, caso esteja sendo utilizado agrupamento para parcelas geradas.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *YFDST1* |
| **Requisito (ISSUE):** | *N/A* |

divs
