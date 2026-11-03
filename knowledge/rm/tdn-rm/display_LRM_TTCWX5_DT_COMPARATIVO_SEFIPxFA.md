---
content_hash: 000b1ba00e8b0e4fe8d188985fba30953f52fe16024fde992ddbb8c9ed3b8a8f
fetched_at: '2026-06-29T00:06:09.331547+00:00'
page_id: '203752990'
product: rm
source: tdn-rm
title: TTCWX5_DT_COMPARATIVO_SEFIPxFA
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCWX5_DT_COMPARATIVO_SEFIPxFA
version: 1
---

# COMPARATIVO SEFIP X FOLHA ANALÍTICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Obtenção dos dados do arquivo da Folha Analítica* |
| **Situação/Requisito:** | *O sistema reportava a mensagem "O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres".* |
| **Solução/Implementação:** | No  comparativo SEFIP x FA foi otimizado o tratamento quanto a obtenção dos campos vindo do Layout da Folha Analítica, quando este arquivo encontra-se corrompido, por não ter todas as informações necessárias no registro 30 a ser importado no comparador. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTCWX5 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
