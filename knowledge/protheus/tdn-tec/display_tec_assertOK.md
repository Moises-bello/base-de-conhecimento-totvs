---
content_hash: 304aa5da6f078e3bcef6800c11729bfb5e3b5c07307bbbdfe857d414d32ee7aa
fetched_at: '2026-07-02T19:24:26.966090+00:00'
page_id: '654948161'
product: protheus
source: tdn-tec
title: assertOK
type: documentation
url: https://tdn.totvs.com/display/tec/assertOK
version: 2
---

Causa um resultado OK de forma deliberada.

##### Sintaxe

```
tlpp.probat.assertOK( < cMessage > )
```

ou

```
using namespace tlpp.probat

assertOK( < cMessage > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cMessage | character | Mensagem de OK customizada | X |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Sempre irá retornar verdadeiro (.T.). |

##### Observações

* Caso o assertOK() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertOK()

  local n1 := 1 as numeric

  if ( valtype( n1 ) == 'N' )
    assertOK( "valid type for variable n1" )
  endif

return .T.
```

##### Abrangência

01.02.10
