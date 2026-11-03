---
content_hash: efa1cc7f5673a7693f822143530a6f55fd8da85c97da1acd755e91bb6bc2c6c0
fetched_at: '2026-06-29T00:08:55.462122+00:00'
page_id: '349183790'
product: rm
source: tdn-rm
title: New Model
type: documentation
url: https://tdn.totvs.com/display/LRM/New+Model
version: 56
---

]]>]]>

# Sumário

Sumário

# Introdução

Este documento é um guia de instalação e configuração do serviço de cache centralizado para os produtos da linha TOTVS RM. Dentre os benefício que o cache centralizado traz estão: racionalização de recursos de memória e eliminação de chaves duplicadas em instancias distintas de servidores de aplicação.

## Organização do documento

Para instalar o serviço de cache centralizado será necessário realizar as operações dos seguintes tópicos deste documento:

* Intalação do Redis, tópico 2. (requerido)
* Caso opte por utilizar a criptografia SSL, tópico 3. (opcional)
* Configuração dos serviços de host do Totvs RM, tópico 4. (requerido)

## Entendendo os benefícios

Os benefícios de utilização do cache centralizado está relacionado com o tamanho do ambiente. Quanto maior o ambiente, ou seja, quanto maior o número de instancias de servidores de aplicação (Host) e servidores de job (Job Server) maiores serão os ganhos na utilização deste serviço.

# Instalando o Redis

Dentre as opções de instalação do Redis estão: Instalação nativa nos sistemas operacionais Linux, Windows e instalação  via Docker em ambos os sistemas operacionais.

A versão corrente para  Windows é a 3.2.1 e atualmente não recebe atualizações, apesar de suportar o uso do serviço de cache do Totvs RM.

O Docker Container oficial disponível no Docker Hub é para Linux. Desta forma se você pretende utiliza-lo em ambiente Windows terá que realizar as configurações mencionadas no tópico 2.2 deste documento.

## Instalando o Redis no Linux

Para instalar o Redis no Linux utilizando o gerenciador de pacotes apt-get, abra uma sessão ssh e entre com os camandos abaixo:

Sincronizando os índices dos pacotes

sudo apt-get update

sudo apt-get upgrade

Instalando o Redis

sudo apt-get install redis-server

Configurando o Redis – Abra o arquivo de configuração

sudo vi /etc/redis/redis.conf

Procure pela chave **bind**, descomente-a e altere-a para o IP o qual será visto pelos servidores RM. **NÃO** utilize um IP que seja expoto à internet.

bind 10.1.21.102

A porta default do redis é 6379, caso precise alterar esta porta altere a chave **port**.

port 6379

Procure pela chave **protected-mode**, descomente-a e altere-a para **no**.

protected-mode no

Procure pela chave requirepass, descomente-a e altere-a para o valor do password que desejar. Este password deverá ser informado na configuração do RM.Host.Service.

requirepass MYPASSWORD

]]>
