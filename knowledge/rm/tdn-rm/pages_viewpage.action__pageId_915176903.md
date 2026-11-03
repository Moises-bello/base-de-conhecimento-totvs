---
content_hash: 65a3bfb06bd561c9a4aee3727e647a929121190fc154644a2d2ce76a91c85ee8
fetched_at: '2026-06-29T00:12:06.423453+00:00'
page_id: '915176903'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Linha de Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=915176903
version: 3
---

Foi criada a API para uso dos produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Linhas de Vale Transporte", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Linhas de Vale Transporte que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/LinhaValeTransporte/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Linha Vale Transporte",  
    "version": "1.0",  
    "identifier": "TransportLine",  
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
            "property": "codColigada",  
            "label": "Coligada",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "required": true,  
            "maxLength": 20,  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 4,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "key": true,  
            "property": "codigo",  
            "label": "Codigo",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "required": true,  
            "maxLength": 50,  
            "layoutDefinition": [  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 8,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 8,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "nomeLinha",  
            "label": "Descrição de vale transporte",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código",  
                    "property": "codigo"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Descrição",  
                    "property": "descricao"  
                },  
                {  
                    "fieldLabel": false,  
                    "format": "dd/MM/yyyy",  
                    "label": "Início Vigência",  
                    "property": "inicioVigencia",  
                    "type": "date"  
                },  
                {  
                    "fieldLabel": false,  
                    "format": "dd/MM/yyyy",  
                    "label": "Final Vigência",  
                    "property": "finalVigencia",  
                    "type": "date"  
                }  
            ],  
            "searchService": "/api/rh/v1/tarifaTransporte",  
            "format": [  
                "codigo",  
                "descricao"  
            ],  
            "fieldLabel": "descricao",  
            "fieldValue": "codigo",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "searchServiceFilter": "lookup",  
            "property": "codTarifa",  
            "label": "Código Tarifa",  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "widthColumnTable": 120,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "AdvancedFilterLayout"  
                }  
            ],  
            "property": "nomeCodTarifa",  
            "label": "Tarifa",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código",  
                    "property": "codCliente"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Descrição",  
                    "property": "descricao"  
                }  
            ],  
            "required": true,  
            "searchService": "/api/rh/v1/itinerario",  
            "format": [  
                "codCliente",  
                "descricao"  
            ],  
            "fieldLabel": "descricao",  
            "fieldValue": "codCliente",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "codItinerario",  
            "label": "Código Itinerario",  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "widthColumnTable": 120,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "AdvancedFilterLayout"  
                }  
            ],  
            "property": "nomeCodItinerario",  
            "label": "Itinerario",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "columns": [  
                {  
                    "fieldLabel": false,  
                    "label": "Código",  
                    "property": "codCliente"  
                },  
                {  
                    "fieldLabel": false,  
                    "label": "Descrição",  
                    "property": "descricao"  
                }  
            ],  
            "required": true,  
            "searchService": "/api/rh/v1/grupoTransporte",  
            "format": [  
                "codCliente",  
                "descricao"  
            ],  
            "fieldLabel": "descricao",  
            "fieldValue": "codCliente",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "property": "grupoTransp",  
            "label": "Grupo Transporte",  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "widthColumnTable": 120,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "AdvancedFilterLayout"  
                }  
            ],  
            "property": "nomeGrupoTransp",  
            "label": "Grupo Transporte",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "required": true,  
            "options": [  
                {  
                    "value": "B",  
                    "label": "Barca"  
                },  
                {  
                    "value": "I",  
                    "label": "Integração"  
                },  
                {  
                    "value": "M",  
                    "label": "Metrô"  
                },  
                {  
                    "value": "N",  
                    "label": "Bonde"  
                },  
                {  
                    "value": "O",  
                    "label": "Ônibus"  
                },  
                {  
                    "value": "T",  
                    "label": "Trem"  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "tipoTransp",  
            "label": "Tipo Transporte",  
            "componentType": "Select"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "widthColumnTable": 120,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "AdvancedFilterLayout"  
                }  
            ],  
            "property": "nomeTipoTransp",  
            "label": "Tipo Transporte",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "unico",  
            "label": "Apenas um vale transporte",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "ativo",  
            "label": "Ativo",  
            "type": "boolean",  
            "componentType": "Switch"  
        }  
    ],  
    "groups": []  
}

Inclusão de Registro

**Endpoint:  /**/api/rh/v1/LinhaValeTransporte/ **Método:** POST **Objetivo:**Incluir registros da Linha de Vale Transporte.

Exemplo de requisição

{  
  "codigo": "3742",  
  "nomeLinha": "LOTACAO 3742",  
  "codTarifa": "003",  
  "codItinerario": "01",  
  "grupoTransp": "00",  
  "tipoTransp": "O",  
  "ativo": true  
}

Exemplo de Retorno

**Status Code: 201 Created**  
{  
    "codColigada": 1,  
    "codigo": "3742",  
    "nomeLinha": "LOTACAO 3742",  
    "codTarifa": "003",  
    "codItinerario": "01",  
    "grupoTransp": "00",  
    "tipoTransp": "O",  
    "unico": false,  
    "ativo": true  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:

150Edição de Registro

**Endpoint:** /api/rh/v1/LinhaValeTransporte/1%7C3742 **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / CODIGO )**  
**Método:** PUT

**Objetivo:**Alterar um registro já incluido anteriormente

Exemplo de requisição

{  
  "codColigada": 1,  
  "codigo": "3742",  
  "nomeLinha": "LOTACAO 3742 UPDATE",  
  "codTarifa": "003",  
  "codItinerario": "01",  
  "grupoTransp": "00",  
  "tipoTransp": "O",  
  "unico": false,  
  "ativo": true  
}

Exemplo de Retorno

**Status Code: 200  OK**

{  
    "codColigada": 1,  
    "codigo": "3742",  
    "nomeLinha": "LOTACAO 3742 UPDATE",  
    "codTarifa": "003",  
    "codItinerario": "01",  
    "grupoTransp": "00",  
    "tipoTransp": "O",  
    "unico": false,  
    "ativo": true  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Exclusão de Registro

**Endpoint:** /api/rh/v1/LinhaValeTransporte/1%7C3742  **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / CODIGO )**  
  
**Método:** DELETE

**Objetivo:**Excluir um registro já incluido anteriormente

Exemplo de Retorno

**Status Code: 204  No Content**

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150
