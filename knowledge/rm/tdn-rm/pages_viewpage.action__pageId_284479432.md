---
content_hash: d0b371110c56ec288f2218dc717ea0b29c74aa0e45cbdc39f5e98c5f8faaed40
fetched_at: '2026-06-29T00:08:36.866807+00:00'
page_id: '284479432'
product: rm
source: tdn-rm
title: 856634 FINANCEIRO01-739 Baixa - Atualização da fatura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284479432
version: 105
---

# Baixa - Atualização da fatura

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Informe a função. |
| **Situação/Requisito:** | Ao realizar a baixa de mais de um vencimento de fatura de uma só vez, o sistema baixa alguns e para outros apresenta a mensagem de erro quando o parâmetro OneLog está marcado: "Não foi possível concluir o processo de baixa para o(s) lançamento(s) [513204]. Estouro de SqlDateTime. Deve estar entre 1/1/1753 e 31/12/9999 11:59:59PM." |
| **Solução/Implementação:** | Otimização no processo de baixa. Agora o sistema realiza a baixa corretamente quando é executada por mais de um vencimento de fatura de uma só vez. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FINTRF000207 |

divs
