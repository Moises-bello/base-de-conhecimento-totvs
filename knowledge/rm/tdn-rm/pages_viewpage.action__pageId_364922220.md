---
content_hash: 3e8286c633617a3185b233f53ec91777f10d4d0748cebb67506bcdee56aecc4c
fetched_at: '2026-06-29T00:09:00.158651+00:00'
page_id: '364922220'
product: rm
source: tdn-rm
title: 2930653 DEDUINTEGRACOES-2531 DT Geração de lançamentos - tela congelada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364922220
version: 2
---

# GERAÇÃO DE LANÇAMENTOS - TELA CONGELADA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Geração de lançamentos financeiros |
| **Situação/Requisito:** | Na geração de lançamentos em lote, o sistema não prosseguia e a barra de progresso do processo ficava parada.  Na geração de lançamentos por parcela, o sistema derrubava o host em determinados casos dando erro de socket ou erro de rede.  **Observação:** Isso acontecia quando o parâmetro "Usar valor de crédito da matriz curricular do aluno" estava marcado e o sistema tentava encontrar alguma equivalência para as disciplinas matriculadas do aluno. |
| **Solução/Implementação:** | Ajuste na busca de disciplinas equivalentes que fazia com que o sistema entrasse em loop na geração de lançamentos para alunos com equivalência e parâmetro "Utilizar valores da matriz curricular do aluno" marcado. Dica As correções saíram a partir da versão 12.1.20.123. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
