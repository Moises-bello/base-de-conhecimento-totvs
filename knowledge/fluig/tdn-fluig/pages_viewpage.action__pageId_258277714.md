---
content_hash: 5f2cfa7ddaa92ac42e0771b8b721368b9c67dc0bc6c55d5a6a126e5fda6dd991
fetched_at: '2026-06-28T21:35:23.783319+00:00'
page_id: '258277714'
product: fluig
source: tdn-fluig
title: Integrando widget com serviços REST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258277714
version: 9
---

Atenção

Esta página foi revisada para considerar as novas configurações de server do TOTVS Fluig Plataforma para a atualização 1.6.

Caso possua uma atualização anterior do Fluig Plataforma acesse: .

# Índice

4true.\*ndicenone

# Objetivo

O objetivo desse guia é apresentar a integração de *widgets* com serviços REST.

# Integração de widget com serviços REST

Para obter dados de uma fonte externa à plataforma, a forma mais aconselhável é por chamada REST. Vamos criar um REST  dentro do próprio *widget*, para isso devemos seguir alguns passos.

Dúvidas para criar o *widget*? Siga o .

Primeiro devemos criar uma classe chamada *ApplicationConfig* que extende a classe *Application*.

java

Depois devemos criar a classe REST que desejamos acessar.

java

Em seguida, temos que alterar os arquivos *jboss-web.xml*

Fique atento!

A propriedade ***context-root*** precisa ser idêntica ao ***application.code*** fornecido para a sua widget no arquivo *[application.info](http://application.info)*, precedida por uma "/".

Exemplo: se sua widget possui o código ***news***, o *context-root* precisa ser ***/news.***

xml

/news
false
TOTVSTech

user
totvstech

totvstech
totvstech

sysadmin
wcmadmin

admin
wcmadmin
]]>

Também temos que alterar o arquivo *web.xml* para que possamos acessar esse REST.

xml



30


REST

REST
REST
/api/rest/\*

REST
user

FLUIGAUTH,FORM
TOTVSTech

/login.jsp
/loginfail.jsp

totvstech

user

sysadmin

index.jsp
]]>

Depois disso, é possível utilizar o REST que se encontra dentro do *widget* por meio do método *WCMAPI.Read*, utilizado para fazer chamadas REST.

js

O método *WCMAPI.getServerURL()*  traz a URL do servidor que será utilizado para montar a URL da chamada REST. Em seguida, concatenamos o caminho do REST que pretendemos chamar. Neste caso, utilizamos o seguinte caminho: '/news/api/rest/news/feed'. Onde:

* '/news': é o código do *widget*;
* '/api/rest': é o @Path da classe *ApplicationConfig.java;*
* '/news': é o @Path da classe *NewsRest.java*;
* '/feed': é o @Path do método da classe *NewsRest.java* que desejamos chamar.
