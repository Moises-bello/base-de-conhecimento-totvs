---
article_id: 360026889751
category: Escrita Fiscal - Error.log
content_hash: a436a0cef8c2f409f9ee906381f1197b9027cdcabe1d6307096ba4fda729bf0b
fetched_at: '2026-06-28T22:39:32.873020+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - type mismatch on
  + on MAFISINI(MATXFIS.PRX)
type: support-article
updated_at: '2021-07-08T12:55:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026889751-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-type-mismatch-on-on-MAFISINI-MATXFIS-PRX
---

**Ocorrência**

Ao gerar um nota fiscal de saída (MATA460A) está ocorrendo os seguintes error logs.

type mismatch on + on MAFISINI(MATXFIS.PRX) 07/02/2019 12:51:45 line : 890  
  
**Ambiente**

Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
**Causa**

 O parâmetro MV\_2DUPNAT/MV\_1DUPNAT está apontando um campo incorreto ou vazio.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

Exemplo do conteúdo padrão do parâmetro MV\_2DUPNAT:  
![](https://totvssuporte.zendesk.com/attachments/token/8SIYFfEJ1J7qpOvmTrZjRtVaj/?name=inline-1553215540.png)​  
Exemplo do conteúdo padrão do parâmetro MV\_1DUPNAT:  
![](https://totvssuporte.zendesk.com/attachments/token/BRuJBMr52s08ZCoOQ7aiFIpif/?name=inline-904852929.png)​  
  
Segue sugestão como do que preencher o parâmetro, mas altere conforme sua necessidade.
