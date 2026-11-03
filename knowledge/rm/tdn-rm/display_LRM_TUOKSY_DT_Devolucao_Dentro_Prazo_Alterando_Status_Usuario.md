---
content_hash: a0adc5033d7c528f5b1ea1d56ea4c416d8fdcab3c0996db3200ee435ec9bf931
fetched_at: '2026-06-29T00:06:30.333864+00:00'
page_id: '235319815'
product: rm
source: tdn-rm
title: TUOKSY_DT_Devolucao_Dentro_Prazo_Alterando_Status_Usuario
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOKSY_DT_Devolucao_Dentro_Prazo_Alterando_Status_Usuario
version: 120
---

# MOVIMENTAÇÃO - DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentação - devolução - suspensão por atraso* |
| **Situação/Requisito:** | *Caso o usuário esteja irregular e suspenso por devoluções em atraso, se o mesmo fizer uma devolução que não esteja em atraso, o status de irregular é alterado para regular incorretamente.* |
| **Solução/Implementação:** | *Foi identificado que o sistema não validava o status atual antes de definir o status regular por aquele empréstimo, sendo assim, foi incluído uma validação para que se o usuário estiver irregular não alterar para regular.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TUOOH3 |
| **Requisito (ISSUE):** | *N/A* |

divs
