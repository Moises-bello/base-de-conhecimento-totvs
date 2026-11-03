---
content_hash: 0291afc9831f4b37139451a0247ab9fe4c5db2b3e76488869f9b56b6237970c5
fetched_at: '2026-06-29T00:06:01.420170+00:00'
page_id: '198937956'
product: rm
source: tdn-rm
title: TSWNSS_DT_Processo_Geracao_Plano_de_Aula
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWNSS_DT_Processo_Geracao_Plano_de_Aula
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Turma/Disciplina* |
| **Função:** | *Geração de Plano de Aula* |
| **Situação/Requisito:** | *Erro ao gerar Plano de Aula quando é selecionado os parâmetros para não gerar Planos de Aulas para feriados.* |
| **Solução/Implementação:** | *Durante a inclusão no log do processo dos dias que não foram gerados os planos de aulas, era retornado o nome do feriado deste dia. Estava sendo buscado o nome de feriados para dias que não eram necessariamente um feriado, causando um erro no processo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **Versões/Release:** | *12.1.7* |
