---
content_hash: fcbd49a5ed0f5ea3b56207e6ff6de0f1fe9bf8f0459a586f8807a38c2feeb64f
fetched_at: '2026-06-29T00:08:32.543846+00:00'
page_id: '273990511'
product: rm
source: tdn-rm
title: 626025 EDUCACIONAL01-243 Geração de Lançamento - o lançamento não pode ser
  gerado pois o valor é menor que zero
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273990511
version: 106
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Lançamento Financeiro |
| **Situação/Requisito:** | Em Contratos >> anexos >> parcelas >> processos >> gerar lançamento  Deparamo-nos com a seguinte situação:Ao tentar regerar um lançamento cancelado, o sistema não permite e exibe a seguinte mensagem de erro:  "O lançamento não pode ser gerado pois o valor é menor que zero."  Esta situação ocorre quando o aluno possui um valor na conta corrente superior ao valor do lançamento fianceiro a ser gerado. |
| **Solução/Implementação:** | Melhoria no serviço de geração de lançamento financeiro para que não seja apresenta a mensagem “O lançamento não pode ser gerado pois o valor é menor que zero.” Para alunos que tenham valores na conta corrente superior ao valor líquido do lançamento financeiro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 626025 |
| **Requisito:** |  |

divs
