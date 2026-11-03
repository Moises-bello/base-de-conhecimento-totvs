---
content_hash: 553bd35aed9982d28d895cac60363e2164a96ca73ce620e7e675ae83f38a33e3
fetched_at: '2026-06-29T00:08:59.738064+00:00'
page_id: '364910976'
product: rm
source: tdn-rm
title: Provedor Integrado (Construção de APIs)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364910976
version: 94
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     O objetivo desse documento é especificar os serviços para criação de provedores integrados para dados relacionais.

Essa especificação deve ser utilizada como guia para o desenvolvimento de provedores integrados para dados relacionais do TReports.

Os endpoints expostos por esses serviços serão chamados automaticamente pela ferramenta TReports utilizando para isso o cadastro de provedores de dados localizado no front-end do TReports.

A documentação dos provedores de dados está disponível em :[Provedor de Dados](http://tdn.totvs.com/x/lyGTEg)

**Você pode encontrar um provedor integrado de exemplo com swagger em nosso repositório no Github:**

<https://github.com/totvs/treports-provider-sample>

O TReports segue o guia de implementação das API's da TOTVS, disponível no link: [Guia de implementacao das APIs TOTVS](http://tdn.totvs.com/x/nDUxE)

# Pré-requisitos:

---

1. Plataforma com suporte REST e autenticação Basic.
2. Suporte a tratamento cross-domain, por conta das requisições de serviços em servidores de domínio diferente.
3. Modelo de implementação de acordo com o documento "Guia de implementação de API" disponível no link: <http://tdn.totvs.com/pages/viewpage.action?pageId=274849083>

# Definições gerais:

---

      O retorno dos serviços REST dos endpoints descritos abaixo devem estar encapsulados dentro de um objeto JSON com a seguinte especificação

Mensagens de erro (códigos HTTP 4xx e 5xx retornados no cabeçalho da resposta)

1. 1. Devem-se retornar os campos a seguir:

      |  |
      | --- |
      | `{     code: "",     message: "", }`  **Exemplo:**  `POST http://totvs.com.br/api/trep/v1/dbdataproviders/testeconnection`  `{` `code:` `""``,` `message:` `"Erro ao testar conexão com o banco de dados"``,` `detailedMessage:` `"Banco de dados oracle não disponível"` `}` |

      **Mensagens de sucesso** (código http **2xx retornados no cabeçalho da resposta**)

      Devem-se retornar diretamente a entidade que representa o objeto resultado da operação do *endpoint*.

      |  |
      | --- |
      | `Exemplo:`  `POST http:``//totvs.com.br/api/trep/v1/dbdataproviders/testeconnection`  `{` `testConnection``:` `"true"`  `}` |
   2. Todas as linhas de produto devem estabelecer uma URL base, a partir da qual os serviços REST de provedor integrado serão disponibilizados.
   3. Como exemplo, no ERP RM foi definida a seguinte  URL base:   
      **/api/trep/v1/dbdataproviders/**

Essa Url base deve ser informada no cadastro de provedores de dados localizado no front-end do TReports no campo "Rota" conforme figura abaixo:

Com o objetivo de facilitar o entendimento do documento, a URL base do RM descrita acima será utilizada no restante do documento para melhor localização dos endpoints.

# Definição dos serviços:

---

      Segue abaixo os serviços REST que precisam ser implementados:

* Serviço de leitura de parâmetros gerais;
* Serviço de teste de conexão;
* Serviço de teste de sentenças sql;
* Serviço de leitura de schema de tabelas físicas;
* Serviço de leitura de schema de sentença sql;
* Serviço de leitura de relacionamentos entre tabelas físicas;
* Serviço de pesquisa de tabelas;
* Serviço de leitura de dados;

Na descrição de cada serviço podemos encontrar os seguintes elementos:

* Definição da URL do serviço;
* Descrição do serviço com detalhes relativos ao seu funcionamento;
* Detalhamento dos parâmetros de entrada (request) e saída (response);

## **a) Serviço de leitura de parâmetros de provedor:**

*GET /api/trep/v1/dbdataproviders/parameters*

1544618824145\_9340548891538500986708\_-44195125

|  |  |
| --- | --- |
| Recebe | Não recebe parâmetros |
| Retorna | Application/JSON |

Esse método é utilizado para obtenção dos parâmetros do provedor integrado. A necessidade e definição desses parâmetros é de responsabilidade do dono do provedor.

No JSON de retorno, deve constar as seguintes informações:

* **name:** Nome do parâmetro;
* **description:** Descrição do parâmetro;
* **value:** Valor do parâmetro;
* **isPassword:** Define se o valor do parâmetro será gravado e mostrado de forma criptografada. Pode ser true ou false

  Exemplo de json de retorno

  {

         "providerParams" : [{

               "name" : "aliasName",

               "description" : "Nome do alias do RM",

               "value" : "CorporeRM",

               "isPassword" : false

         }]

  }

Os parâmetros retornados por esse serviço aparecerão na grid de parâmetros localizada no "cadastro de provedores de dados" do front-end do TReports, conforme abaixo:

## **b) Serviço de teste de conexão do provedor:**

POST /api/trep/v1/dbdataproviders/testconnection

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para testar a conexão de um provedor integrado.

No Json de entrada devem ser enviados os parâmetros cadastrados na tela de "Provedores de dados". Esses parâmetros são os mesmos recuperados pelo serviço definido acima "**GET /api/trep/v1/dbdataproviders/parameters**".

Exemplo de json de retorno

{

       "providerParams" : [{

             "name" : "aliasName",

             "description" : "Nome do alias do RM",

             "value" : "CorporeRM",

             "isPassword" : false

       }]

}

 No JSON de retorno, deve constar as seguintes informações:

**testSuccess:**Informa se o teste no provedor foi bem sucedido ou não. Pode ser true ou false

Exemplo de json de retorno

{

       “testSuccess” : true;

}

Esse método é utilizado no click do botão "Testar conexão" localizado no "cadastro de provedores de dados" do front-end do TReports, conforme abaixo:

## **c) Serviço de teste de sentenças sql:**

POST /api/trep/v1/dbdataproviders/testquery

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para testar a sintaxe de uma sentença sql.

No Json de entrada devem ser enviadas os seguintes informações:

* + **providerParams:**Parâmetros do provedor de dados.
  + **sqlText:** Texto da sentença sql;
  + **sqlParameters:** Parâmetros da sentença sql;
    - **paramName**: Nome do parâmetro da sentença sql;
    - **paramValue**: Valor do parâmetro da sentença sql;
    - **paramType**: Tipo do parâmetro;

Exemplo de json de entrada

{

  "providerParams" : [{

             "name" : "aliasName",

             "description" : "Nome do alias do RM",

             "value" : "CorporeRM",

             "isPassword" : false

       }],

            "sqlText": "select \* from pfunc where codcoligada = :codcol",

            "sqlParameters": [{

                        "paramName": "codcol",

                        "paramValue": "1",

                        "paramType": "system.Int32"

            }]

}

No JSON de retorno, deve constar as seguintes informações:

**testSuccess:**Informa se o teste foi bem sucedido ou não. Pode ser true ou false

Exemplo de json de retorno

{

       “testSuccess” : true;

}

## **d) Serviço de leitura de schema de tabelas físicas:**

POST /api/trep/v1/dbdataproviders/schema/table

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para retornar o schema (estrutura) de uma tabela ou view localizada fisicamente em um determinado banco de dados.

No Json de entrada devem ser enviadas os seguintes informações:

* **providerParams:**Parâmetros do provedor de dados.
* **tableSourceName:** Nome da tabela ou view do banco de dados;

Exemplo de json de entrada

{

"providerParams" : [{

             "name" : "aliasName",

             "description" : "Nome do alias do RM",

             "value" : "CorporeRM",

             "isPassword" : false

       }],

            "tableSourceName": "PFUNC",

}

No JSON de retorno, deve constar as seguintes informações:

**schemaTable**: Objeto contendo as seguinte informações:

* **tableSourceName**: Nome da tabela de banco de dados;
* **tableSourceDescription**: Descrição da tabela de banco de dados. Essa informação pode ser recuperada de um dicionário de dados.
* **columns**: lista contendo as seguinte informações:
  + **columnName**: Nome da coluna;
  + **columnDescription**: Descrição da coluna da tabela. Essa informação pode ser recuperada de um dicionário de dados.;
  + **columnType**: tipo da coluna;

Obs: segue abaixo uma tabela definindo o mapeamento correto dos tipos das colunas. O nome do tipo definido na coluna "Tipo do TReports" deve ser retornado na propriedade "columnType" do objeto de retorno.



| Definição do tipo | Tipo do TReports | Tipo da framework .Net |
| --- | --- | --- |
| Sequência de caracteres | String | System.string |
| Data | DateTime | System.DateTime |
| Representa um número de 64-bit de precisão dupla com valores que variam do negativo 1.79769313486232e308 ao positivo 1.79769313486232e308, bem como zero positivo ou negativo | Double | System.Double |
| Representa um número de 32 bits de precisão simples com valores que variam do negativo 3.402823e38 ao positivo 3.402823e38, bem como zero positivo ou negativo | Float | System.Single |
| Representa um número de com valroes que variam entre 79,228,162,514,264,337,593,543,950,335 ao positivo 79,228,162,514,264,337,593,543,950,335. É apropriado para cálculos financeiros que requere um grande número de dígitos e frações sem falhas em arrendondamentos. | Decimal | System.Decimal |
| Representa inteiros com sinal com valores que variam de 32768 negativo a 32767 positivo. | Integer16 | System.Int16 |
| Representa inteiros com sinal com valores que variam de 2.147.483.648 negativo ao  2.147.483.647 positivo | Integer32 | System.Int32 |
| Representa inteiros com sinal com valores que variam de negativo 9,223,372,036,854,775,808 ao positivo 9,223,372,036,854,775,807 | Integer64 | System.Int64 |
| Representa os valores "true" ou "false" | Boolean | System.Boolean |
| Array de bytes. Geralmente usado para representação de uma imagem. | Bytes | System.Byte[] |

Exemplo de json de retorno

{  
 "schemaTable": {  
 "tableSourceName": "PFUNC",  
 "tableSourceDescription": "Funcionários",  
 "columns": [  
 {  
 "columnName": "CODCOLIGADA",  
 "columnDescription": "Codigo da coligada",  
 "columnType": "Integer32"  
 },  
 {  
 "columnName": "CHAPA",  
 "columnDescription": "Chapa do funcionario",  
 "columnType": "String"  
 },  
 {  
 "columnName": "SALARIO",  
 "columnDescription": "Salario do funcionário",  
 "columnType": "Double"  
 } ]  
},  
   
 }

Esse método é utilizado na tela de cadastro de entidade do tront-end do TReports, ao escolher uma fonte de dados ligada a uma tabela física:

## **e) Serviço de leitura de schema de sentenças sql:**

POST /api/trep/v1/dbdataproviders/schema/sql

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para retornar o schema (estrutura) de uma sentença sql disparada em um determinado provedor de dados.

No Json de entrada devem ser enviadas os seguintes informações:

* **providerParams:**Parâmetros do provedor de dados.
* **sqlText:** Sentença sql cadastrada na fonte de dados do relatório;
* **sqlParameters:**Lista de objeto contendo informações dos parâmetros da sentença sql:

  + **paramName**: Nome do parâmetro da sentença sql;
  + **paramValue:** Valor do parâmetro da sentença sql;
  + **paramType**: Tipo do parâmetro;

Exemplo de json de entrada

{

"providerParams" : [{

             "name" : "aliasName",

             "description" : "Nome do alias do RM",

             "value" : "CorporeRM",

             "isPassword" : false

       }],

            "sqlText": "select \* from pfunc where codcoligada = :codcol",

            "sqlParameters": [{

                        "paramName": "codcol",

                        "paramValue": "1",

                        "paramType": "system.Int32"

            }]

}

No JSON de retorno, deve constar as seguintes informações:

* **schemaSql**: objeto contendo as seguinte informações:

  + **columns**: lista contendo as seguinte informações:
    - **columnName**: Nome da coluna;
    - **columnType**: tipo da coluna;

  Obs: segue abaixo uma tabela definindo o mapeamento correto dos tipos das colunas. O nome do tipo definido na coluna "Tipo do TReports" deve ser retornado na propriedade "columnType" do objeto de retorno.

  | Definição do tipo | Tipo do TReports | Tipo da framework .Net |
  | --- | --- | --- |
  | Sequência de caracteres | String | System.string |
  | Data | DateTime | System.DateTime |
  | Representa um número de 64-bit de precisão dupla com valores que variam do negativo 1.79769313486232e308 ao positivo 1.79769313486232e308, bem como zero positivo ou negativo | Double | System.Double |
  | Representa um número de 32 bits de precisão simples com valores que variam do negativo 3.402823e38 ao positivo 3.402823e38, bem como zero positivo ou negativo | Float | System.Single |
  | Representa um número de com valroes que variam entre 79,228,162,514,264,337,593,543,950,335 ao positivo 79,228,162,514,264,337,593,543,950,335. É apropriado para cálculos financeiros que requere um grande número de dígitos e frações sem falhas em arrendondamentos. | Decimal | System.Decimal |
  | Representa inteiros com sinal com valores que variam de 32768 negativo a 32767 positivo. | Integer16 | System.Int16 |
  | Representa inteiros com sinal com valores que variam de 2.147.483.648 negativo ao  2.147.483.647 positivo | Integer32 | System.Int32 |
  | Representa inteiros com sinal com valores que variam de negativo 9,223,372,036,854,775,808 ao positivo 9,223,372,036,854,775,807 | Integer64 | System.Int64 |
  | Representa os valores "true" ou "false" | Boolean | System.Boolean |
  | Array de bytes. Geralmente usado para representação de uma imagem. | Bytes | System.Byte[] |

Exemplo de json de retorno

{

            “schemaSql” : {

                        "columns": [ {"columnName": "CODCOLIGADA", "columnType": "Integer32"},

                                                 {"columnName": "CHAPA", "columnType": "String"},

                                                 {"columnName": "SALARIO", "columnType": "Double"}]

            }

}

Esse método é utilizado na tela de cadastro de entidade do tront-end do TReports, ao escolher uma fonte de dados ligada a uma sentença sql:

## **f) Serviço de leitura de relacionamentos entre tabelas físicas:**

POST /api/trep/v1/dbdataproviders/relations

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para retornar os relacionamentos existentes entre duas tabelas físicas.

No Json de entrada devem ser enviadas os seguintes informações:

* **parentTableName:** Nome da tabela pai no relacionamento.
* **childTableName:** Nome da tabela filha no relacionamento;

Exemplo de json de entrada

{

"providerParams" : [{

             "name" : "aliasName",

             "description" : "Nome do alias do RM",

             "value" : "CorporeRM",

             "isPassword" : false

       }],

        "parentTableName": "PFUNC",

        "childTableName": "PFDEPEND"

}

No JSON de retorno, deve constar as seguintes informações:

**relations**: lista contendo as seguinte propriedades:

* **relationName**: Nome do relacionamento;
* **parentTableName**: Nome da tabela pai no relacionamento.
* **childTableName**: Nome da tabela filha no relacionamento:
* **parentColumns:** Lista contendo as colunas pai no relacionamento
  + ****columnName**:** Nome da tabela pai no relacionamento;
* **childColumns:**Lista contendo as colunas filha no relacionamento
  + **columnName**: Nome da coluna filha no relacionamento;

Exemplo de json de retorno

{  
 "relations":[  
 {  
 "relationName": "",  
 "parentTableName": "PFUNC",  
 "childTableName": "PPESSOA",  
 "parentColumns": [  
 {  
 "columnName": "CODCOLIGADA",  
 },  
 {  
 "columnName": "CODPESSO",  
 }  
 ],  
 "childColumns": [  
 {  
 "columnName": "CODCOLIGADA",  
 },  
 {  
 "columnName": "CODIGO",  
 }  
 ],  
 }]  
}

Esse método é utilizado na tela de cadastro de relacionamento do tront-end do TReports, ao escolher uma tabela filha ou pai.

## **g) Serviço de pesquisa de tabelas:**

POST /api/trep/v1/dbdataproviders/search/tables

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para retornar as tabelas pesquisadas em um determinado provedor de dados.

No Json de entrada devem ser enviadas os seguintes informações:

* **findTable:**Nome completo da tabela ou início do nome da tabela.
* **page:** Número da página a ser retornada;
* **pageSize:** Tamanho da página a ser retornada;

Exemplo de json de entrada

{

"providerParams" : [{

             "name" : "aliasName",

             "description" : "Nome do alias do RM",

             "value" : "CorporeRM",

             "isPassword" : false

       }],

        "findTable": "PF",

        "page": 1,

"pageSize": 10

}

No JSON de retorno, deve constar as seguintes informações:

**hasNext:**Informa se existem mais registro para serem recuperados na paginação;

**searchTables**: lista contendo os nomes e descrição das tabelas recuperadas:

* **tableSourceName**: Nome da tabela;
* **tableSourceDescription**: Descrição da tabela.

Exemplo de json de retorno

{

"hasNext": "false",  
 "searchTables":[  
 {

"tableSourceName": "PFUNC",  
 "tableSourceDescription": "Funcionários"

},

{

"tableSourceName": "PFDEPEND",  
 "tableSourceDescription": "Dependentes"

}

]

Esse método é utilizado na tela de cadastro de fonte de dados. Aparecerá um lookup de pesquisa nessa tela se a fonte de dados estiver ligada a um provedor de dados integrado. Caso seja uma fonte de dados ligada a um provedor de banco de dados relacional, o usuário informará o nome da tabela manualmente.

## **h) Serviço de leitura de dados:**

POST /api/trep/v1/dbdataproviders/data

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para retornar os dados do relatórios.

No Json de entrada devem ser enviadas as seguintes informações:

* **providerParams:**Parâmetros do provedor de dados.
* **sentenceMember:** Objeto contendo as seguinte informações:

* + **entityName**: Nome da entidade cadastrada no TReports que receberá os dados.
  + **sqlText:** sentença sql a ser disparada no banco de dados;
  + **sqlParameters:**Lista de objeto contendo informações dos parâmetros da sentença sql:

    - **paramName**: Nome do parâmetro da sentença sql;
    - **paramValue:** Valor do parâmetro da sentença sql;
    - **paramType**: Tipo do parâmetro;

* **maxRecords:** número máximo de registros a serem retornados. Se o valor for < 0 (default), serão retornados todos os registros.

Exemplo de json de entrada

{

"providerParams" : [{

             "name" : "aliasName",

             "description" : "Nome do alias do RM",

             "value" : "CorporeRM",

             "isPassword" : false

       }],

            "sentenceMember": {

                        "entityName": "Funcionarios",

                        "sqlText": "select \* from pfunc where codcoligada = :codcol",

                        "sqlParameters": [{

                                    "paramName": "codcol",

                                    "paramValue": "1",

                                    "paramType": "system.Int32"

                        }],

                        "maxRecords": 10

}

}

No JSON de retorno, deve constar as seguintes informações:

* + - **data**: Dados recuperadas no banco de dados através da execução da sentença sql enviada no objeto de request:
    - **dataContentType**: Deve ser informado o MIME correspondente ao tipo de dado informado na propriedade "Data". Caso não seja informado, o valor default é : application/json.   
      Atualmente o TReports oferece suporte para os seguintes tipos de MIME:
      * application/json - Formato JSON;
      * application/xml - Formato XML;

Exemplo de json de retorno

{

              "data": "xml ou json contendo o resultado da execução da sentença sql",

"dataContentType": "application/json"

}

Obs: No exemplo abaixo, os dados estão sendo retornados no formato json. Perceba que os dados devem ser retornados em uma string entre aspas duplas.

Exemplo de retorno de Json

{"data":"[{\"Id\":1,\"Code\":\"1\",\"CompanyId\":1},{\"Id\":2,\"Code\":\"01.01\",\"CompanyId\":1},{\"Id\":3,\"Code\":\"2\",\"CompanyId\":1},{\"Id\":4,\"Code\":\"02.01\",\"CompanyId\":1},{\"Id\":5,\"Code\":\"01.02\",\"CompanyId\":1},{\"Id\":6,\"Code\":\"01.03\",\"CompanyId\":1}]"}

## **i) Serviço de leitura de****possíveis****caminhos entre tabelas físicas:**

POST /api/trep/v1/dbdataproviders/paths

|  |  |
| --- | --- |
| Recebe | Application/JSON |
| Retorna | Application/JSON |

Esse método é utilizado para retornar os possíveis caminhos entre duas tabelas físicas.

No Json de entrada devem ser enviadas as seguintes informações:

* **tableName**: Nome da tabela principal.
* **targetTableName**: Nome da tabela que se deseja alcançar.

Exemplo de json de entrada

{

"providerParams" : [{

"name" : "aliasName",

"description" : "Nome do alias do RM",

"value" : "CorporeRM",

"isPassword" : false

}],

"tableName": "PFUNC",

"targetTableName": "PFDEPEND"

}

}

No JSON de retorno, deve constar as seguintes informações:

**paths**: lista contendo as seguinte propriedades:

* **pathName**: Nome do caminho.
* **parentTableName**: Nome da tabela pai.
* **childTableName**: Nome da tabela filha.
* **parentColumns:**Lista contendo as colunas da tabela pai.
  + ****columnName**:** Nome da coluna da tabela pai que se relaciona com a tabela filha.
* **childColumns:**Lista contendo as colunas da tabela filha.
  + **columnName**: Nome da coluna da tabela filha que se relaciona com a tabela pai.
* **childPaths**: Caminho para "chegar" até uma tabela. Usado somente quando não existe uma ligação direta entre duas tabelas. Conforme exemplo abaixo, não existe uma ligação direta entre as tabelas "PFunc" e "GUsuario". Sendo assim, foi criado um caminho passando pela tabela "PPessoa".

Exemplo de json de retorno

{  
"paths":[  
{  
"pathName": "",  
"parentTableName": "PFUNC",  
"childTableName": "PPESSOA",  
"parentColumns": [  
{  
"columnName": "CODCOLIGADA",  
},  
{  
"columnName": "CODPESSO",  
}  
],  
"childColumns": [  
{  
"columnName": "CODCOLIGADA",  
},  
{  
"columnName": "CODIGO",  
}  
],  
"childPaths": [  
{  
"pathName": "",  
"parentTableName": "PPESSOA",  
"childTableName": "GUSUARIO",  
"parentColumns": [  
{  
"columnName": "CODUSUARIO",  
}  
],  
"childColumns": [  
{  
"columnName": "CODUSUARIO",  
}  
],  
"childPaths": {}   
}  
]   
}]  
}

Esse método é utilizado na tela de criação de caminhos no cadastro de "campos virtuais relacionais".

# Exemplo de integração:

---

      Um código exemplo demonstrando um provedor trabalhando com json e xml está disponível em [treports-provider-sample](https://github.com/totvs/treports-provider-sample).

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Provedor Integrado

**Exemplo:** <https://github.com/totvs/treports-provider-sample>

falsefalse

**Status:** Finalizado

false

**Data:** 08/12/2017

false

**Autores:**
