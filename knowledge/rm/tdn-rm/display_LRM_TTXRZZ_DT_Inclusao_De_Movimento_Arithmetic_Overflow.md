---
content_hash: 10c2a773a5dbc17da868f7ef416ee105b2ff6c77cc093af71324416aa0d83f12
fetched_at: '2026-06-29T00:06:21.852878+00:00'
page_id: '223182633'
product: rm
source: tdn-rm
title: TTXRZZ_DT_Inclusao_De_Movimento_Arithmetic_Overflow
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXRZZ_DT_Inclusao_De_Movimento_Arithmetic_Overflow
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
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |
