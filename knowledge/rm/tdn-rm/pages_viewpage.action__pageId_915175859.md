---
content_hash: 1d7b305834b0a8d99fd43c41d6ca0356625452545a133ae46b1030cfd91257ae
fetched_at: '2026-06-29T00:12:06.401880+00:00'
page_id: '915175859'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Histórico de Encargos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=915175859
version: 4
---

Foi criada a API para uso do produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Histórico de Encargos", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Histórico de Encargos que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/HistoricoEncargo/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Histórico de Encargo",  
    "version": "1.0",  
    "identifier": "HistoricoEncargo",  
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
                    "gridColumns": 5,  
                    "componentType": "EditLayout"  
                },  
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
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 5,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "nome",  
            "label": "Nome da pessoa colaboradora",  
            "disabled": true,  
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
                }  
            ],  
            "required": true,  
            "searchService": "/api/rh/v1/encargo",  
            "format": [  
                "codigo",  
                "descricao"  
            ],  
            "fieldLabel": "descricao",  
            "fieldValue": "codigo",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 5,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 3,  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                },  
                {  
                    "order": 1,  
                    "componentType": "FilterLayout"  
                }  
            ],  
            "clean": true,  
            "noAutoComplete": true,  
            "key": true,  
            "property": "codEncargo",  
            "label": "Código do Encargo",  
            "componentType": "Lookup"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "order": 3,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "descricao",  
            "label": "Descrição",  
            "disabled": true,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "layoutDefinition": [  
                {  
                    "order": 1,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 1,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 1,  
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
                    "widthColumnTable": 60,  
                    "componentType": "TableLayout"  
                },  
                {  
                    "gridColumns": 1,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 1,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "key": true,  
            "property": "mesComp",  
            "label": "Mês",  
            "componentType": "Select"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 6,  
            "minValue": "0.00",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 6,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                }  
            ],  
            "locale": "pt-BR",  
            "property": "baseEncargo",  
            "label": "Base do Encargo",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 2,  
            "thousandMaxlength": 6,  
            "minValue": "0.00",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 6,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "gridColumns": 6,  
                    "componentType": "DetailLayout"  
                },  
                {  
                    "componentType": "TableLayout"  
                }  
            ],  
            "locale": "pt-BR",  
            "property": "valor",  
            "label": "Valor Nominal",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "aplicacao",  
            "label": "Aplicacao",  
            "disabled": true,  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        }  
    ],  
    "groups": []  
}

Inclusão de Registro

**Endpoint:  /**/api/rh/v1/HistoricoEncargo/ **Método:** POST **Objetivo:**Incluir registros no Histórico da Encargos de maneira manual, não necessitando do processo de geração de Histórico de Encargos.

Exemplo de requisição

{  
  "chapa": "00002",  
  "codEncargo": "015",  
  "anoComp": "2026",  
  "mesComp": 3,  
  "baseEncargo": 200,  
  "valor": 250  
}

Exemplo de Retorno

**Status Code: 201 Created**{  
    "codColigada": 1,  
    "chapa": "00002",  
    "codEncargo": "015",  
    "anoComp": 2026,  
    "mesComp": 3,  
    "baseEncargo": 200.0,  
    "valor": 250.0,  
    "aplicacao": "P"  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Edição de Registro

**Endpoint:** /api/rh/v1/HistoricoEncargo/1%7CA0004%7C015%7C2011%7C10 **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / CHAPA / CODENCARGO / ANOCOMP / MESCOMP  )**  
**Método:** PUT

**Objetivo:**Alterar um registro já incluido anteriormente

Exemplo de requisição

{  
  "codColigada": 1,  
  "chapa": "A0004",  
  "nome": "FL LANÇAMENTO FINANCEIRO PROXIMO MÊS FUNCIONÁRIO AFASTADO TIPO T",  
  "codEncargo": "015",  
  "descricao": "FGTS AFASTAMENTO DO TIPO T",  
  "anoComp": 2011,  
  "mesComp": 10,  
  "baseEncargo": 1102,  
  "valor": 88.4,  
  "aplicacao": "P",  
  "links": [  
    {  
      "relation": "RateioEncargosCC",  
      "apiMetaData": "api/rh/v1/RateioEncargoCC/schema",  
      "apiData": "api/rh/v1/RateioEncargoCC/",  
      "apiDataFilter": "?$filter=codColigada eq 1 and chapa eq 'A0004' and anoComp eq 2011 and mesComp eq 10 and codEncargo eq '015'",  
      "type": "RelatedItems",  
      "label": "Rateio de Encargo por Centro de Custo",  
      "mapper": {  
        "anoComp": "2011",  
        "mesComp": "10",  
        "codColigada": "1",  
        "codEncargo": "015",  
        "chapa": "A0004"  
      }  
    }  
  ]  
}

Exemplo de Retorno

**Status Code: 200  OK**

{  
    "codColigada": 1,  
    "chapa": "A0004",  
    "nome": "FL LANÇAMENTO FINANCEIRO PROXIMO MÊS FUNCIONÁRIO AFASTADO TIPO T",  
    "codEncargo": "015",  
    "descricao": "FGTS AFASTAMENTO DO TIPO T",  
    "anoComp": 2011,  
    "mesComp": 10,  
    "baseEncargo": 1102.0,  
    "valor": 88.4,  
    "aplicacao": "P"  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Exclusão de Registro

**Endpoint:** /api/rh/v1/HistoricoEncargo/1%7CT0001%7C003%7C2011%7C9 **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / CHAPA / CODENCARGO / ANOCOMP / MESCOMP  )**  
  
**Método:** DELETE

**Objetivo:**Excluir um registro já incluido anteriormente

Exemplo de Retorno

**Status Code: 204  No Content**

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150
