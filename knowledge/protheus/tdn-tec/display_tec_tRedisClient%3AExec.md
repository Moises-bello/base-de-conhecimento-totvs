---
content_hash: cf8ddd0d82ee9ddcbc93f1423634f1cb93e948759d6f5d26993fee6662bcaf09
fetched_at: '2026-07-02T19:24:24.061766+00:00'
page_id: '454835745'
product: protheus
source: tdn-tec
title: tRedisClient:Exec
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AExec
version: 55
---

Dispara a execução de um comando a ser processado pelo servidor Redis.

## Sintaxe

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Observações |
| --- | --- | --- | --- | --- | --- |
| `cCommand` | Caracter | Comando Redis a ser executado | X |  |  |
| ``` cParam1 ``` | Caracter | Complemento do comando |  |  | Substituirá a **primeira** interrogação (ou `?`) que houver no comando `cCommand`. |
| ``` cParam2 ``` | Caracter | Complemento do comando |  |  | Substituirá a **segunda** interrogação (ou `?`) que houver no comando `cCommand`. |
| ... | ... | ... |  |  | Quantidade indefinida de parâmetros complementares adicionais |
| ``` cParamN ``` | Caracter | Complemento do comando |  |  | Substituirá a **n-ésima** interrogação (ou `?`) que houver no comando `cCommand`. |
| `retVal` | Variável | Receberá o resultado da execução | X | X | Irá conter o resultado do comando executado no Redis conforme o tipo de operação, podendo ser status (lógico), numérico, texto (caracter), array, nulo. |

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` oRedisAfter ``` | objeto `tRedisClient` | Cópia do objeto sobre o qual foi feita a chamada, alterado por ela.\* |  |

`*`Isto permite acoplar outros métodos e propriedades à chamada de `::Exec()`  
   Por exemplo,   
`oRedisClient:Exec(cCommand, @outParm):lOk`

   testará se o comando foi bem sucedido, sem a necessidade de uma consulta à parte a `::lOk` sobre o objeto `oRedisClient`.

## Observações

* O número de parâmetros complementares é ao comando é praticamente ilimitado, suficiente para a imensa maioria das aplicações que usem Redis;
* Alguns comandos do Redis admitem parâmetros adicionais. Neste caso, para facilidade de programação, pode-se ter uma *string* de comando fixa (ou constante), com possibilidade de substituição por variáveis nos pontos onde for inserido um ponto de interrogação, o caractere ?

* O método `::Exec()` é muito semelhante em propósito ao método `::Append()`: ambos disparam a execução de comandos no servidor Redis.

* A maior diferença é que o programa que dispare `::Exec()` terá que aguardar seu término e receberá dele o resultado do comando, ao passo que isso não ocorre com `::Append()`. Por isso `::Exec()` fica limitado à programação sequencial e síncrona.

* Pontos importantes a serem observados:
  + o resultado da função é passado para o parâmetro `retVal`, que deve por isso ser passado por referência. `::Exec()` também altera o estado do objeto sobre o qual é chamado. Por isso, também as propriedades do objeto terão que ser avaliadas depois da chamada ao método `::Exec()`;
* o tipo de dados do resultado da chamada a `::Exec()` vai variar de acordo com o comando executado. Por exemplo, o comando `set` retorna valor lógico (`.T.` ou `.F.`), enquanto que`get` retorna uma cadeia de caracteres.
* O comando altera o estado da propriedade  indicando se o comando foi executado corretamente ou com erro, e neste caso o número do erro é atualizado nas propriedades  e .

## Exemplos

### Exemplo 1 - Emissão do comando `set` para o servidor  Redis true

cpptrue

### Exemplo 2 - Emissão do comando `set` para o servidor  Redis, parametrizado true

cpptrue

### Exemplo 3 - Emissão do comando `get` para o servidor  Redis  true

cpptrue

## Veja também
