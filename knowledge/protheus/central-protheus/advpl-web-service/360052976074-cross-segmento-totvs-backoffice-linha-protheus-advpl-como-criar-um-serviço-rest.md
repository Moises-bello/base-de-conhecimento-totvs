---
article_id: 360052976074
category: ADVPL - Web Service
content_hash: d148988dd6fae87a0380bf2bc19ffcddd3e02699aa0f2e126a1ea1ca4929e146
fetched_at: '2026-06-28T22:40:10.188220+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Como criar um
  serviço REST no protheus
type: support-article
updated_at: '2024-07-04T14:59:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052976074-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-servi%C3%A7o-REST-no-protheus
---

**Dúvida**O que eu preciso para criar um serviço ***REST*** no protheus?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**Antes de começar o desenvolvimento de sua aplicação , certifique-se que o ambiente está configurado para utilização do *WebService REST* (**veja em saiba mais**).

Para criar um serviço *REST*, utilizamos a classe *WSRESTFUL*, onde através dela iremos publicar nosso serviço e declarar e desenvolver nossos métodos *GET,POST,PUT* e *DELETE*. É importante ressaltar que hoje o produto só suporta esses métodos.

Vamos iniciar nosso fonte, declarando os includes necessário para a utilização da classe.   
\***Importante**: Estar com os includes sempre atualizados conforme o portal de download.

```
#INCLUDE 'totvs.ch'  
#INCLUDE 'restful.ch'
```

Depois disso iremos criar a classe WSRESTFUL informando um nome  ***helloworld*(**nome**)**, uma descrição ***DESCRIPTION***"Meu Primeiro serviço REST!" e o fechamento da classe com ***END WSRESTFUL*.**

```
WSRESTFUL helloworld DESCRIPTION "Meu Primeiro serviço REST!"  
  
END WSRESTFUL
```

 Vamos também declarar os métodos que vamos ter na nossa classe. Para isso utilizamos o comando **WSMETHOD**, indicaremos o nome do método e uma descrição para ele:

```
WSMETHOD GET DESCRIPTION "Retornar um Hello World"
```

Com isso, só nos resta desenvolver o método que declaramos, para isso utilizaremos novamente o método **WSMETHOD**, só que agora vamos "amarrar" ele a nossa classe usando o comando **WSSERVICE,** que serve para indicar a qual classe o método pertence. Usaremos também o ***SetResponse***, que serve para informar a resposta da requisição, e ao fim daremos o ***Return***, para o programa entender que finalizamos o desenvolvimento do nosso método.

\***importante**: O retorno precisa ser logico.

```
WSMETHOD GET WSSERVICE helloworld  
    ::setResponse('[{"Status":"Hello World"}]')  
return .T.
```

Ao final de nosso desenvolvimento, teremos o seguinte resultado:

```
#include "protheus.ch"  
#include "restful.ch"  
  
WSRESTFUL helloworld DESCRIPTION "Meu Primeiro serviço REST!"  
    WSMETHOD GET DESCRIPTION "Retornar um Hello World"   
END WSRESTFUL  
  
WSMETHOD GET WSSERVICE helloworld  
    ::setResponse('[{"Status":"Hello World"}]')  
return .T.
```

Após compilar esse exemplo, será necessário reiniciar o seu AppServer, para que o seu serviço seja publicado na lista de *API's*.

O exemplo acima é básico, para desenvolvedores que nunca tiveram contato com WS em ADVPL, e serve para dar um "norte" ao desenvolvedor que quer construir suas *API's*

**Saiba Mais**:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793)  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Criação de Web Service REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021376912)
