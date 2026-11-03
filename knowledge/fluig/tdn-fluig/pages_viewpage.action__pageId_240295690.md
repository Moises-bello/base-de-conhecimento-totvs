---
content_hash: 5dad68296faca52550898e91df15a5b4723d083cd4297251d0a4a92d17b8353d
fetched_at: '2026-06-28T21:35:22.784699+00:00'
page_id: '240295690'
product: fluig
source: tdn-fluig
title: DES - Ativar e Inativar usuários automaticamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240295690
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Nosso ambiente ultrapassou a quantidade de licenças de usuários, quando determinado usuário precisa se logar no sistema, outro usuário necessita ser desativado. Teria alguma customização para automatizar este processo de alguma forma?

# Solução

É possível utilizar o *webservice* ECMColleagueService para verificar o status do usuário (método getSimpleColleague), ativar um usuário com o metodo activateColleague deste mesmo *webservice* e desativar outro usuário através do método updateColleague. Veja a documentação destes métodos em .

Você também pode utilizar as APIs para realizar este processo. Veja a documentação em [UserServiceRest](https://api.fluig.com/old/resource_UserServiceRest.html#path__social_user.html). Você pode buscar o usuário com a API /social/user/{genericId}, desativar o usuário com a API /social/user/disable/{genericId}, e ativar o usuário com a API /social/user/enable/{genericId}.

Lembrando que não é possível desativar usuários que possuam tarefas pendentes na plataforma.
