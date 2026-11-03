---
content_hash: 6eb6a82f24c535d024cefa31a2b9dada979ffb6b6a53f5a666ecc062383c5c6a
fetched_at: '2026-06-29T00:06:03.948877+00:00'
page_id: '200903239'
product: rm
source: tdn-rm
title: TSAOWI_DT_Usa_Deducao_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/TSAOWI_DT_Usa_Deducao_Contrato
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque Compras e Faturamento |
| **Função:** | Parâmetro Integração - Usa Dedução de Contrato |
| **Situação/Requisito:** | Nas deduções do contrato é retornado o valor do produto mencionado no movimento de Faturamento Direto, porém o esperado é que seja retornado o valor informado no rateio do movimento, pois este reflete o valor real do custo do faturamento Direto. Ao deduzir valores de um determinado movimento do nucleus, o sistema não atualizava o valor do produto no contrato do solum |
| **Solução/Implementação:** | Ajuste na parametrização Usa Dedução de Contrato responsável pela integração do RMNucleus com o RMSolum |
| **Conversores e Parâmetros:** | Não se aplica |
| **Chamados relacionados:** | Não se aplica |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | *12.1.7* |
