---
article_id: 12407848974359
category: Materiais - Compras (SIGACOM)
content_hash: 728d1522566ee75c05b999eb88fcbbbd4ee19768050ede7d9761361cf49fbca9
fetched_at: '2026-06-28T22:41:25.453910+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM- Como calcular e gravar
  o valor do IPI no pedido de compras?
type: support-article
updated_at: '2023-02-14T13:56:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12407848974359-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-calcular-e-gravar-o-valor-do-IPI-no-pedido-de-compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02mm** **Dúvida**Como gravar o valor do IPI no pedido de compras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras- A partir da versão 12  
  
**Solução**

Para que o campo valor do IPI, **C7\_VALIPI** seja gravado no pedido de compras, é necessário que o sistema esteja configurado conforme abaixo, considerando as possibilidade mencionadas são:

informar alíquota na linha do item do pedido de compras, Cadastro de Tes, Cadastro de Produtoe

1.  Informar o percentual da alíquota no campo **C7\_IPI, no pedido de compras e utilizar uma TES que esteja configurada o campo Calcula  IPI = Sim**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12407990382231)![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12407405372567)**

**Visualização na Aba impostos:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12407516539543)**

**Cadastro de TES:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12407807684247)**

Caso alíquota esteja cadastrada diretamente no produto, também haverá o cálculo do imposto IPI.

**Cadastro de Produto:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12408097461015)

**Saiba Mais:**

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
