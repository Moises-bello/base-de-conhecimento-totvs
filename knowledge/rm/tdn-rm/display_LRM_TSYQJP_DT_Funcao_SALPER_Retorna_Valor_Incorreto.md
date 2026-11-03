---
content_hash: 562ca029a28f8fccb779b8731db1163a98042da6716b19173288c49950d88652
fetched_at: '2026-06-29T00:06:08.789928+00:00'
page_id: '201752029'
product: rm
source: tdn-rm
title: TSYQJP_DT_Funcao_SALPER_Retorna_Valor_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYQJP_DT_Funcao_SALPER_Retorna_Valor_Incorreto
version: 1
---

# FUNÇÃO DE FÓRMULA SALPER

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *Função de fórmula SALPER, para salário composto, não traz o valor correto quando a data da mudança salarial é no mês competência, e possui horas e minutos acrescentados.* |
| **Solução/Implementação:** | *Ajuste na função de fórmula SALPER para desconsiderar as horas e minutos acrescentados à data da mudança salarial, na verificação do salário composto vigente no dia.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSYQJP* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
