---
content_hash: c2aa9af6a9685761d62e407fa6a23eb384a622dacbd99d5b20271394ba2466ed
fetched_at: '2026-06-29T00:12:08.339501+00:00'
page_id: '929944779'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Histórico Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929944779
version: 9
---

Foi criada a API para uso do produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Histórico Salarial", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Histórico Salarial que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Retorna Registros

**Endpoint:  /**/api/rh/v1/SalaryHistory **Método:** GET **Objetivo:**Retorna todos os Históricos Salariais

Inclusão de Registro

**Endpoint:  /**/api/rh/v1/SalaryHistory **Método:** POST **Objetivo:**Incluir registro no Histórico Salarial

Exemplo de Retorno

**Status Code: 201 Created**

{  
    "companyId": 1,  
    "employeeRegistration": "00001",  
    "changeDate": "2011-09-01T00:00:00-03:00",      
    "salaryNro": 1,  
    "processingDate": "2011-09-01T00:00:00-03:00",  
    "salary": 291.60,  
    "reasonChange": "08",  
    "changeJourney": 0,  
    "salaryHour": 0.0,  
    "percentageApplied": 0.0,  
    "includedDate": "2025-01-01T00:00:00-03:00",  
    "journey": "0",  
    "reference": "0",  
    "journeyChar": "000:00"  
}

Edição de Registro

**Endpoint:** /api/rh/v1/SalaryHistory/1|00001|1314846000|1 **CODCOLIGADA / CHAPA / DATA MUDANÇA/ NRO SALÁRIO**  
**Método:** PUT  
**Objetivo:**Alterar um registro já incluido anteriormente  
**Observação:** A data de mudança deve ser informada no formato de segundos\*

Exemplo de Retorno

**Status Code: 200  OK**

{  
    "companyId": 1,  
    "employeeRegistration": "00001",  
    "changeDate": "2011-09-01T00:00:00-03:00",      
    "salaryNro": 1,  
    "processingDate": "2011-09-01T00:00:00-03:00",  
    "salary": 291.60,  
    "reasonChange": "02",  
    "changeJourney": 0,  
    "salaryHour": 0.0,  
    "percentageApplied": - 0.0,  
    "includedDate": "2025-01-01T00:00:00-03:00",  
    "journey": "0",  
    "reference": "0",  
    "journeyChar": "000:00"  
}

Exclusão de Registro

**Endpoint:** /api/rh/v1/SalaryHistory/1|00001|1314846000|1 **CODCOLIGADA / CHAPA / DATA MUDANÇA/ NRO SALÁRIO**  
**Método:** DELETE  
**Objetivo:**Excluir um registro já incluído anteriormente  
**Observação:** A data de mudança deve ser informada no formato de segundos\*

Exemplo de Retorno

**Status Code: 204  No Content**

Postman collection Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
250

Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor.

Schema

**Endpoint:**  /api/rh/v1/SalaryHistory/Schema **Método:** GET **Objetivo:**Retornar o Schema neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

 "title": "Histórico Salarial",  
    "version": "1.0",  
    "identifier": "HistoricoSalarial",  
    "fields": [  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "companyId",  
            "label": "Coligada",  
            "disabled": true,  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 1,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 6,  
                    "order": 1,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 1,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "employeeRegistration",  
            "label": "Matrícula",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "order": 2,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "order": 2,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "order": 2,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "changeDate",  
            "label": "Data da Mudança",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "changeDatePK",  
            "label": "Data da Mudança",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 3,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "order": 3,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "salaryNro",  
            "label": "Nro. Salário",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "order": 9,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "visible": false,  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "order": 9,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "processingDate",  
            "label": "Data Processamento",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "maxLength": 6,  
            "layoutDefinition": [  
                {  
                    "order": 4,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 4,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "order": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "journeyChar",  
            "label": "Jornada",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 9999999,  
            "layoutDefinition": [  
                {  
                    "order": 5,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 5,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "order": 5,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "salary",  
            "label": "Salário",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 6,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 6,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "order": 6,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "eventId",  
            "label": "Código do evento",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "maxLength": 6,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 4,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "visible": false,  
                    "order": 7,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "visible": false,  
                    "order": 7,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "referenceChar",  
            "label": "Referência",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código",  
                    "property": "code"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Descrição",  
                    "property": "description"  
                }  
            ],  
            "required": true,  
            "searchService": "/api/rh/v1/readonly/lookups/generic/reasonChange",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "code",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "order": 7,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "order": 8,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "reasonChange",  
            "label": "Motivo da Mudança",  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 7,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "descriptionReason",  
            "label": "Desc. Motivo",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Cód da Tabela Salarial",  
                    "property": "code"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Tabela",  
                    "property": "description"  
                }  
            ],  
            "searchService": "/api/rh/v1/readonly/lookups/generic/salaryHistoryTable",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "code",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 7,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "order": 10,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "salaryHistoryTable",  
            "label": "Histórico Tabela Salarial",  
            "visible": false,  
            "componentType": "Lookup"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código identificador",  
                    "property": "code"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Faixa",  
                    "property": "description"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Percentual do Valor de Refrência",  
                    "property": "complementaryField"  
                }  
            ],  
            "searchService": "/api/rh/v1/readonly/lookups/generic/salaryRangeHistory",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "code",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 7,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "order": 11,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "salaryRangeHistory",  
            "label": "Histórico de Faixa",  
            "visible": false,  
            "componentType": "Lookup"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código identificador",  
                    "property": "code"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Nome do Nível",  
                    "property": "description"  
                }  
            ],  
            "searchService": "/api/rh/v1/readonly/lookups/generic/salaryLevelHistory",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "code",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 7,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "order": 12,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "salaryLevelHistory",  
            "label": "Histórico de Nível",  
            "visible": false,  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 15,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 2,  
                    "visible": false,  
                    "order": 12,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "changeJourney",  
            "label": "Alteração de Jornada",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 5,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "percentage",  
            "label": "% Variação Salarial",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 9999999,  
            "layoutDefinition": [  
                {  
                    "order": 6,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "salaryHour",  
            "label": "Salário Hora",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 7,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "percentageHour",  
            "label": "% Salário Hora",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 7,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "monthlyPercentage",  
            "label": "% Salário Mensal",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 11,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "percentageApplied",  
            "label": "% Aplicado",  
            "type": "number",  
            "componentType": "Number"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "order": 12,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "includedDate",  
            "label": "Data de Inlusão",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 14,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "journey",  
            "label": "Jornada",  
            "type": "number",  
            "componentType": "Number"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 14,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "reference",  
            "label": "Referência",  
            "type": "string",  
            "componentType": "Input"  
        }  
    ],  
    "groups": []  
}
