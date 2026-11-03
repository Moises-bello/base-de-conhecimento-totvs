---
content_hash: cd2e61194fa41de6c56974dbce82617c56f1d3c42ea83f9ebbb68eddd1d24eef
fetched_at: '2026-06-29T00:11:10.164295+00:00'
page_id: '641680514'
product: rm
source: tdn-rm
title: Ativação do novo HASH de Senhas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641680514
version: 3
---

A partir da versão **12.1.34**, será possível ativar um parâmetro para alterar a forma como os hashs de senhas são gerados.

Esta ação visa aumentar consideravelmente a proteção das senhas dos usuários, principalmente contra quebras via força bruta.

A imagem abaixo, mostra o fluxo que irá promover a atualização gradativa dos hashs de senhas (a cada novo login ou ao alterar a senha o hash será atualizado):

Para ativar o parâmetro, basta ir à aba Segurança e marca-lo:

Delphi

**Esse parâmetro não deve ser marcado caso haja alguma aplicação Delphi sendo utilizada em paralelo à MDI!**

Caso o parâmetro seja marcado, os hahs serão atualizados a medida que os usuários forem fazendo login, dessa forma, caso haja alguma aplicação Delphi rodando em paralelo a MDI, não será mais possível fazer login via aplicação Delphi, visto que a lógica não é compartilhada, sendo assim necessário resetar a senha do usuário que teve seu hash alterado, e também desmarcar o parâmetro.

Ao desmarcar o parâmetro será necessário fazer o primeiro login pela MDI, para que o hahs seja atualizado para o padrão antigo, permitindo login pela aplicação Delphi.
