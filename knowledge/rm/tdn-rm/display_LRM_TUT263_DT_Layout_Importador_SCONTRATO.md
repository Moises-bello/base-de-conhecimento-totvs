---
content_hash: 296839d30a16e4d50da57b582ace2dfc8737f03ebf82662fc052206d0ec4edc9
fetched_at: '2026-06-29T00:08:06.539808+00:00'
page_id: '236591758'
product: rm
source: tdn-rm
title: TUT263_DT_Layout_Importador_SCONTRATO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUT263_DT_Layout_Importador_SCONTRATO
version: 111
---

# LAYOUT IMPORTADOR - SCONTRATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Layout Importador - SCONTRATO* |
| **Situação/Requisito:** | *Ao ajustar o arquivo txt com as informações relacionada ao Contrato do aluno, o dado referente ao STATUS da tabela SCONTRATO, está induzindo o usuário ao erro. Atualmente a validação está seguindo a estrutura: STATUS: S=ATIVO: N=CANCELADO. Se informarmos S (entende-se como Ativo), mas na verdade determina que o contrato está cancelado e ao importar segue a mesma estrutura.* |
| **Solução/Implementação:** | *Alterado layout do campo STATUS da tabela SCONTRATO para S= CANCELADO N= NÃO CANCELADO.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
