---
content_hash: adf57993323c3da28e72d14b12bcdde9efe4c278634ec98e8c5b088d2c81c581
fetched_at: '2026-06-28T21:35:17.059612+00:00'
page_id: '1022376715'
product: fluig
source: tdn-fluig
title: Como criar um Evento Global
type: documentation
url: https://tdn.totvs.com/display/fluig/Como+criar+um+Evento+Global
version: 3
---

---

Esse guia visa orientar a como criar um Evento Global via Fluig Studio para ser utilizado na plataforma Fluig.

## Pré-requisitos

---

* Ter baixado e instalado o .

## Quem pode criar um evento global?

---

Usuários administradores da empresa ou usuários com permissões configuradas no recurso ["Configurar Eventos Globais"](http://tdn.totvs.com/pages/viewpage.action?pageId=269431799).

## Demonstração

---

Abaixo, temos uma demonstração de como criar um evento global.

854480

## Desenvolvimento de Eventos

---

**01.** A partir do , crie um novo projeto (ou utilize um já existente), clique com o botão direito sobre a pasta ***events***e em seguida ***Novo** -> **Evento Global fluig*** conforme a imagem abaixo.

**Criação de evento - fluig Studio.**

**02.** Em seguida, informe o **Servidor** e **Nome** do evento que será adicionado. Uma tela para edição do evento será aberta, conforme imagem abaixo:

**Criação de evento - fluig Studio.**

#f2f2f2#f2f2f2

É possível observar também que o arquivo **.js** foi adicionado a pasta ***events*** do projeto.

O Fluig permite utilizar o log de execução nos eventos desenvolvidos sobre a plataforma. Através da variável global **log** é possível obter o feedback da execução de cada evento. Existem quatro níveis de log, são eles:

* **ERROR:** apresentação de erros.
* **DEBUG:** depurar a execução.
* **WARN:** informar possível problema de execução.
* **INFO:** apresentação de mensagens.

A forma como cada tipo de log é exibido depende da configuração do servidor de aplicação. Por padrão, no servidor de aplicação, as mensagens do tipo **info** e **warn** são apresentadas no console, enquanto as mensagens do tipo **debug** e **error** são registradas no arquivo de log.

A seguir, é apresentado um exemplo de uso de log em script:

java#f2f2f2#f2f2f2

Teríamos no console do servidor a mensagem **"Testando o log info"**.

Atenção

A maioria dos eventos utiliza o parâmetro **WKUser** para identificar o usuário responsável pela ação. Quando a funcionalidade de **substituto** é utilizada — em que um usuário pode atuar em nome de outro — o valor retornado em **WKUser** será sempre o usuário que estiver efetivamente logado no sistema no momento da ação.

exemplo  
 Ana definiu Bruno como seu substituto. Ao acessar o sistema, Bruno realiza uma ação em nome de Ana. Nesse caso, os eventos que utilizam **WKUser** irão retornar o código do usuário **Bruno**, e não o de Ana.

Em todos os eventos é possível realizar chamadas para os serviços disponíveis na API pública. Acesse **[aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=185736325)** nosso guia de consumo da API pública em eventos.
