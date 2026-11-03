---
article_id: 360028699492
category: ADVPL - Web Service
content_hash: f4c9eeb74b0eb2a8aa666747535f9c675efc777c01e20a05c68292772d5bcbaa
fetched_at: '2026-06-28T22:40:10.283768+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - O que é REST
type: support-article
updated_at: '2022-02-07T14:33:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028699492-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-O-que-%C3%A9-REST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**O que é, pra que serve e como funciona a comunicação em uma *web* API **RESTful**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução  
REST** (*Representational State Transfer*) é um estilo de arquitetura de *software* que define um conjunto de restrições/regras a serem usados para a criação de serviços *web*.  
  
**Pra que serve?**  
Inicialmente quando escrevemos nossas aplicações elas estão isoladas, contudo, para que seja possível consumi-las em outras aplicações é necessário expô-las por algum método de comunicação.

Dentre diversos outros métodos, o REST (RESTful API) é um deles.  
  
**Exemplo**  
Tenho um aplicativo mobile que registra a quantidade de estoque de cada produto.  
Preciso acessar as informações do estado de estoque corrente (entradas, bloqueios e saídas), assim como enviar os dados das coletas e operações realizadas diariamente.  
Estas informações precisam estar disponíveis no meu smartphone, assim como no sistema de gerenciamento da empresa.  
A partir dessa necessidade, eu crio uma API **RESTful** e programo meu software de gerenciamento e meu smartphone para fazerem solicitações para esse serviço.  
Desta forma, eu tenho um serviço único, que é consumido da mesma maneira e que mantém as informações disponíveis para diversas aplicações.  
  
**Comunicação**Na grande maioria dos casos, as comunicações **RESTful** ocorrem sob o protocolo HTTP utilizando o padrão **JSON** (*JavaScript Object Notation*), onde são utilizados métodos HTTP (GET, POST, PUT, DELETE e outros).  
  
**Exemplo**Preciso que seja possível visualizar os dados de um cliente com código, nome, tipo e endereço, como os dados poderão serão trazidos?  
Eu irei realizar um consumo para um serviço já criado através da **URI** (*Uniform Resource Identifier*) abaixo no método GET:

```
{method} {schema}://{domain}/{patch}?{query}  
{GET} {https}://{mydomain.com.br}/{rest/customer}?{id=CLT008}
```

E quando eu fizer a requisição, me será retornado o JSON abaixo:

```
{  
    "code": CLT018",  
    "name": "IMPACTART DIGITAL",  
    "strategicCustomerType": "F",  
    "address": {  
        "address": "AVENIDA ALVES CARMO, 7811",  
        "stateId": "SP",  
        "city": "JARDIM CARLOS MENDES"              
    }  
}
```

**O que fazer com o JSON?**  
Uma vez recebida a resposta da *web* API, realize a conversão da *string* para um objeto JSON e extraia os valores desejados para integrar ao seu sistema:

**Exemplo em ADVPL**

```
/** RESTANTE DA APLICAÇÃO **/  
  
cJSON := "JSON_RESPOSTA_DO_WS_REST_AQUI"  
oJSON := JSONObject():New()  
  
// AQUI CONTÉM TODOS OS CAMPOS E CONTEÚDOS  
// (ex: oJSON["code"] => "CLT018" | oJSON["address"]["stateId"] => "SP")  
oJSON:FromJSON(cJSON)  
  
/** RESTANTE DA APLICAÇÃO **/
```

**Saiba mais**  
[REST ADVPL](http://tdn.totvs.com/display/framework/REST+ADVPL)  
[REST - Wikipedia](https://pt.wikipedia.org/wiki/REST)  
[JSON - Wikipedia](https://pt.wikipedia.org/wiki/JSON)  
[URI - Wikipedia](https://pt.wikipedia.org/wiki/URI)
