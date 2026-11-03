---
content_hash: d5b9da6a1bdccb4778dde7ef29fbe041535e26558a53d79261cc605d0729d072
fetched_at: '2026-06-29T00:05:51.702205+00:00'
page_id: '1053169767'
product: rm
source: tdn-rm
title: Controle com binding incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+com+binding+incorreto
version: 3
---

# Código de Referência

---

false

**control-with-incorrect-binding**

# Contexto

---

Quando um controle faz referência a uma tabela que não está mais presente na lista de campos do relatório o mesmo será marcado com a limitação de controle com binding incorreto para posterior correção.

Veja que a ligação de dados do Label está apontando para a tabela "teste\_binding", porém a tabela que existe na listagem de campos é "teste\_binding2".

# Solução

---

Antes de avançar com a aceleração do relatório, deve-se corrigir a ligação de dados, apontando para a tabela correta.
