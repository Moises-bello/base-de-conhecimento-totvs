---
content_hash: a4826020603f3a1b100a876bdfcddf98129b682736b97a00a3d7cf36b6193d9f
fetched_at: '2026-06-28T21:35:23.352570+00:00'
page_id: '244911442'
product: fluig
source: tdn-fluig
title: WCM - Como resolver o erro "Recurso não encontrado" ao acessar a Home?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244911442
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

A página Home para não está funcionando para usuários comuns (papel *user*). Apenas para os usuários Administradores está funcionando. É apresentado o seguinte erro:

**"Recurso não foi encontrado. Entre em contato com o administrador para obter mais informações."**

# Solução

Verificamos que o problema está ocorrendo porque foi removida a permissão de acesso a página Home dos usuários comuns, somente os administradores estão com acesso.

Para solucionar o problema, execute os seguintes passos:

* Acesse o **Painel de Controle**, localize o agrupador **Pessoas** e acesse o recurso **Permissões**.
* Na seção **Home** acione o ícone de configuração (engrenagem)
* No item **Home** acione o ícone de configuração novamente (engrenagem)
* Selecione o tipo de permissão **Por papel**, e adicione a permissão de **Visualizar página** para os usuários do papel *user*:

* Feito isso, basta atualizar a página e os usuários com perfil comum terão acesso à página Home.
