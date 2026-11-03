---
content_hash: 8bec2ac84710200cb2b95f22c56de8b8525a739aeabe97fda918149aa6c9b57c
fetched_at: '2026-06-29T00:12:06.361950+00:00'
page_id: '915167496'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Dados do Dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=915167496
version: 6
---

Foi criada a API para uso dos produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Dados do Dissídio", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Dados do Dissídio (Acordo Coletivo / Reajuste por Lei) que já conhecíamos anteriormente.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/DadosDissidio/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Dados Dissidio",  
    "version": "1.0",  
    "identifier": "DadosDissidio",  
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
            "required": true,  
            "mask": "9999",  
            "maskFormatModel": true,  
            "maxLength": 4,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "key": true,  
            "property": "id",  
            "label": "Identificador",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "maxLength": 12,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 4,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "numeroLei",  
            "label": "Número da Lei do reajuste retroativo",  
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
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "mesCompPagto",  
            "label": "Mês Pagamento",  
            "componentType": "Select"  
        },  
        {  
            "quickFilter": true,  
            "mask": "9999",  
            "maskFormatModel": true,  
            "maxLength": 4,  
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
            "property": "anoCompPagto",  
            "label": "Ano Pagamento",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "dtAcordo",  
            "label": "Data da assinatura do acordo",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "dtEfeito",  
            "label": "Data do efeito",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "quickFilter": true,  
            "required": true,  
            "options": [  
                {  
                    "value": "A",  
                    "label": "A - Acordo Coletivo de Trabalho"  
                },  
                {  
                    "value": "B",  
                    "label": "B - Legislação federal, estadual, municipal ou distrital"  
                },  
                {  
                    "value": "C",  
                    "label": "C - Convenção Coletiva de Trabalho"  
                },  
                {  
                    "value": "D",  
                    "label": "D - Sentença Normativa - Dissídio"  
                },  
                {  
                    "value": "E",  
                    "label": "E - Conversão de Licença Saúde em Acidente de Trabalho"  
                },  
                {  
                    "value": "F",  
                    "label": "F - Outras verbas de natureza salarial ou não salarial devidas após o desligamento"  
                },  
                {  
                    "value": "G",  
                    "label": "G - Antecipação de diferenças de Acordo, Convenção ou Dissídio Coletivo"  
                },  
                {  
                    "value": "I",  
                    "label": "I - Sentença judicial (exceto reclamatória trabalhista)"  
                },  
                {  
                    "value": "J",  
                    "label": "J - Parcelas complementares conhecidas após o fechamento da folha"  
                }  
            ],  
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
            "forceOptionsComponentType": "select",  
            "property": "tpAcordo",  
            "label": "Tipo do acordo",  
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
                    "componentType": "AdvancedFilterLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "FilterLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "DetailLayout"  
                }  
            ],  
            "property": "tpAcordoTextoTableLayout",  
            "label": "Tipo do Acordo",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "required": true,  
            "maxLength": 255,  
            "rows": 3,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 12,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "descricao",  
            "label": "Descrição",  
            "componentType": "TextArea"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 12,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "sucessaoVinculo",  
            "label": "Pagamento de verbas devidas pela empresa sucessora a empregados desligados ainda na sucedida",  
            "type": "boolean",  
            "componentType": "Switch"  
        }  
    ],  
    "groups": []  
}

Inclusão de Registro

**Endpoint:  /**api/rh/v1/DadosDissidio/ **Método:** POST **Objetivo:** Incluir registros na pagina de Dados do Dissidio

Exemplo de requisição

{  
  "id": "12",  
  "numeroLei": "21318",  
  "mesCompPagto": 2,  
  "anoCompPagto": "2025",  
  "dtAcordo": "2025-01-01",  
  "dtEfeito": "2025-12-31",  
  "tpAcordo": "A",  
  "descricao": "INCLUSAO DADOS DO DISSIDIO"  
}

Exemplo de Retorno

**Status Code: 201 Created**{  
    "codColigada": 1,  
    "id": 12,  
    "numeroLei": "21318",  
    "mesCompPagto": 2,  
    "anoCompPagto": 2025,  
    "dtAcordo": "2025-01-01T00:00:00-03:00",  
    "dtEfeito": "2025-12-31T00:00:00-03:00",  
    "tpAcordo": "A",  
    "descricao": "INCLUSAO DADOS DO DISSIDIO",  
    "sucessaoVinculo": false  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Edição de Registro

**Endpoint:  /api/rh/v1/DadosDissidio/1%7C13** **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / NUMERO DO IDENTIFICADOR  )**  
**Método:** PUT

**Objetivo:**Alterar um registro já incluido anteriormente

Exemplo de requisição

{  
  "codColigada": 1,  
  "id": "13",  
  "numeroLei": "342534",  
  "mesCompPagto": 2,  
  "anoCompPagto": "2025",  
  "dtAcordo": "2024-01-01T00:00:00-03:00",  
  "dtEfeito": "2025-12-31T00:00:00-03:00",  
  "tpAcordo": "C",  
  "tpAcordoTextoTableLayout": "C - Convenção Coletiva de Trabalho",  
  "descricao": "teste mockoon 123",  
  "sucessaoVinculo": false  
}

Exemplo de Retorno

**Status Code: 200  OK**

{  
    "codColigada": 1,  
    "id": 13,  
    "numeroLei": "342534",  
    "mesCompPagto": 2,  
    "anoCompPagto": 2025,  
    "dtAcordo": "2024-01-01T00:00:00-03:00",  
    "dtEfeito": "2025-12-31T00:00:00-03:00",  
    "tpAcordo": "C",  
    "tpAcordoTextoTableLayout": "C - Convenção Coletiva de Trabalho",  
    "descricao": "teste mockoon 123",  
    "sucessaoVinculo": false  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
150

Exclusão de Registro

**Endpoint:** /api/rh/v1/DadosDissidio/1%7C432 **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / IDENTIFICADOR   )**  
  
**Método:** DELETE

**Objetivo:**Excluir um registro já incluido anteriormente

Exemplo de Retorno

**Status Code: 204  No Content**

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150
