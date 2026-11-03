---
content_hash: b0f4fe8176c752b8656811e167d51411a88d9258b453e8f091894c87d427b586
fetched_at: '2026-06-29T00:06:19.308653+00:00'
page_id: '219696213'
product: rm
source: tdn-rm
title: TTRH85_DT_Mensagem_Exclusao_Responsavel_Financeiro_Desmatricular_Processo_Seletivo_RM
type: documentation
url: https://tdn.totvs.com/display/LRM/TTRH85_DT_Mensagem_Exclusao_Responsavel_Financeiro_Desmatricular_Processo_Seletivo_RM
version: 1
---

# DESMATRICULAR PROCESSO SELETIVO RM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Desmatricular Processo Seletivo RM.* |
| **Situação/Requisito:** | *Mensagem exibida equivocadamente de exclusão de responsável financeiro com lançamentos existentes no log do processo Desmatricular do*  *Processo Seletivo RM, exibindo-a mesmo quando todos os lançamentos foram excluídos. Foi identificado que uma exceção lançada na tentativa*  *de excluir o responsável financeiro foi mascarada pela mensagem que está incoerente com o ocorrido.* |
| **Solução/Implementação:** | *Ajuste da mensagem para que seja mais genérica quanto a exceção lançada ao tentar excluir o responsável financeiro, além de adicionar no log*  *a informação/mensagem presente na referida exceção.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.9.* |
| **Versão Corrigida:** | *12.1.9.* |
| **Versão Expedida:** | *12.1.9.* |

divs
