---
content_hash: e89aaaa6d4a04fdcd8665420bf459df323c96c06b85913d3d0e892f571c5ab62
fetched_at: '2026-06-28T21:35:28.164739+00:00'
page_id: '615412474'
product: fluig
source: tdn-fluig
title: Log de acesso aos recursos
type: documentation
url: https://tdn.totvs.com/display/fluig/Log+de+acesso+aos+recursos
version: 11
---

Fique atento!

Esta página é válida para atualizações **1.7.0-210504** e **superiores** do TOTVS Fluig.

4.\*ndice

# Objetivo

---

O objetivo deste guia é auxiliar o suporte e desenvolvedores da plataforma a ativar as mensagens de *log* que trazem informações relevantes sobre os acessos a algumas URLs importantes do produto. Essencialmente, esse *log* ajuda a identificar se a plataforma está lenta porque está recebendo muitas requisições.

# Pré-requisitos

---

Para ativar e monitorar as mensagens de *log*, é importante conhecer o procedimento de Gestão de *logs*.

# Ativando o modo DEBUG

---

Para habilitar, siga os passos abaixo:

falseVersão1A partir da 2.0

**01**. Acesse o arquivo **standalone.xml** localizado em **[diretório\_instalação]/appserver/standalone/configuration/** e procure por:

         
         
           
         
       ]]>

**02**. Em seguida, altere a linha: **<level name="WARN" />** para: **<level name="DEBUG" />**.

**03**. Reinicie os serviços do Fluig.

21.7.0 até 1.8.2

**01**. Acesse o arquivo **domain.xml** localizado em **[diretório\_instalação]/appserver/domain/configuration/** e procure por:

         
         
           
         
       ]]>

**02**. Em seguida, altere a linha: **<level name="WARN" />** para: **<level name="DEBUG" />**.

**03**. Reinicie os serviços do Fluig.

Com isso, será criado um novo arquivo na pasta de *logs*, chamado **logurl.log**.

Importante!

A ativação do modo Debug pode causar impacto na performance da plataforma, portanto habilite-a apenas quando necessário e desative-a ao concluir a análise.
