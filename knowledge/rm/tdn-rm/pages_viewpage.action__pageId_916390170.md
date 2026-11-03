---
content_hash: 9fe1f796272e6ecdabe0419f9fd50d550a9ffe3cfa74b2bc76dd8fa692863ac5
fetched_at: '2026-06-29T00:12:06.431102+00:00'
page_id: '916390170'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Múltiplos Vínculos que precisa de Recálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=916390170
version: 3
---

Foi criada a API para uso dos produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Múltiplos Vínculos que precisa de Recálculo", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Múltiplos Vínculos que precisa de Recálculo que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:** /api/rh/v1/MultiVinculosPrecisaRecalculo/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Múltiplos Vínculos que precisa de Recálculo",  
    "version": "1.0",  
    "identifier": "MultiVinculosPrecisaRecalculo",  
    "fields": [  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "codColigada",  
            "label": "Coligada",  
            "visible": false,  
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
                    "gridColumns": 6,  
                    "componentType": "DetailLayout"  
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
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "nomeChapa",  
            "label": "Nome da pessoa colaboradora",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "anoComp",  
            "label": "Ano",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "options": [  
                {  
                    "value": 1,  
                    "label": "Janeiro"  
                },  
                {  
                    "value": 2,  
                    "label": "Fevereiro"  
                },  
                {  
                    "value": 3,  
                    "label": "Março"  
                },  
                {  
                    "value": 4,  
                    "label": "Abril"  
                },  
                {  
                    "value": 5,  
                    "label": "Maio"  
                },  
                {  
                    "value": 6,  
                    "label": "Junho"  
                },  
                {  
                    "value": 7,  
                    "label": "Julho"  
                },  
                {  
                    "value": 8,  
                    "label": "Agosto"  
                },  
                {  
                    "value": 9,  
                    "label": "Setembro"  
                },  
                {  
                    "value": 10,  
                    "label": "Outubro"  
                },  
                {  
                    "value": 11,  
                    "label": "Novembro"  
                },  
                {  
                    "value": 12,  
                    "label": "Dezembro"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "gridColumns": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "key": true,  
            "property": "mesComp",  
            "label": "Mês",  
            "componentType": "Select"  
        }  
    ],  
    "groups": []  
}
