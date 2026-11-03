---
content_hash: 7162ef84ab3126a1519ca604970ee65f190db2e9280f8d07f3f1087d27e745e9
fetched_at: '2026-06-28T21:35:27.031685+00:00'
page_id: '454434362'
product: fluig
source: tdn-fluig
title: Encriptação de senha do banco de dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454434362
version: 27
---

Fique atento!

Esta página é válida a partir da atualização **Voyager (2.0)** do TOTVS Fluig.

Se você utiliza uma atualização anterior, acesse Como encriptar a senha do banco de dados da atualização **1.6 até 1.8.2**.

.\*ndice

# Objetivo

---

Este guia tem como finalidade demonstrar os passos necessários para realizar a encriptação sobre a senha de acesso ao banco de dados.

Importante!

Esse procedimento pode ser realizado para encriptação da senha de todos os bancos de dados homologados pela  do TOTVS Fluig.

# Encriptação de senha

---

A encriptação de senha do banco de dados da plataforma é um procedimento muito importante para evitar o acesso não autorizado à base de dados e com isso aumentar a segurança das suas informações.

Para realizar esse procedimento, é necessário seguir as etapas abaixo, que consistem em gerar a senha criptografada e, em seguida, criar a política de autenticação da aplicação com essa senha.

oculto

**Informação interna:**

Este passo a passo foi duplicado para o artigo: <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360033268194>

Se for feita alguma atualização, lembrar de repassar pra lá.

## Encriptação da senha da base de dados (DataSource)

---

Nessa etapa, a senha da base de dados é encriptada usando o método principal da classe **SecureIdentityLoginModule**, passando como parâmetro a senha em texto plano do banco de dados utilizado. Para fazer a configuração, siga os passos abaixo:

falseEncriptaçãotrue01Passo 01

* Navegue até a pasta raiz de instalação, e acesse a pasta **appserver.**

**Linux**              ==> /opt/fluig/appserver

**Windows**        ==> c:\fluig\appserver

02Passo 02

* Gere a senha encriptada.

**Linux:**

**Windows**:

Importante!

Neste caso, **senha-do-banco** será a senha de acesso ao banco de dados e o resultado será:

**Encoded password: 4c5ab21b9ec71385f5e13f39fd754340**

## Criar a política de autenticação da aplicação com a senha encriptada

---

Nessa etapa é mostrado onde fica o arquivo de configuração para acesso ao banco de dados (**standalone.xml**), a aplicação da política de autenticação pelo aplicativo e a sua respectiva configuração.

Importante!

Antes de fazer qualquer alteração, é importante manter uma cópia do arquivo standalone.xml original, caso seja necessário retornar alguma configuração.

falsePolíticatrue01Passo 01

* Navegue até a pasta raiz de instalação do TOTVS Fluig Plataforma e acesse a pasta de configuração onde está o arquivo **standalone.xml**. Abra esse arquivoem modo administrador ou root.

**Linux**              ==> /opt/fluig/appserver/standalone/configuration

**Windows**        ==> c:\fluig\appserver\standalone\configuration

02Passo 02

* Edite o arquivo **standalone.xml** incluindo o bloco que contém a política de autenticação e a senha encriptada gerada na etapa anterior. Ao abrir o arquivo standalone.xml, procure pela *tag*:

xml]]>

* Dentro da *tag* **<security-domains>** é necessário inserir o seguinte bloco:

xml








]]>

* O atributo **security-domain name** será usados posteriormente na configuração de acesso ao banco de dados.

03Passo 03

* Edite o arquivo **standalone.xml** alterando o bloco de acesso ao banco de dados. Ao abrir o arquivo, procure pelas *tags*:

xml



]]>

* No primeiro *datasource* cujo *pool-name* é **FluigDS**, é necessário eliminar o seguinte bloco:

xml
admin
senhaDeTextoPlano
]]>

* Após remover o bloco acima, substituí-lo pelo bloco abaixo:

xml
encrypted-FluigDS
]]>

* No segundo *datasource* cujo *pool-name* é **FluigDSRO**, é necessário eliminar o seguinte bloco:

xml
admin
senhaDeTextoPlano
]]>

* Após remover o bloco acima, substituí-lo pelo bloco abaixo.

xml
encrypted-FluigDS
]]>

## Pronto!

---

Após estes procedimentos, sua plataforma pode ser iniciada e passa a operar com a senha do banco encriptada, evitando acessos não autorizados e trazendo mais segurança para as suas informações.

$("b:contains('oculto')").parent().parent().hide();
]]>
