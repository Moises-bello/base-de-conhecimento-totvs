---
content_hash: 5a37c43d8ae0b8596b455fe90f9ed96b8c0729f198f086c7e0ebc8385e66e8fa
fetched_at: '2026-07-02T19:24:26.880442+00:00'
page_id: '654948076'
product: protheus
source: tdn-tec
title: assertEquals
type: documentation
url: https://tdn.totvs.com/display/tec/assertEquals
version: 3
---

Verifica se o resultado do teste é IGUAL ao de um valor esperado.

##### Sintaxe

```
tlpp.probat.assertEquals( < xValue >, < xExpected >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertEquals( < xValue >, < xExpected >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xValue | variant | Valor produzido pelo teste | X |  |
| xExpected | variant | Valor esperado | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se os valores xValue e xExpected são iguais. |

##### Observações

* Caso o assertEquals() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertEquals()

  local n1  := 10   as numeric
  local n2  := 10   as numeric
  local n3  := 11   as numeric

  assertEquals( n1, n2 ) // Ok
  assertEquals( n1, n3 ) // Erro

return .T.
```

##### Abrangência

01.02.10
