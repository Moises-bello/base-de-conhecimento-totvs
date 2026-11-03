---
content_hash: 4af14e945535c6a7a743ae6fcc712df241baf69c58ba7591a243ea016178aae8
fetched_at: '2026-06-29T00:05:47.804916+00:00'
page_id: '1017446360'
product: rm
source: tdn-rm
title: API de DataServer
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+DataServer
version: 3
---

Exemplos de uso de api de dataserver

Verbo: Get

Ação: Com filtro

URI: **<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData?filter=> ["nome like :nome and CPFCNPJ = :cpf", "%teste%", "044.266.846-50"]**

Verbo: Get

Ação: Primary Key

URI: **<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/2>**

Verbo: Get

Ação: Primary Key Composta

URI: [http://localhost:8051/rmsrestdataserver/rest/FinCFODataBR/1$\_$C100338](http://localhost:8051/rmsrestdataserver/rest/FinCFODataBR/0$_$01;C100338)

Verbo: POST

Ação: Somente para inserir

URI: **<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData>**

[

    {

        "ID":-1,

         "NOME": "teste api 5",

         "CPFCNPJ": "044.266.846-50",

         "TIPO": 0,

         "TIPOPESSOA": 0,

         "DATAHORACADASTRO":"2022-10-27T11:09:58.52-03:00",

         "INSCRICAOESTADUAL":" ",

         "CONJUGE\_PROFISSAO\_ID": 1,

         "LEAD": 0,

         "LEAD\_POTENCIAL": 0

    }

]

Verbo: DELETE

Ação: Deletar o registro com a primary key

URI:

**<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/2>**

Verbo: PUT

Ação: Atualiza todos os registros, a lib faz o merge de todos os campos

URI:

**<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/2>**

{

         "ID": 2,

         "NOME": "teste api PUT",

         "CPFCNPJ": "044.266.846-50",

         "TIPO": 0,

         "TIPOPESSOA": 0,

         "DATAHORACADASTRO":"2022-10-27T11:09:58.52-03:00",

         "INSCRICAOESTADUAL":" ",

         "CONJUGE\_PROFISSAO\_ID": 1,

         "LEAD": 0,

         "LEAD\_POTENCIAL": 0

    }

Verbo: PATCH

Ação: Atualiza alguns campos dos registros, a lib faz o merge somente dos campos enviados

URI:

**<http://localhost:8051/rmsrestdataserver/rest/ImbPVIClienteData/2>**

    {

         "NOME": "teste api patch"

    }

Demais exemplos segue a documentação da lib: [Serviços RESTful de DataServer no RM](https://tdn.totvs.com/pages/releaseview.action?pageId=190515801)
