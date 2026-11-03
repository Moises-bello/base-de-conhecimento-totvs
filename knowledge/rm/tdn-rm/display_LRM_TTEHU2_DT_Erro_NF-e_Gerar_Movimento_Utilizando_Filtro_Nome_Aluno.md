---
content_hash: 611a2372a325e7c8bac73834aef44fa1b436f5c46bbf9a1ddeadad09f3390317
fetched_at: '2026-06-29T00:06:07.781863+00:00'
page_id: '201737917'
product: rm
source: tdn-rm
title: TTEHU2_DT_Erro_NF-e_Gerar_Movimento_Utilizando_Filtro_Nome_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEHU2_DT_Erro_NF-e_Gerar_Movimento_Utilizando_Filtro_Nome_Aluno
version: 2
---

# Geração de Movimento NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Geração de Movimento NF-e.* |
| **Situação/Requisito:** | *Erro ao gerar movimento utilizando o filtro "Nome aluno". Isto ocorre devido ao fato de que na *query que carrega os boletos do* *movimento não existe**   *a* *tabela* *PPESSOA no "JOIN"* *e existe* *o campo PPESSOA.NOME no "WHERE".* |
| **Solução/Implementação:** | *Inclusão da tabela PPESSOA no JOIN com a tabela SALUNO para que se consiga filtrar pelo nome do aluno.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8.* |
