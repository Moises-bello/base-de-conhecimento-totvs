---
content_hash: 620d8c85299f34bbd59193f939faa601ee75a3681089d421bdde49b8a032ce97
fetched_at: '2026-06-29T00:06:05.798188+00:00'
page_id: '201727428'
product: rm
source: tdn-rm
title: TTAROS_DT_Erro_Na_Geração_De_Contabilização_Em_Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201727428
version: 2
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Contabilização por competência para vários contratos* |
| **Situação/Requisito:** | *Ao realizar arredondamento da última parcela mensal de um contrato, o valor total de serviço é calculado com base no valor de todos os contratos selecionados. Assim, sempre que utilizada a contabilização para mais de um contrato ocorrerá divergência de valores. Dessa forma se for utilizada a tabela default de serviço para uma das partidas, a contabilidade não permitirá a operação, devido a diferença de valores entre as partidas.* |
| **Solução/Implementação:** | *Foi realizada otimização do assistente de contabilização por competência para que seja possível a contabilização de vários contratos quando as partidas da contabilização mensal utilizarem default de serviço.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8* |
