---
content_hash: 832d07b25c1df5cb483c04e73038ca1117a9d8e080e32956200eb25cf1b6f90a
fetched_at: '2026-06-28T21:35:26.154918+00:00'
page_id: '344470997'
product: fluig
source: tdn-fluig
title: ARQ - Como configurar o Servidor de indexação para executar em cluster da release
  1.6.0 a 1.6.3?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344470997
version: 10
---

Atenção

Esta página é válida da atualização **1.6.0** à **1.6.3** do TOTVS Fluig Plataforma.

Caso possua uma atualização **1.6.4** à **1.8.1**, acesse: [ARQ - Como configurar o Servidor de indexação para executar em cluster da release 1.6.4 à 1.8.1?](https://tdn.totvs.com/pages/viewpage.action?pageId=804798298).

Caso possua a **Atualização Crystal Mist (1.8.2)**, acesse: .

# Índice

4true.\*ndicenone

# Introdução

As instruções a seguir completarão a instalação de um servidor de indexação em um *cluster* de servidores dedicados, continuando as instruções iniciadas na página .

# Fluig Indexer Primary

Somente um dos servidores precisa ser eleito como **Primary**. Nele será executado o processo de coordenação dos nós do *cluster* de servidores (*ZooKeeper*).

* Execute o script [Fluig Indexer]/solr/startCloudMaster.sh (Linux) ou [Fluig Indexer]\solr\startCloudMaster.bat (Windows) para iniciar o Fluig Indexer.

* Para interromper, execute o arquivo [Fluig Indexer]/solr/stopCloud.sh (Linux) ou [Fluig Indexer]\solr\stopCloud.bat (Windows).

Atenção!

É importante que o Fluig Indexer seja iniciado antes do Fluig, caso contrário o Fluig irá considerar que não há Serviço de Indexação disponível.

# Fluig Indexer Secondary

Um ou mais servidores podem ser utilizados como **Secondary**.

* Edite o arquivo [Fluig Indexer]/solr/startCloudSlave.sh (Linux) ou [Fluig Indexer]\solr\startCloudSlave.bat (Windows) para configurar o **IP e porta** do processo de coordenação (*ZooKeeper*) do *cluster* de indexação que é executado no servidor Primary (informado após o parâmetro -z).

bashEclipseNo LinuxbashEclipseNo Windows

* Se desejar subir duas instâncias na mesma máquina ou apenas subir o **Fluig Indexer** em outra porta, adicione o parâmetro "-p". e informe a porta.

* Nesse caso também é necessário adicionar o mesmo parâmetro nos *scripts*de interrupção do serviço: [Fluig Indexer]/solr/stopCloud.sh (Linux) ou [Fluig Indexer]\solr\stopCloud.bat (Windows).

bashEclipseNo LinuxbashEclipseNo WindowsAtenção!

É importante que o Fluig Indexer Primary seja iniciado antes do Fluig Index Secondary, caso contrário este último irá considerar que não há Serviço de Coordenação disponível.

# Configurando o Fluig para usar o Indexer

Se o **Fluig** tiver em **execução**, siga os passos abaixo:

0.5falseSamplefadetrue1Passo 1

* Acesse a plataforma com o usuário '**wcmadmin**':

2Passo 2

* Clique no menu **Painel de Controle → Aba WCM → Configurações do Sistema**:

3Passo 3

* Clique na Aba **Parâmetros da Plataforma** e localize as configurações do Servidor de**Indexação**:

4Passo 4

* **Configure** da seguinte forma:
  + **Diretório do Solr**: Incluir o caminho para a pasta do Solr.
  + **URL de acesso ao Solr**:  Deve ser informando o endereço do servidor onde está sendo executado o**Fluig Indexer Primary.**Deverá ser incluido da seguinte forma: http://[Host Servidor Primary]:[Porta].  A porta utilizada será a do serviço de coordenação do *cluster* que por padrão é a porta do 9983.
  + **Solr em Servidor Remoto**: Deve estar ativado (ON).
  + **Solr em Cluster**: Deve estar ativado (ON). Esta opção ativa o Solr em *Cluster*, necessária para ambientes em *cluster*.

5Passo 5

* As alterações nos parâmetros exigem a reinicialização da plataforma. Portanto inicie os serviços na ordem correta.

Se o **Fluig** estiver **parado**, siga os passos abaixo:

No servidor onde está instalada a plataforma, acesse o diretório [Instalação fluig]/repository/wcmdir/config e edite o arquivo **[configuration.properties](http://tdn.totvs.com/pages/viewpage.action?pageId=257623022)**. Caso o arquivo configuration.properties não exista, crie um novo arquivo com este nome.

jsEclipseconfiguration.properties:9983
totvs/solrCloud=true
totvs/solrRemote=true]]>

Modifique o parâmetro totvs/solrURL informando o endereço do servidor onde está sendo executado o**Fluig Indexer Primary**. Deverá ser informado **apenas** o **IP ou *hostname*** do servidor e a **porta**, sem o protocolo e contexto. A porta utilizada será a do serviço de coordenação do *cluster* que por padrão é a porta do 9983.

O parâmetro **totvs/solrCloud** irá condicionar o Fluig para ativar a opção do Solr em *Cluster*, necessária para ambientes em *cluster*.

# Criação de Core

Cada empresa (*tenant*) criada na plataforma é mapeada para um **Core** no Indexer. Quando em *cluster*, os *Cores* não são criados automaticamente, por isso é preciso criá-los manualmente **antes** de criar a empresa na plataforma.

* Inicie o Primary e o(s) Secondary(s) e crie o Core com o seguinte comando:

bashEclipseNo Linux -d fluig -shards 1 -replicationFactor 2]]>bashEclipseNo Windows -d fluig -shards 1 -replicationFactor 2]]>

Considerações:

* Informe o código que será usado para a empresa criada em <ID do Tenant>.

* Se utilizar mais de um Secondary, informe o número de instâncias totais (Primary + Secondaries) após o parâmetro -replicationFactor**.**

# Registrando o Fluig Indexer como Serviço no Windows/Linux

Para registrar Fluig Indexer como serviço, utilize os [procedimentos](http://tdn.totvs.com/pages/viewpage.action?pageId=285662306) padrões do sistema operacional em questão.
