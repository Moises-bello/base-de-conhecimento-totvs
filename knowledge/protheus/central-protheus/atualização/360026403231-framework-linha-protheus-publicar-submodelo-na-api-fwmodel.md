---
article_id: 360026403231
category: Atualização
content_hash: 11e005a3a36fe64de5627f39ad94496846b1b6a895bceec9d201c61438a2001b
fetched_at: '2026-06-28T22:42:21.277193+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Publicar SubModelo na API FWModel
type: support-article
updated_at: '2024-05-08T11:15:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026403231-Framework-Linha-Protheus-Publicar-SubModelo-na-API-FWModel
---

**Dúvida**Como publicar um submodelo na API FWModel?  
   
 **Ambiente**Protheus - AppServer - Todas as versões  
   
**Solução**Para publicar o submodelo, siga os passos abaixo:  
1. Compile o **User Model** (exemplo abaixo) no RPO:

```
#INCLUDE 'totvs.ch'  
#INCLUDE "fwmvcdef.ch"  
  
PUBLISH USER MODEL REST NAME MATA090 source MATA090
```

2. Chame a API /rest/fwmodel/"Rotina"
