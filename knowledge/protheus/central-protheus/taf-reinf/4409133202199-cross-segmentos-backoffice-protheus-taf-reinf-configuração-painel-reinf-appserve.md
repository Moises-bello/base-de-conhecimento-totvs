---
article_id: 4409133202199
category: TAF - REINF
content_hash: d78fa99a664f75568b2308fb2676150eacb26b0d0aa899135c79939468fcf901
fetched_at: '2026-06-28T22:41:33.544989+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Configuração Painel
  Reinf - Appserver
type: support-article
updated_at: '2023-04-04T12:14:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409133202199-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-Appserver
---

**Dúvida**

Como configurar o Painel REINF.

**Ambiente**

TAF - A partir de 12.1.23

**Solução**

O Painel REINF tem como objetivo centralizar as tarefas referentes a entrega da obrigação Fiscal EFD-REINF. Anteriormente as mesmas eram realizadas em diversas rotinas dentro do TAF. A partir de agora com poucos cliques será possível realizar as principais tarefas como: apuração, transmissão e monitoramento de eventos, incluindo os eventos de fechamento e reabertura de período, de uma maneira muito mais intuitiva. Além de ter uma visão geral através de um painel de eventos que permite a extração dos relatórios das entregas.

A configuração envolve atualização do ambiente e configuração do appserver.ini.

### Atualização

OBS: as configurações do appserver.ini **não deve** ser efetuadas no appserver.ini do TSS, pois são produtos diferentes.

Para o correto funcionamento o ambiente precisa está atualizado, binário desatualizado gera tela em branco ao acessar o ambiente, lib desatualizada gera erro na conexão do Rest, entre outros erros.

[MP - TAF - REINF - Atualização Completa REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-MP-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-REINF?source=search)

Binários (Harpia - Release 12.1.33 e Lobo Guará - Release 12.1.27):

AppServer: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/appserver>

Smartclient: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/smartclient>

[Procedimento para atualizar o binário do Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=224123650)

Lib: <https://suporte.totvs.com/portal/p/10098/download#detail/989259>

Para mais detalhes da rotina e como utilizar a mesma:

<https://tdn.totvs.com/display/TAF/Painel+REINF>

### Configuração Appserver

Há **duas** formas de configurar o Painel Reinf:

**Utilizando Porta Multiprotocolo (recomendado)**

Recomendamos que seja efetuada a configuração do Painel Reinf conforme a documentação a seguir:

[TAF - REINF - Configuração Painel Reinf utilizando MPP - Porta Multiprotocolo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415235211799-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-utilizando-MPP-Porta-Multiprotocolo?source=search)

Caso não seja efetuada a configuração com porta MPP, seguir o passo abaixo:

**Utilizando REST e HTTP (Obsoleto)**

O Painel da Reinf utiliza a integração via RestAPI e Frameworks Web para a parte visual. Nesse tipo de arquitetura, é necessário realizar algumas configurações adicionais sendo elas:

* Criação do serviço REST
* Criação do serviço HTTP Server

O formato é:

[HTTP]  
Enable=1  
Port={porta-http-desejada}  
Path={mesmo-caminho-do-rootpath-do-ambiente-utilizado}/http-root (valor fixo)

Inserir também a chave MAXSTRINGSIZE=10 na seção GENERAL

As configurações são feitas no arquivo AppServer.ini seguindo o exemplo:

**AppServer.ini**

**Para ambiente com balanceamento é necessário criar um ini REST para configuração do Painel REINF.**

;EXEMPLO  
  
[ONSTART]  
JOBS=HTTPJOB  
REFRESHRATE=120  
  
[HTTPJOB]  
MAIN=HTTP\_START  
ENVIRONMENT=IPFIS229  
  
[HTTPV11]  
Enable=1  
Sockets=HTTPREST  
  
[HTTPREST]  
Port=3000  
IPsBind=  
URIs=HTTPURI  
Security=1  
  
[HTTPURI]  
URL=/rest  
CORSEnable=1

PrepareIn=T1-------->  Código da empresa, para grupos com mais de uma empresa conteúdo "**ALL**"  
Instances=2,2  
AllowOrigin=\*

Obs: não utilizar a linha **PrepareIn**  em release inferior a 33 na seção **HTTPURI**, pois gera consumo de licenças.  
  
[HTTP]  
Enable=1  
Port=8081  
Path=c:\users\totvs\protheus\_data\http-root

Inserir também a chave MAXSTRINGSIZE=10 na seção GENERAL

**WEBAPP**

Caso o Webapp (Smartclient HTML) seja utilizado para acesso ao Painel Reinf, é necessário configurações adicionais:

Na seção HTTP:

[HTTP]  
Enable=1  
Port=8081  
Path=c:\users\totvs\protheus\data\http-root

**Cache-Control = no-store**

**XFRAMEOPTIONS = ALLOW-FROM \***

Na seção WEBAPP

[WEBAPP]  
PORT=8989  
WebSocket=1  
**HttpHeaders\_Options={"Access-Control-Allow-Origin": "HTTP://IP"}**(onde, IP, deve ser substituído pelo IP que será utilizado na comunicação com o HTTP do Painel)

Caso o ambiente utilize o MeuRH, avaliar a documentação:

[TAF - REINF - Configuração Painel REINF para ambiente que Utiliza MEU RH com chave de baixo consumo de licença Habilitada.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004554961-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-REINF-para-ambiente-que-Utiliza-MEU-RH-com-chave-de-baixo-consumo-de-licen%C3%A7a-Habilitada-?source=search)

## Parâmetros

Para que o cliente consiga concluir a configuração informar o conteúdo dos parâmetros abaixo.

* Parâmetro **MV\_GCTPURL**  conteúdo http://{hostname-do-servidor}:{porta-http}
* Parâmetro **MV\_BACKEND** conteúdo <http://{hostname-do-servidor}:{porta-rest}/rest>
* Criar o parâmetro **MV\_TAFPO** do tipo lógico, com .T. se possui mais módulos de Protheus além do TAF ou possui mais de uma placa de rede no servidor onde está sendo executado o serviço HTTP e com .F. se possui apenas o TAF Segregado e apenas uma placa de rede;

Documentação completa

<https://tdn.totvs.com/display/public/TAF/Painel+REINF#PainelREINF-Instala%C3%A7%C3%A3o>
