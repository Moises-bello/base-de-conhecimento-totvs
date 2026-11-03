---
content_hash: d93858ac811af2f854da991e09a4a049b10c108f38c4f621f6f44ee8f6db1f87
fetched_at: '2026-06-29T00:12:09.278035+00:00'
page_id: '943120772'
product: rm
source: tdn-rm
title: Documentação Técnica - Período de Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=943120772
version: 4
---

Foi criada a API para uso do produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Período de Apuração", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Período de Apuração que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Retorna Registros

**Endpoint:  /**/api/rh/v1/EsocialMonthlySheet **Método:** GET **Objetivo:**Retorna todos os Períodos de Apurações

Inclusão de Registro

**Endpoint:  /**/api/rh/v1/EsocialMonthlySheet **Método:** POST **Objetivo:**Incluir registro no Período de Apuração

Exemplo de Retorno

**Status Code: 201 Created**

{  
            "companyId": 1,  
            "monthComp": 9,  
            "yearComp": 2015,  
            "indPeriod": 1,  
            "generateTaker": 0,  
            "law11774ReductionPercentage": 0.00,  
            "employerSubsidyIndicator": 0,  
            "employerContributionPercentage": 0.00,  
            "monthlyFactor": 0.00,  
            "thirteenthMonthFactor": 0.00,  
            "compWithoutMovement": 0,  
            "ruralProductionAcquisitionIndicator": 0,  
            "excludeRuralProductionAcquisitionInfo": 0,  
            "immediateDctfWebTransmission": 0,  
            "finalProfitSocialContributionPercentage": 0,  
            "indicativeDoesNotValidateClosing": 0,  
            "retentionValue": 0.00  
}

Edição de Registro

**Endpoint:** /api/rh/v1/EsocialMonthlySheet/1|1|2015|9 **CODCOLIGADA / INDICATIVO DE PERIODO DE APURACAO** **/  ANO / MES**  
**Método:** PUT  
**Objetivo:**Alterar um registro já incluido anteriormente

Exemplo de Retorno

**Status Code: 200  OK**

{  
            "companyId": 1,  
            "monthComp": 10,  
            "yearComp": 2015,  
            "indPeriod": 1,  
            "generateTaker": 0,  
            "law11774ReductionPercentage": 0.00,  
            "employerSubsidyIndicator": 0,  
            "employerContributionPercentage": 0.00,  
            "monthlyFactor": 0.00,  
            "thirteenthMonthFactor": 0.00,  
            "compWithoutMovement": 0,  
            "ruralProductionAcquisitionIndicator": 0,  
            "excludeRuralProductionAcquisitionInfo": 0,  
            "immediateDctfWebTransmission": 0,  
            "finalProfitSocialContributionPercentage": 0,  
            "indicativeDoesNotValidateClosing": 0,  
            "retentionValue": 0.00  
}

Exclusão de Registro

**Endpoint:** /api/rh/v1/EsocialMonthlySheet/1|1|2015|9  **CODCOLIGADA / INDICATIVO DE PERIODO DE APURACAO** **/  ANO / MES**  
**Método:** DELETE  
**Objetivo:**Excluir um registro já incluído anteriormente

Exemplo de Retorno

**Status Code: 204  No Content**

Postman collection Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
250  
  

Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor.

Schema

**Endpoint:**  /api/rh/v1/EsocialMonthlySheet/Schema **Método:** GET **Objetivo:**Retornar o Schema neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Esocial Folha Mensal",  
    "version": "1.0",  
    "identifier": "EsocialFolhaMensal",  
    "fields": [  
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
            "key": true,  
            "property": "companyId",  
            "label": "Coligada",  
            "disabled": true,  
            "visible": false,  
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
                    "gridColumns": 2,  
                    "visible": false,  
                    "order": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "radioGroup",  
            "key": true,  
            "property": "indApuracao",  
            "label": "Indicativo de Período de Apuração",  
            "componentType": "RadioGroup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 4,  
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
            "property": "indApuracaoDescription",  
            "label": "Indicativo de Período de Apuração",  
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
                    "gridColumns": 1,  
                    "order": 2,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 2,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "yearComp",  
            "label": "Ano",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "maxValue": "12",  
            "minValue": "1",  
            "layoutDefinition": [  
                {  
                    "order": 1,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 1,  
                    "order": 1,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 1,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "monthComp",  
            "label": "Mês",  
            "type": "number",  
            "componentType": "Number"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "order": 3,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "divider": "Informações de Identificação",  
                    "order": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 3,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "compWithoutMovement",  
            "label": "Sem Movimento",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "options": [  
                {  
                    "value": 0,  
                    "label": "ㅤ"  
                },  
                {  
                    "value": 1,  
                    "label": "Contrib. Patronal Integralmente Substituída"  
                },  
                {  
                    "value": 2,  
                    "label": "Contribuição Patronal Parcialmente Substituída"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 3,  
                    "divider": "Informações Substituição Patronal",  
                    "order": 5,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "employerSubsidyIndicator",  
            "label": "Indicativo de Substituição",  
            "componentType": "Select"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "disabled": true,  
                    "gridColumns": 3,  
                    "order": 6,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "reductionPercentage",  
            "label": "Percentual de Redução (Lei 12.546/2011)",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 2,  
                    "divider": "Atividades Concomitantes",  
                    "order": 7,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "monthlyFactor",  
            "label": "Fator Mês",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 2,  
                    "order": 8,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "thirteenthMonthFactor",  
            "label": "Fator 13° Salário",  
            "type": "string",  
            "componentType": "Input"  
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
                    "gridColumns": 6,  
                    "divider": "DCTFWeb",  
                    "order": 9,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "immediateDctfWebTransmission",  
            "label": "Transmissão Imediata da DCTFWeb",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "options": [  
                {  
                    "value": 0,  
                    "label": "ㅤ"  
                },  
                {  
                    "value": 1,  
                    "label": "1 - 0,2000"  
                },  
                {  
                    "value": 2,  
                    "label": "2 - 0,4000"  
                },  
                {  
                    "value": 3,  
                    "label": "3 - 0,6000"  
                },  
                {  
                    "value": 4,  
                    "label": "4 - 0,8000"  
                },  
                {  
                    "value": 5,  
                    "label": "5 - 1,0000"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "gridColumns": 6,  
                    "divider": "Transformação em Sociedade de Fins Lucrativos",  
                    "order": 10,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "finalProfitSocialContributionPercentage",  
            "label": "Percentual de Contribuição Social",  
            "componentType": "Select"  
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
                    "gridColumns": 6,  
                    "divider": "Informações Sobre Aquisição de Produto Rural",  
                    "order": 11,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "ruralProductionAcquisitionIndicator",  
            "label": "Possui Informações Sobre Aquisição de Produto Ruaral de Pessoas Físicas",  
            "type": "boolean",  
            "componentType": "Switch"  
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
                    "gridColumns": 6,  
                    "order": 12,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "excludeRuralProductionAcquisitionInfo",  
            "label": "Exclui Informação Sobre Aquisições de Produção Rural",  
            "type": "boolean",  
            "componentType": "Switch"  
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
                    "gridColumns": 6,  
                    "order": 13,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "indicativeDoesNotValidateClosing",  
            "label": "Não Validar Regra de Fechamento da Folha",  
            "type": "boolean",  
            "componentType": "Switch"  
        }  
    ],  
    "groups": []  
}
