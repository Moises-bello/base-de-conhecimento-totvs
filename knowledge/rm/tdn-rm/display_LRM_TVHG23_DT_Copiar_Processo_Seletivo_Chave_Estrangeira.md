---
content_hash: 0a04c7d7e25182768dc9864a03103ca913ed2dc2efc886c49c690ca3c2426086
fetched_at: '2026-06-29T00:08:13.975554+00:00'
page_id: '244436008'
product: rm
source: tdn-rm
title: TVHG23_DT_Copiar_Processo_Seletivo_Chave_Estrangeira
type: documentation
url: https://tdn.totvs.com/display/LRM/TVHG23_DT_Copiar_Processo_Seletivo_Chave_Estrangeira
version: 118
---

# COPIAR PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Copiar processo seletivo* |
| **Situação/Requisito:** | *O processo de cópia de Processos Seletivos está retornando um erro não tratado de chave estrangeira e não conclui a operação.* |
| **Solução/Implementação:** | *A mensagem é gerada quando o processo seletivo é de outra filial, com a opção marcada de ser visível em todas as filiais e possui categoria. O campo categoria é copiado diretamente do processo seletivo de origem, porém, a categoria está vinculada a filial, como o processo seletivo de origem é de outra filial, o erro de chave estrangeira é retornado. Foi feito o ajuste para que a categoria não seja copiada diretamente, assim será exibido um campo na tela do processo para informar qual a categoria da filial corrente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
