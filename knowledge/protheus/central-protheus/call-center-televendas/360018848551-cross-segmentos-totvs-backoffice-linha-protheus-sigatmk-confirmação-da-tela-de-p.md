---
article_id: 360018848551
category: Call Center - Televendas
content_hash: e5479864f6d807651b8fbdbde88d575170677df53d4396eba59217f0c32a8794
fetched_at: '2026-06-28T22:41:30.326844+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Confirmação da tela
  de pagamento do Call Center
type: support-article
updated_at: '2022-09-16T13:15:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018848551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Confirma%C3%A7%C3%A3o-da-tela-de-pagamento-do-Call-Center
---

**Dúvida**

Qual a necessidade de clicar 2 vezes no botão ok na tela de condição de pagamento do televendas?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - desde as versões anteriores a 11.  
  
**Solução**

O primeiro clique no botão ok, válida a condição escolhida, quando esta não possui 3 dígitos, exemplo:

Condição 01 -  CH

Condição 001- BOL

Se digitar 01, o sistema não faz o refresh no campo de parcelas, ao clicar no botão ok, o sistema lê a condição escolhida e efetua a atualização das parcelas.

O 2º ok é para sair da tela com a condição escolhida confirmada.

OBS: O duplo clique pode ser inibido através do parâmetro: **[MV\_TMKTCPG](https://www.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/sigatmk_t.htm)**

Ponto de entrada para tratar essa rotina na chamada da tela de condição de pagamento:

[**TMKCPG - Condição de pagamento**](http://tdn.totvs.com/pages/releaseview.action?pageId=6787781) :

P.E. executado antes da abertura da tela de pagamento para que se possa mudar a variável lHabilAux
