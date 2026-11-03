---
content_hash: 53db0b8d898784b4c52dee9313d5c5dc3616594399067fd4288ee22c5a1cb846
fetched_at: '2026-06-29T00:06:08.041312+00:00'
page_id: '201742359'
product: rm
source: tdn-rm
title: TTEXQG_DT_Excluir_Prova_Com_Registros_Associados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEXQG_DT_Excluir_Prova_Com_Registros_Associados
version: 2
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
| **Versões/Release:** | *11.82.41* |
