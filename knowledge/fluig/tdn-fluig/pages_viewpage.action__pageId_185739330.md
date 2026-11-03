---
content_hash: 1710b1a89ac2e7a3cc111f2d1e3d7ca78d8ff255a1b778003a867fb715e80f94
fetched_at: '2026-06-28T21:35:18.817793+00:00'
page_id: '185739330'
product: fluig
source: tdn-fluig
title: WCM - Como integrar um widget com serviços REST?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739330
version: 12
---

Atenção

Página destinada a atualizações anteriores ao Fluig Plataforma 1.6. Acesse a página original para atualizações a partir do Fluig Plataforma1.6: .

# Índice

4true.\*ndicenone

**Produto:** TOTVS Fluig Plataforma

**Versão:** Anteriores a 1.6.x

# Objetivo

O objetivo desse guia é apresentar a integração de *widgets* com serviços REST.

# Integração de widget com serviços REST

Para obter dados de uma fonte externa à plataforma, a forma mais aconselhável é por chamada REST. Vamos criar um REST  dentro do próprio *widget*, para isso devemos seguir alguns passos.

Dúvidas para criar o *widget*? Siga o .

Primeiro devemos criar uma classe chamada *ApplicationConfig* que extende a classe *Application*.

java

Depois devemos criar a classe REST que desejamos acessar.

java

Em seguida, temos que alterar os arquivos *jboss-web.xml.*

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

com.totvs.technology.auth.saml.TOTVSAuthenticatorValve
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

FORM
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

## Pom.xml

Por fim, temos de declarar a dependência ao módulo *foundation-security-authentication-saml*no *pom.xml* do *widget*.

xml
com.fluig
foundation-security-authentication-saml
compile
 ]]>
