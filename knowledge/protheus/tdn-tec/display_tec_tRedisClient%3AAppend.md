---
content_hash: 8c9363fc990bed7dfbea067adab053d4dccf2d408aea829eadc85aed22708c75
fetched_at: '2026-07-02T19:24:24.029569+00:00'
page_id: '454834814'
product: protheus
source: tdn-tec
title: tRedisClient:Append
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AAppend
version: 75
---

Enfileira um comando na fila de comandos para serem processados pelo servidor Redis.

## Sintaxe

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Observações |
| --- | --- | --- | --- | --- | --- |
| ``` cCommand ``` | Caracter | Comando a ser enfileirado | X |  | Pode conter ? que será preenchida por parâmetro |
| cParam1 | Caracter | Complemento do comando |  |  | Substituirá a **primeira** interrogação (ou `?`) que houver no comando `cCommand`. |
| `cParam2` | Caracter | Complemento do comando |  |  | Substituirá a **segunda** interrogação (ou ?) que houver no comando `cCommand.` |
| ... | ... | ... |  |  | Quantidade indefinida de parâmetros complementares |
| ``` cParamN ``` | Caracter | Complemento do comando |  |  | Substituirá a **n-ésima** interrogação (ou `?`) que houver no comando `cCommand`. |

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` oRedisAfter ``` | objeto `tRedisClient` | Cópia do objeto sobre o qual foi feita a chamada, alterado por ela.\* |  |

`*`Isto permite acoplar outros métodos e propriedades à chamada de `::Append()`  
   Por exemplo,   
`oRedisCli:Append(cCommand, @retVal):lOk`

   testará se o comando foi bem sucedido, sem a necessidade de uma consulta à parte a `::lOk` sobre o objeto `oRedisClient`.

## Observações

* `::Append()` apenas enfileira comandos para processamento pelo servidor Redis. A resposta a eles deve ser obtida por chamadas ao método `::GetReply()`

* O método `::Exec()` é muito semelhante em propósito ao método `::Append()`: ambos disparam a execução de comandos no servidor Redis.

* A maior diferença entre `::Append()` e `::Exec()` é que o programa que dispare `::Append()` não precisará aguardar o término de sua execução. E só receberá o resultado do comando quando executar o método `::GetReply()`.

* O fato de não ser necessário acompanhar a execução do comando torna `::Append()` ideal para a programação assíncrona e concorrente do servidor Redis, ao passo que `::Exec()` fica limitado à programação sequencial e síncrona.  
  O método `::Append()` altera o estado da propriedade [tRedisClient:lOk](http://tdn.totvs.com.br/display/tec/tRedisClient%3AlOk) indicando se o comando foi executado corretamente ou com erro, e neste caso o número do erro é atualizado na propriedades [tRedisClient:nError](http://tdn.totvs.com.br/display/tec/tRedisClient%3AnError). O erro é então decodificado como texto legível por humanos na propriedade [tRedisClient:cError](http://tdn.totvs.com.br/display/tec/tRedisClient%3AcError).

## Exemplos

### Exemplo 1 – Comando `set` com *string* de comando fixatrue

cpp

* Nesta listagem, são mostrados o estado das propriedades do objeto `oRedisClient`depois da chamada aos métodos `::Append()` e `GetReply()`.

* É interessante observar que:
  + a propriedade `oRedisClient:nReplyType`é negativa depois da chamada do método `::Append()`, indicando que este comando não teve uma resposta do servidor Redis a ser processada pelo cliente;
  + o resultado (*output*) da execução do comando `set x 'aaa'`, disparado por `::Append()` e recebido por `::GetReply()`, é `.T.`, indicando que foi bem sucedida a atribuição da *string* `'aaa'` ao campo `x`;
  + o tipo de resposta de `::GetReply()` é marcado como 5, indicando que é variável do tipo Status no contexto do Redis, ou lógica, no contexto do AdvPL.

### Exemplo 2 – Comando `set` com *string* de comando parametrizada true

cpptrue

Este outro programa AdvPL é bastante similar ao anterior. Sua maior diferença é o fato de que a chamada ao comando `set` do AdvPL é parametrizada; ou seja: neste exemplo o comando Redis `'set x "aaa"``'` é quebrado em duas partes: `'set x ?' e "aaa"`.   
  
A utilidade deste recurso é permitir que uma parte do comando possa ser mantida fixa, e que outras partes possam ser parametrizadas. Inclusive através de variáveis de programa, que podem ter seus valores obtidos por interação com o usuário, ou através de consulta a bases de dados.   
  
Outro ponto interessante deste programa é o uso do comando `'get x'`, que recupera o resultado da atribuição ao campo `x` neste caso confirma que o par `'set x`'e `"aaa"` de fato colocou o valor `aaa` no campo `x`.

### Exemplo 3 – Comando `mset` com *string* de comando parametrizada e múltiplos campos e valorestrue

cpptrue

Nesta listagem são mostrados dois campos sendo afetados por um único comando, no qual os valores são passados como parâmetros. Um ponto importante é que para que os mesmos comandos `set` e `get` da listagem anterior possam lidar com múltiplos campos, eles devem ser prefixados por `'m'` e transformados em `'mset'` e `'mget'`.   
  
O comando `mset` do Redis trabalha de modo similar ao comando `set`; isto é: devolve verdadeiro (ou `.T.`) se todos campos foram atribuídos de modo corret, ou `.F.` caso contrário). Contudo, o comando `mget` retorna seu resultado como um vetor.

## Veja também

* [tRedisClient:lOk](http://tdn.totvs.com.br/display/tec/tRedisClient%3AlOk)
* [tRedisClient:nError](http://tdn.totvs.com.br/display/tec/tRedisClient%3AnError)
* [tRedisClient:cError](http://tdn.totvs.com.br/display/tec/tRedisClient%3AcError)
