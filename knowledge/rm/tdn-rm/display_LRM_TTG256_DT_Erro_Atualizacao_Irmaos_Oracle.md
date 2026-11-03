---
content_hash: b602f7593b767ad8991209ef3cf6e24b8a3668840c150ca917bc032711be4cae
fetched_at: '2026-06-29T00:06:08.582069+00:00'
page_id: '201750089'
product: rm
source: tdn-rm
title: TTG256_DT_Erro_Atualizacao_Irmaos_Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/TTG256_DT_Erro_Atualizacao_Irmaos_Oracle
version: 1
---

# Atualização de irmãos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Atualização de irmãos.* |
| **Situação/Requisito:** | *Erro de conversão inválida ao atualizar irmãos no Oracle. Isto ocorre porque ao retornar o data table com os irmãos existentes, as colunas que correspondem*  *ao código do* *pai e ao código da mãe estão vindo com o tipo **Decimal**, e na busca de irmãos inconsistentes, o filtro está convertendo estas colunas para **int?**.* |
| **Solução/Implementação:** | *Ajustar a busca de irmãos inconsistentes, alterando a conversão das colunas no filtro.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8.* |
