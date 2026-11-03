---
content_hash: 101805424972f9b0bc5a5f8016fd89e41c6715144fed6159eb5cbbe6b128b10e
fetched_at: '2026-06-29T00:11:53.912343+00:00'
page_id: '852324782'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Log de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852324782
version: 7
---

Foi criada a API para uso dos produtos de Folha de Pagamento das linhas RM, Datasul e Protheus, que será utilizada na nova tela "Log de Integração", desenvolvida em PO UI. Esta tela oferece recursos avançados para a identificação e detalhamento dos erros nas integrações, como eventos do eSocial entre a folha de pagamento e os sistemas TAF e TSS, entre outros.

Essa implementação representa um avanço significativo para nossos clientes e equipes de atendimento. Ao facilitar a identificação precisa de problemas, reduzirá os custos associados à análise de incidentes, aumentando a eficiência e a assertividade ao direcionar as questões para os times responsáveis. Além disso, proporcionará uma redução significativa no tempo e no esforço dedicados à análise de problemas por parte das equipes de desenvolvimento.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

notech

## Informações Técnicas da API

**Facilitadores.**

Para análise rápida, importe o postman:

150

Site postman: [Postman API Platform | Sign Up for Free](https://www.postman.com/)

Fora feito um mock da api usando a tool mockoon, segue o enviroment:

É possível abrir esse enviroment e utilizar todo o mock feito.

150

Site mockoon: [Create mock APIs in seconds with Mockoon](https://mockoon.com/)

**Erros.**

Seguir padrão especificado em <https://tdn.totvs.com/display/public/INT/Guia+de+implementacao+das+APIs+TOTVS#GuiadeimplementacaodasAPIsTOTVS-Formatodasmensagensderesposta>

LoggerLoggerTiposIntegraçãoTipos de integração e tipos logs

**Objetivo:** Busca tipos de integração e tipos de logs.

Esses endpoint's serão usados para o preenchimento dos componentes 'Integração' e 'Tipo de log'

Recomenda-se o backend realizar cache desses endpoints, devida suas características invariantes.

**Tipo de requisição:** GET

**Endpoints:** api/rh/logs/v1/integrations/types e  api/rh/logs/v1/integrations/logTypes

**Estrutura de Retorno:**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| hasNext | boolean |
| items | array de objetos detalhado abaixo |

Para o array de items, a estrutura do objeto de retorno no json deve conter obrigatoriamente os campos abaixo.

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| id | int |
| description | string |

**Exemplos de Requisição:**

GET /api/rh/logs/v1/integrations/types

Exemplo de retorno

{  
  "hasNext": false,  
  "items": [  
    {  
      "id": 1,  
      "description": "TAF"  
    },  
    {  
      "id": 2,  
      "description": "TSS"  
    },  
    {  
      "id": 3,  
      "description": "Feedz"  
    }  
  ]  
}

GET /api/rh/logs/v1/integrations/logTypes

Exemplo de retorno

{  
  "hasNext": false,  
  "items": [  
    {  
      "id": 1,  
      "description": "Trace"  
    },  
    {  
      "id": 2,  
      "description": "Error"  
    }  
  ]  
}

LoggerProcessesListListagem de processos

**Objetivo**: Obter os processos de uma determinada integração.

**Tipo de requisição:** GET

**Endpoint:** /api/rh/logs/v1/integrations/processes

**Query Params:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| idIntegration | Equivale ai [items.id](http://items.id) retornado em /api/rh/logs/v1/integrations/types | inteiro | sim | 1 |

**Estrutura de Retorno:**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| hasNext | boolean |
| items | array de objetos detalhado abaixo |

Para o array de items:

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| id | int |
| description | string |

**Exemplo de Requisição:**

GET /api/rh/logs/v1/integrations/processes?idIntegration=1

Exemplo de retorno

{  
  "hasNext": false,  
  "items": [  
    {  
      "id": 1,  
      "description": "Status"  
    },  
    {  
      "id": 2,  
      "description": "Evento xpto"  
    }  
  ]  
}

LoggerActiveAtivar log

**Objetivo**: Ativar ou desativar captura de logs.

**Tipo de requisição:** POST

**Endpoint:** /api/rh/logs/v1/integrations

**Estrutura do corpo da requisição (Body)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| active | Flag para ativar ou desativar o log. | boolean | Sim | true |
| companyId | Company id injetado na session storage do frontEnd | int | Sim | 1 |
| idIntegration | Identificação a integração | int | Sim | 1 |
| idLogType | Identificação do tipo de log que será ativado | int | Sim | 1 |
| idProcess | Identificação do processo da integração | int | Sim | 1 |

POST /api/rh/logs/v1/integrations

Exemplo body request

{  
    "active": true,  
    "companyId": 1,  
    "idIntegration": 1,  
    "idLogType": 1,  
    "idProcess": 5  
}

**Estrutura de Retorno:**

Para o retorno, utilizamos a forma abaixo.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Tipo** |
| timer | 'Cronômetro' representado em milissegundos, cujo valor irá determinar o tempo máximo que o front-end, aguardará a resposta da primeira página. | int |
| interval | Intervalo entre requisições em milissegundos, que serão feitas pelo front-end para verificar o retorno da primeira página. | int |

Exemplo de retorno

{  
    "timer": 60000,  
    "interval": 2000  
}

LoggerSummaryListListagem resumida dos logs

**Objetivo:**Obtenção paginada dos logs gerados pela aplicação após sua ativação.

O front end, após a chamada do endpoint que faz a ativação do log, se o mesmo fora para ativar, entrará em modo de 'espera', aguardando o retorno da primeira página contendo os primeiros logs.

Mesmo que o backend retorne uma lista vazia e com a flag hasNext igual a false, a tela continuará tentando obter resultados até seu ciclo de espera terminar ou o backend retornar uma lista de itens em 'items'

**Motivo:** Entende-se que nem sempre logo após a ativação será captado algum log, portanto se faz necessário esperar até que haja algum estímulo para captação do log.

O ciclo de espera do front-end é terminado pelos campos 'timer' e 'interval' retornados na requisição da ativação, portanto cada linha poderá configurar da melhor forma que entender, tanto o tempo de espera, quando a frequência de validação.

**Tipo de requisição:** GET

**Endpoint:** /api/rh/logs/v1/integrations

**Query Params:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Observação** | **Obrigatório** | **Exemplo** |
| companyId | int |  | Sim | 1 |
| idIntegration | int |  | Sim | 1 |
| idLogType | int |  | Sim | 1 |
| idProcess | int |  | Sim | 0 |
| startDateTime | dateTime | Formato yyyy-mm-ddThh:mm:ss, usado para filtrar a partir de qual data hora se deseja obter a listagem, o filtro se aplica no campo 'dateTime' | Não | 2024-05-10T09:53:37 |
| page | int |  | Sim | 1 |
| pageSize | int |  | Sim | 30 |

Exemplo: **/api/rh/logs/v1/integrations?companyId=1&idIntegration=0&idLogType=0&idProcess=1&startDateTime=2024-05-10T09:53:37&page=1&pageSize=30**

**Estrutura de Retorno:**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| hasNext | boolean |
| items | array de objetos detalhado abaixo |

Para o array de items, a estrutura do objeto de retorno no json deve conter obrigatoriamente os campos abaixo.

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| id | string |
| dateTime | Data hora formato yyyy-mm-ddThh:mm:ss |
| isError | boolean |
| statusCode | string |
| verb | string |
| process | string |
| url | string |

Exemplo

{  
    "hasNext": true,  
    "items": [  
        {  
            "id": "11620630817",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": false,  
            "statusCode": "200",  
            "verb": "GET",  
            "process": "",  
            "url": "<http://localhost:8051/api/something/to/do?id=80982&scope=global>"  
        },  
        {  
            "id": "11081228397",  
            "dateTime": "2024-05-11T10:15:45",  
            "isError": true,  
            "statusCode": "404",  
            "verb": "POST",  
            "process": "",  
            "url": "<http://localhost:8051/api/another/endpoint>"  
        }  
    ]  
}

LoggerDetailsDetalhes de um log

**Objetivo:**Detalhes de um log, a partir do seu id.

**Tipo de requisição:** GET

**Endpoint:** /api/rh/logs/v1/integrations/details/:id

**PathParam:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Observação** | **Obrigatório** | **Exemplo** |
| id | string | Mesmo Id retornado em 'Listagem resumida dos logs' | Sim | "11620630817" |

Exemplo: /api/rh/logs/v1/integrations/details/11620630817

**Estrutura de Retorno:**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| id | string |
| dateTime | Data hora formato yyyy-mm-ddThh:mm:ss |
| isError | boolean |
| statusCode | string |
| verb | string |
| server | string |
| process | string |
| url | string |
| comments | string |
| request | objeto |
| response | objeto |

Para os objetos request / response, estrutura:

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| header | array de objetos |
| body | objeto |

***Não é recomendável retornar nesta api valores relativos a autenticação e autorização da requisição.***

Para array de objetos campo header:

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| key | string |
| value | string |

Para objeto campo body:

|  |  |  |
| --- | --- | --- |
| **Campo** | **Tipo** | **Observações** |
| type | string | valor suportado nesta primeira versão : "raw" |
| format | string | valores suportados : "json" / "xml" ou "txt" |
| content | string | **atenção** se trata de uma string, portanto ao colocar um json ou xml deve-se retornar corretamente formatado para tal, veja os exemplos. |

Exemplo retorno com json

{  
    "id": "11620630817",  
    "dateTime": "2024-05-10T09:53:37",  
    "isError": true,  
    "statusCode": "200",  
    "verb": "GET",  
    "url": "<http://localhost:8051/api/something/to/do?id=80982&scope=global>",  
    "server": "10.29.0.0",  
    "process": "AtualizarStatusEvento",  
    "comments": "algum comentário útil",  
    "request": {  
        "header": [  
            {  
                "key": "User-Agent",  
                "value": "PostmanRuntime/7.37.3"  
            },  
            {  
                "key": "Connection",  
                "value": "keep-alive"  
            }  
        ],  
        "body": {  
            "type": "raw",  
            "format": "json",  
            "content": "{}"  
        }  
    },  
    "response": {  
        "header": [],  
        "body": {  
            "type": "raw",  
            "content": "{\"example\":\"value\"}"  
        }  
    }  
}

Exemplo retorno com xml

{  
    "id": "116351206011",  
    "dateTime": "2024-05-10T09:53:37",  
    "isError": false,  
    "statusCode": "200",  
    "verb": "POST",  
    "url": "<http://spon010119801:8051/wsDataServer/IwsDataServer>",  
    "server": "20.10.0.0",  
    "comments": "algum comentário útil",  
    "process": "",  
    "request": {  
        "header": [  
            {  
                "key": "Content-Type",  
                "value": "text/xml; charset=utf-8"  
            },  
            {  
                "key": "SOAPAction",  
                "value": "<http://www.totvs.com/IwsDataServer/ReadRecord>"  
            },  
            {  
                "key": "Authorization",  
                "value": "Basic bWVzdHJlOnRvdHZz"  
            }  
        ],  
        "body": {  
            "type": "raw",  
            "format": "xml",  
            "content": "<soapenv:Envelope xmlns:soapenv=\"<http://schemas.xmlsoap.org/soap/envelope/\>" xmlns:tot=\"http://www.totvs.com/\">\r\n   <soapenv:Header/>\r\n   <soapenv:Body>\r\n      <tot:ReadRecord>\r\n         <!--Optional:-->\r\n         <tot:DataServerName>FopFuncData</tot:DataServerName>\r\n         <!--Optional:-->\r\n         <tot:PrimaryKey>1;00001</tot:PrimaryKey>\r\n         <!--Optional:-->\r\n         <tot:Contexto>codcoligada=1;codusuario=mestre;codsistema=p</tot:Contexto>\r\n      </tot:ReadRecord>\r\n   </soapenv:Body>\r\n</soapenv:Envelope>"  
        }  
    },  
    "response": {  
        "header": [],  
        "body": {  
            "type": "raw",  
            "content": ""  
        }  
    }  
}

LoggerDetailsListDetalhes de vários logs por id

**Objetivo:**Detalhes de vários logs dado um conjunto de ids.

**Tipo de requisição:** GET

**Endpoint:** /api/rh/logs/v1/integrations/details

**QueryParam:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Observação** | **Obrigatório** | **Exemplo** |
| ids | string | Uma string contendo vários logs separados por vírgula **,** | Sim | "11620630817,11620630812,11620630812" |

Exemplo: /api/rh/logs/v1/integrations/details?ids=11620630817,11081228397,11628122137,116351206011

**Estrutura de Retorno:**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| hasNext | boolean |
| items | array de objetos detalhado abaixo |

Items - cada objeto terá o mesmo retorno especificado em 'Detalhes de um log'

Exemplo retorno

{  
    "hasNext": false,  
    "items": [  
        {  
            "id": "11620630817",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": true,  
            "statusCode": "200",  
            "verb": "GET",  
            "url": "<http://localhost:8051/api/something/to/do?id=80982&scope=global>",  
            "server": "11.29.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "User-Agent",  
                        "value": "PostmanRuntime/7.37.3"  
                    },  
                    {  
                        "key": "Connection",  
                        "value": "keep-alive"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "json",  
                    "content": "{}"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": "{}"  
                }  
            }  
        },  
        {  
            "id": "11081228397",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": false,  
            "statusCode": "200",  
            "verb": "GET",  
            "url": "<http://localhost:8051/api/framework/v2/companies/>",  
            "server": "11.10.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "Authorization",  
                        "value": "Basic bWVzdHJlOnRvdHZz"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "json",  
                    "content": "{}"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": "{\"hasNext\":false,\"items\":[{\"id\":1,\"nomeFantasia\":\"TOTVS SA\",\"federalId\":\"21.867.387/0001-58\",\"name\":\"TOTVS SA\",\"phoneNumber\":\"31-21229000\",\"email\":\"silvana@[totvs.com.br](http://totvs.com.br)\",\"rua\":\"AVENIDA RAJA GABAGLIA\",\"numero\":\"2664\",\"complemento\":\"2º ANDAR\",\"bairro\":\"SANTA LÚCIA\",\"cidade\":\"Belo Horizonte\",\"estado\":\"MG\",\"pais\":\"Brasil\",\"cep\":\"30350-540\"},{\"id\":6,\"nomeFantasia\":\"INSTITUTO TOTVS DE ENSINO SA\",\"federalId\":\"25.578.337/0001-01\",\"name\":\"INSTITUTO TOTVS DE ENSINO SA\",\"phoneNumber\":\"31-21229000\",\"email\":\"masterkeyweb@[totvs.com.br](http://totvs.com.br)\",\"rua\":\"AVENIDA RAJA GABAGLIA\",\"numero\":\"2664\",\"complemento\":\"2º ANDAR\",\"bairro\":\"SANTA LÚCIA\",\"cidade\":\"BELO HORIZONTE\",\"estado\":\"MG\",\"pais\":\"BRASIL\",\"cep\":\"30350-540\"},{\"id\":7,\"nomeFantasia\":\"INSTITUTO TOTVS DE ENSINO SUPERIOR SA\",\"federalId\":\"05.295.401/0001-30\",\"name\":\"INSTITUTO TOTVS DE ENSINO SUPERIOR SA\",\"phoneNumber\":\"31-21229000\",\"email\":\"masterkeyweb@[totvs.com.br](http://totvs.com.br)\",\"rua\":\"AVENIDA RAJA GABAGLIA\",\"numero\":\"2664\",\"complemento\":\"2º ANDAR\",\"bairro\":\"SANTA LÚCIA\",\"cidade\":\"BELO HORIZONTE\",\"estado\":\"MG\",\"pais\":\"BRASIL\",\"cep\":\"30350-540\"}]}"  
                }  
            }  
        },  
        {  
            "id": "11628122137",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": false,  
            "statusCode": "200",  
            "verb": "POST",  
            "url": "<http://localhost:8051/api/rh/esocial/v1/reportEsocialBaseConfer/>",  
            "server": "20.10.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "CodUsuario",  
                        "value": "mestre"  
                    },  
                    {  
                        "key": "CodColigada",  
                        "value": "1"  
                    },  
                    {  
                        "key": "CodSistema",  
                        "value": "p"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "json",  
                    "content": "{\"companyId\":1,\"lotationCode\":[],\"eSocialCategory\":[],\"cpfNumber\":[\"21170836097\"],\"eSocialRegistration\":[],\"paymentPeriod\":\"202304\",\"tribute\":\"3\",\"pageSize\":\"50\",\"differencesOnly\":false}"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": ""  
                }  
            }  
        },  
        {  
            "id": "116351206011",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": false,  
            "statusCode": "200",  
            "verb": "POST",  
            "url": "<http://spon010119801:8051/wsDataServer/IwsDataServer>",  
            "server": "20.10.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "Content-Type",  
                        "value": "text/xml; charset=utf-8"  
                    },  
                    {  
                        "key": "SOAPAction",  
                        "value": "<http://www.totvs.com/IwsDataServer/ReadRecord>"  
                    },  
                    {  
                        "key": "Authorization",  
                        "value": "Basic bWVzdHJlOnRvdHZz"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "xml",  
                    "content": "<soapenv:Envelope xmlns:soapenv=\"<http://schemas.xmlsoap.org/soap/envelope/\>" xmlns:tot=\"http://www.totvs.com/\">\r\n   <soapenv:Header/>\r\n   <soapenv:Body>\r\n      <tot:ReadRecord>\r\n         <!--Optional:-->\r\n         <tot:DataServerName>FopFuncData</tot:DataServerName>\r\n         <!--Optional:-->\r\n         <tot:PrimaryKey>1;00001</tot:PrimaryKey>\r\n         <!--Optional:-->\r\n         <tot:Contexto>codcoligada=1;codusuario=mestre;codsistema=p</tot:Contexto>\r\n      </tot:ReadRecord>\r\n   </soapenv:Body>\r\n</soapenv:Envelope>"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": ""  
                }  
            }  
        }  
    ]  
}

LoggerDetailsListDetalhes de vários logs

**Objetivo:**Detalhes de vários logs

**Tipo de requisição:** GET

**Endpoint:** /api/rh/logs/v1/integrations/details

**QueryParam:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Observação** | **Obrigatorio** | **Exemplo** |
| companyId | int |  | Sim | 1 |
| idIntegration | int |  | Sim |  |
| idLogType | int |  | Sim |  |
| idProcess | int |  | Sim |  |
| startDateTime | Date Time | formato yyyy-mm-ddThh:mm:ss | Não | **2024-05-10T09:53:37** |
| order | string | de acordo com a documentação (<https://tdn.totvs.com/display/public/INT/Guia+de+implementacao+das+APIs+TOTVS#GuiadeimplementacaodasAPIsTOTVS-Filtros>) nesse contexto, só será usado para ordenação do campo dateTime | Não | "-dateTime" |
| page | int |  | Sim | 0 |
| pageSize | int |  | Sim | 30 |

Exemplo: GET /api/rh/logs/v1/integrations/details?companyId=1&idIntegration=0&idLogType=0&idProcess=1&startDateTime=2024-05-10T09:53:37&order=-dateTime&page=1&pageSize=30  
  
Mais detalhes sobre o campo order:

**Estrutura de Retorno:**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| hasNext | boolean |
| items | array de objetos detalhado abaixo |

Items - cada objeto terá o mesmo retorno especificado em 'Detalhes de um log'

Exemplo retorno

{  
    "hasNext": false,  
    "items": [  
        {  
            "id": "11620630817",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": true,  
            "statusCode": "200",  
            "verb": "GET",  
            "url": "<http://localhost:8051/api/something/to/do?id=80982&scope=global>",  
            "server": "11.29.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "User-Agent",  
                        "value": "PostmanRuntime/7.37.3"  
                    },  
                    {  
                        "key": "Connection",  
                        "value": "keep-alive"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "json",  
                    "content": "{}"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": "{}"  
                }  
            }  
        },  
        {  
            "id": "11081228397",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": false,  
            "statusCode": "200",  
            "verb": "GET",  
            "url": "<http://localhost:8051/api/framework/v2/companies/>",  
            "server": "11.10.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "Authorization",  
                        "value": "Basic bWVzdHJlOnRvdHZz"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "json",  
                    "content": "{}"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": "{\"hasNext\":false,\"items\":[{\"id\":1,\"nomeFantasia\":\"TOTVS SA\",\"federalId\":\"21.867.387/0001-58\",\"name\":\"TOTVS SA\",\"phoneNumber\":\"31-21229000\",\"email\":\"silvana@[totvs.com.br](http://totvs.com.br)\",\"rua\":\"AVENIDA RAJA GABAGLIA\",\"numero\":\"2664\",\"complemento\":\"2º ANDAR\",\"bairro\":\"SANTA LÚCIA\",\"cidade\":\"Belo Horizonte\",\"estado\":\"MG\",\"pais\":\"Brasil\",\"cep\":\"30350-540\"},{\"id\":6,\"nomeFantasia\":\"INSTITUTO TOTVS DE ENSINO SA\",\"federalId\":\"25.578.337/0001-01\",\"name\":\"INSTITUTO TOTVS DE ENSINO SA\",\"phoneNumber\":\"31-21229000\",\"email\":\"masterkeyweb@[totvs.com.br](http://totvs.com.br)\",\"rua\":\"AVENIDA RAJA GABAGLIA\",\"numero\":\"2664\",\"complemento\":\"2º ANDAR\",\"bairro\":\"SANTA LÚCIA\",\"cidade\":\"BELO HORIZONTE\",\"estado\":\"MG\",\"pais\":\"BRASIL\",\"cep\":\"30350-540\"},{\"id\":7,\"nomeFantasia\":\"INSTITUTO TOTVS DE ENSINO SUPERIOR SA\",\"federalId\":\"05.295.401/0001-30\",\"name\":\"INSTITUTO TOTVS DE ENSINO SUPERIOR SA\",\"phoneNumber\":\"31-21229000\",\"email\":\"masterkeyweb@[totvs.com.br](http://totvs.com.br)\",\"rua\":\"AVENIDA RAJA GABAGLIA\",\"numero\":\"2664\",\"complemento\":\"2º ANDAR\",\"bairro\":\"SANTA LÚCIA\",\"cidade\":\"BELO HORIZONTE\",\"estado\":\"MG\",\"pais\":\"BRASIL\",\"cep\":\"30350-540\"}]}"  
                }  
            }  
        },  
        {  
            "id": "11628122137",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": false,  
            "statusCode": "200",  
            "verb": "POST",  
            "url": "<http://localhost:8051/api/rh/esocial/v1/reportEsocialBaseConfer/>",  
            "server": "20.10.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "CodUsuario",  
                        "value": "mestre"  
                    },  
                    {  
                        "key": "CodColigada",  
                        "value": "1"  
                    },  
                    {  
                        "key": "CodSistema",  
                        "value": "p"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "json",  
                    "content": "{\"companyId\":1,\"lotationCode\":[],\"eSocialCategory\":[],\"cpfNumber\":[\"21170836097\"],\"eSocialRegistration\":[],\"paymentPeriod\":\"202304\",\"tribute\":\"3\",\"pageSize\":\"50\",\"differencesOnly\":false}"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": ""  
                }  
            }  
        },  
        {  
            "id": "116351206011",  
            "dateTime": "2024-05-10T09:53:37",  
            "isError": false,  
            "statusCode": "200",  
            "verb": "POST",  
            "url": "<http://spon010119801:8051/wsDataServer/IwsDataServer>",  
            "server": "20.10.0.0",  
            "comments": "algum comentário útil",  
            "process": "",  
            "request": {  
                "header": [  
                    {  
                        "key": "Content-Type",  
                        "value": "text/xml; charset=utf-8"  
                    },  
                    {  
                        "key": "SOAPAction",  
                        "value": "<http://www.totvs.com/IwsDataServer/ReadRecord>"  
                    },  
                    {  
                        "key": "Authorization",  
                        "value": "Basic bWVzdHJlOnRvdHZz"  
                    }  
                ],  
                "body": {  
                    "type": "raw",  
                    "format": "xml",  
                    "content": "<soapenv:Envelope xmlns:soapenv=\"<http://schemas.xmlsoap.org/soap/envelope/\>" xmlns:tot=\"http://www.totvs.com/\">\r\n   <soapenv:Header/>\r\n   <soapenv:Body>\r\n      <tot:ReadRecord>\r\n         <!--Optional:-->\r\n         <tot:DataServerName>FopFuncData</tot:DataServerName>\r\n         <!--Optional:-->\r\n         <tot:PrimaryKey>1;00001</tot:PrimaryKey>\r\n         <!--Optional:-->\r\n         <tot:Contexto>codcoligada=1;codusuario=mestre;codsistema=p</tot:Contexto>\r\n      </tot:ReadRecord>\r\n   </soapenv:Body>\r\n</soapenv:Envelope>"  
                }  
            },  
            "response": {  
                "header": [],  
                "body": {  
                    "type": "raw",  
                    "content": ""  
                }  
            }  
        }  
    ]  
}

LoggerStatusEstado do log

**Objetivo:**Identificar se o log ainda está ativo.

**Tipo de requisição:** GET

**Endpoint:** /api/rh/logs/v1/integrations/status

**Query Param:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Observação** | **Obrigatório** | **Exemplo** |
| companyId | int |  | Sim | 1 |
| idIntegration | int |  | Sim | 1 |
| idLogType | int |  | Sim | 1 |
| idProcess | int |  | Sim | 1 |

Exemplo: /api/rh/logs/v1/integrations/status?companyId=1&idIntegration=1&idLogType=0&idProcess=1

**Estrutura de Retorno:**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| active | boolean |

Exemplo retorno

{  
    "active": true  
}

LoggerDeleteRemoção de logs

**Objetivo:**Remoção em lote de logs visualizados no histórico

**Tipo de requisição:** DELETE

**Endpoint:** /api/rh/logs/v1/integrations/

**Query Param:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tipo** | **Observação** | **Obrigatório** | **Exemplo** |
| ids | string |  | Sim | "12910,19120,1234" |

Exemplo: DELETE /api/rh/logs/v1/integrations?ids=12910,19120,1234

**Estrutura de Retorno:**

Apenas status code.
