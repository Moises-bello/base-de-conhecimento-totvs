---
content_hash: a6bcf8a5d5809384cde5848a9c67eb68afc8fd7b3e464028e8bcc8275d1d3343
fetched_at: '2026-06-29T00:11:12.532175+00:00'
page_id: '654305445'
product: rm
source: tdn-rm
title: Criação do aplicativo do Azure AD - Troubleshoot
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654305445
version: 5
---

# Troubleshoot

32

* ### **Email incorreto ou inexistente**

Caso o email em qualquer uma das duas pontas não tenha sido preenchido corretamente, o seguinte erro ocorrerá caso seja feita a tentativa de entrada:

Neste caso, siga as instruções abaixo para configurar o email corretamente, tanto no **RM** quanto no **Azure AD**

RM

#### **Configurando email no RM**

Adicionar Email

Adicione ao cadastro de usuário o email que será utilizado para login com o **Azure AD** (Deve ser o mesmo login que será utilizado na autenticação do Azure AD):

Azure AD

#### **Configurando email no Azure AD**

Por vezes, pode ser que o usuário no **Azure AD** não esteja configurado com o email corretamente (É possível logar na **Azure** sem possuir nas informações de contato o Email. Como a integração **OAuth** utiliza o email das informações de contato, a integração falha, mesmo com o acesso ao **Azure**). Para verificar se o email está configurado corretamente, siga as instruções abaixo:

Users

Acesse a aba **Users**/**Usuários** do Azure AD:

Verificando/Alterando o Email

Acesse o usuário a ser verificado. Na área **Informações de Contato** / **Contact Info**, verifique se o email está corretamente preenchido. Caso esteja como o abaixo, edite-o com o email correto

Após configurar as duas pontas, conforme descrito acima, teste a integração. O acesso deve ocorrer normalmente

---

* ### **AADSTS700016: Application with identifier 'XXXXXXXX' was not found in the directory "XXXXX"**

O erro acima ocorre caso a **Chave Pública**esteja preenchida de forma incorreta, confirme se os dados foram inseridos corretamente:

---

* ### **AADSTS90002: Tenant '1626c1ab-b9a5-41fbe2b13919' not found.**

Este erro ocorre quando alguma das seguintes URL's não foram inseridas corretamente. Confira os dados conforme citado acima na documentação:

---

* ### **O servidor remoto retornou um erro: (404) Não Localizado.**

Este erro ocorre quando o seguinte campo foi inserido incorretamente. Este campo deve receber o valor padrão:

**<https://graph.microsoft.com/oidc/userinfo>:**

---

* ### **AADSTS50011: The reply URL specified in the request does not match the reply URLs configured for the application**

Este erro pode ocorrer quando a URL de Retorno não foi inserida corretamente, tanto no **Azure AD** quanto na configuração do **RM**. Devemos atentar que esta é a URL que fará a ponte entre a Azure e o RM, e deve ser composta da seguinte forma: [http://{servidor}:{porta}/RMRestCallback/oauth/callback](http://localhost:8051/RMRestCallback/oauth/callback). Exemplo: <http://localhost:8051/RMRestCallback/oauth/callback>

---

* ### **AADSTS900144: The request body must contain the following parameter: 'scope'.**

O erro acima pode ocorrer caso o **Escopo Padrão** não seja preenchido corretamente. Confira-o e tente realizar a integração novamente:
