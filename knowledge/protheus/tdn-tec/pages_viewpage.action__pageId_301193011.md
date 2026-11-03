---
content_hash: 9c8f3ee33a8f5aea463e4169825a2dec9982b0c374e106cc8666a5861e808838
fetched_at: '2026-07-02T19:24:23.296502+00:00'
page_id: '301193011'
product: protheus
source: tdn-tec
title: Correção - TListBox dump no GetSelText
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301193011
version: 3
---

Foi adicionada uma proteção ao TListBox para que ele não gere dump em algumas ocasiões ao chamar o método GetSelText.

|  |  |
| --- | --- |
| Situação | Algumas vezes o TListBox gera dump ao chamar GetSelText. |
| Ocorrência | O problema ocorre pois o registro selecionado do TListBox não existe, já foi excluído. |
| Correção | Adicionada proteção para que retorne um texto vazio também em ocasiões como essa. |
| Informações adicionais | * Referente à ocorrência: MTEC-708 * Disponível em builds superiores a 131227A-13.2.3.25 |
