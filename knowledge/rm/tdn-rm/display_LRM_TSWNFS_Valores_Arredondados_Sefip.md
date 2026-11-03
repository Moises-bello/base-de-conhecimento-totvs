---
content_hash: 732005e10cfee121a6ba55c16f9246553a85f4106a6217118fdfc017c65d47fd
fetched_at: '2026-06-29T00:06:03.402952+00:00'
page_id: '198953987'
product: rm
source: tdn-rm
title: TSWNFS_Valores_Arredondados_Sefip
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWNFS_Valores_Arredondados_Sefip
version: 2
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *C&P.* |
| **Módulo:** | *Folha de pagamento.* |
| **Função:** | *SEFIP.* |
| **Situação/Requisito:** | Cliente informa que lançou folha para funcionário, e a soma dos eventos que incide FGTS aplicada a alíquota de recolhimento teria que apresentar o valor de R$ 603,5288. Porém ao gerar o lançamento financeiro do tipo 15 – FGTS conforme SEFIP o sistema está arredondando o valor para mais ficando assim o valor de R$ 603,53. Desta forma esta diferença somada a todos os funcionários está impactando no fechamento do cliente  *.* |
| **Solução/Implementação:** | Otimizada rotina SEFIP, criada regra de correção de valores para geração dos lançamentos financeiros, executando rateio das diferenças de arredondamento conforme regra do SEFIP (distribui a diferença funcionário a funcionário de 1 centavo até o total da diferença)  *.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSWNFS |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
