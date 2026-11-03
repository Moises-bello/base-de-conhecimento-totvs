---
content_hash: 8fc2823d3cd903f38fe97f512ace3c08bd5be4acdea743e6faca2bdd8044f249
fetched_at: '2026-06-29T00:11:32.247904+00:00'
page_id: '745750165'
product: rm
source: tdn-rm
title: Relação de API's Dimensões Contábeis - Documento técnico (conteúdo Interno)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745750165
version: 7
---

### Cadastro de dimensões contábeis (CDIMENSAO)

##### [URL: http://localhost:8051/api/ctb/v1/accountingDimensions](http://localhost:8051/api/ctb/v1/accountingDimensions)jbh Body:

{  
    "companyId": 1,  
    "dimensionsId": 1,  
    "description": "Dimensão cli/for",  
    "entity": "FCFO",  
    "apportionment": true,  
    "dynamicTableApplication": "C",  
    "dynamicTableCode": "POLO",  
    "dynamicTableCompanyId": 1  
}

##### GET

Obrigatório: Informar nos parâmetros da requisição Coligada e Id Dimensão (separados por pipe).  
exemplo: <http://localhost:8051/api/ctb/v1/accountingDimensions/1|2>

##### GET ALL

Opcional: Caso necessário podem ser informados filtros separados por & na requisição  
exemplo: <http://localhost:8051/api/ctb/v1/accountingDimensions?companyid=1>

##### POST

Informar o body da requisição conforme especificado.

Regras:

1. A entidade deve ser obrigatoriamente, alguma que esteja disponível na tabela CDIMENSAOENTIDADE
2. Caso entidade seja TABELADINAMICA, os campos relacionados são obrigatórios.
3. Caso dimensão seja global, obrigatoriamente a da tabela dinâmica (caso informada) deve ser global.
4. Não insere registro duplicado.

##### PATCH

Altera apenas a descrição da dimensão, qualquer informação a mais no body será desconsiderada.

Obrigatório:

1. Informar nos parâmetros da requisição Coligada e Id Dimensão (separados por pipe).
2. Informar no body da requisição apenas a descrição.

Regra: Descrição deve ser preenchida.

##### DELETE

Obrigatório: Informar nos parâmetros na requisição Coligada e Id Dimensão (separados por pipe).  
exemplo: <http://localhost:8051/api/ctb/v1/accountingDimensions/1|2>

Regra: Não deleta dimensão contábil que esteja sendo utilizada.

---

### Entidades das dimensões contábeis (CDIMENSAOENTIDADE) - exclusiva para consulta

#### URL: <http://localhost:8051/api/ctb/v1/accountingDimensionEntities>

Body:

{  
            "entity": "FCFO",  
            "relatedEntity": "CDIMENSAOFCFO",  
            "description": "Cliente/Fornecedor",  
            "apportionmentAllow": true,  
            "globalAllow": true,  
            "pkEntity": "CODCOLIGADA;CODCFO"  
        },

##### GET

Obrigatório: Informar no parâmetro da requisição a entidade (campo entity)  
exemplo: <http://localhost:8051/api/ctb/v1/accountingDimensionEntities/FCFO>FC

##### GET ALL

Opcional: Caso necessário podem ser informados filtros separados por & na requisição  
exemplo: <http://localhost:8051/api/ctb/v1/accountingDimensionEntities?globalAllow=true>
