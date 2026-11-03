---
content_hash: 8e16ad2f7ef03995221e03b13461059ba4126a8e024b6edf65162e23c823c50e
fetched_at: '2026-07-02T19:24:26.867394+00:00'
page_id: '654948032'
product: protheus
source: tdn-tec
title: c - Teste completo com classe
type: documentation
url: https://tdn.totvs.com/display/tec/c+-+Teste+completo+com+classe
version: 5
---

Ao utilizar classe para escrever seu teste, é possível a utilização de mais recursos para estruturar a lógica dele.

Além das annotations já citadas, temos ainda a possibilidade de utilizar as seguintes:

***[OneTimeSetUp]***  
Indica os métodos a serem executados somente uma vez **antes** de qualquer método de teste.

***[SetUp]***  
Indica os métodos a serem executados imediatamente **antes** de cada método de teste.

***[OneTimeTearDown]***  
Indica os métodos a serem executados somente uma vez **após** de todos os métodos de teste.

***[TearDown]***  
Indica os métodos a serem executados imediatamente **após** cada método de teste.

***[ErrorLog]***  
Indica um método que terá obrigatóriamente um error.log em tempo de execução (runtime). Esse recurso será explicado melhor em (Recursos Avançados).

Para ficar claro, abaixo segue um exemplo com todas as annotatios para facilitar o entendimento da ordem de execução dos métodos através do console do appserver.

Vamos a implementação:

```
# include "tlpp-core.th"
# include "tlpp-probat.th"

using namespace tlpp.probat

@TestFixture()
class test_max_class_completo

  private data nInt_1     as integer
  private data nInt_2     as integer
  private data nInt_max   as integer

  public method new()     constructor

  // Setups
    @OneTimeSetUp()
    public method SetOne_1()

    @OneTimeSetUp()
    public method SetOne_2()

    @Setup()
    public method SetAll()

  // Tests
    @Test('first example test for full use of resources')
    public method FirstExampleMethod()

    @Test('second example test for full use of resources')
    public method SecondExampleMethod()

  //TearDown's
    @TearDown()
    public method DownAll()

    @OneTimeTearDown()
    public method DownOne()

endclass

method new() class test_max_class_completo
  ::nInt_1 := 10
  ::nInt_2 := 20
  conout( '-> [constructor] Method: ' + procname() )
return self

method SetOne_1() class test_max_class_completo
  ::nInt_1 += 5
  ::nInt_2 += 1
  conout( '  -> [OneTimeSetUp] Method: ' + procname() )
return .T.

method SetOne_2() class test_max_class_completo
  ::nInt_1 += 3
  ::nInt_2 += 2
  conout( '  -> [OneTimeSetUp] Method: ' + procname() )
return .T.

method SetAll() class test_max_class_completo
  ::nInt_1 += 5
  ::nInt_2 += 1
  conout( '    -> [SetUp] Method: ' + procname() )
return .T.

method FirstExampleMethod() class test_max_class_completo
  ::nInt_max := max( ::nInt_1, ::nInt_2 )
    assertEquals( ::nInt_max, 24 )
  conout( '       -> [Test] Method: ' + procname() )
return .T.

method SecondExampleMethod() class test_max_class_completo
  ::nInt_max := max( ::nInt_1, ::nInt_2 )
    assertEquals( ::nInt_max, 26 )
  conout( '       -> [Test] Method: ' + procname() )
return .T.

method DownAll() class test_max_class_completo
  ::nInt_1 -= 2
  conout( '    -> [TearDown] Method: ' + procname() )
return .T.

method DownOne() class test_max_class_completo
  ::nInt_1 := Nil
  ::nInt_2 := Nil
  conout( '  -> [OneTimeTearDown] Method: ' + procname() )
return .T.
```

Com esse exemplo, teremos a seguinte saída no console:

```
-> [constructor] Method: NEW                  | nInt_1 [10] | nInt_2 [20]
  -> [OneTimeSetUp] Method: SETONE_1          | nInt_1 [15] | nInt_2 [21]
  -> [OneTimeSetUp] Method: SETONE_2          | nInt_1 [18] | nInt_2 [23]
    -> [SetUp] Method: SETALL                 | nInt_1 [23] | nInt_2 [24]
       -> [Test] Method: FIRSTEXAMPLEMETHOD   | nInt_1 [23] | nInt_2 [24]
    -> [TearDown] Method: DOWNALL             | nInt_1 [21] | nInt_2 [24]
    -> [SetUp] Method: SETALL                 | nInt_1 [26] | nInt_2 [25]
       -> [Test] Method: SECONDEXAMPLEMETHOD  | nInt_1 [26] | nInt_2 [25]
    -> [TearDown] Method: DOWNALL             | nInt_1 [24] | nInt_2 [25]
  -> [OneTimeTearDown] Method: DOWNONE        | nInt_1 [  ] | nInt_2 [  ]
```

##### **Importante**

Os métodos **SETONE** e **DOWNONE** somente são executados uma única vez, ou seja, no início de todos os testes executa o **SETONE** e ao final de todos os testes executa o **DOWNONE**.

Porém, como temos mais de 1 (um) método de teste, os métodos **SETALL** e **DOWNALL** são executados mais de uma vez, sempre antes de cada método de teste executa o **SETALL** e após cada método de teste executa o **DOWNALL**.

O fluxo de execução da classe fica então:

1. Inicia Objeto TestFixture (método new)
2. Executa método OneTimeSetup **[Opcional]**
3. Executa método Setup **[Opcional]**
4. Executa método Test
5. Executa método TearDown **[Opcional]**
6. Executa método OneTimeTearDown **[Opcional]**

1. Não há limites para quantidade de métodos a serem executados através das marcações por annotation, ou seja, todos os métodos marcados serão executados.
2. Os passos 3-4-5, caso tenham sido declarados pelas annotations correspondentes e exista mais de um teste, sempre haverá esse Loop de execução dos 3 passos, ou seja, >> setup >> test >> tearDown.
