---
content_hash: 9240f60b1b6e50e29ed3f85fdf91ace081c86652d49e13e96ceb5c23d9b885ab
fetched_at: '2026-07-02T19:24:26.917810+00:00'
page_id: '654948093'
product: protheus
source: tdn-tec
title: assertIsRegExFull
type: documentation
url: https://tdn.totvs.com/display/tec/assertIsRegExFull
version: 2
---

Verifica se o valor produzido pelo teste coincide em sua totalidade com a expressão regular informada.

##### Sintaxe

```
tlpp.probat.assertIsRegExFull( < cValue >, < cPattern >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertIsRegExFull( < cValue >, < cPattern >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cValue | character | Valor produzido pelo teste | X |  |
| cPattern | character | Pattern da expressão regular que valida todo o conteúdo de "cValue" | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor coincide totalmente com a expressão regular. |

##### Observações

* Caso o assertIsRegExFull() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertIsRegExFull()

  assertIsRegExFull( "So tem letras", "[A-Za-z ]+" ) // Ok
  assertIsRegExFull( "Tem 1 numero" , "[A-Za-z ]+" ) // Erro

return .T.
```

##### Abrangência

01.02.10
