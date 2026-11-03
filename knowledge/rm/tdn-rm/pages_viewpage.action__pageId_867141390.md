---
content_hash: eff0ea85424416d7356c7028c013057911ab2fd5d4f59dcb7e98498eafe7b28c
fetched_at: '2026-06-29T00:11:56.507793+00:00'
page_id: '867141390'
product: rm
source: tdn-rm
title: Esqueceu sua senha?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867141390
version: 15
---

A opção de Esqueceu sua senha? tem como objetivo redefinir uma nova senha do aluno/responsável, para que o(s) mesmo(s) efetue o login no portal do aluno.

Funcionalidade não disponível para login com aplicativo externo

Esta funcionalidade **não está disponível** para login com aplicativo externo.

Parametrização necessária

Para que a execução desse processo seja efetivo, é necessário algumas parametrizações, sendo:

* No cadastro do Aluno/ responsável deverá estar informado um e-mail válido, pois o link para alterar a senha, por segurança é enviado para o e-mal parametrizado.

 

* Nos parâmetros Globais em: **Gestão Educacional | Ambiente | Parâmetros |Parâmetros Globais | Envio de e-mails | Parâmetros globais (Coligada Global)**

Parametrização da Coligada Global

Para realizar o envio do e-mail, deve-se preencher o campo destacado com o e-mail da organização

A partir da versão: 12.1.2602.130

Para aumentar a segurança no processo de recuperação de senha, é necessário informar a URL do FrameHTML nos parâmetros gerais.

Acessar a configuração dos parâmetros gerais em:**Gestão Educacional | Ambiente | Parâmetros |Parâmetros Globais | FrameHTML**

## **01. ACESSO A FUNCIONALIDADE**

Ao acessar o link do novo portal, na tela de login, será exibido a opção: Esqueceu sua senha?

Ao clicar nessa opção, o usuário será redirecionado para uma nova tela, sonde será necessário informar os dados:

* Usuário: O usuário, é o mesmo utilizado para efetuar o login;
* E-mail: E-mail parametrizado no cadastro do usuário;

Após informar, o usuário será notificado que a solicitação para alteração de sena, foi enviado para o e-mail parametrizado no cadastro do usuário.

Ao acessar a caixa de e-mail, terá uma nova mensagem com um link de acesso, as orientações necessárias para alterar a senha.

Ao clicar no link, o usuário será redirecionado para uma nova página, onde será necessário digitar a nova senha e a confirmação da nova senha, e em seguida clicar em: Continuar

Após conformar, o usuário será redirecionado a tela de login, onde será necessário informar o usuário e a nova senha (redefinida no passo anterior).
