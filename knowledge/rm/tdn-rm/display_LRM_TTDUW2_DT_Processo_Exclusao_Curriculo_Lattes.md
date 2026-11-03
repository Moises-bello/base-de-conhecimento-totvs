---
content_hash: 9f2f944e7f211c97242d313cf4ebfda1623fad5de6836cb239d45dac906dcb0d
fetched_at: '2026-06-29T00:06:08.548404+00:00'
page_id: '201749569'
product: rm
source: tdn-rm
title: TTDUW2_DT_Processo_Exclusao_Curriculo_Lattes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDUW2_DT_Processo_Exclusao_Curriculo_Lattes
version: 4
---

# PROCESSO DE EXCLUSÃO DE CURRÍCULO LATTES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Processo de exclusão de currículo lattes* |
| **Situação/Requisito:** | *Ao executar o processo: Apagar Currículo Lattes do professor, ocorre o erro: O índice estava fora dos limites da matriz.* |
| **Solução/Implementação:** | *Ajuste no método do data server que efetua a exclusão do currículo lattes para considerar a pessoa como chave para a exclusão do mesmo.*  *Foi inserido uma mensagem ao confirmar a exclusão do currículo, pois ao excluir o currículo será excluído da pessoa em questão, ou seja, se a pessoa estiver vinculada a um aluno, ou outro professor etc, também será excluído.*  *Segue nova mensagem: "Como o currículo lattes está vinculado a pessoa, caso existir outro professor associado, o currículo também será excluído. Confirma a execução deste processo?".* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7 e 12.1.8* |
