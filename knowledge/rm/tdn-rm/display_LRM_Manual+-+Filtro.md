---
content_hash: 62af6d622e7300a2f359c6653260e63ad74faa3317e65f63555806459af854b9
fetched_at: '2026-06-29T00:08:47.236188+00:00'
page_id: '319787275'
product: rm
source: tdn-rm
title: Manual - Filtro
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Filtro
version: 3
---

A aba filtro permite criar uma expressão de filtro para o registro independente da ligação. Esta expressão deverá retornar um valor do tipo lógico (bool) e diferente do filtro da ligação, o filtro do registro somente pode utilizar dados do contexto, pois ele será executado antes do gerador percorrer a lista da ligação do registro.

Normalmente este filtro será utilizado para ignorar a geração do registro, de acordo com um parâmetro informado pelo usuário, indicando se o Layout irá gerar ou não o registro determinado. Neste caso o gerador não irá percorrer a lista de origem do registro, agilizando o processo de geração do arquivo. Para mais informações consulte [Expressões](/pages/viewpage.action?pageId=319787306).

![](/download/attachments/319787275/filtro.png?version=1&modificationDate=1512921847000&api=v2)
