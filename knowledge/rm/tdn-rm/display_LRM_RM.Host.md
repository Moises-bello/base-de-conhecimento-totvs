---
content_hash: e212a1e2bc3eb4a4868e282a4d0406bc7755d47ab05d9813aef2c35a41424ae9
fetched_at: '2026-06-29T00:09:37.329568+00:00'
page_id: '425459586'
product: rm
source: tdn-rm
title: RM.Host
type: documentation
url: https://tdn.totvs.com/display/LRM/RM.Host
version: 10
---

**RM.Host**

---

Os Web Services também podem ser hospedados diretamente no RM.Host.   
    
 **1º - Alterar no RM.Host.Exe.Config**

Realize a seguinte configuração no RM.Host.Exe.Config:   
    
 <appSettings>  
<add key="DEFAULTDB" value="CORPORERM" />  
 </appSettings>

**2º Consumindo os Web Services**

Para consumir os Web Services do TOTVS Business Conector é necessário a passagem do Token de Segurança, fazendo com que não seja possível consumir os web services através do browser (exceto o web service wsDataServer, que possui alguns WebMethods que podem ser consumidos no browser).   
  
 É necessário utilizar um aplicativo (como por exemplo, a solução SOAPUI) que realiza autenticação SOAP, instanciar o Web Service por ela e executar um ou mais WebMethods tratando os parâmetros necessários em cada caso.   
  
 No RM.Host, também é necessário que o Certificado de Segurança seja configurado no cliente, de acordo com o aplicativo utilizado para consumir os WS.   
  
 Para consultar a lista completa dos Web Services consulte o seguinte endereço:  \*+[http://localhost:8051/wsPageIndex/+\*](http://localhost:8051/wsPageIndex/+*)  
  
 Sendo "localhost" substituído pelo nome ou IP correspondente.   
  
 O valor da porta (8051) é definido pela tag  **HttpPort**.

* **HttpPort**

A tag encontra-se no arquivo "rm.host.exe.config" ou "rm.host.service.exe.config".  
 Descrição: Porta utilizada pela comunicação WCF (CommunicationStyle = WCF) quando o protocolo de comunicação for HTTP (WcfProtocol = HTTP). Caso a comunicação esteja sendo feita em Remoting, desconsidere este parâmetro.   
    
 Tanto o Server quanto o Client devem estar configurados sempre na mesma porta, para que possam se comunicar corretamente.   
 Exemplo:  <add key="HttpPort" value="1234" />   
 Default: 8051  
    
 **4º Configurações para Geração de Logs**

* **TraceFile**

Descrição: A tag TraceFile indica se algum log de execução do host será salvo dentro da pasta (...)CorporeRM\Logs\Broker.  
    
 Caso não se consiga enxergar os Web Services, realize a configuração abaixo na tag para que os logs da execução do Host sejam carregados, possibilitando a análise de alguma inconsistência.  
     
 Exemplo: <add key = "TraceFile" value = "True">

Veja mais em: 

* **System Diagnostcs:**

Descrição: O namespace System.Diagnostics oferece classes que permitem a interação com os processos do sistema, Logs de Evento e Contadores de Performance.  
    
 A principal funcionalidade desta tag é a chamada de log quando os Web Services são consumidos.  
    
 *Observação:* Esta tag proporciona **exclusivamente** os logs de erro ou de alerta **quando** os Web Services são **consumidos**.  
    
 A configuração deve ocorrer no arquivo RM.Host.exe.config ou RM.Host.Service.exe.config, conforme **exemplo** abaixo:  
    
 <?xml version="1.0" encoding="utf-8"?>  
 <configuration>  
 <appSettings>  
 <add key="DEFAULTDB" value="CORPORERM" />  
 <add key = "TraceFile" value = "True">  
 </appSettings>  
 **<system.diagnostics>**  
 **<trace autoflush="true" />**  
 **<sources>**  
 **<source name="System.ServiceModel" switchValue="Error, Warning" propagateActivity="true">**  
 **<listeners>**  
 **<add name="wcfTraceListener" type="System.Diagnostics.XmlWriterTraceListener" initializeData="RM.host.exe.svclog" />**  
 **</listeners>**  
 **</source>**  
 **</sources>**  
 **</system.diagnostics>**  
 </configuration>
