---
content_hash: ea6802fe2ea59b893d1967f3fa708c69fcef16efb0403c97ffb14cb4dacf9cfd
fetched_at: '2026-06-29T00:06:21.310064+00:00'
page_id: '223168355'
product: rm
source: tdn-rm
title: Segurança no Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223168355
version: 14
---

# Segurança no Portal

|  |  |
| --- | --- |
| **Produto:** | Portal Corpore RM |
| **Versões:** | 11.82, 12.1 |
| **Ocorrência:** | Falha na segurança |
| **Ambiente:** |  |
| **Passo a passo:** | Para melhorar a segurança de acesso ao Portal RM, a partir da versão 11.82.42, não será possível logar no sistema com o usuário de código “rm”. Além disso, não será permitido a adição de perfis a este usuário. Caso queira manter um usuário com as mesmas permissões de acesso do usuário “rm” será necessário criar outro usuário com as mesmas permissões do usuário “rm”. Para realizar esse processo utilize a funcionalidade “Cópia de Permissão de Usuários”.  Exemplo: [Cópia de Permissão de Usuários](http://tdn.totvs.com/pages/releaseview.action?pageId=146181524)  Ao acessar os menus de serviço do Portal, o sistema adiciona na carteirinha do usuário o código de usuário igual ao utilizado na autenticação do Banco de Dados. Então, caso o usuário “rm” possua associação com algum perfil que possua permissões no Portal, a possibilidade de se acessar o Portal sem autenticação de usuário e senha será enorme. Por esse motivo é aconselhável a não utilização do usuário “rm” no sistema. |
| **Observações:** |  |
