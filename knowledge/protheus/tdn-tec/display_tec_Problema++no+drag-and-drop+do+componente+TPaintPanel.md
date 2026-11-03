---
content_hash: dc0c38e6c3db837b66f0509e3e9ffea9fcdd17e06c1cba82f0922947a2548c3d
fetched_at: '2026-07-02T19:24:18.945443+00:00'
page_id: '221554414'
product: protheus
source: tdn-tec
title: Problema  no drag-and-drop do componente TPaintPanel
type: documentation
url: https://tdn.totvs.com/display/tec/Problema++no+drag-and-drop+do+componente+TPaintPanel
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Quando existem vários shapes vinculados com o mesmo código, apenas o último habilita o drag-and-drop dentro do container pai |
| Ocorrência | Ao criar um componente TPaintPanel com vários shapes com o mesmo código, só é possível clicar e arrastar o container pai.  Para os shapes filhos não é habilitado o drag-and-drop. |
| Correção | Corrigido o drag-and-drop do componente TPaintPanel quando existe vários shapes com o mesmo código. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-293 * Disponível a partir da build 7.00.131227A -2.2.23 |
