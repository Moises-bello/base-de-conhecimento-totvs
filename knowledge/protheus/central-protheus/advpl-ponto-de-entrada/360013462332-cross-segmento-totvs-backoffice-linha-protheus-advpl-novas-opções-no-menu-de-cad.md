---
article_id: 360013462332
category: ADVPL - Ponto de Entrada
content_hash: 5c396b3494c678e47355b1ad53a073686c8697d102ae220b4a92df70b7fed677
fetched_at: '2026-06-28T22:40:11.771484+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Novas opções no
  menu de Cadastro de Produtos (MATA010)
type: support-article
updated_at: '2021-12-29T14:23:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013462332-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Novas-op%C3%A7%C3%B5es-no-menu-de-Cadastro-de-Produtos-MATA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como inserir novas opções no menu do Cadastro de Produtos (MATA010) ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL - A partir da versão 12.1.17  
  
**Solução**

```
#Include "TOTVS.ch"  
User Function MTA010MNU()  
    AAdd(aRotina, {"Minha função", "U_MYFUNC", 0, 2, 0, NIL})  
Return (NIL)  
  
User Function MyFunc()  
    MsgInfo("Minha função", "MTA010MNU")  
Return (NIL)
```

|  |
| --- |
|  |

  
**Saiba mais**  
[MTA010MNU - Novas opções no menu de Cadastro de Produtos (MATA010)](https://tdn.totvs.com/pages/releaseview.action?pageId=370617549)
