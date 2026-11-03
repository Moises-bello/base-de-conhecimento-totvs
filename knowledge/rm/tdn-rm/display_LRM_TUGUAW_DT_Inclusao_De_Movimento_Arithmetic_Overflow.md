---
content_hash: 0e24505dac793b1d839882ba98e2b49f7b830a2002244f0aeb14ab354d4081ac
fetched_at: '2026-06-29T00:06:29.606480+00:00'
page_id: '234614105'
product: rm
source: tdn-rm
title: TUGUAW_DT_Inclusao_De_Movimento_Arithmetic_Overflow
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGUAW_DT_Inclusao_De_Movimento_Arithmetic_Overflow
version: 2
---

# Inclusao De Movimento Arithmetic Overflow

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Inclusão de movimento. |
| **Situação/Requisito:** | Ao inserir movimento com um item que ultrapassa valor permitido no banco de dados sistema emite mensagem de inconsistência sem o identificador do produto. |
| **Solução/Implementação:** | Adicionando idprd do produto à mensagem de inconsistência quando a quantidade do mesmo ultrapassa o limite permitido no banco de dados. |
| **Conversores e Parâmetros:** | *NA.* |
| **Chamados relacionados:** | TUNDEU |
| **Requisito (ISSUE):** | *NA.* |
