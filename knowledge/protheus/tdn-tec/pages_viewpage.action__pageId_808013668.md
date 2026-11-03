---
content_hash: 80e2e965f251584e603bb5480048984761f9b62346953d6fec9043b12c63745b
fetched_at: '2026-07-02T19:24:28.685238+00:00'
page_id: '808013668'
product: protheus
source: tdn-tec
title: Correção - Ao acionar a tecla "Tab", os campos anteriores são selecionados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808013668
version: 2
---

Algumas teclas estavam com comportamento errático, como por exemplo, a tecla "tab", seleciona o campo anterior ao invés do seguinte.

|  |  |
| --- | --- |
| Situação | Teclas com comportamentos erráticos |
| Ocorrência | O problema ocorreu por um efeito colateral de uma correção feita no QCefView para aceitar a tecla AltGR |
| Correção | O método do QCefView com a correção da para tecla AltGr estava com um "return" no lugar errado, fazendo com que o código de tecla retornado não fosse consistente |
| Informações adicionais | * Referente ao chamado: [DTCLIENT01-4433](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-4433) * Referente à ocorrência: [18562569](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=18562569) * Disponível em builds superiores a 20.3.2.2 |
