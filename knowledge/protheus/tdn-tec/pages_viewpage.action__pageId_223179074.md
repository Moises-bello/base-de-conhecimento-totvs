---
content_hash: 7ee7a0a204991c1289ad155eee69e28261255940cf73b9d4493b1843f26b780c
fetched_at: '2026-07-02T19:24:19.583861+00:00'
page_id: '223179074'
product: protheus
source: tdn-tec
title: Correção - GzStrComp não compacta strings pequenas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223179074
version: 1
---

Essa build contém uma correção na função AdvPL GzStrComp.

|  |  |
| --- | --- |
| Situação | GzStrComp não compacta strings pequenas |
| Ocorrência | Ao chamar a função **GzStrComp** com uma string pequena, a função retornava **.F.** e não compactava a string. |
| Correção | Corrigido a função GzStrComp para compactar strings independente do tamanho da mesma. |
| Informações adicionais | * Não há chamado relacionado * Referente à ocorrência: TEC-6946 * Disponível em builds superiores a 7.00.131227A com data de geração superior a 27/11/2015. |
