---
article_id: 10392641693591
category: SIGAEST - CUSTOS
content_hash: ee6893de76731716fafa9f4635c6e889d104899af3f36ce166857bf2c4e2a53f
fetched_at: '2026-06-28T22:39:02.145088+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Custo médio
  histórico B9_CM1 zerado?
type: support-article
updated_at: '2025-03-12T12:20:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10392641693591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Custo-m%C3%A9dio-hist%C3%B3rico-B9-CM1-zerado
---

**Dúvida**Em determinado periodo das movimentações de um produto, após a virada de saldos, o custo médio histórico dele não foi mantido, tendo seu custo médio zerado na B9\_CM1, o que aconteceu?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Questão**Ao realizar a virada de saldos, todos os saldos do produto, serão repassados para o próximo periodo, e mesmo se os valores e quantidades desse periodo anterior, terminarem zerados, por padrão o sistema assume o ultimo valor histórico de custo médio do produto calculado, para com o campo B2\_CMFIM1, que por fim é levado para o novo periodo.

**Mas o meu produto, iniciou o periodo com custo médio histórico zerado, o que aconteceu?**

Existem hoje dois parâmetros, que podem efetuar esse comportamento para com o processamento do custo médio, onde não será calculado produtos com "saldos e valores" zerados finais, bem como na virada de saldos, não será carregado os saldos iniciais, aos produtos os quais terminaram o periodo com o "saldo e valor" também zerados (sendo considerados produtos obsoletos)

**MV\_A330GRV**

[MP - SIGAEST - Parâmetro para Saldos Iniciais obsoletos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021854152-MP-SIGAEST-Par%C3%A2metro-para-Saldos-Iniciais-obsoletos)

**MV\_A280GVR**

[MP - SIGAEST - Validação do parâmetro MV\_A280GRV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062164934-MP-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-A280GRV)

A orientação do suporte, é que os dois parâmetros, sejam usados em conjunto, ou seja:

**Caso deseje que seja gravado e recalculado todos os produtos, e levado para a virada de saldos.**  
MV\_A330GRV = .T.  
MV\_A280GRV = .T.  
  
**Caso deseje que seja gravado e recalculado somente os produtos que possuem movimentações vigentes no periodo, e levado assim então para o próximo periodo, após a virada de saldos.**  
MV\_A330GRV = .F.  
MV\_A280GRV = .F.

**Obs**: Sempre que houver a necessidade de alterar um dos parâmetros, é necessário a reinstalação da procedure 17,19,20, esses parâmetros trabalham em conjunto com a utilização das procedures.

**Saiba mais:**

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
