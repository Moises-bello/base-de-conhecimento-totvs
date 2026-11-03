---
content_hash: 7358c4e81dd92af1aba2dd4871c8709110e903d563c80abeaf8f37fbf346f754
fetched_at: '2026-06-28T21:35:19.275782+00:00'
page_id: '201720494'
product: fluig
source: tdn-fluig
title: ESB - Erro de versão no momento de realizar o deploy
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201720494
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**ESB 12.3.5

# Ocorrência

No momento de realizar deploy do diagrama do ESB, ocorre erro do print abaixo:

# Causa

O problema ocorre pelo fato do plugin do ESB no TOTVS Developer Studio estar em uma versão diferente do ESB Server, essa validação é realizada para não ocorrer erros de negócios, que pode variar dependendo da versão do ESB.

# Solução

Atualizar o plugin do TOTVS Developer Studio e o ESB Server para mesma versão. É sempre indicado atualizar para versão mais recente disponível no portal da TOTVS.
