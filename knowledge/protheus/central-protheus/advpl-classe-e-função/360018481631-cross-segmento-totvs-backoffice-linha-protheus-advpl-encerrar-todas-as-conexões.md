---
article_id: 360018481631
category: ADVPL - Classe e Função
content_hash: 4f96a918b14be6874de51f6441d206091a92283aa0ddf6089650ccbb5b3a698b
fetched_at: '2026-06-28T22:40:14.295049+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Encerrar todas
  as conexões quando solicitado uma compilação
type: support-article
updated_at: '2025-08-04T14:13:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018481631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Encerrar-todas-as-conex%C3%B5es-quando-solicitado-uma-compila%C3%A7%C3%A3o
---

**Dúvida**Como derrubar todas as conexões no momento da compilação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**A chave **buildKillUser** informada no ini do servidor, encerra todas as conexões quando solicitado uma compilação. 

```
[General]  
InstallPath= C:\PROTHEUS  
BuildKillUsers=1  
CONSOLELOG=1  
MAXSTRINGSIZE=10  
DIRINCLUDE=C:\PROTHEUS\include
```

**Saiba Mais**[Arquivo de configuração](http://tdn.totvs.com/pages/viewpage.action?pageId=6064745)  
[Configuração do AppServer e Dbaccess](http://tdn.totvs.com/pages/releaseview.action?pageId=210044134)
