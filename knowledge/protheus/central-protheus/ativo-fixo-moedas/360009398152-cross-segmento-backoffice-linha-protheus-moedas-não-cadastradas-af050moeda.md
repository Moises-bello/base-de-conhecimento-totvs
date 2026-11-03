---
article_id: 360009398152
category: Ativo Fixo - Moedas
content_hash: 65cc66911c270ad99545388964dd6c2de29820a1c943b82052445b15a23bb083
fetched_at: '2026-06-28T22:41:37.770067+00:00'
product: protheus
section_id: 1500001536641
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -  MOEDAS NÃO CADASTRADAS - AF050MOEDA
type: support-article
updated_at: '2021-11-17T20:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009398152-Cross-Segmento-Backoffice-Linha-Protheus-MOEDAS-N%C3%83O-CADASTRADAS-AF050MOEDA
---

**Ocorrência**Moeda não cadastrada em todos os dias do mês de calculo.

**Ambiente**PROTHEUS - ATIVO FIXO - A PARTIR DA VERSÃO 11.8

**Causa**

Moeda não cadastrada em todos os dias do mês do calculo.

**Solução**A moeda deve ser cadastrada para todos os dias do mês, não deve haver nenhum dia sem a informação da moeda.

* Através da rotina MATA090 Moedas -  realize :

1º inclua três dias

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413465911063/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413458179351/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413453804055/mceclip3.png)

2º Logado com a data base no 3º dias

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413453849367/mceclip4.png)

* Realize a projeção da moeda , dessa forma terá certeza que  o sistema criou todas os dias

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413458068375/mceclip0.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413465975959/mceclip5.png)

* o sistema irá criar todos os dias automaticamente

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413453884439/mceclip6.png)

Link com mais informações sobre outras causas que podem impedir o calculo

<http://tdn.totvs.com/pages/releaseview.action?pageId=6067622>

[ATFA050 - Não processa o calculo de depreciação mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019761431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-N%C3%A3o-processa-o-calculo-de-deprecia%C3%A7%C3%A3o-mensal?source=search)

[Lançamentos em outras moedas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007149771-MP-SIGACTB-Lan%C3%A7amentos-em-outras-moedas?source=search)

[CADASTRO DE MOEDAS CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020781892-MP-SIGACTB-CADASTRO-DE-MOEDAS-CONT%C3%81BEIS?source=search)
