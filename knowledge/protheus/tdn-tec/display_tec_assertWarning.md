---
content_hash: b8825c0b0ae51b366628c0dbacaa924827322a00351b626fe89cdfca8a7003af
fetched_at: '2026-07-02T19:24:26.984953+00:00'
page_id: '654948177'
product: protheus
source: tdn-tec
title: assertWarning
type: documentation
url: https://tdn.totvs.com/display/tec/assertWarning
version: 3
---

Gera log de warning na tabela PROBAT\_TEST\_WARNING.

##### Sintaxe

```
tlpp.probat.assertWarning( < cWarning > )
```

ou

```
using namespace tlpp.probat

assertWarning( < cWarning > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cWarning | character | Mensagem de warning | X |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | logical | Indica se a mensagem foi registrada |

##### Observações

* Embora essa função seja um assert, ela não gera resultado positivo ou negativo de teste. Irá apenas gerar uma mensagem de AVISO que no momento de exportação dos resultados será gerado um arquivo XML com todas as mensagens, caso existam.
* Caso o assertWarning() for chamado sem que tenha o **PROBAT** em execução, os valores gerados serão somente exibidos no console.log da aplicação.

##### Exemplos

```
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
user function sample_assertWarning()

  assertWarning( "esse é somente um AVISO, não será gerado resultado de teste" )

return .T.
```

##### Abrangência

01.02.12
