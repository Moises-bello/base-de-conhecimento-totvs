---
article_id: 360020205191
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: c8d14442df312dd7be4b309834fe1b7851a127b38cb864690c235d8cc1f3958d
fetched_at: '2026-06-28T22:40:32.630022+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: MP - SIGACTB Qual o comportamento do campo CTK_TPSALD  para lançamento gerado
  como Pré lançamento
type: support-article
updated_at: '2021-04-28T22:11:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020205191-MP-SIGACTB-Qual-o-comportamento-do-campo-CTK-TPSALD-para-lan%C3%A7amento-gerado-como-Pr%C3%A9-lan%C3%A7amento
---

**Dúvida**

Qual o comportamento do campo CTK\_TPSALD  para lançamento gerado como Pré lançamento

**Ambiente**  
Protheus – Contabilidade Gerencial  – A partir da versão 11.80  
  
  
**Solução**

Quando o usuário visualiza o lançamento, no momento da contabilização é apresentada  a tabela  CTK. Neste momento o sistema não faz a validação do Prelan, que será validado somente no momento da gravação da CT2.

Sendo assim independente do saldo do lançamento o campo CTK\_TPSALD terá sempre o saldo 1.

Saiba mais:

* [CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)
