---
article_id: 360026230174
category: Portal de Gestão de Capital Humano
content_hash: 77e1c1275453ac0f380ebffc7d4c827eb67966dbf725ae0bc4ff3f1c2a0f74a5
fetched_at: '2026-06-28T22:42:59.239048+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Como efetuar configuração para o Cadastro
  de Artefatos
type: support-article
updated_at: '2021-04-07T12:39:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026230174-RH-Linha-Protheus-PORTAL-GCH-Como-efetuar-configura%C3%A7%C3%A3o-para-o-Cadastro-de-Artefatos
---

**Dúvida**Como efetuar configuração para o Cadastro de Artefatos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Entre no módulo SIGATCF (18) e acesse o menu*> Atualizações > Artefatos > Configurações* para possibilitar o download dos arquivos.  
  
Para facilitar o preenchimento das informações desse cadastro é recomendado ter acesso ao arquivo AppServer do Protheus (AppServer.ini).  
  
Ao clicar em incluir, será necessário preencher os campos abaixo:  
Informe no campo "**Ambiente"** o nome do ambiente utilizado para acesso ao Portal GCH:  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_16-12-49.png?version=1&modificationDate=1551467569673&api=v2)

No arquivo "AppServer.ini" essa informação pode ser encontrada na sessão de configuração do Portal na chave **ENVIRONMENT:**![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_14-25-58.png?version=1&modificationDate=1551461158630&api=v2)  
  
Campo**"IP Servidor"**, informe o endereço de IP do servidor onde o Portal esta configurado.   
Neste exemplo o acesso está sendo efetuado na mesma máquina que o Portal esta instalado, por isso informei Localhost.  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_16-13-21.png?version=1&modificationDate=1551467601867&api=v2)  
  
Essa informação pode ser encontrada na sessão de configuração do Portal (AppServer.ini):  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_14-33-35.png?version=1&modificationDate=1551461615653&api=v2)  
  
Campo**"Porta TCP"**, é a porta utilizada pelo ambiente:  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_17-57-37.png?version=1&modificationDate=1551473857983&api=v2)  
  
No AppServer.ini essa informação está na sessão onde foi configurado a comunicação com o smartclient.  
Neste exemplo minha sessão foi nomeado **TCP**.  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_14-37-50.png?version=1&modificationDate=1551461870287&api=v2)  
  
Campo **"Porta WEB"**, é a porta utilizada pelo Portal para comunicação do web service:  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_17-57-57.png?version=1&modificationDate=1551473877307&api=v2)  
  
No AppServer.ini, essa informação está na sessão HTTP do arquivo.  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_14-43-58.png?version=1&modificationDate=1551462238803&api=v2)  
  
Campo **"End. Pasta"** deve ser informado o caminho da **pasta** onde ficarão os arquivos disponibilizados no portal.  
**Obrigatoriamente a pasta deve estar dentro da pasta Web, definida na configuração do portal.**Neste exemplo o caminho da minha é pasta *C:\ADVPR\_LOCAL\Robo\_DicBanco\Protheus\_Data\Web\pp\Artefatos* a*o* utilizar a barra invertida "\" no começo do caminho, o sistema entende que o caminho informado começa dentro da pasta Protheus\_Data (RootPath do ambiente).  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_18-0-53.png?version=1&modificationDate=1551474053977&api=v2)  
  
No AppServer.ini, podemos identificar o caminho da pasta Web no arquivo:  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_18-4-0.png?version=1&modificationDate=1551474240983&api=v2)  
  
Campo **"Instância"** é informado o nome utilizado na instância do Portal:  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_18-5-38.png?version=1&modificationDate=1551474338453&api=v2)  
  
No AppServer.ini essa informação se encontra na sessão de configuração do Portal, na chave **INSTANCENAME:****![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_18-6-57.png?version=1&modificationDate=1551474417953&api=v2)**Campo **Chave .INI** é a Chave da sessão de configuração do portal no arquivo .INI do aplication server:  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_18-8-14.png?version=1&modificationDate=1551474495130&api=v2)  
  
No AppServer.ini fica localizado na sessão de configuração do Portal:  
  
![](http://tdn.totvs.com/download/attachments/463805869/image2019-3-1_18-8-45.png?version=1&modificationDate=1551474525637&api=v2)  
  
**Observação:** O preenchimento correto dessas informações é essencial para o funcionamento dos artefatos no Portal Gestão do Capital Humano.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
