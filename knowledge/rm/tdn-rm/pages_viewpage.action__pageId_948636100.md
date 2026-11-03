---
content_hash: e1d4abefca1ad64ca5c5502dab822e7030d4d858faa258e7db27f54b45dc977a
fetched_at: '2026-06-29T00:12:09.643730+00:00'
page_id: '948636100'
product: rm
source: tdn-rm
title: Documentação Técnica - Remuneração de Trabalhadores Avulsos não Portuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=948636100
version: 1
---

Foi criada a API para uso do produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Remuneração de Trabalhadores Avulsos não Portuário", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Remuneração de Trabalhadores Avulsos não Portuário que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Retorna Registros

**Endpoint:  /**/api/rh/v1/EsocialRemunerationWorkingNonPort **Método:** GET **Objetivo:** Retornar todos os registros de Remuneração de Trabalhadores Avulsos Não Portuários.

Inclusão de Registro

**Endpoint:  /**/api/rh/v1/EsocialRemunerationWorkingNonPort **Método:** POST **Objetivo:** Incluir novo registro deRemuneração de Trabalhador Avulso Não Portuário.

Exemplo de Retorno

**Status Code: 201 Created**

   {  
            "companyId": 1,  
            "identifier": 1,  
            "monthComp": 12,  
            "yearComp": 2025,  
            "indApuracao": 1,  
            "sectionCode": "01",  
            "locationCodeSection": "01",  
            "locationCode": "01",  
            "vrbCcp00": 0.00,  
            "vrbCcp15": 0.00,  
            "vrbCcp20": 0.00,  
            "vrdEscCp": 0.00,  
            "vrbCcp25": 0.00,  
            "vrbCcp13": 0.00,  
            "vrbFgts": 0.00,  
            "useTaker": false  
        }

Edição de Registro

**Endpoint:** /api/rh/v1/EsocialRemunerationWorkingNonPort/1|1 **CODCOLIGADA / IDENTIFICADOR**  
**Método:** PUT  
**Objetivo:**Alterar um registro já incluído anteriormente

Exemplo de Retorno

**Status Code: 200  OK**

  {  
            "companyId": 1,  
            "identifier": 1,  
            "monthComp": 12,  
            "yearComp": 2025,  
            "indApuracao": 1,  
            "sectionCode": "01",  
            "locationCodeSection": "01",  
            "locationCode": "01",  
            "vrbCcp00": 1.00,  
            "vrbCcp15": 1.00,  
            "vrbCcp20": 1.00,  
            "vrdEscCp": 1.00,  
            "vrbCcp25": 1.00,  
            "vrbCcp13": 1.00,  
            "vrbFgts": 1.00,  
            "useTaker": false  
        }

Exclusão de Registro

**Endpoint:** /api/rh/v1/EsocialRemunerationWorkingNonPort/1|1 **CODCOLIGADA / IDENTIFICADOR**  
**Método:** DELETE  
**Objetivo:**Excluir um registro já incluído anteriormente

Exemplo de Retorno

**Status Code: 204  No Content**

Postman collection Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
  
250

Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor.

Schema

**Endpoint:**  /api/rh/v1/EsocialRemunerationWorkingNonPort/Schema **Método:** GET **Objetivo:**Retornar o Schema neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

"title": "Remuneração de Trabalhadores Avulsos não Portuários",  
    "version": "1.0",  
    "identifier": "EsocialRemunTrabNaoPortuario",  
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
                    "gridColumns": 2,  
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
            "property": "identifier",  
            "label": "Identificador",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 2,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 2,  
                    "order": 2,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 2,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "monthComp",  
            "label": "Mês",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 3,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 2,  
                    "order": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 3,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "yearComp",  
            "label": "Ano",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "options": [  
                {  
                    "value": 1,  
                    "label": "Mensal"  
                },  
                {  
                    "value": 2,  
                    "label": "13° Salário"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 6,  
                    "order": 4,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "radioGroup",  
            "property": "indApuracao",  
            "label": "Indicativo de Período de Apuração",  
            "componentType": "RadioGroup"  
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
            "searchService": "/api/rh/v1/readonly/lookups/generic/section",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "description",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "order": 4,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "divider": "Identificação do Estabelecimento (S-1005)",  
                    "order": 5,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 5,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "sectionCode",  
            "label": "Cód. Seção",  
            "componentType": "Lookup"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Cliente/Fornecedor",  
                    "property": "code"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Nome Fantasia/Social",  
                    "property": "description"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Nome",  
                    "property": "name"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "CPF/CNPJ",  
                    "property": "cpfCnpj"  
                }  
            ],  
            "searchService": "/api/rh/v1/readonly/lookups/generic/taker",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "description",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "order": 5,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "order": 6,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 13,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "takerCode",  
            "label": "Cód. Tomador",  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
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
            "property": "takerCompanyId",  
            "label": "Coligada Tomador",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "CEI",  
                    "property": "complementaryField"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Descrição",  
                    "property": "description"  
                }  
            ],  
            "searchService": "/api/rh/v1/readonly/lookups/generic/cei",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "description",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "order": 6,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 3,  
                    "order": 7,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 14,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "ceiCode",  
            "label": "CEI",  
            "componentType": "Lookup"  
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
            "searchService": "/api/rh/v1/readonly/lookups/generic/locationCodeSection",  
            "format": [  
                "code",  
                "description"  
            ],  
            "fieldLabel": "description",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 3,  
                    "divider": "Identificação de Lotação Tributária (S-1020)",  
                    "order": 8,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "locationCodeSection",  
            "label": "Seção",  
            "componentType": "Lookup"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código da Lotação",  
                    "property": "code"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Seção",  
                    "property": "sectionCode"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Nome da Seção",  
                    "property": "sectionName"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Código do Tomador",  
                    "property": "contractorCode"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Nome do Tomador",  
                    "property": "contractorName"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Cei",  
                    "property": "ceiRegistration"  
                }  
            ],  
            "searchService": "/api/rh/v1/readonly/lookups/generic/locationCode",  
            "format": [  
                "code",  
                "code"  
            ],  
            "fieldLabel": "description",  
            "fieldValue": "code",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 3,  
                    "divider": "Identificação de Lotação Tributária (S-1020)",  
                    "order": 8,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "locationCode",  
            "label": "Lotação Tributária",  
            "componentType": "Lookup"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 99999999,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "divider": "Remuneração dos Trabalhadores Avulsos não Portuários",  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 6,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "vrbCcp00",  
            "label": "Contribuição Previdenciária:",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 99999999,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 7,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "vrbCcp15",  
            "label": "Contribuição Previdenciária 13°:",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 99999999,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 8,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "vrbCcp20",  
            "label": "FGTS:",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 99999999,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "divider": " ",  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 9,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "vrdEscCp",  
            "label": "Valor Total da Contribuição Descontada:",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 99999999,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 10,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "vrbCcp25",  
            "label": "Aposentadoria Especial Após 15 Anos:",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 99999999,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 11,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "vrbCcp13",  
            "label": "Aposentadoria Especial Após 20 Anos:",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 99999999,  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "order": 1,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "order": 12,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "vrbFgts",  
            "label": "Aposentadoria Especial Após 25 Anos:",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
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
            "property": "useTaker",  
            "label": "Usa Tomador",  
            "visible": false,  
            "type": "boolean",  
            "componentType": "Switch"  
        }  
    ],  
    "groups": []  
}
