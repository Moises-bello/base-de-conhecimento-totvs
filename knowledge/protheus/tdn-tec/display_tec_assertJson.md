---
content_hash: ee392c10cf9cf21af935a265f175a91176085a7c0abe217e81544df24f7eb3a2
fetched_at: '2026-07-02T19:24:26.933815+00:00'
page_id: '654948099'
product: protheus
source: tdn-tec
title: assertJson
type: documentation
url: https://tdn.totvs.com/display/tec/assertJson
version: 2
---

Verifica se o resultado do teste em Json é IGUAL ao de um json esperado.

##### Sintaxe

```
tlpp.probat.assertJson( < xValue >, < xExpected >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertJson( < xValue >, < xExpected >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| jValue | json | Valor produzido pelo teste | X |  |
| xExpected | json ou character | Valor esperado | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se os valores jValue e xExpected são iguais. |

##### Observações

* Caso o assertJson() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
# include "tlpp-core.th"
# include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertJson()

  local oJson1     as json
  local oJson2     as json
  local oJson3     as json
  local cJson1     as character
  local cJson2     as character
  local cJson3     as character

  cJson1 := '{"key":"value"}'
  cJson2 := cJson1
  cJson3 := '{"key":"value_1"}'

  oJson1 := JsonObject():New()
    oJson1:fromJson( cJson1 )

  oJson2 := JsonObject():New()
    oJson2:fromJson( cJson2 )

  oJson3 := JsonObject():New()
    oJson3:fromJson( cJson3 )

  assertJson( oJson1, oJson2 ) // Ok
  assertJson( oJson1, oJson3 ) // Erro
  assertJson( oJson1, cJson2 ) // Ok
  assertJson( oJson1, cJson3 ) // Erro

return .T.
```

##### Abrangência

01.02.10
