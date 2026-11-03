---
content_hash: 03dbd638b082e256399b826e912c3c6097f86bb3ec89e0762931fce594a07e40
fetched_at: '2026-06-29T00:06:10.322470+00:00'
page_id: '203760928'
product: rm
source: tdn-rm
title: TTHJY2_DT_Envelope_LogAlteracaoValores
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHJY2_DT_Envelope_LogAlteracaoValores
version: 1
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
| **Chamados relacionados:** | *TTHJY2.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8.* |
