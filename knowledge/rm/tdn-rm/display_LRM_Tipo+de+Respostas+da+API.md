---
content_hash: 2555464032e0bdc51115a34fe8dde1c907d5cf09740b0353cac7d407ee935447
fetched_at: '2026-06-29T00:05:47.795437+00:00'
page_id: '1017446297'
product: rm
source: tdn-rm
title: Tipo de Respostas da API
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipo+de+Respostas+da+API
version: 2
---

Quando o servidor recebe uma solicitação HTTP, o cliente deve saber o resultado da ação. Se houve sucesso ou falhou. Os códigos de status HTTP são vários códigos padronizados, com várias explicações em vários cenários. O servidor sempre deve retornar o código de status correto.

A seguir estão as categorias dos códigos HTTP:

* 2xx - Status de sucesso
* 3xx - Categoria de redirecionamento
* 4xx - Erro no Cliente
* 5xx - Erro no server

## 2xx - Sucesso

Abaixo uma tabela de quando utilizar cada um dos Status Code.

* 200 Ok - Padrão que representa sucesso. Resposta padrão para GET, quando há resultados.
* 201 Created - Indica que um recurso foi criado. Utilize para a resposta do POST. E também retorne o **Header** `Location` indicando o GET dessa informação.
* 204 No Content - Representa que a request foi processada com **sucesso**, mas não há conteúdo para ser retornado. Utilize para PUT, PATCH e DELETE. E também para situações em que o GET não retornou resultados.
* 202 Accepted - Indica que o servidor aceitou a request. Esse é um ótimo Status para processos assíncronos. Por exemplo um cenário onde o usuário faz upload de uma planilha que será processada em background.

## 3xx - Redirect

Como desenvolvedor, não consigo visualizar cenários em que será utilizado o redirect a partir de uma API RESTFul.

Em geral o 302 é bastante utilizado em desenvolvimento Frontend, como Razor. E o **301 Moved Permanently** é utilizado por sysadmins, para indicar que um site foi permanentemente redirecionado para um novo endereço.

## 4xx - Client error

Indica que o client cometeu uma falha na requisição.

* 400 Bad Request - A solicitação não foi processada, pois o servidor não entendeu o que o cliente está solicitando.
* 401 Unauthorized - Indica que o client não está autenticado e não tem autorização para acessar o recurso.
* 403 Forbidden - Indica que o Client está **autenticado** e a requisição é **válida**. Porém o client não tem permissão de acesso naquele recurso.
* 404 Not Found - indica que o recurso não foi localizado.
* 422 - Unprocessable Entity - A validação não pode ser processada por que algum valor inválido foi enviado na requisição.

## 5xx - Erros no servidor

Os status 5xx há dois que merecem destaque. É o erro 500, houve uma falha no servidor e não conseguiu processar a requisição. E o erro 503 que vai botar o pessoal de infra para correr. Indica que o serviço está indisponível. Status comum quando o Webserver sobrecarrega de requisições e não consegue mais processar **nenhuma** requisição. O **503** é comum em cenários de ataques **DDoS**.
