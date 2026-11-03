---
content_hash: 699dbbed4b0ab814fde26881bd0636747002a92e26be9ed0a7d51f387f8e6cff
fetched_at: '2026-06-29T00:08:56.530695+00:00'
page_id: '351379381'
product: rm
source: tdn-rm
title: 2009259 RMSAU-2209 DT Inserção de Guia Automática a partir do pedido de exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351379381
version: 1
---

# Inserção de Guia Automática a partir do pedido de exame

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Pedido de Exames |
| **Situação/Requisito:** | Acessei os parâmetros gerais, aba UNIDADES DIAGNÓSTICO, marquei o parâmetro "Incluir na Guia de Autorização os exames solicitados para paceintes externos e execução externa". EM seguida fiz um pedido de exame com dois exames, e notei que o sistema incluiu duas guias com números diferentes na aba GUIA/AUTORIZAÇÃO. Nossos convênios exigem que temos apenas um número de Guia para cada conta, ou seja, o sistema deveria lançar as duas guis com o mesmo número. |
| **Solução/Implementação:** | Realizado ajuste na rotina de pedido de exames para utilizar o mesmo critério de geração do número da guia |
