---
content_hash: f1e74602cac492e41fc1be1fb876801e2e3c72c8c5f0c3fce697c7d29bd99d58
fetched_at: '2026-06-29T00:11:42.713197+00:00'
page_id: '795905294'
product: rm
source: tdn-rm
title: Esqueci minha senha.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795905294
version: 10
---

A partir da versão **12.1.2310.101** foi disponibilizado aos usuários do aplicativo a funcionalidade "Esqueci minha senha" .

**Para utilizar esta funcionalidade o envio de e-mails do RM deve estar parametrizado.**Para mais informações sobre o envio de e-mail acesse o link:**[Envio de E-mail Linha RM](http://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM)**

Na tela de login selecione a opção Esqueci minha senha.

Ao clicar no link de esqueci minha senha o usuário será direcionado para uma sequência de telas onde poderá realizar o processo de recuperação de senha.

Na primeira tela, será solicitado o preenchimento do usuário utilizado para fazer login no aplicativo.

Após informar o usuário deve ser selecionada a opção de Enviar e-mail de recuperação, onde ele receberá um **código de 4 digitos** que utilizaremos na tela seguinte..

O usuário deverá informar o código correto e selecionar a opção Verificar. Este código possui um tempo de vida e a possibilidade de reenvio após 1 minuto.

Com o preenchimento e validação do código, o usuário poderá avançar para a tela onde relizará o cadastro de uma nova senha.

Para concluir o processo deverá ser digitada sua nova senha, e a confirmação dela, então será feito o redirecionado para a tela de login, onde poderá utilizar a nova senha criada para acessar o aplicativo normalmente.

Importante!**O usuário só conseguirá realizar o envio do e-mail se for encontrado o registro na tabela GUSUARIO ( CODUSUARIO , EMAIL ) .**
