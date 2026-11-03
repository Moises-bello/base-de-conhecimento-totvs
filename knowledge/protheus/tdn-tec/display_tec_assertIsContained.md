---
content_hash: 34a6ff68131ee8deea518b44a508a82c96a5d574e49beeb362cf7da7803d1db3
fetched_at: '2026-07-02T19:24:26.911678+00:00'
page_id: '654948090'
product: protheus
source: tdn-tec
title: assertIsContained
type: documentation
url: https://tdn.totvs.com/display/tec/assertIsContained
version: 2
---

Verifica se o valor produzido (string) pelo teste contém uma string determinada.

##### Sintaxe

```
tlpp.probat.assertIsContained( < cValue >, < cExpected >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertIsContained( < cValue >, < cExpected >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cValue | character | Valor produzido pelo teste | X |  |
| cExpected | character | Valor que deve estar contido em "cValue" | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Retorna o resultado de ( cExpected $ cValue ) |

##### Observações

* Caso o assertIsContained() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertIsContained()

  local c1        := "the value is correct"   as character
  local c2        := "the value is invalid"   as character
  local cExpected := "invalid"                as character

  assertIsContained( c1, cExpected ) // Erro
  assertIsContained( c2, cExpected ) // Ok

return .T.
```

##### Abrangência

01.02.10
