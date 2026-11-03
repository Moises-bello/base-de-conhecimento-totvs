---
content_hash: 5b75c8bae3ea4b9badb4a9766f8f1684e85bf1d3c6fba1d7c16d8c3d04482aec
fetched_at: '2026-06-28T21:35:27.587394+00:00'
page_id: '555865966'
product: fluig
source: tdn-fluig
title: CON - Como configurar o envio de e-mail na release 1.6
type: documentation
url: https://tdn.totvs.com/display/fluig/CON+-+Como+configurar+o+envio+de+e-mail+na+release+1.6
version: 3
---

Atenção

Esta página foi revisada para considerar as configurações de servidor para a atualização 1.6.

Caso possua atualização 1.7 acesse 

Caso possua atualização da 1.5.6 à 1.5.13, acesse: [Como configurar o envio de e-mail da release 1.5.6 à 1.5.13?](http://tdn.totvs.com/x/MmoSCw)

Para atualizações 1.5.6 ou anteriores da plataforma, acesse: [Como configurar o envio de e-mail na release 1.5.6 e inferiores?](http://tdn.totvs.com/x/Pd1bDQ)

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é realizar a configuração de envio de *e-mail* no TOTVS Fluig Plataforma. Existem duas formas de configuração de e-mail:  a configuração é feita individualmente e será aplicada apenas para a empresa em questão e a configuração  que, caso for configurado, será obedecido por todas as empresa cadastradas na plataforma. É importante lembrar que prevalecerá a configuração por empresa caso ambas forem realizadas.

# Configuração de envio de *e-mail*

---

Importante!

Caso você tenha envio de e-mail configurado anterior à atualização 1.6.1, será necessário limpar os dados antigos de conexão do Servidor de e-mail pois a partir da atualização 1.6.1 essas configurações são feitas em tela.

Autentique-se na plataforma com o usuário **wcmadmin** e acesse: **Painel de Controle** → **WCM** → **Configurações do Sistema** → aba **Parâmetros da Plataforma**: 

Edite as opções da seção **Notificações por *e-mail***: 

* **Remetente padrão**: ative para habilitar o envio de *e-mail* utilizando o endereço informado no parâmetro ***E-mail* do remetente**;

* ***E-mail* do remetente**: informe o endereço de *e-mail* que deve ser utilizado para enviar os *e-mails* do sistema;

* **Nome do remetente**: preencha para definir um nome junto ao *e-mail* de origem, por exemplo, para identificar a empresa;

* **Todas as notificações por *e-mail***: ative para que todos os e-mails do produto sejam enviados com o *e-mail* informado no parâmetro ***E-mail* do remetente**.

* **Agrupar *e-mails* no envio**: ative para que os *e-mails* a serem enviados sejam agrupados e disparados a cada 2 segundos. Quando desabilitado, cada *e-mail* será disparado individualmente, o que em grandes quantidades pode causar o bloqueio das mensagens por serviços como o Gmail.

Alguns servidores de e-mail podem não suportam o envio de e-mails em nome de outros usuários, ou seja, utilizarão sempre o e-mail configurado nesta tela como remetente padrão no ato do envio das notificações.

**Figura 1 - Notificações por *e-mail***

global

## Configuração de e-mail global na atualização 1.6.2 e superiores

---

A partir da versão 1.6.2 a plataforma passa a suportar protocolo SSL.

Autentique-se na plataforma com o usuário **wcmadmin** e acesse:**Painel de Controle** → aba **WCM** → **Configurações do Sistema** → aba **Parâmetros da Plataforma**:

Edite as opções da seção **Configuração de *e-mail***:

* **Segurança:**
  + **Não:** Seleciona-o caso não utilize segurança no envio de e-mail.
  + **TLS** *(Transport Layer Security):* Selecione-o caso deseje utilizar este protocolo de criptografia.
  + **SSL** *(**Secure Socket Layer):*Selecione-o caso deseje utilizar este protocolo de criptografia.
* **Host do Servidor:**Endereço do servidor de envio de *e-mails* (SMTP);
* **Porta do Servidor:** Porta do servidor de envio de *e-mails* (SMTP). A porta padrão é 25.
* **Autenticação:**Habilite se for necessário informar um usuário e senha para autenticação no servidor de *e-mail*. Se for habilitado, os campos de usuário e senha deverão ser preenchidos.Ao habilitar o recurso, é exibido o indicativo ***ON***, informando que o recurso está ativo. Quando esse recurso é desabilitado, é exibido o indicativo ***OFF***.
* **Usuário:***Login* do usuário utilizado na autenticação do servidor de *e-mail*.
* **Senha:**Senha utilizada na autenticação do servidor de*e-mail*.

**Figura 2 - **Configuração Global de *E-Mail***** **na versão 1.6.2**

## Configuração de e-mail global na versão 1.6.1

---

Autentique-se na plataforma com o usuário **wcmadmin** e acesse:**Painel de Controle** → aba **WCM** → **Configurações do Sistema** → aba **Parâmetros da Plataforma**:

Edite as opções da seção **Configuração de *e-mail***:

* **Host do Servidor:**Endereço do servidor de envio de *e-mails* (SMTP);
* **Porta do Servidor:** Porta do servidor de envio de *e-mails* (SMTP). A porta padrão é 25.
* **Segurança (TLS):**Habilite se o servidor de *e-mail* utilizar TLS. Somente o protocolo TLS é suportado na plataforma. Ao habilitar o recurso, é exibido o indicativo ***ON***, informando que o recurso está ativo. Quando esse recurso é desabilitado, é exibido o indicativo ***OFF***.
* **Autenticação:**Habilite se for necessário informar um usuário e senha para autenticação no servidor de *e-mail*. Se for habilitado, os campos de usuário e senha deverão ser preenchidos.Ao habilitar o recurso, é exibido o indicativo ***ON***, informando que o recurso está ativo. Quando esse recurso é desabilitado, é exibido o indicativo ***OFF***.
* **Usuário:***Login* do usuário utilizado na autenticação do servidor de *e-mail*.
* **Senha:**Senha utilizada na autenticação do servidor de*e-mail*.

Atenção!

Tudo que for configurado como global será aplicado para todas as empresas cadastradas na plataforma. Para realizar a configuração para uma única empresa, siga a documentação .

**Figura 3 - Configuração Global de *E-Mail* na versão 1.6.1**

## Configuração de e-mail global na versão 1.6

---

Para realizar o restante da configuração de envio de *e-mail* na plataforma, é preciso parar todos os serviços iniciados: FLUIG, Fluig\_Indexer e Fluig\_RealTime.

Depois disso, basta seguir os passos abaixo para configuração de *e-mail* global. Tudo o que for configurado como global será aplicado para todas as empresas cadastradas na plataforma. Para realizar a configuração para uma única empresa, siga a documentação .

Atenção!

É essencial que os serviços do fluig sejam parados para realizar esta configuração, e que após configurada os serviços podem ser reinicializados normalmente.

0.5falsesamplesfadetrue1Passo 1

* Após parar os serviços do fluig acesse o diretório [diretório\_instalação]\appserver\domain\configuration.

2Passo 2  

* Edite o arquivo domain.xml.

* Procure por "mail-smtp" para localizar o bloco de configuração abaixo.

* Altere os parâmetros ***host*** e ***port*** de acordo com as definições do seu servidor de *e-mail.*

xml



]]>

3Passo 3

* Para configuração do *e-mail* utilizando TLS localize o bloco de configuração "java:jboss/mail/Default".

A plataforma aceita apenas o protocolo de segurança TLS. O padrão SSL não é suportado.

xml



]]>4Passo 4

* Substitua o bloco localizado no Passo 3 com o conteúdo do exemplo abaixo.

* Preencha os dados de autenticação (*username* e *password*), lembrando de adicionar o parâmetro **tls="true"**:

xml






]]>

* Salve o arquivo e inicie os serviços do fluig.

empresa

# Configuração de e-mail por empresa

---

No cadastro por empresa, cada configuração será feita individualmente e será aplicada apenas para a empresa em questão.

A plataforma sempre dará preferência para as configurações aplicadas por empresa, mesmo quando alguma alteração for realizada na configuração global.

falseempresaPasso 1

* Caso deseje configurar o envio de *e-mail* de uma empresa específica, de forma diferente dos , autentique-se na plataforma com o usuário **wcmadmin**.

* Acesse o **Painel de Controle** → aba **WCM** → **Empresas**.

* Selecione a empresa desejada e clique no *link* **Editar**.

* Acesse a aba ***E-mail**.*

**Figuras 4 - Acessando as configurações da empresa**

Passo 2

Preencha os campos de acordo com a orientação a seguir:

* **Habilitar:** habilita a configuração de e-mail específica para a empresa selecionada;

* **Agrupar *e-mails* no envio**: agrupa e dispara a cada 2 segundos os *e-mails* que devem ser enviados. Quando desabilitado, cada *e-mail* será disparado individualmente, o que em grandes quantidades pode causar o bloqueio das mensagens por serviços como o Gmail.

* ***Host*:** endereço do servidor de envio de *e-mails* (SMTP);

* **Porta:** porta do servidor de envio de *e-mails* (SMTP);

* **Remetente:** endereço de *e-mail* do remetente;

* **Segurança:** habilite se o servidor de *e-mail* utilizar TLS. Somente o protocolo TLS é suportado na plataforma;

* **Autenticação:** habilite se for necessário informar um usuário e senha para autenticação no servidor de *e-mail*. Se for habilitado, os campos de usuário e senha serão exibidos em tela.

**Figura 5 - Exemplo de configuração de e-mail por empresa**
