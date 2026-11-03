---
content_hash: 26656acc0405dcf5dc5b0e4a34b65e53ddf6546ae1a4226cfd2f38487ff7121f
fetched_at: '2026-06-29T00:06:07.835236+00:00'
page_id: '201738669'
product: rm
source: tdn-rm
title: TTEQSN_DT_Erro_NF-e_Gerar_Movimento_Utilizando_Filtro_Nome_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEQSN_DT_Erro_NF-e_Gerar_Movimento_Utilizando_Filtro_Nome_Aluno
version: 1
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
| **Versões/Release:** | *11.82.41.* |
