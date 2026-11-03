---
content_hash: 43c8d4ac4131d0f9fdc5f46df166e6f28b4e19d21f3dcb726e18b9dc561b0b47
fetched_at: '2026-06-29T00:11:45.913912+00:00'
page_id: '822222467'
product: rm
source: tdn-rm
title: Esqueceu a senha Novo
type: documentation
url: https://tdn.totvs.com/display/LRM/Esqueceu+a+senha+Novo
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Recuperar a Senha**
4. **Redefinir a Senha**

PainelVisão Geral

## **VISÃO GERAL**

A página "Esqueceu a Senha" permite que usuário redefina uma nova senha de acesso ao Portal do Paciente caso o mesmo a tenha esquecido ou por algum motivo não consiga fazer o login.

Exemplo de Utilização

## **EXEMPLO DE UTILIZAÇÃO**

Na página de "Login", clicar no botão "Esqueceu sua senha?". O sistema irá abrir uma tela para que o usuário informe os dados necessários (CPF, Data de Nascimento e E-mail) para que seja possível validar o seu cadastro no Portal do Paciente e consequentemente, seguir com a redefinição de uma nova senha. Após preencher os campos e clicar no botão "Enviar e-mail", o sistema irá validar os dados informados e, caso encontre um cadastro válido no Portal do Paciente, irá disparar um e-mail para a redefinição de uma nova senha.

O usuário então deve acessar a caixa do e-mail referente ao e-mail vinculado no cadastro de acesso ao Portal do Paciente, o qual foi informado na etapa anterior. **OBS**: Em alguns casos poderá ser necessário verificar se o e-mail recebido não caiu na caixa de "Span".

Nos casos em que não tenha sido o usuário responsável pela conta do Portal do Paciente quem solicitou uma redefinição de senha, este por questões de segurança, poderá facilmente ir para o Portal e alterar sua senha.

Se realmente desejar redefiniar a senha de acesso ao Portal, o usuário deverá clicar no botão "Redefinir nova senha". Feito isto, o usuário será redirecionado novamente para o Portal do Paciente na página de redefinição, onde deverá informar uma nova senha que atenda os critérios mínimos de aceite. Após clicar no botão "Criar senha", o sistema irá validar as informações necessárias e, caso estas estejam corretas, irá cadastrar a nova senha para o usuário.

**Importante**: O link de redefinição de senha possui um tempo pré-determinado para expiração de 24h.

Recuperar Senha

## **RECUPERAR A SENHA**

01. Clicar no botão "Esqueceu a senha?".

02. Informar os dados necessários para validação da conta do usuário e clicar no botão "Enviar e-mail".

03. O sistema irá validar as informações preenchidas no formulário e, irá notificar o usuário e interromper o processo quando algum dado informado não corresponder ao cadastro do usuário.

04. Se todas as informações estiverem corretas, o sistema irá disparar um e-mail com um link para redefinição de senha. Após isso o usuário será notificado quanto ao envio do e-mail e poderá voltar para a tela de login clicando no botão "Ir para login".

Redefinir Senha

01. Abrir a caixa de entrada referente ao e-mail vinculado no cadastro de usuário do Portal do Paciente.

02. Nos casos em que não tenha sido o usuário responsável pela conta do Portal do Paciente quem solicitou uma redefinição de senha, clicar no link "Ir para o Portal do Paciente", acessar sua conta e alterar a senha.

03. Para confirmar a redefinição de uma nova senha, o usuário deverá clicar no botão "Redefinir nova senha".

04. Feito isto, o usuário será redirecionado para o Portal do Paciente, na pagina de redefinição de senha. Nesta, será necessário informar os campos obrigatórios, seguindo os critérios mínimos de aceitação e clicar no botão "Criar senha".

05. O sistema irá validar as informações contidas no token para verificar se o mesmo ainda está ativo e se não houve nenhuma alteração maliciosa em seu conteúdo. Caso esta validação falhe, o sitema irá notificar o usuário e o processo será interrompido.

06. Se o token for corretamente validado, o sistema irá atualizar a senha de acesso ao Portal do Paciente e notificar o usuário. Após isso, o usuário poderá navegar novamente para a página de "Login", basta clicar no botão "Ir para Login".

07. Na página de "Login", informar o CPF e a nova senha cadastrada e clicar no botão "Entrar".
