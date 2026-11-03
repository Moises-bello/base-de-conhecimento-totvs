---
article_id: 23608602938519
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 3ca2500884d5451537ac57b205ff434ff94dae481ae885cd7ac3b662c6d4483d
fetched_at: '2026-06-28T22:38:57.004021+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA242 - Campo D3_RATEIO,
  qual cálculo efetuar para produtos com estrutura?
type: support-article
updated_at: '2026-03-26T14:48:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23608602938519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA242-Campo-D3-RATEIO-qual-c%C3%A1lculo-efetuar-para-produtos-com-estrutura
---

O campo % Rateio (D3\_RATEIO) na desmontagem de produto acabado deve ratear o custo proporcionalmente à quantidade do produto de origem, somando sempre 100%. O cálculo recomendado é: 100 dividido pelo custo médio do produto acabado, multiplicado pelo custo médio do componente. Assim, garante-se o rateio exato para a rotina de desmontagem no TOTVS Protheus.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23608602911767) Tempo aproximado para leitura: **00:03:30 min**  
  
**Dúvida**

Ao efetuar a Desmontagem de Produto Acabado é necessário ***digitar manualmente*** o campo **% Rateio (D3\_RATEIO).** Qual o cálculo mais adequado para os componentes sejam rateados com o custo atual considerado?

![estrutura.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23611158210071)

![MATA242 IMAG 01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23611172037527)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

A finalidade do campo **% Rateio (D3\_RATEIO)** **é Ratear o valor de Custo**, proporcional à quantidade do **Produto de Origem**. Dessa forma a soma Total do campo D3\_RATEIO de todos os itens, deve ser sempre 100%.

![CUSTO ATUAL IMAGE 03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23611158254999)

No exemplo acima, ao efetuar a desmontagem, pode utilizar o seguinte cálculo:

**100 dividido ( / ) pelo Custo Médio (B2\_CM1) do PA vezes ( \* ) o Custo Médio (B2\_CM1) do Componente onde o resultado ( = ) é pode ser considerado em cada componente da estrutura.** Veja mais:

|  |
| --- |
| **100 / B2\_CM1 (PA) \* B2\_CM1 (MP) = D3\_RATEIO** |

Veja na prática para os componentes acima:

**Item 1 -> 100/50,00\*37,00 =** **74%** **(D3\_RATEIO)**

**Item 2 -> 100/50,00\*9,00   =** **18%** **(D3\_RATEIO)**

**Item 3 -> 100/50,00\*4,00   =** **8%** **(D3\_RATEIO)**

Nesse exemplo observe que a soma da **porcentagem dos 3 componentes** é 100%

![MATA242 IMAG 04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23611172062103)

**IMPORTANTE:** É possível alterar o Tamanho do Campo ou mesmo as Decimais do D3\_RATEIO?

**Resp.:** Sim, é possível, mas veja bem, é necessário **sempre realizar o cálculo da Soma de todos os rateios de forma que seja equivalente e 100%.** Pois, a rotina Desmontagem de Produtos concretiza a Desmontagem somente com o rateio **exato** de 100%.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - Utilizando a desmontagem para controle de saldo na segunda unidade de medida](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410189373591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilizando-a-desmontagem-para-controle-de-saldo-na-segunda-unidade-de-medida)

[MP - SIGAEST - MATA242 - Processo de Desmontagem de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061648474-MP-SIGAEST-MATA242-Processo-de-Desmontagem-de-Produtos)

[SIGAEST - Como tratar quando efetuada a compra de produto em Caixa, porém, vendo/consumo as unidades da caixa?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6027746860567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-tratar-quando-efetuada-a-compra-de-produto-em-Caixa-por%C3%A9m-vendo-consumo-as-unidades-da-caixa-)

<https://tdn.totvs.com/x/DNwKDg>
