---
content_hash: d7feb1dffe856b03e035e4d4b6f495313017c483536b67c207aad6a0fffa7e6c
fetched_at: '2026-07-02T19:24:27.037977+00:00'
page_id: '655864264'
product: protheus
source: tdn-tec
title: a - Discovery - Encontrando os Testes no RPO
type: documentation
url: https://tdn.totvs.com/display/tec/a+-+Discovery+-+Encontrando+os+Testes+no+RPO
version: 2
---

Como dito anteriormente, o **PROBAT** antes de executar os testes ele precisa encontrá-los e faz isso em seu processo de configuração pré-execução.

Esse processo de descoberta pode ocorrer em duas situações:

* Quando solicitado.
* Sempre antes da execução dos testes;

Ambos os casos possuem prós e contras, vamos a eles:

| Modo | Prós | Contra |
| --- | --- | --- |
| Por Solicitação | Garante performance na velocidade dos testes. (\*1) | É preciso solicitar a descoberta sempre que houver novos fontes de testes compilados. |
| Na Execução | Garante a descoberta de fontes recém compilados. | Em RPO´s grandes, pode-se encontrar lentidão a cada execução. (\*2) |

> (\*1) Os testes só serão executados se já foi solicitado anteriormente a descoberta.
>
> (\*2) - É possível configurar um intervalo de tempo entre cada descoberta, portanto, para execuções efetuadas dentro desse prazo, realizará somente 1 (um) processo de descoberta, porém nesse intervalo pode-se "perder" algum fonte novo recém compilado.

É preciso indicar ao **PROBAT** por qual modo deseja que ele funcione, e para isso é preciso indicar através do INI, segue:

```
[PROBAT]
TESTS_DISCOVERY_MODE=1
```

Sendo:  
0 - Por Solicitação;  
1 - Na Execução.

## Por Solicitação

Ao definir por esse modo, teremos que solicitar a descoberta dos fontes quando:

* Primeira execução do motor;
* Quando houver nova compilação de código-fonte de testes.

> Caso fontes sejam compilados e não seja solicitada nova descoberta, o **PROBAT** sequer saberá da existência desses testes e portanto não irá executá-los

Para solicitar a descoberta, podemos fazer uso de duas maneiras:

#### 1 - Main Function:

c#

```
Essa função tem retorno do tipo lógico, sendo:
```

* .T. conseguiu fazer a descoberta.
* .F. quando ocorrer algum problema.

#### 2 - Via api Rest:

xml

```
Json Retorno:
```

{ "sucess": yes|no, "message": "" }

## Na Execução

Ao indicar que a descoberta deve sempre ocorrer ao executar, quando solicitado a execução por *tlpp.probat.run()* o **PROBAT** irá sempre procurar por fontes de testes compilados, exceto quando a execução ocorrer dentro de um intervalo de tempo configurável pela chave abaixo:

```
[PROBAT]
TESTS_DISCOVERY_TIME_INTERVAL=3600
```

> O Valor deve ser numérico e é em segundos.
