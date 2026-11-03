---
article_id: 360050719274
category: RH - Folha de Pagamento
content_hash: aaa33ff0f492e7c8ef078b8880b294dd2dbd83b8eab04b667a829d4debd29f3f
fetched_at: '2026-06-28T22:44:14.794906+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como Sistema calcula automaticamente desconto de
  DSR falta quando lançada verba de ID 0054-Falta
type: support-article
updated_at: '2025-03-19T17:21:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050719274-RH-Linha-Protheus-GPE-Como-Sistema-calcula-automaticamente-desconto-de-DSR-falta-quando-lan%C3%A7ada-verba-de-ID-0054-Falta
---

#### time.png Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Como Sistema calcula automaticamente desconto de DSR falta quando lançada verba de ID 0054-Falta?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Solução**Quando a folha de pagamento realiza o cálculo de faltas e DSR através da **importação** das horas no módulo **Ponto Eletrônico** (SIGAPON), os lançamentos integrados possuem origem **(E)** e o DSR é calculado automaticamente.

Caso não seja utilizado o módulo do Ponto Eletrônico para cálculo de Faltas e DSR, em folha de pagamento é necessário o **lançamento\importação** tanto da verba de Falta quanto da verba de DSR.

A verba de DSR deve ser do mesmo tipo que a verba de faltas.  
No exemplo abaixo, utilizei a verba de faltas e de DSR sobre faltas como Dias.

**Verba de Desconto DSR - Sem id de cálculo**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30769293672855)

**Verba de Faltas- ID 0054**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30769282997015)**

**Lançamento de 1 dia de falta e 1 dia de DSR em Atualizações > Lançamentos > Por Funcionário**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30769282997399)  
  
**Cálculo da Folha de pagamento**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30769293676439)

**Importante**  
Entende-se que quando o funcionário possui **1 dia de falta**, perde **1 dia de DSR**.  
Se utilizar a configuração de **relacionamento** entre verbas através do campo **Verba DSR** da aba **funcionais,** o **cálculo** realizado pelo Sistema ficará **errado,** como se fosse um cálculo de DSR sobre horas extras, por exemplo.

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)
