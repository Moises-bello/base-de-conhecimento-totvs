---
content_hash: 17d2ea216cff77c0a25b4c2b4cfc523270373b6291e2e0222a22ddc0b0fe5ee0
fetched_at: '2026-07-02T19:24:26.925142+00:00'
page_id: '654948097'
product: protheus
source: tdn-tec
title: assertIsRegExPartial
type: documentation
url: https://tdn.totvs.com/display/tec/assertIsRegExPartial
version: 2
---

Verifica se o valor produzido pelo teste coincide em parte com a expressão regular.

##### Sintaxe

```
tlpp.probat.assertIsRegExPartial( < cValue >, < cPattern >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertIsRegExPartial( < cValue >, < cPattern >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cValue | character | Valor produzido pelo teste | X |  |
| cPattern | character | Pattern da expressão regular que valida o conteúdo de "cValue" | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor coincide parcialmente com a expressão regular. |

##### Observações

* Caso o assertIsRegExPartial() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertIsRegExPartial()

  assertIsRegExPartial( "123 tem letras e numeros 456 tambem", "[A-Za-z ]+" ) // OK
  assertIsRegExPartial( "So tem letras"                      , "[0-9]+"     ) // Erro

return .T.
```

##### Abrangência

01.02.10
