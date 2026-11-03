---
content_hash: 6df353276a9e3954f282a361bb673e672ef0c486272766d495bdb8c71170c3c2
fetched_at: '2026-06-28T21:35:26.099130+00:00'
page_id: '337349115'
product: fluig
source: tdn-fluig
title: ARQ - Como configurar load balance, alta disponibilidade e tolerância a falha
  na release 1.6.0 a 1.6.2?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337349115
version: 6
---

Atenção

Esta página foi revisada para considerar as configurações entre a atualização 1.6.0 e 1.6.2.

Caso possua uma atualização 1.6.3 ou superior, acesse:

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** da 1.6.0 à 1.6.2

# Ocorrência

Como configurar balanceamento de carga,alta disponibilidade e tolerância a falha (cluster) da atualização 1.6.0 à 1.6.2?

# Solução

Veja abaixo os procedimentos necessários para a criação de um ambiente em *cluster*, onde é possível ter balanceamento de carga, alta disponibilidade e tolerância a falha.

## Considerações iniciais

* O  (Solr) é compartilhado por todas as instâncias, podendo ser único ou ;

* Um servidor de cache externo deve ser utilizado. Recomenda-se o [Redis](http://tdn.totvs.com/pages/viewpage.action?pageId=205917413).

* O repositório de arquivos da plataforma ([Volume](http://tdn.totvs.com/pages/viewpage.action?pageId=233766796)) deve estar em uma pasta compartilhada por todas as instâncias;

* A pasta de aplicativos "[Instalação fluig]/appserver/apps" deve estar em um diretório compartilhado por todas as instâncias;

* O banco de dados dever ser único para todas as instâncias;

* Todas as instâncias devem estar atualizadas com a mesma versão da plataforma.

## Preparando ambiente

Antes de começar a instalação, é preciso estar com o ambiente preparado.

0.5falseSamplesslidetrue1Passo 1

* Instale o banco de dados e crie uma instância.
2Passo 2

* Instale e configure o servidor de cache externo ([Redis](http://tdn.totvs.com/pages/viewpage.action?pageId=205917413))
3Passo 3

* Escolha uma pasta em um servidor (chamaremos de GLOBAL\_DATA\_DIR) e torne-a acessível para todas as máquinas. Dentro dessa pasta compartilhada, crie uma nova pasta:  "apps".

Atenção!

Nas versões anteriores a 1.6.0, deverá também ser criada a pasta "wcmdir" dentro da GLOBAL\_DATA\_DIR.

4Passo 4

* Escolha uma pasta em um servidor (chamaremos aqui de VOLUME\_DIR) e torne-a acessível para todas as máquinas. Será usada para salvar os volumes das empresas.

## Tipos de configuração

Há dois modelos de configuração: apenas balanceamento de carga e alta disponibilidade com tolerância a falha.

* Configuração de balanceamento de carga: [Plataforma em Load Balance com Apache mod\_cluster em Linux](http://tdn.totvs.com/display/fluig/Fluig+em+Load+Balance+com+Apache+mod_proxy+em+Linux) ou [Plataforma em Load Balance com Microsoft NLB](http://tdn.totvs.com/display/fluig/Fluig+em+Load+Balance+com+Microsoft+NLB).

* Configuração de alta disponibilidade com tolerância a falha: [Plataforma em alta disponibilidade com tolerância a falha](http://tdn.totvs.com/pages/viewpage.action?pageId=269072543).

Caso tiver dificuldades na [Configuração do Realtime para execução em Load Balance](http://tdn.totvs.com/pages/viewpage.action?pageId=257623378) clique no link para acesso a documentação.
