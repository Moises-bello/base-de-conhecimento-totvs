---
content_hash: b7bf964f0b0682502af2e8bf3d53ed952e6e95199b4bd50e10c6f5174cba0e93
fetched_at: '2026-06-29T00:10:52.075314+00:00'
page_id: '570040635'
product: rm
source: tdn-rm
title: TOTVS Assinatura Eletrônica - Login Automático via Token
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570040635
version: 6
---

# **Introdução**

---

Facilitando a integração dos usuários do RM com o portal TOTVS Assinatura Eletrônica, esta funcionalidade permitirá aos usuários do RM, ter um usuário cadastrado no TOTVS Assinatura Eletrônica a partir das informações já existentes de login do RM (Nome Completo e E-mail).

# **Utilização**

---

O RM necessita da integração com o TOTVS Assinatura Eletrônica ativa.

No momento de realizar a autenticação no TOTVS Assinatura Eletrônica a partir do RM, o TOTVS Assinatura Eletrônica, irá verificar se o usuário logado já existe em sua base. Se este usuário já existir ele irá realizará o login automaticamente.

Caso o usuário ainda não exista, neste primeiro acesso, o TOTVS Assinatura Eletrônica cadastra o usuário com os dados que o RM fornece (Nome Completo e E-mail) e este usuário poderá então acessar as funcionalidades do portal.

É importante lembrar que após o primeiro login, será necessário trocar a senha do usuário para que o mesma consiga acessar o Portal em outra oportunidade.

**Importante:**

Ao criar este novo usuário, caso o domínio, extraído do e-mail, faça parte / exista em na base de dados, como empresa licenciada, este usuário, será criado como:

• Usuário colaborador  
• Associado ao primeiro CNPJ encontrado, da empresa licenciada.

Caso o domínio não seja de empresa licenciada, será criado como:

• Usuário externo  
• Não associado a nenhum CNPJ.
