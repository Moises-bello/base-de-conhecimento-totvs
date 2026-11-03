---
article_id: 17383402763287
category: Integrações - Conceito e WebService
content_hash: 5b7623c77fe8005d9d2f462a776267f6c061fcc7db31676d7943bf8cad0def11
fetched_at: '2026-06-28T22:46:44.907782+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP -  Como Habilitar Webservice via RM Host
type: support-article
updated_at: '2025-01-07T18:29:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17383402763287-RH-RM-FOP-Como-Habilitar-Webservice-via-RM-Host
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17383400908183) Tempo aproximado para leitura: 00:05:30 min*****Dúvida**Como Habilitar Webservice via RM **Host**?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Segue abaixo o passo a passo de como habilitar o webservice via HOST.  
1. Edite os arquivos **RM.Host.Service.exe.config** e **RM.Host.exe.config**, que estão na pasta ***<diretório de instalação do RM>\RM.Net:***

![](http://tdn.totvs.com/download/attachments/89620766/WebService-01.png?version=2&modificationDate=1468947806000&api=v2)

2. Adicione as seguintes *tags* no bloco de instruções **<appSettings> ... </appSettings>**

```
<add key="DEFAULTDB" value="CorporeRM" />
```

No *value* da tag **DefaultDB** deve ser informado o Alias, do arquivo Alias.dat que contém a base de dados que será utilizada.

```
<add key="HTTPPORT" value="8051" />
```

Na tag **HttpPort** informe a porta utilizada pelo Host para os serviços via WS (Geralmente é informado o padrão 8051).

```
<add key="ServicesHostName" value="DNS da instituição" />
```

Para expor os *WebServices* para acesso externo, torna-se necessária a inclusão da tag **ServicesHostName**, onde seu valor deverá ser o DNS ou IP Público da instituição.

```
<add key="WebServiceCulture" value="Invariant" />
```

A tag **WebServiceCulture** é utilizada para alterar a cultura de leitura e conversão dos dados recebidos pelo WebService.  
Veja um arquivo de exemplo de configuração do Host:  
**RM.Host.exe.config**

```
<?xml version="1.0"?>  
<configuration>  
 <appSettings>  
  <add key="JobServer3Camadas" value="false" />  
  <add key="Port" value="8050" />  
  <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />  
  <add key="EnableCompression" value="true" />  
  <add key="DEFAULTDB" value="CorporeRM" />  
  <add key="HTTPPORT" value="8051" />  
 </appSettings>  
 <runtime>  
  <gcServer enabled="true" />  
 </runtime>  
</configuration>
```

3. Execute *prompt* de comando do Windows como Administrador e efetue o comando:

```
netsh http add urlacl url=http://+:8051/ user=NetworkService
```

![](http://tdn.totvs.com/download/attachments/89620766/image2017-7-18%2011%3A2%3A58.png?version=1&modificationDate=1500386579000&api=v2)

Será exibida uma mensagem de que a URL foi reservada com sucesso, conforme print abaixo:

![](http://tdn.totvs.com/download/attachments/89620766/image2017-7-18%2011%3A5%3A43.png?version=1&modificationDate=1500386743000&api=v2)

Neste exemplo a porta utilizada é a 8051. Caso deseje adicionar mais serviços do Host com outras portas ou a porta utilizada seja diferente da padrão, deve-se executar o comando **netsh** para a(s) porta(s) desejada(s).

4. Para verificar se as configurações estão corretas, informe a URL abaixo no *browser* (Internet Explorer, Mozilla Firefox, etc):

http://<IP ou **HostName** da máquina em que o **HOST** está configurado>:<porta informada no arquivo de configuração do host, tag **HTTPPORT**>/wsPageIndex  
Exemplo:

```
http://servidor.com:8051/wsPageIndex  
  
http://servidor.com:8051/wsdataserver  
  
http://servidor.com:8051/wsReports
```

Exemplo WSDL:

```
http://localhost:8051/wsReport/MEX?wsdl  
  
http://servidor.com:8051/wsDataServer/MES?wsdl
```

![](http://tdn.totvs.com/download/attachments/89620766/image2013-10-21%2011%3A38%3A25.png?version=1&modificationDate=1382362794000&api=v2)

**Importante**Para consumir os ***WebServices***, utilize um aplicativo que faça uso do protocolo **SOAP**nas chamadas. Um exemplo de ferramenta é a **SoapUI**, para baixar o software, [Clique aqui.](http://sourceforge.net/projects/soapui/files/)
