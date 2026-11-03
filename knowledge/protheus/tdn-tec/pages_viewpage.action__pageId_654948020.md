---
content_hash: 339c010d5de710b889afa648f4e5c633b02acae072a03b350a22388ff827d8fa
fetched_at: '2026-07-02T19:24:26.837575+00:00'
page_id: '654948020'
product: protheus
source: tdn-tec
title: a - Teste simples com função
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654948020
version: 3
---

O modo mais simples e menos verboso para escrever um teste é através de uma "function" ou "user function".

No exemplo abaixo iremos construir um teste validando a função Max(), segue:

```
#include "tlpp-core.th"
#include "tlpp-probat.th"

using namespace   tlpp.probat

@TestFixture()
user function test_Max()

  local nInt_1    as integer
  local nInt_2    as integer
  local nInt_max  as integer

  nInt_1 := 10
  nInt_2 := 20
  nInt_max := max( nInt_1, nInt_2 )

              // Result , Expected
  assertEquals( nInt_max, 20      )

return .T. // NOTA: Sempre retornar TRUE
```

* Por esse modo só temos poucas obrigações:  
     1 - Importação da include **[tlpp-probat.th]**  
     2 - Uso da annotation **[TestFixture]**   3 - Uso de alguma função de **assert**, nesse exemplo usamos o assertEquals().  
  Porém a facilidade tem um custo, possui menos recursos avançados para estruturar o teste. Uso de classe habilita mais recursos.
* Pode ser extremamente útil para testes simples que não exigem complexidade em sua funcionalidade.
* Simplifica o uso do PROBAT para quem tem dificuldades em escrever códigos com orientação a objetos.
