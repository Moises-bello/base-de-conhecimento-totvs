---
article_id: 360033304474
category: Escrita Fiscal - Error.log
content_hash: 4329b9918275762fbef22276a7fac0d05aee2cb3ebbc7528cf4cddbdef84adb6
fetched_at: '2026-06-28T22:39:32.880036+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - variable does not
  exist IPI on GRVAPURCDP(FISXAPUR.PRX)
type: support-article
updated_at: '2021-07-08T13:33:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033304474-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-variable-does-not-exist-IPI-on-GRVAPURCDP-FISXAPUR-PRX
---

**Ocorrência**Ao gerar apuração de IPI (MATA952) está ocorrendo seguinte error log :

variable does not exist IPI on GRVAPURCDP(FISXAPUR.PRX)   
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

É necessário que conteúdo do parâmetro **MV\_PFAPUIP** esteja entre aspas, por exemplo:  
  
MV\_PFAPUIP = "IPI"

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043557073/mceclip1.png)
