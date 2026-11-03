---
content_hash: 5b066f19cbb3fc478ab761525f6fb95a0eea75042669d0793ab434ef6e00434f
fetched_at: '2026-06-29T00:12:06.342296+00:00'
page_id: '915155042'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Consulta Movimento Passivo Trabalhista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=915155042
version: 4
---

Foi criada a API para uso do produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Consulta Movimento Passivo Trabalhista", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais da Consulta Movimento Passivo Trabalhista que já conhecíamos anteriormente.  
Este cadastro contém dados relativos aos dados das verbas calculadas no processo do Passivo Trabalhista.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/ConsultaMovimentoPassivoTrabalhista/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Consulta Movimento Passivo Trabalhista",  
    "version": "1.0",  
    "identifier": "ConsultationMovementPassiveLabor",  
    "fields": [  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "codColigada",  
            "label": "Coligada",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Chapa",  
                    "property": "chapa"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Nome",  
                    "property": "nome"  
                }  
            ],  
            "required": true,  
            "searchService": "/api/rh/v1/chapa",  
            "format": [  
                "chapa",  
                "nome"  
            ],  
            "fieldLabel": "nome",  
            "fieldValue": "chapa",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "order": 1,  
                    "componentType": "FilterLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "key": true,  
            "property": "chapa",  
            "label": "Matrícula",  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 9,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "nome",  
            "label": "Nome da pessoa colaboradora",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "codEvento",  
            "label": "Código do Evento",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "evento",  
            "label": "Evento",  
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
                    "gridColumns": 4,  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "tipoEvento",  
            "label": "Id Tipo de Evento",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "nomeTipoEvento",  
            "label": "Tipo de Evento",  
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
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "hora",  
            "label": "Hora",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "horaFormatada",  
            "label": "Horas",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 6,  
            "minValue": "0.00",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "ref",  
            "label": "Referência",  
            "type": "decimal",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 6,  
            "minValue": "0.00",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "valor",  
            "label": "Valor",  
            "type": "currency",  
            "componentType": "Decimal"  
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
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "origemMov",  
            "label": "Id Origem do Movimento",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "desOrigemMov",  
            "label": "Origem do Movimento",  
            "type": "string",  
            "componentType": "Input"  
        }  
    ],  
    "groups": []  
}
