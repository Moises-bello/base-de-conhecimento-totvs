---
content_hash: 1f30b61641b4f40311a3d13434992ba7e4b429fc1a9839dfc1bd22d288f1e19a
fetched_at: '2026-06-29T00:08:28.102010+00:00'
page_id: '271659216'
product: rm
source: tdn-rm
title: 376601 MEDU-2084 DT Emissão Recebimento Cheque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271659216
version: 114
---

# Emissão / Recebimento de cheque

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Emissão / Recebimentos de cheque. |
| **Situação/Requisito:** | Ao inserir um cheque para lançamentos a pagar ou para lançamentos a receber, marcar a flag de Pré-Datado e inserir a data de vencimento na aba dados adicionais o sistema não permite concluir sem clicar na opção de recálculo do valor do cheque. Apresenta a seguinte mensagem:  "É necessário calcular o valor do cheque pois houve alteração em campos que influenciam no cálculo deste valor".  Porém tal data de vencimento não influencia no valor do cheque considerando que a flag de “Considerar a Data de vencimento para o Cálculo do Valor do Cheque" (Aba ‘Dados Adicionais’ esteja desmarcada. Se marcada realmente é necessário recalcular. |
| **Solução/Implementação:** | No caso de cheques pré-datados, somente será necessário recalcular o valor do cheque, quando a flag “Considerar a Data de vencimento para o Cálculo do Valor do Cheque" estiver marcada e a data do vencimento for diferente da data do cheque. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito (informe o requisito relacionado):** | FIN000156. |

divs
