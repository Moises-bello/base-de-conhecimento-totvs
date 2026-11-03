---
content_hash: 24f3f473e19200037f63c379381bb3017fabe83d05ce19b14947e5ae7a1cc212
fetched_at: '2026-06-29T00:06:06.123334+00:00'
page_id: '201728554'
product: rm
source: tdn-rm
title: TTCYSL_DT_Diferenca_Arredondamento_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCYSL_DT_Diferenca_Arredondamento_Ferias
version: 1
---

# DIFERENÇA DE ARREDONDAMENTO NAS FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença de Férias* |
| **Situação/Requisito:** | *No cálculo da Diferença de Férias por dissídio está sendo calculada a diferença do evento de CC 129 - Arredondamento nas Férias, e lançada no evento de CC 88.*  *O arredondamento não pode ser recalculado neste caso.* |
| **Solução/Implementação:** | *Ajustar no processo de Diferença de Férias, quando for cálculo por dissídio, para não recalcular o evento de CC 129 - Arredondamento nas Férias.*  *Este evento nunca deve ser recalculado no processo de Diferença, independente se for por dissídio ou não.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTCYSL* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
