---
content_hash: 93e3857800df051b423969b19b1bfc9482e730c160bc1f48282d774ebc67521d
fetched_at: '2026-06-28T21:35:25.112008+00:00'
page_id: '274638452'
product: fluig
source: tdn-fluig
title: Identity | Por que alguns usuários não conseguem acessar o RM pelo Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274638452
version: 12
---

---

Nas configurações do aplicativo no Identity, o campo **Mapeamento ID de Usuário** está definido como "samAccountName".

Os usuários que não conseguem acessar o aplicativo não possuem o samAccountName preenchido (ou preenchido de forma incorreta) em seus cadastros do Active Directory.

**O Mapeamento ID de Usuário define qual informação do AD será utilizada como login**

Para resolver isso, primeiramente, o administrador deve regularizar os cadastros dos usuários no Active Directory, informando corretamente o samAccountName.

Além disso,é preciso verificar o login SAML que foi definido para os usuários no aplicativo do RM. Para isso, deve-se acessar o perfil do usuário no Identity e selecionar **Aplicativos**.

Ao localizar o aplicativo desejado (nesse caso, o RM) acionar **Definir login SAML**. Na janela aberta, verificar se o valor do campo é o samAccountName correto do usuário. Caso não seja, o campo deve ser alterado manualmente pelo administrador.

**Definir login SAML**
