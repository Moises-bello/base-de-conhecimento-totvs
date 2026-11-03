---
content_hash: a0abe63f198ba56093b0af4caa4dec0581976245467a1a9df8939927b11e1f4a
fetched_at: '2026-06-29T00:08:37.171703+00:00'
page_id: '284878430'
product: rm
source: tdn-rm
title: 1081886 EDUCACIONAL01-1666 DT Ao gerar lançamento solicita conta caixa mesmo
  ja estando parametrizada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284878430
version: 100
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Lançamento |
| **Situação/Requisito:** | Ao realizar a geração de lançamentos o sistema emite a seguinte mensagem:  Parâmetro [Coligada da conta caixa - CodColCxa] não informado.  Parâmetro [Código da conta caixa - CodCxa] não informado.  Foi conferido e a conta/caixa está parametrizada corretamente na parametrização por curso, referente ao contrato do aluno. |
| **Solução/Implementação:** | Ao gerar o lançamento de um contrato com matriz curricular vinculada e e a conta caixa está parametrizada para ser carregada da parametrização por curso o sistema sempre valida se a conta caixa padrão que será utilizada para disciplina isolada foi preenchida.  Realizada uma melhoria para que a validação seja aplicada somente se for geração de lançamento para um contrato sem matriz curricular vinculada. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
