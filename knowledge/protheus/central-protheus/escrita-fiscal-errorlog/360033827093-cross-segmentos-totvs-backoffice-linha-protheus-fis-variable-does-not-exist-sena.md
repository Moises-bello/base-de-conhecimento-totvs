---
article_id: 360033827093
category: Escrita Fiscal - Error.log
content_hash: e4693a649abc561170396ae99ffa8365c396a8e61e6b19e5eeb718d498b1d379
fetched_at: '2026-06-28T22:39:32.883092+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - variable does not
  exist SENAR on GRAVATIT(FISXAPUR.PRX)
type: support-article
updated_at: '2021-07-08T13:54:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033827093-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-variable-does-not-exist-SENAR-on-GRAVATIT-FISXAPUR-PRX
---

**Dúvida**Ao rodar a rotina de apuração de ICMS (MATA953) a rotina apresentou o seguinte erro:   
  
Variable does not exist SENAR on GRAVATIT(FISXAPUR.PRX)   
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1.  Abra o parâmetro MV\_PFSENAR pelo configurador;  
2.  Coloque ASPAS duplas = "SEN".

Exemplo : 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043557793/mceclip0.png)
