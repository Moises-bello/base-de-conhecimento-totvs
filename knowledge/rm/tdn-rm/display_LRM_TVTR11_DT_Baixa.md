---
content_hash: 6fe163c47c58f13c36dec0c00b3b7f69da41837d4a9a8ac8ddecadfc700d23b8
fetched_at: '2026-06-29T00:08:17.958652+00:00'
page_id: '260538760'
product: rm
source: tdn-rm
title: TVTR11_DT_Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVTR11_DT_Baixa
version: 113
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa |
| **Situação/Requisito:** | Ao selecionar vários lançamentos para baixa, o sistema não esta respeitando a opção marcada de "Data da Baixa igual ao vencimento". |
| **Solução/Implementação:** | Ajustado formulário da baixa, para que ao selecionar a opção de "Data da Baixa igual ao vencimento", a validação para verificar se a data da baixa e anterior a data de emissão, utilize a data de vencimento de cada lançamento em comparação a data de emissão, pois nesse caso, a data de baixa corresponderá a data de vencimento de cada lançamento. |
| **Conversores e Parâmetros:** | N/A. |
| **Chamados relacionados:** | N/A. |
| **Requisito (ISSUE):** | FIN000040 |

divs
