---
content_hash: 27d1f9172711ed2a59c3b780378f3d46337f7abec294e3cc7490e8e92939991c
fetched_at: '2026-06-29T00:06:03.435630+00:00'
page_id: '198954277'
product: rm
source: tdn-rm
title: TSZOC7_Valores_Arredondados_Sefip
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZOC7_Valores_Arredondados_Sefip
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
| **Chamados relacionados:** | TSZOC7 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
