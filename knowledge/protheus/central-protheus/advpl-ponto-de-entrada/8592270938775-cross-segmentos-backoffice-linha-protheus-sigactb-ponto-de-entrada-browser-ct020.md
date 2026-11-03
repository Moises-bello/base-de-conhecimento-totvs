---
article_id: 8592270938775
category: ADVPL - Ponto de Entrada
content_hash: b82fb4602f80aaac4de916dd7234a06812b2114960f141843c1455e92563826e
fetched_at: '2026-06-28T22:40:12.945398+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGACTB  - Ponto de entrada -
  Browser- CT020ROT
type: support-article
updated_at: '2022-10-10T14:40:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8592270938775-Cross-Segmentos-Backoffice-Linha-Protheus-SIGACTB-Ponto-de-entrada-Browser-CT020ROT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Ponto de entrada para adição de item no meu outras Ações *-* CT020ROT  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Todas as versões  
  
**Solução**Ponto de entrada: CT020ROT

Ponto de entrada para criação de um item de menu no botão 'Outras Ações' do cadastro do Plano de Contas.

**PoC**

```
#INCLUDE "PROTHEUS.CH""  
#INCLUDE "FWMVCDEF.CH"  
  
User function CT020ROT()  
Local aNovoItem := PARAMIXB[1]  
  
ADD OPTION aNovoItem TITLE "Copiar" ACTION 'U_FunCpy' OPERATION MODEL_OPERATION_UPDATE ACCESS 0 //Alterar  
  
Return (aNovoItem)  
  
User Function FunCpy()  
  
MsgAlert("Novo Item de Menu")  
  
Return
```

Exemplo:

Saiba mais:  
[CT020ROT](https://tdn.totvs.com/pages/releaseview.action?pageId=307839744)
