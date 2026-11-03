---
content_hash: a677afb8d988e8aafb244201f9c7f9963528724a57531a7a7a3c88eeebafa4a7
fetched_at: '2026-06-29T00:11:11.063166+00:00'
page_id: '645254815'
product: rm
source: tdn-rm
title: Customizando novos arquivos a serem baixados
type: documentation
url: https://tdn.totvs.com/display/LRM/Customizando+novos+arquivos+a+serem+baixados
version: 6
---

Por padrão, o SmartClient irá baixar determinados arquivos, essenciais para o funcionamento do RM, porém existe a possibilidade, caso necessário, de adicionar novos arquivos àqueles que serão baixados, tal qual demontrado abaixo:

Primeiramente, a pasta-raiz do servidor da qual serão baixadas as informações deve possuir um arquivo de nomenclatura ***ArquivosEspeciais.xml***. Este arquivo possuirá a lista de todos os arquivos que devem ser baixados junto da instalação do Smart Client. Você pode baixar este arquivo no  ou criá-lo na pasta-raiz da aplicação, contendo como conteúdo o snippet abaixo (*Lembre-se, em ambos os casos, de editar e remover os arquivos e pastas inexistentes/de exemplo*):

xmlArquivosEspeciais.xml


Arquivo.xml

Arquivo.xml

Arquivo.xml
pasta
]]>

## Explicando a estrutura do ArquivosEspeciais.xml

O ***ArquivosEspeciais.xml*** é dividido por arquivos de ***Server*** (que não serão baixados pelo SmartClient), ***Client*** (que são os arquivos que serão ativamente baixados pelo Smart Client) e ***Both***, que são arquivos contemplados tanto pelo Client quanto pelo Server. No caso de permitir um arquivo ser baixado pelo Smart Client, este deve ser preeenchido dentro das tags **Both** ou **Client.**

É possível permitir o download tanto de arquivos avulsos quanto de pastas inteiras. Assim sendo, para permitir que um novo arquivo seja baixado pelo SmartClient, basta preencher uma nova tag **<item tipo="arquivo">*[NOME\_DO\_ARQUIVO]*</item>** e quanto a pasta, basta preencher a tag da seguinte forma: **<item tipo="pasta">*[NOME\_DA\_PASTA]*</item>**

## Na Prática

Agora, no passo-a-passo, demonstraremos como configurar o Smart Client para baixar arquivos além dos já baixados normalmente pelo instalador.

Primeiramente, baixamos o arquivo conforme demonstrado acima e o configuramos para baixar um arquivo XML de nome ***demonstracao.xml*** e uma pasta chamada **documentos** (Dentro da pasta existe o arquivo *apresentacao.pptx*):

Reinicie o serviço (Host.Service) para que as alterações tenham efeito.

Agora, solicitamos uma instalação pelo Smart Client:

E após a instalação, se conferirmos a pasta aonde os arquivos foram instalados, podemos notar tanto a pasta documentos quanto o arquivo demonstracao.xml foram baixados junto aos arquivos pré-definidos:

A partir do momento que a instalação foi feita, todas as instalações do Smart Client irão baixar os novos arquivos especiais quando o RM for iniciado em cada instalação

## Avisos importantes:

Arquivos de tamanho menor que 1KB **NÃO** serão baixados pelo instalador do Smart Client.
