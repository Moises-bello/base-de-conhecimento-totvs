---
content_hash: 4fef30914239c62224fb1f2647297105ae731c26b9894c651c986c7f81425fb1
fetched_at: '2026-06-29T00:06:03.485101+00:00'
page_id: '198955232'
product: rm
source: tdn-rm
title: TSYMQR_DT_Concluir_Pedido
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYMQR_DT_Concluir_Pedido
version: 3
---

# Concluir Pedido

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento.* |
| **Função:** | *Concluir Pedido* |
| **Situação/Requisito:** | O sistema não permite a execução do processo "Concluir Pedido" em movimentos gerados pelo RMOfficina. |
| **Solução/Implementação:** | Ajuste realizado no processo responsável por concluir pedido, o sistema estava impedindo a conclusão de movimentos gerados por outros módulos, ajustamos a consistência para que este bloqueio fosse realizado apenas em movimentos gerados pelo RMSolum, pois neste caso, será obrigatório utilizar o processo de estorno dos itens. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.7* |
