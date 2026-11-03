---
content_hash: b8c0645a0001368efdb402424b613a7f47794fda5b77a9458a0686d260838743
fetched_at: '2026-07-02T19:24:18.941796+00:00'
page_id: '221554400'
product: protheus
source: tdn-tec
title: Informação do campo não está sendo gravada quando clicado no botão de confirmar
  sem sair do campo antes.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221554400
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Informação do campo não está sendo gravada quando clicado no botão de confirmar sem sair do campo antes. |
| Ocorrência | Entrar em qualquer cadastro, alterar a informação de um tget e sem sair do campo, clicar no botão confirmar. Informação não é gravada. Precisa executar o evento focusout do campo.  Quando altero a informação, pressiona TAB para ir para outro campo e clico em confirmar, grava a informação corretamente. |
| Correção | Corrigido o componente TGet |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-276 * Disponível a partir da build 7.00.131227A - 3.0.11 |
