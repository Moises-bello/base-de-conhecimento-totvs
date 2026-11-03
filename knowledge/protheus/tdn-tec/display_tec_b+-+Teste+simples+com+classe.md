---
content_hash: 0a701fd69576e16abdf5c0d0b502677bd0078d37ef6bce122bf8c97771bff7db
fetched_at: '2026-07-02T19:24:26.843691+00:00'
page_id: '654948028'
product: protheus
source: tdn-tec
title: b - Teste simples com classe
type: documentation
url: https://tdn.totvs.com/display/tec/b+-+Teste+simples+com+classe
version: 3
---

Utilizando a mesma aplicação no exemplo anterior, agora iremos implementar o mesmo teste só que utilizando classe.

Veja o exemplo:

```
#include "tlpp-core.th"
#include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
class test_max_class

  private data nInt_1     as integer
  private data nInt_2     as integer
  private data nInt_max   as integer

  public method new()     constructor

  @Test('aqui deve-se colocar o descritivo sobre o teste') 
  public method test_Max() 

endclass

method new() class test_max_class
  ::nInt_1 := 10
  ::nInt_2 := 20
return self

method test_Max() class test_max_class

  ::nInt_max := max( ::nInt_1, ::nInt_2 )

                // Result   , Expected
    assertEquals( ::nInt_max, 20      )

return .T. // NOTA: Sempre retornar TRUE
```

Nesse exemplo não há acréscimo de funcionalidades e apenas mudou a forma de escrever o teste, fazendo uso de classe e por consequência, uso de mais uma annotation **[Test]** para indicar qual método da classe deve ser executado como teste.
