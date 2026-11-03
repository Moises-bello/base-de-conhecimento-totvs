---
content_hash: 548607e90098a6e23758b88d92144fb4ff3845b4cf3f5bd1a29b568cb0fce62b
fetched_at: '2026-07-02T19:24:27.012050+00:00'
page_id: '655431283'
product: protheus
source: tdn-tec
title: e-3 - Ordem e Prioridade
type: documentation
url: https://tdn.totvs.com/display/tec/e-3+-+Ordem+e+Prioridade
version: 2
---

Os testes escritos com **PROBAT** são localizados no RPO através das funções de Reflection, portanto a ordem de retorno das Reflections incidirá sobre a ordem de execução dos testes, pois será também a ordem de gravação na tabela *PROBAT\_CONFIG\_ROUTINES* no SQLite.

> Se algum dia a lógica da ordem de retorno das Reflections mudar, irá mudar também a ordem para o **PROBAT**.

Ou seja, se não for usado nenhum outro recurso do **PROBAT**, essa será a ordem de execução dos testes.

Porém, ainda existem alguns recursos que podem ser usados para mudar a ordem de execução conforme convém, sendo:

* [TestFixture >> Priority] - Mudar a prioridade do Teste;
* [TestFixture >> Thread] - Informar que o Teste não deve ser em nova Thread.

#### 1 - Prioridade

Esse recurso especificamente é usado somente para mudar a ordem de execução dos testes, e é muito simples usar.

> **Os valores informados em [TestFixture >> Priority] devem ser:**
>
> * Ser do tipo [numeric].
> * Estar entre 0 e 999, ou seja, até 3 dígitos.
> * Não podem ser negativos.

Para isso, basta usar a propriedade [priority] da annotation [TestFixture], vejamos:

```
@TestFixture()
user function teste_1()
```

```
@TestFixture()
user function teste_2()
```

```
@TestFixture()
user function teste_3()
```

Nesse caso, como todos os testes possuem a mesma prioridade (100 é o valor default), serão executados na seguinte ordem:

1o. - teste\_1()  
2o. - teste\_2()  
3o. - teste\_3()

Agora, vamos aplicar a prioridade e vejamos o que acontece:

```
@TestFixture()
user function teste_1()
```

```
@TestFixture(priority=999)
user function teste_2()
```

```
@TestFixture(priority=1)
user function teste_3()
```

Teremos então a seguinte ordem:

1o. - teste\_3()  
2o. - teste\_1()  
3o. - teste\_2()

#### 2 - Thread

Embora esse recurso não tem a finalidade de organizar a ordem de execução dos testes, na prática acaba alterando pois todos os testes "marcados" para não abrir uma Thread destacada serão executados ao final para amenizar o risco de ocorrer um error.log e derrubar as demais execuções.

Portanto, não é aconselhado usar esse recurso para manipular a ordem, mas é bom saber que os testes com @TestFixture[thread="no"] sejam lançadas ao final de todos os testes.

Saiba mais sobre esse recurso em ().
