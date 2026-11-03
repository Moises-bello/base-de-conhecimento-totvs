---
content_hash: 7a8dfbaec0346ebb0c2b65cd96fc0e4d025654df3b9ae19e9c7423282fd1769c
fetched_at: '2026-06-29T00:05:59.407269+00:00'
page_id: '190515801'
product: rm
source: tdn-rm
title: 4. Serviços RESTful no RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190515801
version: 21
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso

Versão

 Disponível à partir da versão 12.1.6 da linha RM.

# Serviço

Os dataservers do RM poderão ser acessados via RESTful através do serviço RMSRestDataServer, sendo esse publicado automaticamente no endereço http://<servidor>:8051/RMSRestDataServer/getAvailableServices e os dados são transmitido no formato [json](http://json.org/json-pt.html). Por padrão esse serviço é publicado com suporte à [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), o que permite que as páginas e o serviço em si sejam publicados em servidores diferente.

Os métodos disponibilizados pelo serviço são:

| Método | URL | Nome | Descrição |
| --- | --- | --- | --- |
| GET | /getavailableservices?name={name}&start={start}&limit={limit} |  | Lista de todos os serviços REST dos RMSDataServer's. |
| GET | /service/{serviceName}/schema |  | Lista o schema dos dados retornados pelo serviço. |
| GET | /service/{serviceName} |  | Lista o WADL do serviço. |
| GET | /rest/{dataServerName}/{id} |  | Retorna o registro do dataserver especificado. |
| GET | /rest/{dataServerName}?start={start}&limit={limit}&filter={filter} |  | Retorna lista os registros do dataserver especificado. |
| POST | /rest/{dataServerName} |  | Cria um registro utilizando o dataserver especificado. |
| DELETE | /rest/{dataServerName}/{id} |  | Remove um registro utilizando o dataserver especificado. |
| PUT | /rest/{dataServerName}/{id} |  | Atualiza o registro do dataserver especificado. |
| PATCH | /rest/{dataServerName}/{id} |  | Atualiza parcialmente o registro do dataserver especificado. |

Obs.: Para utilizar dataserver de metadados, é necessário informar o nome da tabela no JSON. veja um exemplo no método Post (Create) acima.

# Segurança por perfil

Todos os dataserver's do RM estão protegidos quando o acesso se dá via RMSRestDataServer. Para que a segurança seja ativada, é necessário que os DataServers sejam decorados com o atributo **RMSServerSecurityInfo**. Este atributo tem a mesma função que o atributo **ActionInfo**. Portanto, o módulo e o securityId informados devem ser iguais aos informados nas actions. Caso o atributo não seja encontrado, o acesso ao dataserver será negado.

Para cada DataServer, deve-se definir um ou mais atributos com os devidos parâmetros. Exemplo:

RMSServerSecurityInfo

# Serialização das tabelas

vários DataSets incluem tabelas que não fazem parte da definição da entidade que o mesmo representa. Isso gera um erro ao realizar as operações do CRUD através do RMSRestDataServer. Para contornar esse problema, foram adicionadas as propriedade **Master** e **Detail** no enumerador **TabProps**. Essas propriedade devem ser utilizadas para marcar quais tabelas do DataSet serão serializadas. Exemplo:

Seja DS um dataset contém as tabelas A, B e C, sendo que a tabela A tem um relacionamento com a tabela B e a tabela C não faz parte da entidade que o dataset representa (somente dados de controle). Para que o serviço RMSRestDataServer funcione corretamente, a propriedade TabProps.Master deve ser adicionada à tabela A e a propriedade TabProps.Detail deve ser adicionada à tabela B.

Dessa forma somente as tabelas A e B serão serializadas, sendo a B um detalhe de A.

**Atenção:** Caso exista mais de uma tabela no DataSet marcada como “Master”, somente a primeira tabela, e suas filhas (caso existam), serão serializadas.

c#DataSetProps

# Filtros

Ao utilizar o parâmetro **&filter={filter}**, será possível utilizar qualquer campo (desde que seja da tabela **Master**).

Não são aceitos nos filtros campos de tabelas **Detail**!
