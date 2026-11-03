---
content_hash: 71257b81fad8e4e956e9f21af0f694adcc6d53f8268769d9886c7ff717227f34
fetched_at: '2026-07-02T19:24:26.898663+00:00'
page_id: '654948086'
product: protheus
source: tdn-tec
title: assertGreater
type: documentation
url: https://tdn.totvs.com/display/tec/assertGreater
version: 2
---

Verifica se o resultado do teste é MAIOR ao de um valor esperado.

##### Sintaxe

```
tlpp.probat.assertGreater( < xValue >, < xLess >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertGreater( < xValue >, < xLess >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xValue | variant | Valor produzido pelo teste | X |  |
| xLess | variant | Valor utilizado na comparação (xValue > xLess) | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor xValue é maior que xLess. |

##### Observações

* Caso o assertGreater() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertGreater()

  local n1  := 10   as numeric
  local n2  := 11   as numeric

  assertGreater( n1, n2 ) // Erro
  assertGreater( n2, n1 ) // Ok

return .T.
```

##### Abrangência

01.02.10
