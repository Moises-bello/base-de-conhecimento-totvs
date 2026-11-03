---
content_hash: f5371400df413132d5444830c76e3b2a7a6613942960c6786c65db4a9c20b6ba
fetched_at: '2026-06-28T21:35:19.032125+00:00'
page_id: '189305564'
product: fluig
source: tdn-fluig
title: DES - Validação de campo de formulário em processo workflow
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189305564
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Após preencher todos os campos do formulário no processo e clicar em "Salvar e Enviar" é exibida a mensagem de que um dos campos não foi preenchido.

# Causa

O campo que está sendo validado no evento validateForm não existe no formulário.

# Solução

Acesse o evento validateForm.js do seu formulário e verifique qual é o campo que ele está validando. O campo deve existir no formulário.   
  
Para corrigir basta confirmar o campo no formulário e alterá-lo no evento.   
  
Após fazer isso, exporte o evento para a plataforma novamente. Ao inicializar uma nova solicitação, a validação utilizará o evento atualizado.
