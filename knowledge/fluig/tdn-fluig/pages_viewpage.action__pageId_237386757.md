---
content_hash: 19c2e9bd5bfeac0f40fab7bcb23bc6793fd8e6dfe47392aa4ab319bca3a3d24f
fetched_at: '2026-06-28T21:35:22.525474+00:00'
page_id: '237386757'
product: fluig
source: tdn-fluig
title: WCM - Meus widgets estão todos com as mesmas preferências, como resolvo?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237386757
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

# Ocorrência

Meus widgets estão todos com as mesmas preferências, como resolvo?

# Causa

Geralmente isso ocorre quando há mais de um elemento com o mesmo "id" na página. O risco de isso ocorrer é maior quando, montando uma pagina, use-se mais de uma  de um *widget* que não esteja com os "ids" de seus elementos nomeados corretamente.

# Solução

Dentro dos arquivos .ftl, sempre que é criado um novo elemento, é importante utilizar a variável *instanceId* como sufixo na hora de nomeá-lo. Abaixo um exemplo:

xml


...
