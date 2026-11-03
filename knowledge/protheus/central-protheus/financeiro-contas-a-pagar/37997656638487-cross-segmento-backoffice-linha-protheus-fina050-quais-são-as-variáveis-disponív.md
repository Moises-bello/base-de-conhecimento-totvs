---
article_id: 37997656638487
category: Financeiro - Contas a Pagar
content_hash: 207b9336cd877e956a9cd25aab380abcf34892267010b0a0f79b5a7d2ee40d9c
fetched_at: '2026-06-28T22:38:06.906890+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA050 - Quais são as variáveis
  disponíveis para LP 511
type: support-article
updated_at: '2026-01-29T12:20:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37997656638487-Cross-Segmento-Backoffice-Linha-Protheus-FINA050-Quais-s%C3%A3o-as-vari%C3%A1veis-dispon%C3%ADveis-para-LP-511
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37997656626839) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Quais são as variáveis disponíveis para LP 511?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
A seguir, o passo a passo para o modelo de lançamento padrão para a LP 511.

Utilizando somente uma partida dobrada:

| Tipo de Lançamento | 3 (partida dobrada) |
| --- | --- |
| Conta Débito | DEBITO |
| Conta Crédito | CREDITO |
| Valor do Lançamento | VALOR |
| Histórico | HISTORICO |
|

Utilizando 1 débito e 1 crédito:

| Tipo de Lançamento | 1 (débito) | 2 (crédito) |
| --- | --- | --- |
| Conta Débito | DEBITO |  |
| Conta Crédito |  | CREDITO |
| Valor do Lançamento | VALOR | VALOR |
| Histórico | HISTORICO | HISTORICO |
|

Utilizando mais que 2 sequências para Rateio Bruto:

| Tipo de Lançamento | 1 (débito) | 2 (crédito) | 2 (crédito) |
| --- | --- | --- | --- |
| Conta Débito | DEBITO |  |  |
| Conta Crédito |  | CREDITO | Conta do Plano de Contas |
| Valor do Lançamento | VALOR | SE2->E2\_SALDO | SE2->E2\_IRRF |
| Histórico | HISTORICO | "Lançamento Rateio" | "Lançamento IR" |
|

Variáveis disponíveis para a montagem do LP 511

| VALOR | Valor rateado |
| --- | --- |
| HISTORICO | Histórico informado na tela de rateio |
| DEBITO | Conta a débito informada na tela de rateio |
| CREDITO | Conta a crédito informada na tela de rateio |
| CUSTOD | Centro de custo a débito informado na tela de rateio |
| CUSTOC | Centro de custo a crédito informado na tela de rateio |
| ITEMD | Item contábil a débito informado na tela de rateio |
| ITEMC | Item contábil a crédito informado na tela de rateio |
| CLVLD | Classe de Valor a débito informado na tela de rateio |
| CLVLC | Classe de Valor a crédito informado na tela de rateio |
| VALOR2 | Valor do IRRF rateado |
| VALOR3 | Valor do INSS rateado |
| VALOR4 | Valor do ISS rateado |
| VALOR5 | Valor do PIS rateado |
| VALOR6 | Valor do COFINS rateado |
| VALOR7 | Valor do CSLL rateado |
| SEST | Valor do SEST rateado |
|

**Saiba mais**

[Como montar o LP](https://tdn.totvs.com/pages/releaseview.action?pageId=397379594)
