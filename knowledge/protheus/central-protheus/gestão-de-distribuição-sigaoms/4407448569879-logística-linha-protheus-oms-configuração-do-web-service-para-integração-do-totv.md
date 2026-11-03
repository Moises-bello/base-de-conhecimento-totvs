---
article_id: 4407448569879
category: Gestão de Distribuição (SIGAOMS)
content_hash: 6f995e7c8d976e1acfe26eb42141a840288485b71b02b5365506104cb9680d1b
fetched_at: '2026-06-28T22:45:49.773096+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Configuração do Web Service para integração
  do TOTVS OMS x TOL/TRE
type: support-article
updated_at: '2024-01-05T12:03:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407448569879-Log%C3%ADstica-Linha-Protheus-OMS-Configura%C3%A7%C3%A3o-do-Web-Service-para-integra%C3%A7%C3%A3o-do-TOTVS-OMS-x-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20293431848727) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quais **configurações do Web Service** são necessárias para integração do **TOTVS OMS x TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para que a integração do **TOTVS OMS x TOL/TRE** seja realizada, abaixo descrevemos  os itens a serem avaliados, além da documentação completa que está disponível, logo abaixo no **Saiba mais**:  
1. Configuração **Webservice****AppServer** **Protheus**:  
Para que seja possível **receber as viagens** do **TOL/TRE**  é necessário configurar um **Webservice** no servidor de aplicação **Protheus**. A configuração do **JOB** do **Webservice** para ser utilizado nesta integração não utiliza os métodos padrão do **Framework Protheus**, sendo assim as rotinas **ONSTART** e **ONCONNECT** são específicas do módulo, portanto, os métodos disponíveis neste **WS** não são listados no **WS do Protheus**.  
  
2. É recomendado criar um **Webservice** com as seguintes configurações, modificando o arquivo **Appserver.ini**:  
  
**;Serviço webserver HTTP**  
[HTTP]  
ENABLE=1  
PATH=<Caminho\_Cache\_imagens>;C:\TOTVS\Prottheus\data\web  
PORT=<porta>;8080  
INSTANCES=<nInicio>,<nMaximo>;1,10  
SESSIONTIMEOUT=60  
INSTANCENAME=WS\_HTTP  
  
**;URL de resposta**  
[<ip ou nome>:<porta>/neolog]  
ENABLE=1  
PATH=<Caminho\_Cache\_imagens>;C:\TOTVS\Prottheus\data\web  
ENVIRONMENT=<ambiente>  
INSTANCENAME=WS\_NEOLOG  
RESPONSEJOB=JOB\_WS\_NEOLOG  
DEFAULTPAGE=wsindex.apw  
  
**;JOB de resposta**  
[JOB\_WS\_NEOLOG]  
TYPE=WEBEX  
ENVIRONMENT=<ambiente>  
INSTANCES=<nInicio>,<nMaximo>;1,10  
INSTANCENAME=JOB\_WS\_NEOLOG  
ONSTART=OMSXStart  
ONCONNECT=OMSXConnect

3. Para que seja possível **reprogramar ou cancelar as viagens** do **TOL/TRE** é necessário configurar as informações de conexão com o **DBAccess** diretamente na seção **Environment,** modificando o arquivo **Appserver.ini**, conforme exemplo abaixo:  
  
**;Nome do Ambiente acessado pelo Webservice**  
[Environment]  
SourcePath=C:\Totvs\Protheus\Apo  
RootPath=C:\Totvs\Protheus\Data  
StartPath=\system\  
. . . ; outras chaves  
DBDatabase=MSSQL  
DBAlias=PLS101  
DBServer=192.168.1.20  
DBPort=7890  
  
Para testar o serviço, inicie um navegador e digite:  
**http://<ip ou nome>:<porta>/neolog/PublishReleasedTrip.APW?WSDL**.  
Um **WSDL** - descrição do serviço em **XML** será exibido no navegador.

![Capture.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4407534900375)

4. Para evitar inconsistências do tipo **Failed Handshake SSL**recomenda-se incluir a seguinte configuração no **Appserver.ini**:  
  
[SSLConfigure]  
TryProtocols=1  
Verbose=1  
  
Logo abaixo anexamos um exemplo de um arquivo  **Appserver.ini****Saiba mais**Mais informações poderão ser acessadas no *link*: [Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-Log%C3%ADstica-Linha-Protheus-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOL)  
  
**Anexo**  
Acesse o exemplo de arquivo **Appserver.ini**, com as configurações acima.  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
