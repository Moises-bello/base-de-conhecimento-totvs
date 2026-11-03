---
content_hash: 52f035492b46a0fb4808cc4ee98b3beade0ce1e8829050e5e71280cee4a34e24
fetched_at: '2026-06-29T00:10:46.919363+00:00'
page_id: '556389626'
product: rm
source: tdn-rm
title: FISCAL01-13177 DT API RM Cadastro de Filiais
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-13177+DT+API+RM+Cadastro+de+Filiais
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Api Cadastrod e Filiais |

## **02. SITUAÇÃO/REQUISITO**

Para possibilitarmos a integração do Backoffice RM com o Master CRM, precisamos implementar a API do Cadastro de Filial (dados globais).

Para isso devemos seguir o contrato abaixo:

[https://api.totvs.com.br/apidetails/Branch\_v1\_000.json](https://api.totvs.com.br/apidetails/Branch_v1_000.json "Follow link")

## **03. SOLUÇÃO**

Implementação da API de Filiais conforme orientação: <https://api.totvs.com.br/apidetails/Branch_v1_000.json>

Implementação REST: GET, POST, PATCH, PUT

URL Exemplo: <http://localhost:8051/api/fiscal/v1/branches/>

Obs: Quando executado o método GET ALL o registros sempre virão ordenados por Código da Coligada e Código da Filial.

Mapeamento dos Campos

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
| City | GMUNICIPIONOMEMUNICIPIO |  |
| ZipCode | GFILIAL.CEP |  |
| CityCode | GFILIAL.CODMUNICIPIO |  |
| CNAECode | GFILIAL.CODATIVFED |  |
| NIRE | GFILIAL.NUMREGJUNTA |  |
| DTRE | GFILIAL.DATAREGJUNTA |  |
| Suframa | GFILIAL.SUFRAMA |  |

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
