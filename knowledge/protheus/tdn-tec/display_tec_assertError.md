---
content_hash: 8cffb9e53fb0f7a14db94e3907283ed177f7815ae8408dcbd74d072e5bbcd4dc
fetched_at: '2026-07-02T19:24:26.886304+00:00'
page_id: '654948080'
product: protheus
source: tdn-tec
title: assertError
type: documentation
url: https://tdn.totvs.com/display/tec/assertError
version: 2
---

Causa um resultado de ERRO de forma deliberada.

##### Sintaxe

```
tlpp.probat.assertError( < cError >, [ cDesc ], [ xValue ] )
```

ou

```
using namespace tlpp.probat

assertError( < cError >, [ cDesc ], [ xValue ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cError | character | Mensagem de erro customizada | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |
| xValue | variante | Valor produzido pelo teste (opcional), caso haja a necessidade de manter histórico |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Sempre irá retornar falso (.F.). |

##### Observações

* Caso o assertError() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertError()

  local n1 := 1 as numeric

  if ( valtype( n1 ) <> 'N' )
    assertError( "invalid type for variable n1" )
  endif

return .T.
```

##### Abrangência

01.02.10
