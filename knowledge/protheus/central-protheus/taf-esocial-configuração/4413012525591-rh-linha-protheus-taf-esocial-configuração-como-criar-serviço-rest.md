---
article_id: 4413012525591
category: TAF - eSocial - Configuração
content_hash: 6e1ae291b4420ce55ba6a568f9b2eeda02d0026119065c9fbb2fca8ae6157814
fetched_at: '2026-06-28T22:45:14.490044+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como criar serviço REST
type: support-article
updated_at: '2024-05-24T20:16:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413012525591-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-criar-servi%C3%A7o-REST
---

**Dúvida**Como criar serviço REST no Protheus?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial -Todas as versões   
  
**Solução**

1 - Pare todos os serviços do Protheus (Servidor de Aplicação, Servidor de Licenças, DBAccess, Ctree, etc);

2 - Faça uma cópia da pasta **appserver** (Ex.: appserver\_TAF\_Full);

3 - Nesta nova pasta, abra o arquivo appserver.ini e altere a porta da seção [TCP] para uma nova porta de sua preferência;  
  
4 - Se for iniciar o **appserver** como um serviço, altere o nome do serviço na seção [Service] o Name e o DisplayName para diferenciar os serviços existentes;

5 - Para que funcione do serviço de forma adequada, as seções e os parâmetros deverão ter as seguintes configurações:

[TAF\_FULL]  
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
consolelog=1  
MaxStringSize=10  
  
[SERVICE]  
NAME=TOTVS-TAF-FULL  
DISPLAYNAME=TOTVS-TAF-FULL  
  
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
ENVIRONMENT=TAF\_FULL  
  
[TAF\_CFGJOB]  
MAIN=TAF\_CFGJOB  
Instances=5,30,5,1  
PrepareIn=ALL  
Environment=TAF\_FULL  
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
Environment=TAF\_FULL

**Observação:**

Clientes Cloud (T-Cloud) do TOTVS, precisam solicitar a configuração do TAF do Futuro á área do CLoud:

[Automação Fiscal - Como solicitar suporte TOTVS para o produto, TSS ou Cloud](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413617765783)

6 - Após a criação do serviço deverá ser configurado os parâmetros: MV\_BACKEND e MV\_GCTPURL;

7 - Analise se o parâmetro MV\_BACKEND se está preenchido com a URL do serviço REST:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413012475287)

**Obs.:** O IP, tem que ser o endereço do servidor da Aplicação do TAF. Para confirmar qual a porta da conexão REST, abre o arquivo appserver.ini e verifique a seção [HTTPREST] a porta configurada. **Exemplo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413012483735)**

8 - Verifique outro parâmetro MV\_GCTPURL se está apontando para a URL do serviço HTTP:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413021054743)  
**Obs.:** O IP, tem que ser o endereço do servidor da Aplicação do TAF. Para confirmar qual a porta da conexão HTTP, abre o arquivo appserver.ini e verifique a seção [HTTP] a porta configurada.

**Exemplo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413010736663)**

9 - Verifique o parâmetro **MV\_TAFPO**\*:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413010756631)

* Obs.: Preencher o parâmetro **MV\_TAFPO** com **.T.** se possui mais módulos de Protheus além do TAF ou possui mais de uma placa de rede no servidor onde está sendo executado o serviço HTTP e com **.F.** se possui apenas o TAF e apenas uma placa de rede;
* Se usar o TAF Segregado, usar o valor .F.;

10 - Verifique se as portas configuradas nos parâmetros MV\_BACKEND e MV\_GCTPURL estão liberadas caso possua Firewall ou Proxy;

11 - Realizado a configuração do serviço acesse a rotina Miscelânea > Esocial > Esocial do Futuro:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413021162647)

Se houver erro ou outra inconsistência ao acessar a rotina, encaminhe as seguintes evidências para o time do suporte avaliar:

1. Arquivo console.log REST e console.log do appserver Master;
2. Arquivo appserver.ini do REST e appserver.ini do appserver Master;
3. Print da inconsistência apresentada;
4. Pasta http-root;
5. Caso possua bloqueio encaminhe evidência das portas desbloqueadas no Firewall ou Proxy;
