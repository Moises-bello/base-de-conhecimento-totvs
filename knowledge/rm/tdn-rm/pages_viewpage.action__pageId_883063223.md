---
content_hash: 2a1ca778be60ea79a74f503a6745fc50e449c93c918f269409b37c0b02f2d305
fetched_at: '2026-06-29T00:12:00.535814+00:00'
page_id: '883063223'
product: rm
source: tdn-rm
title: API - Documentação Técnica - Histórico de Provisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883063223
version: 10
---

Foi criada a API para uso dos produto TOTVS Folha de Pagamento, que será utilizada na nova tela "Histórico de Provisão", desenvolvida em Smart UI. Esta tela oferece novos recursos visuais e funcionais do Histórico de Provisões que já conhecíamos anteriormente.  
Este módulo contém dados relativos às provisões mensais de Férias e 13º salário.

Este documento contém detalhes técnicos sobre os parâmetros, os retornos de cada um e a funcionalidade da API.

### **Informações Técnicas das API's utilizadas**

Schema

**Endpoint:**  /api/rh/v1/HistoricoProvisao/Schema **Método:** GET **Objetivo:**Retornar o Schema utilizado neste endpoint, com propriedades e tipos de dados

Exemplo de Retorno

**{**  
**"title": "Histórico de Provisão",**  
**"version": "1.0",**  
**"identifier": "ProvisionHistory",**  
**"fields": [**  
**{**  
**"layoutDefinition": [**  
**{**  
**"visible": false,**  
**"componentType": "TableLayout"**  
**},**  
**{**  
**"visible": false,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"visible": false,**  
**"componentType": "DetailLayout"**  
**}**  
**],**  
**"key": true,**  
**"property": "codigoColigada",**  
**"label": "Coligada",**  
**"disabled": true,**  
**"type": "string",**  
**"componentType": "Input"**  
**},**  
**{**  
**"quickFilter": true,**  
**"layoutDefinition": [**  
**{**  
**"order": 1,**  
**"componentType": "TableLayout"**  
**},**  
**{**  
**"gridColumns": 2,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 2,**  
**"componentType": "DetailLayout"**  
**}**  
**],**  
**"key": true,**  
**"property": "ano",**  
**"label": "Ano",**  
**"type": "string",**  
**"componentType": "Input"**  
**},**  
**{**  
**"quickFilter": true,**  
**"options": [**  
**{**  
**"value": 1,**  
**"label": "Janeiro"**  
**},**  
**{**  
**"value": 2,**  
**"label": "Fevereiro"**  
**},**  
**{**  
**"value": 3,**  
**"label": "Março"**  
**},**  
**{**  
**"value": 4,**  
**"label": "Abril"**  
**},**  
**{**  
**"value": 5,**  
**"label": "Maio"**  
**},**  
**{**  
**"value": 6,**  
**"label": "Junho"**  
**},**  
**{**  
**"value": 7,**  
**"label": "Julho"**  
**},**  
**{**  
**"value": 8,**  
**"label": "Agosto"**  
**},**  
**{**  
**"value": 9,**  
**"label": "Setembro"**  
**},**  
**{**  
**"value": 10,**  
**"label": "Outubro"**  
**},**  
**{**  
**"value": 11,**  
**"label": "Novembro"**  
**},**  
**{**  
**"value": 12,**  
**"label": "Dezembro"**  
**}**  
**],**  
**"layoutDefinition": [**  
**{**  
**"widthColumnTable": 60,**  
**"componentType": "TableLayout"**  
**},**  
**{**  
**"gridColumns": 2,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 2,**  
**"componentType": "DetailLayout"**  
**}**  
**],**  
**"forceOptionsComponentType": "select",**  
**"key": true,**  
**"property": "mes",**  
**"label": "Mês",**  
**"componentType": "Select"**  
**},**  
**{**  
**"quickFilter": true,**  
**"columns": [**  
**{**  
**"fieldLabel": false,**  
**"label": "Chapa",**  
**"property": "chapa"**  
**},**  
**{**  
**"fieldLabel": false,**  
**"label": "Nome",**  
**"property": "nome"**  
**}**  
**],**  
**"required": true,**  
**"searchService": "/api/rh/v1/chapa",**  
**"format": [**  
**"chapa",**  
**"nome"**  
**],**  
**"fieldLabel": "nome",**  
**"fieldValue": "chapa",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 8,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 8,**  
**"componentType": "DetailLayout"**  
**}**  
**],**  
**"clean": true,**  
**"noAutoComplete": true,**  
**"key": true,**  
**"property": "chapa",**  
**"label": "Funcionário",**  
**"componentType": "Lookup"**  
**},**  
**{**  
**"format": "dd/MM/yyyy",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"divider": "Provisão de Férias",**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"widthColumnTable": 120,**  
**"componentType": "TableLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"divider": "Provisão de Férias",**  
**"componentType": "DetailLayout"**  
**}**  
**],**  
**"property": "dataVencimentoFerias",**  
**"label": "Data de vencimento férias",**  
**"type": "date",**  
**"componentType": "DatePicker"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"locale": "pt-BR",**  
**"property": "valorPagoFeriasMes",**  
**"label": "Valor pago Férias Mês",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "valorProvisaoFeriasEmDobro",**  
**"label": "Valor provisão férias em Dobro",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "avosFeriasVencidos",**  
**"label": "Avos férias vencidos",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "mediasFeriasVencidas",**  
**"label": "Médias férias vencidas",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "valorProvisaoFeriasVencidas",**  
**"label": "Valor provisão férias vencidas",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "avosFeriasProporcionais",**  
**"label": "Avos férias proporcionais",**  
**"type": "decimal",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "mediasFeriasProporcionais",**  
**"label": "Médias férias proporcionais",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "valorProvisaoFeriasProporcionais",**  
**"label": "Valor provisão férias proporcionais",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "valorAbatimentoFerias",**  
**"label": "Valor abatimento férias",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "valorSemAbatimentoFerias",**  
**"label": "Valor sem abatimento férias",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "valorProvisaoFerias",**  
**"label": "Valor provisão férias",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"divider": "Provisão de 13º Salário",**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"divider": "Provisão de 13º Salário",**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "avos13",**  
**"label": "Avos 13º",**  
**"type": "decimal",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "medias13Salario",**  
**"label": "Médias 13º salário",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**},**  
**{**  
**"decimalsLength": 2,**  
**"thousandMaxlength": 6,**  
**"minValue": "0.00",**  
**"layoutDefinition": [**  
**{**  
**"gridColumns": 4,**  
**"componentType": "EditLayout"**  
**},**  
**{**  
**"gridColumns": 4,**  
**"componentType": "DetailLayout"**  
**},**  
**{**  
**"componentType": "TableLayout"**  
**}**  
**],**  
**"property": "valorProvisao13",**  
**"label": "Valor provisão 13º",**  
**"type": "currency",**  
**"componentType": "Decimal"**  
**}**  
**],**  
**"groups": []**  
**}**

Inclusão de Registro

**Endpoint:  /**api/rh/v1/HistoricoProvisao/ **Método:** POST **Objetivo:**Incluir registros no Histórico da provisão de maneira manual, não necessitando do processo de geração de historico de provisão.

Exemplo de requisição

{  
  "codigoColigada": 1,  
  "ano": 2024,  
  "mes": 7,  
  "chapa": "F0002",  
  "dataVencimentoFerias": "2025-02-01T00:00:00-03:00",  
  "valorPagoFeriasMes": 0,  
  "valorProvisaoFeriasEmDobro": 210.46,  
  "avosFeriasVencidos": 24,  
  "mediasFeriasVencidas": 150,  
  "valorProvisaoFeriasVencidas": 960,  
  "avosFeriasProporcionais": 9.85,  
  "mediasFeriasProporcionais": 0,  
  "valorProvisaoFeriasProporcionais": 110.23,  
  "valorAbatimentoFerias": 1083.8,  
  "valorSemAbatimentoFerias": 1083.8,  
  "valorProvisaoFerias": 4400.97,  
  "avos13": 9.9,  
  "medias13Salario": 15.96,  
  "valorProvisao13": 792  
}

Exemplo de Retorno

**Status Code: 201 Created  
  
{**  
**"codigoColigada": 1,**  
**"ano": 2024,**  
**"mes": 7,**  
**"chapa": "F0002",**  
**"dataVencimentoFerias": "2025-02-01T00:00:00-03:00",**  
**"valorPagoFeriasMes": 0.0,**  
**"valorProvisaoFeriasEmDobro": 210.46,**  
**"avosFeriasVencidos": 24.0,**  
**"mediasFeriasVencidas": 150.0,**  
**"valorProvisaoFeriasVencidas": 960.0,**  
**"avosFeriasProporcionais": 9.85,**  
**"mediasFeriasProporcionais": 0.0,**  
**"valorProvisaoFeriasProporcionais": 110.23,**  
**"valorAbatimentoFerias": 1083.8,**  
**"valorSemAbatimentoFerias": 1083.8,**  
**"valorProvisaoFerias": 4400.97,**  
**"avos13": 9.9,**  
**"medias13Salario": 15.96,**  
**"valorProvisao13": 792.0**  
**}**

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Edição de Registro

**Endpoint:** /api/rh/v1/HistoricoProvisao/CODCOLIGADA %7C ANOCOMP %7C MESCOMP %7C  CHAPA **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / ANOCOMP / MESCOMP / CHAPA   )**Exemplo de requisição com Endpoint montado:  
  
/api/rh/v1/HistoricoProvisao/1%7C1998%7C2%7C00004  
  
**Método:** PUT

**Objetivo:**Alterar um registro já incluido anteriormente

Exemplo de requisição

{  
    "codigoColigada": 1,  
    "ano": 1998,  
    "mes": 2,  
    "chapa": "00003",  
    "dataVencimentoFerias": "1997-08-14T00:00:00-03:00",  
    "valorPagoFeriasMes": 0,  
    "valorProvisaoFeriasEmDobro": 15,  
    "avosFeriasVencidos": 12,  
    "mediasFeriasVencidas": 200,  
    "valorProvisaoFeriasVencidas": 0,  
    "avosFeriasProporcionais": 6,  
    "mediasFeriasProporcionais": 0,  
    "valorProvisaoFeriasProporcionais": 0,  
    "valorAbatimentoFerias": 4400.97,  
    "valorSemAbatimentoFerias": 4400.97,  
    "valorProvisaoFerias": 4400.97,  
    "avos13": 2,  
    "medias13Salario": 0,  
    "valorProvisao13": 323.18  
}

Exemplo de Retorno

**Status Code: 200  OK**

**{**  
**"codigoColigada": 1,**  
**"ano": 1998,**  
**"mes": 2,**  
**"chapa": "00003",**  
**"dataVencimentoFerias": "1997-08-14T00:00:00-03:00",**  
**"valorPagoFeriasMes": 0.0,**  
**"valorProvisaoFeriasEmDobro": 15.0,**  
**"avosFeriasVencidos": 12.0,**  
**"mediasFeriasVencidas": 200.0,**  
**"valorProvisaoFeriasVencidas": 0.0,**  
**"avosFeriasProporcionais": 6.0,**  
**"mediasFeriasProporcionais": 0.0,**  
**"valorProvisaoFeriasProporcionais": 0.0,**  
**"valorAbatimentoFerias": 4400.97,**  
**"valorSemAbatimentoFerias": 4400.97,**  
**"valorProvisaoFerias": 4400.97,**  
**"avos13": 2.0,**  
**"medias13Salario": 0.0,**  
**"valorProvisao13": 323.18**  
**}**

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150

Exclusão de Registro

**Endpoint:** /api/rh/v1/HistoricoProvisao/CODCOLIGADA %7C ANOCOMP %7C MESCOMP %7C  CHAPA **( Este end point é dinâmico, onde o que se mantém sempre é %7C e o que sempre se altera são as informações CODCOLIGADA / ANOCOMP / MESCOMP / CHAPA   )**Exemplo de requisição com Endpoint montado:  
  
/api/rh/v1/HistoricoProvisao/1%7C1998%7C2%7C00004  
  
**Método:** DELETE

**Objetivo:**Excluir um registro já incluido anteriormente

Exemplo de Retorno

**Status Code: 204  No Content**

Exemplo de utilização

Para análise rápida, importe a seguinte collection no [Postman](https://www.postman.com/):  
  
150  
  
Para a utilização da collection, podemos utilizar um mock, para melhor visualização da API, basta importar o seguinte arquivo .json, usando a ferramenta [Mockoon](https://mockoon.com/), basta importar o enviroment na ferramenta e iniciar o servidor:  
  
150
