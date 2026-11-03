---
content_hash: baeddf6cdcbb1452396305f84f1ae3c808e951b51b8d4d1a0bd0f6af8eb6d563
fetched_at: '2026-06-29T00:08:36.140014+00:00'
page_id: '284462425'
product: rm
source: tdn-rm
title: Como aumentar a segurança de sua aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284462425
version: 40
---

## **Índice**

---

Índice

## **Introdução**

---

O RM é desenvolvido baseado nos princípios fundamentais de segurança abordados pelo OWASP(Open Web Application Security Project). Porem existem configurações que permitem ajustar o nível de segurança da aplicação.

As configurações referentes ao item "**Portal Corpore.Net e Web API"** podem ser feitas automaticamente pelo instalador **"TOTVS RM Portal"**. As demais configurações devem ser feitas manuais.

Abaixo falaremos um pouco de cada uma dessas configurações.

## **Portal**

---

* ### Robots.txt e Indexação em Buscadores/Rastreadores

Documentação:  (caso este arquivo não exista em seu Default Web Site no IIS nosso instalador irá adicioná-lo se optar em habilitar a segurança no portal);

* ### SSL no IIS

Para garantir que a comunicação com o portal seja segura, habilite o SSL para a sua aplicação no IIS. Isso é recomendado principalmente quando o portal é exposto em uma DMZ ou servidor com acesso via rede pública:

Para isso é necessário adquirir um certificado através de uma autoridade certificadora confiável e seguir as documentações. Para mais informações acesse:

<https://en.wikipedia.org/wiki/SSL>

<https://www.digicert.com/ssl-certificate-installation-microsoft-iis-7.htm>

<https://www.digicert.com/ssl-certificate-installation-microsoft-iis-8.htm>

* ### Reduzir o nível de detalhamento de mensagens exibidas para o usuário

Para isso basta inserir a tag abaixo dentro da sessão AppSettings do web.config do portal Corpore.Net.

xml]]>

A partir das versões 12.1.2310, 12.1.2306.144, 12.1.2302.201 e 12.1.2209.268, a tag **StackTraceVisible** é definida como **false** por padrão.

Para mais detalhes veja:

<https://www.owasp.org/index.php/Improper_Error_Handling>

* ### Desabilitar o Debug: **"[ASP.NET](http://asp.net/) DEBUG Method Enabled"**

No ***web.config***, no nó ***<system.web>***:

xml]]>

Por padrão, vem desabilitado no Corpore.Net, mas habilitado no FrameHTML.

Referência: <https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/development/disable-debugging-application>

* ### Como fazer para remover do cabeçalhos de resposta HTTP dos seguintes itens

    
  + **Server**  
    Esse cabeçalho de resposta pode ser removido com uma configuração no arquivo ***web.config***, no nó ***<system.webServer>*** adicione:

    xml
     
    ]]>

* + **X-Powered-By**  
    Esse cabeçalho de resposta pode ser removido com uma configuração no arquivo ***web.config***, no nó ***<system.webServer>*** adicione:

    xml
     
       
     
    ]]>

* + **X-AspNet-Version**  
    Esse cabeçalho de resposta pode ser removido com uma configuração no arquivo ***web.config***, no nó ***<system.web>*** adicione:

    xml]]>
* **Habilitar Segurança CSRF (Cross-Site Request Forgery)**CSRF é um ataque onde um site malicioso faz o navegador de uma vítima enviar uma requisição para o seu sistema sem ela perceber.

 <add key="**CSRFEnabled**" value="**true**" />  
           Ao utilizar a tag como true, token será gerado e validado no servidor, garantindo que a informação não foi **alterada**, **fabricada**, ou **disparada por terceiros** sem o consentimento do usuário.

Atenção

Caso utilize WebFarm é um pré requisito da configuração inserir a tag machinekey conforme documentação [Configuração do Portal RM e Portal FrameHTML em WebFarm](https://tdn.totvs.com/pages/viewpage.action?pageId=162168956#Configura%C3%A7%C3%A3odoPortalRMePortalFrameHTMLemWebFarm-EXEMPLODEUTILIZA%C3%87%C3%83O).

* ### Criptografar o *ViewState*

O *ViewState*, caso não esteja criptografado, pode abrir brechas para roubo de informações sensíveis.

Para criptografá-lo, no ***web.config***, no nó ***<system.web>***, adicionar as opções  **enableViewStateMac="true"** **viewStateEncryptionMode="Always"** ao final da *tag **pages***:

           O ViewState sempre terá **MAC** (integridade)

           O ViewState sempre estará **criptografado** (confidencialidade)

xml]]>

Referência: <https://learn.microsoft.com/en-us/dotnet/api/system.web.ui.page.viewstateencryptionmode?view=netframework-4.8>

* ### **Ativar a flag “Secure” para os cookies de sessão**

Importante para garantir que os cookies, responsáveis por armazenar alguns dados de autenticação (não inclui usuário e senha) e outras informações, seja transportado em segurança. Basta seguir os passos listados no link abaixo:

<https://stackoverflow.com/questions/1442863/how-can-i-set-the-secure-flag-on-an-asp-net-session-cookie>

* ### Habilitar HSTS na aplicação

Isso garante que sua comunicação será feita com segurança, ou seja, utilizando o SSL. Para mais informações acesse:

<https://www.poppastring.com/blog/UsingHTTPStrictTransportSecurityInIIS.aspx>

* ### **Definir HttpOnlyCookies como true**

A configuração HttpOnlyCookies definida como true ajuda a atenuar as ameaças de scripts entre sites que pode resultar em roubo de cookies.

<https://msdn.microsoft.com/library/ms228262%28v=vs.100%29.aspx>

* ### Remover a permissão de listar os artefatos do ambiente diretamento no IIS

[https://docs.microsoft.com/en-us/iis/configuration/system.webserver/directorybrowse](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/directorybrowse "Follow link")

## **Comunicação Portal / RM.exe com o HOST**

---

* A comunicação com o HOST já é feita com segurança e os dados não são trafegados em “plain text” por padrão. Porem para aumentar a segurança e fazer que as informações trafeguem criptografadas e com ainda mais segurança, sugerimos que habilitem o SSL no HOST. Para isso sigam a documentação abaixo:  
  <http://tdn.totvs.com.br/display/LRM/Habilitar+SSL+no+Host>  
  OBS.: A documentaçãoa cima contempla como aumentar a segurança também dos Web Services providos pelo HOST.

## **Portal Corpore.Net e Web API**

---

* Para garantir que a comunicação com o portal Web Api seja mais segura, foram adicionadas na sessão system.webServer >> httpProtocol >> customHeaders, três novas entradas que poderam ser customizadas pelo usuário, são elas:

| Nº | Nome da entrada | Valor padrão | Valores Possíveis | Descrição |
| --- | --- | --- | --- | --- |
| 1 | X-Content-Type-Options | nosniff | nosniff | ``` Para evitar o sniffing do tipo MIME, você pode adicionar o cabeçalho X-Content-Type-Options. Isso torna mais difícil para os hackers adivinharem o tipo certo de mime, inspecionando o conteúdo. ``` |
| 2 | X-Xss-Protection | 0; mode=block | ``` 0 1 0; mode=block 1; mode=block 0; report=<reporting-uri> 1; report=<reporting-uri> ``` | ``` O X-Xss-Protection é um recurso implementado no navegador mais moderno, que interrompe o carregamento da página quando um ataque de script entre sites é detectado. ``` |
| 3 | X-Frame-Options | -- | ``` X-Frame-Options: DENY X-Frame-Options: SAMEORIGIN X-Frame-Options: ALLOW-FROM https://example.com/ ``` | ``` O cabeçalho X-Frame-Options garante que os hackers não criem iframe para o seu site, a fim de induzi-lo a clicar em links que você nunca quis. Se você estiver usando a ASP.NET MVC 5 ou mais recente, esse cabeçalho será adicionado automaticamente. ``` |

## **Configurações feitas pelo Instalador RM**

Para que o instalador inclua essas tags, é necessário clicar em 'Sim' no assistente de instalação quando for solicitada permissão para habilitar a segurança.  
As tags de configuração a seguir são aplicadas automaticamente durante a instalação do RM e são definidas com os seguintes valores:

* **X-AspNet-Version**
  + **Valor:** `null`
  + **Descrição:** Oculta a versão do ASP.NET, prevenindo a exploração de vulnerabilidades conhecidas dessa versão específica.
* **X-Content-Type-Options**
  + **Valor:** `nosniff`
  + **Descrição:** Previne que o navegador tente inferir o tipo de conteúdo do arquivo, o que ajuda a evitar ataques de tipo MIME.
* **X-PoweredBy**
  + **Valor:** `null`
  + **Descrição:** Remove a informação sobre a tecnologia usada no servidor, dificultando a identificação e exploração de possíveis vulnerabilidades específicas da tecnologia.
* **X-Xss-Protection**
  + **Valor:** `1; mode=block`
  + **Descrição:** Habilita a proteção contra ataques XSS (Cross-Site Scripting) no navegador e bloqueia a página quando um ataque é detectado.

Passo a passo para configuração manual dos headers:

* **Acessar o Gerenciador do IIS (Internet Information Services):**
  + Abra o Gerenciador do IIS no servidor onde o portal está hospedado.
* **Selecionar o Site ou Aplicação:**
  + Na árvore de conexões à esquerda, selecione o site ou aplicação onde você deseja adicionar os headers.
* **Abrir a Opção "HTTP Response Headers":**
  + No painel central, clique duas vezes na opção "HTTP Response Headers".
* **Adicionar Cada Header:**
  + Para cada header listado acima:
  + Clique em "Add..." no painel à direita.
  + No campo "Name", insira o nome do header (por exemplo, `Cache-Control`).
  + No campo "Value", insira o valor correspondente (por exemplo, `no-store`).
  + Clique em "OK" para salvar.
* **Verificar Configuração:**
  + Após adicionar todos os headers, verifique se eles aparecem corretamente na lista conforme a imagem fornecida.
