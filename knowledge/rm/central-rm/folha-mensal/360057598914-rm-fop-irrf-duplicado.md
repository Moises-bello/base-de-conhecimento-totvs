---
article_id: 360057598914
category: Folha Mensal
content_hash: ef469ecbb76a06b178d14e24e5c5a4f80974ac883798a11f7da471ce7ed7e464
fetched_at: '2026-06-28T22:46:59.493535+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RM - FOP - IRRF Duplicado '
type: support-article
updated_at: '2021-06-18T13:23:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057598914-RM-FOP-IRRF-Duplicado
---

**Ocorrência**

O fechamento da folha mensal fica com IRRF Duplicado quando há férias antecipadas.  
  
**Ambiente**

RM - Totvs Folha de Pagamento - Todas as versões  
  
**Causa**

Antecipação de Pagamento de Férias.  
  
**Solução**

No processo padrão de férias ocorre o seguinte:

O pagamento das férias é antecipado através do cálculo realizado no recibo de férias, ou seja, ocorre neste momento o adiantamento das férias. Neste momento acontece o lançamento dos proventos e descontos que influencia diretamente no liquido das férias.

Exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097671894/mceclip0.png)  
  
Para o fechamento da folha, ocorre o processo de lançamento das férias para o envelope de pagamento, que nada mais é que um espelho do que foi calculado no recibo de férias. Neste momento, são lançados os proventos e os descontos, juntamente com o evento de adiantamento conforme recibo *(cc43)* para fazer o estorno do que foi lançado no recibo e assim **não ocorrer o pagamento e desconto em duplicidade**.  
  
[Código de Cálculo 43 - Adiantamento Conforme Recibo.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719758)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097672654/mceclip1.png)  
  
Como o **IRRF** é regime caixa, todo desconto é lançado com data referente ao mês de pagamento das férias para que atenda a necessidade legal da Receita Federal.
