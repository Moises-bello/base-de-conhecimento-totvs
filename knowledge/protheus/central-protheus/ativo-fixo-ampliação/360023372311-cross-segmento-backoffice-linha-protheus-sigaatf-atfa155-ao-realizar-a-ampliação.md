---
article_id: 360023372311
category: Ativo Fixo - Ampliação
content_hash: 2d7488f2637a6429cbd1196cb4c81f48ff037857a11783112e68e96fb0a9c0d0
fetched_at: '2026-06-28T22:41:58.179595+00:00'
product: protheus
section_id: 1500001535321
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA155 - AO REALIZAR
  A AMPLIAÇÃO TAXA DE DEPRECIAÇÃO NÃO É REGISTRADA CORRETAMENTE '
type: support-article
updated_at: '2023-11-20T15:59:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023372311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA155-AO-REALIZAR-A-AMPLIA%C3%87%C3%83O-TAXA-DE-DEPRECIA%C3%87%C3%83O-N%C3%83O-%C3%89-REGISTRADA-CORRETAMENTE
---

**Dúvida**

A realizar Ampliação do bem através da rotina ATFA155 o sistema não está registrando no bem o valor da taxa informada na ampliação

* Ao realizar a ampliação foi informada taxa 10

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021194292)

* No cadastro do bem a taxa de depreciação foi registrar 11,111

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021194532)

**Ambiente**  
Microsiga Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Causa**

Situação ocorre pois parâmetro "Tipo de Vida Útil" foi informada como "Vinculada"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021194852)

Veja o que está descrito na Documentação : <http://tdn.totvs.com/pages/releaseview.action?pageId=6067597>

* Tipo de vida útil : Vinculada: Usa-se como base a taxa de depreciação anual do item tipo 01. Com as movimentações de cálculo de depreciação são geradas taxas de depreciação anual, em que a vida útil do bem termina junto com o item tipo 01. Esta opção calcula a taxa de depreciação do novo item 11 ou da nova incorporação com base na vida útil do bem original.

**Solução**

Para que o sistema registre  no bem a taxa informada na ampliação necessário que o parâmetro "Tipo de Vida Útil" seja  informada como "Própria"

* Tipo de vida útil :Própria: Ao escolher essa opção, deve-se informar em Dados do Bem a opção Incorporação, a taxa de depreciação anual estar na moeda 1 e a moeda de calculo do ativo. Esta taxa é usada para o novo item ou incorporação.

* Ao realizar a ampliação foi informada taxa 10

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021133791)

* No cadastro do bem a taxa de depreciação foi registrar 10

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021195572)

Veja mais : [Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA155 AMPLIAÇÃO DO BEM COM OU SEM AUMENTO DA VIDA UTIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007572691-MP-SIGAATF-AMPLIA%C3%87%C3%83O-DO-BEM-COM-OU-SEM-AUMENTO-DA-VIDA-UTIL?source=search)
