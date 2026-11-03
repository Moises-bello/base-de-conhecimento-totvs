---
content_hash: c0c8b6d8dad2801d807e00a97122392c83a54c8d26b4b87635c3b9ccb9a3cc16
fetched_at: '2026-07-02T19:24:29.412826+00:00'
page_id: '868234132'
product: protheus
source: tdn-tec
title: 2 - SKIPASSERT
type: documentation
url: https://tdn.totvs.com/display/tec/2+-+SKIPASSERT
version: 2
---

Pulando asserts específicos - SKIPASSERT

Ao contrário da opção @skip(), talvez seja necessário somente "pular" um determinado assert e não o teste inteiro.

Para isso existe um comando que é inserido em seu fonte logo antes da execução do assert.

O "pulo" ficará condicionado a somente ao próximo assert que for executado, sendo assim, o assert posterior será executado normalmente.

Igualmente ao @Skip(), o **PROBAT** irá registar o salto no resultado dos testes sem gerar resultado negativo, porém agora ele fará referência ao assert "pulado".

Exemplo:

Usaremos no exemplo uma função, mas o procedimento pode ser usado em métodos também, pois esse recurso é por assert.

cpptrue
