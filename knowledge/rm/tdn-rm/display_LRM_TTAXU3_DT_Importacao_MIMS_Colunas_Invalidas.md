---
content_hash: d0dd2efa78ddb7b0e9377c0c998202d33b8bef5eac4e1fe54f4bc50b47ab9722
fetched_at: '2026-06-29T00:06:04.638129+00:00'
page_id: '200910008'
product: rm
source: tdn-rm
title: TTAXU3_DT_Importacao_MIMS_Colunas_Invalidas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAXU3_DT_Importacao_MIMS_Colunas_Invalidas
version: 2
---

# IMPORTAÇÃO MIMS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Importação MIMS* |
| **Situação/Requisito:** | *Ao realizar a importação MIMS, o sistema exibe a seguinte mensagem de erro:*  *Ocorreram erros na execução do processo. Invalid column name 'DATAPRIMEIRACNH'.* *Invalid column name 'UFCNH'.* *Invalid column name 'CODCLASSIFTRABESTRANG'.* *Invalid column name 'INDPAGTOJUIZO'.* |
| **Solução/Implementação:** | *Tratar no processo de importação o nome das colunas informadas para que sejam ignoradas durante o processo de importação, já que a importação deve seguir o layout com as colunas informadas no arquivo de texto.* |
| **Chamados relacionados:** | TTAXU3 |
| **Versões/Release:** | *12.1.7* |
