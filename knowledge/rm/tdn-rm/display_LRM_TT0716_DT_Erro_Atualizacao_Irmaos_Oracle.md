---
content_hash: 754915b26d6087b857d8c7b99342a4bc90c5c166ff68e40502841b9658a79777
fetched_at: '2026-06-29T00:06:08.570299+00:00'
page_id: '201749941'
product: rm
source: tdn-rm
title: TT0716_DT_Erro_Atualizacao_Irmaos_Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/TT0716_DT_Erro_Atualizacao_Irmaos_Oracle
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
| **Versões/Release:** | *11.82.41.* |
