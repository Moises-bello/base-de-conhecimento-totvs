---
article_id: 360051174513
category: Faturamento - Orçamentos
content_hash: 606154094adc287d581ab672f1055ddfeeaa71356c7d875bedbd1b677f153539
fetched_at: '2026-06-28T22:38:24.914292+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Cancelamento
  automático de orçamento
type: support-article
updated_at: '2023-06-14T20:56:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051174513-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Cancelamento-autom%C3%A1tico-de-or%C3%A7amento
---

**Dúvida**

Como efetuar o cancelamento automático de um orçamento(**MATA415**) quando não aprovado?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Para que o orçamento não aprovado em pedido seja cancelado automaticamente, os parâmetros ***MV\_ORCVLD***tem que estar igual a .T. e ***MV\_ORCUVLD*** com uma data para o cancelamento automático e na validação da Rotina (SCJ), informar a função "**MA415AUTO()"**

Desta forma, assim que o sistema é iniciado , é conferido e orçamento se enquadra na data de cancelamento automático, onde automaticamente o sistema  o cancela deixando com a cor da legenda em preto.

![](https://totvssuporte.zendesk.com/attachments/token/IVrWauPyaaBMW1TQriQk579xc/?name=inline-17982682.png)​  
Sintaxe dos parâmetros:

***MV\_ORCVLD** : Cancela os Orçamentos por validade automaticamente.*

***Tipo:** Lógico*

***Conteúdo:** .T. ou .F.*

***MV\_ORCUVLD:**Data do cancelamento de Orçamento automático**.***

***Tipo:** Data*

***Conteúdo:** Ex. 20191105*

Inclusão da função **"MA415AUTO()"** Acessar o configurador(SIGACFG);

Ir em Base de Dados > Dicionário > Base de Dados;

Localize a tabela "Orçamentos - SCJ" e Acione o botão **Editar**;

Acesse o campo **Rotina** e inclua a chamada da função **MA415AUTO()** conforme demonstrado na imagem abaixo. Essa função é a responsável por realizar o **cancelamento automático dos Orçamentos** ao acessar a rotina de **Orçamentos**.

![008-img.PNG](https://tdn.totvs.com/download/attachments/564332808/008-img.PNG?version=1&modificationDate=1601474516190&api=v2)

Confirme e alteração e grave a alteração realizada.

***Saiba******Mais:***

[9579939 DSERFAT-17645 DT Orçamento de Vendas - Cancelamento Automático de Orçamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=564332808)
