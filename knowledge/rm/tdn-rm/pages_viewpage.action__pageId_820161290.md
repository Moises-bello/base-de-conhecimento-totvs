---
content_hash: 7eb8d59467382e487940a6900047c7802a6c29432e37b5a9167ff719105ff1c8
fetched_at: '2026-06-29T00:11:45.566539+00:00'
page_id: '820161290'
product: rm
source: tdn-rm
title: Integração RM x SmartLink Data Sharing 2.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820161290
version: 66
---

## **Introdução**

Aqui você encontrará as informações necessárias para utilizar a **Integração RM com SmartLink DataSharing v2.** Para essa integração será utilizado o protocolo de comunicação gRPC. 

Nesse modelo de integração, o dado é recuperado do RM e enviado para o SmartLink Server (serviço hospedado na plataforma TOTVS Apps).

Na versão anterior de integração com SmartLink DataSharing v1, o dado é recuperado do RM e enviado diretamente para a Carol (mais detalhes disponíveis em <https://tdn.totvs.com/x/l-55IQ>,).

## **01. Serviço RM de envio dos dados**

Na integração anterior (SmartLink Data Sharing v1) os dados são enviados em ciclos de execução de Job's (mecanismo de  Job do RM - <https://tdn.totvs.com/x/_Z4YIQ>).

Já na integração SmartLink Data Sharing v2, os dados serão enviados através da execução automática de um serviço de Host chamado NotifyServer.

Nesse mecanismo, somente uma máquina do ambiente do cliente (seja um servidor de aplicação ou um servidor de Job) terá a responsabilidade de enviar os dados. Em nenhum momento duas ou mais máquinas poderão enviar os dados simultaneamente.

Caso ocorra algum problema com a máquina responsável pelo envio, ficando portanto indisponível, outra máquina assumirá o papel de envio.

O envio dos dados ocorrerá de 15 em 15 segundos, ou seja, caso um algum registro (de alguma tabela integrada) seja alterado, a alteração será enviada para o SmartLink Server após, no máximo, 15 segundos.

Ciclo de vida

O modelo de integração **SmartLink DataSharing v1** em breve será **descontinuado** pela equipe de Framework BH.   
Portanto, os times dos segmentos que possuem integração dessa natureza devem migrar para o novo modelo.

## **02. Envio dos pacotes (batches)**

Nesta versão, a sincronização de dados entre o RM → SmartLink → Carol seguirá o conceito de envio por pacotes (batches). Cada pacote possui um identificador que será utilizado para rastreio dos dados conforme são enviados pelo SmartLink, para a Carol e por fim até ao app.

Atenção

Para evitar conflito nas staging tables entre a integração DataSharing 1.0 e 2.0, a integração 2.0 adiciona o prefixo "DS2\_" no nome das tabelas.

Exemplo na Carol: Tabela PFUNC

Data Share 1.0 = pfunc  
Data Share 2.0 = ds2\_pfunc

O batch será composto por múltiplas mensagens que irão conter os registros das tabelas que deverão ser enviadas para o serviço de ingestão utilizando o protocolo de comunicação **gRPC.**

Cada mensagem é formada por até 2000 registros.

No RM, o rastreio dos dados enviados podem ser verificados através de uma sentença SQL na tabela *GDataShareRecords*.

A tabela *GDataShareRecords* é responsável em manter um rastro dos registros que já foram enviados (por tabelas).

Portanto, operações de update, delete e insert não poderão ser efetuadas nessa tabela de forma manual.

O processo de limpeza dessa tabela é feito automaticamente pelo serviço de envio de dados.

## **03. Serviço de entidades**

As entidades consistem em uma parte fundamental do processo. Elas determinam todas as entidades que o RM deve subir de acordo com os app's contratados.

A lista das tabelas que participarão do processo de envio é recuperada através da chamada de um serviço com endpoint "[/api/carol-definitions/v1/entities/RM](https://provisioning.dev.totvs.app/api/carol-definitions/v1/entities/RM)".

O retorno da chamada desse serviço terá o seguinte padrão de objeto:

 1000",
"forceReload": false,
"isNative": true,
"isCustom": false,
"metadata": null
}
]
}
]]>

### Características:

1. Cada item da lista "queries", representa uma tabela do RM que será integrada. No exemplo acima, teremos a integração das tabelas TMOV e FLAN.
2. **Filtro de dados (atributo filter)**: clausula SQL ANSI **obrigatória** para entidades que possuem dados históricos ou de movimentação. Será utilizado sempre que o ciclo de envio estiver enviando a tabela pela primeira vez (carga inicial) ou quando uma solicitação de recarga dessa tabela (*forceReload* = *true*) seja sinalizada para o RM.

No filtro, sempre deve ser informado "Tabela.Campo" conforme exemplo abaixo:

**TMOV.DATAMOVIMENTO > '2012-01-01'.**

3. **Recarga de uma tabela específica (atributo forceReload)**: é um campo do tipo booleano que indicará para o RM efetuar a recarga desta tabela. Recurso importante para tratar cenários com problema sem a necessidade de acessar o ambiente do cliente.

Solicitações de inclusão/exclusão de tabelas devem ser tratadas diretamente com a equipe de plataformas do TOTVS Apps.
