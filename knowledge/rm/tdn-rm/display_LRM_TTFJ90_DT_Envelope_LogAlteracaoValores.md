---
content_hash: 69a30d79474714a22d3ddf4f1bde54c2407f0c056da3a1efd2639ea7405d9fb3
fetched_at: '2026-06-29T00:06:10.265893+00:00'
page_id: '203760353'
product: rm
source: tdn-rm
title: TTFJ90_DT_Envelope_LogAlteracaoValores
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFJ90_DT_Envelope_LogAlteracaoValores
version: 3
---

# ENVELOPE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Envelope.* |
| **Situação/Requisito:** | *Quando o usuário acessava o envelope de um funcionário que tinha algum registro de o campo "hora" do página de “Log dos valores alterados do envelope” estava menor que "000:00" (negativo), o sistema apresentava erro e não carregava o envelope.* |
| **Solução/Implementação:** | *Foi implementado um tratamento na rotina que carrega o envelope mais especificamente a parte de “Log dos valores alterados do envelope”, para trazer o campo “hora” 0:00 quando o mesmo estiver com valor inferior a 0:00, fazendo com que o envelope carregue sem apresentar erro.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTFJ90.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41.* |
