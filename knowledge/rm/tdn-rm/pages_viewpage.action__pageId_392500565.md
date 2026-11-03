---
content_hash: 56c657102bc2147c8c2bf7f66b5a9383dad8e2c4de3fc0a2af8079b024a4b262
fetched_at: '2026-06-29T00:09:09.144819+00:00'
page_id: '392500565'
product: rm
source: tdn-rm
title: Criação do aplicativo do WSO2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=392500565
version: 19
---

Índice:

---

.\*ndice:

# Objetivo

---

       A seguir será apresentado o passo-a-passo de como criar um aplicativo do WSO2 para ser usado no RM, como provedor de login.

       Para mais informações sobre as opções de login, acesse o .

# Criando um novo aplicativo do WSO2

---

**1º-** Acesse a página de Login do WSO2  e faça o login como administrador do sistema.

**2**º**-** Acesse a opção Add em  Service Providers.

**3º-** Preencha as informações básicas do aplicativo e clique em Register:

**4º-**  Após Registrar o Aplicativo expanda a opção "Claim Configuration", e adicione a Claim URI "http://wso2.org/claims/emailaddress" conforme imagem abaixo.

**5º-**  Após configurar a Claim URI é necessário configurar as URIs de redirecionamento.

      Expanda os itens Inbound Authentication Configuration | OAuth/OpenID Connect Configuration e clique em Edit.

Após clicar em Edit será exibida a tela de visualização e atualização das configurações do aplicativo, onde precisaremos preencher somente a URL de redirecionamento (Callback Url).

Login

Para que o login funcione é necessário inserir uma Url de Callback para cada aplicativo do RM (**MDI** , **Portal**, **Portal Educacional, WebAPI** e etc) separados por pipe "|".

Exemplo:

* Para o portal do aluno de teste, nós poderíamos informar um endereço baseado em “localhost”, pois o Portal do Aluno de exemplo encontra-se na mesma máquina em que é feito a configuração (definimos o endereço: <http://localhost:8080/web/app/edu/PortalEducacional/login/>).
* Para o portal que está configurado com SSL informe o endereço correto de redirecionamento. (Neste exemplo usamos: <https://testeframe.com.br/RM12122/Login.aspx>)
* Para o correto funcionamento do login na MDI, preencha com a sua URL de redirecionamento (Neste exemplo usamos: <http://localhost:8080/login>)
* Caso não tenha uma Url de Retorno, utilizar o link disponibilizado no RM.Host ([http://Servidor:PortaHttp/RMRestCallback/oauth/callback](http://localhost:8051/RMRestCallback/oauth/callback)).  
    
  Onde o CallbackURL ficaria assim:   
   regexp=(<http://localhost:8080/web/app/edu/PortalEducacional/login/>|<https://testeframe.com.br/RM12122/Login.aspx>|<http://localhost:8080/login>)  
    
  Após adicionar a url de redirecionamento clique em update.

**6º-**  Após preencher as URL´s de redirecionamento é necessário pegar o ID do cliente e a chave secreta do Cliente

Esses dados serão importantes para fazermos a configuração do aplicativo com o sistema RM.

**7º-** Agora é necessário cadastrar o aplicativo dentro do RM. Abra a MDI e acesse Serviços Globais | Gestão | Comunicação | Aplicativos Externos e inclua um novo Aplicativo Externo.

falseVer exemplo da configuração deste app no RM. 

Selecione o Provedor do aplicativo  3 - WSO2 

Preencha a Chave Pública com o ID do cliente (Aplicativo WSO2)

Chave Privada com a Chave Secreta do cliente (Aplicativo WSO2)

Antes de Salvar siga para o passo abaixo "Preenchendo as URL´s"

Preenchendo as URL´s

Para configurar as Url´s é necessário consultá-las na URL de descoberta dos endpoints do WSO2.

A url de descoberta tem o seguinte prefixo:

[https://seuWSO2:porta/oauth2/oidcdiscovery/.well-known/openid-configuration](https://bh-teste-ws16:9443/oauth2/oidcdiscovery/.well-known/openid-configuration)

Atenção

Certifique-se de que a rota da URL de descoberta esteja liberada para acesso anônimo.

Esta configuração deve ser feita no arquivo **identity.xml** do ambiente **WSO2:**

<Resource context="(.\*)/.well-known(.\*)" **secured="false"** http-method="all"/>

Ao acessar a URL serão exibidos os endpoints do WSO2, onde serão necessários os seguintes endpoints:

```
 authorization_endpoint, token_endpoint, userinfo_endpoint		
```

Os mesmos devem ser inseridos em seus respectivos campos

URL de Retorno

No caso da URL de Retorno é necessário preencher com uma URL válida que responda o código de resposta HTTP 200.

  

A URL de retorno é utilizada somente pela MDI. Sendo que em aplicativos WEB é necessário fazer o redirecionamento para o próprio aplicativo.

Após salvar o Aplicativo o mesmo será exibido na tela de login.

 e veja mais sobre a configuração dos aplicativos no RM.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.22

false

**Processo:** Aplicativo do WSO2

falsefalse

**Status:** Em andamento

false

**Data:**

false

**Autores:**

.
