---
content_hash: 3421a88b5c90e41486646439b6b1a9b2733a841f2230d8c536d64c5ecc639197
fetched_at: '2026-06-29T00:08:47.029629+00:00'
page_id: '317320957'
product: rm
source: tdn-rm
title: 1289775 MATESTCNTFTOF01-872 DT Inclusão de consistência ao alterar tipo de
  produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317320957
version: 94
---

# INTEGRAÇÃO DE PRODUTO COM ORDEM DE SERVIÇO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cadastro Produto |
| **Situação/Requisito:** | Ao realizar a alteração do tipo de um produto é preciso garantir que não tenha ordem de serviço em andamento que faça uso do mesmo, essa alteração nesse caso pode gerar comportamento indevido no andamento e conclusão da ordem de serviço. |
| **Solução/Implementação:** | Inclusão de consistência no cadastro de produto. Quando uma alteração do tipo do produto for realizada (Produto -> Serviço) ou (Serviço → Produto), o sistema vai verificar e garantir que não existe ordem de serviço em andamento que faça uso desse produto. Se existe esse caso o usuário vai ser alertado com a seguinte mensagem "O produto está sendo utilizado por uma “Ordem de Serviço não finalizada” e não pode ter seu tipo alterado" |
| **Conversores e Parâmetros:** | Desnecessário. |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | Não se aplica |

divs
