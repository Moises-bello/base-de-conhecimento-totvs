---
content_hash: af476627c1a3fc4c4553956115f50c0258f1f987be28791fca94791fd7bf3d2f
fetched_at: '2026-06-29T00:08:37.848754+00:00'
page_id: '284884313'
product: rm
source: tdn-rm
title: Recuperação de Senha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284884313
version: 9
---

Caso algum candidato esqueça a senha, será possível solicitar uma nova senha para acessar a central do candidato. Na tela da Central do candidato possui o link "Esqueci minha senha/login", ao clicar nesse link será redirecionado para uma tela idêntica a de login, porem o texto parametrizável pode ser outro.

O candidato escolherá uma das formas de login parametrizadas para o login e em seguida digitará a data de nascimento e por fim clicar em "Receber senha" e a nova senha será enviada para o e-mail indicado no cadastro do usuário.

Deve ser parametrizado no RM no cadastro "**Mensagens de Notificação**" um modelo de e-mail para o envio de senha.

# **Parametrização do Texto de Recuperação de Senha**

**1-**Acesse o cadastro de Processo seletivo para parametrizar um texto de recuperação de senha.

 **TOTVS Processo Seletivo| Cadastros| Processo seletivo| Aba Parâmetros| SubAba Central do candidato 2/2**

**2-**Acesse a Central do candidato no novo portal e clique em "Esqueci minha senha/login".

Ao solicitar a recuperação da senha será apresentado ao candidato a mensagem abaixo.

Comportamento disponível a partir da versão  12.1.32.287, 12.1.33.249 e 12.1.34.152

A mensagem abaixo poderá ser apresentada em algumas situações, tais como:

* Os parâmetros globais para o envio de e-mail não foram configurados corretamente.
* Os parâmetros do Processo Seletivo "E-mail do remetente do processo seletivo" não foi configurado.

# **Parametrização do E-mail de envio de senha**

**1-**Acesse os anexos do cadastro de Processo seletivo e selecione "Mensagens de notificação".

 **TOTVS Processo Seletivo| Cadastros| Processo seletivo| Anexos| Mensagens de Notificação**

**2-**Inclua uma nova mensagem de notificação e escolha o objetivo de "Enviar e-mail para o candidato com sua senha de acesso ao portal", configure o template do e-mail e salve o cadastro.

Dica

Utilize as Tag's disponíveis para envio da senha e login.
