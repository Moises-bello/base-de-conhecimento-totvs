---
article_id: 360043647533
category: TAF - eSocial - Atualização
content_hash: 3d27da3a28580d2be537354cccfe178646d2fdf441ade687e1a6d7c5beeae5a8
fetched_at: '2026-06-28T22:45:13.357328+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Replicando o SmartClient
  do servidor para outras estações de trabalho
type: support-article
updated_at: '2025-04-11T21:02:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043647533-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Replicando-o-SmartClient-do-servidor-para-outras-esta%C3%A7%C3%B5es-de-trabalho
---

**Dúvida**

Como replicar o aplicativo do TAF para outras máquinas?

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Todas as versões

**Solução**

1 - Com o TAF instalado no Servidor, acesse diretório da instalação e localize a pasta \bin:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059175573)

2 - Acesse a pasta \bin e localize a pasta \smartclient:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059175593)

3 - Copie a pasta \smartclient com o seu conteúdo para outras máquinas;

4 - Acesse o conteúdo da pasta \smartclient e localize o arquivo smartclient.ini. Localize as seções [TCP] e [WS] e veja se o parâmetro Server, está apontando para o servidor onde está instalado o TAF:

**Exemplo:**

*[TCP]*

*Server=192.168.1.50*

*[WS]*

*Server=192.168.1.50*

5 - Após copiar a pasta \smatclient e configurar o arquivo smartclient.ini apontando para o servidor, acesse o arquivo executável smartclient.exe. Pode criar um atalho para área de trabalho:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059175613)
