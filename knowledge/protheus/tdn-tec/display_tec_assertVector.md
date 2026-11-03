---
content_hash: 2fb307dbebdb36b5bbc217b1df4f1afe1ae99972f7ec1910d8bc9a2aedf3347c
fetched_at: '2026-07-02T19:24:26.979777+00:00'
page_id: '654948165'
product: protheus
source: tdn-tec
title: assertVector
type: documentation
url: https://tdn.totvs.com/display/tec/assertVector
version: 2
---

Verifica se o resultado do teste é um Vetor (array) IGUAL ao de um Vetor esperado.

##### Sintaxe

```
tlpp.probat.assertVector( < aValue >, < aExpected >, [ cDesc ] )
```

ou

```
using namespace tlpp.probat

assertVector( < aValue >, < aExpected >, [ cDesc ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| aValue | array | Vetor (array) produzido pelo teste | X |  |
| aExpected | array | Vetor (array) esperado | X |  |
| cDesc | character | Descrição do teste (opcional) |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se os vetores (array) aValue e aExpected são iguais em todos os seus elementos. |

##### Observações

* O assertVector() somente compara vetores. Ele não é capaz de comparar array multidimensionais.
* Caso o assertVector() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
function sample_assertVector()

  local a1  := {1,2,'3', ,date()}   as array
  local a2  := {1,2,'3', ,date()}   as array
  local a3  := {1,2,'3',4,date()}   as array

  assertVector( a1, a2 ) // Ok
  assertVector( a1, a3 ) // Erro

return .T.
```

##### Abrangência

01.02.10
