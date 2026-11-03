---
content_hash: 3335edb97463c041feac86b230e1a7ccb5daa0b8c1f93f98e77d99a1d8b4604c
fetched_at: '2026-06-29T00:12:14.583721+00:00'
page_id: '967623020'
product: rm
source: tdn-rm
title: Contrato 2.0 - API
type: documentation
url: https://tdn.totvs.com/display/LRM/Contrato+2.0+-+API
version: 128
---

# Sumário

---

Sumário

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API da  utilizando todos os métodos implementados. E as api's complementares referente aos itens do contrato e processos do contrato, item e parcela.

Importante

Em requisições do tipo **PUT**, o objeto deve ser enviado de forma **completa**. Qualquer campo que não seja informado na requisição será interpretado como **nulo** (vazio) ou **removido**, resultando na limpeza do valor previamente armazenado.

Existe controle de concorrência baseado no campo **RecModifiedOn**. Esse campo deve ser sempre preenchido com o **último valor persistido na base de dados**. Caso seja informado um valor diferente do atual, a requisição será rejeitada por **conflito de concorrência**.

# 1 - Contrato

---

Serão apresentados 4 métodos, os quais foram implementados na API de Contrato, são eles:

* GET
* POST
* PUT
* DELETE

## 1.1 - GET

---

### 1.1.1 - Get All (Recuperar todos os contratos)

falseGetAll

Retorna todos os contratos cadastrados.

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 1.1.2 - Paginação

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Valor1:** 1

**Valor2:** 2

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts?page=1&pageSize=2>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 1.1.3 - Fields (Retorno de campos específicos no resultado)

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Campo 1:** name

**Campo 2:** codeStatusInvoicing

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts?fields=name,codeStatusInvoicing>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 1.1.4 - GetOne (Recuperar contrato pelo identificador)

Nessa requisição será retornado o contrato de identificador informado

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 236

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|236>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 1.2 - POST

---

### 1.2.1 - Post (Inserir um contrato)

falsePost

A inclusão de um novo contrato será feita contendo os seus dados.

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...

```
{  
  
    "code": "FE006",  
  
    "message": "Chave duplicada\r\n\r\nPossíveis causas:\r\n  - inclusão de registro cujo valor da chave primária já existe\r\n  - inclusão de registro cujo valor do índice único já existe",  
  
    "detailedMessage": null,  
  
    "helpUrl": null,  
  
    "details": [  
  
        {  
  
            "code": "SqlException",  
  
            "message": "Cannot insert duplicate key row in object 'dbo.TCNT' with unique index 'TXCNTCOD'. The duplicate key value is (1, 1, 468303).\r\nThe statement has been terminated.",  
  
            "detailedMessage": "   em System.Data.SqlClient.SqlConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction)\r\n   em System.Data.SqlClient.TdsParser.ThrowExceptionAndWarning(TdsParserStateObject stateObj, Boolean callerHasConnectionLock, Boolean asyncClose)\r\n   em System.Data.SqlClient.TdsParser.TryRun(RunBehavior runBehavior, SqlCommand cmdHandler, SqlDataReader dataStream, BulkCopySimpleResultSet bulkCopyHandler, TdsParserStateObject stateObj, Boolean& dataReady)\r\n   em System.Data.SqlClient.SqlCommand.FinishExecuteReader(SqlDataReader ds, RunBehavior runBehavior, String resetOptionsString, Boolean isInternal, Boolean forDescribeParameterEncryption, Boolean shouldCacheForAlwaysEncrypted)\r\n   em System.Data.SqlClient.SqlCommand.RunExecuteReaderTds(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, Boolean async, Int32 timeout, Task& task, Boolean asyncWrite, Boolean inRetry, SqlDataReader ds, Boolean describeParameterEncryptionRequest)\r\n   em System.Data.SqlClient.SqlCommand.RunExecuteReader(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, String method, TaskCompletionSource`1 completion, Int32 timeout, Task& task, Boolean& usedCache, Boolean asyncWrite, Boolean inRetry)\r\n   em System.Data.SqlClient.SqlCommand.InternalExecuteNonQuery(TaskCompletionSource`1 completion, String methodName, Boolean sendToPipe, Int32 timeout, Boolean& usedCache, Boolean asyncWrite, Boolean inRetry)\r\n   em System.Data.SqlClient.SqlCommand.ExecuteNonQuery()\r\n   em Dapper.SqlMapper.ExecuteCommand(IDbConnection cnn, CommandDefinition& command, Action`2 paramReader) na C:\\projects\\dapper\\Dapper\\SqlMapper.cs:linha 2827\r\n   em Dapper.SqlMapper.ExecuteImpl(IDbConnection cnn, CommandDefinition& command) na C:\\projects\\dapper\\Dapper\\SqlMapper.cs:linha 570\r\n   em Dapper.SqlMapper.Execute(IDbConnection cnn, String sql, Object param, IDbTransaction transaction, Nullable`1 commandTimeout, Nullable`1 commandType) na C:\\projects\\dapper\\Dapper\\SqlMapper.cs:linha 443\r\n   em RM.Lib.Data.ORM.Dapper.RMSDapperORMAdapter.Insert[T](T entity, IClassMapper classMap, Boolean insertControlColumns)\r\n   em RM.Lib.Data.ORM.Dapper.RMSDapperORMAdapter.Insert[T](T entity, IClassMapper classMap)\r\n   em RM.Lib.Data.DbServices.Insert[T](T entity, IClassMapper classMap)",  
  
            "helpUrl": null,  
  
            "details": null  
  
        }  
  
    ]  
  
}
```

## 1.3 - PUT

---

### 1.3.1 - Put (Atualização de um contrato)

falsePut

A atualização do contrato será feita contendo os seus dados.

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 249

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|249>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 1.4 - DELETE

---

### 1.4.1 - Delete (Excluir um contrato)

falseDelete

**Máscara de Url:**http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 249

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|249>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado o respondeCode = 204 e a resposta em branco.

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 2 - Complemento do Contrato

---

Serão apresentados 2 métodos, os quais foram implementados na API do item de complemento de contrato, são eles:

* GET
* PUT

## 2.1 - GET

---

### 2.1.1 - Get All (Recuperar todos os complementos de contratos)

falseGetAll

Retorna todos os campos complementados de um contrato.

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/complementary-fields/TCNTCOMPL/{coligada}{id contrato}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Url Utilizada:** [http://localhost:8052/api/framework/v1/complementary-fields/TCNTCOMPL/1|67](http://localhost:8052/api/ctr/v1/contracts/1|236/items) 

p

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 2.1.2 - Paginação

Parâmetros

**Page:** Página que será apresentada.

**PageSize**: Quantidade máxima de registros por página que serão apresentados.

**Exemplo:** ?page=1&pageSize=1

**Valores padrão:** Caso não sejam preenchidos os parâmetros evidenciados acima serão preenchidos com valores padrão.

**Page:** 1

**PageSize:** 20

falsePaginação

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts?page={valor1}&pageSize={valor2}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Valor1:** 1

**Valor2:** 2

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts?page=1&pageSize=2>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 2.1.3 - Fields (Retorno de campos específicos no resultado)

Parâmetros

**Fields:** parâmetro responsável pela especialização de campos em um resultado, ou seja, o usuário define quais campos serão apresentados no resultado.

**Exemplo:** ?fields=campo1

**Múltiplos campos de ordenação:** ?fields=campo1, campo2, campo3 ...

falseFields

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts?fields={campos}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Campo 1:** name

**Campo 2:** codeStatusInvoicing

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts?fields=name,codeStatusInvoicing>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 2.1.4 - GetOne (Recuperar contrato pelo identificador)

Nessa requisição será retornado o contrato de identificador informado

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 236

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|236>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 2.1 - PUT

---

### 2.1.1 - Put (Atualização de um contrato)

falsePut

A atualização do contrato será feita contendo os seus dados.

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/complementary-fields/TCNTCOMPL/{coligada}|{id contrato}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 249

**Url Utilizada:** http://localhost:8052/api/framework/v1/complementary-fields/TCNTCOMPL/1|67 

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 3 - Item do Contrato

---

Serão apresentados 4 métodos, os quais foram implementados na API do item de contrato, são eles:

* GET
* POST
* PUT
* DELETE

## 3.1 - GET

---

### 3.1.1 - Get All (Recuperar todos os itens de um contrato)

falseGetAll

Retorna todos os itens de um contrato.

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}{id contrato}/items

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|236/items>

p

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

### 3.1.2 - GetOne (Recuperar item do contrato pelo identificador)

Nessa requisição será retornado o item de identificador informado

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}/items/{coligada}|{id contrato}|{id item}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 236

**Id item:** 1

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|236/items/1|236|1>

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 3.2 - POST

---

### 3.2.1 - Post (Inserir um item)

falsePost

A inclusão de um novo item de contrato será feita contendo os seus dados.

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}/items/

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|236/items/>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...

```
{  
    "code": "FE016",  
    "message": "Coligada e/ou Identificador do contrato inválidos!",  
    "detailedMessage": "",  
    "helpUrl": "",  
    "details": null  
}
```

## 3.3 - PUT

---

### 3.3.1 - Put (Atualização de um item)

falsePut

A atualização do item do contrato será feita contendo os seus dados.

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}/items/{coligada}|{id contrato}|{id item}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 236

**Id item:** 1

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|236/items/1|236|1>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 3.4 - DELETE

---

### 3.4.1 - Delete (Excluir um item)

falseDelete

**Máscara de Url:**http://{domínio}:{porta}/api/ctr/v1/contracts/{coligada}|{id contrato}/items/{coligada}|{id contrato}|{id item}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 236

**Id item:** 1

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contracts/1|236/items/1|236|1>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado true

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 4 - Parcela do Item

---

Serão apresentados 2 métodos, os quais foram implementados na API da parcela do item, são eles:

* GET
* PUT

## 4.1 - GET

---

### 4.1.1 - Get All (Recuperar todos as parcelas de um item)

falseGetAll

Recupera todas as parcelas de um item.

**Máscara de Url:**  http://{domínio}:{porta}/api/ctr/v1/contract-item/{coligada}|{id contrato}|{id item do contrato}/installments

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**coligada**: 1

**id contrato:** 122

**id item do contrato:** 1

**Url Utilizada:** [http://localhost:8082/api/ctr/v1/contract-item/1|122|1/installments](http://localhost:8082/api/ctr/v1/contractitem/1|122|1/installments)

p

falseExemplo de ResultadoVer resultado JSON...

{

    "hasNext": false,  
    "items": [  
        {  
            "companyId": 1,  
            "contractId": 122,  
            "contractItemId": 1,  
            "installmentNumber": 1,  
            "status": 0,  
            "descriptionStatus": "A Faturar",  
            "dueDate": "2025-03-01T00:00:00-03:00",  
            "valueInstallment": 1000.0000,  
            "presentValue": 0.0,  
            "balanceDue": 0.0,  
            "interestAmortization": 0.0,  
            "installmentAmortization": 0.0,  
            "termClassification": "N",  
            "reductionValue": 0.0,  
            "increaseValue": 0.0  
        },  
        {  
            "companyId": 1,  
            "contractId": 122,  
            "contractItemId": 1,  
            "installmentNumber": 2,  
            "status": 0,  
            "descriptionStatus": "A Faturar",  
            "dueDate": "2025-04-01T00:00:00-03:00",  
            "valueInstallment": 1000.0000,  
            "presentValue": 0.0,  
            "balanceDue": 0.0,  
            "interestAmortization": 0.0,  
            "installmentAmortization": 0.0,  
            "termClassification": "N",  
            "reductionValue": 0.0,  
            "increaseValue": 0.0  
        },  
        {  
            "companyId": 1,  
            "contractId": 122,  
            "contractItemId": 1,  
            "installmentNumber": 3,  
            "status": 0,  
            "descriptionStatus": "A Faturar",  
            "dueDate": "2025-05-01T00:00:00-03:00",  
            "valueInstallment": 1000.0000,  
            "presentValue": 0.0,  
            "balanceDue": 0.0,  
            "interestAmortization": 0.0,  
            "installmentAmortization": 0.0,  
            "termClassification": "N",  
            "reductionValue": 0.0,  
            "increaseValue": 0.0  
        }  
    ]  
}

### 4.1.2 - GetOne (Recuperar parcela de um item pelo identificador)

Nessa requisição será retornado a parcela de identificador informado

falseFilter

**Máscara de Url:**  http://{domínio}:{porta}/api/ctr/v1/contract-item/{coligada}|{id contrato}|{id item do contrato}/installments/{coligada}|{id contrato}|{id item do contrato}|{id parcela do item}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**Id contrato:** 236

**Id item:** 1

**Url Utilizada:** [http://localhost:8052/api/ctr/v1/contract-item/1|122|1/installments/1|122|1|1](http://localhost:8052/api/ctr/v1/contracts/1|236/items/1|236|1)

falseExemplo de ResultadoVer resultado JSON...js1Resultado (JSON)true

## 4.2 - PUT

---

### 4.2.1 - Put (Atualização de uma parcela)

falsePut

Atualiza a data de vencimento da parcela de um item

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contractitem/{coligada}|{id contrato}|{id item do contrato}/installments/{coligada}|{id contrato}|{id item do contrato}|{id parcela do item}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**id contrato:** 122

**id item do contrato:** 1

**id parcela do item:** 1

**Url Utilizada: <http://localhost:8052/api/ctr/v1/contract-item/1|122|1/installments/1|122|1|1>**

falseExemplo de EntradaVer resultado JSON...

{  
    "companyId": 1,  
    "contractId": 122,  
    "contractItemId": 1,  
    "installmentNumber": 1,  
    "status": 0,  
    "descriptionStatus": "A Faturar",  
    "dueDate": "2025-09-11T00:00:00-03:00",  
    "valueInstallment": 1000,  
    "presentValue": 0,  
    "balanceDue": 0,  
    "interestAmortization": 0,  
    "installmentAmortization": 0,  
    "termClassification": "N",  
    "reductionValue": 0,  
    "increaseValue": 0  
}

falseExemplo de Resultado PositivoVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 5 - Rateio do Item

---

 Serão apresentados 4 métodos, os quais foram implementados na API do rateio do item, são eles:

* GET
* POST
* PUT
* DELETE

## 5.1 - GET

---

### 5.1.1 - Get All (Recuperar todos os rateios de um item)

falseGetAll

Recupera todos os rateios de um item.

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contract-item/{coligada}|{id contrato}|{id item do contrato}/cost-center-apportionments

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**coligada:** 1

**id contrato:** 122

**id item do contrato:** 1

**Url Utilizada: <http://localhost:8052/api/ctr/v1/contract-item/1|122|1/cost-center-apportionments>**

p

falseExemplo de ResultadoVer resultado JSON...{  
    "hasNext": false,  
    "items": [  
        {  
            "companyId": 1,  
            "contractId": 122,  
            "contractItemId": 1,  
            "costCenterInternalId": "1|01",  
            "costCenter": "01",  
            "description": "Administrativo",  
            "percentage": 10.0000,  
            "value": 300.00000000,  
            "history": "teste",  
            "itemValue": 3000.0000  
        },  
        {  
            "companyId": 1,  
            "contractId": 122,  
            "contractItemId": 1,  
            "costCenterInternalId": "1|01.1",  
            "costCenter": "01.1",  
            "description": "Departamento Pessoal",  
            "percentage": 10.0000,  
            "value": 300.00000000,  
            "itemValue": 3000.0000  
        }  
    ]  
}

### 5.1.2 - GetOne (Recuperar um rateio de um item pelo identificador)

Nessa requisição será retornado o rateio de identificador informado.

falseFilter

**Máscara de Url:** http://{domínio}:{porta}/api/ctr/v1/contract-item/{coligada}|{id contrato}|{id item do contrato}/cost-center-apportionments/{coligada}|{id contrato}|{id item do contrato}|{codigo de centro de custo}

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Coligada:** 1

**coligada:** 1

**id contrato:** 122

**id item do contrato:** 1

**codigo de centro de custo:** 01.5

**Url Utilizada:** <http://localhost:8052/api/ctr/v1/contract-item/1|122|1/cost-center-apportionments/1|122|1|01.5>

falseExemplo de ResultadoVer resultado JSON...

{  
    "companyId": 1,  
    "contractId": 122,  
    "contractItemId": 1,  
    "costCenterInternalId": "1|01.5",  
    "costCenter": "01.5",  
    "description": "Comercial",  
    "percentage": 5.0000,  
    "value": 150.00000000,  
    "history": "teste comercial rateio",  
    "itemValue": 3000.0000  
}

## 5.2 - POST

---

### 5.2.1 - Post (Inserir rateio em um item)

falsePost

Inclusão de rateio para um item

**Máscara de Url: http://{domínio}:{porta}/api/ctr/v1/contract-item/{coligada}|{id contrato}|{id item do contrato}/cost-center-apportionments**

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**coligada:** 1

**id contrato:** 122

**id item do contrato:** 1

**Url Utilizada:**  <http://localhost:8052/api/ctr/v1/contract-item/1|122|1/cost-center-apportionments/>

falseExemplo de EntradaVer resultado JSON...js1Resultado (JSON)truefalseExemplo de Resultado PositivoVer resultado JSON...

{

    "companyId": 1,  
    "contractId": 122,  
    "contractItemId": 1,  
    "costCenterInternalId": "1|01.5",  
    "costCenter": "01.5",  
    "percentage": 5.0,  
    "value": 0.0,  
    "history": "teste comercial rateio",  
    "itemValue": 0.0  
}falseExemplo de Resultado NegativoVer resultado JSON...

```
{  
    "code": "FE016",  
    "message": "Coligada e/ou Identificador do contrato inválidos!",  
    "detailedMessage": "",  
    "helpUrl": "",  
    "details": null  
}
```

## 5.3 - PUT

---

### 5.3.1 - Put (Atualização do rateio de um item)

falsePut

Atualização do rateio de um item

**Máscara de URL:** `http://{domínio}:{porta}/api/ctr/v1/contract-item/{coligada}|{id contrato}|{id item do contrato}/cost-center-apportionments/{coligada}|{id contrato}|{id item do contrato}|{codigo de centro de custo}`

falseExemplo de Configuração

**Domínio:** localhost

**Porta:** 8052

**coligada:** 1

**id contrato:** 122

**id item do contrato:** 1

**codigo de centro de custo:** 01.5

**Url Utilizada:**  <http://localhost:8052/api/ctr/v1/contract-item/1|122|1/cost-center-apportionments/1|122|1|01.5>

falseExemplo de EntradaVer resultado JSON...

{  
    "companyId": 1,  
    "contractId": 122,  
    "contractItemId": 1,  
    "costCenterInternalId": "1|01.5",  
    "costCenter": "01.5",  
    "description": "Comercial",  
    "percentage": 2.0,  
    "value": 0.0,  
    "history": "teste comercial rateio editado",  
    "itemValue": 0.0  
}

falseExemplo de Resultado PositivoVer resultado JSON...

{  
    "companyId": 1,  
    "contractId": 122,  
    "contractItemId": 1,  
    "costCenterInternalId": "1|01.5",  
    "costCenter": "01.5",  
    "description": "Comercial",  
    "percentage": 2.0,  
    "value": 0.0,  
    "history": "teste comercial rateio editado",  
    "itemValue": 0.0  
}

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

## 5.4 - DELETE

---

### 5.4.1 - Delete (Excluir um rateio de um item)

falseDelete

**Máscara de URL:** `http://{domínio}:{porta}/api/ctr/v1/contract-item/{coligada}|{id contrato}|{id item do contrato}/cost-center-apportionments/{coligada}|{id contrato}|{id item do contrato}|{codigo de centro de custo}`

falseExemplo de Configuração

**Domínio:** localhost

**Porta:** 8052

**coligada:** 1

**id contrato:** 122

**id item do contrato:** 1

**codigo de centro de custo:** 01.5

**Url Utilizada:**  <http://localhost:8052/api/ctr/v1/contract-item/1|122|1/cost-center-apportionments/1|122|1|01.5>

falseExemplo de Resultado Positivo Postman

Obs.: Em caso de sucesso, será retornado true

falseExemplo de Resultado NegativoVer resultado JSON...js1Resultado (JSON)true

# 6 - Processos do Contrato

---

Serão apresentados 11 processos do contrato, são eles:

* Faturar Contrato
* Cancelar Faturamento Contrato
* Gerar Previsão Financeira
* Cancelar Previsão Financeira
* Alterar Status Contrato
* Copiar Contrato
* Reajustar Preço
* Cancelar Reajuste Preço
* Reclassificar Contabilidade
* Cancelar Reclassificação Contábil
* Contabilizar Contrato

Eles podem ser realizados pelo método POST da API de [JobScheduler](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-1.2.1-Post(Inserirumagendamentodejob)).

falsePost

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/jobscheduler

falseExemplo de Configuração

**Domínio:**localhost

**Porta:** 8052

**Url Utilizada:** <http://localhost:8052/api/framework/v1/jobscheduler>

falseExemplo de entrada 3 camadas

Caso a propriedade recurrent seja igual a true, obrigatoriamente deve-se informar o [Tipo de Recorrência](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-recurrencyType).

**Propriedades obrigatórias:**

processID, firstExecution, recurrent, executionParameter

executionParameter: Context, ProcessName, UserName, PrimaryKeyList, PrimaryKeyNames

falseExemplo de entrada ambiente local

Se o Host estiver executando local (3camadas = false) não é possível criar um agendamento de job. Neste cenário, para executar o job imediatamente, é preciso que no Body da requisição a recorrência esteja como 'false' e não sejam enviadas as propriedades "ScheduleDateTime" e [Tipo de Recorrência](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-recurrencyType).

**Propriedades obrigatórias:**

processID, recurrent, executionParameter

executionParameter: Context, ProcessName, UserName, PrimaryKeyList, PrimaryKeyNames

falseExemplo de resultado negativoVer resultado JSON...js1Resultado (JSON)true

## 6.1 - Faturar Contrato

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.2 - Cancelar Faturamento Contrato

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.3 - Gerar Previsão Financeira

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.4 - Cancelar Previsão Financeira

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.5 - Alterar Status Contrato

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.6 - Copiar Contrato

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.7 - Reajustar Preço

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.8 - Cancelar Reajuste Preço

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.9 - Reclassificar Contabilidade

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.10 - Cancelar Reclassificação Contábil

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 6.11 - Contabilizar Contrato

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

# 7 - Processos do Item do Contrato

---

Serão apresentados 6 processos do contrato, são eles:

* Gerar Aditivo
* Cancelar Aditivo
* Gerar Medição
* Gerar Medição Múltiplos Itens
* Cancelar Medição
* Redistribuir Valor Parcela

Eles podem ser realizados pelo método POST da API de [JobScheduler](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-1.2.1-Post(Inserirumagendamentodejob)).

## 7.1 - Gerar Aditivo

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 7.2 - Cancelar Aditivo

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 7.3 - Gerar Medição

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 7.4 - Gerar Medição Múltiplos Itens

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 7.5 - Cancelar Medição

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

## 7.6 - Redistribuir Valor Parcela

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

# 8 - Processos da Parcela

---

Será apresentado o processo de Gerar Abatimento ou Acréscimo. 

Eles podem ser realizados pelo método POST da API de [JobScheduler](https://tdn.totvs.com/display/public/LRM/API+de+JobScheduler#APIdeJobScheduler-1.2.1-Post(Inserirumagendamentodejob)).

## 8.1 - Gerar Abatimento ou Acréscimo

falseExemplo de entrada 3 camadasVer resultado JSON...js1Resultado (JSON)truefalseExemplo de entrada ambiente localVer resultado JSON...js1Resultado (JSON)truefalseExemplo de resultado positivoVer resultado JSON...js1Resultado (JSON)true

# 9 - Descrição dos campos JSON de entrada/retorno

---

Descrição dos campos JSON de entrada/retorno

## 9.1 - Contrato

* companyId: Identifcador do código da coligada do contrato
* contractId: Identificador do contrato
* userCode: Usúario de inclusão
* contractCode: Código do contrato
* name: Nome do contrato
* codeStatusInvoicing: Código do status do faturamento
* descriptionStatusInvoicing: Descrição do status do faturamento
* statusFinancialForecast: Status da previsão financeira
* statusFinancialForecastDescription: Descrição do status da previsão financeira
* statusCodeInternalId: Identifcador do status do contrato
* statusCode: Código do status do contrato
* typeCodeInternalId: Identifcador do tipo do contrato
* typeCode: Código do tipo do contrato
* typeDescription: Descrição do tipo do contrato
* natureContract: Natureza do contrato
* contractorInternalId: Identifcador do contratante
* customerVendorInternalId: Identifcador do contratado
* branchId: Identifcador da filial
* branchName: Nome Filial
* customerVendorCompanyId: Identifcador da coligada do contratado
* customerVendorId: Identifcador do contratado
* customerVendorCnpj: CNPJ do contratado
* customerVendorName: Nome fantasia do contratado
* customerVendorRegisteredName: Razão Social do contratado
* contractDate: Data do contrato
* startDate: Data de ínicio vigência do contrato
* endDate: Data fim vigência do contrato
* contractValue: Valor do contrato
* invoicedValue: Valor faturado
* balanceContract: Saldo do contrato
* classificationTable1InternalId: Identificador da Tabela de Classificação 1
* classificationTable1: Código da Tabela de Classificação 1
* classificationTable2InternalId: Identificador da Tabela de Classificação 2
* classificationTable2: Código da Tabela de Classificação 2
* classificationTable3InternalId: Identificador da Tabela de Classificação 3
* classificationTable3: Código da Tabela de Classificação 3
* classificationTable4InternalId: Identificador da Tabela de Classificação 4
* classificationTable4: Código da Tabela de Classificação 4
* classificationTable5InternalId: Identificador da Tabela de Classificação 5
* classificationTable5: Código da Tabela de Classificação 5
* optionalTable1InternalId: Identificador da Tabela de Faturamento 1
* optionalTable1: Código da Tabela de Faturamento 1
* optionalTable2InternalId: Identificador da Tabela de Faturamento 2
* optionalTable2: Código da Tabela de Faturamento 2
* optionalTable3InternalId: Identificador da Tabela de Faturamento 3
* optionalTable3: Código da Tabela de Faturamento 3
* optionalTable4InternalId: Identificador da Tabela de Faturamento 4
* optionalTable4: Código da Tabela de Faturamento 4
* optionalTable5InternalId: Identificador da Tabela de Faturamento 5
* optionalTable5: Código da Tabela de Faturamento 5
* seller1InternalId: Identificador Funcionário 1
* sellerCode1: Código Funcionário 1
* sellerCommission1: Comissão Funcionário 1
* seller2InternalId: Identificador Funcionário 2
* sellerCode2: Código Funcionário 2
* sellerCommission2: Comissão Funcionário 2
* seller3InternalId: Identificador Funcionário 3
* sellerCode3: Código Funcionário 3
* sellerCommission3: Comissão Funcionário 3
* seller4InternalId: Identificador Funcionário 4
* sellerCode4: Código Funcionário 4
* sellerCommission4: Comissão Funcionário 4
* **representativeCommission:**
* fiscalNatureInternalId: Identifcador da Natureza Fiscal do contrato
* fiscalNatureId: Identifcador da Natureza de Operação
* costCenterInternalId: Identifcador do Centro de Custo
* costCenterCode: Código do Centro de Custo
* departmentCodeInternalId: Identifcador do código do Departamento
* departmentCode: Código do Departamento
* hasAccounting: Possui Contabilidade
* observation: Observação
* freeField1: Campo Livre 1
* freeField2: Campo Livre 2
* freeField3: Campo Livre 3
* history: Histórico
* birthdayMonth: Mês de Aniversário
* version: Versão do contrato
* recModifiedOn: Última modificação do registro

## 9.2 - Item do Contrato

* customerVendorCompanyId: Identificador da Coligada do Cli/For Destinatário
* codeStatusInvoicing: Código do status do faturamento
* statusFinancialForecast: Status da previsão financeira
* companyId: Código da Coligada
* contractId: Identificador do contrato
* contractItemId: Identificador do item do contrato
* sequentialNumber: Número sequencial do item
* productCode: Código do produto
* productDescription: Descrição do produto
* fantasyName: Nome fantasia do produto
* typeOfInvoicing: Tipo de Faturamento
* descriptionTypeOfInvoicing: Descrição do Tipo de faturamento
* productId: Identificador do Produto/Serviço
* unitCode: Código da Unidade
* descriptionStatusInvoicing: Descrição do status do faturamento
* statusFinancialForecastDescription: Descrição do Status da previsão financeira
* startDate: Data de ínicio vigência do contrato
* endDate: Data fim vigência do contrato
* quantity: Quantidade
* price: Preço
* discount: Valor do desconto
* expense: Valor da despesa
* installmentValue: Valor da parcela
* totalValue: Valor total
* classificationTable1InternalId: Identificador da Tabela de Classificação 1
* classificationTable1: Código da Tabela de Classificação 1
* classificationTable2InternalId: Identificador da Tabela de Classificação 2
* classificationTable2: Código da Tabela de Classificação 2
* classificationTable3InternalId: Identificador da Tabela de Classificação 3
* classificationTable3: Código da Tabela de Classificação 3
* classificationTable4InternalId: Identificador da Tabela de Classificação 4
* classificationTable4: Código da Tabela de Classificação 4
* classificationTable5InternalId: Identificador da Tabela de Classificação 5
* classificationTable5: Código da Tabela de Classificação 5
* optionalTable1InternalId: Identificador da Tabela de Faturamento 1
* optionalTable1: Código da Tabela de Faturamento 1
* optionalTable2InternalId: Identificador da Tabela de Faturamento 2
* optionalTable2: Código da Tabela de Faturamento 2
* optionalTable3InternalId: Identificador da Tabela de Faturamento 3
* optionalTable3: Código da Tabela de Faturamento 3
* optionalTable4InternalId: Identificador da Tabela de Faturamento 4
* optionalTable4: Código da Tabela de Faturamento 4
* optionalTable5InternalId: Identificador da Tabela de Faturamento 5
* optionalTable5: Código da Tabela de Faturamento 5
* financialBudgetaryNatureInternalId: Identificador da Natureza Orçamentária/Financeira
* financialBudgetaryNature: Natureza Orçamentária/Financeira
* financialBudgetaryNatureCompanyId: Identificador da Coligada da Natureza Orçamentária/Financeira
* immediateDueDate: Pagamento imediato da primeira parcela (sem a carencia do periodo)
* periodicity: Periodicidade
* dueDay: Dia do Vencimento
* installmentNumber: Número de Parcelas
* paymentConditionInternalId: Identificador da Condição de Pagamento
* paymentConditionCode: Código da Condição de Pagamento
* typeofMovementInternalId: Identificador do Tipo de Movimento
* typeofMovementCode: Código Tipo de Movimento
* freightType: Tipo de Frete
* branchInternalId: Identificador da Filial
* warehouseInternalID: Identificador do Local de Estoque
* warehouseCode: Código do Local de Estoque
* citiesInternalId: Identificado do Município e Estado
* cities: Código do Município
* codEtd: Código do Estado
* customerVendorInternalId: Identificador do Destinatário
* customerVendorCode: Código do Cli/for
* fiscalNatureInternalId: Identifcador da natureza fiscal do contrato
* fiscalNatureId: Identifcador da Natureza de Operação
* costCenterInternalId: Identifcador do centro de custo
* costCenterCode: Código do Centro de Custo
* departmentCodeInternalId: Identifcador do código do departamento
* departmentCode: Código do Departamento
* branchId: Identificador da Filial
* currencyIndex: Código do índice de Reajuste
* quoteDay: Dia da Cotação
* cashAccountInternalId: Identificador da Conta Caixa
* cashAccountCompanyId: Identifcador da coligada da Conta Caixa
* cashAccount: Código da Conta Caixa
* currency: Código da Moeda
* freeField1: Campo Livre 1
* freeField2: Campo Livre 2
* history: Histórico

## 9.3 - Parcela do Item

* companyId: Código da Coligada
* contractId: Identificador do contrato
* contractItemId: Identificador do item do contrato
* installmentNumber: Número da Parcela
* status: Código do Status
* descriptionStatus: Descrição do Status
* dueDate: Data de Vencimento
* valueInstallment: Valor da parcela
* presentValue: Valor Presente
* balanceDue: Saldo Devedor
* interestAmortization: Amortização do Juros
* installmentAmortization: Amortização da Parcela
* termClassification: Classificação Prazo
* reductionValue: Valor do Abatimento
* increaseValue: Valor do Acréscimo

## 9.4 - Rateio do Item

* companyId: Código da Coligada
* contractId: Identificador do contrato
* contractItemId: Identificador do item do contrato
* costCenterInternalId: Identificador do Centro de Custo
* costCenter: Centro de Custo
* description: Descrição
* percentage: Percentual
* value: Valor Referência
* history: Histórico
* itemValue: Valor do Item

## 9.5 Processos

Processos do Contrato

**Processo - Faturar Contrato**

* ProcessStartDate: Data Inicial
* ProcessEndDate: Data final
* CompleteInvoicing: Fatura Todo o Contrato
* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Cancela Faturamento Contrato**

* ProcessStartDate: Data Inicial
* ProcessEndDate: Data final
* CompleteCancelInvoicing: Cancela TodoFaturamento do Contrato
* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Gerar Previsão Financeira**

* ProcessStartDate: Data Inicial
* ProcessEndDate: Data final
* CodTdoInternalId: Tipo de Documento
* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Cancelar Previsão Financeira**

* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Alterar Status Contrato**

* StatusChangeDate: Data de alteração do status do contrato
* CodStatusContratoInternalId: Identificador do Novo status do contrato
* CodMotivoInternalId: Identificador do Motivo da mudança de status do contrato
* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo -** **Copiar Contrato**

* CompanyId: [ código da coligada ]
* BranchInternalId: Identificador da Coligada/Filial de destino da cópia do contrato
* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Reajustar Preço**

* ReadjustmentDate: Coligada/Filial de destino da cópia do contrato
* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Cancelar Reajuste Preço**

* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Reclassificar Contabilidade**

* MonthsAdded: Número de meses a incrementar
* LastDayInMonth: Utiliza o último dia do mês
* AccountingDate: Data de Contabilização
* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo - Cancelar Reclassificação Contábil**

* PrimaryKeyList: [ código da coligada, identificador do contrato ]

**Processo -** **Contabilizar Contrato**

* Operation: Operação
* PrimaryKeyList: [ código da coligada, identificador do contrato ]
Processos do Item do Contrato

**Processo - Gerar Aditivo**

* Type: Tipo do Aditivo
* AdditiveNumber: Número
* SignatureDate: Data Assinatura
* StartDate: Data Início Vigência
* AdditiveEffect: Efeito Aditivo
* AdditiveValue: Valor do Aditivo
* AdditivePercentage: Percentual do Aditivo
* AdditiveQuantity: Quantidade do Aditivo
* InstallmentsQuantity: Quantidade Parcelas
* InterestRate: Taxa Juros
* EditInstallmentValue: Definir valor para novas parcelas em itens periodicos
* NewInstallmentValue: Novo Valor Parcela
* Justification: Justificativa
* PrimaryKeyList: [ código da coligada, identificador do contrato, identificador do item do contrato ]

**Processo - Cancelar Aditivo**

* PrimaryKeyList: [ código da coligada, identificador do contrato, identificador do item do contrato ]

**Processo - Gerar Medição/Gerar Medição de Múltiplos Itens**

* NseqItem: NseqItem
* MeasurementType: Tipo da Medição
* MeasurementDate: Data Medição
* Quantity: Quantidade
* Value: Valor
* Justification: Justificativa
* CitiesInternalId: Identificador do Município
* StateInternalId: Identificador do Estado
* ServiceCode: Código do Serviço
* PrimaryKeyList: [ código da coligada, identificador do contrato, identificador do item do contrato ]

**Processo - Cancelar Medição**

* PrimaryKeyList: [ código da coligada, identificador do contrato, identificador do item do contrato ]

**Processo - Redistribuir Valor Parcela**

* NSeqItem: NSeqItem
* NSeqStartInstallment: NSeqItem Inicial Medição
* NSeqEndInstallment: NSeqItem Final Medição
* InstallmentValue: Valor Medição
* PrimaryKeyList: [ código da coligada, identificador do contrato, identificador do item do contrato ]
Processos da Parcela do Contrato

**Processo - Gerar Abatimento/Gerar Acréscimo**

* Operacao: Operação
* Valor: Valor por parcela
* Justificativa: Justificativa
* PrimaryKeyList: [ código da coligada, identificador do contrato, identificador do item do contrato, número da parcela ]
