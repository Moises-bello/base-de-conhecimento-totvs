---
content_hash: a2a948fc2fd474412788ca3e41c1e476c0ce052f41c4e1ea4946dbfbf4fc385b
fetched_at: '2026-06-29T00:12:06.470417+00:00'
page_id: '916390987'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Valores Fixos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=916390987
version: 3
---

Foi criada a API para uso dos produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Valores Fixos", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais dos Valores Fixos que já conhecíamos anteriormente.  
Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/FixedValues/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Valores Fixo",  
    "version": "1.0",  
    "identifier": "FixedValue",  
    "fields": [  
        {  
            "quickFilter": true,  
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
            "property": "codigo",  
            "label": "Código",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "required": true,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 4,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "nome",  
            "label": "Nome",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "required": true,  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "key": true,  
            "property": "inicioVigencia",  
            "label": "Início de Vigência",  
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
            "property": "finalVigencia",  
            "label": "Final de Vigência",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "decimalsLength": 4,  
            "thousandMaxlength": 12,  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
                    "componentType": "EditLayout"  
                }  
            ],  
            "property": "valor",  
            "label": "Valor",  
            "type": "decimal",  
            "componentType": "Decimal"  
        },  
        {  
            "quickFilter": true,  
            "options": [  
                {  
                    "value": 0,  
                    "label": "Sem finalidade específica."  
                },  
                {  
                    "value": 1,  
                    "label": "Limite salário família."  
                },  
                {  
                    "value": 2,  
                    "label": "Valor salário família abaixo do limite."  
                },  
                {  
                    "value": 3,  
                    "label": "Valor salário família acima do limite."  
                },  
                {  
                    "value": 4,  
                    "label": "Valor a deduzir de IRRF por dependente."  
                },  
                {  
                    "value": 5,  
                    "label": "Desconto mínimo do IRRF."  
                },  
                {  
                    "value": 6,  
                    "label": "Valor a deduzir para funcionário maior de 65 anos."  
                },  
                {  
                    "value": 7,  
                    "label": "Valor do salário mínimo."  
                },  
                {  
                    "value": 8,  
                    "label": "Desconto mínimo de IRRF 13o salário."  
                },  
                {  
                    "value": 9,  
                    "label": "Teto para pagamento do salário família."  
                },  
                {  
                    "value": 10,  
                    "label": "Limite para desconto de salário Maternidade em GRPS."  
                },  
                {  
                    "value": 11,  
                    "label": "Taxa CPMF para salário família."  
                },  
                {  
                    "value": 12,  
                    "label": "Valor mínimo para recolhimento da GPS."  
                },  
                {  
                    "value": 13,  
                    "label": "Alíquota FAP."  
                },  
                {  
                    "value": 14,  
                    "label": "Valor a deduzir no IRRF simplificado."  
                },  
                {  
                    "value": 15,  
                    "label": "Aliquota da reoneração gradual  da folha."  
                }  
            ],  
            "layoutDefinition": [  
                {  
                    "gridColumns": 6,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                }  
            ],  
            "forceOptionsComponentType": "select",  
            "property": "finalidade",  
            "label": "Finalidade",  
            "componentType": "Select"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "widthColumnTable": 150,  
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
            "property": "nomeFinalidade",  
            "label": "Finalidade",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "required": true,  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "layoutDefinition": [  
                {  
                    "gridColumns": 3,  
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

**Endpoint:**/api/rh/v1/FixedValues/ **Método:** POST **Objetivo:** Incluir registros da Consulta de Movimento de Integração

Exemplo de Requisição

 {  
  "codigo": "NEWF",  
  "nome": "NOVO VALOR FIXO",  
  "inicioVigencia": "2001-01-01",  
  "finalVigencia": "2025-12-31",  
  "valor": 350,  
  "finalidade": 0  
}

Exemplo de Retorno

**Status Code: 201 Created**{  
    "codColigada": 1,  
    "codigo": "NEWF",  
    "nome": "NOVO VALOR FIXO",  
    "inicioVigencia": "2001-01-01",  
    "finalVigencia": "2025-12-31",  
    "valor": 350.0,  
    "finalidade": 0,  
    "atualizaVigencia": false  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Edição de Registro

**Endpoint:  /api/rh/v1/FixedValues/1%7CNEWF%7C2001-01-01**(Este é um exemplo do End Point onde o " 1%7CNEWF%7C2001-01-01  " é variável)  
  
**Apesar de ser variável a construção do End point utiliza o seguinte padrão:**1%7CNEWF%7C2001-01-01   
 **/1%7C = Codigo da Coligada****NEWF%7C= Codigo do Valor Fixo****2011-01-01  = Ano / Mes / Dia  
  
  
Método:** PUT **Objetivo:** Edita registros dos Valores Fixos

Exemplo de Requisição

{  
  "codColigada": 1,  
  "codigo": "NEWF",  
  "nome": "NOVO VALOR FIXO",  
  "inicioVigencia": "2001-01-01",  
  "finalVigencia": "2025-12-31",  
  "valor": 352,  
  "finalidade": 0,  
  "nomeFinalidade": "Sem finalidade específica.",  
  "atualizaVigencia": false  
}

Exemplo de Retorno

**Status Code: 200 OK**{  
    "codColigada": 1,  
    "codigo": "NEWF",  
    "nome": "NOVO VALOR FIXO",  
    "inicioVigencia": "2001-01-01",  
    "finalVigencia": "2025-12-31",  
    "valor": 352.0,  
    "finalidade": 0,  
    "nomeFinalidade": "Sem finalidade específica.",  
    "atualizaVigencia": false  
}

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Exclusão de Registro

**Endpoint:  /api/rh/v1/FixedValues/1%7CNEWF%7C2001-01-01** (Este é um exemplo do End Point onde o " 1%7CNEWF%7C2001-01-01  " é variável)Apesar de ser variável a construção do End point utiliza o seguinte padrão: **1%7CNEWF%7C2001-01-01   
   
/1%7C =** Codigo da Coligada **NEWF%7C=** Codigo do Valor Fixo **2011-01-01  =** Ano / Mes / Dia **Método:** DELETE **Objetivo:** Excluir registros dos Valores Fixos

Exemplo de Retorno

**Status Code: 204 No Content**
