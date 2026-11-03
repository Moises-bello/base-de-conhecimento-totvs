---
content_hash: 8ad710317e5de7a5590610ce4f6898d3cc549931a26fce2247a6fe4ee6dffadb
fetched_at: '2026-07-02T19:24:27.980113+00:00'
page_id: '701668828'
product: protheus
source: tdn-tec
title: oRest:setLastChunkedResponse
type: documentation
url: https://tdn.totvs.com/display/tec/oRest%3AsetLastChunkedResponse
version: 3
---

Deve ser utilizado para informar que o ultimo chunk (pedaço) do corpo(body) da resposta da requisicao está sendo enviado setando no header a chave 'Content-Length: 0'

##### Sintaxe

 )]]>

##### 

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cMessage | string | Conteudo COMPACTADO do ultimo corpo(Body) da resposta da requisição que anteriormente já foi enviado em Chunked. | X |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Indica se o método foi executado(.T.) ou (.F.) caso tenha ocorrido algum problema |

##### Observações

* Para visualizar um exemplo completo do funcionamento do Chunked do REST TLPP, visite a documentação completa:

##### Abrangência 01/2020
