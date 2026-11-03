---
article_id: 14552650424599
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 471e508d539cc105d184e76f1a0b4b428bb852c3ae139e6784ca428196f0e31a
fetched_at: '2026-06-28T22:45:20.940665+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como criar serviço REST
  para integração entre Quírons e TAF
type: support-article
updated_at: '2026-06-26T12:16:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14552650424599-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-criar-servi%C3%A7o-REST-para-integra%C3%A7%C3%A3o-entre-Qu%C3%ADrons-e-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23702474826135) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como criar serviço REST no Protheus para integração entre **Quírons e TAF** ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial  - Configuração - Todas as versões  
  
**Solução**

1 - Pare todos os serviços do Protheus (Servidor de Aplicação, Servidor de Licenças, DBAccess, Ctree, etc);

2 - Faça uma cópia da pasta **appserver** (Ex.: crie uma pasta "*appserver\_REST\_TAF\_QUIRONS*");

3 - **Nesta nova pasta**, abra o arquivo **appserver.ini** e altere a porta da seção **[TCP]** para uma nova porta de sua preferência;  
  
4 - Se for iniciar o **appserver** como um serviço, altere o nome do serviço na seção **[Service]** o renomeie a chave **DisplayName** para diferenciar os serviços existentes;

5 - Para que o serviço funcione de forma adequada, as seções e os parâmetros deverão ter as seguintes configurações:

[TAF\_QUIRONS]  
**SourcePath=CAMINHO DO RPO**  
**RootPath=CAMINHO PROTHEUS DATA**  
StartPath=\SYSTEM\  
RpoDb=top  
RpoLanguage=portuguese  
RpoVersion=120  
LocalFiles=ctree  
localdbextension=.dtc  
Logprofiler=0  
TOPMEMOMEGA=1  
TAFMultInt=1  
x2\_path=\data\

[Drivers]  
Active=TCP

[TCP]  
TYPE=TCPIP  
**Port=PORTA DE SUA ESCOLHA**

[General]  
InstallPath= CAMINHO CONSOLE.LOG  
consolelog=1  
Segmento=YddTQHWW=VZF=yhu  
Serie===AV  
MaxStringSize=10  
BUILDKILLUSERS=1  
CheckSpecialKey=0

[SERVICE]  
NAME=TOTVS-TAF\_QUIRONS  
DISPLAYNAME=TOTVS-TAF\_QUIRONS

**[TopConnect]**  
**Database=BANCO DE DADOS**  
**Server=IP DO BANCO DE DADOS**  
**Alias=NOME DO ALIAS**  
**Port=PORTA DBACCESS**

[HTTPV11]  
SOCKETS=HTTPREST  
ENABLE=1

[HTTPREST]  
**Port=PORTA DE SUA ESCOLHA PARA O REST**  
URIs=HTTPURI  
Security=0

[HTTPURI]  
URL=/rest  
Instances=2,2  
CORSEnable=1  
AllowOrigin=\*

[HTTPJOB]  
MAIN=HTTP\_START  
ENVIRONMENT=TAF\_QUIRONS

[TAF\_CFGJOB]  
MAIN=TAF\_CFGJOB  
Instances=5,30,5,1  
PrepareIn=ALL  
Environment=TAF\_QUIRONS  
RefreshRate=120

**[LICENSECLIENT]**  
**SERVER=IP License Server**  
**PORT=Porta License Server**

[OnStart]  
JOBS=HTTPJOB,TAF\_CFGJOB  
RefreshRate=120

[HTTP]  
Enable=1  
**Port=PORTA DE SUA ESCOLHA PARA O ROOT**  
**Path=CAMINHO DA PASTA HTTP-ROOT NA PROTHEUS DATA**  
Environment=TAF\_QUIRONS

**Observação:**

1. Se o cliente já possuir um appserver.ini contendo as configurações para um serviço REST (ou seja, ele já utiliza um serviço REST no Protheus), o mesmo pode ser utilizado, somente deve-se conferir, se todas as chaves, citadas á cima, estão contempladas no appserver.ini em questão.

Deve-se utilizar no Quírons a mesma porta apontada no appserver, na seção [HTTPREST]

Exemplo:

**[HTTPREST]**  
Port=8081  
URIs=HTTPURI  
Security=0

2. Clientes Cloud (T-Cloud) do TOTVS, precisam solicitar a configuração do serviço REST para integração entre Quírons e TAF para o Cloud:

[Automação Fiscal - Como solicitar suporte TOTVS para o produto, TSS ou Cloud](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413617765783)
