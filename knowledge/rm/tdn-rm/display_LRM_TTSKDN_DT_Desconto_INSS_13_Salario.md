---
content_hash: b3a62bb6eb7054544626f18bedcc920639629250cba7a5f43a10dd2fa687b190
fetched_at: '2026-06-29T00:06:19.459410+00:00'
page_id: '219698081'
product: rm
source: tdn-rm
title: TTSKDN_DT_Desconto_INSS_13_Salario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSKDN_DT_Desconto_INSS_13_Salario
version: 3
---

# DIRF/Informe de Rendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | *Quando tem na movimentação o código de cálculo 108 e 91 o sistema deve considerar para o cálculo do inss de 13º apenas o código de cálculo 91, hoje ele está considerando os dois, duplicando o valor.* |
| **Solução/Implementação:** | *Alterado para considerar apenas o código de cálculo 108 quando não tiver o código de cálculo 91.* |
| **Chamados relacionados:** | *TTSKDN* |
| **Versões/Release:** | *11.82.43* |

divs
