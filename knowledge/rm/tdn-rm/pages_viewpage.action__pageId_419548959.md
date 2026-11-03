---
content_hash: ffb27c638ebfc765ab773b44ea80966f7a5a3415151779f1a509dfef6635dcb6
fetched_at: '2026-06-29T00:09:13.404227+00:00'
page_id: '419548959'
product: rm
source: tdn-rm
title: API de Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419548959
version: 75
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

Para mais informações sobre consumo de Licença, [Veja Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=419548455#APIsdeFrameworkM%C3%B3duloServi%C3%A7osGlobais-5-ConsumodeLicen%C3%A7aspeloLicenseServer).

# 1 - Métodos

---

Serão apresentados 4 métodos, os quais foram implementados na API de Usuários, são eles:

* GET
* POST
* PUT
* DELETE

# 1.1 - GET

---

## 1.1.1 - Get All (Recuperar todos os usuários)

---

false1.1.1 GetAllfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Url Utilizada:** <http://localhost:8051/api/framework/v1/users>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

1.1.2 - Order (Resultado Ordenado)

Parâmetros

**Order:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente. O resultado com a ordem descendente deve ser precedida do caractere "-" (menos).

**Exemplo 1:** ?order=campo1 (Ascendente)

**Exemplo 2:** ?order=-campo1 (Descendente)

**Múltiplos campos de ordenação:** ?order=[-]campo1, [-]campo2, [-]campo3 ...

---

**Padrão scim:**

**SortBy:** define o campo que será ordenado.

**SortOrder:** parâmetro responsável pela ordenação do resultado, podendo ser ascendente ou descendente.

**Exemplo 1:** ?sortBy=campo1&sortOrder=ascending (Ascendente)

**Exemplo 2:** ?sortBy=campo1&sortOrder=descending (Descendente)

false1.1.2 Order (Asc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/glb/v1/framework?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** active

**Tipo de Ordenação:** Ascendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users?order=active](http://localhost:8099/api/rm/glb/v1/users?order=active)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)truefalse1.1.2 Order (Desc)falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users?order=[-]{campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** active

**Tipo de Ordenação:** Descendente

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users?order=-active](http://localhost:8099/api/rm/glb/v1/users?order=-active)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.3 - Filter (Resultado filtrado)

---

false1.1.3 FilterfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users?{campo}={valor}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** userName

**Valor:** carlosphilippe

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users?userName=carlosphilippe](http://localhost:8099/api/rm/glb/v1/users?userName=carlosphilippe)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.4 - Paginação

---

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=valor1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

---

**Padrão scim:**

**StartIndex:** valor inicial do índice do registro que será retornado.

**Count:** quantidade máxima de registros que serão apresentados.

**Exemplo 1:** ?startIndex=7&count=8

false1.1.4 PaginacaofalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Valor1:** 1

**Valor2:** 1

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users?page=1&pageSize=1](http://localhost:8099/api/rm/glb/v1/users?page=1&pageSize=1)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.5 - Fields (Retorno de campos específicos no resultado)

---

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

---

**Padrão scim:**

**Attributes:** define quais campos serão apresentados no resultado.

**Exemplo 1:** ?attributes=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

---

Obs.: Ainda não é possível utilizar campos complexos no filtro de Fields. Por exemplo: ?fields=name.givenName não irá funcionar.

Entretando, é possível utilizar ?fields=name, onde as 3 propriedades serão retornadas (givenName, familyName e formattedName)

false1.1.5 FieldsfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users?fields={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Campo:** userName

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users?fields=userName](http://localhost:8099/api/rm/glb/v1/users?fields=userName)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.1.6 - GetOne (Recuperar usuário pelo Identificador)

---

Parâmetros

**Expand:** Parâmetro opcional, usado para determinar a(s) propriedade(s) expandables que devem ser retornadas expandidas.

**Exemplo:** ?expand=roles - Nesse exemplo, os perfis associados ao usuário serão retornados na resposta da requisição.

**Valores padrão:** Caso não sejam preenchidos todas as propriedades expandables serão retornadas sem serem expandidas.

---

**Padrão scim:**

O padrão scim não adota o expandable. Por isso, ao adotar esse padrão, para retornar um registro com todas as propriedades expandables expandidas, é necessário utilizar uma propriedade do padrão scim (sortBy/sortOrder ou startIndex/count).

Exemplos: /api/glb/v1/users/id?sortBy=campo1&sortOrder=descending - O retorno dessa chamada exibirá todas as propriedades expandidas.

false1.1.6 GetOnefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 00001

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/00001](http://localhost:8099/api/rm/glb/v1/users/00001)

js1Resultado (JSON)truefalse1.1.6 GetOne expandablefalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users/{id}?expand={campo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** 00001

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/00001?expand=roles](http://localhost:8051/api/rm/glb/v1/users/00001?expand=roles)

js1Resultado (JSON)true

# 1.2 - POST

---

## 1.2.1 - Post (Inserir um usuário)

---

false1.2.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8099

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users](http://localhost:8099/api/rm/glb/v1/users)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)truec\_\_DisplayClass10.b\_\_9(Object instance, Object[] methodParameters)\r\n em System.Web.Http.Controllers.ReflectedHttpActionDescriptor.ExecuteAsync(HttpControllerContext controllerContext, IDictionary`2 arguments, CancellationToken cancellationToken)\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.ApiControllerActionInvoker.d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.ActionFilterResult.d\_\_2.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Runtime.CompilerServices.TaskAwaiter`1.GetResult()\r\n em RM.Lib.Api.Server.ApiAuthenticationFilter.ResultWithChallenge.d\_\_2.MoveNext() na C:\\RM\\Atual\\Release\\Lib\\RM.Lib.Api.Server\\Filters\\Api.AuthenticationFilter.cs:linha 193\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.AuthenticationFilterResult.d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.ExceptionFilterResult.d\_\_0.MoveNext()",
"HelpUrl": null,
"Details": [
{
"Code": "Exception",
"Message": "Violation of PRIMARY KEY constraint 'PKGUSUARIO'. Cannot insert duplicate key in object 'dbo.GUSUARIO'. The duplicate key value is (testeapiusuario).\r\nThe statement has been terminated.",
"DetailMessage": null,
"HelpUrl": null,
"Details": [
{
"Code": "Exception",
"Message": "INSERT INTO [GUSUARIO] ([CODUSUARIO], [NOME], [STATUS], [DATAINICIO], [IGNORARAUTENTICACAOLDAP], [DATAEXPIRACAO], [CONFIRMABTNOK], [SENHA], [CONTROLE], [ULTIMACOLIGADA], [CODACESSO], [DTAEXPSENHA], [DIASEXPSENHA], [OBRIGAALTERARSENHA], [NUMLOGININVALIDO], [DATALOGININVALIDO], [EMAIL], [ACESSONET], [INTERNO1], [DATAULTIMOACESSO], [CODUSUARIOREDE], [DOMINIOREDE], [DATAULTIMOACESSOVALIDO], [USUARIOTWITTER], [SENHATWITTER], [USUARIOFACEBOOK], [SENHAFACEBOOK], [USUARIOLINKEDIN], [SENHALINKEDIN], [USERIDFLUIGIDENTITY], [NOMESOCIAL], [USERID], [RECCREATEDBY], [RECCREATEDON], [RECMODIFIEDBY], [RECMODIFIEDON]) VALUES ('testeapiusuario', null, 1, '08/10/2018 00:00:00', 'F', null, 1, 'jcmaAAAA', -17702, , 'Acesso01', null, , 'T', , null, 'testeapi.usuario@totvs.com.br', 'F', null, null, null, null, null, null, '\\FEz\\1B\\7F1\\18\\B7\\27', null, '\\FEz\\1B\\7F1\\18\\B7\\27', null, '\\FEz\\1B\\7F1\\18\\B7\\27', null, null, '9b69c210-8d20-45b6-afae-534ce10fd4b7', 'mestre', CONVERT ( DATETIME, CONVERT ( VARCHAR, GETDATE(), 120) ), 'mestre', CONVERT ( DATETIME, CONVERT ( VARCHAR, GETDATE(), 120) ))",
"DetailMessage": null,
"HelpUrl": null,
"Details": null
}
]
},
{
"Code": "Exception",
"Message": "INSERT INTO [GUSUARIO] ([CODUSUARIO], [NOME], [STATUS], [DATAINICIO], [IGNORARAUTENTICACAOLDAP], [DATAEXPIRACAO], [CONFIRMABTNOK], [SENHA], [CONTROLE], [ULTIMACOLIGADA], [CODACESSO], [DTAEXPSENHA], [DIASEXPSENHA], [OBRIGAALTERARSENHA], [NUMLOGININVALIDO], [DATALOGININVALIDO], [EMAIL], [ACESSONET], [INTERNO1], [DATAULTIMOACESSO], [CODUSUARIOREDE], [DOMINIOREDE], [DATAULTIMOACESSOVALIDO], [USUARIOTWITTER], [SENHATWITTER], [USUARIOFACEBOOK], [SENHAFACEBOOK], [USUARIOLINKEDIN], [SENHALINKEDIN], [USERIDFLUIGIDENTITY], [NOMESOCIAL], [USERID], [RECCREATEDBY], [RECCREATEDON], [RECMODIFIEDBY], [RECMODIFIEDON]) VALUES ('testeapiusuario', null, 1, '08/10/2018 00:00:00', 'F', null, 1, 'jcmaAAAA', -17702, , 'Acesso01', null, , 'T', , null, 'testeapi.usuario@totvs.com.br', 'F', null, null, null, null, null, null, '\\FEz\\1B\\7F1\\18\\B7\\27', null, '\\FEz\\1B\\7F1\\18\\B7\\27', null, '\\FEz\\1B\\7F1\\18\\B7\\27', null, null, '9b69c210-8d20-45b6-afae-534ce10fd4b7', 'mestre', CONVERT ( DATETIME, CONVERT ( VARCHAR, GETDATE(), 120) ), 'mestre', CONVERT ( DATETIME, CONVERT ( VARCHAR, GETDATE(), 120) ))",
"DetailMessage": null,
"HelpUrl": null,
"Details": null
}
]
}]]>

# 1.3 - PUT

---

## 1.3.1 - Put (Atualizar um usuário)

---

false1.3.1 PostfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8099

**Id:** 00001

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/testeapiusuario](http://localhost:8099/api/rm/glb/v1/users/testeapiusuario)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)truec\_\_DisplayClass10.b\_\_9(Object instance, Object[] methodParameters)\r\n em System.Web.Http.Controllers.ReflectedHttpActionDescriptor.ExecuteAsync(HttpControllerContext controllerContext, IDictionary`2 arguments, CancellationToken cancellationToken)\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.ApiControllerActionInvoker.d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.ActionFilterResult.d\_\_2.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Runtime.CompilerServices.TaskAwaiter`1.GetResult()\r\n em RM.Lib.Api.Server.ApiAuthenticationFilter.ResultWithChallenge.d\_\_2.MoveNext() na C:\\RM\\Atual\\Release\\Lib\\RM.Lib.Api.Server\\Filters\\Api.AuthenticationFilter.cs:linha 193\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.AuthenticationFilterResult.d\_\_0.MoveNext()\r\n--- Fim do rastreamento de pilha do local anterior onde a exceção foi gerada ---\r\n em System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n em System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n em System.Web.Http.Controllers.ExceptionFilterResult.d\_\_0.MoveNext()",
"HelpUrl": null,
"Details": null
}]]>

# 1.4 - DELETE

---

## 1.4.1 - Delete (Deletar um usuário)

---

false1.4.1 DeleteClique aqui para expandir...falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** Teste\_01

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/Teste\_01](http://localhost:8099/api/rm/glb/v1/users/Teste_01)

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 1.5 - PATCH

---

## 1.5.1 - Patch (Atualizar alguns campos de um usuário)

---

false1.5.1 PatchfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users/{id}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8051

**Id:** Teste\_01

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/Teste\_01](http://localhost:8099/api/rm/glb/v1/users/testeapiusuario)

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)true

# Referências (Links)

---

## Roles (Manipulação de Perfis) **A partir da versão 12.1.2306**

---

Associação de Perfis (Roles)

```
Para adicionar e remover perfis á um usuário é necessário realizar as operações de Post/Delete nas rotas de perfis conforme abaixo
```

Víncular perfil ao usuário (Post)false

**Método HTTP: Post**

**Máscara de Url:**  **http://{domínio}:{porta}/api/framework/v1/users/{user}/roles**

falseExemplo de Configuração

**Url Utilizada:** <http://localhost:8051/api/framework/v1/users/apiteste/roles>

| Variável | Descrição | Valor |
| --- | --- | --- |
| **domínio** | endereço do serviço de webservice | localhost |
| **porta** | porta do serviço | 8051 |
| **user** | código do usuário | apiteste |

Exemplo SucessofalseRequest BodyjsJsontruefalseResponse

**HttpStatus: 200**

jsJsontrueAtenção

Ao enviar o codigo da coligada (**Company**) como **0** o sistema irá adicionar o perfil para **todas** as coligadas que o usuário possuir permissão.

Como no exemplo da resposta, o perfil **DBA\_G** foi associado para as coligadas **1,6 e 7**.

Exemplo ErroUsuário já possui algum perfil associadofalseRequest BodyjsJsontrue

**HttpStatus:** 400

falseResponse

{  
    "Code": "FE019",  
    "Message": "Usuário APITESTE já está associado ao perfil 'CodColigada:'1'|Sistema:'G'|CodPerfil:'DBA'|IdPerfil:DBA\_G'!",  
    "DetailMessage": "",  
    "HelpUrl": "",  
    "Details": null  
}

Usuário sem permissãofalseRequest BodyjsJsontrue

**HttpStatus:** 401

falseResponse

{  
    "Code": "FE005",  
    "Message": "O Usuário informado não tem permissão para associar perfis na coligada 1 sistema S!",  
    "DetailMessage": "",  
    "HelpUrl": "",  
    "Details": null  
}

Remover perfil do usuário (Delete)false

**Método HTTP: Delete**

**Máscara de Url:**  **http://{domínio}:{porta}/api/framework/v1/users/{user}/roles/company/{company}/role/{role}**

falseExemplo de Configuração

**Url Utilizada: http://localhost:8051/api/framework/v1/users/apiteste/roles/company/0/role/DBA\_S**

| Variável | Descrição | Valor |
| --- | --- | --- |
| **domínio** | endereço do serviço de webservice | localhost |
| **porta** | porta do serviço | 8051 |
| **user** | código do usuário | apiteste |
| **company** | código da coligada que será utilizada | 0 |
| **role** | Identificador(**IDPERFIL**) do perfil que será atribuído | DBA\_S |

falseResponse (Sucesso ou Erro)

**HttpStatus:** 204

**Response Body:** Vazio

Atenção

Por padrão, nas mensagens de DELETE, a resposta deve ser enviada com HTTP Code 204 (No content) e sem corpo no retorno, **mesmo se não obtiver sucesso**.
