---
content_hash: 67b46fde41dbd8c67af7e06284a136ea2865ffc6351e6df338916699de24571d
fetched_at: '2026-06-28T21:35:23.605712+00:00'
page_id: '257623320'
product: fluig
source: tdn-fluig
title: Plataforma em load balance com Apache mod_proxy em Linux
type: documentation
url: https://tdn.totvs.com/display/fluig/Plataforma+em+load+balance+com+Apache+mod_proxy+em+Linux
version: 88
---

Fique atento!

Esta página foi revisada para considerar as configurações de *server* do TOTVS Fluig para a atualização **1.6.3** ou **superiores**.

Para atualizações entre 1.6.0 e 1.6.2 acesse:

.\*ndice

# Pré-requisitos

---

Para atualizar os parâmetros de configuração, deve-se obedecer aos seguintes pré-requisitos:

* O usuário deve ser administrador da plataforma;

* O usuário deve ter acesso aos arquivos de configuração da plataforma.

Atenção!

Antes de prosseguir com as instruções descritas nessa página, siga com atenção as instruções contidas na documentação [Alta disponibilidade e Balanceamento de carga](http://tdn.totvs.com/pages/viewpage.action?pageId=257622931)

# Considerações iniciais

---

A configuração de balanceamento de carga (*load balance)* é a forma mais simples de se obter distribuição de carga e algum nível de alta disponibilidade.

Importante!

Em ambientes com *load balance*, é muito importante manter todos os servidores com o horário sincronizado.

A grande desvantagem é a necessidade de afinidade de sessão, ou seja, uma vez que o usuário foi autenticado em uma instância, sempre será direcionado para a mesma instância. Nesse caso, se essa instância ficar indisponível, o usuário terá que logar novamente na aplicação.

# Instalando a primeira instância

---

Siga os procedimentos abaixo para realizar a instalação da primeira instância do Fluig em um ambiente *load balance.*

falseFirstNodetrue1Passo 1

* Faça uma instalação normal, conforme o , mas **não** inicie os serviços do Fluig.

2Passo 2

* **A partir da atualização 2.0**:  
  Abra o arquivo **standalone.xml** que está disponível em **[diretório\_instalação]/appserver/standalone/configuration** em um editor de texto.

* **Para atualizações 1.6.3 até 1.8.2**:  
  Abra o arquivo **domain.xml** que está disponível em **[diretório\_instalação]/appserver/domain/configuration** em um editor de texto.

3Passo 3

* No arquivo correspondente à atualização do Fluig que você utiliza (**standalone.xml** ou **domain.xml**), localize a propriedade de *binding* "java:global/wcm/globalDataDir" e altere-a informando o caminho da pasta compartilhada entre as instâncias;

html/xml]]>

* Localize o *subsystem* "urn:com.totvs.technology.wcm:1.0" e altere-o informando o caminho da pasta compartilhada entre as instâncias;

html/xml]]>4Passo 4  

* Mova o conteúdo da pasta **[diretório\_instalação]/repository/wcmdir** para a pasta **GLOBAL\_DATA\_DIR/wcmdir**

* Mova o conteúdo da pasta **[diretório\_instalação]/appserver/apps** para a pasta **GLOBAL\_DATA\_DIR****/apps**

5Passo 5

* Configure o servidor de indexação (fluig Indexer) para ser executado em servidor separado, conforme instruções [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=257623442).

6Passo 6  

* Inicie os serviços **fluig\_Indexer,** **fluig\_RealTime** e em seguida, inicie o **fluig**.

* Acesse a plataforma com o usuário "wcmadmin", crie uma nova empresa (*tenant*) e realize as configurações necessárias.

* Pare o **fluig** e os serviços do **fluig\_RealTime** e **fluig\_Indexer.**

# Criando uma segunda instância na mesma instalação

---

O Fluig permite executar uma segunda instância na mesma instalação, ou seja, sem a necessidade de instalar tudo novamente.

falseSecondInstancetrue1Passo 1

* Abra em um editor de texto o arquivo **[diretório\_instalação]/appserver/domain/configuration/host.xml**

* Localize a *tag* **<servers>**

* Dentro dela haverão *tags* chamadas **<server>**

* Adicione uma nova tag **<server>**, conforme exemplo:

xmlEclipsehost.xml










]]>2Passo 2

* Certifique-se que o atributo **name** contenha um valor que jamais será repetido em outra instância.

* A primeira instância **sempre** deverá se chamar "fluig1", enquanto as demais instâncias podem ter qualquer nome definido.

3Passo 3  

* O atributo **auto-start** indica se a instância deve (true) ou não (false) ser iniciada imediatamente quando o Fluig for iniciado. Se informado **false**, será preciso iniciá-la manualmente posteriormente usando a ferramenta **jboss-cli**. A recomendação é que a primeira instância seja iniciada sozinha e posteriomente sejam iniciadas as demais instâncias.
4Passo 4  

* Caso desejar ou for necessário, altere o atributo **port-offset** da *tag* **socket-bindings**. Cada nova instância precisa de um valor diferente (múltiplos de 150 são uma boa indicação).

5Passo 5  

* Ajuste as configurações de memória na *tag* **heap**.

É possível adicionar mais instâncias na mesma instalação. Basta replicar toda a seção **<server>** e tomar o cuidado de alterar, pelo menos, os atributos **port-offset** e **name**.

As instâncias que forem configuradas para não iniciar automaticamente (auto-start="false") devem ser iniciadas manualmente utilizando a ferramenta jboss-cli, que se encontra em **[diretório\_instalação]/****appserver/bin**, com o seguinte comando:

No Linux:

bashLinux:9990" --connect --command="/host=master/server-config=fluig2:start"]]>

No Windows:

bashWindows:9990" --connect --command="/host=master/server-config=fluig2:start"]]>

Onde <ip-da-maquina> é o endereço IP/hostname configurado no arquivo **host.xml** (localizado em [diretório\_instalação]/appserver/domain/configuration), na seção:

    
]]>

```

```

# Criando uma instância em outra máquina

---

falseThirdInstance1Passo 1

* Instale a aplicação pelo  e siga as instruções até o procedimento antes de iniciar o servidor.

2Passo 2  

* Abra em um editor de texto o arquivo **[diretório\_instalação]/appserver/domain/configuration/host.xml**.

* Localize a *tag* **<servers>**.

* Dentro dela haverão *tags* chamadas **<server>**. Altere o atributo **name** dessas *tags*. O valor desse atributo precisa ser diferente em cada instância.

# Configurando o balanceador (mod\_proxy)

---

O Fluig homologa o Apache com o módulo mod\_proxy para fazer o balanceamento de carga.

falseModProxytrue1Passo 1

* Instale o servidor [HTTP Apache](https://httpd.apache.org/download.cgi), versão 2.4.x.

2Passo 2

* Configure o Apache para carregar os módulos necessários (comumente feito através do arquivo **/etc/apache2/mods-enabled/mod\_proxy.load**), conforme abaixo.

A ordem de carregamento dos módulos é extremamente importante.

text

* A primeira linha indica o tipo de balanceamento que será feito. No exemplo acima, ele é feito por carga do servidor. Para conhecer outras formas, [consulte o manual](https://httpd.apache.org/docs/2.4/mod/mod_proxy_balancer.html) do Apache.

3Passo 3

* Habilite o mod\_proxy (em geral isso é feito criando o arquivo **/etc/apache2/sites-enabled/mod\_proxy.conf**).

xml
ProxyRequests Off
ProxyPreserveHost On
BalancerMember http://{ip servidor 1}:8080 route=fluig1
BalancerMember http://{ip servidor 1}:8230 route=fluig2
BalancerMember http://{ip servidor 2}:8230 route=fluig3
ProxySet stickysession=FLUIGCOOKIE

SetHandler balancer-manager
Order Deny,Allow
Allow from all

Order allow,deny
Allow from all
ProxyPass / balancer://mycluster/ stickysession=FLUIGCOOKIE nofailover=Off
ProxyPassReverse / balancer://mycluster/
]]>Atenção!

* Cada “BalancerMember” indica um servidor e deve apontar para o IP e porta corretos.

* Um *cookie* chamado “FLUIGCOOKIE” é criado para manter a afinidade da sessão. Sem o *cookie*, o procedimento não irá funcionar.
4Passo 4Load Balance RealTimeAtenção!

O procedimento abaixo deve ser realizado para utilizar o serviço de Realtime em Load balance.

## Passos para usar o Load Balance do Realtime

---

* Realizar a configuração do Realtime para Load Balance conforme apresentado em .
* Adicionar o módulo abaixo, ao final dos demais módulos citados no passo 2.

text

* Realizadas as configurações acima, adicionar o código abaixo ao arquivo de configuração do servidor (Passo 3).

ProxyRequests Off
ProxyPreserveHost On
BalancerMember http://{ip servidor realtime1}:8888 route=load1
BalancerMember http://{ip servidor realtime2}:8888 route=load2
ProxySet stickysession=SERVERID

SetHandler balancer-manager
Order Deny,Allow
Allow from all

Order allow,deny
Allow from all
ProxyPass / balancer://mycluster1/ stickysession=SERVERID nofailover=Off
ProxyPassReverse / balancer://mycluster1/
Listen 7777
Header add Set-Cookie "SERVERID=sticky.%{BALANCER\_WORKER\_ROUTE}e; path=/" env=BALANCER\_ROUTE\_CHANGED
AllowConnect 7777
ProxyRequests Off
ProxyPreserveHost On
BalancerMember http://{ip servidor realtime1}:7777 route=read1
BalancerMember http://{ip servidor realtime2}:7777 route=read2
ProxySet stickysession=SERVERID

BalancerMember ws://{ip servidor realtime1}:7777 route=read1
BalancerMember ws://{ip servidor realtime2}:7777 route=read2
ProxySet stickysession=SERVERID
RewriteEngine On
RewriteCond %{HTTP:Upgrade} =websocket [NC]
RewriteRule /(.\*) balancer://nodes\_ws/$1 [P,L]
RewriteCond %{HTTP:Upgrade} !=websocket [NC]
RewriteRule /(.\*) balancer://nodes\_polling/$1 [P,L]
]]>

# Ambientes HTTPS

---

Quando o usuário estiver usando um ambiente HTTPS, é necessário que as *flags* de segurança "*Secure*" e "*HttpOnly*" dos *cookies* estejam habilitadas na sessão. Para isso, siga a instrução abaixo:

* Editar o arquivo **/etc/apache2/sites-enabled/mod\_proxy.conf** e adicionar a seguinte linha no final do arquivo:

Importante!

Ao utilizar balanceamento de carga em ambientes com HTTPS, a [configuração de HTTPS](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Configura%C3%A7%C3%A3odeHTTPSmanual) deve ser replicada manualmente para todos os servidores do Fluig.
