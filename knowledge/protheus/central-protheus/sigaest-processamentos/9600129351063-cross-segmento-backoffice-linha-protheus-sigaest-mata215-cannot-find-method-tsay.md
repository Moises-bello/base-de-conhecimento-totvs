---
article_id: 9600129351063
category: SIGAEST - PROCESSAMENTOS
content_hash: d4f86776400eb30f1f78cc26621d65108ceea1df7c4b1234f3d7953bbc828ded
fetched_at: '2026-06-28T22:39:04.904773+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Cannot find
  method TSAY:SETREGUA1 on A103REFAZ(MATA103COM.PRW)
type: support-article
updated_at: '2023-09-04T14:49:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9600129351063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Cannot-find-method-TSAY-SETREGUA1-on-A103REFAZ-MATA103COM-PRW
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17264405114647) Tempo aproximado para leitura: 00:01:02 min****Ocorrência**Ao processar a rotina Refaz Empenhos - MATA215, é apresentado o error.log:

**"*Cannot find method TSAY:SETREGUA1 on A103REFAZ(MATA103COM.PRW)*"**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Não estava atualizada a régua de processamento da rotina Refaz Empenhos (MATA215) quando utilizado o novo processamento

**Solução**Realizado tratamento para atualizar a régua de processamento da rotina **Refaz Empenhos (MATA215)** quando utilizado o novo processamento, ou o texto do painel quando utilizado o modelo padrão. O fonte atual MATA103COM.PRW contempla os parâmetros da régua na função A103REFAZ.

Esta correção está no fonte MATA103COM.PRW com a data a partir de 13/09/2022. Para ser contemplado com esta função, basta atualizar a **Expedição Contínua do Compras (SIGACOM)**, por meio do link abaixo (para clientes na release 12.1.33), importante que o fonte da rotina **REFAZ EMPENHOS (MATA215)** também esteja atualizado com o **Expedição Contínua do Estoque (SIGAEST)**.

**[Expedição Contínua - Módulo Compras 12.1.33](https://suporte.totvs.com/portal/p/10098/download#detail/1039089) | [12.1.2210](https://suporte.totvs.com/portal/p/10098/download#detail/1080335)**

[**Expedição Contínua - Módulo Estoque 12.1.33**](https://suporte.totvs.com/portal/p/10098/download#detail/1039086) **|** [**12.1.2210**](https://suporte.totvs.com/portal/p/10098/download#detail/1080339)

***OBS.:*** Sempre aplicar pacotes primeiramente em ambiente de homologação com backup prévio do RPO.

Acesse e conheça também a página com todas as Atualizações do Protheus. [Clique aqui e acesse](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596#OINF0011.2-Atualiza%C3%A7%C3%B5esProtheus-Modulos).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)
