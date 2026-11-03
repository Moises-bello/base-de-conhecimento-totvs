---
content_hash: 506257f7813e28fa713420944fa5befa2fc4d8426207b339c31e61de5bdb8bca
fetched_at: '2026-06-28T21:35:31.119472+00:00'
page_id: '876216905'
product: fluig
source: tdn-fluig
title: Plataforma em load balance com NGINX em Linux
type: documentation
url: https://tdn.totvs.com/display/fluig/Plataforma+em+load+balance+com+NGINX+em+Linux
version: 14
---

Fique atento!

Esta página é válida a partir da atualização **Voyager (2.0)** do TOTVS Fluig.

Se você utiliza uma atualização anterior, acesse Plataforma em *load balance* com NGINX em Linux da atualização **1.6.3 até 1.8.2**.

.\*ndice

# Pré-requisitos

---

Para atualizar os parâmetros de configuração, deve-se obedecer aos seguintes pré-requisitos:

* o usuário deve ser administrador da plataforma;

* o usuário deve ter acesso aos arquivos de configuração da plataforma;

* possuir o NGINX na versão 1.20.1 ou superior instalado. Detalhes de instalação e configuração do NGINX estão disponíveis na [documentação oficial](https://docs.nginx.com/);

  Importante!

  Somente é possível utilizar o NGINX **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.
* possuir a configuração de *proxy* reverso;

* possuir o [nginx-sticky-module-ng](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/src/master/) (módulo externo) para implementar o comportamento de *sticky sessions* sem o uso do NGINX Plus. Esse procedimento só é necessário realizar na versão *open-source* do NGINX.

Atenção!

Antes de prosseguir com as instruções descritas nessa página, siga com atenção as instruções contidas na documentação [Alta disponibilidade e balanceamento de carga](http://tdn.totvs.com/pages/viewpage.action?pageId=257622931).

# Considerações iniciais

---

A configuração de balanceamento de carga (*load balance*) é a forma mais simples de se obter distribuição de carga e algum nível de alta disponibilidade.

A grande desvantagem é a necessidade de afinidade de sessão, ou seja, uma vez que o usuário foi autenticado em uma instância, sempre será direcionado para a mesma instância. Nesse caso, se essa instância ficar indisponível, o usuário terá que se autenticar novamente na aplicação.

Importante!

* Em ambientes com *load balance*, é muito importante manter todos os servidores com o horário sincronizado.

* É necessário reiniciar todos os servidores depois de finalizar as configurações.

# Instalando a primeira instância

---

Siga os procedimentos abaixo para realizar a instalação da primeira instância do Fluig em um ambiente *load balance.*

falseFirstNodetrue1Passo 1

* Faça uma instalação normal, conforme o , mas **não** inicie os serviços do Fluig.

2Passo 2

* Abra o arquivo **standalone.xml** que está disponível em **[diretório\_instalação]/appserver/standalone/configuration** em um editor de texto.

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

# Criando uma instância em outra máquina

---

Siga os procedimentos abaixo para criar uma instância em outra máquina.

falseThirdInstance1Passo 1

* Instale a aplicação pelo  e siga as instruções até o procedimento antes de iniciar o servidor.

2Passo 2

* Abra o arquivo **standalone.xml** que está disponível em **[diretório\_instalação]/appserver/standalone/configuration** em um editor de texto.

3Passo 3

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

O procedimento abaixo deve ser realizado para utilizar o serviço de Realtime em *load balance*.

**Passos para usar o *load balance* do Realtime**

* Faça a configuração do Realtime para *load balance* conforme descrito em Configurando o Fluig Realtime para execução em *load balance*.

* Feitas as configurações acima, adicione o código abaixo no arquivo de configuração do servidor.

  xmlEclipsenginx.conf

5Passo 5Load Balance Bloco completo

* Após efetuar os passos anteriores, o arquivo "/etc/nginx/conf.d" estará desta forma:

  xmlEclipsenginx.conf

# Ambiente HTTPS

---

Quando o Fluig estiver configurado em HTTPS, é necessário que as *flags* de segurança "*Secure*" e "*HttpOnly*" dos *cookies* estejam habilitadas na sessão. Para isso, siga a instrução abaixo:

Importante!

Ao utilizar balanceamento de carga em ambientes com HTTPS, a [configuração de HTTPS](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Configura%C3%A7%C3%A3odeHTTPSmanual) deve ser replicada manualmente para todos os servidores do Fluig.
