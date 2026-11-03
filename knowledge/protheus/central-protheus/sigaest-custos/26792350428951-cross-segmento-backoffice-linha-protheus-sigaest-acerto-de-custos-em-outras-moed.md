---
article_id: 26792350428951
category: SIGAEST - CUSTOS
content_hash: 072b1e7f79d9a56a10348a586617428687a585f70be9690ffa113369ca3ad376
fetched_at: '2026-06-28T22:39:00.581308+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Acerto de Custos em
  outras Moedas (Moedas diferente de 01)
type: support-article
updated_at: '2025-03-12T12:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26792350428951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custos-em-outras-Moedas-Moedas-diferente-de-01
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26792322920599) Tempo aproximado para leitura: **00:04:15 min** **Dúvida**

Como é possível efetuar acerto de Custos em outras Moedas no Protheus?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para esse caso, é possível de duas formas, é necessário avaliar as particularidades de cada uma delas, vamos destacar abaixo um passo a passo de **exemplo de uso**:

No cenário hipotético abaixo, temos um produto com o Custo de R$ 10,00 na Moeda 01 e 40,00 na Moeda 02, **precisamos acertar o custo apenas na Moeda 02 para 50,00**.

![001 CUSTO ACERTO OUTRA MOEDA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/26794995204631)

As opções de ajustes são as seguintes:

***- 1ª -*** Acertos de Custos por **Movimentação Interna valorizada ([link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque))**, é importante compreender que a Moeda 01 ***sempre deve ser informada nas movimentações***, portanto, sugerimos utilizar um valor simbólico na Moeda 01, por exemplo R$ 0,01 (Hum centavo) e nesse exemplo a Moeda 02 com 10,00 para incrementar a diferença.

![002 CUSTO ACERTO OUTRA MOEDA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/26795261170711)

**Observe o resultado:**

![003 CUSTO ACERTO OUTRA MOEDA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/26795752623639)

Certo, e como posso ajustar o **valor simbólico que foi incluido anteriormente?** Nesse caso, pode efetuar o processo inverso, somente do valor simbólico, no nosso exemplo requisitando o custo de R$ 0,01 (Hum centavo) na Moeda 01. Veja abaixo:

![004 CUSTO ACERTO OUTRA MOEDA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/26795768300567)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26795768301207)

***- 2ª -*** Caso desejar no final do período, antes de efetuar o processo de FECHAMENTO DE CUSTOS, utilizar a rotina **[REAVALIAÇÃO DO CUSTO MÉDIO (MATA338)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338)** indicando o custo desejado na MOEDA 02. **Observação importante:** Mesmo informando o custo desejado na MOEDA 02 é necessário informar o CUSTO em CADA MOEDA utilizada na empresa para o produto e Armazém.

No cenário hipotético abaixo, agora o Custo de R$ 10,00 na Moeda 01 e 50,00 na Moeda 02, **precisamos acertar o custo apenas na Moeda 02 para 60,00**.

Veja o print com exemplo de Configuração na rotina **[REAVALIAÇÃO DO CUSTO MÉDIO (MATA338)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26795876568215)

Verifique a **[FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338)** sobre o conceito de utilização da rotina **[REAVALIAÇÃO DO CUSTO MÉDIO (MATA338)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338)** e as parametrizações envolvidas.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[Backoffice (Linha Protheus) - SIGAEST - Reavaliação de Custo Médio (MATA338)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338)

[Backoffice (Linha Protheus) - SIGAEST - Acerto de Custo dos Produtos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque)
