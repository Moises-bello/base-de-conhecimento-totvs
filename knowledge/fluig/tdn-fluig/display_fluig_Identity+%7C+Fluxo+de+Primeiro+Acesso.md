---
content_hash: 9f76b7de4ef17098bf56f1ab720d7079a5f9cdd1d93c008bbf4cf9d9f0de9e77
fetched_at: '2026-06-28T21:35:17.379625+00:00'
page_id: '1057971225'
product: fluig
source: tdn-fluig
title: Identity | Fluxo de Primeiro Acesso
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Fluxo+de+Primeiro+Acesso
version: 38
---

5.\*ndice

  

# Falando do Fluxo de Primeiro Acesso no Identity...

---

O fluxo de primeiro acesso varia ligeiramente dependendo de como o usuário foi criado (manualmente, via convite ou sincronizado via Active Directory), mas o padrão de segurança segue estas etapas:

Fluxo de Primeiro AcessoAtivação de Conta

O usuário recebe um e-mail de boas-vindas contendo um link de ativação exclusivo. Esse link possui um token de expiração (configurável no painel administrativo).

Definição de Credenciais

Ao clicar no link, o usuário é direcionado para a página de criação de senha.

* **Validação de Política:** O sistema valida em tempo real se a senha atende aos requisitos (ex: 8 caracteres, letras maiúsculas, números e símbolos).
* **MFA (Opcional):** Se o Segundo Fator de Autenticação estiver habilitado, o usuário é instigado a configurar o TOTP (Google Authenticator) nesta etapa.
Termos de Uso e Privacidade

Conformidade com a LGPD. O usuário deve aceitar os termos antes de prosseguir para o Launchpad.

Launchpad (Dashboard)

O destino final onde os aplicativos (Fluig, Protheus, RM, etc.) são exibidos conforme as permissões de contexto do usuário.

# Visão Geral

---

O primeiro acesso ao **TOTVS Identity** é o processo pelo qual você ativa sua conta e define sua senha de acesso. Para garantir a segurança dos seus dados, este processo utiliza uma **validação por código de segurança (OTP)**, garantindo que apenas o proprietário do e-mail cadastrado consiga ativar a conta.

# Passo a Passo do Acesso

---

Detalhamento Técnico (Endpoints)Passo 1: Recebimento do Convite

Você receberá um e-mail de boas-vindas ou será direcionado pelo ERP da sua empresa para a tela de ativação.

* **Importante:** Seu e-mail já aparecerá preenchido na tela, não sendo necessário digitá-lo.
Passo 2: Validação por Código de Segurança

Ao carregar a página de primeiro acesso, o sistema enviará automaticamente um **Código de Autenticação** para o seu e-mail.

1. Acesse sua caixa de entrada do e-mail cadastrado.
2. Localize o e-mail enviado pelo TOTVS Identity com o assunto **"Fluig Identity - Redefinir a Senha"**, remetido pelo endereço [support@fluigidentity.com](mailto:support@fluigidentity.com).
3. **Copie o código de 6 dígitos** (em destaque verde) que foi gerado.

**Atenção à Validade:** Por motivos de segurança, este código possui uma **validade de 10 minutos**. Se você não concluir o processo dentro desse período, será necessário solicitar um novo código.

Retorne à página do TOTVS Identity que está aberta no seu navegador e siga para o próximo passo.

1. Digite o código de 6 dígitos no campo **"Código de Autenticação"**.
2. Clique em **Confirmar Código**.

Dica

**Não recebeu o e-mail?** Verifique sua caixa de Spam. Caso o código expire, utilize a opção **"Reenviar Código"** na tela.

Passo 3: Definição de Senha

Após validar o código, você será direcionado para a tela de criação de senha (conforme Passo 2). Sua senha deve seguir as políticas de segurança da sua empresa, que geralmente exigem:

* Mínimo de **8 caracteres**;
* Ao menos uma **letra maiúscula**;
* Ao menos um **número**;
* Ao menos um **caractere especial** (ex: @, #, $).

Passo 4: Conclusão e Launchpad

Após clicar em **Alterar Senha**, sua conta estará ativa. Você será redirecionado para o seu **Launchpad**, onde encontrará todos os aplicativos e sistemas TOTVS liberados para o seu perfil.

# Perguntas Frequentes (Troubleshooting)

---

| Problema | Solução |
| --- | --- |
| O código de autenticação é inválido | Verifique se você digitou o código mais recente enviado ao seu e-mail. Cada novo pedido cancela o código anterior. |
| O link/código expirou | Por segurança, o código possui validade temporária. Clique em "Reenviar" para gerar um novo. |
| A senha não é aceita | Certifique-se de que sua senha atende a todos os requisitos exibidos na tela (letras, números e símbolos). |
