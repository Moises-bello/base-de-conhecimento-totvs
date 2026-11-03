---
article_id: 4407178330903
category: Materiais - Compras (SIGACOM)
content_hash: 44541aaafabaf9cb009cbcdd81c0eb5589c5b7bd2f2eae4a65c50db01c01c5e6
fetched_at: '2026-06-28T22:41:16.054370+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como são exibidos os
  valores na Análise de Cotação em outra Moeda ?
type: support-article
updated_at: '2021-08-26T20:28:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407178330903-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-s%C3%A3o-exibidos-os-valores-na-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-em-outra-Moeda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como é realizado o processo de Analisa Cotação com Cotações em outras Moedas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Contratos - Todas as versões  
  
**Solução**Na Analise da Cotação o Sistema apresenta os Valores da Moeda Principal (Real) para comparação os valores do melhor preço para Analise.

Exemplo:

Quando é feita uma Atualização de Cotação na rotina MATA150 e a Cotação de um fornecedor é informada na Moeda "Dólar" e a de outro Fornecedor na Moeda "Real", na rotina de Analise de Cotação os valores são apresentados sempre na moeda principal do sistema ("Real")

Este conceito do sistema ocorre para que se possa ter uma melhor visualização da comparação dos valores que estão sendo analisados na Cotação.

No exemplo em que um fornecedor vende a 500 reais e outro a 120 dólares, qual produto está mais barato ?

O calculo de comparação teria que ser realizado manualmente pelo usuário para converter 120 Dólares em Reais para ver qual produto tem menor valor.

Para que não seja preciso o usuário realizar esta conta manualmente,  o sistema realiza este cálculo e exibe as informações na mesma Moeda para verificação da melhor proposta.

Depois que é definido o Fornecedor Ganhador, é gerado o Pedido de Compra nas condições ofertadas na proposta (rotina Atualiza Cotação - MATA150) , ou seja, se a Cotação foi informada em Dólar, ao confirmar a Analise da Cotação o Valor do pedido gerado será em Dólar, e se na Cotação foi informado valor em "Real" o Pedido gerado será em Real.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
