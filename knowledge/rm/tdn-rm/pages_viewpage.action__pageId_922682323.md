---
content_hash: ed053bcf57b28230e895158727a1667c300420070e766de8c7e4eac8f0d78744
fetched_at: '2026-06-29T00:12:07.268314+00:00'
page_id: '922682323'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Parametrização do Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=922682323
version: 4
---

Foi criada a API para uso dos produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Parametrização do Lançamento Financeiro", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais dos Parametrização do Lançamento Financeiro que já conhecíamos anteriormente.  
Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/ParametrizacaoLancamentosFinanceiros/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Parametrização dos Lançamentos Financeiros",  
    "version": "1.0",  
    "identifier": "ParametrizacaoLancamentosFinanceiros",  
    "fields": [  
        {  
            "key": true,  
            "property": "codColigada",  
            "label": "Coligada",  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "required": true,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "key": true,  
            "property": "codLanc",  
            "label": "Código",  
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
                    "gridColumns": 10,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "descricao",  
            "label": "Descrição",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "required": true,  
            "options": [  
                {  
                    "value": 1,  
                    "label": "1 - Líquido salarial"  
                },  
                {  
                    "value": 2,  
                    "label": "2 - Líquido rescisão"  
                },  
                {  
                    "value": 3,  
                    "label": "3 - Líquido férias"  
                },  
                {  
                    "value": 4,  
                    "label": "4 - INSS a pagar"  
                },  
                {  
                    "value": 5,  
                    "label": "5 -IRRF a pagar"  
                },  
                {  
                    "value": 6,  
                    "label": "6 - Encargos de FGTS"  
                },  
                {  
                    "value": 7,  
                    "label": "7 - Valor calculado por fórmula"  
                },  
                {  
                    "value": 8,  
                    "label": "8 - IRRF de Férias"  
                },  
                {  
                    "value": 9,  
                    "label": "9 - IRRF de Rescisão"  
                },  
                {  
                    "value": 10,  
                    "label": "10 - FGTS 13º"  
                },  
                {  
                    "value": 11,  
                    "label": "11 - INSS 13º a pagar"  
                },  
                {  
                    "value": 12,  
                    "label": "12 - IRRF 13º a pagar"  
                },  
                {  
                    "value": 13,  
                    "label": "13 - Total da GRFC"  
                },  
                {  
                    "value": 14,  
                    "label": "14 - Total da pensão"  
                },  
                {  
                    "value": 15,  
                    "label": "15 - FGTS conforme Sefip"  
                },  
                {  
                    "value": 16,  
                    "label": "16 - Pensão folha"  
                },  
                {  
                    "value": 17,  
                    "label": "17 - Pensão Férias"  
                },  
                {  
                    "value": 18,  
                    "label": "18 - Pensão 13º"  
                },  
                {  
                    "value": 19,  
                    "label": "19 - Pensão participação nos lucros"  
                },  
                {  
                    "value": 20,  
                    "label": "20 - Total de IRRF"  
                },  
                {  
                    "value": 21,  
                    "label": "21 - IRRF de participação nos lucros"  
                },  
                {  
                    "value": 22,  
                    "label": "22 - Pensão férias - somente eventos de pensão férias"  
                },  
                {  
                    "value": 24,  
                    "label": "24 - Total guia FGTS Digital"  
                },  
                {  
                    "value": 25,  
                    "label": "25 - Total guia INSS DCTFWeb"  
                },  
                {  
                    "value": 26,  
                    "label": "26 - Total guia INSS DCTFWeb 13º Salário"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "gridColumns": 4,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "lanFin",  
            "label": "Tipo do lançamento financeiro",  
            "componentType": "Select"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Codigo",  
                    "property": "codigo"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Título",  
                    "property": "titulo"  
                }  
            ],  
            "searchService": "/api/rh/v1/formulasFolha",  
            "format": [  
                "codigo",  
                "titulo"  
            ],  
            "fieldLabel": "titulo",  
            "fieldValue": "codigo",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 5,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "codFormCalc",  
            "label": "Fórmula",  
            "componentType": "Lookup"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Nao",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "arredTotal",  
            "label": "Aplicar arredondamento sobre o valor total do lançamento",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código",  
                    "property": "codTDO"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Descrição",  
                    "property": "descricao"  
                }  
            ],  
            "required": true,  
            "searchService": "/api/rh/v1/tipoDocumento",  
            "format": [  
                "codTDO",  
                "descricao"  
            ],  
            "fieldLabel": "descricao",  
            "fieldValue": "codTDO",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 4,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "codTDO",  
            "label": "Tipo de Documento",  
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
                    "visible": false,  
                    "componentType": "AdvancedFilterLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "tipoDocumento",  
            "label": "Descrição documento",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "property": "codColCFO",  
            "label": "Código Coligada Fornecedor",  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Coligada",  
                    "property": "codColigada"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Código",  
                    "property": "codCFO"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Nome Fantasia",  
                    "property": "nomeFantasia"  
                }  
            ],  
            "required": true,  
            "searchService": "/api/rh/v1/fornecedor",  
            "format": [  
                "codColigada",  
                "codCFO",  
                "nomeFantasia"  
            ],  
            "fieldLabel": "nomeFantasia",  
            "fieldValue": "codCFO",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 6,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "codCFO",  
            "label": "Código Fornecedor",  
            "componentType": "Lookup"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "fornecedorGlobal",  
            "label": "Fornecedor Global",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Codigo",  
                    "property": "codigo"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Descrição",  
                    "property": "descricao"  
                }  
            ],  
            "searchService": "/api/rh/v1/rateios",  
            "format": [  
                "codigo",  
                "descricao"  
            ],  
            "fieldLabel": "descricao",  
            "fieldValue": "codigo",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "codRateio",  
            "label": "Rateio que o lançamento segue",  
            "componentType": "Lookup"  
        },  
        {  
            "options": [  
                {  
                    "value": 1,  
                    "label": "Mês Atual"  
                },  
                {  
                    "value": 2,  
                    "label": "Período Aquisitivo"  
                },  
                {  
                    "value": 3,  
                    "label": "Ano de competência"  
                },  
                {  
                    "value": 4,  
                    "label": "Mês anteior"  
                },  
                {  
                    "value": 5,  
                    "label": "Competência passada no processo"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "perCalcRateio",  
            "label": "Período de Cálculo do Rateio",  
            "componentType": "Select"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 5,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "complHistorico",  
            "label": "Complemento do histórico",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Codigo",  
                    "property": "codigo"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Aplicação",  
                    "property": "aplicacao"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Título",  
                    "property": "titulo"  
                }  
            ],  
            "searchService": "/api/rh/v1/formulasFolhaComplemento",  
            "format": [  
                "codigo",  
                "aplicacao",  
                "titulo"  
            ],  
            "fieldLabel": "titulo",  
            "fieldValue": "codigo",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 5,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "formComplHist",  
            "label": "Fórmula para complemento histórico",  
            "componentType": "Lookup"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Nao",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "usarHistoricoPadrao",  
            "label": "Usar histórico padrão",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Nao",  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "desconsiderarAutonomos",  
            "label": "Desconsiderar Autônomos TOTVS Gestão Financeira",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "options": [  
                {  
                    "value": 1,  
                    "label": "Mensal"  
                },  
                {  
                    "value": 2,  
                    "label": "Rescisório"  
                },  
                {  
                    "value": 3,  
                    "label": "Rescisório + Mensal"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 12,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "radioGroup",  
            "container": "FGTS Digital",  
            "property": "tipoGuiaFGTSDigital",  
            "label": "Gerar guia para o tipo",  
            "componentType": "RadioGroup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                },  
                {  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "tipoGuiaFGTSDigitalDescricao",  
            "label": "FGTS Digital",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "property": "codColCxa",  
            "label": "Código Coligada Caixa",  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        }  
    ],  
    "groups": [  
        {  
            "title": "Parâmetros",  
            "identifier": "parametros",  
            "order": 1,  
            "componentType": "Tab",  
            "fields": [  
                {  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 2,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "property": "acrescimo",  
                    "label": "Percentual de acréscimo",  
                    "type": "number",  
                    "componentType": "Number"  
                },  
                {  
                    "options": [  
                        {  
                            "value": 0,  
                            "label": "Não Contábil"  
                        },  
                        {  
                            "value": 1,  
                            "label": "Contábil"  
                        },  
                        {  
                            "value": 2,  
                            "label": "Baixa Contábil"  
                        },  
                        {  
                            "value": 3,  
                            "label": "A Contabilizar"  
                        }  
                    ],  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 5,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "forceOptionsComponentType": "select",  
                    "property": "tipoContabil",  
                    "label": "Tipo contábil do lançamento",  
                    "componentType": "Select"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Símbolo",  
                            "property": "id"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "description"  
                        }  
                    ],  
                    "searchService": "/api/financial/v1/currencies",  
                    "format": [  
                        "id",  
                        "description"  
                    ],  
                    "fieldLabel": "description",  
                    "fieldValue": "id",  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 5,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "moeda",  
                    "label": "Moeda",  
                    "componentType": "Lookup"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Código",  
                            "property": "codTbOrcamento"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "descricao"  
                        }  
                    ],  
                    "searchService": "/api/rh/v1/NaturezaFinanceira",  
                    "format": [  
                        "codTbOrcamento",  
                        "descricao"  
                    ],  
                    "fieldLabel": "descricao",  
                    "fieldValue": "codTbOrcamento",  
                    "layoutDefinition": [  
                        {  
                            "gridColumns": 3,  
                            "componentType": "EditLayout"  
                        },  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "codNatFinanceira",  
                    "label": "Natureza Financeira",  
                    "componentType": "Lookup"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Coligada",  
                            "property": "codColigada"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Código",  
                            "property": "codCxa"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "descricao"  
                        }  
                    ],  
                    "searchService": "/api/rh/v1/ContaCaixa",  
                    "format": [  
                        "codColigada",  
                        "codCxa",  
                        "descricao"  
                    ],  
                    "fieldLabel": "descricao",  
                    "fieldValue": "codCxa",  
                    "layoutDefinition": [  
                        {  
                            "gridColumns": 6,  
                            "componentType": "EditLayout"  
                        },  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "codCxa",  
                    "label": "Conta/Caixa",  
                    "componentType": "Lookup"  
                },  
                {  
                    "booleanTrue": "Sim",  
                    "booleanFalse": "Não",  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 3,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "property": "caixaGlobal",  
                    "label": "Caixa Global",  
                    "type": "boolean",  
                    "componentType": "Switch"  
                },  
                {  
                    "booleanTrue": "Sim",  
                    "booleanFalse": "Não",  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 12,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "property": "usarDataPagNoVencimento",  
                    "label": "Usar data de pagamento para vencimento do lançamento",  
                    "type": "boolean",  
                    "componentType": "Switch"  
                },  
                {  
                    "options": [  
                        {  
                            "value": 0,  
                            "label": "Agrupar por seção"  
                        },  
                        {  
                            "value": 3,  
                            "label": "Agrupar por seção e fornecedor"  
                        },  
                        {  
                            "value": 1,  
                            "label": "Individual por funcionário"  
                        },  
                        {  
                            "value": 2,  
                            "label": "Individual por dependente"  
                        },  
                        {  
                            "value": 4,  
                            "label": "Individual por sindicato"  
                        },  
                        {  
                            "value": 5,  
                            "label": "Tomador"  
                        },  
                        {  
                            "value": 6,  
                            "label": "Tomador/CEI"  
                        },  
                        {  
                            "value": 7,  
                            "label": "Agrupar por coligada"  
                        },  
                        {  
                            "value": 8,  
                            "label": "Agrupar por lotação tributária"  
                        }  
                    ],  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 6,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "forceOptionsComponentType": "radioGroup",  
                    "property": "tipoIndividual",  
                    "label": "Agrupamentos",  
                    "componentType": "RadioGroup"  
                },  
                {  
                    "options": [  
                        {  
                            "value": 0,  
                            "label": "Parametrização"  
                        },  
                        {  
                            "value": 1,  
                            "label": "Funcionário"  
                        },  
                        {  
                            "value": 2,  
                            "label": "Dependente"  
                        },  
                        {  
                            "value": 3,  
                            "label": "Sindicato"  
                        }  
                    ],  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 6,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "forceOptionsComponentType": "radioGroup",  
                    "property": "origemFornec",  
                    "label": "Origem do fornecedor",  
                    "componentType": "RadioGroup"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Código",  
                            "property": "codTb1Flx"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "descricao"  
                        }  
                    ],  
                    "searchService": "/api/rh/v1/FinSecao",  
                    "format": [  
                        "codTb1Flx",  
                        "descricao"  
                    ],  
                    "fieldLabel": "descricao",  
                    "fieldValue": "codTb1Flx",  
                    "layoutDefinition": [  
                        {  
                            "gridColumns": 2,  
                            "componentType": "EditLayout"  
                        },  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "codTb1Flx",  
                    "label": "Seção",  
                    "componentType": "Lookup"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Código",  
                            "property": "codTb2Flx"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "descricao"  
                        }  
                    ],  
                    "searchService": "/api/rh/v1/FinPortador",  
                    "format": [  
                        "codTb2Flx",  
                        "descricao"  
                    ],  
                    "fieldLabel": "descricao",  
                    "fieldValue": "codTb2Flx",  
                    "layoutDefinition": [  
                        {  
                            "gridColumns": 2,  
                            "componentType": "EditLayout"  
                        },  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "codTb2Flx",  
                    "label": "Portador",  
                    "componentType": "Lookup"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Código",  
                            "property": "codTb3Flx"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "descricao"  
                        }  
                    ],  
                    "searchService": "/api/rh/v1/FinCentroDeDespesa",  
                    "format": [  
                        "codTb3Flx",  
                        "descricao"  
                    ],  
                    "fieldLabel": "descricao",  
                    "fieldValue": "codTb3Flx",  
                    "layoutDefinition": [  
                        {  
                            "gridColumns": 2,  
                            "componentType": "EditLayout"  
                        },  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "codTb3Flx",  
                    "label": "Centro de Despesa",  
                    "componentType": "Lookup"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Código",  
                            "property": "codTb4Flx"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "descricao"  
                        }  
                    ],  
                    "searchService": "/api/rh/v1/FinNaturezaDeGasto",  
                    "format": [  
                        "codTb4Flx",  
                        "descricao"  
                    ],  
                    "fieldLabel": "descricao",  
                    "fieldValue": "codTb4Flx",  
                    "layoutDefinition": [  
                        {  
                            "gridColumns": 2,  
                            "componentType": "EditLayout"  
                        },  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "codTb4Flx",  
                    "label": "Natureza de Gasto",  
                    "componentType": "Lookup"  
                },  
                {  
                    "columns": [  
                        {  
                            "fieldLabel": false,  
                            "label": "Código",  
                            "property": "codTb5Flx"  
                        },  
                        {  
                            "fieldLabel": false,  
                            "label": "Descrição",  
                            "property": "descricao"  
                        }  
                    ],  
                    "searchService": "/api/rh/v1/FinContratosVendor",  
                    "format": [  
                        "codTb5Flx",  
                        "descricao"  
                    ],  
                    "fieldLabel": "descricao",  
                    "fieldValue": "codTb5Flx",  
                    "layoutDefinition": [  
                        {  
                            "gridColumns": 2,  
                            "componentType": "EditLayout"  
                        },  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        }  
                    ],  
                    "clean": true,  
                    "noAutoComplete": true,  
                    "property": "codTb5Flx",  
                    "label": "Contratos Vendor",  
                    "componentType": "Lookup"  
                },  
                {  
                    "columns": 1,  
                    "options": [  
                        {  
                            "value": "01",  
                            "label": "Todos"  
                        },  
                        {  
                            "value": "02",  
                            "label": "Lançamentos de folha"  
                        },  
                        {  
                            "value": "03",  
                            "label": "Lançamentos de férias"  
                        },  
                        {  
                            "value": "04",  
                            "label": "Lançamentos de rescisão"  
                        }  
                    ],  
                    "optionsMulti": true,  
                    "layoutDefinition": [  
                        {  
                            "visible": false,  
                            "componentType": "TableLayout"  
                        },  
                        {  
                            "gridColumns": 12,  
                            "componentType": "EditLayout"  
                        }  
                    ],  
                    "property": "lancamentosAtivos",  
                    "label": "Lançamentos Ativos",  
                    "componentType": "CheckboxGroup"  
                }  
            ]  
        }  
    ]  
}

Inclusão de Registro

**Endpoint:**/api/rh/v1/ParametrizacaoLancamentosFinanceiros/ **Método:** POST **Objetivo:** Incluir registros na Parametrizacao de Lancamentos Financeiros

Exemplo de Requisição

{  
  "codColigada": 0,  
  "codLanc": "078",  
  "descricao": "TESTE 78",  
  "lanFin": 1,  
  "arredTotal": false,  
  "codTDO": "01",  
  "codColCFO": 0,  
  "codCFO": "RM",  
  "fornecedorGlobal": false,  
  "perCalcRateio": 0,  
  "usarHistoricoPadrao": false,  
  "desconsiderarAutonomos": false,  
  "tipoGuiaFGTSDigital": 0,  
  "tipoGuiaFGTSDigitalDescricao": "",  
  "acrescimo": 0,  
  "tipoContabil": 0,  
  "codColCxa": 0,  
  "caixaGlobal": false,  
  "usarDataPagNoVencimento": false,  
  "tipoIndividual": 0,  
  "origemFornec": 0,  
  "lancamentosAtivos": []  
}

Exemplo de Retorno

**Status Code: 201 Created**

{  
    "codColigada": 0,  
    "codLanc": "078",  
    "descricao": "TESTE 78",  
    "lanFin": 1,  
    "arredTotal": false,  
    "codTDO": "01",  
    "codColCFO": 0,  
    "codCFO": "RM",  
    "fornecedorGlobal": false,  
    "perCalcRateio": 0,  
    "usarHistoricoPadrao": false,  
    "desconsiderarAutonomos": false,  
    "tipoGuiaFGTSDigital": 0,  
    "tipoGuiaFGTSDigitalDescricao": "",  
    "acrescimo": 0.0,  
    "tipoContabil": 0,  
    "codColCxa": 0,  
    "caixaGlobal": false,  
    "usarDataPagNoVencimento": false,  
    "tipoIndividual": 0,  
    "origemFornec": 0,  
    "lancamentosAtivos": []  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:

150Edição de Registro

**Endpoint:  /api/rh/v1/ParametrizacaoLancamentosFinanceiros/1|078** **Método:** PUT **Objetivo:** Edita registros dos Parametros do Lançamento Financeiro

Exemplo de Requisição

{  
  "codColigada": 1,  
  "codLanc": "078",  
  "descricao": "TESTE 78 EDICAO",  
  "lanFin": 1,  
  "arredTotal": false,  
  "codTDO": "01",  
  "tipoDocumento": "NF",  
  "codColCFO": 1,  
  "codCFO": "RM",  
  "fornecedorGlobal": false,  
  "perCalcRateio": 0,  
  "usarHistoricoPadrao": false,  
  "desconsiderarAutonomos": false,  
  "tipoGuiaFGTSDigitalDescricao": "",  
  "acrescimo": 0,  
  "tipoContabil": 0,  
  "codColCxa": 0,  
  "caixaGlobal": true,  
  "usarDataPagNoVencimento": false,  
  "tipoIndividual": 0,  
  "origemFornec": 0,  
  "lancamentosAtivos": []  
}

Exemplo de Retorno

**Status Code: 200 OK**{  
    "codColigada": 1,  
    "codLanc": "078",  
    "descricao": "TESTE 78 EDICAO",  
    "lanFin": 1,  
    "arredTotal": false,  
    "codTDO": "01",  
    "tipoDocumento": "NF",  
    "codColCFO": 1,  
    "codCFO": "RM",  
    "fornecedorGlobal": false,  
    "perCalcRateio": 0,  
    "usarHistoricoPadrao": false,  
    "desconsiderarAutonomos": false,  
    "tipoGuiaFGTSDigital": 0,  
    "tipoGuiaFGTSDigitalDescricao": "",  
    "acrescimo": 0.0,  
    "tipoContabil": 0,  
    "codColCxa": 0,  
    "caixaGlobal": true,  
    "usarDataPagNoVencimento": false,  
    "tipoIndividual": 0,  
    "origemFornec": 0,  
    "lancamentosAtivos": []  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Exclusão de Registro

**Endpoint: /api/rh/v1/ParametrizacaoLancamentosFinanceiros/1|078** **Método:** DELETE **Objetivo:** Excluir registros da Parametrização do Lançamento Financeiro

Exemplo de Retorno

**Status Code: 204 No Content**

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150
