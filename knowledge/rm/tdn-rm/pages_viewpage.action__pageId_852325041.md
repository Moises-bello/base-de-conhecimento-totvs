---
content_hash: a8690f6e4b5f3763c82fe5e234469ca99136a04464ad15e1f1c852525431295b
fetched_at: '2026-06-29T00:11:53.942235+00:00'
page_id: '852325041'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Relatório de Conferência de INSS Patronal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852325041
version: 8
---

Foi criada uma API para uso nos produtos de Folha de Pagamento das linhas RM, Datasul e Protheus, que será utilizada na nova tela em PO UI, "Relatório de Conferência de INSS Patronal".

Os campos a serem retornados pela API são os que estão definidos no protótipo e na documentação do relatório.

* <https://drive.google.com/u/0/open?id=1Z8ouqlED8zjYxxf7WhlzS9PLcn6ZovQUb7W8quf3bIU>
* <https://docs.google.com/document/d/1-Il0cshN3pxmjAdgu5IzjbJVNGdwIIV2lGql-_Gv2PY/edit>
* <https://docs.google.com/document/d/1NfO_TwKni1TxtI3KqeIpJQbu15EDny09VzK4avvPIAU/edit>

LoggerAPI Relatório API Relatório 

**1) API para chamar execução do relatório (****reportEsocialInssDctfWeb****)** **<http://localhost:8051/api/rh/esocial/v1/reportEsocialInssDctfWeb>**

**Parâmetros POST:**

|  |  |  |  |
| --- | --- | --- | --- |
| Identificador da empresa | (1-1) | companyId | string |
| Período folha (obrigatório)   * AAAAMM →  mensal * AAAA → anual | (1-1) | paymentPeriod | string |

**Exemplo do Json body:**

{

"companyId": 1,

     "paymentPeriod": "202002"

}

**Response:**

|  |  |  |
| --- | --- | --- |
| Id da requisição | requestId | string |

**Exemplo do Json response:**

{

"requestId": “106095|1”

}

API Percentual de CompletudeAPI Percentual de Completude

**2) API para consultar percentual de completude (****reportEsocialInssDctfWeb/Status****)**

**<http://localhost:8051/api/rh/esocial/v1/reportEsocialInssDctfWeb/Status>**

**Parâmetros GET:**

|  |  |  |  |
| --- | --- | --- | --- |
| Identificação da empresa | (1-1) | companyId | string |
| Id da requisição | (1-1) | requestId | string |

**Exemplo do queryParams:**

companyId=1&requestId=106095|1

**Response**:

|  |  |  |
| --- | --- | --- |
| Concluído | finished | boolean |
| Percentual de completude | percent | decimal |

**Exemplo do Json response:**

{

"finished":false,

"percent":0

}

API Valores CalculadosAPI Valores Calculados

**3) API para obter os valores calculados (****reportEsocialInssDctfWeb/InssValues****)**

[**http://localhost:8051/api/rh/esocial/v1/**](http://localhost:8051/api/rh/esocial/v1/reportEsocialBaseConfer/InssValues)**reportEsocialInssDctfWeb**[**/InssValues**](http://localhost:8051/api/rh/esocial/v1/reportEsocialBaseConfer/InssValues)

**Parâmetros GET:**

|  |  |  |  |
| --- | --- | --- | --- |
| Identificador da empresa | (1-1) | companyId | string |
| Período folha (obrigatório)   * AAAAMM →  mensal * AAAA → anual | (1-1) | paymentPeriod | string |
| Inscrição estabelecimento | (0-N) | registrationNumber | Array<string> |
| Somente divergências | (0-1) | differencesOnly | boolean (default: false) |

**Exemplo do query Params:**

companyId=1&paymentPeriod=202205&registrationNumber=07.577.599/0001-70,07.577.599/0002-50&differencesOnly=true

**Exemplo do Json response:**

{

    "hasNext": **false**,

    "items": [

        {

            "companyId": 1,

            "month": 1,

            "year": 2022,

            "period": 1,

            "totalEmployees": 3681.56,

            "totalCompany": 18383.02,

            "totalDeductions": 0.00,

            "totalInss": 22064.58,

            "totalEmployeesRet": 865.88,

            "totalCompanyRet": 2000.00,

            "totalDeductionsRet": 0.00,

            "totalInssRet": 3545.88,

            "establishments": [

                {

                    "registrationNumber": "07.577.599/0001-70",

                    "description": "RM Sistemas - Matriz 2",

                    "cnae": "4511104",

                    "aliquotRat": 2.0,

                    "aliquotRatAdjusted": 1.0000,

                    "fap": 0.5000,

                    "employerReplacement": **false**,

                    "cnaeRet": "4511104",

                    "aliquotRatRet": 2.0,

                    "aliquotRatAdjustedRet": 1.0000,

                    "fapRet": 0.5000,

                    "employerReplacementRet": **false**,

                    "establishmentValues": [

                        {

                            "code": "1138-01",

                            "payrollValue": 8282.74,

                            "retValue": 2000.00,

                            "divergent": **true**

                        },

                        {

                            "code": "1170-01",

                            "payrollValue": 60.05,

                            "retValue": 250.00,

                            "divergent": **true**

                        },

                        {

                            "code": "1176-01",

                            "payrollValue": 4.80,

                            "retValue": 20.00,

                            "divergent": **true**

                        },

                        {

                            "code": "1191-01",

                            "payrollValue": 24.02,

                            "retValue": 100.00,

                            "divergent": **true**

                        },

                        {

                            "code": "1196-01",

                            "payrollValue": 36.03,

                            "retValue": 150.00,

                            "divergent": **true**

                        },

                        {

                            "code": "1200-01",

                            "payrollValue": 14.41,

                            "retValue": 60.00,

                            "divergent": **true**

                        },

                        {

                            "code": "1646-01",

                            "payrollValue": 621.20,

                            "retValue": 100.00,

                            "divergent": **true**

                        }

                    ],

                    "lotations": [

                        {

                            "lotationCode": "Z101",

                            "description": "RM Sistemas - Matriz 2",

                            "fpas": "515",

                            "thirdCode": "0115",

                            "fpasRet": "",

                            "thirdCodeRet": "",

                            "lotationValues": [

                                {

                                    "category": 101,

                                    "valueGroup": "basesCp",

                                    "valueType": "vrBcCp00",

                                    "payrollValue": 41413.74,

                                    "retValue": 0.00,

                                    "divergent": **true**

                                }

                            ]

                        }

                    ]

                },

                {

                    "registrationNumber": "07.577.599/0002-50",

                    "description": "RM Sistemas - FRJ",

                    "cnae": "4522501",

                    "aliquotRat": 2.0,

                    "aliquotRatAdjusted": 2.0000,

                    "fap": 1.0000,

                    "employerReplacement": **false**,

                    "cnaeRet": "",

                    "aliquotRatRet": 0.0,

                    "aliquotRatAdjustedRet": 0.0000,

                    "fapRet": 0.0000,

                    "employerReplacementRet": **false**,

                    "establishmentValues": [

                        {

                            "code": "1138-01",

                            "payrollValue": 1091.44,

                            "retValue": 0.00,

                            "divergent": **true**

                        },

                        {

                            "code": "1646-01",

                            "payrollValue": 109.14,

                            "retValue": 0.00,

                            "divergent": **true**

                        }

                    ],

                    "lotations": [

                        {

                            "lotationCode": "Z102",

                            "description": "RM Sistemas - FRJ",

                            "fpas": "515",

                            "thirdCode": "0115",

                            "fpasRet": "",

                            "thirdCodeRet": "",

                            "lotationValues": [

                                {

                                    "category": 410,

                                    "valueGroup": "basesCp",

                                    "valueType": "vrBcCp00",

                                    "payrollValue": 5457.24,

                                    "retValue": 0.00,

                                    "divergent": **true**

                                }

                            ]

                        }

                    ]

                }

            ]

        }

    ]

}

API Estabelecimentos API Estabelecimentos 

**4) API para obter os estabelecimentos (EsocialEstablishment)**

Mesma api relatório de funcionários

DiagramaDiagrama

**Diagrama do json retorno:**
