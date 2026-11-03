---
article_id: 13199299579671
category: SIGAEST - CUSTOS
content_hash: d679f85006028424adfd562fb61c8a956e60973cdd8b48aca5ce831d099356e9
fetched_at: '2026-06-28T22:39:02.249531+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Meu produto tipo MO
  ficou com o valor de custo negativo, como ajustar?
type: support-article
updated_at: '2025-03-12T12:27:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13199299579671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Meu-produto-tipo-MO-ficou-com-o-valor-de-custo-negativo-como-ajustar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:50 min****Dúvida**Durante a avaliação de custos do produto MO ou MOD+CC, foi identificado que o custo médio do mesmo ficou negativo, levando um valor negativo nas requisições e consequentemente nas produções utilizadas.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Hoje existe dois tipos de configuração para utilização de um produto mão de obra.

- Com o código do produto MOD+CC (Centro de custo)

- Ou com código comum, exemplo: XTPO e amarrado a um centro de custo ou grupo de centro de custo, B1\_CCCUSTO , B1\_GCCUSTO, se desejar integrar ao contábil.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MOD/GGF - Conceito e Usabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402117444247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MOD-GGF-Conceito-e-Usabilidade)

Normalmente, o produto MO tem seu custo negativado, devido aos lançamentos efetuados nas contas contábeis, ao qual ele se refere, e somente quando ele é integrado ao contábil.

Então, caso chegue em um cenário onde o produto MO esteja com custo médio negativo, após execução do custo médio, nos campos (B2\_CM1 ou B2\_CMFIM1), o primeiro passo e primordial, é avaliar as contas/lançamentos as quais o seu produto se refere.

**Porque olhar os dados no contábil?**

O grande motivo de um produto MO ficar com custo negativo, são consequências de possuir lançamentos de "Crédito" maior que "Débito", e caso esteja dessa forma, as requisições ficaram então negativas.

Os cliente utilizam bastante os relatórios de Razão e outros para avaliarem os lançamentos, abaixo segue 2 mais utilizados e suas diferenças.

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR400 e CTBR040 diferença entre os relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013411871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR400-e-CTBR040-diferen%C3%A7a-entre-os-relat%C3%B3rios)

Referente a duvidas de valores na "contabilidade", sugerimos validar junto ao time Protheus Ativo e Contábil.

O custo do produto MO, que possui integração contábil, será sempre o reflexo dos valores na contabilidade, então se esses forem incorretos, o custo do seu produto consequentemente também será.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo de configuração de MOD e GGF com e sem integração contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071)*
