---
content_hash: e94c5d74bad6ac026dc943e94ddb97ecc96e9adcb15b5c857cef6a73033ef417
fetched_at: '2026-06-29T00:06:08.045092+00:00'
page_id: '201742367'
product: rm
source: tdn-rm
title: TTFH76_DT_Excluir_Prova_Com_Registros_Associados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFH76_DT_Excluir_Prova_Com_Registros_Associados
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Avaliação e Pesquisa* |
| **Função:** | *Prova* |
| **Situação/Requisito:** | *O sistema apresenta erro ao excluir provas que tenham algum registro associado, ou seja, candidatos, ranking, questões e etc.* |
| **Solução/Implementação:** | *Quando a prova já possui registros associados não é possível fazer a exclusão pois pode gerar vários impactos nos locais em que é utilizada, ou seja, colocar em risco a integridade dos dados, sendo assim foi inserido uma mensagem de alerta para o usuário. Caso a prova não tenha nenhum registro associado a mesma será excluída sem erros.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
