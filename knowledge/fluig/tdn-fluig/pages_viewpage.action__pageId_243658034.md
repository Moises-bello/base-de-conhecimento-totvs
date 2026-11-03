---
content_hash: 7b008ef4c95237a0bf78e43599b30e9b199259ea64d96ff0e0b12aa5912f765c
fetched_at: '2026-06-28T21:35:23.088680+00:00'
page_id: '243658034'
product: fluig
source: tdn-fluig
title: BPM 055 - Como atrelar um processo convertido a um formulário?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243658034
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Ao encontrar um erro no desenvolvimento de um formulário atrelado a um processo, foi criada uma nova versão do processo para corrigi-lo. Porém, após a conversão das solicitações já iniciadas para a versão corrigida, o formulário não foi atualizado.

# Causa

Atualmente, o fluig não possui uma ferramenta de conversão de versão de formulário, sendo assim, quando a solicitação foi convertida, o processo foi atualizado para a versão corrente, porém o formulário continua apontando para a versão anterior.

# Solução

Novas versões do formulário só devem ser criadas caso haja a necessidade de alterar campos do formulário.
