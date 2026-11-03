---
content_hash: 47a9ab001c8873b3eaf06b0d703a529385b9673fe33c9b3bdfeebffc8b3ced94
fetched_at: '2026-06-29T00:09:55.517667+00:00'
page_id: '447092780'
product: rm
source: tdn-rm
title: Consultar Autorização Automática (Job)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=447092780
version: 2
---

O processo irá selecionar as NF-e que estejam com Status “Pendente”, para a coligada corrente (selecionada no Contexto). Após selecionar as notas, o Job irá efetuar a Consulta da Autorização da NF-e, através do TSS, atualizando o Status da Nota para Autorizada ou Rejeitada, conforme retorno da SEFAZ.

O resultado do processamento do Job poderá ser visto na tela de “Gerenciamento de Jobs”, já disponível no sistema.

Para evitar concorrência entre processos, o agendamento automático somente será disparado caso não esteja sendo executado outro processo de consulta.

A permissão ao processo de “Consultar Autorização Automática (Job)” será a mesma concedida ao processo de “Consultar Autorização”, já existente no sistema.
