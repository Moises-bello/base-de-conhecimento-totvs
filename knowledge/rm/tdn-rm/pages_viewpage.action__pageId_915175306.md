---
content_hash: 1616e81d4fdefd3e0e7d220fd6de1e180680dead0005181ef1db5982b83781ef
fetched_at: '2026-06-29T00:12:06.381987+00:00'
page_id: '915175306'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Gerenciador do Log de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=915175306
version: 3
---

Foi criada a API para uso do produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Gerenciador do Log de Cálculo", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Gerenciador do Log de Cálculo que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rhv1/GerenciadorLogCalculo/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Gerenciador de Log de Cálculo",  
    "version": "1.0",  
    "identifier": "GerenciadorLogCalculo",  
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
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "execId",  
            "label": "Id de Execução",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "locale": "pt-BR",  
            "key": true,  
            "property": "dthrinicio",  
            "label": "Data Inicio",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "dataFim",  
            "label": "Data Fim",  
            "disabled": true,  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "computador",  
            "label": "Máquina utilizada",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "usuario",  
            "label": "Usuário",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "options": [  
                {  
                    "value": 0,  
                    "label": "Folha"  
                },  
                {  
                    "value": 1,  
                    "label": "Recalculo"  
                },  
                {  
                    "value": 2,  
                    "label": "Diferença Salarial"  
                },  
                {  
                    "value": 3,  
                    "label": "Importação"  
                },  
                {  
                    "value": 4,  
                    "label": "Importação Centro de Custo"  
                },  
                {  
                    "value": 5,  
                    "label": "Cancelamento do Movimento"  
                },  
                {  
                    "value": 6,  
                    "label": "Lançamento de 13º 1º Parcela"  
                },  
                {  
                    "value": 7,  
                    "label": "Lançamento de 13º 2ª Parcela"  
                },  
                {  
                    "value": 8,  
                    "label": "Diferença de 13º"  
                },  
                {  
                    "value": 9,  
                    "label": "Provisão de 13º"  
                },  
                {  
                    "value": 10,  
                    "label": "Cálculo de Férias"  
                },  
                {  
                    "value": 11,  
                    "label": "Cálculo de Férias Coletivas"  
                },  
                {  
                    "value": 12,  
                    "label": "Lançamento de Férias"  
                },  
                {  
                    "value": 13,  
                    "label": "Finalização de Férias"  
                },  
                {  
                    "value": 14,  
                    "label": "Diferença de Férias"  
                },  
                {  
                    "value": 15,  
                    "label": "Provisão de Férias"  
                },  
                {  
                    "value": 16,  
                    "label": "Cancelamento de Férias"  
                },  
                {  
                    "value": 17,  
                    "label": "Acerta Período Aquisitivo"  
                },  
                {  
                    "value": 18,  
                    "label": "Ad. Férias Portugal"  
                },  
                {  
                    "value": 19,  
                    "label": "Conversão de Férias Portugal"  
                },  
                {  
                    "value": 20,  
                    "label": "Cálculo de Rescisão"  
                },  
                {  
                    "value": 21,  
                    "label": "Líquido de Rescisão"  
                },  
                {  
                    "value": 22,  
                    "label": "Rescisão Complementar"  
                },  
                {  
                    "value": 23,  
                    "label": "Cancelamento de Rescisão"  
                },  
                {  
                    "value": 24,  
                    "label": "Sefip"  
                },  
                {  
                    "value": 25,  
                    "label": "GRRF"  
                },  
                {  
                    "value": 26,  
                    "label": "CAGED"  
                }  
            ],  
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
                },  
                {  
                    "gridColumns": 5,  
                    "componentType": "FilterLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "tipoProcesso",  
            "label": "Tipo de Cálculo",  
            "componentType": "Select"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "nomeTipoProcesso",  
            "label": "Tipo de Processo",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "chapa",  
            "label": "Matrícula",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "status",  
            "label": "Status",  
            "disabled": true,  
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
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "idJob",  
            "label": "Id Job",  
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
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "idProcesso",  
            "label": "Id Processo",  
            "type": "string",  
            "componentType": "Input"  
        },  
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
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "codColigada",  
            "label": "Coligada",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        }  
    ],  
    "groups": []  
}
