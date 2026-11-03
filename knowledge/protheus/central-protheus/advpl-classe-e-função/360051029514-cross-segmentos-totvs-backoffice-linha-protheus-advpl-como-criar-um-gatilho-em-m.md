---
article_id: 360051029514
category: ADVPL - Classe e Função
content_hash: 2e13d5b15956680f8b89879258cd8e70504d24147ff48da64f30e2f868575993
fetched_at: '2026-06-28T22:40:19.383026+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Como criar um gatilho
  em MVC
type: support-article
updated_at: '2023-06-27T21:03:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051029514-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-gatilho-em-MVC
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como criar um gatilho em MVC?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**O domínio (X7\_CAMPO) e contra domínio (X7\_CDOMIN) apontando para o mesmo campo que irá disparar a função.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Domínio** | **Sequencia** | **Contra Domínio** | **Regra** | **Posiciona?** |
| N1\_DESCRIC | 001 | N1\_DESCRIC | U\_xGatMVC() | Não |

```
User Function xGatMVC()  
  
Local oModel    := FWModelActive()  
Local cDesc     := oModel:GetValue('SN1MASTER','N1_DESCRIC')  
  
oModel:SetValue('SN3DETAIL','N3_HISTOR',cDesc)  
  
Return cDesc
```

**Observação**Retorne na função o conteúdo esperado pelo campo de **contra domínio.**
