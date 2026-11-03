---
content_hash: b06c762aebbf84f82684d5be2b7aba761717c056515f3ecd60d7a9b8d52c737a
fetched_at: '2026-07-02T19:24:27.032420+00:00'
page_id: '655648819'
product: protheus
source: tdn-tec
title: e-7 - Error Log
type: documentation
url: https://tdn.totvs.com/display/tec/e-7+-+Error+Log
version: 4
---

Podem existir casos onde seu teste cause error.log no sistema, e talvez seja exatamente o esperado.

Mas como então iremos transformar o error.log causado em resultado positivo já que o **PROBAT** automaticamente captura os erros catastróficos e gera um resultado negativo no plano de testes?

Para esses casos serão necessários utilizar a annotation [ErrorLog] junto com as annotations [Test] para métodos ou [TestFixture] para funções.

Ao utilizar esta annotation, deve-se obrigatoriamente informar a descrição do erro, ou seja, o error.log esperado para que não o teste não falhe.

c#

ou

c#

Neste exemplo, o if falhará pois é realizado a comparação de uma variável do tipo string com um valor booleano. Porém, como foi utilizado a annotation [ErrorLog] na definição do Teste e com a indicação de "type mismatch", o resultado do teste será verdadeiro.

Porém, se na definição do erro tivesse qualquer outra descrição que não fosse o error.log causado, mesmo fazendo uso de [ErrorLog] o resultado será negativo, pois não é exatamente o erro esperado.

> Nota: Em caso de não utilização desta annotation, será gerada uma falha no XML com o error log encontrado durante a execução da thread.
