---
content_hash: 2a7eb4dd049162c1c7bb5838ad2b7665017ad4da2a46667bb68800ce3e494fd6
fetched_at: '2026-06-29T00:08:06.968947+00:00'
page_id: '236598477'
product: rm
source: tdn-rm
title: TUL375_DT_Acordo_Estouro_SqlDatetime
type: documentation
url: https://tdn.totvs.com/display/LRM/TUL375_DT_Acordo_Estouro_SqlDatetime
version: 117
---

# GERAR ACORDO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Gerar acordo* |
| **Situação/Requisito:** | Ao gerar acordo para lançamentos oriundos do Educacional é exibida a seguinte mensagem de erro: Não foi possível gerar acordo para os lançamentos oriundos do Módulo Educacional Estouro de SqlDateTime. Deve estar entre 1/1/1753 e 31/12/9999. Somente ocorria quando houve migração do Ensino Basico para ClassisNet (tabela EDESCLAN campo DTALT em branco). |
| **Solução/Implementação:** | Otimizado geração de acordo, quando o lançamento veio de uma migração do Ensino Básico para o ClassisNet. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUWDX1* |
| **Requisito (ISSUE):** | *N/A* |

divs
