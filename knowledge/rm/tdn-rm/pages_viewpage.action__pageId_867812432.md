---
content_hash: 3fe060223da4c0955240fbfc71a0d2de7c7ad1fa3c746e890dd8077ca118579d
fetched_at: '2026-06-29T00:11:56.632625+00:00'
page_id: '867812432'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Integração RM X Ahgora - Resultado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867812432
version: 27
---

Implementamos a integração que permite ao sistema **Ahgora** enviar os resultados do ponto, ou seja, a movimentação mensal do funcionário, como horas extras, faltas e outros dados, diretamente para a tabela PFMOVTEMP (menu Consulta Movimentação da Integração) e PFHSTFALTAS (menu Funcionários | Movimentos | Controle de Faltas para Cálculo de Avos) do sistema RM.

## Informações Técnicas da API

notech

Criação de API REST que atende no endpoint 'api/rh/v1/ahgora/results' requisições da Ahgora, para envio de resultados do ponto.

ResultsApiAutenticacaoAPI - Autenticação

Possível usar 2 métodos de autenticação;

* Basic Authentication
  + Basta informar usuário / senha em base64 no header > key Authorization.
  + Exemplo: 'Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=='
* OAuth Bearer Token
  + Consumir um endpoint para obtenção do access token
    - Consumir o mesmo endpoint para realizar o refresh token.

**Objetivo:**Detalhar uso do OAuth Bearer Token no RM

**Tipo de requisição:** POST

**Endpoint:** /api/connect/token

**Body:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| grant\_type |  | string | Sim | "password" |
| usename |  | string | Sim | "mestre" |
| password |  | string | Sim | "totvs" |

Exemplo Body

{  
    "grant\_type": "password",  
    "username": "mestre",  
    "password": "totvs"  
}

**Retorno:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| access\_token |  | string | Sim | "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg4QjE0REZCQUNBMDZBMjk4OEQ5MUI3NDMxNkVBNTRCQ0Y3NzlEMzYiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJt" |
| expires\_in |  | int | Sim | 300 |
| refresh\_token |  | string | Sim | "eyJUb2tlbktleSI6Im9TWnR3ZnRQSG1EbXVLNk" |
| token\_type |  | string | Sim | "Bearer" |

Exemplo Retorno.

{  
    "access\_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg4QjE0REZCQUNBMDZBMjk4OEQ5MUI3NDMxNkVBNTRCQ0Y3NzlEMzYiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJtZXN0cmUiLCJodHRwOi8vd3d3LnRvdHZzLmNvbS9ybS9jb25uZWN0aW9uSWQiOiJDb3Jwb3JlUk0iLCJ0ZW5hbnRJZCI6IjMwNzMyN2Q0LTI1ZTgtNDQ5YS04YTIzLTAyNDMxMjk3YzZmYSIsIm5iZiI6MTcyNjUxOTgzMiwiZXhwIjoxNzI2NTIwMTMyLCJpYXQiOjE3MjY1MTk4MzIsImlzcyI6InRvdHZzLXJtLWhvc3QifQ.diemDdno7FSNnjYnufHa-ujbQNNMsrYaH0fVttFXuQ6aOTix9ASAnRTqwGhjwkABpN5LWKz3BdpZOCkWISMWvV0J8RMD5Eb3AEIgy\_nfz6H2Q-bRHKoxrP4Fx0IXOCosBZcu2pTZw2bBma2Fsyfl\_Q9mxh0G0nFSyg6IhRLJXFkKwUyDtxG9ynrdorYclywNiurRvKwyxsGCddLwUWOSQ8G-andwIE0XkCTioUqvYpJDOyw3tgtxZyyqV4IQNoKiNf\_Lm0jix1tRIgFqoBb0QwsAKb7nbEOT1RduciBuSmpfzk82neZapKcqG7MKCcqYyxv\_6jh8KDlZoiPWqzFZ\_Q",  
    "expires\_in": 300,  
    "refresh\_token": "eyJUb2tlbktleSI6Im9TWnR3ZnRQSG1EbXVLNklZWUJoSTRzWDFGcmx4RXVXN0dRMkkzbjhKTSIsImNvbm5lY3Rpb25JZCI6IkNvcnBvcmVSTSJ9",  
    "token\_type": "Bearer"  
}

Será necessário usar o refresh token para atualizar o access\_token, para isso use o mesmo endpoint, porém com um body diferente:

**Tipo de requisição:** POST

**Endpoint:** /api/connect/token

**Body:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| refresh\_token |  | string | Sim | "eyJUb2tlbktleSI6ImRxUHFIcVozUzByQTlmcEl0aU1ub1FSdDdWTzg3RGtWbEV3aVFnaG85U2ciLCJjb25uZWN0aW9uSWQiOiJDb3Jwb3JlUk0ifQ==" |
| grant\_type |  | string | Sim | "refresh\_token" |

Exemplo Body

{  
  "refresh\_token" : "eyJUb2tlbktleSI6ImRxUHFIcVozUzByQTlmcEl0aU1ub1FSdDdWTzg3RGtWbEV3aVFnaG85U2ciLCJjb25uZWN0aW9uSWQiOiJDb3Jwb3JlUk0ifQ==",  
  "grant\_type" : "refresh\_token"  
}

**Retorno:**

O mesmo de quando você autentica.

Exemplo Retorno.

{  
    "access\_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg4QjE0REZCQUNBMDZBMjk4OEQ5MUI3NDMxNkVBNTRCQ0Y3NzlEMzYiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJtZXN0cmUiLCJodHRwOi8vd3d3LnRvdHZzLmNvbS9ybS9jb25uZWN0aW9uSWQiOiJDb3Jwb3JlUk0iLCJ0ZW5hbnRJZCI6IjMwNzMyN2Q0LTI1ZTgtNDQ5YS04YTIzLTAyNDMxMjk3YzZmYSIsIm5iZiI6MTcyNjUxOTgzMiwiZXhwIjoxNzI2NTIwMTMyLCJpYXQiOjE3MjY1MTk4MzIsImlzcyI6InRvdHZzLXJtLWhvc3QifQ.diemDdno7FSNnjYnufHa-ujbQNNMsrYaH0fVttFXuQ6aOTix9ASAnRTqwGhjwkABpN5LWKz3BdpZOCkWISMWvV0J8RMD5Eb3AEIgy\_nfz6H2Q-bRHKoxrP4Fx0IXOCosBZcu2pTZw2bBma2Fsyfl\_Q9mxh0G0nFSyg6IhRLJXFkKwUyDtxG9ynrdorYclywNiurRvKwyxsGCddLwUWOSQ8G-andwIE0XkCTioUqvYpJDOyw3tgtxZyyqV4IQNoKiNf\_Lm0jix1tRIgFqoBb0QwsAKb7nbEOT1RduciBuSmpfzk82neZapKcqG7MKCcqYyxv\_6jh8KDlZoiPWqzFZ\_Q",  
    "expires\_in": 300,  
    "refresh\_token": "eyJUb2tlbktleSI6Im9TWnR3ZnRQSG1EbXVLNklZWUJoSTRzWDFGcmx4RXVXN0dRMkkzbjhKTSIsImNvbm5lY3Rpb25JZCI6IkNvcnBvcmVSTSJ9",  
    "token\_type": "Bearer"  
}

FGTSDigitalListaAPI - Envio Resultados ponto

**Objetivo:** Envio por parte da Ahgora, resultados de ponto, de várias coligadas e seus funcionários.

**Tipo de requisição:** POST

**Endpoint:** api/rh/v1/ahgora/results

**Autenticação:**Envio no header a key "Authorization " com o access\_token formato Bearer.

**Pré-requisito:** Integração Ahgora ativa para coligadas que a usarão. (PPARAMADICIONAIS.INTAHGORAATIVA)

**Body:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| items | Array de objetos funcionário | objeto | Sim |  |

*Objeto funcionário*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| matricula | Matrícula do funcionário (campo exclusivo da Ahgora) | string | Sim | "0101000001" |
| anocomp | Ano competência. | string | Sim | "2024" |
| mescomp | Mês competência. | string | Sim | "08" |
| codfuncionario | Campo usado para identificar a coligada e a chapa do funcionário. É composto por CODCOLIGADA|CHAPA. | string | Sim | "01|00001" |
| resultados | Array de objetos rubrica, representa os resultados de ponto do funcionário. | objeto | Sim |  |

ImportanteAo enviar 'resultados' vazio será validado se o RM usa o parâmetro 'Utiliza controle de faltas para cálculo de avos' (PPARAMADICIONAIS.USACONTROLEFALTASCALCAVOS). Caso positivo e, houver dados na tabela 'PFHSTFALTA' relativos a Ahgora, para coligada, chapa, mês  / ano competência. Ocorrerá a exclusão.

*Objeto evento*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| rubrica | Composto por CODCOLIGADA + PEVENTO.CODIGO. O sistema só irá considerar os últimos 4 dígitos para encontrar o código da verba/rubrica. | string | Sim | "100001" |
| referencia | Valor de referência, dado tipo da verba, será considerado como hora, valor ou ref.  (PFMOVTEMP - HORA, REF, VALOR).  Quando se trata de HORA, o sistema considerará notação sexagesimal. Logo, 1 hora e 59 minutos é igual a "1,59" portando qualquer valor a direita acima de 59 é inválido. | string | Sim | "2024" ou "1,30" ou  "10.5" |
| datafalta | Quando pertinente, informar a data da falta, caso o RM estiver parametrizado, a falta será grava em PFHSTFALTA. | string | Não | "20240802" |

Exemplo Body

{  
    "items": [  
        {  
            "matricula": "0101000001",  
            "anocom": "2024",  
            "mescom": "08",  
            "codfuncionario": "01|00001",  
            "resultados": [  
                {  
                    "rubrica": "0001",  
                    "referencia": "1,33",  
                    "datafalta": "20240802"  
                }  
            ]  
        },  
        {  
            "matricula": "0101000001",  
            "anocom": "2024",  
            "mescom": "07",  
            "codfuncionario": "01|00001",  
            "resultados": [  
                {  
                    "rubrica": "0001",  
                    "referencia": "1,59",  
                    "datafalta": ""  
                }  
            ]  
        }  
    ]  
}

**Estrutura de Retorno:**

O retorno é por rubrica processada, se foram enviados 6 funcionários, cada um com 2 rubricas. A api vai retornar 12 rubricas, cada uma com seu 'status' e 'mensagem'.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| response | Array de objetos resultado | objeto | Sim |  |

*Objeto resultado.*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| resultados | Array de objetos rubrica | objeto | Sim |  |

*Objeto rubrica.*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Descrição** | **Tipo** | **Obrigatório** | **Exemplo** |
| matricula | Matricula enviada na requisição | string | Sim | "0101000001" |
| rubrica | Rubrica enviada na requisição. | string | Não | "10001" |
| status | Informa se foi concluído ou não. Entende-se 'E'  como erro e 'S' como sucesso. | string | Sim | "E" ou "S" |
| mensagem | Mensagem com descrição do status. | string | Sim | "Verba inválida." |
| referencia | Referencia enviada na requisição. | string | Não | "1,59" |
| datafalta | Datafalta enviada na requisição. | string | Não | "20240802" |

Exemplo de retorno, sucesso.

{  
    "response": [  
        {  
            "resultados": [  
                {  
                    "matricula": "0101000001",  
                    "rubrica": "10001",  
                    "status": "S",  
                    "mensagem": "Operação realizada com sucesso",  
                    "referencia": "1,33",  
                    "datafalta": "20240802"  
                },  
                {  
                    "matricula": "0101000001",  
                    "rubrica": "10001",  
                    "status": "S",  
                    "mensagem": "Operação realizada com sucesso",  
                    "referencia": "1,59",  
                    "datafalta": ""  
                }  
            ]  
        }  
    ]  
}

Exemplo de retorno, sucesso parcial.

{  
    "response": [  
        {  
            "resultados": [  
                {  
                    "matricula": "0101000001",  
                    "rubrica": "0001",  
                    "status": "E",  
                    "mensagem": "Para esta verba. O valor a direta do campo referencia deve ser representado em minutos e não pode ser superior a 59",  
                    "referencia": "1,67",  
                    "datafalta": "20240802"  
                },  
                {  
                    "matricula": "0101000001",  
                    "rubrica": "0001",  
                    "status": "S",  
                    "mensagem": "Operação realizada com sucesso",  
                    "referencia": "1,59",  
                    "datafalta": ""  
                }  
            ]  
        }  
    ]  
}

Exemplo de retorno, sucesso enviando resultados vazio de um funcionário.

{  
    "response": [  
        {  
            "resultados": [  
                {  
                    "matricula": "0101000001",  
                    "status": "S",  
                    "mensagem": "Operação realizada com sucesso"  
                }  
            ]  
        }  
    ]  
}

**Para o retorno de erro (status code diferente da família 200), seguir a estrutura abaixo.**

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| code | string |
| message | string |
| detailedMessage | string |
| details | array de objetos com mais detalhes |

Objeto detalhes

|  |  |
| --- | --- |
| **Campo** | **Tipo** |
| code | string |
| message | string |
| detailedMessage | string |

Exemplo de retorno

{  
    "code": "FE017",  
    "message": "Código coligada inválido ou inativo : 15",  
    "detailedMessage": null,  
    "helpUrl": null,  
    "details": [  
        {  
            "code": "RMSApplicationException",  
            "message": "Código coligada inválido ou inativo : 15",  
            "detailedMessage": "   em RM.Fop.Api.Server.FopAhgoraApiServer.<ValidarCodColigada>d\_\_9.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em RM.Fop.Api.Server.FopAhgoraApiServer.<InserirResultadosPonto>d\_\_7.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em RM.Fop.Api.FopAhgoraController.<InserirResultadosPonto>d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Threading.Tasks.TaskHelpersExtensions.<CastToObject>d\_\_3`1.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Controllers.ApiControllerActionInvoker.<InvokeActionAsyncCore>d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d\_\_5.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d\_\_5.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<ExecuteActionFilterAsyncCore>d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d\_\_5.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d\_\_5.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<ExecuteActionFilterAsyncCore>d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d\_\_5.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d\_\_5.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.ActionFilterAttribute.<ExecuteActionFilterAsyncCore>d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Controllers.ActionFilterResult.<ExecuteAsync>d\_\_2.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.AuthorizationFilterAttribute.<ExecuteAuthorizationFilterAsyncCore>d\_\_2.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Filters.AuthorizationFilterAttribute.<ExecuteAuthorizationFilterAsyncCore>d\_\_2.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em RM.Lib.Api.Server.ApiAuthenticationFilter.ResultWithChallenge.<ExecuteAsync>d\_\_2.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Controllers.AuthenticationFilterResult.<ExecuteAsync>d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n   em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   em System.Web.Http.Controllers.ExceptionFilterResult.<ExecuteAsync>d\_\_0.MoveNext()",  
            "helpUrl": null,  
            "details": null  
        }  
    ]  
}
