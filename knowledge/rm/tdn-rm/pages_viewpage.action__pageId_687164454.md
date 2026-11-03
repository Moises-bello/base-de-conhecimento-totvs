---
content_hash: 61d08daa06922385a854636491993484342cd425450a6c502f652eef7880c80f
fetched_at: '2026-06-29T00:11:20.645163+00:00'
page_id: '687164454'
product: rm
source: tdn-rm
title: Padrão de Api
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687164454
version: 50
---

### REST é um **estilo de arquitetura ou até mesmo um** Design Patterns, que tem uma série de critérios que devem ser seguidas no processo de sua criação

Restrições para uma API RESTful

### **RESTful seria, então, a API que está de acordo com todas as restrições definidas por Roy.**

Os principais critérios para uma API ser **RESTful** são:

* Uniform Interface;
  + **Resource-based**: tenta lidar com recursos invés de métodos;
  + **Manipulation of resources through representations**: recursos através de uma representação (JSON, XML, HTML.);
  + **Self-descriptive Messages:** As respostas são auto descritivas, incluindo informação suficiente para que o cliente saiba como utilizá-las;
  + **HATEOAS:** Padrão que sempre inclui links uteis junto as respostas de uma requisição.
* Stateless;
  + Não guarde nenhum tipo de estado referente a comunicação;
* Cacheable;
  + Reduzir o número de chamadas feitas para o endpoint e também melhorar a latência de solicitações para a sua API.
* Client-Server;
  + web/aplicação deve ser separada da solicitação/armazenamento dos dados.
* Layered system.
  + O cliente nunca deve chamar diretamente o servidor da aplicação sem antes passar por um intermediador, no caso, pode ser um load balancer ou qualquer outra máquina que faça a interface com o(s) servidor(es)

Sem seguir todas estas restrições, sua API não será RESTful, será apenas mais uma **implementação RPC**em cima do protocolo HTTP.

**[Apis TCGI](https://tdn.totvs.com/pages/editpage.action?pageId=781211647)**

PadrõesURIs legíveis - EndpointsVerbos HTTPRespostasDocumentaçãoImplementado APIs TCGIApi de DataServer

# **Conclusão**

Se você leu atentamente todos os itens citados acima, você ja tem a total certeza que para construir uma API Rest de alta qualidade, não basta apenas conhecer uma linguagem de desenvolvimento, é preciso conhecer muito bem o protocolo HTTP e um conjunto de padrões que com certeza elevam o nível de sua API.

Fontes:

[Serviços RESTful de DataServer no RM](http://tdn.totvs.com)

<https://api.totvs.com.br/guia>

<https://blog.geekhunter.com.br/sua-api-nao-e-restful-entenda-por-que/>

<https://www.alura.com.br/artigos/rest-principios-e-boas-praticas>

<https://www.brunobrito.net.br/api-restful-boas-praticas/>

<https://wssilva-willian.medium.com/design-de-api-rest-9807a5b16c9f>

<https://imasters.com.br/desenvolvimento/definicao-restricoes-e-beneficios-modelo-de-arquitetura-rest>

<https://martinfowler.com/articles/richardsonMaturityModel.html>

<https://docs.aws.amazon.com/pt_br/apigateway/latest/developerguide/api-gateway-caching.html>
