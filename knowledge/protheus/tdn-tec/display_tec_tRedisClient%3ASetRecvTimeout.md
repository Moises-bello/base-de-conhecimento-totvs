---
content_hash: f51bab9488936639de6962d26899ef011127425d688d13377135690f678293b9
fetched_at: '2026-07-02T19:24:24.077959+00:00'
page_id: '454837042'
product: protheus
source: tdn-tec
title: tRedisClient:SetRecvTimeout
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3ASetRecvTimeout
version: 30
---

Atribui um valor máximo de espera (ou *timeout*) para a recepção de repostas de comandos vindas do servidor.

## Sintaxe

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Observações |
| --- | --- | --- | --- | --- | --- |
| ``` nTimeInSeconds ``` | numérico | Número de segundos máximo a esperar; frações de segundo podem ser usadas | X |  |  |

## Retorno

## Observações

* Caso o método `::SetRecvTimeout()` receba como parâmetro um valor inadequado de tempo de *timeout*, negativo ou nulo, o valor anterior não será alterado, e nem haverá indicação de erro.
* O método `::SetRecvTimeout()` altera diretamente o valor da propriedade `::nTimeout`.  Apenas ele pode alterá-la;
* O método `::SetRecvTimeout()` é muito importante para aplicações críticas que dependam de tempo de resposta preciso; isto é: quanto o tempo o servidor Redis levará para responder.
* `::SetRecvTimeout()` também é útil para uma aplicação que interaja com um servidor Redis ou muito ocupado, ou muito instável, pois permite ajustar o limite máximo de tempo que o cliente poderá aguardar por uma resposta, antes de considerar que ela não virá;
* A chamada método `::SetRecvTimeout()` não gera um valor específico de resultado, e isto é indicado pelo valor negativo na propriedade `::nReplyType` do objeto através`tRedisClient` do qual foi chamado.   
    
  Em vez disso `::SetRecvTimeout()` retorna o próprio objeto `tRedisClient` sobre o qual foi chamado.
* Para avaliar o efeito de `::SetRecvTimeout()`, e confirmar sua ação, deve-se consultar a propriedade `::nTimeout`;
* Caso o servidor não responda um comando emitido pelo cliente em um tempo (em segundos) menor do que o valor especificado em `::SetRecvTimeout()`, o comando retornará com erro e essa informação será registrada na propriedade `::lOk`, que conterá `.F.`

## Exemplos

### Exemplo 1 - uso básico de `::SetRecvTimeout()`

cpptrue

A função de usuário `SetTout()` mostra a ação de `::SetRevTimeout()` de duas formas: a listagem dos atributos do objeto `tRedisClient` através de `VarInfo()`, e através da impressão direta da propriedade `::nTimeout`.

## Veja também
