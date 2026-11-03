---
content_hash: 802530dab9259a7c377c0e875a4000cf3994672e4ca7320a6a50d4d0b161771e
fetched_at: '2026-06-28T21:35:25.457204+00:00'
page_id: '285662306'
product: fluig
source: tdn-fluig
title: Recriar Serviços do Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285662306
version: 14
---

Atenção!

Esta página foi revisada para considerar as novas configurações do Fluig para a atualização 1.6.x.

Caso possua uma atualização anterior, acesse:

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é informar os passos para criar, desinstalar, recriar e renomear os serviços do Fluig, sendo eles: memCached, fluig\_Indexer, fluig\_RealTime e fluig.

Local

# Localização dos arquivos

---

Para cada tipo de serviço existe um arquivo correspondente que deve ser executado.

Atenção!

Em uma instalação padrão do Fluig 1.6.1, os serviços de RealTime e Servidor de Indexação são instalados juntamente com o servidor de aplicação no mesmo diretório. Caso a instalação seja em módulos, será necessário informar seus respectivos diretórios.

| Serviço | Executável | Localização |
| --- | --- | --- |
| fluig | service.bat | [Instalação fluig]/appserver/bin/service |
| fluig\_RealTime | nodeSetup.bat | Raíz da pasta de instalação do Fluig |
| fluig\_Indexer | solrSetup.bat | Raíz da pasta de instalação do Fluig |

# Criar serviços

---

Navegue nos passos abaixo para conhecer os procedimentos de criação dos serviços do Fluig:

0.5falsecriarfadetrue1Fluig

criar\_fluig

**1)** Abra o prompt de comando e acesse a  ao serviço que deseja criar:

bashEclipse

**2)** Para criar o serviço, digite:

bashEclipse2RealTime

criar\_Real

**1)** Acesse o prompt de comando e acesse a  ao serviço que deseja criar:

bashEclipse

**2)** Para criar o serviço, digite:

bashEclipse3Indexer

criar\_Indexer

**1)** Acesse o prompt de comando e acesse a ao serviço que deseja criar:

bashEclipse

**2)** Para criar o serviço, digite:

bashEclipseAtenção

Para recriar os serviços em **servidor Linux**, o caminho das pastas são os mesmos, basta apenas substituir o **.bat** por **.sh** nos comandos.

Desinstalar

---

Siga os passos abaixo para desinstalar os serviços do Fluig:

0.5falsedesinstalarfadetrue1Fluig

des\_fluig

**1)** Abra o prompt de comando e acesse a  ao serviço que deseja desinstalar:

bashEclipse

**2)** Para desinstalar o serviço, digite:

bashEclipse2RealTime

des\_Real

**1)** Acesse o prompt de comando e acesse a  ao serviço que deseja desinstalar:

bashEclipse

**2)** Para desinstalar o serviço, digite:

bashEclipse3Indexer

des\_Indexer

**1)** Acesse o prompt de comando e acesse a  ao serviço que deseja desinstalar:

bashEclipse

**2)** Para desinstalar o serviço, digite:

bashEclipse

# Recriar

---

Navegue nos passos abaixo para conhecer os procedimentos de recriar os serviços do Fluig:

0.5falserecriarfadetrue1Fluig

1. Abra o Prompt de Comandos ou Console e  correspondente do serviço Fluig;
2. Execute o comando para ;
3. Execute o comando para ;
2RealTime

1. Abra o Prompt de Comandos ou Console e  correspondente do serviço RealTime;
2. Execute o comando para  (nodejs);
3. Execute o comando para ;
3Indexer

1. Abra o Prompt de Comandos ou Console e  correspondente do serviço do Servidor de Indexação;
2. Execute o comando para  (solr);
3. Execute o comando para ;
oculto

O conteúdo desse passo foi repassado ao artigo: <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033246754> (Como recriar os serviços)

Lembrar de atualizar esse artigo caso tenha alguma alteração!

# Renomear

---

Siga os passos abaixo para renomear os serviços do Fluig:

0.5falserecriarfadetrue1Fluig

1. Abra o Prompt de Comandos ou Console e  correspondente do serviço Fluig;

2. Execute o comando para ;

3. Edite o arquivo **service.bat** localizado em [Instalação fluig]/appserver/bin/service;

4. Procure pelo trecho de configuração abaixo e altere o nome dos serviços nas variáveis SHORTNAME, DISPLAYNAME e DESCRIPTION:

xml

5. Em seguida, salve o arquivo.

6. Execute o comando para ;

2RealTime

1. Abra o Prompt de Comandos ou Console e  correspondente do serviço RealTime;

2. Execute o comando para  (nodejs);

3. Acesse o diretório da nova instalação **[Instalação fluig]** e localize o arquivo “**nodeSetup.bat**” para editá-lo.

4. Procure pelo trecho de configuração abaixo e altere o nome dos serviços nas variáveis SVCNAME, SVCDISP e SVCDESC:

xml

5. Em seguida, salve o arquivo.

6. Execute o comando para ;

3Indexer

1. Abra o Prompt de Comandos ou Console e  correspondente do serviço do Servidor de Indexação;

2. Execute o comando para  (solr);

3. Acesse o diretório da nova instalação **[Instalação fluig]** e localize o arquivo “**solrSetup.bat**” para editá-lo.

4. Procure pelo trecho de configuração abaixo e altere o nome dos serviços nas variáveis SVCNAME, SVCDISP e SVCDESC:

xml

5. Em seguida, salve o arquivo.

6. Execute o comando para ;

# Serviço de Cache (memCached)

---

A partir da atualização 1.6.2, não é necessário configurar o serviço de memCached.

Atenção!

Caso possua a atualização 1.6.0 ou 1.6.1, acesse:

Caso possua uma atualização anterior a 1.6.0, acesse: 

$("b:contains('oculto')").parent().parent().hide();
]]>
