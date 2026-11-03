---
article_id: 37528870409367
category: Financeiro - Comissão
content_hash: 316ff1d07cfba78a1eddbaa1fdd7e4414ca197bcaf1e635992a0d591a9fb9d10
fetched_at: '2026-06-28T22:37:50.706685+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - É possível contabilizar
  a comissão?
type: support-article
updated_at: '2026-01-08T14:23:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37528870409367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-%C3%89-poss%C3%ADvel-contabilizar-a-comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37528853680407) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
É possível contabilizar a comissão?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

**Por padrão, não existe LP específica para realizar a contabilização do movimento de geração da comissão.**

A contabilização das comissões é realizada pelo **módulo de origem do movimento**. Dessa forma, tanto os lançamentos de **inclusão** quanto os de **baixa** dos registros de comissão são processados e contabilizados de acordo com as **LPs** associadas ao módulo que originou o respectivo movimento.

Em outras palavras, cada movimentação relacionada à comissão segue integralmente as regras contábeis definidas no módulo responsável por sua geração, garantindo consistência e aderência às parametrizações contábeis específicas de cada processo.

A seguir, apresentam-se as **LPs responsáveis pela contabilização**, conforme o módulo de origem do movimento.

[Lançamento padrão financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)

Como exemplo, ao utilizar a LP 520, referente ao processo de baixa, a comissão será gerada e contabilizada no momento em que a baixa do título for efetivada.

Devem ser cadastradas duas LPs do tipo 520: uma destinada à contabilização do valor principal do título e outra destinada à contabilização da comissão, utilizando as expressões conforme ilustrado na imagem a seguir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37529772466583)

Com a realização da baixa, será gerada a contabilização correspondente ao valor do título, no montante de **R$ 10.000,00**, bem como o lançamento referente à comissão, no valor de **R$ 500,00**, correspondente a **5%** do valor do título.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37529772469015)
