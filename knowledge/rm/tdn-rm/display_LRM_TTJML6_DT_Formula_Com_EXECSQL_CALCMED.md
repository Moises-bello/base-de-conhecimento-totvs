---
content_hash: 3b488c667a3336e42e0510fde134b548569fce91ae3271259fd4166dd9965ac5
fetched_at: '2026-06-29T00:06:15.334875+00:00'
page_id: '210052779'
product: rm
source: tdn-rm
title: TTJML6_DT_Formula_Com_EXECSQL_CALCMED
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJML6_DT_Formula_Com_EXECSQL_CALCMED
version: 2
---

# UTILIZAÇÃO DE FÓRMULA COM EXECSQL E CALCMED

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *No cálculo de um evento que possui fórmula utilizando as funções EXECSQL e RESULTSQL com uma chamada da CALCMED no meio, estava retornando o erro: "A fórmula XXX não pode ser executada! Consulta SQL ZZZ não foi inicializada!".* |
| **Solução/Implementação:** | *Alterado o tratamento para a passagem do contexto no método de execução de fórmulas para sempre utilizar o mesmo objeto de row, ao invés de criar um novo a cada chamada.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTJML6* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42* |
