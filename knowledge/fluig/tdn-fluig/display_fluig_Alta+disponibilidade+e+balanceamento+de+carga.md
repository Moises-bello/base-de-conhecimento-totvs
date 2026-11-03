---
content_hash: 5b2a5fbce38efec6f5e0550b9196a0a5432566e11022edb769d2b25262224129
fetched_at: '2026-06-28T21:35:23.537250+00:00'
page_id: '257622931'
product: fluig
source: tdn-fluig
title: Alta disponibilidade e balanceamento de carga
type: documentation
url: https://tdn.totvs.com/display/fluig/Alta+disponibilidade+e+balanceamento+de+carga
version: 44
---

Fique atento!

Esta página foi revisada para considerar as configurações de server para a atualização **1.6.3** ou **superior**.

Caso possua uma atualização entre **1.6.0** à **1.6.2**, acesse:

4.\*ndice

# Objetivo

---

O objetivo deste guia é apresentar os procedimentos necessários para a criação de um ambiente TOTVS Fluig com balanceamento de carga, afim de ter uma alta disponibilidade.

# Considerações iniciais

---

Atenção!

Em ambientes com servidores **Windows**, o uso de pastas compartilhadas ou unidades mapeadas está apresentando inconsistências na rotina de *deploy* de alguns componentes. Já estamos avaliando essa situação para que seja corrigida o mais breve possível. No momento, como forma paliativa, é necessário realizar a atualização individualmente de cada servidor e reiniciá-los.

Lembrando que a nossa **recomendação** é utilizar servidores **Linux** em ambientes configurados com ***Load balance*** para um melhor desempenho.

* O  (Solr) é compartilhado por todas as instâncias, podendo ser único ou ;

* O repositório de arquivos da plataforma ([Volume](http://tdn.totvs.com/pages/viewpage.action?pageId=233766796)) deve estar em uma pasta compartilhada por todas as instâncias;

* A pasta de aplicativos "[diretório\_instalação]/appserver/apps" deve estar em um diretório compartilhado por todas as instâncias;

* O banco de dados dever ser único para todas as instâncias;

* Todas as instâncias devem estar atualizadas com a mesma versão do TOTVS Fluig.

* Ao utilizar balanceamento de carga em ambientes com HTTPS, a [configuração de HTTPS](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Configura%C3%A7%C3%A3odeHTTPSmanual) deve ser replicada manualmente para todos os servidores do Fluig.

Importante!

* A partir da atualização Snowflake (1.6.3), o controle e sincronização do cache da plataforma é realizado através do banco de dados e é compartilhado entre todos os nós de um cluster.

* É necessário reiniciar todos os servidores depois de finalizar as configurações.

# Preparando ambiente

---

Antes de começar a instalação, é preciso estar com o ambiente preparado.

0.5falsesamplesfadetrue1Passo 1

* Instale o banco de dados e crie uma instância.

2Passo 2

* Escolha uma pasta em um servidor (chamaremos de GLOBAL\_DATA\_DIR) e torne-a acessível para todas as máquinas. Dentro dessa pasta compartilhada, crie uma nova pasta:  "apps".

Atenção!

Nas versões anteriores a 1.6.0, deverá também ser criada a pasta "wcmdir" dentro da GLOBAL\_DATA\_DIR.

3Passo 3

* Escolha uma pasta em um servidor (chamaremos aqui de VOLUME\_DIR) e torne-a acessível para todas as máquinas. Será usada para salvar os volumes das empresas.

# Configuração

---



* [Plataforma em load balance com NGINX em Linux](https://tdn.totvs.com/x/SQI6N)

Nota:

Se tiver dificuldades na , clique no *link* para acessar a documentação.
