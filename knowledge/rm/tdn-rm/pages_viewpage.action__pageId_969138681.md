---
content_hash: af8ddc3cd2f03fbbfba38f9a5afd0a6369ce64ae53e0197a66127bb9f492a30c
fetched_at: '2026-06-29T00:12:14.646246+00:00'
page_id: '969138681'
product: rm
source: tdn-rm
title: Serviço de Local da Operação do IBS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969138681
version: 5
---

## **Conteúdo**

**3Conteúdo**

## **1. O que é**

O **Serviço de Local da Operação** é um recurso do **TOTVS Gestão Fiscal** que auxilia no preenchimento automático do campo *Local da Operação* no Cadastro do Movimento, utilizando informações previamente registradas no sistema.

Esse preenchimento segue uma regra definida, com base em dados de entrada específicos, conforme o fluxo descrito abaixo. O objetivo é determinar corretamente o **Código do Município** e a **UF (Unidade Federativa)** associados à operação.

## **2. Regras**

O sistema segue algumas regras para determinar qual será o **Local da Operação** em cada situação. Veja abaixo como funciona:

1. **O sistema verifica se foi informado um Local do imóvel.**

* + **Se sim**: o Local da Operação será exatamente o **Local do imóvel**.

    - *Exemplo: a prestação de serviço (instalação do carpet, pintura, etc) estará ocorrendo em um determinado imóvel da incorporadora.*
  + **Se não**:

1. 1. 1. **Quando a operação é presencial**

         * Primeiro, o sistema verifica se foi informado um **Local da Coleta**.

           + **Se sim**: o Local da Operação será exatamente o **Local da Coleta**.

             - *Exemplo: o cliente retira a mercadoria diretamente em um ponto de coleta informado.*
           + **Se não**: o Local da Operação será considerado como a **Filial Emitente** ou o **Cliente/Fornecedor Emitente**.

             - *Exemplo: não há ponto de coleta definido, então o sistema assume a própria empresa emissora como local da operação.*
      2. **Quando a operação não é presencial**

         * O sistema então verifica se existe um **Local da Entrega** informado.

           + **Se sim**: o Local da Operação será o **Local da Entrega**.

             - *Exemplo: a nota indica entrega em uma filial específica do cliente; esse será o local da operação.*
           + **Se não**: o sistema verifica se existe um **Local do destinatário do serviço** informado:

             - **Se sim**: o Local da Operação será a **Local do destinatário do serviço**.

               * *Exemplo: um curso adquirido será ministrado em uma universidade ou local específico*
             - **Se não**: o sistema analisa o **Tipo da Operação**:

               * **Se for uma entrada**: o Local da Operação será a **Filial Destino**.

                 + *Exemplo: uma compra sem local de entrega definido; a filial que recebe o produto será considerada o local da operação.*
               * **Se for uma saída**: o Local da Operação será o **Cliente/Fornecedor Destinatário** ou a **Filial Destino**.

                 + *Exemplo: numa venda em que não há entrega definida, o sistema assume como local da operação o destinatário da nota.*
