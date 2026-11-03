---
article_id: 360033547554
category: Escrita Fiscal - Error.log
content_hash: f89b6c3ff826ce7cbf45343ce78b403bc19ccb108363b82129f07d666c8f690e
fetched_at: '2026-06-28T22:39:32.875337+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - type mismatch on
  compare  on MAITARRED(MATXFIS.PRX)
type: support-article
updated_at: '2021-07-08T13:38:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033547554-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-type-mismatch-on-compare-on-MAITARRED-MATXFIS-PRX
---

**Ocorrência**Ao incluir uma nota fiscal de entrada, ao tentar selecionar um produto o sistema está gerando erro log :

type mismatch on compare on MAITARRED(MATXFIS.PRX)  
  
**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17  
  
**Causa**O tipo do parâmetro divergente.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Abra o parâmetro MV\_TXPIS pelo configurador;  
2. Altere o Tipo para numérico ;

Exemplo :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043124874/mceclip0.png)
