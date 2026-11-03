---
article_id: 4408510846871
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 0b9521e584c66e30efecb3f09d78f15c1dfd0d7d5ff003d9893d86bb55f7ae14
fetched_at: '2026-06-28T22:39:36.874439+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular  PIS/COFINS
  ST no total da NF?
type: support-article
updated_at: '2021-09-15T11:24:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408510846871-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-PIS-COFINS-ST-no-total-da-NF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como calcular PIS/COFINS ST no total da NF?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para fazermos o calculo do PIS/COFINS por ST, precisamos Criar os campos na SB1

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408496147095/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408496153367/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408510316183/mceclip2.png)

Parâmetros

**MV\_B1CPSST = B1\_PPSSTCG**

**MV\_B1CCFST = B1\_PCFSTCG**

**MV\_PUPCCST = B1\_PUPCCST**

Colocar no cadastro de produto informar a alíquota do PIS/COFINS apuração e PIS/COFINS ST

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408496235671/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408496265623/mceclip4.png)

TES

* Campo **PIS/COFINS (F4\_PISCOF)** igual a 4= Não Considera
* Campo **Cred.PIS/COF (F4\_PISCRED)** igual a 4= Calcula
* Campo **Sit. Trib. PIS (F4\_CSTPIS)** igual a 05
* Campo **Sit. Trib. COF (F4\_CSTCOF)** igual a 05
* Campo **PIS/COF ST (F4\_PSCFST)** igual a 1= Sim
* Campo **Tp Reg (F4\_TPREG)** igual a 2= Cumulativo

exemplo de calculo

Uma venda onde o preço unitário de venda no varejo seja R$ 5,00, e quantidade de 10.000 unidades, totalizando um valor de R$ 50.000,00, o cálculo ficará da seguinte forma:

**PIS**

* Base de cálculo do PIS: R$ 50.000,00 \* 3.42 = R$ 171.000,00
* Valor do PIS: R$ 171.000,00 \* 0,65% = R$ 1.111,50

**COFINS**

* Base de cálculo da COFINS: R$ 50.000,00 \* 2,9169 = R$ 145.845,00
* Valor da COFINS: R$ 145.845,00 \* 3% = R$ 4.375,35

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408510547223/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408510557719/mceclip6.png)

Após a NT005 será gravado campo CD2\_PSCFST

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408510744215/mceclip7.png)

O campo CD2\_PSCFST foi criado com o intuito de indicar se o valor do PIS/COFINS-ST serão somados no total do Documento Fiscal. Esse campo servirá como base para o preenchimento das tags <indSomaPISST> e <indSomaCofinsST>, criados nesta Nota Técnica.
