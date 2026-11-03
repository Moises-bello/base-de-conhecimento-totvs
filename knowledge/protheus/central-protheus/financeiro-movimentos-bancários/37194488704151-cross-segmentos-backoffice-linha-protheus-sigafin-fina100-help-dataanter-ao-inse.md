---
article_id: 37194488704151
category: Financeiro - Movimentos Bancários
content_hash: 0813d23f54a4cf2be1a2a0c0f1a537a5a2600e7723680e8759491e2b7c3abc83
fetched_at: '2026-06-28T22:37:31.840422+00:00'
product: protheus
section_id: 35057601824535
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINA100 - HELP: DATAANTER
  ao inserir movimento com com data anterior a data base'
type: support-article
updated_at: '2025-12-22T16:44:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37194488704151-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA100-HELP-DATAANTER-ao-inserir-movimento-com-com-data-anterior-a-data-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37194474114327) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37194488693015)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Este cenário ocorre pois, dentro do padrão não é permitido que seja feita movimentação financeira em períodos anteriores a data base **"data logada no sistema**".  
  
**Solução**  
Pode configurar o parâmetro **MV\_DTMOVRE** que permite a utilização de uma data menor(retroativa) e **MV\_DTMOVDR** quantidades de dias corridos que usuário poderá relação a data-base no momento da inclusão de uma movimentação bancária.  
  
**Saiba mais:**  
**Utilização do parâmetro MV\_DTMOVRE -** <https://tdn.totvs.com/pages/releaseview.action?pageId=638721921>  
**Utilização do parâmetro MV\_DTMOVDR -** <https://tdn.totvs.com/pages/releaseview.action?pageId=653424946>
