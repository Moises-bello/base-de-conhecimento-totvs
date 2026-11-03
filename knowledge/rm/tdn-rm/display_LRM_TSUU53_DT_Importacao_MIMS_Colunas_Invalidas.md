---
content_hash: 9070c397b7999f80c3aa4f287571edb69e101a832fbbd9f73d4c0287facb5724
fetched_at: '2026-06-29T00:06:04.317738+00:00'
page_id: '200908485'
product: rm
source: tdn-rm
title: TSUU53_DT_Importacao_MIMS_Colunas_Invalidas
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUU53_DT_Importacao_MIMS_Colunas_Invalidas
version: 2
---

# IMPORTAÇÃO MIMS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *construção e projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Importação MIMS* |
| **Situação/Requisito:** | *Ao realizar a importação MIMS, o sistema exibe a seguinte mensagem de erro:*  *Ocorreram erros na execução do processo. Invalid column name 'DATAPRIMEIRACNH'.* *Invalid column name 'UFCNH'.* *Invalid column name 'CODCLASSIFTRABESTRANG'.* *Invalid column name 'INDPAGTOJUIZO'.* |
| **Solução/Implementação:** | *Tratar no processo de importação o nome das colunas informadas para que sejam ignoradas durante o processo de importação, já que a importação deve seguir o layout com as colunas informadas no arquivo de texto.* |
| **Chamados relacionados:** | TSUU53 |
| **Versões/Release:** | *11.82.41* |
