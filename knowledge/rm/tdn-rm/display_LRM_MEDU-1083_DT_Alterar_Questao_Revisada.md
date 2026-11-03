---
content_hash: ad240ff8361e4aab69fb6fec083c3c8f46749341266000f9bcfcc24b8b1291f6
fetched_at: '2026-06-29T00:08:22.203611+00:00'
page_id: '269083536'
product: rm
source: tdn-rm
title: MEDU-1083_DT_Alterar_Questao_Revisada
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1083_DT_Alterar_Questao_Revisada
version: 111
---

# QUESTÕES - REVISÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Avaliação e Pesquisa* |
| **Função:** | *Questões* |
| **Situação/Requisito:** | *Ao revisar uma questão que já foi executada e está anulada e também desativada, na questão revisada ao tentar ativar a o sistema exibe um erro de chave duplicada e não conclui a operação.* |
| **Solução/Implementação:** | *Foi identificado que no momento de validar se a questão já foi executada o sistema desconsidera incorretamente as questões que já foram revisadas, neste caso, como o sistema não identifica a questão executada é feito uma tentativa de inserir a questão novamente gerando assim o erro de chave duplicada. Foi feito o ajuste na validação e o sistema passou a validar corretamente as questões e assim concluir a operação com sucesso.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
