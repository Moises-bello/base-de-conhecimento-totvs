---
content_hash: 6c4d1c0e055e36c32861c7e1e425927742c9eb3fc6f08f3790f3da8375196f52
fetched_at: '2026-06-28T21:35:19.884003+00:00'
page_id: '224124221'
product: fluig
source: tdn-fluig
title: CON - Como configurar o envio de e-mail na release 1.5.6 ou anterior?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224124221
version: 7
---

Atenção

Página destinada a atualizações 1.5.6 e inferiores do TOTVS Fluig Plataforma.

Caso possua uma atualização 1.6 ou superior, acesse:

Para atualizações 1.5.6 a 1.5.13, acesse:

# Índice

4true.\*ndicenone

# Objetivo

O objetivo desta página é realizar a configuração de envio de *e-mail* no TOTVS Fluig Plataforma.

Importante

Clientes que possuem a plataforma hospedada no Cloud não terão acesso para verificar as configurações abaixo.

Nesse caso entre em contato com o Atendimento ou com o Cloud através de *ticket* ou e-mail para que a equipe verifique.

# Configuração de envio de *e-mail*

Para realizar a configuração de envio de *e-mail* na plataforma é preciso, em primeiro lugar, parar todos os serviços iniciados: FLUIG, Fluig\_MemCached e Fluig\_RealTime. Depois disso, basta seguir os passos abaixo:

0.5falsesamplesfadetrue1Passo 1

* Após **parar os serviços** do fluig acesse o diretório [diretório\_instalação]\jboss\standalone\configuration.

2Passo 2

* Edite o arquivo **standalone.xml**.  
   

  Procure pelos seguintes parâmetros:

  + **fluig/mail.defaultSender**: informe "**true**" para habilitar o envio de *e-mail* utilizando o *e-mail* informado no parâmetro "fluig/mail.from";
  + **fluig/mail.from**: informe o endereço de *e-mail* que deve ser utilizado para enviar os *e-mails* do sistema;
  + **fluig/mail.personal**: preencha para definir um nome junto ao *e-mail* de origem, por exemplo para identificar a empresa. Exemplo da exibição: NOME\_DA\_EMPRESA [adm@fluig.com](mailto:adm@fluig.com);
  + **fluig/mail.allNotification**: informe "**true**" para que todos os *e-mails* do produto sejam enviados com o *e-mail* informado no parâmetro "fluig/mail.from".

  Procure por "**mail-smtp**" para encontrar o bloco de configuração abaixo e altere "**host**" e "**port**" de acordo com a necessidade:

  xmlEclipsestandalone.xml



  ]]>

3Passo 3

* Para configuração do *e-mail* utilizando TLS procure por "**java:jboss/mail/Default**" para encontrar o bloco de configuração abaixo:

  xmlEclipsestandalone.xml



  ]]>

4Passo 4

* Substitua esse bloco de acordo com o exemplo abaixo e preencha os dados, lembrando de adicionar o parâmetro **tls="true"**:

  xmlEclipsestandalone.xml










  ]]>

  Salve o arquivo e inicie os três serviços do fluig.
