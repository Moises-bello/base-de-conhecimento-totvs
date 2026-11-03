---
content_hash: ede378dabe0f126188a9e3697039d0a58d4c1aec77a8ec9f07ddefe4e13ded9b
fetched_at: '2026-07-02T19:24:26.971665+00:00'
page_id: '654948163'
product: protheus
source: tdn-tec
title: assertTrue
type: documentation
url: https://tdn.totvs.com/display/tec/assertTrue
version: 2
---

Verifica se o resultado do teste é Verdadeiro (.T.).

##### Sintaxe

```
tlpp.probat.assertTrue( < lValue >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertTrue( < lValue >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| lValue | logical | Valor produzido pelo teste | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor lValue é Verdadeiro (.T.). |

##### Observações

* Caso o assertTrue() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertTrue()

  local l1  := .F.  as logical
  local l2  := .T.  as logical

  assertTrue( l1 ) // Erro
  assertTrue( l2 ) // Ok

return .T.
```

##### Abrangência

01.02.10
