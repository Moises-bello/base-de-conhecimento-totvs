---
content_hash: 408601f62286cb89bc2019958bfce56a4c57e87492de18ba859c473f2bbe3159
fetched_at: '2026-06-28T21:35:18.945624+00:00'
page_id: '185757267'
product: fluig
source: tdn-fluig
title: Login Único
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185757267
version: 14
---

Atenção

Esta página foi revisada para atualizações 1.6 e superiores do TOTVS Fluig Plataforma.

Caso possua uma atualização anterior escolha o tópico da versão 1.5.13 e anteriores desta página.

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste documento é direcionar desenvolvedores que desejam criar *widgets* e componentes para o TOTVS Fluig Plataforma, aproveitando sua infraestrutura de autenticação.

# Single Sign-On (SSO)

---

O Single Sign-On ou login único, é um mecanismo pelo qual é possível um usuário obter acesso a múltiplos serviços autenticando-se apenas uma vez em algum destes serviços.

Na plataforma TOTVS Fluig a autenticação deve ser sempre iniciada na própria plataforma (acessando a Home e informando usuário/senha). A partir daí então, os *widgets* e componentes poderão fazer uso do SSO para confiarem na autenticação.

Uma vez autenticado, os *widgets* poderão acessar os serviços do fluig (por exemplo, API pública) diretamente, sem a necessidade de fazer uma autenticação a cada requisição (por exemplo, via OAuth).

# A partir da atualização 1.6

---

A autenticação das widgets via SSO depende de três arquivos:

0.5falsesamples1fadetrue1web.xml

* Localizado dentro da pasta **WEB-INF**, o arquivo **web.xml** deve conter o seguinte conteúdo:

xmlEclipseweb.xml


REST

REST
REST
/api/rest/\*

REST
user

FLUIGAUTH, FORM
TOTVSTech

/login.jsp

totvstech

user

sysadmin
]]>

* Deve-se atentar para a tag **<security-constraint>**, que define os caminhos que irão precisar de autenticação para serem acessados (no exemplo, **<contexto-da-windget>/api/rest/\***).
* Deve-se conter pelo menos uma tag **<security-constraint>.** A quantidade desta tag pode variar conforme necessidade.
2jboss-web.xml

* Localizado dentro da pasta **WEB-INF**, o arquivo **jboss-web.xml** deve conter o seguinte conteúdo:

xmlEclipsejboss-web.xml

/[contexto-da-widget]
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

* Deve-se atentar para a tag **<context-root>**, que define o contexto que fará parte da URL para acessar recursos estáticos (js, css, etc.) dessa widget.
3beans.xml

* Localizado dentro da pasta **WEB-INF**, o arquivo **beans.xml** deve conter o seguinte conteúdo:

xmlEclipsebeans.xml

]]>

# Atualização 1.5.13 e Anteriores

---

A autenticação das widgets via SSO depende de quatro arquivos:

0.5falsesamples1fadetrue1web.xml

* Localizado dentro da pasta **WEB-INF**, o arquivo **web.xml** deve conter o seguinte conteúdo:

xmlEclipseweb.xml


REST

REST
REST
/api/rest/\*

REST
user

FORM
TOTVSTech

/login.jsp

totvstech

user

sysadmin
]]>

* Deve-se atentar para a tag **<security-constraint>**, que define os caminhos que irão precisar de autenticação para serem acessados (no exemplo, **<contexto-da-windget>/api/rest/\***).
* Deve-se conter pelo menos uma tag **<security-constraint>.** A quantidade desta tag pode variar conforme necessidade.
2jboss-web.xml

* Localizado dentro da pasta **WEB-INF**, o arquivo **jboss-web.xml** deve conter o seguinte conteúdo:

xmlEclipsejboss-web.xml

/[contexto-da-widget]
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

* Deve-se atentar para a tag **<context-root>**, que define o contexto que fará parte da URL para acessar recursos estáticos (js, css, etc.) dessa widget.
3beans.xml

* Localizado dentro da pasta **WEB-INF**, o arquivo **beans.xml** deve conter o seguinte conteúdo:

xmlEclipsebeans.xml

]]>4foundation-security-authentication-smal.jar

* Localizado dentro da pasta **WEB-INF/lib**.
* O arquivo pode ser obtido no endereço http://nexus.fluig.com/content/groups/public/com/fluig/foundation-security-authentication-saml/[versao-do-fluig.
* Ou, para widgets gerenciadas pelo Maven, esse arquivo é adicionado usando a seguinte dependência:

xmlEclipsefoundation-security-authentication-smal.jar
com.fluig
foundation-security-authentication-saml
compile
[versão-do-fluig]
]]>
