---
content_hash: 1b50a8821f4d73b2b73894b67ccf713163e5abc45dcfbf3207607b9051934346
fetched_at: '2026-06-28T21:35:26.110824+00:00'
page_id: '337350257'
product: fluig
source: tdn-fluig
title: ARQ - Como configurar a plataforma em load balance com Apache mod_proxy em
  Linux das releases 1.6.0 a 1.6.2?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337350257
version: 5
---

Atenção

Esta página foi revisada para considerar as configurações da atualização 1.6.0 à 1.6.2.

Para atualizações 1.6.3 ou superiores, acesse: .

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** da 1.6.0 à 1.6.2

# Ocorrência

Como configurar a plataforma com balanceamento de carga (*load balance*) utilizando Apache mod\_proxy em Linux das releases 1.6.0 à 1.6.2?

# Solução

Importante

Antes de prosseguir com as instruções descritas nessa página, siga com atenção as instruções contidas na documentação

A configuração em *load balance* é a forma mais simples de se obter distribuição de carga e algum nível de alta disponibilidade.

A grande desvantagem é a necessidade de afinidade de sessão, ou seja, uma vez que o usuário foi autenticado em uma instância, sempre será direcionado para a mesma instância. Nesse caso, se essa instância ficar indisponível, o usuário terá que logar novamente na aplicação.

## Instalando a primeira instância

Siga os procedimentos abaixo para realizar a instalação da primeira instância da plataforma em um ambiente Load Balance.

falseFirstNodetrue1Passo 1

* Faça uma instalação normal, conforme o , mas **não** inicie os serviços da plataforma.

2Passo 2

* Abra em um editor de texto o arquivo **[Instalação fluig]/appserver/domain/configuration/domain.xml** e altere as seguintes configurações:

* Localize a propriedade de *binding* "java:global/wcm/globalDataDir" e altere-a informando o caminho da pasta compartilhada entre as instâncias;

html/xml]]>

* Localize o *subsystem* "urn:com.totvs.technology.wcm:1.0" e altere-o informando o caminho da pasta compartilhada entre as instâncias;

html/xml]]>3Passo 3  

* Abra em um editor de texto o arquivo **[Instalação fluig]/repository/wcmdir/config/configuration.properties** e altere a seguinte configuração:

* Localize a chave "wcm/cacheServerAddress" e altere o valor com o endereço do servidor de cache configurado conforme [recomendação](http://tdn.totvs.com/pages/viewpage.action?pageId=205917413).

4Passo 4  

* Mova o conteúdo da pasta **[Instalação fluig]/repository/wcmdir** para a pasta **GLOBAL\_DATA\_DIR/wcmdir**

* Mova o conteúdo da pasta **[Instalação fluig]/appserver/apps** para a pasta **GLOBAL\_DATA\_DIR****/apps**

5Passo 5

* Configure o fluig Indexer (Solr) para ser executado em servidor separado, conforme instruções [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=257623442).

6Passo 6  

* Inicie os serviços do cache, **fluig\_Indexer** e **fluig\_RealTime** e em seguida inicie o **fluig**.

* Acesse a plataforma com o usuário "wcmadmin", crie uma nova empresa (*tenant*) e realize as configurações necessárias.

* Derrube a plataforma e os serviços do **fluig\_RealTime**, **fluig\_Indexer** e do *cache*.

## Criando uma segunda instância na mesma instalação

É possível executar uma segunda instância na mesma instalação, ou seja, sem a necessidade de instalar tudo novamente.

falseSecondInstancetrue1Passo 1  

* Abra em um editor de texto o arquivo **[Instalação fluig]/appserver/domain/configuration/host.xml**

* Localize a *tag* **<servers>**

* Dentro dela haverão *tags* chamadas **<server>**

* Adicione uma nova tag **<server>**, conforme exemplo:

xml










]]>2Passo 2

* Certifique-se que o atributo **name** contenha um valor que jamais será repetido em outra instância.

* A primeira instância **sempre** deverá se chamar "fluig1", enquanto as demais instâncias podem ter qualquer nome definido.

3Passo 3  

* O atributo **auto-start** indica se a instância deve ser iniciada imediatamente quando a plataforma for iniciada. Se informado **false**, será preciso iniciá-la manualmente posteriormente usando o painel de controle do servidor de aplicação.

4Passo 4  

* Caso desejar ou for necessário, altere o atributo **port-offset** da *tag* **socket-bindings**. Cada nova instância precisa de um valor diferente (múltiplos de 150 são uma boa indicação).

5Passo 5  

* Ajuste as configurações de memória na *tag* **heap**.

É possível adicionar mais instâncias na mesma instalação. Basta replicar toda a seção **<server>** e tomar o cuidado de alterar, pelo menos, os atributos **port-offset** e **name**.

## Criando uma instância em outra máquina

falseThirdInstance1Passo 1

* Instale a aplicação pelo procedimento normal e siga as instruções até o procedimento antes de iniciar o servidor.

2Passo 2  

* Abra em um editor de texto o arquivo **[Instalação fluig]/appserver/domain/configuration/host.xml**.

* Localize a *tag* **<servers>**.

* Dentro dela haverão *tags* chamadas **<server>**. Altere o atributo **name** dessas *tags*. O valor desse atributo precisa ser diferente em cada instância.

## Configurando o balanceador (mod\_proxy)

A plataforma homologa o Apache com o módulo mod\_proxy para fazer o balanceamento de carga.

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

SetHandler balancer-manager
Order Deny,Allow
Allow from all

Order allow,deny
Allow from all
ProxyPass / balancer://mycluster/ stickysession=FLUIGCOOKIE nofailover=Off
ProxyPassReverse / balancer://mycluster/
]]>Atenção

* Cada “BalancerMember” indica um servidor e deve apontar para o IP e porta corretos.

* Um *cookie* chamado “FLUIGCOOKIE” é criado para manter a afinidade da sessão. Sem o *cookie*, o procedimento não irá funcionar.
