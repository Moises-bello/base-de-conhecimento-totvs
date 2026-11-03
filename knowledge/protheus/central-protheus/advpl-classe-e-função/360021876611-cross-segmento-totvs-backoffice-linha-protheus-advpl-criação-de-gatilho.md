---
article_id: 360021876611
category: ADVPL - Classe e Função
content_hash: 7d204002239088a3428fd910888ebe2b6889cd5c8077791c7d0724fb53ef6697
fetched_at: '2026-06-28T22:40:14.134166+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Criação de gatilho
type: support-article
updated_at: '2021-11-19T13:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021876611-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-gatilho
---

**Dúvida**Como realizar a criação de Gatilho na rotina de compras no padrão MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**Disponibilizamos o exemplo conforme abaixo:

```
User Function GatSN3()  
  
Local lRet := .T.  
  
Local oModel    := FWModelActive()  
  
Local cDesc     := oModel:GetValue('SN1MASTER','N1_DESCRIC')  
  
oModel:SetValue('SN3DETAIL','N3_HISTOR',cDesc)  
  
Return lRet
```

Outro exemplo na CN9

| Domínio | Sequencia | Contra Domínio | Regra | Posiciona? |
| --- | --- | --- | --- | --- |
| CN9\_CLIENT | 001 | CNC\_CLIENT | u\_GatCN9() | Não |

```
#Include "Protheus.ch"  
  
  
User Function GatCN9()  
Local lRet := .T.  
Local oModel := FWModelActive()  
Local cDesc := oModel:GetValue('CN9MASTER','CN9_CLIENT')  
  
oModel:SetValue('CNCDETAIL','CNC_CLIENT',cDesc)  
  
Return lRet
```
