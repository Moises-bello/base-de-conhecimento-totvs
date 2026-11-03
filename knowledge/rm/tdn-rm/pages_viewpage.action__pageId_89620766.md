---
content_hash: e1da415fe3582ae8112a5877ee568fb99568f9c0dee786250716fcf4af34d601
fetched_at: '2026-06-29T00:12:01.485440+00:00'
page_id: '89620766'
product: rm
source: tdn-rm
title: Como Expor os Web Services do RM através do Host (recomendado)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=89620766
version: 36
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Este documento tem por objetivo demonstrar qual é o procedimento para configurar o Host para disponibilizar os WebServices responsáveis pela integração de aplicativos de terceiros com o RM.

# Introdução:

---

          Cada WebServices possui os seus métodos. O WebService indicado para consulta de cadastro e inclusão/alteração/exclusão de um cadastro é o wsDataServer. Já o indicado para executar um processo (faturar movimento, cancelar movimento, cancelar lançamento, etc) é o wsProcess.

falsePROCEDIMENTOSProcedimentosProcesso - 01)

          Edite o arquivo RM.Host.Service.exe.config e RM.Host.exe.config, que estão na pasta ***<diretório de instalação do RM>\RM.Net:***

Para configurar as tags pelo RM.Host.ServiceManager.exe, .

Processo - 02)

          Adicione as seguintes tags no bloco de instruções **<appSettings> ... </appSettings>**

<add key="**DEFAULTDB**" value="**CorporeRM**" />

<add key="**HTTPPORT**" value="**8051**" />

false

***No value da tag DefaultDB deve ser informado o Alias, do arquivo Alias.dat que contém a base de dados que será utilizada. Na tag HTTPPORT informe a porta utilizada pelo Host para os serviços via WS (Geralmente é informado o padrão 8051).***

<add key="**ServicesHostName**" value="**DNS da instituição**" />

false

***Para expor os Web Services para acesso externo, torna-se necessária a inclusão da tag ServicesHostName, onde seu valor deverá ser o DNS ou IP Público da instituição.***

<add key="**WebServiceCulture**" value="**Invariant**" />

false

***A tag WebServiceCulture é utilizada para alterar a cultura de leitura e conversão dos dados recebidos pelo WebService.***

***Ex.: Quando utilizado por exemplo o método WsDataServer, o separador decimal é o mesmo da cultura definida no sistema operacional, entretando esta configuração de leitura pode ser alterada quando utilizada a tag "WebServiceCulture" no arquivo .config do host (RM.Host.exe.config ou RM.Host.Service.exe.config).***

Processo - 03)

          Abaixo segue um arquivo de exemplo de configuração do Host:

xmlEclipseRM.Host.exe.config












]]>Processo - 04)

         Configuração necessária para reservar a porta:

         Executar o comando **netsh http add urlacl url=http://+:8051/ user=NetworkService** no prompt de comando do Windows.

  Será exibida uma mensagem de que a URL foi reservada com sucesso, conforme print abaixo:

 

false

***Neste exemplo a porta utilizada é a 8051. Caso deseje adicionar mais serviços do Host com outras portas ou a porta utilizada seja diferente da padrão, deve-se executar o comando netsh para a(s) porta(s) desejada(s).***

 Caso deseje utilizar uma porta diferente da padrão, deve-se alterar o valor da chave HTTPPORT presente no arquivo  ***.config do host***

  
Processo - 05)

          Para verificar se as configurações estão corretas, informe a URL abaixo no browser (Internet Explorer, Mozilla Firefox, etc):

http://<IP ou HostName da máquina em que o Host está configurado>:<porta informada no arquivo de configuração do host, tag HTTPPORT>/wsPageIndex

Ex:

<http://servidor.com:8051/wsPageIndex>

[http://servidor.com:8051/w](http://servidor.com:8051/wsPageIndex)sDataServer

[http://servidor.com:8051/](http://servidor.com:8051/wsPageIndex)wsReport

Ex. WSDL:

<http://localhost:8051/wsReport/MEX?wsdl>

[http://servidor.com:8051/w](http://servidor.com:8051/wsPageIndex)sDataServer/MEX?wsdl

false

***Para a integração de mensagem única, o link a ser utilizado para comunicação com o o RM deve ser composto por:***

***http://<IP ou HostName da máquina em que o Host está configurado>:<porta informada no arquivo de configuração do host, tag HTTPPORT>/EAISERVICE/IConWSEAIService***

***Ex.: http://10.31.8.140:8051/EAISERVICE/IConWSEAIService***

---

Em ambientes MuiltTenancy, veja os detalhes de configuração e utilização aqui: <https://tdn.totvs.com/x/9XwcEQ>

false

**Para consumir os WebServices, utilize um aplicativo que faça uso do protocolo Soap nas chamadas. Indicamos o SoapUI.**

****Para baixar o software,** [Clique aqui](http://sourceforge.net/projects/soapui/files/)**

---

Para maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 2 – (CRM), 3 - (Vendas e CRM) e 3 –  (Microsoft CRM).

falsefalse

**Produto:** Framework - Conector

false

**Versão:** 11.50.XX e Superiores

false

**Processo:** Expor Web Services através do Host

falsefalse

**Status:** Construção

false

**Data:**

false

**Autores:**
