---
content_hash: 28eeb0dbe5885c45da070cead02d1ac6edb5745b15974daf64055e6cde363fdf
fetched_at: '2026-06-29T00:08:32.568661+00:00'
page_id: '273991092'
product: rm
source: tdn-rm
title: 504342 FINANCEIRO01-297 Baixa - Inclusão do Extrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273991092
version: 104
---

# Baixa - Inclusão do Extrato

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Baixa - Inclusão do Extrato |
| **Situação/Requisito:** | Ao realizar o pagamento em cheque de mais de um lançamento com boletos diferentes, o sistema está gerando um extrato de caixa por boleto mesmo apresentando a mensagem que será gerado um extrato para todos os lançamentos. |
| **Solução/Implementação:** | Otimização no processo de baixa de lançamentos. Agora o sistema realiza a baixa corretamente dos lançamentos com boletos diferentes gerando um extrato de caixa para todos quando o parâmetro (Contas a Pagar -> Baixa -> Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa) está marcado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FINTRF000194 |

divs
