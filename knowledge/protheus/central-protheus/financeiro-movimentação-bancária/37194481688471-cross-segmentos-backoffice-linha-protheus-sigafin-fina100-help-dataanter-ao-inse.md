---
article_id: 37194481688471
category: Financeiro - Movimentação Bancária
content_hash: d479e39e00b638a8e02bab5cadf15fff25362e61f300325e8643f5f34ec25121
fetched_at: '2026-06-28T22:38:19.294381+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINA100 - HELP: DATAANTER
  ao inserir movimento com com data anterior a data base'
type: support-article
updated_at: '2025-12-22T16:44:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37194481688471-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA100-HELP-DATAANTER-ao-inserir-movimento-com-com-data-anterior-a-data-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37194465313943) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37194465315735)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Este cenário ocorre pois, dentro do padrão não é permitido que seja feita movimentação financeira em períodos anteriores a data base **"data logada no sistema**".  
  
**Solução**  
Pode configurar o parâmetro **MV\_DTMOVRE** que permite a utilização de uma data menor(retroativa) e **MV\_DTMOVDR** quantidades de dias corridos que usuário poderá relação a data-base no momento da inclusão de uma movimentação bancária.  
  
**Saiba mais:**  
**Utilização do parâmetro MV\_DTMOVRE -** <https://tdn.totvs.com/pages/releaseview.action?pageId=638721921>  
**Utilização do parâmetro MV\_DTMOVDR -** <https://tdn.totvs.com/pages/releaseview.action?pageId=653424946>
