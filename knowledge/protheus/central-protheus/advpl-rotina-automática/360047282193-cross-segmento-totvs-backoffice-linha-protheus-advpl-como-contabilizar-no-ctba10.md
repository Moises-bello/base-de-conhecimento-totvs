---
article_id: 360047282193
category: ADVPL - Rotina Automática
content_hash: 6900e91de29b1583c4a7723077d2d8cd1ca49ef68cf96de603a9d96e85824e42
fetched_at: '2026-06-28T22:40:24.227107+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como contabilizar
  no CTBA102 uma moeda via execauto
type: support-article
updated_at: '2021-12-29T12:57:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047282193-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-contabilizar-no-CTBA102-uma-moeda-via-execauto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura**: 00:02:00 min  
  
Dúvida**Ambiente configurado para contabilizar nas cincos moedas, mas tem a necessidade de contabilizar em apenas uma Moeda via **ExecAuto**, como proceder?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão P12  
  
**Solução**O campo Criterio de Conversao (**CT2\_CONVER)** possui as seguintes opções:  
1 - Efetua o lançamento na **Moeda**  
2 - Não efetua o lançamento.  
  
O mesmo pode ser usado na montagem do *array* dos itens antes da chamada do **ExecAuto** e deverá obedecer a configuração mencionada.  
Neste caso, foi passado com o conteúdo 1.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066982534/mceclip0.png)

**Saiba Mais**  
[CTBA102 - Rotina automática Inclusão Lançamentos Contábeis](https://tdn.totvs.com/pages/releaseview.action?pageId=285656831)
