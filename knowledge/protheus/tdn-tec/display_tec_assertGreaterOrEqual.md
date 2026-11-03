---
content_hash: cef8fcc0a1be3bafa93deddd4be0319ef66820943d577a56b8d75b5df9d35b5d
fetched_at: '2026-07-02T19:24:26.905030+00:00'
page_id: '654948088'
product: protheus
source: tdn-tec
title: assertGreaterOrEqual
type: documentation
url: https://tdn.totvs.com/display/tec/assertGreaterOrEqual
version: 2
---

Verifica se o resultado do teste é MAIOR OU IGUAL ao de um valor esperado.

##### Sintaxe

```
tlpp.probat.assertGreaterOrEqual( < xValue >, < xLess >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertGreaterOrEqual( < xValue >, < xLess >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xValue | variant | Valor produzido pelo teste | X |  |
| xLess | variant | Valor utilizado na comparação (xValue >= xLess) | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor xValue é maior ou igual que xLess. |

##### Observações

* Caso o assertGreaterOrEqual() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertGreaterOrEqual()

  local n1  := 10   as numeric
  local n2  := 10   as numeric
  local n3  := 11   as numeric

  assertGreaterOrEqual( n1, n2 ) // Ok
  assertGreaterOrEqual( n1, n3 ) // Erro
  assertGreaterOrEqual( n3, n1 ) // Ok

return .T.
```

##### Abrangência

01.02.10
