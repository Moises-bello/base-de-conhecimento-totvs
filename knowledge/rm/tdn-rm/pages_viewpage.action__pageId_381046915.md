---
content_hash: 245f0e522fde4636c18510a02542064a16db13caaceb129f33ff01ad735b5df7
fetched_at: '2026-06-29T00:09:03.523121+00:00'
page_id: '381046915'
product: rm
source: tdn-rm
title: 2536240 DSAUGHFATF-737 Erro XML com óbito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381046915
version: 1
---

# Erro XML com óbito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão Hospitalar |
| **Função:** | Faturamento para Convênios |
| **Situação/Requisito:** | Quando há óbito de um recém nascido ou da mãe de um recém nascido, o sistema não está gerando a tag indicadorDORN no XML da TISS.  Morte do RN: <ans:indicadorDORN>S</ans:indicadorDORN>  Morte da mãe: <ans:indicadorDORN>N</ans:indicadorDORN>  \*outros casos não deve sair a tag. |
| **Solução/Implementação:** | Implementada regra para a tag <ans:indicadorDORN> no XML da TISS |
| **Tickets relacionados:** | <https://totvssuporte.zendesk.com/agent/tickets/2536240> |
