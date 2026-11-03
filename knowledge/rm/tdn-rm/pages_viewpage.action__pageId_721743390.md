---
content_hash: c5ba28a415f649c7f11b9ad99b570713e788223dd46572739a47f57b41d5c4d3
fetched_at: '2026-06-29T00:11:27.285393+00:00'
page_id: '721743390'
product: rm
source: tdn-rm
title: Configurando grupo de e-mails com autenticação OAuth 2.0 no Microsoft Exchange
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721743390
version: 7
---

O Microsoft Exchange não aceita mais autenticação básica (usuário e senha) para acessar e-mails via aplicativo, dessa forma, o cadastro de grupo de e-mails do TOTVS Aprovações e Atendimento precisou ser modificado para tratar esse tipo de autenticação.

O usuário precisa agora configurar um novo aplicativo no Active Directory da sua conta Azure e informar os dados no cadastro de grupo de e-mail

Abaixo segue o link oficial da Microsoft de como realizar tal cadastro:

<https://learn.microsoft.com/pt-br/graph/auth-register-app-v2>

Agora, segue um exemplo de um aplicativo cadastrado no Azure com usas informações informadas no cadastro de grupo de e-mail do TOTVS Aprovações e Atendimento:

Ao escolher o tipo de autenticação OAuth 2.0, os campos, ID do aplicativo (cliente), URI de redirecionamento, e o botão Autenticar são exibidos. Ao preencher os dois campo e acionar o botão, uma tela de login é exibida para que o usuário digite o e-mail e senha de autenticação. Caso seja bem sucedido, um ícone verde é apresentado no botão de Autenticar e o usuário pode salvar o registro. A partir desse momento os serviços que acessam as mensagem da caixa de entrada podem ser acessados normalmente.

Para conhecer esses campos, é necessário acessar o portal Azure com a conta do Exchange e seguir os seguintes passos:

 - Acessar o Active Directory:

 - Acesse o registro de aplicativo:

Registre um novo aplicativo com qualquer nome e selecione a opção da imagem abaixo:

 - Selecione o aplicativo criado e acesse Autenticação:

 - Habilite a opção de Permitir fluxo de cliente público:

 - Ainda em autenticação, adicione uma plataforma:

 - Escolha a seguinte opção:

 - Selecione um URI de redirecionamento:

 - Copie a URI de redirecionamento e cole no cadastro de grupo de e-mail:

 - Acesse a visão geral do aplicativo e copie o ID do aplicativo (cliente):

 - Cole no campo do cadastro de grupo de e-mails, acione o botão Autenticar e digite seu e-mail e senha na página de autenticação que será exibida:

 - Confira se o ícone verde irá aparecer no botão Autenticar, em caso positivo basta salvar o registro e os serviços que acessam e-mail podem ser usados normalmente.

**Importante:** Para o uso da autenticação Auth 2.0 (Exchange), o parâmetro do TAA Serviços→ Gerar atend por grupo de email, deve obrigatoriamente usar os dados do Exchange, que são os seguintes:

POP

Servidor: outlook.office365.com

Porta: 995

ou

IMAP

Servidor: outlook.office365.com

Porta: 993

Segue abaixo um exemplo do uso como POP:
