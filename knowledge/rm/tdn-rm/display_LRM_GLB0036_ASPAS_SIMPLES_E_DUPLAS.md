---
content_hash: 2947dcd8445c5f1f55c215fb8b0b2a857811b50f5399be105cdf324b4b611b49
fetched_at: '2026-06-29T00:06:27.956322+00:00'
page_id: '233740924'
product: rm
source: tdn-rm
title: GLB0036_ASPAS_SIMPLES_E_DUPLAS
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0036_ASPAS_SIMPLES_E_DUPLAS
version: 3
---

# Aspas Simples e Duplas

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.50 e Superiores |
| **Ocorrência:** | Aspas simples e duplas em sentenças SQL’s |
| **Ambiente:** | Biblioteca RM |
| **Passo a passo:** | É costumeiro o uso de alias para nomear colunas de retorno nas sentenças SQL’s em banco de dados SQL Server ou Oracle.    Para atribuição de um Alias em SQL utilizamos, ou não, aspas simples. Enquanto no Oracle utilizamos aspas duplas.    Para alias que não contenha espaço é dispensada a utilização das aspas simples (para SQL) ou duplas (para Oracle), porém para os produtos da linha RM, não é permitido a utilização de aspas duplas, seja para SQL ou Oracle, por limitação do executor de sentenças SQL’s.    Alguns exemplos de como cadastrar sentenças SQL’s que façam uso das aspas:      Cadastrando uma sentença SQL que contenha aspas duplas de forma incorreta, erros serão apresentados, como:   - FROM keyword not found where expected (Palavra-chave FROM não localizada onde esperada) |
| **Observações:** |  |
