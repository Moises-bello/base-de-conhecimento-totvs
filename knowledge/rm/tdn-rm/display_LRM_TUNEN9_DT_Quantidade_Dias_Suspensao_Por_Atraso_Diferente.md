---
content_hash: 83393227dc39656649bb4a3e88e1b473272670f2495ceb73fa2f5dfd7a8fc057
fetched_at: '2026-06-29T00:06:30.157714+00:00'
page_id: '235314672'
product: rm
source: tdn-rm
title: TUNEN9_DT_Quantidade_Dias_Suspensao_Por_Atraso_Diferente
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNEN9_DT_Quantidade_Dias_Suspensao_Por_Atraso_Diferente
version: 120
---

# MOVIMENTAÇÃO - DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentação - devolução - suspensão por atraso* |
| **Situação/Requisito:** | *Quando a regra de empréstimo define que o atraso irá causar suspensão, no momento da devolução de mais de um exemplar em atraso sistema está efetuando o cálculo correto da data de suspensão porém no cadastro do usuário está informando a quantidade de dias incorretamente, está mostrando a quantidade de dias de atraso do último empréstimo devolvido.* |
| **Solução/Implementação:** | *Foi identificado que o sistema não estava somando o valor dos dias de suspensão, sendo assim foi feito o ajuste para somar corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TUOCBQ |
| **Requisito (ISSUE):** | *N/A* |

divs
