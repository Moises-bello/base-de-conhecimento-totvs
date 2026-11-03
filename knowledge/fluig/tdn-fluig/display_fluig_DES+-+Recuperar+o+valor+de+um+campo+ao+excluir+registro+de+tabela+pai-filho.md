---
content_hash: 7498ebad8aaa0cd532b84d156961806d49b1a13c3ea9a52e32c9f1282420b7e7
fetched_at: '2026-06-28T21:35:23.016504+00:00'
page_id: '243639438'
product: fluig
source: tdn-fluig
title: DES - Recuperar o valor de um campo ao excluir registro de tabela pai-filho
type: documentation
url: https://tdn.totvs.com/display/fluig/DES+-+Recuperar+o+valor+de+um+campo+ao+excluir+registro+de+tabela+pai-filho
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.9

# Ocorrência

É possível recuperar o valor de um registro pai-filho quando o usuário clicar no botão excluir?

# Solução

Com o uso da função [fnCustomDelete](http://tdn.totvs.com/x/U4l8B) é possível interferir na chamada que elimina um filho da tabela. Para obter o valor do campo a ser excluído, utilize o seguinte código:

js

[Anexo](http://tdn.totvs.com/download/attachments/243639438/teste_pai_filho.zip?api=v2) segue o formulário de exemplo.
