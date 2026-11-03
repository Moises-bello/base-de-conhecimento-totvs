---
content_hash: 9ac451f1f54e5890fbac3dfd37d35c8b9ad1069dffc07bf60cea41640ac54fe6
fetched_at: '2026-06-29T00:11:26.476593+00:00'
page_id: '717713561'
product: rm
source: tdn-rm
title: Configurando uma conta GMAIL para ser usada no cadastro de Grupo de e-mails
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+uma+conta+GMAIL+para+ser+usada+no+cadastro+de+Grupo+de+e-mails
version: 16
---

Para que o Gmail seja utilizado nos serviços do TOTVS Aprovações e Atendimento (que acessam contas de e-mails através do cadastro de grupo de e-mails), é necessário realizar as seguintes configurações na conta Google:

* **Ativar verificação em duas etapas**

* **Criar senha de app na opção “Senhas de app”**

## **Instruções para configurar a verificação em duas etapas e as senhas de app**

**1.Login na Conta Google**

Acesse [myaccount.google.com](http://myaccount.google.com).

**2. Gerenciar sua Conta Google**

Após o login, clique em “Gerenciar sua Conta Google”.

**3.Segurança e login**

No menu lateral, vá até a aba “Segurança e login”.

**4.Ativar verificação em duas etapas**

**OBS: Para que a opção “Senhas de app” apareça, é obrigatório a verificação em duas etapas estar habilitada.**

**5.Procure a opção “Senhas de app”**

Defina um nome personalizado para identificar o app/dispositivo.

Gere uma senha de 16 caracteres.

Copie a senha gerada.

## **Caso a opção “Senhas de app” não esteja disponível ou tenha dificuldade na opção “Verificação em duas etapas”, consulte a documentação oficial do Google abaixo:**

**Senhas de app:**

* **👉**[**https://support.google.com/accounts/answer/185833**](https://support.google.com/accounts/answer/185833)

**Verificação em duas etapas:**

* **👉**[**https://support.google.com/accounts/answer/185839**](https://support.google.com/accounts/answer/185839)

**6.Cadastrar senha no TOTVS  Aprovações e Atendimento**

Cole a senha criada em “Senhas de app” no cadastro do respectivo grupo de e-mail.

Por fim, nos parâmetros do TOTVS Aprovações e Atendimento, deve ser configurados os dados para acesso POP3 do gmail:
