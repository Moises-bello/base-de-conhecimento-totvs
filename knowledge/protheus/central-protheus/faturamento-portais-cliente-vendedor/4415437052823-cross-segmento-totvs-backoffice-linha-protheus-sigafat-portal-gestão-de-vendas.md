---
article_id: 4415437052823
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 4868f93f4355a83b7be46bc921dc55ae119a75d9509d743789702ebdf4197ba5
fetched_at: '2026-06-28T22:38:24.037810+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Portal Gestão
  de Vendas
type: support-article
updated_at: '2024-04-12T15:06:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415437052823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Portal-Gest%C3%A3o-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15286003328407) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**O que é necessário para configurar o novo Portal Gestão de Vendas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.33  
  
**Solução**

Quer um passo a passo, com vídeos, sobre essa implementação? Acesse: [Implementação Portal Gestão de Vendas](https://tdn.totvs.com/x/Etk1LQ)

O **Portal** **Gestão de Vendas** (PGV) é uma plataforma Web para usuários do **Protheus** que utilizem o modulo **Faturamento** (**SIGAFAT**) para gerenciar as suas vendas.

Para sua utilização é preciso::

* Estar na release 12.1.33 ou superior com binários expedidos a parit de Agosto/2020;
* Realizar a configuração da chave "**UseRowStamp"** no **DBACCESS.**
* **Configurar o AppServer com comunicação [Rest ,](https://tdn.totvs.com/x/84J8B)sendo que para uso do portal é utilizado REST 2.0 de acordo com as TAGS no Exemplo da configuração do appserver.ini;**

****Exemplo da Configuração do APPSERVER.INI****

;==================================================  
;CONFIGURAÇÃO DE PORTAIS - PORTAL GESTÃO DE VENDAS  
;==================================================

**[Drivers]**  
Active=TCP  
MultiProtocolPort=1  
multiprotocolportsecure=0  
Secure=SSL

[**HTTPJOB**]  
ENVIRONMENT=ENVIRONMENT  
MAIN=HTTP\_START

[**HTTPREST**]  
BUGS=0  
HSM=0  
MaxQueue=10  
Port=8282

**SECURITY=1 -> Importante**

Para o correto funcionamento das APIs do **Portal Gestão de Vendas**, é de extrema importância que a chave **SECURITY** do **APPSERVER** esteja habilitada.

SSL2=0

SSL3=0

State=0  
TLS1=0  
URIs=HTTPURI  
Verbose=0

[**HTTPURI**]  
AllowOrigin=\*  
CORSEnable=0  
Instances=1,2  
OnConnect=REST\_CONNECT  
OnExit=REST\_EXIT  
OnStart=REST\_START  
PrepareIn=All  
URL=/rest/

**[HTTPV11]**  
ADVPL=0  
Enable=1  
Sockets=HTTPREST  
TimeOut=120

**[HTTPSERVER]**  
Enable=0  
Servers=HTTP\_REST  
​  
[**HTTP\_REST**]  
hostname=localhost  
port=9995  
locations=HTTP\_ROOT  
​  
[**HTTP\_ROOT**]  
Path=/rest/  
RootPath=root/web  
ThreadPool=THREAD\_POOL  
​  
[**THREAD\_POOL**]  
Environment=ENVIRONMENT  
MinFreeThreads=1  
MinThreads=1  
MaxThreads=10

[**OnStart**]  
JOBS=HTTPJOB  
REFRESHRATE=120

No Appserver.INI validar o preenchimento da Chave **SECURITY=1**;

* Configurar o **[TOTVS Mingle](https://mingle.totvs.com.br/landpage/)**;

Na solicitação passar as seguintes informações:

**Exemplo:**

REST: <http://10.100.11.111:8085/rest>

Grupo/Empresa: 01

Filial: 01 ou 0101

Caso tenha mais de uma filial informar as filiais 01,02,03,04.

* Após as configurações, para entrar na plataforma, o **Vendedor** deve informar o mesmo **Usuário** e **Senha** utilizados no Protheus e informar o Alias;

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Usuário não possui vinculo com um Vendedor! (PGV)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6297344354711-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Usu%C3%A1rio-n%C3%A3o-possui-vinculo-com-um-Vendedor-TGV-)

* Para realizar a inclusão do Pedido de Venda, é necessário que este Vendedor esteja associado ao cliente para visualização da carteira.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15285993869975)

Certifique-se que o **cadastro do cliente** esteja **associado**ao **Vendedor** do Gestão de Vendas, através do campo **A1\_VEND**, somente desta forma, a carteira de clientes aparecerá corretamente no portal de Gestão de Vendas no momento da inclusão do pedido de vendas.

* Na primeira vez que acessar o portal,  a aplicação deverá efetuar a carga inicial. Esta carga é efetuada apenas no primeiro acesso ou caso o usuário seja alterado.

Exemplo de utilização:

**Opção: Meus Pedidos** - usuário pode consulta como incluir pedidos.

![](https://tdn.totvs.com/download/attachments/579468339/Meus%20Pedidos.gif?version=1&modificationDate=1610539989000&api=v2)

**Saiba Mais:**

**[Perguntas mais frequentes do Portal Gestão de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=649301318)**

[DT Descontinuação do programa SetupTGV](https://tdn.totvs.com/pages/releaseview.action?pageId=716359906)

Para mais exemplos  e informações, acesse: **[Portal Gestão de Vendas: Guia de Referencia](https://tdn.totvs.com/x/M-yJIg)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Ao incluir o pedido no portal TGV , não aparece a carteira de clientes do vendedor.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6455673044119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Ao-incluir-o-pedido-no-portal-TGV-n%C3%A3o-aparece-a-carteira-de-clientes-do-vendedor-?source=search)**

**[Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519719292)****- Documentação explica como liberar o REST para acesso externo.**
