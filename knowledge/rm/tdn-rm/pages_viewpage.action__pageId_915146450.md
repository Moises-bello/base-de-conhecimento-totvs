---
content_hash: 9f3a5860673c38f8fa244cfda3077037d39a884cc8159104a5a825fa37e811ec
fetched_at: '2026-06-29T00:12:06.330936+00:00'
page_id: '915146450'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Consulta Movimento de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=915146450
version: 4
---

Foi criada a API para uso do produto de TOTVS Folha de Pagamento que será utilizada na nova tela "Consulta Movimento de Integração", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais da Consulta Movimento de Integração que já conhecíamos anteriormente.  
Este cadastro contém dados relativos as verbas provenientes das integrações com modulo Folha de Pagamento;

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/MovimentoIntegracao/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

{  
    "title": "Consulta Movimento Integração",  
    "version": "1.0",  
    "identifier": "IntegrationMoviment",  
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
            "layoutDefinition": [  
                {  
                    "order": 1,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "key": true,  
            "property": "chapa",  
            "label": "Matrícula",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "EditLayout"  
                },  
                {  
                    "order": 2,  
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
                    "widthColumnTable": 50,  
                    "order": 3,  
                    "componentType": "TableLayout"  
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
            "layoutDefinition": [  
                {  
                    "widthColumnTable": 50,  
                    "order": 4,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "key": true,  
            "property": "mesComp",  
            "label": "Mês",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "quickFilter": true,  
            "layoutDefinition": [  
                {  
                    "order": 5,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "key": true,  
            "property": "codEvento",  
            "label": "Codigos Eventos",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 6,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "nomeCodEvento",  
            "label": "Eventos",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "key": true,  
            "property": "idMovTemp",  
            "label": "Id Movimento Temp",  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "visible": false,  
                    "componentType": "TableLayout",  
                    "allowColumnsManager": false  
                }  
            ],  
            "property": "hora",  
            "label": "Hora",  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 7,  
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
            "thousandMaxlength": 2,  
            "layoutDefinition": [  
                {  
                    "order": 8,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "ref",  
            "label": "Referências",  
            "type": "decimal",  
            "componentType": "Decimal"  
        },  
        {  
            "decimalsLength": 6,  
            "thousandMaxlength": 2,  
            "minValue": "0.00",  
            "layoutDefinition": [  
                {  
                    "order": 9,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "valor",  
            "label": "Valores",  
            "type": "currency",  
            "componentType": "Decimal"  
        },  
        {  
            "booleanTrue": "Sim",  
            "booleanFalse": "Não",  
            "property": "valorForcado",  
            "label": "Valores Forçados",  
            "type": "boolean",  
            "componentType": "Switch"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "widthColumnTable": 140,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "codCCusto",  
            "label": "Cod. Centro Custo",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "property": "origemEvento",  
            "label": "Codigo Origem Evento",  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 10,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "nomeOrigemEvento",  
            "label": "Origem Evento",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "property": "codUsuario",  
            "label": "Usuário",  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "format": "dd/MM/yyyy",  
            "layoutDefinition": [  
                {  
                    "order": 12,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "dataInclusao",  
            "label": "Datas Inclusão",  
            "type": "date",  
            "componentType": "DatePicker"  
        },  
        {  
            "property": "tipoLancamento",  
            "label": "Id Tipo Lançamento",  
            "visible": false,  
            "type": "string",  
            "componentType": "Input"  
        },  
        {  
            "layoutDefinition": [  
                {  
                    "order": 11,  
                    "componentType": "TableLayout"  
                }  
            ],  
            "property": "nomeTipoLancamento",  
            "label": "Tipo Lançamento",  
            "type": "string",  
            "componentType": "Input"  
        }  
    ],  
    "groups": []  
}

Exclusão de Registro

**Endpoint:  /api/rh/v1/MovimentoIntegracao/1%7C00002%7C2011%7C8%7C0001%7C1175**(Este é um exemplo do End Point onde o " /1%7C00002%7C2011%7C8%7C0001%7C1175 " é variável)  
  
**Apesar de ser variável a construção do End point utiliza o seguinte padrão:**/1%7C00002%7C2011%7C8%7C0001%7C1175  
 **/1%7C = Codigo da Coligada****00002%7C = Chapa do Funcionário****2011%7C  = Ano  
8%7C = Mês  
0001%7C = Código do Evento  
1175 = Id Sequencial  
  
Método:** DELETE **Objetivo:** Excluir registros da Consulta de Movimento de Integração

Exemplo de Retorno

**Status Code: 204 No Content**
