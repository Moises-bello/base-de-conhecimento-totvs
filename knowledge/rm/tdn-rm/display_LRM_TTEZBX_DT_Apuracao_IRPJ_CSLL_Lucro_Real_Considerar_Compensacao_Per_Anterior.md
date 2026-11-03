---
content_hash: 8d29ff3b2979ce06f5b8b5d25721ed0e485b6cc92e990a02c5861b9ea024f895
fetched_at: '2026-06-29T00:06:08.841698+00:00'
page_id: '203555096'
product: rm
source: tdn-rm
title: TTEZBX_DT_Apuracao_IRPJ_CSLL_Lucro_Real_Considerar_Compensacao_Per_Anterior
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEZBX_DT_Apuracao_IRPJ_CSLL_Lucro_Real_Considerar_Compensacao_Per_Anterior
version: 1
---

# Apuração IRPJ e CSLL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Apuração de Tributo |
| **Situação/Requisito:** | Lucro Real – Anual /Mensal Estimado - Acumulativo / Levantamento de Balanço  Para apurações acumulativas o sistema esta calculando o valor do imposto devido no mês anterior desconsiderando as compensações anteriores, conforme regras do PVA da ECF o imposto devido no mês anterior deve considerar as compensações.  Exemplo (comportamento atual):  Mês Janeiro:  Saldo Devedor = Provisão Atual - Dedução - Imposto Per. Anterior - Compensação;  Para o mês Fevereiro o sistema considerava no"Imposto Per. Anterior" apenas o "Saldo Devedor". |
| **Solução/Implementação:** | Quando o "Valor do imposto do mês anterior" for aplicado na apuração do tributo, neste valor devem estar contidos os valores das compensações.  Exemplo: No mês de Fevereiro o Imposto. Per Anterior deve ser "Saldo Devedor" + "Compensação do Período Anterior"   * Ao calcular o imposto devido no mês anterior o sistema tem que considerar as compensações do mês anterior. * Evolução na tela de simulação para demonstrar o item “Imposto devido no mês” este item não contempla o valor da compensação. * Ao identificar a compensação quando temos levantamento de balanço o sistema deve considerar apenas a compensação do período que esta sendo apurado, e não as compensações dos meses anteriores. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTEZBX / TTFZSX |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 11.82.40 / 12.1.7 |
