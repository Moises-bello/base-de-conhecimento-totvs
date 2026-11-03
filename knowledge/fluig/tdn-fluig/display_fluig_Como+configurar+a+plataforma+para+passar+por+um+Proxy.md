---
content_hash: bd24f1170a2c003b2f5f5e35ad0817c821441fad98fd45d64df39fa43c4a0e6d
fetched_at: '2026-06-28T21:35:23.694193+00:00'
page_id: '258277455'
product: fluig
source: tdn-fluig
title: Como configurar a plataforma para passar por um Proxy
type: documentation
url: https://tdn.totvs.com/display/fluig/Como+configurar+a+plataforma+para+passar+por+um+Proxy
version: 18
---

Fique atento!

Esta página é válida para atualizações **1.6** e **superiores** do TOTVS Fluig.

.\*ndice

# Objetivo

---

O objetivo deste guia é detalhar como configurar o serviço do Fluig para se autenticar em um servidor de *proxy*.

# Configuração

---

É possível configurar a plataforma para se autenticar em um servidor de *proxy*. Essa configuração é necessária para utilização de algumas soluções, como por exemplo *Push* e SMS, que possuem requisições HTTP *e* HTTPS para aplicações externas.

A seguir são apresentadas as configurações a serem executadas.

falseVersão1A partir da 2.0

**01**. Pare o serviço do Fluig.

**02**. Acesse [diretório\_instalação]\appserver\standalone\configuration, localize o arquivo “standalone.xml” e faça um *backup.*

**03**.Acesse [diretório\_instalação]\appserver\standalone\configuration e edite o arquivo “standalone.xml”.

**04**.Na tag **<system-properties>**, adicione as seguintes linhas e substitua os valores dos parâmetros *value* pelos dados do *proxy* de seu ambiente.

xml




]]>

**05**.Caso seja necessário também utilizar conexões HTTPS através do *proxy*, no **<system-properties>** adicione as seguintes linhas e substitua o valor dos parâmetros *value* pelos dados do *proxy* de seu ambiente:

xml
]]>

**06**.Caso seja necessário que algum endereço não passe pelo *proxy*, no **<system-properties>** adicione a seguinte linha e substitua o valor do parâmetro *value* pelos endereços IPs que não devem passar pelo *proxy*:

xml]]>

**07**. Inicie o serviço do Fluig novamente.

21.6 até 1.8.2

**01**. Pare o serviço do Fluig.

**02**. Acesse [diretório\_instalação]\appserver\domain\configuration, localize o arquivo “domain.xml” e faça um *backup.*

**03**.Acesse [diretório\_instalação]\appserver\domain\configuration e edite o arquivo “domain.xml”.

**04**.Na tag **<system-properties>**, adicione as seguintes linhas e substitua os valores dos parâmetros *value* pelos dados do *proxy* de seu ambiente.

xml




]]>

**05**.Caso seja necessário também utilizar conexões HTTPS através do *proxy*, no **<system-properties>** adicione as seguintes linhas e substitua o valor dos parâmetros *value* pelos dados do *proxy* de seu ambiente:

xml
]]>

**06**.Caso seja necessário que algum endereço não passe pelo *proxy*, no **<system-properties>** adicione a seguinte linha e substitua o valor do parâmetro *value* pelos endereços IPs que não devem passar pelo *proxy*:

xml]]>

**07**. Inicie o serviço do Fluig novamente.
