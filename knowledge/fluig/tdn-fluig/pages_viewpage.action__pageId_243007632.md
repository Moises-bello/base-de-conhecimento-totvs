---
content_hash: 79c01bc0484f3f3d49f6277d6ee40a6f8d51e197a01e7bfd93bd1d9a4b751304
fetched_at: '2026-06-28T21:35:22.938919+00:00'
page_id: '243007632'
product: fluig
source: tdn-fluig
title: DES - Quebra de linha nas mensagens de validação da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243007632
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

# Ocorrência

Após atualização da plataforma percebemos que a mensagem exibida para validação dos campos obrigatórios no validateForms não está mais aceitando quebra de linha.

Gostaria de saber qual é o procedimento para quebrar linhas nas mensagens de validação.

# Solução

Conforme a o guia de [Desenvolvimento de Formulários](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormulários-ValidateForm), as mensagens de erro, bem como os componentes de mensagem do Guia de Estilo (alertas, confirmação e erro) devem utilizar **\n** para quebra de linha em mensagens.
