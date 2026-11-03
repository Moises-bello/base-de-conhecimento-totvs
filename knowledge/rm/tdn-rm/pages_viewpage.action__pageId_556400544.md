---
content_hash: 1e48fe20fe64e473a2eb7281630ee1738678b62b0ba3ddbcf8f0c12f86bf2b2e
fetched_at: '2026-06-29T00:10:46.990364+00:00'
page_id: '556400544'
product: rm
source: tdn-rm
title: API (Filiais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556400544
version: 7
---

## **CONTEÚDO**

1. **Visão Geral**

Possibilitar a integração do Cadastro de Filiais RM via API (rest)

Para isso devemos seguir o contrato abaixo:

[https://api.totvs.com.br/apidetails/Branch\_v1\_000.json](https://api.totvs.com.br/apidetails/Branch_v1_000.json "Follow link")

1. **Tabela utilizada**

**GFILIAL**

## **01. VISÃO GERAL**

Implementação REST: GET, POST, PATCH, PUT

Obs:

Quando executado o método GET ALL o registros sempre virão ordenados por Código da Coligada e Código da Filial.

O método DELETE não foi implementado por questão de regras Segurança.

**Mapeamento dos Campos**

|  |  |  |
| --- | --- | --- |
| API | RM | Observação |
| BranchInternalId | GFILIAL.CODCOLIGADA | GFILIAL.CODFILIAL | campo calculado |
| CompanyCode | GFILIAL.CODCOLIGADA |  |
| Description | GFILIAL.NOME |  |
| Code | GFILIAL.CODFILIAL |  |
| Title | GFILIAL.NOMEFANTASIA |  |
| CGC | GFILIAL.CGC |  |
| StateRegistration | GFILIAL.INSCRICAOESTADUAL |  |
| DDD | GFILIAL.DDD |  |
| Phone | GFILIAL.TELEFONE |  |
| Street | GFILIAL.RUA |  |
| Complement | GFILIAL.COMPLEMENTO |  |
| Neighborhood | GFILIAL.BAIRRO |  |
| State | GFILIAL.ESTADO |  |
| City | GMUNICIPIO.NOMEMUNICIPIO |  |
| ZipCode | GFILIAL.CEP |  |
| CityCode | GFILIAL.CODMUNICIPIO |  |
| CNAECode | GFILIAL.CODATIVFED |  |
| NIRE | GFILIAL.NUMREGJUNTA |  |
| DTRE | GFILIAL.DATAREGJUNTA |  |
| Suframa | GFILIAL.SUFRAMA |  |

## **02. EXEMPLO DE UTILIZAÇÃO**

URL Exemplo: [http://localhost:8051/api/framework/v1/Branches/](http://localhost:8051/api/fiscal/v1/branches/)

Exemplo JSON:

{  
"CompanyCode": 8,  
"Code": 3,  
"Title": "Filial 3 Fantasia",  
"CGC": "64.667.260/0001-06",  
"Description": "Filial 3 Nome",  
"StateRegistration": "853/5905845",  
"DDD": "31",  
"Phone": "35952912",  
"Street": "Siqueira Campos",  
"Complement": "Complemento 123",  
"Neighborhood": "Centro",  
"State": "RS",  
"ZipCode": "90010-907",  
"CityCode": "14902",  
"CNAECode": "12345",  
"NIRE": "30121970",  
"DTRE": "2020-01-01T00:00:00",  
"Suframa": "1544787",  
"City": "Porto Alegre",  
"BranchInternalId": "8|3"  
}

Exemplo de utilização com Postman:
