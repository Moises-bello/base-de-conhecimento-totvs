---
content_hash: 7474e1ddb7dce62b832d55cc5da4721a7f8bc7e6d3fed60d8e43523e1cacd8d0
fetched_at: '2026-06-29T00:09:33.461656+00:00'
page_id: '425459037'
product: rm
source: tdn-rm
title: BackOffice Protheus x TOTVS Incorporação - Configuração e Parâmetros Linha
  RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459037
version: 9
---

**Configuração e Parâmetros do TOTVS RM**

---

A integração entre os sistemas TOTVS RM e TOTVS Protheus  deverá ser configurada em ambos os sistemas. Abaixo  serão descritos os passos para a configuração e habilitação dos parâmetros necessários para o funcionamento da integração Backoffice Proteus x Totvs Incorporação.

Esta integração terá algumas particularidades na configuração do WS. Nas integrações que utilizam mensagem única como forma de comunicação entre os aplicativos deve ser realizada uma configuração no web services diferente das outras integrações.

Para utilizar a autenticação customizada (projetos de integração com Mensagem Única) do WebService TBC no IIS7 ou superior, deve ser realizada a configuração abaixo:

**1**. Manter as tags do web.config abaixo:

<!--Inicio - Tags utilizadas para autenticação do tipo "HTTP Basic"-->   
<httpModules>  
<add name="BasicAuthenticationModule" type="RM.Con.Conector.WSSecurity.BasicAuthenticationModule,RM.Con.Conector.WSSecurity"/>  
</httpModules>  
<authentication mode="None"/>  
<authorization>  
<deny users="?"/>  
</authorization>  
<!--Fim→

**2**. Definir o Pool de Aplicativos como "Classic .Net AppPool"  
**3**. As restrições ISAPI e CGI deve ser alteradas de modo que permita ASP.NET.  
Para informações sobre a Mensagem Única, clique aqui.

Para informações sobre a Mensagem Única, [**clique aqui**.](http://tdn.totvs.com/pages/viewpage.action?pageId=425459231)

**Configurador**

A configuração da integração no RM é feita através do configurador acessando o menu Integração, aba Ferramentas e em seguida Configurar.

* **Nome Integração:** Campo apenas informativo insira uma descrição. Exemplo: TOTVS Incorporação x BackOffice Protheus.
* **Nome Reduzido:** Campo apenas informativo insira uma descrição. Exemplo: TINPROT.
* **Sistema Integrado:** Mnemônico que identifica a aplicação de origem. O texto informado nesse campo será enviado no atributo “name” da tag <Product> do XML trafegado na integração. Exemplo: PROTHEUS.
* **URL Web Service:** Endereço do WebService para envio de mensagens.
* **Usuário Autenticação**: Usuário de autenticação do WebService.
* **Senha Autenticação**: Senha de autenticação do WebService.
