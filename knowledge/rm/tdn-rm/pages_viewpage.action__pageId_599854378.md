---
content_hash: da6f8f9f9e7572d4bf68c0bb2399ace6100ab1a3b1dc65d9ff045854ee85270e
fetched_at: '2026-06-29T00:10:57.807210+00:00'
page_id: '599854378'
product: rm
source: tdn-rm
title: Configurando a compressão de dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599854378
version: 9
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Como alterar a configuração padrão de compressão de dados**

## **01. VISÃO GERAL**

O RM tem um mecanismo de compressão de dados que é usado com o objetivo de melhorar a performance do sistema, no trafego de dados entre cliente e servidor.

Atenção

É importante lembrar que o custo para compactação e descompactação dos dados em redes Gigabits, **pode ser** superior a transferências sem a compactação.

Caso seja notado alguma perda de performance/lentidão é recomendado **desativar** a compactação para verificar se ela é o ofensor desta perda de performance.

## **02. COMO ALTERAR A CONFIGURAÇÃO PADRÃO DE COMPRESSÃO DE DADOS**

Até a versão 12.1.31.**113**, a tag **EnableCompression** nos arquivos de configurações é responsável por indicar para o sistema irá operar com ou sem compressão de dados. 

A partir da versão 12.1.31.**114**, o parâmetro **EnableCompression** localizado nos arquivos de configurações do RM foram **descontinuados**. A presença do mesmo nesses config's não terá nenhum efeito.

Nas novas versões a compressão de dados ocorrerá automaticamente na comunicação do client com server.

Existe um novo parâmetro: **DisableCompression,** que será responsável por desabilitar a compressão. Por padrão, se esse parâmetro não existir nos arquivos de configuração ele terá o seguinte valor:

Entre as versões 12.1.31.114 e a versão 12.1.31.139

a) - **DisableCompression =** "false" para máquinas **Jobserver3Camadas**= "true".   
       Nesse caso, a compressão dos dados será realizada.

b) - **DisableCompression  = "**true" para maquinas **JobServer3camadas**= "false".  
      Nesse caso, a compressão dos dados não será realizada;

A partir da versão **12.1.31.140** a tag **Jobserver3Camadas**não influencia mais se a compressão será ativada. 

Por default, a compressão é sempre habilitada. Utilize a tag **DisableCompression** caso necessário desabilitar a compressão.

Para alterar as configurações padrões, a tag **DisableCompression** deve ser usada nos arquivos de configuração do client e server.

Ex.: <add key="DisableCompression" value="true" />

Atenção

Em versões inferiores a **12.1.34** , é essencial que as tags de compressão de dados estejam iguais nos arquivos de configuração **cliente** e **servidor**, como por exemplo no RM.Host.Service.exe.config e RM.exe.config.

A partir da versão **12.1.34** a tag passou a ser utilizada somente nos arquivos de configuração da camada **Server** (RM.Host.Service.exe.config ou RM.Host.exe.config)
