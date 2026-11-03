---
content_hash: 82a876d28b739161a83b3aa702a7ecc41e6a7819c50e2cae87cfd06df1c364a3
fetched_at: '2026-06-29T00:06:17.771419+00:00'
page_id: '213985398'
product: rm
source: tdn-rm
title: TTQIH6_DT_Mensagem_Exclusao_Responsavel_Financeiro_Desmatricular_Processo_Seletivo_RM
type: documentation
url: https://tdn.totvs.com/display/LRM/TTQIH6_DT_Mensagem_Exclusao_Responsavel_Financeiro_Desmatricular_Processo_Seletivo_RM
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
| **Versões/Release:** | *11.82.42.* |
| **Versão Corrigida:** | *11.82.41.* |
| **Versão Expedida:** | *11.82.41.* |

divs
