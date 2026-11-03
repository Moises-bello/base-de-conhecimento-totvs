---
article_id: 360044820973
category: Ferramentas
content_hash: dc66e2eaebecb4c151bb6421874c6ac70ef57d592f2bd7c06eec50f67eed161a
fetched_at: '2026-06-28T22:42:17.998304+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Como realizar atualização dbapi.dll para os binários
  release 19.3.0.X
type: support-article
updated_at: '2024-05-09T11:06:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044820973-Framework-Linha-Protheus-Como-realizar-atualiza%C3%A7%C3%A3o-dbapi-dll-para-os-bin%C3%A1rios-release-19-3-0-X
---

**Dúvida**Como realizar atualização dbapi.dll para os binários release 19.3.0.X ?  
   
 **Ambiente**MP – A partir da versão 12.1.25 - Binários release 19  
   
**Solução**Para a versão de dbaccess a partir da release 19.2.1.0 a dbapi.dll não fica mais na pasta raiz de instalação do executavel, a dbapi.dll versão 64 bits deve ser copiada da pasta client dentro da pasta raiz de instalação conforme print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060253974)

Este arquivo deve sobrescrever os arquivos dbapi.dll dentro da pasta appserver de todas as aplicação que utilizam este dbaccess para acessar o sistema.
