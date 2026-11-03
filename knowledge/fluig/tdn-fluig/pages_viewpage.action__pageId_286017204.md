---
content_hash: 1a11ecbe53c85657159a2c49ef3e4cdb71afaf453173f73108806db993e0db0a
fetched_at: '2026-06-28T21:35:25.574759+00:00'
page_id: '286017204'
product: fluig
source: tdn-fluig
title: ARQ - O que devo verificar quando o fluig_Indexer não sobe?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286017204
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto: TOTVS Fluig Plataforma**

**Versão:** 1.6 e superior

# Ocorrência

O que devo verificar quando o fluig\_Indexer não sobe?

# Solução

Verifique se as situações abaixo apresentadas estão corretamente configuradas:

Atenção!

Para executar os procedimentos abaixo, é necessário estar com o serviço do Servidor de Indexação **parado**. Certifique-se de que ele não esteja **em pausa** após apresentação da mensagem em tela.

0.5falseSamplefadetrue1Situação 1

O endereço do JDK presente no diretório de instalação da plataforma não está configurado corretamente nos arquivos de configuração do Servidor de Indexação.

Importante!

Nas instalações modularizadas ( ou ) em servidor dedicado, se o servidor não possuir o Java instalado, será instalado o JDK juntamente com o Servidor de Indexação. Portanto, o procedimento abaixo ocorrerá de forma automática. Caso o Java já estiver instalado, basta informar o diretório no arquivo de configuração (install.conf) para a correta configuração no momento da instalação.

**Windows**

1. Localize o arquivo '**solr.in.cmd**' em **[diretório\_instalação]/solr/bin** e verifique se está declarado conforme informado abaixo. Em [diretório\_instalação] deve ser apresentado o diretório de instalação da plataforma.

xmlEclipsesolr.in.cmd

2. Salve as alterações e inicie o serviço.

**Linux**

1. Localize o arquivo '**fluig\_Indexer.in.sh**' em **/etc/default/**e verifique se está declarado conforme abaixo. Em [diretório\_instalação] deve ser apresentado o diretório de instalação da plataforma.

xmlEclipsefluig\_Indexer.in.sh

2. Salve as alterações e inicie o serviço.

2Situação 2

A porta utilizada pelo Servidor de Indexação pode estar sendo utilizada portanto, certifique-se de que ela esteja liberada ou .

Confira as portas utilizadas pela plataforma em .
