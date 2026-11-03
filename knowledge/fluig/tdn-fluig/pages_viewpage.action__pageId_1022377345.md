---
content_hash: 522d5f3031ba11d228967265b57d34978a22e5e437932565db3bbc9abeaa7ecc
fetched_at: '2026-06-28T21:35:17.062346+00:00'
page_id: '1022377345'
product: fluig
source: tdn-fluig
title: Diferença entre os eventos Before e After
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1022377345
version: 3
---

---

Esta documentação visa exemplificar e contextualizar a diferença entre os eventos do tipo Before e After.

## Eventos do tipo "Before"

---

De forma geral, os eventos do tipo **before** são executados antes que a ação que disparou o evento seja efetivada. Isso permite filtrar os dados que são passados no evento e, se necessário, **impedir que a ação seja concluída**.

Para bloquear a ação, basta lançar uma **Exception** contendo uma mensagem de texto, que será exibida ao usuário no formato apropriado. Confira o exemplo abaixo:

exemplo

jsEstrutura do Evento

## Eventos do tipo "After"

---

Os eventos do tipo **after** são executados após a efetivação da ação e **não exercem influência** sobre ela. Isso significa que qualquer dado alterado no parâmetro recebido dentro do evento **não será refletido** no conteúdo persistido pela ação.

Outra característica desse tipo de evento é que **não devem lançar Exception**. Caso isso ocorra, a Exception será ignorada pelo sistema e não produzirá efeito sobre a ação já concluída. Confira o exemplo abaixo:

exemplo

jsEstrutura do Evento
