---
content_hash: 6951135e0649b16c31d3754809726148b74d05059d9a34ce4ce6a6ee0e5737c6
fetched_at: '2026-06-28T21:35:23.589548+00:00'
page_id: '257623206'
product: fluig
source: tdn-fluig
title: Servidor de indexação em alta disponibilidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623206
version: 69
---

oculto

Para atualizações 1.5.6 à 1.5.13 acesse: [Como configurar o fluig Indexer para executar em cluster da release 1.5.6 à 1.5.13?](https://tdn.totvs.com/x/zhy7K). *[essa página está arquivada, mas caso seja necessário, solicitar para alguém de Gestão do Conhecimento].*

Nota:

Esta página foi revisada para considerar as configurações do serviço de indexação a partir da **Atualização Crystal Mist (1.8.2)**.

Caso possua uma atualização **1.6.4 à 1.8.1** acesse: .

Caso possua uma atualização **1.6.0 à 1.6.3** acesse: .

# Índice

4true.\*ndicenone

# Introdução

---

As instruções a seguir completarão a instalação de um Servidor de indexação em um *cluster* de servidores dedicados, continuando as instruções iniciadas na página .

Na maioria dos cenários, uma máquina bem dimensionada executando o serviço de indexação é suficiente para atender as demandas de indexação e busca da plataforma.

Sendo assim, as configurações apresentadas nesta página são consideradas avançadas, com maior necessidade de administração do ambiente e recomendadas apenas em casos específicos, quando a busca é uma funcionalidade crítica, ou quando se faz necessário garantir a alta disponibilidade deste serviço.

# Redundância

---

O serviço de indexação na plataforma é realizado pelo Apache® Solr. Em um ambiente de alta disponibilidade, são necessárias mais máquinas com este serviço rodando para, no caso de uma delas falhar, ter outras para continuar processando as requisições e, neste caso, o gerenciamento destas requisições será realizado pelo Apache® ZooKeeper.

Para garantir a alta disponibilidade desta funcionalidade, é necessário que exista redundância em ambos os serviços: Apache® Solr para indexação/busca e Apache® ZooKeeper para gerenciamento das configurações de indexação e das requisições. Também é necessário que todas as máquinas do *cluster* sejam acessíveis entre si (estejam na mesma rede).

O princípio de funcionamento do Apache® ZooKeeper é baseado em *quorum*, ou seja, é necessário que a maioria (>50%) dos servidores estejam disponíveis para o processamento das requisições.

Por exemplo, se existirem apenas dois servidores e um deles ficar indisponível, apenas 50% dos servidores estarão saudáveis e, como isso não é a maioria, o *cluster* será incapaz de processar as requisições. Por outro lado, se existirem três servidores e um ficar indisponível, ainda restarão dois saudáveis, ou 66%, atendendo ao critério de maioria. Por esse motivo é recomendado um número ímpar de servidores executando o Apache® ZooKeeper.

# Configurando o Apache® ZooKeeper

---

O primeiro passo é efetuar o *download* da versão 3.9.1 do Apache® ZooKeeper, que pode ser obtida no endereço <https://archive.apache.org/dist/zookeeper/zookeeper-3.9.1/>.

Após efetuar o *download* e extrair o arquivo compactado no diretório de sua preferência [ZOOKEEPER\_HOME] em cada uma das máquinas do *cluster*, é necessário criar, caso ainda não exista, o arquivo [ZOOKEEPER\_HOME]/conf/zoo.cfg com o seguinte conteúdo:

bashEclipsezoo.cfg:2888:3888
server.2=:2888:3888
server.3=:2888:3888]]>

* **tickTime*:*** corresponde ao tempo em milissegundos entre cada *tick*, sendo que uma das validações para determinar se um nó está disponível é de dois *ticks* (similar ao *ping* para verificar se uma máquina é encontrada na rede). Se dois *ticks* consecutivos não obtiverem resposta, ocorre *timeout* e a máquina é considerada indisponível.

* **dataDir**: aponta o diretório onde serão armazenadas as informações referentes ao *cluster.* No início, este diretório deve estar vazio e com permissão de escrita pelo usuário que irá iniciar o ZooKeeper. **O mapeamento deve ser feito sempre com o caracter '/', mesmo em ambientes Windows.**

* **clientPort**: corresponde à porta que será utilizada pelo Apache® Solr.

* **initLimit**: quantidade de tempo (em *ticks*) para que uma máquina com ZooKeeper se conecte e sincronize com a máquina que foi eleita líder. Neste caso, são 5 *ticks* com 2000 milissegundos cada, totalizando 10 segundos. Este valor pode ser incrementado sob demanda se a quantidade de informações gerenciadas pelo ZooKeeper for elevada.

* **syncLimit**: quantidade de tempo (em *ticks*) que uma máquina com ZooKeeper pode estar atrasada em relação à líder. Se uma máquina não conseguir sincronizar com a líder neste intervalo, ela será descartada do *cluster*.

* **4lw.commands.whitelist**: lista de comandos que o ZooKeeper tem permissão para executar.

* **admin.serverPort**: por padrão, o ZooKeeper roda um servidor Jetty na porta 8080. Fica a seu critério escolher a porta, desde que não esteja sendo utilizada por outra aplicação. Basta remover o caractere # da propriedade e alterar o valor da porta.

* **server.X**: são os IDs e localização (endereço na rede interna) de todos os nós do *cluster* e as portas nas quais eles se comunicam entre si. O ID identifica cada nó do *cluster*, precisando ser referenciado em um arquivo de nome 'myid', dentro do diretório definido na propriedade 'dataDir'. Neste exemplo seria necessário criar o arquivo '/var/lib/zookeeperdata/myid' com o conteúdo '1' (sem aspas) para a máquina configurada na propriedade 'server.1', o mesmo arquivo com conteúdo '2' (sem aspas) para a máquina configurada na propriedade 'server.2', e assim por diante, para cada máquina existente no *cluster*. As portas **2888** e **3888** serão utilizadas para comunicação entre cada uma das máquinas do *cluster* e podem ser alteradas de acordo com a necessidade, desde que informadas na linha correspondente ao servidor em questão, no arquivo 'zoo.cfg' de todas as máquinas do *cluster*.

Importante!

Certifique-se de que o arquivo "myid" foi criado corretamente em cada máquina (na pasta definida pela propriedade dataDir), tendo o ID numérico do servidor como conteúdo.

Com essa configuração em cada máquina do *cluster*, basta iniciá-las com o seguinte comando:

bashEclipseNo Linux/bin
zkServer.sh start zoo.cfg]]>bashEclipseNo Windows/bin
zkServer.cmd]]>

# Configurando o Apache® Solr

---

A instalação do Apache® Solr pode ser realizada através da instalador do Fluig no modo caractere, seguindo o passo a passo para instalar somente o Servidor de indexação em [Windows](http://tdn.totvs.com/pages/viewpage.action?pageId=274325941#Instala%C3%A7%C3%A3oWindows-ModoCaractere-PassoapassoparainstalarsomenteoServidordeIndexa%C3%A7%C3%A3o) ou [Linux](http://tdn.totvs.com/pages/viewpage.action?pageId=152797808#Instala%C3%A7%C3%A3oLinux-ModoCaractere-PassoapassoparainstalarsomenteoServidordeIndexa%C3%A7%C3%A3o).

Para existir redundância, deve conter no mínimo duas máquinas executando este serviço de indexação, podendo estas serem as mesmas máquinas que executam o serviço de gerenciamento (ZooKeeper) ou máquinas distintas na mesma rede, dependendo da arquitetura desejada de tolerância à falhas.

O Solr possui dois modos de inicialização: Standalone e Cloud. Em um ambiente de alta disponibilidade, é necessário utilizar o modo Cloud, apontando para os servidores onde estão sendo executados os serviços de gerenciamento das configurações e requisições (ZooKeeper). Para isso, basta incluir o parâmetro ZK\_HOST no arquivo de configuração do Servidor de indexação, conforme exemplo abaixo:

bashEclipseInicializando o Solr no modo cloud:2181,:2181,:2181"
SOLR\_HOST=""
SOLR\_IP\_ALLOWLIST=",,"]]>

Neste caso, os endereços <server1\_address>, <server2\_address> e <server3\_address> no item ZK\_HOST são os mesmos informados anteriormente nos parâmetros '**server.X'** do arquivo '**zoo.cfg'**, e a porta 2181 corresponde ao parâmetro **clientPort** informado nesse mesmo arquivo. As aspas devem ser mantidas.

O parâmetro <server> utilizado no item SOLR\_HOST se refere ao endereço ou IP do próprio servidor que está configurando. As aspas devem ser mantidas.

Os parâmetros IP utilizados no item SOLR\_IP\_ALLOWLIST restringem o acesso ao Solr, garantindo que qualquer chamada de um IP/hostname diferente dos que foram configurados será bloqueada. Esta propriedade é **imprescindível** para aumentar a **segurança** do ambiente. Para mais informações, consulte a [documentação do Solr](https://solr.apache.org/guide/solr/9_4/deployment-guide/securing-solr.html#ip-access-control).

A localização deste arquivo de configuração varia de acordo com o sistema operacional e pode ser verificada na tabela abaixo:

| Sistema operacional | Arquivo de configuração | Localização |
| --- | --- | --- |
| Linux | [fluig\_Indexer.in](http://fluig_indexer.in/).sh | /etc/default/ |
| Windows | [solr.in](http://solr.in/).cmd | [Instalação fluig Indexer]/solr/bin/ |

**Após esta configuração, é necessário iniciar os serviços do Solr (fluig\_Indexer) em todas as máquinas que o executarão para seguir com os próximos passos.**

Importante!

O serviço de gerenciamento (ZooKeeper) deve ser iniciado antes do serviço de indexação (Solr), caso contrário, este último irá considerar que não há serviço de gerenciamento disponível.

# Configurações de indexação

---

Quando o Apache® Solr é executado no modo Cloud, as configurações do índice são armazenadas e gerenciadas pelo Apache® ZooKeeper. Por isso, primeiramente é necessário publicar as configurações utilizadas pela plataforma. Estas configurações são instaladas juntamente com o serviço de indexação e para publicá-las no serviço de gerenciamento (ZooKeeper), pode-se utilizar o comando abaixo:

bashEclipsePublicando configurações de indexação da plataforma/bin/solr zk upconfig -d fluig -n fluig -z :2181,:2181,:2181]]>

* O parâmetro '**-d** fluig' corresponde ao nome do diretório onde estão armazenadas as configurações utilizadas pela plataforma, instaladas por padrão juntamente com o serviço de indexação, no diretório 'fluig'. O comando irá efetuar o *upload* deste diretório para os endereços informados no parâmetro '**-z**'.
* O parâmetro '**-n** fluig' corresponde ao nome que esta configuração irá receber no serviço de gerenciamento (ZooKeeper) e será utilizado no próximo passo (criação da *collection*).
* O parâmetro '**-z'** informa a lista de serviços de gerenciamento (ZooKeeper) onde serão publicadas estas configurações, conforme detalhado anteriormente.

Importante!

Como existe o ZooKeeper para gerenciar o *cluster*, este comando precisa ser executando apenas em uma das máquinas do Solr.

# Criação de *collection*

---

Cada empresa (*tenant*) criada no Fluig é mapeada para uma ***collection*** no Apache® Solr. Quando em *cluster*, é necessário definir a quantidade de nós (*shards*) em que o índice será dividido e o fator de replicação (*replicationFactor*) das informações referentes a esta *collection*, através do seguinte comando:

bashEclipseCriando collection/bin/solr create\_collection -c  -d fluig -shards 1 -replicationFactor 2]]>

* Informe o código numérico que será usado para a empresa criada no Fluig em <ID do Tenant>.
* Neste caso o parâmetro '**-d**' corresponde ao nome da configuração armazenada no ZooKeeper (parâmetro '**-n**' do comando utilizado anteriormente para *upload*).
* Informe o número total de instâncias do Apache® Solr após o parâmetro '-replicationFactor'**.**

Importante!

Como existe o ZooKeeper para gerenciar o *cluster*, este comando precisa ser executando apenas em uma das máquinas do Solr, mas **as outras máquinas precisam estar com o Solr em execução**.

# Configurando o Fluig para usar o Servidor de indexação

---

Se o Fluig estiver em **execução**, siga os passos abaixo:

0.5falsefifadetrue1Passo 1

* Acesse o Fluig com o usuário '**wcmadmin**':

2Passo 2

* Clique no menu **Painel de Controle → Aba WCM → Configurações do Sistema**:

3Passo 3

* Clique na aba **Parâmetros da Plataforma** e localize as configurações do Servidor de **Indexação**:

4Passo 4

* **Configure** da seguinte forma:
  + **URL de acesso ao Solr**:  Devem ser informados os endereços dos servidores onde estão sendo executados os serviços de gerenciamento (ZooKeeper), em uma lista de endereços separados por vírgula, da mesma forma que foram informados no parâmetro '**-z**' ao iniciar os serviços de indexação (Solr).
  + **Solr em Servidor Remoto**: Deve estar ativado (ON).
  + **Solr em Cluster**: Deve estar ativado (ON). Esta opção ativa o Solr em *Cluster*, necessária para ambientes em *Cluster*.

5Passo 5

* As alterações nos parâmetros exigem a reinicialização da plataforma. Portanto inicie os serviços na ordem correta.

Se o Fluig estiver **parado**, siga os passos abaixo:

0.5falsefi2fadetrue1Passo 1

* No servidor onde está instalado o Fluig, acesse o diretório [Instalação fluig]/repository/wcmdir/config e edite o arquivo . Caso o arquivo configuration.properties não exista, crie um novo arquivo com este nome.

jsEclipseconfiguration.properties

* Modifique o parâmetro '**totvs/solrURL**' informando a lista de endereços dos servidores onde estão sendo executados os serviços de gerenciamento, da mesma forma que foram informados no parâmetro '**-z**' ao iniciar os serviços de indexação (Solr). Deverá ser informado **apenas** o **IP** ou***hostname*** do servidor e a **porta**, sem o protocolo e contexto.

Importante!

O parâmetro '**totvs/solrCloud**' irá condicionar o Fluig para ativar a opção do Solr em *Cluster*, necessária para ambientes em *Cluster*.

2Passo 2

* Inicie os serviços do Fluig na ordem correta.

$("b:contains('oculto')").parent().parent().hide();
]]>
