---
content_hash: 16bf9f519edb7da2a5954bf949e7d5678b871c50427b3aaa46e47ad0953da3c7
fetched_at: '2026-06-28T21:35:24.236671+00:00'
page_id: '269070393'
product: fluig
source: tdn-fluig
title: Inicializar Fluig - Linux
type: documentation
url: https://tdn.totvs.com/display/fluig/Inicializar+Fluig+-+Linux
version: 21
---

# Índice

3true.\*ndicenone

# Inicialização

---

A inicialização da plataforma depende do correto funcionamento de alguns serviços antes da inicialização do servidor de aplicação. Para iniciar o Fluig execute os comandos na ordem: fluig\_Indexer, fluig\_RealTime e fluig.

# Pré requisitos

---

* Para realizar os comandos abaixo é necessário acessar o Console do servidor onde fica instalado o Fluig e seus módulos.

Atenção!

Se desejar saber o status do serviço, no caso de ter dúvidas sobre sua inicialização, pode-se executar o seguinte comando:

bashEclipse

## Servidor de Indexação

---

Para **iniciar** o Indexer, utilize:

bash

ou

bash

Se o serviço não estiver disponível, utilize:

bash

Para **parar** o serviço do Indexer execute:

bashEclipse

## RealTime

---

Para **iniciar** o RealTime, utilize:

bash

ou

bash

Se o serviço não estiver disponível, utilize:

bash/node/bin/
./node ws\_server.js > /dev/null 2>&1 &]]>

Para **parar** o serviço do RealTime execute:

bashEclipse

## Fluig

---

 É necessário que o usuário utilizado para iniciar o serviço do Fluig seja o mesmo usuário proprietário *(owner)* da pasta de instalação.

Para **iniciar** o Fluig, utilize:

bash

ou

bash

Se o serviço não estiver disponível, utilize:

0.5falsesamples3fade1A partir da Voyager (2.0)bash/appserver/bin/standalone.sh &]]>2Versões anterioresbash/appserver/bin/domain.sh &]]>

Para **parar** o serviço do Fluig execute:

bashEclipse

Para **acompanhar o processo de inicialização**, acesse a pasta de instalação do Fluig, navegue até o diretório [diretório\_instalação]\appserver\standalone\log (a partir da **2.0**) ou [diretório\_instalação]\appserver\domain\servers\fluig1\log (**1.6 até 1.8.2**) e consulte o arquivo **server.log**. Quando a inicialização estiver concluída, a seguinte mensagem será exibida neste arquivo:

Dica

Para informações sobre acesso e utilização da plataforma, acesse o , acompanhe os primeiro passos e se familiarize com a plataforma.
