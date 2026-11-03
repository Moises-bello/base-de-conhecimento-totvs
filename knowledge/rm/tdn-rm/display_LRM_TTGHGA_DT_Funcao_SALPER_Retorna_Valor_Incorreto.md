---
content_hash: e7ff45e8ae8c8043675095ff9e20c6e6db33392dc898ea227c387b1b3ef25274
fetched_at: '2026-06-29T00:06:08.813267+00:00'
page_id: '201752270'
product: rm
source: tdn-rm
title: TTGHGA_DT_Funcao_SALPER_Retorna_Valor_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGHGA_DT_Funcao_SALPER_Retorna_Valor_Incorreto
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
| **Chamados relacionados:** | *TTGHGA* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
