---
content_hash: 79405a8cbc27ad576a36325cd127d270bc36db11f917216e24c1176ad22b6d68
fetched_at: '2026-06-28T21:35:19.451898+00:00'
page_id: '205917413'
product: fluig
source: tdn-fluig
title: Configuração do fluig cache com Redis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=205917413
version: 57
---

Atenção!

As informações desta página são válidas para as atualizações 1.6.2 e inferiores.

**Mantenha sua plataforma atualizada!** À partir da atualização Snowflake (1.6.3), o controle e sincronização do cache do fluig é realizado através do banco de dados que, além de já ter uma conexão direta com o fluig em casos de instalações simples, também é compartilhado entre todos os nós (cluster) em casos de balanceamento de carga e alta disponibilidade.

Caso possua uma atualização 1.5.5 ou inferior do fluig acesse:

# Índice

4true.\*ndicenone

# Sobre o Redis

---

O Redis é um banco de dados NoSQL *open source* do modelo chave-valor em memória, que possui [licenciamento BSD](http://redis.io/topics/license) e pode ser utilizado como *cache* para o fluig. Ele possui funcionalidades extras como a possibilidade de ser utilizado em *cluster* com tolerância a falhas (*failover*).

Site oficial: <http://redis.io>

© Redis, *and the* Redis *logo are the trademarks of Salvatore Sanfilippo in the U.S. and other countries*.

# Pré requisito

---

* Ter o Redis instalado na máquina ou realizar o download do instalador nos links abaixo conforme o sistema operacional da máquina.

# Download do Redis

---

* O *download* do instalador do Redis para Linux pode ser realizado [neste link](http://redis.io/download).

* O *download* do instalador do Redis para Windows pode ser realizado [neste link](https://github.com/MSOpenTech/redis/releases).

# Instalação do Redis em Modo Single-Server

---

O modo *single-server* significa que apenas um processo do Redis está no ar. Mesmo neste modo ele pode atender mais de um servidor fluig, porém será considerado um ponto de falha.

## Instalação do Redis como Serviço em Linux

---

Verifique também a [documentação oficial](https://redis.io/topics/quickstart).

A forma sugerida de instalar o Redis em Linux é compilá-lo a partir dos fontes, pois não há outras dependências além do compilador GCC e da biblioteca libc.

bash

Vamos supor que você já copiou os executáveis *redis-server* e *redis-cli* em /usr/local/bin ou executou o comando *make install.*

Crie os seguintes diretórios:

bash

Copie o script de inicialização disponibilizado no diretório utils para /etc/init.d. Sugerimos renomeá-lo com o nome da porta onde você está executando esta instância do Redis.

bash

Edite o *script* de inicialização. Certifique-se de modificar o REDISPORT de acordo com a porta que você está usando. Tanto o caminho do arquivo pid quanto o nome do arquivo de configuração dependem do número da porta.

bash

Copie o arquivo de configuração modelo encontrado no diretório raiz da distribuição Redis em /etc/redis/ utilizando o número da porta como nome:

bash

Crie um diretório dentro de /var/redis que funcionará como os dados e diretório de trabalho para esta instância Redis:

bash

Edite o arquivo de configuração:

* Defina o pidfile para /var/run/redis\_6379.pid (modificar a porta se necessário).

* Altere a porta em conformidade. No nosso exemplo não é necessário, pois a porta padrão já é 6379.

* Defina o seu loglevel preferido.

* Defina o arquivo de log para /var/log/redis\_6379.log

* Definir o dir para /var/redis/6379 (passo muito importante!)

## Instalação do Redis como Serviço em Windows

---

Verifique também a [documentação oficial](https://raw.githubusercontent.com/MSOpenTech/redis/3.0/Windows%20Service%20Documentation.md).

Execute o seguinte comando:

text

# Configurando o Redis para uso com o fluig

---

### Memória

Procure no arquivo de configuração, o parâmetro *maxmemory* e certifique-se de configurar para o tamanho máximo desejado, caso contrário, podem ocorrer problemas de falta de memória.

textObservação

Se estiver sendo utilizada a versão 2.8 do Redis com o Windows, configure também o parâmetro *maxheap*.

### Persistência

Para que o Redis não salve um *snapshot* da memória periodicamente, procure as linhas iniciadas com a palavra *"save"* no arquivo de configuração...

textExemplo do config padrão para windows

...e altere-as para:

text

### Arquivo PID

Para que o Redis grave um arquivo com o PID, defina o seguinte parâmetro:

text

# Configurando o fluig para usar o Redis como Cache

---

A configuração do servidor Redis no fluig pode ser realizada das seguintes formas:

* Arquivo configuration.properties, localizado em [Instalação fluig]\repository\wcmdir\config. Deve ser alterada a propriedade cacheServerAddress para "redis:[endereço IP]:[porta]" e o serviço precisa ser reiniciado para que a mudança seja aplicada;

* Alterar o [parâmetro](http://tdn.totvs.com/pages/viewpage.action?pageId=77299889) CACHE\_SERVER\_ADDRESS [via API](https://api.fluig.com/resource_ConfigurationServiceRest.html);

xml

* Configuração via wcmadmin, caso o fluig já esteja no ar, através do Painel de controle → aba WCM → Configurações do Sistema → aba Parâmetros da Plataforma.

Observação

Essa configuração também pode ser realizada durante a execução do instalador do fluig.

# Configurando o Redis em Ambientes de Alta Disponibilidade com Tolerância a Falhas

---

O Redis usa o modelo Master-Slave com um processo monitor chamado Sentinel. Os passos indicados anteriormente continuam valendo para cada nó do *cluster* Redis.

### Master

O nó Master não necessita de nenhuma configuração adicional além das configurações dos passos anteriores.

### Slaves

Adicione a seguinte configuração (**redis.conf**) em cada nó Slave*:*

 ]]>

**Exemplo:**

text

### Sentinel

O Sentinel oferece um modelo simples e automático de alta disponibilidade (HA) para Redis usando a estratégia de eleição caso o Master venha a falhar. Inicialmente, tem-se uma replicação do Master para um número indeterminado de Slaves.

Um processo Sentinel deve ser adicionado em cada um dos servidores que terão uma ou mais instâncias do Redis para monitorar a execução dos processos e iniciar uma eleição para promover um Slave para Master caso o Master falhe.

Para isso:

* Crie um arquivo redis.sentinel.conf.

* Defina a propriedade daemonize para *"yes"*.

* Defina a propriedade *sentinel monitor* com o nome do *cluster* Redis, informe o IP e porta do Master e o quórum de sentinelas. O quórum é o número mínimo de sentinelas que avaliam que o Master falhou para iniciar uma eleição. É importante usar o valor correto, pois um número inadequado vai impedir a eleição do novo Master.

Template:

text

**Exemplo:**

textObservação

 Durante uma execução em *cluster, o*Sentinel modifica os arquivos de configuração, portanto eles devem ter permissão de escrita.

# Instalando o Sentinel como serviço no Windows

---

O executável do Sentinel é o mesmo do servidor do Redis, exceto pelo parâmetro "--sentinel".

text

# Executar o Redis Sentinel em Servidor Linux

---

A partir da versão 3 o redis-sentinel é instalado por padrão junto do Redis. Para executar o Sentinel:

Sendo que **/etc/redis/sentinel.conf** é o arquivo de configuração padrão.

# Configurando o fluig para usar o Redis Cluster com Sentinel como cache

---

Atenção!

A configuração do Redis com o fluig foi depreciada a partir da versão 1.6.2 da plataforma. Caso possua uma atualização superior à essa acesse: [Configurações da plataforma](http://tdn.totvs.com/x/7gNbDw). Ou se possuir uma atualização inferior à essas acesse: [Como posso ajustar as configurações da plataforma nas releases 1.5.13 e inferiores?](http://tdn.totvs.com/x/JppbDQ)

Abra o arquivo configuration.properties, localizado em [Instalação fluig]\repository\wcmdir\config e modifique a propriedade cacheServerAddress, ou [use a propriedade via API CACHE\_SERVER\_ADDRESS](http://tdn.totvs.com/pages/viewpage.action?pageId=224107046). O formato da configuração é "redisc:[nome\_cluster]:[IP\_Sentinel]:[Porta\_Sentinel],[IP\_Sentinel\_2]:[Porta\_Sentinel\_2], etc.".

xml

**Exemplo:**

xml

Também é possível realizar esta configuração via wcmadmin, caso o fluig já esteja no ar, através do Painel de controle → aba WCM → Configurações do Sistema → aba [Parâmetros da Plataforma](http://tdn.totvs.com/x/vLnxF).

Observação

Essa configuração também pode ser realizada durante a execução do instalador do fluig.
