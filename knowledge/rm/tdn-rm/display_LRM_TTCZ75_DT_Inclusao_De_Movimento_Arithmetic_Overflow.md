---
content_hash: b0052b4d3b683a6018187e0a03fa7daf4afa56bf924443d9597a25e8cd218882
fetched_at: '2026-06-29T00:06:21.752747+00:00'
page_id: '223179610'
product: rm
source: tdn-rm
title: TTCZ75_DT_Inclusao_De_Movimento_Arithmetic_Overflow
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCZ75_DT_Inclusao_De_Movimento_Arithmetic_Overflow
version: 1
---

# Inclusao De Movimento Arithmetic Overflow

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Inclusão de movimento.* |
| **Situação/Requisito:** | *Ao inserir movimento com um item que ultrapassa valor permitido no banco de dados sistema emite mensagem de inconsistência sem o identificador do produto.* |
| **Solução/Implementação:** | *Adicionando idprd do produto à mensagem de inconsistência quando a quantidade do mesmo ultrapassa o limite permitido no banco de dados.* |
| **Conversores e Parâmetros:** | *Não se aplica.* |
| **Chamados relacionados:** | *Não se aplica.* |
| **Requisito (ISSUE):** | *Não se aplica.* |
| **Versões/Release:** | *11.83.55* |
| **Versão Corrigida:** | *11.83.55* |
| **Versão Expedida:** | *11.83.55* |
