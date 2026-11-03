---
article_id: 4419362203671
category: Materiais - Compras (SIGACOM)
content_hash: 4d94b87a3a136e2a1900c9c30ecdea497e3e9c237db680e7bed7a5042f9f4a0f
fetched_at: '2026-06-28T22:41:24.017409+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Posicionamento de linhas
  NF de entrada x Financeiro
type: support-article
updated_at: '2022-05-16T21:02:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419362203671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Posicionamento-de-linhas-NF-de-entrada-x-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:SS min** **Dúvida**

No momento do lançamento de uma Nota Fiscal de entrada com 10 itens em qual item o sistema posiciona para levar os dados para o Financeiro?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Posicionamento de linhas NF de entrada x Financeiro

**Solução**

Ao incluir uma **Nota fiscal de Entrada,** vai gerar apenas **titulo**, independente dos itens porque o título não detalha a nota, é a penas a movimentação financeira ( pagar ou receber)  
O detalhe estará sempre no documento fiscal, salvo se utilizar condição de pagamento diferente de "á vista".  
Ex: nota de 2 itens de R$100 cada item -> titulo financeiro 1 Titulo de R$200  
caso a condição de pagamento divida em 4x serão criados 4 títulos de R$50 independente se tem parcela ou não, ele nunca considera por item, mas sim nota cheia.

Qualquer tratamento diferente a ser efetuada é por meio de implementação de ponto de entrada:  
 **MT100GE2 - Complementa a Gravação dos Títulos Financeiros a Pagar  
Link:<https://tdn.totvs.com/x/ldxc>  
MTA103OK - Altera o resultado da validação padrão para inclusão e alteração  
Link:<https://tdn.totvs.com/x/buRc>**

**Saiba mais em :**

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
