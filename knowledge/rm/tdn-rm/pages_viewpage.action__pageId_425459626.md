---
content_hash: fb4be5a06b36d4a00fa5acccd59adc9a83f79148f4754e9d81b5ce90bd972b77
fetched_at: '2026-06-29T00:09:37.515853+00:00'
page_id: '425459626'
product: rm
source: tdn-rm
title: Internet Information Services (IIS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459626
version: 6
---

**Internet Information Services (IIS)**

---

O IIS é um servidor web desenvolvido para sistemas operacionais Windows Servers. Para que os Web Services do TOTVS Business Conector sejam hospedados no IIS, é necessário instalar:

* Biblioteca RM
* Web Services através do instalador TOTVS Business Connect

Após a instalação, será criado um aplicativo no IIS com o nome *TOTVSBusinessConnect*.   
 Para que os Web Services funcionem corretamente, é necessário configurar o alias e reiniciar o IIS.  
    
 **Alias**  
    
 Para configurar o alias, acesse o arquivo Web.config e altere a tag abaixo informando no lugar de "CORPORE" o alias que será utilizado.

* Diretório do arquivo web.config: C:\totvs\CorporeRM\WS\_TBC
* Tag: <add key="DBAlias" value="CORPORE" />

   
 **Integrações com Mensagem Única**  
    
 Nas integrações que utilizam mensagem única como forma de comunicação entre os aplicativos deve ser realizada uma configuração no web services diferente das outras integrações.  
 Para utilizar a autenticação customizada (projetos de integração com Mensagem Única) do WebService TBC no IIS7 ou superior, deve ser realizada a configuração abaixo:

1. Manter as tags do web.config abaixo:  
 < Inicio - Tags utilizadas para autenticação do tipo "HTTP Basic">   
 <httpModules>  
 <add name="BasicAuthenticationModule" type="RM.Con.Conector.WSSecurity.BasicAuthenticationModule,RM.Con.Conector.WSSecurity"/>  
 </httpModules>  
 <authentication mode="None"/>  
 <authorization>  
 <deny users="?"/>  
 </authorization>  
 <! Fim

2. Definir o Pool de Aplicativos como "Classic .Net AppPool"  
 3. As restrições ISAPI e CGI deve ser alteradas de modo que permita ASP.NET.

* Saiba mais sobre **Mensagem Única**, **clicando aqui****.**

   
 Por default, o alias configurado no web.config é o CORPORE.  
 Após realizar as alterações no alias, reinicie o IIS e o Host.  
    
 **Observação:**

Para que os web services funcionem corretamente, o parâmetro abaixo deve estar igual tanto no arquivo Web.Config quanto no arquivo RM.Host.Exe:  
    
 <add key="JobServer3Camadas" value="false" />   
    
 **Consumindo os Web Services**  
    
 Para consumir os Web Services do TOTVS Business Conector é necessário a passagem do Token de Segurança, fazendo com que não seja possível consumir os web services através do browser (exceto o web service wsDataServer, que possui alguns WebMethods que podem ser consumidos no browser).  
    
 É necessário utilizar um aplicativo (como por exemplo, a solução SOAPUI) que realiza autenticação SOAP, instanciar o Web Service por ela e executar um ou mais WebMethods tratando os parâmetros necessários em cada caso.   
    
 Após realizar as configurações, consulte a lista completa dos Web Services no endereço: <http://localhost/TOTVSBusinessConnect/>

---

**Recursos Adicionais**  
  

Acesse o boletim técnico abaixo para ver mais sobre a configuração do WebService:

[Configuração de WebService para integração com Mensagem Única](http://totvsconnect.blogspot.com.br/2012/11/como-fazer-configuracao-de-webservice)
