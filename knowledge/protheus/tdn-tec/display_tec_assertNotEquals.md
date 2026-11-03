---
content_hash: 5c67918979d74d8b31f01b83e11c74d3902e77289c34828455ee0183af9d9d2d
fetched_at: '2026-07-02T19:24:26.960467+00:00'
page_id: '654948109'
product: protheus
source: tdn-tec
title: assertNotEquals
type: documentation
url: https://tdn.totvs.com/display/tec/assertNotEquals
version: 2
---

Verifica se o resultado do teste é DIFERENTE ao de um valor informado.

##### Sintaxe

```
tlpp.probat.assertNotEquals( < xValue >, < xExpected >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertNotEquals( < xValue >, < xExpected >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xValue | variant | Valor produzido pelo teste | X |  |
| xExpected | variant | Valor não esperado | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se os valores xValue e xExpected são diferentes. |

##### Observações

* Caso o assertNotEquals() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertNotEquals()

  local n1  := 10   as numeric
  local n2  := 10   as numeric
  local n3  := 11   as numeric

  assertNotEquals( n1, n2 ) // Erro
  assertNotEquals( n1, n3 ) // Ok

return .T.
```

##### Abrangência

01.02.10
