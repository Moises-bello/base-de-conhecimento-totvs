---
content_hash: 64fb68a323269659c685b767ff501a1fba31f22e66a3634653f344cfd28ca101
fetched_at: '2026-07-02T19:24:26.892233+00:00'
page_id: '654948084'
product: protheus
source: tdn-tec
title: assertFalse
type: documentation
url: https://tdn.totvs.com/display/tec/assertFalse
version: 2
---

Verifica se o resultado do teste é Falso (.F.).

##### Sintaxe

```
tlpp.probat.assertFalse( < lValue >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertFalse( < lValue >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| lValue | logical | Valor produzido pelo teste | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se o valor lValue é Falso (.F.). |

##### Observações

* Caso o assertFalse() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertFalse()

  local l1  := .F.  as logical
  local l2  := .T.  as logical

  assertFalse( l1 ) // Ok
  assertFalse( l2 ) // Erro

return .T.
```

##### Abrangência

01.02.10
