---
content_hash: 117a81fe41be3bdc81bed5fa15088c7548490fd5be9267d988c4ae39db21ad62
fetched_at: '2026-07-02T19:24:24.906673+00:00'
page_id: '490967059'
product: protheus
source: tdn-tec
title: TCheckBox executa Bloco de código bLClicked ao confirmar tela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490967059
version: 2
---

|  |  |
| --- | --- |
| Situação | Um bloco de código blClicked, quando implementado no componente TCheckBox, estava sendo executado ao pressionar o botão de confirmação da interface onde o mesmo está implementado. |
| Correção | Tratamento para que o bloco de código seja executado somente no evento do componente. |
| Informações adicionais | * Referente ao chamado:  Não há chamado associado * Referente à ocorrência: SCHTML-909 * Disponível a partir da build 7.00.131227A - 4.3.0 |
