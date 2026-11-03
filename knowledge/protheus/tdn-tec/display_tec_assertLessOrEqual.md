---
content_hash: 8fee000ee9406649d88a01796167a672822dbb44fbb29e44b229a452c43d014b
fetched_at: '2026-07-02T19:24:26.946946+00:00'
page_id: '654948104'
product: protheus
source: tdn-tec
title: assertLessOrEqual
type: documentation
url: https://tdn.totvs.com/display/tec/assertLessOrEqual
version: 2
---

Verifica se o resultado do teste é MENOR OU IGUAL ao de um valor esperado.

##### Sintaxe

```
tlpp.probat.assertLessOrEqual( < xValue >, < xGreater >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertLessOrEqual( < xValue >, < xGreater >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xValue | variant | Valor produzido pelo teste | X |  |
| xGreater | variant | Valor utilizado na comparação (xValue <= xGreater) | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor xValue é menor ou igual que xGreater. |

##### Observações

* Caso o assertLessOrEqual() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertLessOrEqual()

  local n1  := 10   as numeric
  local n2  := 11   as numeric
  local n3  := 10   as numeric

  assertLessOrEqual( n1, n2 ) // Ok
  assertLessOrEqual( n2, n1 ) // Erro
  assertLessOrEqual( n1, n3 ) // Ok

return .T.
```

##### Abrangência

01.02.10
