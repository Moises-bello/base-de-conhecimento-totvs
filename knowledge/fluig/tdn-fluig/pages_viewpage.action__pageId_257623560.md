---
content_hash: 4013a0bcb81d43db12a3cf3abe246401f50fefedf7cdd7ceb4973f8c99504dcd
fetched_at: '2026-06-28T21:35:23.688169+00:00'
page_id: '257623560'
product: fluig
source: tdn-fluig
title: Configuração de envio de e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623560
version: 58
---

false

¿Habla Español? Haga [clic aquí](https://tdn.totvs.com/x/E7XDIQ) para ver el Configuración de envío de correo electrónico en Español.

Do you speak English? [Click here](https://tdn.totvs.com/x/L7XDIQ) to view the E-mail sending configuration in English.

Atenção

Esta página foi revisada para considerar as configurações de servidor para a atualização 1.7.

Caso possua atualização anterior, acesse .

* [Configuração global](https://tdn.totvs.com/pages/viewpage.action?pageId=257623560#Configura%C3%A7%C3%A3odeenviodee-mail-Configura%C3%A7%C3%A3oglobal)
* [Configuração por empresa](https://tdn.totvs.com/pages/viewpage.action?pageId=257623560#Configura%C3%A7%C3%A3odeenviodee-mail-Configura%C3%A7%C3%A3oporempresa)

# Objetivo

---

O objetivo deste guia é realizar a configuração de envio de *e-mail* no TOTVS Fluig Plataforma.

# Falando de configuração de envio de e-mail...

---

Existem duas formas de configuração na plataforma: por empresa ou global. Por  a configuração é feita individualmente e será aplicada apenas para a empresa em questão e a  que será obedecida por todas as empresas cadastradas na plataforma. É importante lembrar que prevalecerá a configuração por empresa caso ambas forem realizadas.

falseConfiguração de e-mailtrueConfiguração globalConfiguração por empresaConfiguração no instalador

global

## Configuração global

---

A configuração global de envio de e-mail já ocorre durante a execução do instalador da release , mas pode ser necessário alterar as informações cadastradas.

Para isso, siga os passos abaixo:

Importante!

Caso sua plataforma tenha o envio de e-mail configurado anterior à atualização 1.6.1, será necessário limpar os dados antigos de conexão do Servidor de e-mail, pois a partir da atualização 1.6.1 essas configurações são feitas em tela.

**01**. Autentique-se na plataforma com o usuário **wcmadmin.**

**02**. Acesse o menu **Painel de Controle**, localize o agrupador **WCM** e acione **Configurações do Sistema****.**

**03**. Acesse a aba **Parâmetros da Plataforma** e altere os campos necessários da seção **Configuração de e-mail.**

#f2f2f2#f2f2f2

Os campos disponíveis são:  

48%

**Segurança:**Permite o uso dos protocolos TLS ou SSL na conexão SMTP. Se o servidor de e-mail utilizar o protocolo **TLS** *(Transport Layer Security)* ou **SSL***(**Secure Socket Layer)*, será necessário selecioná-lo, caso contrário, deve-se selecionar a opção 'Não'.

**Porta do Servidor:** Porta do servidor de envio de *e-mails* (SMTP). A porta padrão é 25.

**Usuário:**Login do usuário utilizado na autenticação do servidor de e-mail.

**Todas as notificações por *e-mail***: Quando habilitado, determina que todas as notificações por e-mail serão enviadas com o remetente informado no campo "E-mail do remetente", tanto as de produto (com interação do usuário) quanto as da plataforma. 

**E-mail do remetente**: E-mail que será considerado o remetente padrão para o envio das notificações, quando a opção "Remetente padrão" está habilitada.

**Agrupar *e-mails* no envio**: Quando ativado, determina que os *e-mails* a serem enviados sejam agrupados e disparados a cada 2 segundos. Quando desabilitado, cada *e-mail* será disparado individualmente, o que em grandes quantidades pode causar o bloqueio das mensagens por serviços como o Gmail.

2%48%

**Host do Servidor:**Endereço do servidor de envio de *e-mails* (SMTP);

**Autenticação:**Habilite se for necessário informar um usuário e senha para autenticação no servidor de *e-mail*. Se for habilitado, os campos de usuário e senha deverão ser preenchidos.Ao habilitar o recurso, é exibido o indicativo ***ON***, informando que o recurso está ativo. Quando esse recurso é desabilitado, é exibido o indicativo ***OFF***.

**Senha:**Senha utilizada na autenticação do servidor de e-mail.

**Remetente padrão**: Quando habilitado, determina que o e-mail das notificações será enviado por um remetente padrão. Quando não habilitado esse recurso, o remetente será o *e-mail* que foi definido para a empresa. 

**Nome do remetente**: Nome do remetente padrão para o envio de notificações por e-mail, quando a opção "Remetente padrão" está habilitada.

Sobre o remetente padrão

Mesmo que seja realizada a configuração de um remetente padrão, ele é utilizado apenas para atividades de sistema que não possuem usuário, como criação de usuários, recuperação de senha e teste de conexão. Os demais e-mails da plataforma (workflow e documentos) utilizam como remetente o usuário logado, quem movimentou a solicitação ou até mesmo seus remetentes personalizados.

**Timeout do SMTP (em segundos):**Determina o tempo de expiração que levará para que a notificação seja comunicada por e-mail, este tempo poderá ser definido pelo usuário entre o valor padrão correspondente à 180 segundos ou o mínimo 10 segundos. 

**04**. Para realizar a validação do envio de e-mail, utilize o botão **Testar conexão**.

#f2f2f2#f2f2f2

Após acionar o botão Testar conexão, será apresentada uma nova página para o usuário informar um endereço de e-mail, para que seja realizado o envio de teste.

Atenção!

Devido a atualização dos protocolos de segurança da Google, a opção de apps menos seguros foi desabilitada pela empresa, por isso, para realizar o teste de e-mail, é necessário realizar antes as configurações na conta Google.  [Acesse aqui](https://tdn.totvs.com/x/2O_GKQ) e saiba como realizar essas configurações.

**05**. Acione **Salvar** para gravar as alterações.

empresa

## Configuração por empresa

---

Na configuração de envio de e-mail por empresa, o que for alterado será aplicado individualmente, apenas para a empresa em questão. 

É importante ressaltar que a plataforma sempre dará preferência para as configurações aplicadas por empresa, mesmo quando alguma alteração for realizada na configuração global.

Para realizar a configuração, siga os passos abaixo:

**01**. Autentique-se na plataforma com o usuário **wcmadmin.**

**02**. Acesse o menu **Painel de Controle**, localize o agrupador **WCM** e acione **Empresas.**

**03**. Selecione a empresa desejada e acione **Editar**.

**04**. Acesse a aba **E-mail**.

**05**. Preencha os campos disponíveis.

#f2f2f2#f2f2f2Passo 2

Os campos disponíveis são: 

**Deseja habilitar o envio de e-mail?**Habilita a configuração de e-mail específica para a empresa selecionada.

**Deseja agrupar o envio de e-mails?** Agrupa e dispara a cada 2 segundos os e-mails que devem ser enviados. Quando desabilitado, cada e-mail será disparado individualmente, o que em grandes quantidades pode causar o bloqueio das mensagens por serviços como o Gmail.

**Host:** Endereço do servidor de envio de e-mails (SMTP).

**Porta:** Porta do servidor de envio de e-mails (SMTP).

**Remetente:** Endereço de e-mail do remetente.

**Segurança:** Permite o uso dos protocolos TLS ou SSL na conexão SMTP. Se o servidor de e-mail utilizar o protocolo **TLS** *(Transport Layer Security)* ou **SSL***(**Secure Socket Layer)*, será necessário selecioná-lo, caso contrário, deve-se selecionar a opção 'Não'.

**Timeout do SMTP (em segundos):** Determina o tempo de expiração que levará para que a notificação seja comunicada por e-mail, este tempo poderá ser definido pelo usuário entre o valor padrão correspondente à 180 segundos ou o mínimo 10 segundos. 

**Deseja habilitar a autenticação?** Habilite se for necessário informar um usuário e senha para autenticação no servidor de e-mail. Se for habilitado, os campos de usuário e senha serão exibidos em tela.

**06**. Para realizar a validação do envio de e-mail, utilize o botão **Testar conexão**.

#f2f2f2#f2f2f2

Será necessário informar um endereço de e-mail para que seja realizado o envio de teste.

**07**. Acione **Salvar** para gravar as alterações.
