---
content_hash: 3d4a433fa676ae697c8239ba8064f62100cd66fa126951e0ba601d3a9efcf9b1
fetched_at: '2026-07-02T19:24:26.952902+00:00'
page_id: '654948107'
product: protheus
source: tdn-tec
title: assertNil
type: documentation
url: https://tdn.totvs.com/display/tec/assertNil
version: 2
---

Verifica se o resultado do teste é Nil (Nulo).

##### Sintaxe

```
tlpp.probat.assertNil( < xValue >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertNil( < xValue >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xValue | variant | Valor produzido pelo teste | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor xValue é Nil (Nulo). |

##### Observações

* Caso o assertNil() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertNil()

  local u1
  local n2  := 11     as numeric
  local c3  := 'abc'  as character

  assertNil( u1 ) // Ok
  assertNil( n2 ) // Erro
  assertNil( c3 ) // Erro

return .T.
```

##### Abrangência

01.02.10
