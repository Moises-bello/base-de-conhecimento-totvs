---
content_hash: dee638eff939e4aa62727b98582a1700f6ec8c878f8c7969866df56e58a48943
fetched_at: '2026-06-28T21:35:27.571857+00:00'
page_id: '555277701'
product: fluig
source: tdn-fluig
title: Configuração Redis para uso do Load balance Realtime
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555277701
version: 9
---

true.\*ndicenone

# Sobre o Redis

---

O Redis é um banco de dados NoSQL *open source* do modelo chave-valor em memória, que possui [licenciamento BSD](http://redis.io/topics/license) e pode ser utilizado como *cache* para o TOTVS Fluig Plataforma. Ele possui funcionalidades extras como a possibilidade de ser utilizado em *cluster* com tolerância a falhas (*failover*).

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

O modo *single-server* significa que apenas um processo do Redis está no ar. Mesmo neste modo ele pode atender mais de um servidor Fluig, porém será considerado um ponto de falha.

## Instalação do Redis como Serviço em Linux

---

Verifique também a [documentação oficial](https://redis.io/topics/quickstart).

falseLinuxtruePasso 1

A forma sugerida de instalar o Redis em Linux é compilá-lo a partir dos fontes, pois não há outras dependências além do compilador GCC e da biblioteca libc.

bashPasso 2

Vamos supor que você já copiou os executáveis *redis-server* e *redis-cli* em /usr/local/bin ou executou o comando *make install.*

Crie os seguintes diretórios:

bashPasso 3

Copie o script de inicialização disponibilizado no diretório utils para /etc/init.d. Sugerimos renomeá-lo com o nome da porta onde você está executando esta instância do Redis.

bashPasso 4

Edite o *script* de inicialização. Certifique-se de modificar o REDISPORT de acordo com a porta que você está usando. Tanto o caminho do arquivo pid quanto o nome do arquivo de configuração dependem do número da porta.

bashPasso 5

Copie o arquivo de configuração modelo encontrado no diretório raiz da distribuição Redis em /etc/redis/ utilizando o número da porta como nome:

bashPasso 6

Crie um diretório dentro de /var/redis que funcionará como os dados e diretório de trabalho para esta instância Redis:

bashPasso 7

Edite o arquivo de configuração:

* Defina o pidfile para /var/run/redis\_6379.pid (modificar a porta se necessário).

* Altere a porta em conformidade. No nosso exemplo não é necessário, pois a porta padrão já é 6379.
* Defina o seu loglevel preferido.
* Defina o arquivo de log para /var/log/redis\_6379.log
* Definir o dir para /var/redis/6379 (passo muito importante!)
* Procurar pelo parâmetro **bind** onde deve estar: bind 127.0.0.1

Altere esta linha para o IP externo de acesso para as instâncias do RealTime, exemplo :

Caso o IP da máquina seja 192.168.0.19 fica:

bind 192.168.0.19 127.0.0.1

Configuração

Caso não seja feito o bind para acesso dos servidor externo (máquinas que possuem a instalação do RealTime) as instâncias do Realtime não irão funcionar.

Importante

No arquivo de configuração por padrão a proteção de acesso está ativa, como configuramos o bind direto para o IP, este parâmetro deve ser setado para no:

protected-mode no

Passo 8

Após feitas as alterações:

Para subir o Redis no Linux execute o comando abaixo:

Após subir, verifique no arquivo de log se não ocorreu nenhum erro: /var/log/redis\_6379.log

Para parar o serviço, execute o comando:

## Instalação do Redis como Serviço em Windows

---

Verifique também a [documentação oficial](https://raw.githubusercontent.com/MSOpenTech/redis/3.0/Windows%20Service%20Documentation.md).

Execute o seguinte comando:

text

# Configurando o Redis para uso com o Fluig

---

falseFluigPasso 1 - Memória

Procure no arquivo de configuração, o parâmetro *maxmemory* e certifique-se de configurar para o tamanho máximo desejado, caso contrário, podem ocorrer problemas de falta de memória.

textObservação

Se estiver sendo utilizada a versão 2.8 do Redis com o Windows, configure também o parâmetro *maxheap*.

Passo 2 - Persistência

Para que o Redis não salve um *snapshot* da memória periodicamente, procure as linhas iniciadas com a palavra *"save"* no arquivo de configuração:

textExemplo do config padrão para Windows

Altere-as para:

textPasso 3 - Arquivo PID

Para que o Redis grave um arquivo com o PID, defina o seguinte parâmetro:

textPasso 4 - Reiniciar serviços

Após efetuar as configurações para uso no servidor Fluig, é necessário parar e subir o serviço do Redis, para que sejam aplicadas as configurações.
