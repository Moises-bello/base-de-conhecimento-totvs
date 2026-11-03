---
content_hash: 3ad6daf06014837ea10803c856dad714ce14ea4f8c2fa47d0e25161425309683
fetched_at: '2026-06-28T21:35:18.934986+00:00'
page_id: '185756210'
product: fluig
source: tdn-fluig
title: CON - Como configurar o envio de e-mail da release 1.5.6 à 1.5.13?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185756210
version: 34
---

Atenção

Página destina a atualização 1.5.6 à 1.5.13 do TOTVS Fluig Plataforma.

Acesse a página original a partir da atualização 1.6: .

Caso possua uma atualização anterior à 1.5.6 acesse:

# Índice

4true.\*ndicenone

# Objetivo

O objetivo desta página é realizar a configuração de envio de *e-mail* no TOTVS Fluig Plataforma.

Importante

Clientes que possuem a plataforma hospedada no Cloud não terão acesso para verificar as configurações abaixo.

Nesse caso entre em contato com o Atendimento ou com o Cloud através de um *ticket* ou *e-mail* para que a equipe verifique.

# Configuração de envio de *e-mail*

Logado com o usuário **wcmadmin**, na tela de configurações clique em **Painel de Controle** → aba **WCM** → **Configurações do Sistema** → aba **Parâmetros da Plataforma**:  
Edite as opções da seção **Notificações por *e-mail***: 

* **Remente padrão**: ative para habilitar o envio de *e-mail* utilizando o *e-mail* informado no parâmetro "***E-mail* do remetente**";
* ***E-mail* do remetente**: informe o endereço de *e-mail* que deve ser utilizado para enviar os *e-mails* do sistema;
* **Nome do remetente**: preencha para definir um nome junto ao *e-mail* de origem, por exemplo para identificar a empresa. Exemplo da exibição: NOME\_DA\_EMPRESA [adm@fluig.com](mailto:adm@fluig.com);
* **Todas notificações por *e-mail***: ative para que todos os *e-mails* do produto sejam enviados com o *e-mail* informado no parâmetro "***E-mail* do remetente**".

### Configuração de *e-mail* global

Para realizar o restante da configuração de envio de *e-mail* na plataforma é preciso, parar todos os serviços iniciados: FLUIG, Fluig\_MemCached e Fluig\_RealTime.

Depois disso, basta seguir os passos abaixo para configuração de e-mail global (desta maneira, todas as empresas terão a mesma configuração de envio de *e-mail*).

Tudo o que for configurado como global, se extenderá para todas as empresas cadastradas. Para um cadastro individual, utiliza-se então a configuração de *e-mail* .

0.5falsesamplesfadetrue1Passo 1

* Após **parar os serviços do fluig** acesse o diretório [diretório\_instalação]\jboss\standalone\configuration.

2Passo 2  

* Edite o arquivo **standalone.xml**.  
   

  Procure por "**mail-smtp**" para encontrar o bloco de configuração abaixo e altere "**host**" e "**port**" de acordo com a necessidade:

  xmlEclipsestandalone.xml



  ]]>

3Passo 3

* Para configuração do *e-mail* utilizando TLS procure por "**java:jboss/mail/Default**" para encontrar o bloco de configuração abaixo:

  xmlEclipsestandalone.xml



  ]]>

A plataforma aceita apenas o protocolo de segurança TLS. O padrão SSL não é suportado.

4Passo 4

* Substitua esse bloco de acordo com o exemplo abaixo e preencha os dados, lembrando de adicionar o parâmetro **tls="true"**:

  xmlEclipsestandalone.xml










  ]]>

  Salve o arquivo e inicie os três serviços do fluig.

empresa

### Configuração de *e-mail* por empresa

Caso desejar configurar o envio de *e-mail* de uma empresa específica diferente dos parâmetros globais, acesse o cadastro da Empresa → aba "*E-mail*".

No cadastro por empresa, cada configuração será feita individualmente e as ações só valerão para a empresa em questão.

Caso alguma alteração seja feita no configuração global, o sistema sempre dará preferência para as configurações aplicadas por empresa.

Preencha os campos de acordo com a orientação a seguir:

* **Host:** endereço do servidor de envio de *e-mails* (SMTP);
* **Porta:** porta para SSL ou TLS;
* **Remetente:** endereço de *e-mail* do remetente;
* **Segurança:** habilite se o servidor de e-mail utilizar TLS. Somente o protocolo TLS é suportado na plataforma;
* **Autenticação:** habilite se for necessário informar um usuário e senha para autenticação no servidor de *e-mail*. Se for habilitado, os campos de usuário e senha serão exibidos em tela.

Observação

É importante lembrar que os dados variam de acordo com o servidor de envio de *e-mail* utilizado.

Se tiver dúvidas consulte a documentação do fornecedor ou entre em contato com o administrador de TI da sua empresa.
