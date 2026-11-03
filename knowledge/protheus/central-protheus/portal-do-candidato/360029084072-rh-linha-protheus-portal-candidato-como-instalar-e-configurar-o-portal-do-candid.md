---
article_id: 360029084072
category: Portal do Candidato
content_hash: 24193bf4f15cdf4ba357f983c26a4bc2400913195109ded7869a6a42da37a613
fetched_at: '2026-06-28T22:42:57.856510+00:00'
product: protheus
section_id: 360005048093
source: central-protheus
title: RH - Linha Protheus - PORTAL CANDIDATO - Como Instalar e Configurar o Portal
  do Candidato
type: support-article
updated_at: '2023-06-23T18:34:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029084072-RH-Linha-Protheus-PORTAL-CANDIDATO-Como-Instalar-e-Configurar-o-Portal-do-Candidato
---

**Dúvida**Como Instalar e Configurar o Portal do Candidato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Candidato - Todas as versões  
  
**Solução**1 - Faça o download do arquivo ***WEB\_FILES*** no portal do cliente e descompacte na pasta **systemload;**

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A21%3A56.png?version=1&modificationDate=1478547596000&api=v2)

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A22%3A36.png?version=1&modificationDate=1478547596000&api=v2)

2 - Acesse o**SRVWIZARD**via *SmartClient*para abrir o visualizador oficial de **appserver.ini;**

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A29%3A24.png?version=1&modificationDate=1478547596000&api=v2)

3 - Na sessão**Servidor Internet (HTTP/FTP)** configure a porta de Acesso HTTP;

Necessário configurar o ambiente que utilizará a porta e qual a portal de conexão. Esta porta será a definição do URL de acesso no futuro.

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A29%3A55.png?version=1&modificationDate=1478547596000&api=v2)

4 - Acesse a pasta **módulos web****,**clicque em incluir e selecione a opção**WS - Microsiga Protheus *Web Services;***

**Módulo *Web*:** Será inserido o nome do módulo que será configurado, sendo neste caso o ***WEB SERVICE***

**Nome da Instância:** Nome da pasta que será criada para guardar os arquivos

**Diretório Raiz das imagens (*Web Path*):** Diretório raiz é preenchido automaticamente a partir do nome da instância;

**Selecione o *Enviroment*:** Nome do ambiente que será configurado o ***WEB SERVICE***

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A30%3A44.png?version=1&modificationDate=1478547596000&api=v2)

Após a configuração e clicar em avançar, será demonstrado o relacionamento de URL de acesso e empresas:

Neste momento será incluso um *link* utilizando a porta que configuramos antes e relacionaremos com um vínculo de empresa/ filial.

**Observação**: Sempre será necessário configurar um ***web service*** para cada empresa/filial e para acesso ao portal existem licenças específicas que necessitam da contratação do cliente.

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A31%3A24.png?version=1&modificationDate=1478547596000&api=v2)

Configurar a quantidade de usuários por consumo de licença por job de serviço do porta:

Por padrão, se efetua o apontamento de 1 – 10 que é o máximo de usuário por consumo de licença.

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A32%3A13.png?version=1&modificationDate=1478547596000&api=v2)

**"WS"** Criado:

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A32%3A39.png?version=1&modificationDate=1478547596000&api=v2)

**Obs:**Guarde ou salve em um bloco de notas a URL de acesso antes de salvar para utilizar no próximo passo.

5 - Acesse novamente a pasta **módulos web,**clique em incluir e selecione a opção**Portal do Candidato(PC);**

A única diferença é que agora você deve informar o URL do **web service** contendo**“HTTP://”** para que o *job* encontre as informações do ***web service.***

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A39%3A48.png?version=1&modificationDate=1478547632000&api=v2)

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A38%3A50.png?version=1&modificationDate=1478547596000&api=v2)

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A40%3A54.png?version=1&modificationDate=1478547699000&api=v2)

**"PC"** criado:

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A41%3A14.png?version=1&modificationDate=1478547719000&api=v2)

6 - Reinicie o *Server;*

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A42%3A16.png?version=1&modificationDate=1478547781000&api=v2)

7 - Observe que no **appserver.ini** será criado automaticamente a configuração do Portal:

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A43%3A39.png?version=1&modificationDate=1478547863000&api=v2)

8 - Acesse e teste aos *links* de Web Service e Portal do Candidato.

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A44%3A43.png?version=1&modificationDate=1478547927000&api=v2)

![](http://tdn.totvs.com/download/attachments/268801793/image2016-11-7%2017%3A45%3A2.png?version=1&modificationDate=1478547947000&api=v2)  
**Saiba Mais**  
[Artigos Portal do Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0)
