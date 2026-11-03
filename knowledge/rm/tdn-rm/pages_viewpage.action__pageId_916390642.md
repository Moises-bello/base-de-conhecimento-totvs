---
content_hash: dd9025bf5e9be86824ed28b9bd16a2b20733e4778e15f78fd0ca014e1a6f83c1
fetched_at: '2026-06-29T00:12:06.449412+00:00'
page_id: '916390642'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Tarifas de Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=916390642
version: 7
---

Foi criada a API para uso dos produtos TOTVS Folha de Pagamento, que será utilizada na nova tela "Tarifas de Vale Transporte", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Tarifas de Vale Transporte, que já conhecíamos anteriormente.  
Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/TarifaTransporte/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Tarifa Transporte",  
    "version": "1.0",  
    "identifier": "TarifaTransporte",  
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
            "mask": "99999",  
            "maskFormatModel": true,  
            "maxLength": 5,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "key": true,  
            "property": "codigo",  
            "label": "Código",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "required": true,  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "key": true,  
            "property": "inicioVigencia",  
            "label": "Início vigência",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "required": true,  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 2,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "finalVigencia",  
            "label": "Final vigência",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "required": true,  
            "maxLength": 30,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 5,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "descricao",  
            "label": "Descrição",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "required": true,  
            "decimalsLength": 2,  
            "thousandMaxlength": 11,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "valor",  
            "label": "Valor",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 9,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "atualizaVigencia",  
            "label": "Atualiza final de vigência na liberação de competência",  
            "type": "boolean",  
            "componentType": "Switch"  
        }  
    ],  
    "groups": []  
}

Inclusão de Registro

**Endpoint:**/api/rh/v1/TarifaTransporte/ **Método:** POST **Objetivo:** Incluir registros na Tarifa de Vale Transporte

Exemplo de Requisição

{  
  "codigo": "123",  
  "inicioVigencia": "2011-01-01",  
  "finalVigencia": "2025-12-31",  
  "descricao": "teste",  
  "valor": 200  
}

Exemplo de Retorno

**Status Code: 201 Created**{    "codColigada": 1,"codigo": "123",   "inicioVigencia": "2011-01-01",  
    "finalVigencia": "2025-12-31",  
    "descricao": "teste",  
    "valor": 200.0,  
    "atualizaVigencia": false,  
    "id": 0}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Edição de Registro

**Endpoint:  /api/rh/v1/TarifaTransporte/1%7C123%7C2011-01-01**(Este é um exemplo do End Point onde o " 1%7C123%7C2011-01-01 " é variável)  
  
**Apesar de ser variável a construção do End point utiliza o seguinte padrão:**1%7C123%7C2011-01-01  
 **/1%7C = Codigo da Coligada****123%7C = Codigo da Tarifa****2011-01-01  = Ano / Mes / Dia  
  
  
Método:** PUT **Objetivo:** Edita registros da Tarifa de Transporte

Exemplo de Requisição

 {  
  "codColigada": 1,  
  "codigo": "123",  
  "inicioVigencia": "2011-01-01",  
  "finalVigencia": "2025-12-31",  
  "descricao": "teste update",  
  "valor": 200,  
  "atualizaVigencia": false,  
  "id": 310,  
  "links": [  
    {  
      "relation": "Vales",  
      "apiMetaData": "api/rh/v1/LinhaValeTransporte/schema",  
      "apiData": "api/rh/v1/LinhaValeTransporte/",  
      "apiDataFilter": "?$filter=codColigada eq 1 and codTarifa eq '123'",  
      "type": "RelatedItems",  
      "label": "Vale Transporte",  
      "mapper": {  
        "codTarifa": "123"  
      }  
    }  
  ]  
}

Exemplo de Retorno

**Status Code: 200 OK**{  
    "codColigada": 1,  
    "codigo": "123",  
    "inicioVigencia": "2011-01-01",  
    "finalVigencia": "2025-12-31",  
    "descricao": "teste update",  
    "valor": 200.0,  
    "atualizaVigencia": false,  
    "id": 310  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
150

Exclusão de Registro

**Endpoint:  /api/rh/v1/TarifaTransporte/1%7C123%7C2011-01-01**(Este é um exemplo do End Point onde o " 1%7C123%7C2011-01-01 " é variável)  
  
**Apesar de ser variável a construção do End point utiliza o seguinte padrão:**1%7C123%7C2011-01-01  
 **/1%7C = Codigo da Coligada****123%7C = Codigo da Tarifa****2011-01-01  = Ano / Mes / Dia  
  
  
Método:** DELETE **Objetivo:** Excluir registros da Tarifa de Transporte

Exemplo de Retorno

**Status Code: 204 No Content**
