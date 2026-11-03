---
content_hash: 7fdd088ddc018a92e312d582afbf2f1c53ac36655f15259980fd6f029253cacd
fetched_at: '2026-06-29T00:06:15.350101+00:00'
page_id: '210053044'
product: rm
source: tdn-rm
title: TTNQKA_DT_Formula_Com_EXECSQL_CALCMED
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNQKA_DT_Formula_Com_EXECSQL_CALCMED
version: 2
---

# UTILIZAÇÃO DE FÓRMULA COM EXECSQL E CALCMED

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *No cálculo de um evento que possui fórmula utilizando as funções EXECSQL e RESULTSQL com uma chamada da CALCMED no meio, estava retornando o erro: "A fórmula XXX não pode ser executada! Consulta SQL ZZZ não foi   inicializada!".* |
| **Solução/Implementação:** | *Alterado o tratamento para a passagem do contexto no método de execução de fórmulas para sempre utilizar o mesmo objeto de row, ao invés de criar um novo a cada chamada.* |
| **Chamados   relacionados:** | *TTNQKA* |
| **Versões/Release:** | *12.1.8* |
