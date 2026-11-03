---
article_id: 38769320105239
category: Financeiro - Comissão
content_hash: aa490900b82400f847690a0bcfd27fba60b41e2da45a1f372805b0ef27821fa1
fetched_at: '2026-06-28T22:37:50.754232+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - FINA440 - Cálculo da comissão
  por produto
type: support-article
updated_at: '2026-03-03T18:19:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38769320105239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FINA440-C%C3%A1lculo-da-comiss%C3%A3o-por-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38769320094999) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como é efetuado o cálculo do percentual de comissão quando a regra de comissão está parametrizada por **Produto** ou por **Item do Produto**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro (SIGAFIN) - Todas as versões.  
  
**Solução**  
Quando o sistema está configurado para calcular a comissão com base no **Produto** ou no **Item do Produto**, o Protheus não utiliza um percentual fixo, pois cada item pode ser informado uma porcentagem diferente. O sistema realiza o cálculo baseado na **média das comissões informadas no cadastro do produto ou no item do pedido**.

O sistema realiza o cálculo conforme demonstrado no exemplo abaixo:

O pedido contém dois itens, cada qual com um percentual de comissão distinto:

* **Item 1:** comissão de 30% sobre o valor de R$ 10.000,00, resultando em R$ 3.000,00 de comissão.
* **Item 2:** comissão de 50% sobre o valor de R$ 2.000,00, resultando em R$ 1.000,00 de comissão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38769320095255)

Inicialmente, o sistema soma o valor total das comissões, totalizando R$ 4.000,00.  
Em seguida, multiplica esse montante por 100, obtendo R$ 400.000,00.

Posteriormente, o valor de R$ 400.000,00 é dividido pelo valor total da nota fiscal (R$ 12.000,00), resultando em um percentual médio de comissão de **33,33%**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38769287887895)

**Saiba mais**

[Recálculo de Comissões -FINA440](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528#Rec%C3%A1lculodeComiss%C3%B5es(FINA440SIGAFIN)-Comiss%C3%A3oporproduto)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Hierarquia de Comissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25812640102167-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Hierarquia-de-Comiss%C3%A3o)
