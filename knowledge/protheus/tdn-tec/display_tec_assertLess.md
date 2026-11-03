---
content_hash: e687cc0899dd4cbdd90aec558b79093b9f9f9d39e544c169269c45328288f03f
fetched_at: '2026-07-02T19:24:26.940043+00:00'
page_id: '654948101'
product: protheus
source: tdn-tec
title: assertLess
type: documentation
url: https://tdn.totvs.com/display/tec/assertLess
version: 2
---

Verifica se o resultado do teste é MENOR ao de um valor esperado.

##### Sintaxe

```
tlpp.probat.assertLess( < xValue >, < xGreater >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertLess( < xValue >, < xGreater >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xValue | variant | Valor produzido pelo teste | X |  |
| xGreater | variant | Valor utilizado na comparação (xValue < xGreater) | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor xValue é menor que xGreater. |

##### Observações

* Caso o assertLess() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertLess()

  local n1  := 10   as numeric
  local n2  := 11   as numeric
  local n3  := 10   as numeric

  assertLess( n1, n2 ) // Ok
  assertLess( n2, n1 ) // Erro
  assertLess( n1, n3 ) // Erro

return .T.
```

##### Abrangência

01.02.10
