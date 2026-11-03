---
article_id: 4417553472279
category: Materiais - Compras (SIGACOM)
content_hash: 53f0cbad0266cb7738b229ce882ced5c937e00394b021789545b1b925b5251ce
fetched_at: '2026-06-28T22:41:12.894071+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  -  Uso da Moeda no processo
  de Compras - Pedido de Compras x Nota fiscal de Entrada
type: support-article
updated_at: '2026-06-17T15:08:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417553472279-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Uso-da-Moeda-no-processo-de-Compras-Pedido-de-Compras-x-Nota-fiscal-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41294730833175) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Como utilizar o cadastro de moedas no Módulo De Compras?  
  
**Ambiente**  
Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGACOM –  Todas as versões  
  
**Solução**

***1-) No Peddio de Compras :***

      Caso a moeda da compra, ou seja, informada no pedido de compras, seja diferente da moeda 1 ( real ), devemos preencher a **moeda correspondente no campo** **C7\_MOEDA referente a negociação dessa compra e também preencher o valor da taxa dessa moeda no campo C7\_TXMOEDA.** Porém também podemos deixar o campo **C7\_TXMOEDA sem taxa,** caso essa taxa precise ser atualizada somente na inclusão da pré nota ou da nota de entrada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41294724960919)

***2-) Na inclusão da pré nota ( MATA140 ) ou do documento de entrada direto ( MATA103 ).***

     Se no pedido de compras houve a informação da taxa da moeda, na inclusão da nota, via rotina de pré nota ou documento de entrada, o sistema considerará essa taxa para calcular os valores da nota, pois a nota sempre será convertida para moeda real.

     Caso não haja valor da taxa informada no pedido de compras, o sistema buscará a informação do cadastro de moedas do sistema. Logo, para que haja o cálculo dos valores na pré nota ou no documento de entrada, é necessário que, ou haja taxa informada no pedido de compras, ou haja taxa informada no cadastro de moedas do sistema, considerando sempre a data de emissão da nota.

Por padrão são nesses dois lugares que o sistema buscará a informação para calcular os valores da nota, no pedido de compras ou no cadastro de moedas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41294724962199)

**Logo, se você está vinculando um pedido de compras, com moeda diferente de 1, e o sistema não está calculando valor na pré nota ou no documento de entrada, é necessário verificar :**

**1-) Se há taxa de moeda informada no Pedido de Compras ou**

**2-) Se há taxa de moeda informada para a moeda do PC no cadastro de moeda do sistema.**

**SaibaMais:**

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [MP - SIGACOM - Como gerar o titulo de NF de Entrada em outra Moeda ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061872313-MP-SIGACOM-Como-gerar-o-titulo-de-NF-de-Entrada-em-outra-Moeda-?source=search)
* [MP - MATA090 - MOEDAS : Valor padrão ao iniciar o sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021847812-MP-MATA090-MOEDAS-Valor-padr%C3%A3o-ao-iniciar-o-sistema?source=search)
* [MT103TXPC - Alteração da taxa d moeda e check box conforme Pedido de Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=107383186)
* [Cross Segmento - Backoffice Protheus - SIGACOM - Preenchimento do campo E2\_TXMOEDA com data diferente do dia da inclusão do documento de entrada.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407445402903-Cross-Segmento-Backoffice-Protheus-SIGACOM-Preenchimento-do-campo-E2-TXMOEDA-com-data-diferente-do-dia-da-inclus%C3%A3o-do-documento-de-entrada-?source=search)
