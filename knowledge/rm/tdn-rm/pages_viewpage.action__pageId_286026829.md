---
content_hash: 0370955fa5716347084f834cd3da9df9e60aba380594fa65afe6b8e1024d755d
fetched_at: '2026-06-29T00:08:39.963247+00:00'
page_id: '286026829'
product: rm
source: tdn-rm
title: 834004 FOPROTINAS01-449 DIRF - Impressão de Funcionários Sem Movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286026829
version: 103
---

# PARÂMETRO PARA CONTROLAR IMPRESSÃO DE FUNCIONÁRIOS SEM MOVIMENTAÇÃO NA DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | DIRF |
| **Situação/Requisito:** | Ao gerar a DIRF em arquivo, temos a “Opção de Seleção” e caso seja escolhido a opção “TODOS” o sistema gera o relatório com os valores zerados. |
| **Solução/Implementação:** | Criado o parâmetro "Imprimir Funcionários sem Movimentação(Informe de Rendimentos)", se esse parâmetro estiver desmarcado o sistema verifica se existe algum valor, caso não exista o mesmo é removido. Se o parâmetro estiver marcado o sistema gera o relatório para funcionários sem movimentação.     A alteração é somente no RM Labore, no RM Portal não teve nenhuma alteração. |
| **Tickets relacionados:** | 834004 |

divs
