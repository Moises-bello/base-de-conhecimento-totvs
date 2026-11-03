---
content_hash: 29948ce97e197b400aa24287211bafef5ad8707d2c04285a159600b9bce4e0b5
fetched_at: '2026-06-29T00:05:58.289734+00:00'
page_id: '185748469'
product: rm
source: tdn-rm
title: FAQ - Utilização de DataServers RM via WebServices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185748469
version: 6
---

# **O que é o Soap?**

---

**Soap** (*Simple Object Access Protocol*, em português Protocolo Simples de Acesso a Objetos) é um [protocolo](http://pt.wikipedia.org/wiki/Protocolo "Protocolo") para troca de informações estruturadas em uma plataforma descentralizada e distribuída.

A mensagem Soap é baseada na estrutura XML, e normalmente utiliza protocolos da camada de aplicação, mais notavelmente em chamada de procedimento remoto (RPC) e Protocolo de transferência de hipertexto (HTTP), para negociação e transmissão de mensagens.

# **O que é o SoapUI?**

---

SoapUI é uma solução para testes funcionais livre e *opensource*. Ele permite que facilmente você crie e execute testes funcionais, de regressão, de conformidade e de carga automatizados. Em um ambiente de teste unitário, SoapUI fornece cobertura de teste completo e suporta todos os protocolos e tecnologias padrão, tais como SOAP, REST, HTTP, JMS, AMF e JDBC.

Site oficial: [www.soapui.org](file:///C:/Users/breno.batista/Desktop/www.soapui.org)

# **Qual relação o SoapUI tem com os DataServers RM?**

---

A arquitetura do RM trabalha com estruturas de dados chamadas DataServers, responsáveis por executarem os principais serviços de manutenção dos dados pela aplicação. Por sua vez, os DataServers RM permitem que você manipule e persista os dados sem o auxílio da MDI RM, por meio de um WebService.

Neste momento o SoapUI entra em cena, pois este permitirá você enviar mensagens estruturadas para o Dataserver RM, para trabalhar com registros no sistema. Uma vez configurado devidamente, e repassando ao DataServers RM a mensagem via WebService, o sistema submeterá os dados e fará as validações competentes aos métodos do DataServers.

**Fique atento:** Lembrando que o SoapUI não é a ferramenta que fará a integração de sistemas externos e RM, ele server apenas como interface para você testar suas solicitações aos serviços disponibilizados pelos DataServers da RM.

# **Como configuro o SoapUI para funcionar em conjunto com os DataServers RM?**

---

É preciso inicialmente efetuar algumas configurações para que o SoapUI comunique corretamente com o DataServer RM. São elas:

1. Acrescentar a tag abaixo no arquivo de config do Host do RM. Observe que é necessário que o nome da Alias do banco a ser utilizado seja CorporeRM

   false

   <appSettings>

   <add key="DefaultDB" value="CorporeRM" />

    </appSettings>
2. Com o SoapUI aberto, crie um novo projeto:
3. Preencha os dados para conexão com o WebService RM. É preciso que o Host esteja em execução. Dê OK.

   Preenchendo os dados para conexão com o WebService.
4. Veja que no endereço está apresentando qual o local onde o host está em execução (localhost) e qual porta será utilizada para efetuar a comunicação com os Dataservers (8051). A tag de configuração no config do Host referente a esta porta é a “HTTPPORT”.
5. Neste momento será criada a árvore com os métodos e as requisições para comunicação com os DataServersRM.

# **Como inicializo uma requisição ao DataServer RM via SoapUI?**

---

Depois de conectar ao WebService RM, estarão disponíveis uma série de métodos para que sejam criadas as requisições. Utilizaremos o **RM\_IwsDataServer** para trabalhar com os DataServers RM. Veja como é apresentado no SoapUI:

Lista em árvore dos métodos utilizados pelos dataservers RM.

Expanda o método ReadRecord, e clique duas vezes no Request. Uma template da mensagem a ser enviada ao DataServer é gerada automaticamente, basta preenchermos devidamente os dados. Abaixo estão exemplos das mensagens para salvar e ler os registros no sistema:

falseTemplate da mensagem do ReadRecord (Leitura de Registros):

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
  <soapenv:Header/>  
  <soapenv:Body>  
    <tot:ReadRecord>  
      <!--Optional:-->  
      <tot:DataServerName>?</tot:DataServerName>  
      <!--Optional:-->  
      <tot:PrimaryKey>?</tot:PrimaryKey>  
      <!--Optional:-->  
      <tot:Contexto>?</tot:Contexto>  
    </tot:ReadRecord>  
</soapenv:Body>  
</soapenv:Envelope>

falseTemplate da mensagem do SaveRecord (Gravação de Registros):

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

<soapenv:Header/>  
  <soapenv:Body>  
    <tot:SaveRecord>  
      <!--Optional:-->  
   <tot:DataServerName>?</tot:DataServerName>  
      <!--Optional:-->  
      <tot:XML>?</tot:XML>  
      <!--Optional:-->  
      <tot:Contexto>?</tot:Contexto>  
    </tot:SaveRecord>  
  </soapenv:Body>  
</soapenv:Envelope>

Neste momento será criada a árvore com os métodos e as requisições para comunicação com os DataServersRM.

# **Para toda *request* solicitada é preciso preencher o usuário e senha. Como proceder nesta configuração?**

---

Devemos configurar qual o usuário e senha do sistema utilizaremos para fazer login, antes de executar os processos de leitura e gravação. Para tal, existe uma janela de propriedades que é aberta por *Request* selecionada.

 As duas propriedades em destaque devem ser preenchidas com o nome do usuário do sistema e sua senha:

**Fique atento:** Para toda *request* solicitada é preciso preencher o usuário e senha, caso contrário a mensagem não poderá ser enviada ao dataserver.

**Como obtenho a estrutura XML da mensagem de ReadRecord a ser enviada ao DataServer RM?**

---

A resposta de uma requisição *ReadRecord* é uma boa forma de obtermos a estrutura XML para a inserção de novos registros (*SaveRecord*). Basicamente é preciso enviar dados como a *primary key*, contexto, e o dataserver que você deseja obter resposta.

**Via requisição *ReadRecord* direto no SoapUI, com os parâmetros preenchidos...**

falseExemplo de requisição ReadRecord:

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
  <soapenv:Header/>  
  <soapenv:Body>  
    <tot:ReadRecord>  
      <!--Optional:-->  
      <tot:DataServerName>GlbCalendData</tot:DataServerName>  
      <!--Optional:-->  
      <tot:PrimaryKey>0000008</tot:PrimaryKey>  
      <!--Optional:-->  
      <tot:Contexto>CODCOLIGADA=1;CODSISTEMA=G;CODUSUARIO=mestre</tot:Contexto>  
    </tot:ReadRecord>  
  </soapenv:Body>  
</soapenv:Envelope>

**... obtemos uma resposta como a abaixo:**

falseExemplo da Resposta:

<s:Envelope xmlns:s="<http://schemas.xmlsoap.org/soap/envelope/>">  
  <s:Body>  
    <ReadRecordResponse xmlns="<http://www.totvs.com/>">  
      <ReadRecordResult>  
        <![CDATA[<GlbCalend>  
  <xs:schema id="GlbCalend" xmlns="" xmlns:xs="<http://www.w3.org/2001/XMLSchema>"  
   ...

   </xs:schema>

  <GCalend>  
    <CODIGO>0000008</CODIGO>  
    <NOME>Calendário 2.008</NOME>  
  </GCalend>  
  <GFeriado>  
<CODCALENDARIO>0000008</CODCALENDARIO>  
<DIAFERIADO>2007-02-05T00:00:00</DIAFERIADO>  
    <NOME>Carnaval</NOME>  
    <FERIADO>T</FERIADO>  
    <TIPO>NA</TIPO>  
  </GFeriado>  
</GlbCalend>]]>

</ReadRecordResult>  
    </ReadRecordResponse>  
  </s:Body>  
</s:Envelope>

Quando extraímos apenas a parte do XML que constará na parte destacada em verde acima, encontramos algo como a estrutura abaixo. Esta será a responsável para trabalhar com inserções de dados no sistema.

Basta copiar a estrutura abaixo...

false

<![CDATA[

<GlbCalend>  
  <GCalend>  
    <CODIGO>0000008</CODIGO>  
    <NOME>Calendário 2.008</NOME>  
  </GCalend>  
  <GFeriado>  
    <CODCALENDARIO>0000008</CODCALENDARIO>  
    <DIAFERIADO>2007-02-05T00:00:00</DIAFERIADO>  
    <NOME>Carnaval</NOME>  
    <FERIADO>T</FERIADO>  
    <TIPO>NA</TIPO>  
  </GFeriado>  
</GlbCalend>  
 ]]>

... e colá-la no campo XML do SaveRecord do SoapUI, preenchendo o valor desejado nos campos e em seus parâmetros (Contexto, DataServerName...):

false

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">

  <soapenv:Header/>  
  <soapenv:Body>  
    <tot:SaveRecord>  
      <!--Optional:–>  
      <tot:DataServerName>GlbCalendData</tot:DataServerName>  
      <!--Optional:–>  
      <tot:XML>  
        <![CDATA[  
       <GlbCalend>  
             <GCalend>  
                    <CODIGO>0000008</CODIGO>  
                    <NOME>Calendário 2.008</NOME>  
             </GCalend>  
             <GFeriado>  
                    <CODCALENDARIO>0000008</CODCALENDARIO>  
                    <DIAFERIADO>2007-02-05T00:00:00</DIAFERIADO>  
                    <NOME>Carnaval</NOME>  
                    <FERIADO>T</FERIADO>  
                    <TIPO>NA</TIPO>  
             </GFeriado>  
       </GlbCalend>  
             ]]>  
      </tot:XML>  
      <!--Optional:–>  
      <tot:Contexto>CODCOLIGADA=1;CODSISTEMA=G;CODUSUARIO=mestre</tot:Contexto>  
    </tot:SaveRecord>  
 </soapenv:Body>  
</soapenv:Envelope>

**Fique atento:** Lembrando que se os dados de PK não forem enviados devidamente não será retornado mais do que uma XSD sem o XML necessário à gravação do registro.

# **Como sei se a mensagem enviada funcionou?**

---

No caso das mensagens de *ReadRecord* a validação se a requisição funcionou basicamente é se você conseguir encontrar o XML que a resposta lhe informar. No caso do *SaveRecord* a resposta é mais simples, e possui a estrutura abaixo:

false Resposta da requisição do SaveRecord:

 <s:Envelope xmlns:s="<http://schemas.xmlsoap.org/soap/envelope/>">  
  <s:Body>  
    <SaveRecordResponse xmlns="<http://www.totvs.com/>">  
      <SaveRecordResult>      
1;00002;5  
      </SaveRecordResult>  
    </SaveRecordResponse>  
  </s:Body>  
</s:Envelope>

É preciso analisar a mensagem para verificar a mensagem para saber se houve a inserção/atualização do registro. Neste campo poderão ser apresentados erros comuns à MDI RM, como violação de chave estrangeria, chave duplicada, etc.

**Página: .**
