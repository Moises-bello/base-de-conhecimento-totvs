---
content_hash: ca473cbac6e2bfe47eda871965bb2b8c42ae176190f0124691f19dfc61e907c6
fetched_at: '2026-06-29T00:06:03.335646+00:00'
page_id: '198953552'
product: rm
source: tdn-rm
title: TSUOFB_DT_BOLSA_RETROATIVA_INCLUI_BOLSA_EM_CASO_DE_FALHA
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUOFB_DT_BOLSA_RETROATIVA_INCLUI_BOLSA_EM_CASO_DE_FALHA
version: 1
---

# BOLSA RETROATIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Inclusão de bolsa retroativa.* |
| **Situação/Requisito:** | *Ao executar o procesos de bolsa retroativa, a inclusão da bolsa está sendo feita por meio de outra transação com o banco de dados, o que inclui a bolsa no contrato do aluno, mesmo em caso de falha na execução do processo. Ou seja, o serviço responsável por inserir a bolsa no contrato do aluno cria uma nova transação com o banco ao invés de utilizar a transação existente.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de inclusão de bolsa retroativa, afim de garantir a atomicidade do processo, não permitindo, que um bolsa seja incluída no contrato do aluno, em caso de falhas na execução do processo.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.40* |
