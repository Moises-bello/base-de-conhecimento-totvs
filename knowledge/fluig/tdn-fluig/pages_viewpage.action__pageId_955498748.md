---
content_hash: bd441a8dedd00e8dd7a94368d233a471f99ebbdd3ed4ab2260f37bff1a082eff
fetched_at: '2026-06-28T21:35:31.632917+00:00'
page_id: '955498748'
product: fluig
source: tdn-fluig
title: ARQ - Plataforma em load balance com NGINX em Linux da atualização 1.6.3 até
  1.8.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=955498748
version: 5
---

Fique atento!

Esta página é válida para as atualizações **1.6.3 até 1.8.2**do TOTVS Fluig.

Se você utiliza a atualização **Voyager (2.0) ou superior**, acesse a página original Plataforma em *load balance* com NGINX em Linux.

.\*ndice

# Pré-requisitos

---

Para atualizar os parâmetros de configuração, deve-se obedecer aos seguintes pré-requisitos:

* O usuário deve ser administrador da plataforma;
* O usuário deve ter acesso aos arquivos de configuração da plataforma;
* Possuir o NGINX na versão 1.20.1 ou superior instalado. Detalhes de instalação e configuração do NGINX estão disponíveis na [documentação oficial](https://docs.nginx.com/);Importante!

  Somente é possível utilizar o NGINX **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.
* Possuir a configuração de *proxy* reverso;
* Possuir o [nginx-sticky-module-ng](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/src/master/) (módulo externo), para implementar o comportamento de *sticky sessions* sem o uso do NGINX Plus. Esse procedimento só é necessário realizar na versão *open-source* do NGINX.

Atenção!

Antes de prosseguir com as instruções descritas nessa página, siga com atenção as instruções contidas na documentação [Alta disponibilidade e Balanceamento de carga](http://tdn.totvs.com/pages/viewpage.action?pageId=257622931).

# Considerações iniciais

---

A configuração de balanceamento de carga (*load balance*) é a forma mais simples de se obter distribuição de carga e algum nível de alta disponibilidade.

Importante!

Em ambientes com *load balance*, é muito importante manter todos os servidores com o horário sincronizado.

A grande desvantagem é a necessidade de afinidade de sessão, ou seja, uma vez que o usuário foi autenticado em uma instância, sempre será direcionado para a mesma instância. Nesse caso, se essa instância ficar indisponível, o usuário terá que se autenticar novamente na aplicação.

# Instalando a primeira instância

---

Siga os procedimentos abaixo para realizar a instalação da primeira instância do Fluig em um ambiente *load balance.*

falseFirstNodetrue1Passo 1

* Faça uma instalação normal, conforme o , mas **não** inicie os serviços do Fluig.

2Passo 2

* Abra o arquivo **domain.xml** que está disponível em **[diretório\_instalação]/appserver/domain/configuration** em um editor de texto.

3Passo 3

* Localize a propriedade de *binding* "java:global/wcm/globalDataDir" e altere-a informando o caminho da pasta compartilhada entre as instâncias.

  html/xml]]>

* Localize também o *subsystem* "urn:com.totvs.technology.wcm:1.0" e altere-o informando o caminho da pasta compartilhada entre as instâncias.

  html/xml]]>

4Passo 4  

* Mova o conteúdo da pasta **[diretório\_instalação]/repository/wcmdir** para a pasta **GLOBAL\_DATA\_DIR/wcmdir**.

* Mova o conteúdo da pasta **[diretório\_instalação]/appserver/apps** para a pasta **GLOBAL\_DATA\_DIR****/apps**.

5Passo 5

* Configure o servidor de indexação (Fluig Indexer) para ser executado em servidor separado, conforme instruções descritas em .

6Passo 6  

* Inicie os serviços **fluig\_Indexer,** **fluig\_RealTime** e em seguida, inicie o **Fluig**.

* Acesse a plataforma com o usuário "wcmadmin", crie uma nova empresa (*tenant*) e realize as configurações necessárias.

* Pare o **Fluig** e os serviços do **fluig\_RealTime** e **fluig\_Indexer**.

# Criando uma segunda instância na mesma instalação

---

O Fluig permite executar uma segunda instância na mesma instalação, ou seja, sem a necessidade de instalar tudo novamente.

falseSecondInstancetrue1Passo 1

* Abra o arquivo **[diretório\_instalação]/appserver/domain/configuration/host.xml** em um editor de texto.

* Localize a *tag* **<servers>**. Dentro dela existem *tags* chamadas **<server>**.

* Adicione uma nova tag **<server>**, conforme o exemplo:

xmlEclipsehost.xml










]]>2Passo 2

* Certifique-se de que o atributo **name** contenha um valor que jamais será repetido em outra instância.

* A primeira instância **sempre** deverá se chamar "fluig1", enquanto as demais instâncias podem ter qualquer nome definido.

3Passo 3  

* O atributo **auto-start** indica se a instância deve (*true*) ou não (*false*) ser iniciada imediatamente quando o Fluig for iniciado. Se informado ***false***, será preciso iniciá-la manualmente posteriormente, usando a ferramenta **jboss-cli**.  
  A recomendação é que a primeira instância seja iniciada sozinha e posteriormente sejam iniciadas as demais instâncias.

4Passo 4  

* Se desejar ou for necessário, altere o atributo **port-offset** da *tag* **socket-bindings**. Cada nova instância precisa de um valor diferente (múltiplos de 150 são uma boa indicação).

5Passo 5  

* Ajuste as configurações de memória na *tag* **heap**.

É possível adicionar mais instâncias na mesma instalação. Basta replicar toda a seção **<server>** e tomar o cuidado de alterar, pelo menos, os atributos **port-offset** e **name**.

As instâncias que forem configuradas para não iniciar automaticamente (auto-start="false"), devem ser iniciadas manualmente utilizando a ferramenta jboss-cli, que se encontra em **[diretório\_instalação]/****appserver/bin**, com o comando abaixo, de acordo com o sistema operacional:

* **no Linux**:

  bashLinux:9990" --connect --command="/host=master/server-config=fluig2:start"]]>
* **no Windows**:

  bashWindows:9990" --connect --command="/host=master/server-config=fluig2:start"]]>

Onde <ip-da-maquina> é o endereço IP/hostname configurado no arquivo **host.xml** (localizado em [diretório\_instalação]/appserver/domain/configuration), na seção:

    
]]>

# Criando uma instância em outra máquina

---

falseThirdInstance1Passo 1

* Instale a aplicação pelo  e siga as instruções até o procedimento antes de iniciar o servidor.

2Passo 2  

* Abra o arquivo **[diretório\_instalação]/appserver/domain/configuration/host.xml** em um editor de texto.

* Localize a *tag* **<servers>**. Dentro dela existem *tags* chamadas **<server>**.

* Altere o atributo **name** dessas *tags*. O valor desse atributo precisa ser diferente em cada instância.

3Passo 3

* Abra o arquivo **domain.xml** que está disponível em **[diretório\_instalação]/appserver/domain/configuration** em um editor de texto.

4Passo 4

* Localize a propriedade de *binding* "java:global/wcm/globalDataDir" e altere-a informando o caminho da pasta compartilhada entre as instâncias;

  html/xml]]>

* Localize também o *subsystem* "urn:com.totvs.technology.wcm:1.0" e altere-o informando o caminho da pasta compartilhada entre as instâncias.

  html/xml]]>

# Configurando o balanceador

---

O Fluig homologa o NGINX com o *upstream* para fazer o balanceamento de carga.

falseModProxytrue1Passo 1

* Instale o servidor [NGINX](https://nginx.org/en/), versão 1.20.1 ou superior.

2Passo 2

* Configure o módulo [nginx-sticky-module-ng](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/src/master/) no NGINX para utilizar a afinidade de sessão.

3Passo 3

* Habilite o balanceamento com o parâmetro **upstream** (geralmente é feito criando o arquivo **/etc/nginx/nginx.conf** ou **/etc/nginx/conf.d**).

  Atenção!

  Cada “**BalancerMember**” indica um servidor e deve apontar para o IP e a porta corretos.  
  Um *cookie* chamado “**FLUIGCOOKIE**” é criado para manter a afinidade da sessão. Sem o *cookie*, o procedimento não irá funcionar.

  xmlnginx.conf

4Passo 4Load Balance RealTimeImportante!

O procedimento abaixo deve ser realizado para utilizar o serviço de Realtime em Load balance.

**Passos para usar o Load Balance do Realtime**

* Faça a configuração do Realtime para Load Balance conforme descrito em .

* Feitas as configurações acima, adicione o código abaixo no arquivo de configuração do servidor (Passo 3).

  xmlEclipsenginx.conf

5Passo 5Load Balance Bloco completo

* Após efetuar os passos anteriores, o arquivo "/etc/nginx/conf.d" estará desta forma:

  xmlEclipsenginx.conf

# Ambiente HTTPS

---

Quando o Fluig estiver configurado em HTTPS, é necessário que as *flags* de segurança "*Secure*" e "*HttpOnly*" dos *cookies* estejam habilitadas na sessão. Para isso, siga a instrução abaixo:

Importante!

Ao utilizar balanceamento de carga em ambientes com HTTPS, a [configuração de HTTPS](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Configura%C3%A7%C3%A3odeHTTPSmanual) deve ser replicada manualmente para todos os servidores do Fluig.
