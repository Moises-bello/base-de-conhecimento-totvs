---
article_id: 4410974726679
category: Financeiro - Contas a Receber
content_hash: c28c5e03b8bac20e9dd23d35598dd17c2773aec273b99f05c4ee6b6470791f6d
fetched_at: '2026-06-28T22:38:12.683614+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento -  Backoffice Linha Protheus SIGAFIN - FINA060 - Transferência/Borderô
  para carteira 2, não permite deixar o campo Tx Desc em branco, quando o valor do
  Crédito é menor que o valor total do título
type: support-article
updated_at: '2021-10-18T20:37:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410974726679-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA060-Transfer%C3%AAncia-Border%C3%B4-para-carteira-2-n%C3%A3o-permite-deixar-o-campo-Tx-Desc-em-branco-quando-o-valor-do-Cr%C3%A9dito-%C3%A9-menor-que-o-valor-total-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Rotina Transferência/Borderô (FINA060) para carteira 2, não permite deixar o campo Tx Desc em branco, quando o valor do Crédito é menor que o valor total do título?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA060 - Todas as versões  
  
**Solução**Comportamento é padrão da rotina, sempre que o valor informado no campo **Crédito** for menor que o valor do título, é preenchido a porcentagem de desconto no campo **Tx Desc**.

**Exemplos:**  
Título valor R$ 500,00

Se informado um valor de R$ 450,00 no campo **Crédito,** o campo **Tx Desc** recebera 10%.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410963412119/mceclip0.png)

Informado no campo **Tx Desc** o valor de 20%, o campo **Crédito** receberá R$ 400,00

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410963547031/mceclip1.png)   
  
**Saiba mais:**<https://tdn.totvs.com/pages/releaseview.action?pageId=271405699>
