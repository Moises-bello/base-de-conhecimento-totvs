---
content_hash: 77d7fd5a7dc26c11507e33f77db846b9c1ecdc70f13602908681b00bfa2ce37e
fetched_at: '2026-06-29T00:06:09.340077+00:00'
page_id: '203753245'
product: rm
source: tdn-rm
title: TTGVWA_DT_COMPARATIVO_SEFIPxFA
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGVWA_DT_COMPARATIVO_SEFIPxFA
version: 3
---

# COMPARATIVO SEFIP X FOLHA ANALÍTICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Obtenção dos dados do arquivo da Folha Analítica* |
| **Situação/Requisito:** | *O sistema reportava a mensagem "O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres".* |
| **Solução/Implementação:** | No  comparativo SEFIP x FA foi otimizado o tratamento quanto a obtenção dos campos vindo do Layout da Folha Analítica, quando este arquivo encontra-se corrompido, por não ter todas as informações necessárias no registro 30 a ser importado no comparador. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTGVWA |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
