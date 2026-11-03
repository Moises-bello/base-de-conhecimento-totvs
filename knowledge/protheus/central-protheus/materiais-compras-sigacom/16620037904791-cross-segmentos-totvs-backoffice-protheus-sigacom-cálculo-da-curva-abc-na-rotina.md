---
article_id: 16620037904791
category: Materiais - Compras (SIGACOM)
content_hash: f959433eced86dd8947fb0787c8d260f9b11efb3fb15d73e49bbd83da49c03d0
fetched_at: '2026-06-28T22:41:14.292814+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Cálculo da curva ABC
  na rotina Gerar Demanda (MATA295) para classificação do custo do produto (BL_ABCCUST)
type: support-article
updated_at: '2023-11-21T17:25:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16620037904791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-C%C3%A1lculo-da-curva-ABC-na-rotina-Gerar-Demanda-MATA295-para-classifica%C3%A7%C3%A3o-do-custo-do-produto-BL-ABCCUST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16620065367063) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como é realizado o cálculo da curva ABC na rotina Gerar Demanda (MATA295) para classificação de custo do produto (**BL\_ABCCUST)**?  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**Através dos perguntes da rotina Gerar Demanda (MATA295) é possivel atribuir um determinado valor para calcular e classificar os itens utilizando o método Curva ABC conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16619178716055)

**Cálculo para classificação de custo do produto (Campo BL\_ABCCUST):**

Neste médoto, será possivel classificar o custo do produto através do campo **BL\_ABCCUST** nas cateogorias A | B ou C conforme regra abaixo:

###############################

**- Primeira validação** (Classificando como Categoria 'A') - **Exemplo:**

**Valor da Demanda (BL\_TOTDEM):** 200

**Pergunte: '**% Class 'A' Venda?': 25 (valor definido no pergunte da rotina)

**Resultado:** (25 \* 200 / 100 ) = 50   (Pergunte \* BL\_TOTDEM / 100)

- **Se o valor da Demanda** (BL\_TOTDEM = 200) **for menor** que o **Resultado (50)**, o custo do produto será **classificado como categoria 'A'**

###############################

**- Segunda validação** (Classificando como Categoria 'B') - **Exemplo:**

**Valor da Demanda (BL\_TOTDEM):** 200

**Pergunte: '**% Class 'B' Venda?': 17 (valor definido no pergunte da rotina)

**Resultado:** (17 \* 200 / 100 ) = 34   (Pergunte \* BL\_TOTDEM / 100)

- **Se o valor da Demanda** (BL\_TOTDEM = 200) **for menor** que o **Resultado (35)**,o custo do produto será **classificado como categoria 'B'**

###############################

**- Terceira validação** (Classificando como Categoria 'C') - **Exemplo:**

Caso a primeira e a segunda validação sejam falsas, o custo do produto será classificada automaticamente na categoria 'C'

***Saiba Mais :***

[Gerar demanda (MATA295 - SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=312156967)

[Parametrização (MATA295 - SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=359476949)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
