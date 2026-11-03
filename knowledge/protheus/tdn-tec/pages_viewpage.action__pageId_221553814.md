---
content_hash: f6f5ee1278a6103551d0708d58bb556017c1ecfaa0c69c30612e41fbdf87f03b
fetched_at: '2026-07-02T19:24:18.916217+00:00'
page_id: '221553814'
product: protheus
source: tdn-tec
title: Problema em senhas com caracteres especiais quando utilizado o CTRL+C e CTRL+V
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221553814
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Senha criada com caracteres especiais está dando mensagem de usuário não autenticado |
| Ocorrência | Na tela de login, ao copiar e colar no campo "Senha" uma senha que possua caracteres especiais, ocorre a mensagem de usuário não autenticado. |
| Correção | Corrigido o CTRL+C/CTRL+V no componente TGet - tipo password. |
| Informações adicionais | * Referente ao chamado: não há chamados associado * Referente à ocorrência: SCHTML-284 * Disponível a partir da build 7.00.131227A - 3.0.11 |
